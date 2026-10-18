"""Deterministic, original 48 kHz / 24-bit sound effects. Run with --selftest."""

import argparse
import math
from pathlib import Path
import re
import subprocess
import wave

import numpy as np

SR = 48000
OUT = Path(__file__).resolve().parent / "sfx"
NAMES = ("whoosh-short", "whoosh-long", "riser-2s", "riser-4s", "sub-drop",
         "impact-soft", "impact-hard", "pop", "tick", "tick-high", "glitch")
DURATIONS = (.35, 1., 2., 4., 1.2, .65, .8, .06, .015, .015, .15)


def meter(path):
    run = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
                          "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True, check=True)
    summary = run.stderr.rsplit("Summary:", 1)[-1]
    return float(re.search(r"Peak:\s*(-?[\d.]+|-inf)", summary)[1])


def write(path, x):
    path.parent.mkdir(parents=True, exist_ok=True)
    x = np.asarray(x, dtype=np.float32)
    ceiling = -4 if path.stem == "glitch" else -1.5  # crushed steps overshoot between samples
    x *= min(1., 10 ** (ceiling / 20) / max(float(np.max(np.abs(x))), 1e-9))
    samples = np.round(x * 8388607).astype("<i4").view(np.uint8).reshape(-1, 4)[:, :3]
    with wave.open(str(path), "wb") as wav:
        wav.setparams((1, 3, SR, len(x), "NONE", "not compressed"))
        wav.writeframes(samples.tobytes())


def shaped_noise(n, rng, center):
    """Overlap-add moving Gaussian bandpass; bins under 150 Hz are removed."""
    size, hop = 4096, 1024
    frequencies = np.fft.rfftfreq(size, 1 / SR)
    window = np.hanning(size)
    out = np.zeros(n + size)
    norm = np.zeros(n + size)
    noise = rng.standard_normal(n + size)
    for start in range(0, n, hop):
        pos = min(1., (start + size / 2) / n)
        c = center(pos)
        band = np.exp(-.5 * (np.log2(np.maximum(frequencies, 1) / c) / .9) ** 2)
        band[frequencies < 150] = 0
        frame = np.fft.irfft(np.fft.rfft(noise[start:start + size] * window) * band)
        out[start:start + size] += frame * window
        norm[start:start + size] += window ** 2
    return out[:n] / np.maximum(norm[:n], .1)


def render(name):
    assert name in NAMES
    seconds = DURATIONS[NAMES.index(name)]
    n = round(seconds * SR)
    t = np.arange(n) / SR
    u = np.arange(n) / n
    rng = np.random.default_rng(20260927 + NAMES.index(name))
    if name.startswith("whoosh"):
        noise = shaped_noise(n, rng, lambda p: 450 * 2 ** (2.4 * p))
        width = 960
        power = np.pad(noise ** 2, (width // 2, width // 2 - 1), mode="reflect")
        cumulative = np.r_[0, np.cumsum(power)]
        noise /= np.sqrt(np.maximum((cumulative[width:] - cumulative[:-width]) / width, 1e-8))
        # Beta-like envelope has its maximum at 60% of the duration.
        env = np.maximum(u, 1e-8) ** 3 * np.maximum(1 - u, 1e-8) ** 2
        x = noise * env / env.max()
        x[-240:] *= np.linspace(1, 0, 240)
    elif name.startswith("riser"):
        noise = shaped_noise(n, rng, lambda p: 350 * 2 ** (2.8 * p))
        freq = 180 * 2 ** (2.1 * u)
        tone = np.sin(2 * np.pi * np.cumsum(freq) / SR)
        x = (.45 * noise + .35 * tone) * (u ** 2.2)
    elif name == "sub-drop":
        freq = 110 * (35 / 110) ** (u ** .8)
        phase = 2 * np.pi * np.cumsum(freq) / SR
        x = (np.sin(phase) + .35 * np.sin(2 * phase)) * np.exp(-3.5 * u)
        x *= np.minimum(1, t / .004)
        x[-240:] *= np.linspace(1, 0, 240)
    elif name.startswith("impact"):
        hard = name.endswith("hard")
        transient = rng.standard_normal(n) * np.exp(-t / (.008 if hard else .015))
        if not hard:
            transient = np.convolve(transient, np.ones(11) / 11, mode="same")
        phase = 2 * np.pi * (155 * t - 28 * t * t)
        x = (.52 if hard else .22) * transient + (.65 if hard else .45) * np.sin(phase) * np.exp(-t / (.19 if hard else .13))
        x *= np.minimum(1, t / .0015)
        x[-240:] *= np.linspace(1, 0, 240)
    elif name in ("pop", "tick", "tick-high"):
        freq = {"pop": 540, "tick": 1250, "tick-high": 1700}[name]
        x = (np.sin(2 * np.pi * freq * t) + .15 * np.sin(2 * np.pi * 2 * freq * t)) * np.exp(-t / (seconds / 5))
        x *= np.minimum(1, t / .0005)
        x[-min(80, n):] *= np.linspace(1, 0, min(80, n))
    else:
        held = np.repeat(rng.integers(-8, 8, math.ceil(n / 12)), 12)[:n] / 8
        gates = ((u < .19) | ((u > .29) & (u < .55)) | ((u > .68) & (u < .94))).astype(float)
        x = held * gates
        x[:48] *= np.linspace(0, 1, 48)
        x[-240:] *= np.linspace(1, 0, 240)
    return x


def selftest():
    for name, duration in zip(NAMES, DURATIONS):
        x = render(name)
        assert len(x) == round(duration * SR) and np.isfinite(x).all()
        if name.startswith("whoosh"):
            width = 960
            rms = np.array([np.mean(x[i:i + width] ** 2) for i in range(0, len(x) - width, width)])
            peak_fraction = (rms.argmax() + .5) * width / len(x)
            assert abs(peak_fraction - .6) <= .08, (name, peak_fraction)
        if name.startswith("riser"):
            energy = np.array([np.mean(x[i:i + 4800] ** 2) for i in range(0, len(x), 4800)])
            assert energy[-1] == energy.max(), (name, energy)
        path = OUT / (name + ".wav")
        write(path, x)
        assert meter(path) <= -1.0, (name, meter(path))
        with wave.open(str(path)) as wav:
            assert (wav.getframerate(), wav.getsampwidth(), wav.getnframes()) == (SR, 3, round(duration * SR))
    print("SFX selftest passed: 11 lengths, true peaks and riser end-energy")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    if args.selftest:
        selftest()
    else:
        for sound in NAMES:
            write(OUT / (sound + ".wav"), render(sound))
            print(OUT / (sound + ".wav"))

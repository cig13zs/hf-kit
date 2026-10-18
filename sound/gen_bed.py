"""Original loopable music beds; numpy synthesis, ffmpeg EBU R128 normalization."""

import argparse
from pathlib import Path
import re
import subprocess
import wave

import numpy as np

SR = 48000
OUT = Path(__file__).resolve().parent / "beds"
MOODS = ("calm-pad", "wonder-pad", "tension-drone", "hype-pulse", "story-noir",
         "news-tick", "kids-bounce")
TEMPOS = {"calm-pad": 75, "wonder-pad": 80, "tension-drone": 80, "hype-pulse": 120,
          "story-noir": 70, "news-tick": 100, "kids-bounce": 110}


def midi(note):
    return 440 * 2 ** ((note - 69) / 12)


def place(out, sound, start, pan=.5):
    """Wrap an event across the loop seam, preserving its decay."""
    n = len(out)
    indices = (start + np.arange(len(sound))) % n
    out[indices, 0] += sound * np.cos(pan * np.pi / 2)
    out[indices, 1] += sound * np.sin(pan * np.pi / 2)


def render(mood, seconds=32):
    if mood not in MOODS or seconds <= 0:
        raise ValueError("known mood and positive seconds required")
    n = round(seconds * SR)
    t = np.arange(n) / SR
    out = np.zeros((n, 2), dtype=np.float32)
    rng = np.random.default_rng(4701 + MOODS.index(mood))
    # Quantize beat count to loop length so rhythmic events meet the seam.
    beats = max(1, round(seconds * TEMPOS[mood] / 60))
    beat = n / beats

    if mood in ("calm-pad", "wonder-pad", "story-noir", "kids-bounce"):
        # Cozy / calm row: warm maj7/9, low density, soft keys and rolled-off highs.
        # Wonder / awe row: major/Lydian, slow changes, bright sparse upper motif.
        # Mystery row: minor/modal, soft muted plucks and sparse pulse (story-noir).
        # Childlike row: simple I-IV-V major, bouncy toy-key notes at 110 BPM.
        chords = {
            "calm-pad": ((50, 57, 61, 64), (47, 54, 57, 62), (43, 50, 54, 59), (45, 52, 56, 61)),
            "wonder-pad": ((50, 57, 62, 66), (55, 62, 66, 71), (52, 59, 64, 69), (57, 64, 69, 73)),
            "story-noir": ((45, 52, 57, 60), (41, 48, 53, 57), (43, 50, 55, 58), (40, 47, 52, 55)),
            "kids-bounce": ((60, 64, 67), (65, 69, 72), (67, 71, 74), (60, 64, 67)),
        }[mood]
        xfade = min(.08, 1.5 / seconds)
        position = t / seconds * 4
        for j, chord in enumerate(chords):
            distance = np.abs((position - j - .5 + 2) % 4 - 2)
            env = np.clip((.5 + xfade * 4 - distance) / (2 * xfade * 4), 0, 1)
            if mood == "kids-bounce":
                env *= .4
            for voice, note in enumerate(chord):
                f = round(midi(note) * seconds) / seconds  # exact integer cycles at the seam
                phase = 2 * np.pi * f * t
                tone = np.sin(phase) + (.16 if mood == "wonder-pad" else .08) * np.sin(2 * phase)
                if mood == "calm-pad":
                    tone += .025 * np.sin(3 * phase)
                gain = env * (.13 if mood == "calm-pad" else .10)
                pan = (.35, .62, .42, .68)[voice]
                out[:, 0] += (tone * gain * np.cos(pan * np.pi / 2)).astype(np.float32)
                out[:, 1] += (tone * gain * np.sin(pan * np.pi / 2)).astype(np.float32)

    if mood == "tension-drone":
        # Tension / suspense row: low minor pedal, unresolved slow beating, no melody.
        for note, gain, pan in ((38, .22, .4), (45, .12, .6), (50, .07, .48)):
            f = round(midi(note) * seconds) / seconds
            modulation = 1 + .18 * np.sin(2 * np.pi * 3 * t / seconds)
            tone = gain * modulation * (np.sin(2 * np.pi * f * t) + .16 * np.sin(4 * np.pi * f * t))
            out[:, 0] += (tone * np.cos(pan * np.pi / 2)).astype(np.float32)
            out[:, 1] += (tone * np.sin(pan * np.pi / 2)).astype(np.float32)

    if mood == "wonder-pad":
        for j, note in enumerate((74, 78, 81, 78)):
            d = np.arange(round(.55 * SR)) / SR
            f = midi(note)
            bell = .032 * (np.sin(2 * np.pi * f * d) + .1 * np.sin(4 * np.pi * f * d)) * np.exp(-d * 7)
            place(out, bell, round((j + .5) * n / 4), .4 if j % 2 else .6)

    if mood in ("hype-pulse", "story-noir", "news-tick", "kids-bounce"):
        # Hype / energetic row: 120 BPM four-on-floor kick and off-beat pulse.
        # Urgent / news row: ticking hats and light modal bass (100 BPM adaptation).
        # Mystery row: 70 BPM restrained minor pulse and muted plucks.
        # Childlike row: 110 BPM bouncy, short major-register toy notes.
        for b in range(beats):
            start = round(b * beat)
            if mood == "hype-pulse":
                d = np.arange(round(.23 * SR)) / SR
                freq = 105 * np.exp(-d * 12) + 47
                kick = .36 * np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-d * 19)
                place(out, kick, start)
                pulse = .13 * np.sin(2 * np.pi * 165 * d) * np.exp(-d * 20)
                place(out, pulse, round(start + beat / 2), .55)
            elif mood == "story-noir":
                d = np.arange(round(.25 * SR)) / SR
                pluck = .09 * (np.sin(2 * np.pi * midi((57, 53, 55, 52)[b % 4]) * d)
                               + .12 * np.sin(4 * np.pi * midi((57, 53, 55, 52)[b % 4]) * d)) * np.exp(-d * 13)
                place(out, pluck, start, .4 if b % 2 else .6)
            elif mood == "news-tick":
                d = np.arange(round(.055 * SR)) / SR
                hat = .025 * rng.standard_normal(len(d)) * np.exp(-d * 80)
                place(out, hat, start, .44)
                place(out, hat * .6, round(start + beat / 2), .58)
            else:
                d = np.arange(round(.22 * SR)) / SR
                note = (72, 76, 79, 76, 77, 81, 79, 74)[b % 8]
                f = midi(note)
                toy = .09 * (np.sin(2 * np.pi * f * d) + .2 * np.sin(2 * np.pi * 3.93 * f * d)) * np.exp(-d * 17)
                place(out, toy, start, .4 if b % 2 else .6)
        if mood == "news-tick":
            for b in range(0, beats, 2):
                d = np.arange(round(.34 * SR)) / SR
                bass = .16 * np.sin(2 * np.pi * midi((45, 43, 41, 43)[(b // 2) % 4]) * d) * np.exp(-d * 7)
                place(out, bass, round(b * beat))
            f = round(midi(45) * seconds) / seconds
            out += (.045 * np.sin(2 * np.pi * f * t))[:, None].astype(np.float32)

    return out


def ebur(path):
    run = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
                          "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True, check=True)
    tail = run.stderr.rsplit("Summary:", 1)[-1]
    return (float(re.search(r"I:\s*(-?[\d.]+)", tail)[1]),
            float(re.search(r"Peak:\s*(-?[\d.]+|-inf)", tail)[1]))


def write(path, audio):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = audio.astype("<f4").tobytes()
    run = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR),
                          "-ac", "2", "-i", "pipe:0", "-af", "ebur128=peak=true", "-f", "null", "-"],
                         input=raw, capture_output=True, check=True)
    tail = run.stderr.decode(errors="replace").rsplit("Summary:", 1)[-1]
    measured = float(re.search(r"I:\s*(-?[\d.]+)", tail)[1])
    peak = float(re.search(r"Peak:\s*(-?[\d.]+|-inf)", tail)[1])
    gain_db = min(-20 - measured, -1.2 - peak)
    samples = np.round(np.clip(audio * 10 ** (gain_db / 20), -.999999, .999999) * 8388607).astype("<i4")
    pcm = samples.view(np.uint8).reshape(-1, 4)[:, :3]
    with wave.open(str(path), "wb") as wav:
        wav.setparams((2, 3, SR, len(audio), "NONE", "not compressed"))
        wav.writeframes(pcm.tobytes())


def selftest():
    for mood in MOODS:
        x = render(mood, 32)
        assert len(x) == 32 * SR and np.isfinite(x).all()
        seam = float(np.max(np.abs(x[0] - x[-1])))
        assert seam < .07, (mood, seam)
        path = OUT / (mood + ".wav")
        write(path, x)
        loudness, peak = ebur(path)
        assert abs(loudness + 20) <= 1 and peak <= -1, (mood, loudness, peak)
        with wave.open(str(path)) as wav:
            assert (wav.getframerate(), wav.getsampwidth(), wav.getnframes()) == (SR, 3, 32 * SR)
    print("Bed selftest passed: 7 lengths, seams, loudness and true peaks")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--mood", choices=MOODS)
    p.add_argument("--seconds", type=float, default=32)
    p.add_argument("--out", type=Path)
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    if args.selftest:
        selftest()
    elif args.mood:
        target = args.out or OUT / (args.mood + ".wav")
        write(target, render(args.mood, args.seconds))
        print(target)
    else:
        for mood in MOODS:
            path = OUT / (mood + ".wav")
            write(path, render(mood))
            print(path)

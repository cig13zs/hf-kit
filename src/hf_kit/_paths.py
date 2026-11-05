"""Locate a local hf-kit checkout (blocks/styles/research live there)."""
from __future__ import annotations

import os
from pathlib import Path


def find_kit_root() -> Path:
    env = os.environ.get("HF_KIT_ROOT")
    if env:
        path = Path(env).expanduser().resolve()
        if not (path / "blocks").is_dir():
            raise FileNotFoundError(
                f"HF_KIT_ROOT={path} has no blocks/ directory"
            )
        return path

    here = Path(__file__).resolve()
    candidates = [
        here.parents[2],  # repo root when editable (src/hf_kit/_paths.py)
        Path.cwd(),
        Path.home() / "hf-kit",
    ]
    for candidate in candidates:
        if (candidate / "blocks").is_dir() and (candidate / "styles").is_dir():
            return candidate.resolve()
    raise FileNotFoundError(
        "hf-kit data not found (need blocks/ and styles/). "
        "Clone https://github.com/cig13zs/hf-kit or set HF_KIT_ROOT."
    )

"""Download Epoch AI notable models snapshot."""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw" / "deep" / "epoch"
OUT.mkdir(parents=True, exist_ok=True)
URL = "https://epoch.ai/data/notable_ai_models.csv"


def main(force: bool = False) -> None:
    today = date.today().isoformat()
    path = OUT / f"notable_ai_models_{today}.csv"
    latest = OUT / "notable_ai_models_latest.csv"
    if latest.exists() and not force:
        print("exists", latest)
        return
    r = requests.get(URL, timeout=120)
    r.raise_for_status()
    path.write_bytes(r.content)
    latest.write_bytes(r.content)
    man = {
        "source": "Epoch AI",
        "url": URL,
        "download_date": today,
        "n_bytes": len(r.content),
        "sha256": hashlib.sha256(r.content).hexdigest(),
        "snapshot_file": path.name,
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print("wrote", path, len(r.content))


if __name__ == "__main__":
    import sys

    main(force="--force" in sys.argv)

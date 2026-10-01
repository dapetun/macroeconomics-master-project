"""Загрузка Penn World Table (open-numbers). / Download Penn World Table (open-numbers)."""
from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep.paths import COUNTRIES as COUNTRIES_ISO3, ROOT  # noqa: E402

OUT = ROOT / "data" / "raw" / "deep" / "pwt"
OUT.mkdir(parents=True, exist_ok=True)

BASE = "https://raw.githubusercontent.com/open-numbers/ddf--pwt--penn_world_table/master/"
VARS = ["rtfpna", "ctfp", "rgdpna", "rnna", "emp", "hc", "labsh", "pop"]
COUNTRIES = {c.lower() for c in COUNTRIES_ISO3}


def fetch(var: str) -> pd.DataFrame:
    url = f"{BASE}ddf--datapoints--{var}--by--country--year.csv"
    last = None
    for i in range(3):
        try:
            r = requests.get(url, timeout=90)
            r.raise_for_status()
            df = pd.read_csv(pd.io.common.StringIO(r.text))
            df = df.rename(columns={"country": "country_iso3", var: "value"})
            df["country_iso3"] = df["country_iso3"].str.upper()
            df["var"] = var
            df["source_url"] = url
            return df[(df["year"] >= 2000) & (df["country_iso3"].str.lower().isin(COUNTRIES))]
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(last)


def main(force: bool = False) -> None:
    target = OUT / "pwt_long.csv"
    if target.exists() and not force:
        print("exists", target)
        return
    frames = []
    for v in VARS:
        print("fetch", v)
        frames.append(fetch(v))
        time.sleep(0.3)
    df = pd.concat(frames, ignore_index=True)
    df = df[["country_iso3", "year", "var", "value"]].drop_duplicates(
        ["country_iso3", "year", "var"]
    )
    df.to_csv(target, index=False)
    man = {
        "source": "open-numbers PWT mirror",
        "base_url": BASE,
        "download_date": str(date.today()),
        "n_rows": int(len(df)),
        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "variables": VARS,
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print("wrote", target, len(df))


if __name__ == "__main__":
    import sys

    main(force="--force" in sys.argv)

#!/usr/bin/env python3
"""Download PWT data from open-numbers GitHub mirror (lowercase ISO3)."""

import requests
import pandas as pd
import io
from pathlib import Path
import time

BASE = "https://raw.githubusercontent.com/open-numbers/ddf--pwt--penn_world_table/master"
COUNTRIES = ["usa", "chn", "kor", "jpn", "deu", "gbr", "isr", "fra"]

# PWT variables needed
VARIABLES = {
    "rgdpe": "Real GDP expenditure-side (M 2017 USD)",
    "rgdpo": "Real GDP output-side (M 2017 USD)",
    "labsh": "Share of labour in GDP",
    "hc": "Human capital index",
    "emp": "Employment (millions)",
    "pop": "Population (millions)",
    "rnna": "Capital stock at constant 2017 USD (M)",
    "tfp": "TFP at constant national prices",
    "ctfp": "TFP at constant PPPs",
}

raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

for var, label in VARIABLES.items():
    fname = f"ddf--datapoints--{var}--by--country--year.csv"
    url = f"{BASE}/{fname}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            df = pd.read_csv(io.StringIO(r.text))
            df = df[df["country"].isin(COUNTRIES)]
            df = df.rename(columns={"country": "country_iso3"})
            # Uppercase ISO3
            df["country_iso3"] = df["country_iso3"].str.upper()
            df = df.sort_values(["country_iso3", "year"]).reset_index(drop=True)
            
            if len(df) > 0:
                fpath = raw_dir / f"pwt_{var}.csv"
                df.to_csv(fpath, index=False)
                print(f"[OK] {var}: {len(df)} rows, {sorted(df['country_iso3'].unique())}, {df['year'].min()}-{df['year'].max()}")
            else:
                print(f"[EMPTY] {var}: no matching countries")
        else:
            print(f"[FAIL] {var}: HTTP {r.status_code}")
    except Exception as e:
        print(f"[ERROR] {var}: {e}")
    time.sleep(0.5)

print("\nDone!")

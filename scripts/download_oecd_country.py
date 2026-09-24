#!/usr/bin/env python3
"""Download OECD MSTI BERD and other indicators country-by-country.
OECD SDMX doesn't support semicolons or wildcards on REF_AREA."""

import requests
import pandas as pd
import io
from pathlib import Path
import time

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0"
}

BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"
COUNTRIES = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]

# Map: (measure, unit_measure) -> variable name
# From probe_oecd_measures.py results:
# B + PT_B1GQ = BERD as % of GDP
# G_FA + PT_B1GQ = GERD as % of GDP (for comparison with WB)
# B_SERV + USD_PPP = BERD in USD PPP constant
# B_RS + PS = BERD per researcher
INDICATORS = {
    "berd_pct_gdp": {"measure": "B", "unit": "PT_B1GQ", "label": "BERD % of GDP"},
    "berd_usd_ppp": {"measure": "B_SERV", "unit": "USD_PPP", "label": "BERD USD PPP"},
    "gerd_usd_ppp": {"measure": "G", "unit": "USD_PPP", "label": "GERD USD PPP"},
}

raw_dir = Path("data/raw")

for ind_key, cfg in INDICATORS.items():
    print(f"\n=== {cfg['label']} ===")
    all_frames = []
    
    for country in COUNTRIES:
        key = f"{country}.A.{cfg['measure']}.{cfg['unit']}._Z._Z"
        url = f"{BASE}/{key}"
        params = {
            "startPeriod": "2000",
            "endPeriod": "2024",
            "dimensionAtObservation": "AllDimensions"
        }
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=30)
            if r.status_code == 200 and len(r.content) > 500:
                df = pd.read_csv(io.StringIO(r.text))
                # Extract just the key columns
                if "TIME_PERIOD" in df.columns and "OBS_VALUE" in df.columns:
                    sub = df[["REF_AREA", "TIME_PERIOD", "OBS_VALUE"]].copy()
                    sub.columns = ["country_iso3", "year", "value"]
                    sub["value"] = pd.to_numeric(sub["value"], errors="coerce")
                    all_frames.append(sub)
                    print(f"  {country}: {len(sub)} rows")
                else:
                    print(f"  {country}: no TIME_PERIOD/OBS_VALUE columns")
            else:
                print(f"  {country}: HTTP {r.status_code} ({len(r.content)} bytes)")
        except Exception as e:
            print(f"  {country}: ERROR {e}")
        time.sleep(0.3)
    
    if all_frames:
        combined = pd.concat(all_frames, ignore_index=True)
        combined = combined.drop_duplicates(subset=["country_iso3", "year"])
        combined = combined.sort_values(["country_iso3", "year"]).reset_index(drop=True)
        
        fpath = raw_dir / f"oecd_{ind_key}.csv"
        combined.to_csv(fpath, index=False)
        print(f"  -> Saved {len(combined)} rows to {fpath}")
        print(f"  -> Countries: {sorted(combined['country_iso3'].unique())}")
        years = sorted(combined['year'].unique())
        print(f"  -> Years: {years[0]}-{years[-1]}")
    else:
        print(f"  -> NO DATA collected for {ind_key}")

print("\nDone!")

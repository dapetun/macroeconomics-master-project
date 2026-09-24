#!/usr/bin/env python3
"""Extract all unique MEASURE codes from OECD MSTI wildcard query."""

import requests
import pandas as pd
import io
from pathlib import Path

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0"
}

BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"

# Get all data for USA only, recent years
key = "USA.A....."
params = {
    "startPeriod": "2020",
    "endPeriod": "2024",
    "dimensionAtObservation": "AllDimensions"
}

print("Downloading OECD MSTI data for USA (2020-2024)...")
try:
    r = requests.get(BASE + "/" + key, params=params, headers=HEADERS, timeout=60)
    print(f"HTTP {r.status_code}, size={len(r.content):,}")
    
    if r.status_code == 200 and len(r.content) > 500:
        df = pd.read_csv(io.StringIO(r.text))
        print(f"\nAll columns: {list(df.columns)}")
        print(f"Total rows: {len(df)}")
        
        # Show unique MEASURE values
        if "MEASURE" in df.columns:
            measures = df["MEASURE"].unique()
            print(f"\nUnique MEASURE values ({len(measures)}):")
            for m in sorted(measures):
                # Get sample UNIT_MEASURE for each
                sample = df[df["MEASURE"] == m]["UNIT_MEASURE"].iloc[0] if len(df[df["MEASURE"] == m]) > 0 else "?"
                obs_count = len(df[df["MEASURE"] == m])
                print(f"  {m}: UNIT_MEASURE={sample}, obs={obs_count}")
        
        # Show unique UNIT_MEASURE values
        if "UNIT_MEASURE" in df.columns:
            units = df["UNIT_MEASURE"].unique()
            print(f"\nUnique UNIT_MEASURE values ({len(units)}):")
            for u in sorted(units):
                print(f"  {u}")
        
        # Save raw
        df.to_csv("data/raw/oecd_msti_usa_debug.csv", index=False)
        print("\nSaved raw data to data/raw/oecd_msti_usa_debug.csv")
        
except Exception as e:
    print(f"ERROR: {e}")

#!/usr/bin/env python3
"""Download OECD MSTI - use wildcards since semicolons don't work."""

import requests
import pandas as pd
import io
from pathlib import Path

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0"
}

BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"

# Try different key formats
test_keys = [
    # Full wildcard
    "*.A.G_FA.PT_B1GQ._Z._Z",
    # Single country
    "USA.A.G_FA.PT_B1GQ._Z._Z",
    # Without underscores for null dimensions
    "*.A.G_FA.PT_B1GQ..",
    # Maybe price_base and transformation are different
    "*.A.G_FA.PT_B1GQ.*.*",
    # Maybe just 3 dimensions needed
    "*.A.G_FA.PT_B1GQ",
]

for key in test_keys:
    url = f"{BASE}/{key}"
    params = {"startPeriod": "2020", "endPeriod": "2024", "dimensionAtObservation": "AllDimensions"}
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=30)
        print(f"Key={key}: HTTP {r.status_code}, size={len(r.content):,}")
        if r.status_code == 200 and len(r.content) > 200:
            df = pd.read_csv(io.StringIO(r.text))
            print(f"  -> {len(df)} rows, countries: {sorted(df['REF_AREA'].unique()) if 'REF_AREA' in df.columns else 'N/A'}")
            break
    except Exception as e:
        print(f"Key={key}: ERROR {e}")

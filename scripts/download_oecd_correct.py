#!/usr/bin/env python3
"""Download OECD MSTI indicators with correct measure codes."""

import requests
import pandas as pd
import io
import json
from pathlib import Path
from datetime import datetime

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0"
}

BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"
COUNTRIES = "USA;CHN;KOR;JPN;DEU;GBR;ISR;FRA"

# From probe: key is REF_AREA.FREQ.MEASURE.UNIT_MEASURE.PRICE_BASE.TRANSFORMATION
# Use wildcards for unknown dimensions
INDICATORS = {
    "gerd_pct_gdp": {
        "key": f"{COUNTRIES}.A.G_FA.PT_B1GQ._Z._Z",
        "label": "GERD as % of GDP",
        "raw_file": "oecd_msti_gerd_pct_gdp.csv",
    },
    "berd_pct_gdp": {
        "key": f"{COUNTRIES}.A.B.PT_B1GQ._Z._Z",
        "label": "BERD as % of GDP",
        "raw_file": "oecd_msti_berd_pct_gdp.csv",
    },
    "gerd_usd_ppp": {
        "key": f"{COUNTRIES}.A.G.USD_PPP._Z._Z",
        "label": "GERD in USD PPP",
        "raw_file": "oecd_msti_gerd_usd_ppp.csv",
    },
    "berd_usd_ppp": {
        "key": f"{COUNTRIES}.A.B_SERV.USD_PPP._Z._Z",
        "label": "BERD in USD PPP (by sector)",
        "raw_file": "oecd_msti_berd_usd_ppp.csv",
    },
}

raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

results = []

for ind_key, cfg in INDICATORS.items():
    print(f"\nDownloading {cfg['label']}...")
    params = {
        "startPeriod": "2000",
        "endPeriod": "2024",
        "dimensionAtObservation": "AllDimensions"
    }
    try:
        r = requests.get(BASE + "/" + cfg["key"], params=params, headers=HEADERS, timeout=60)
        print(f"  HTTP {r.status_code}, size={len(r.content):,}")
        
        if r.status_code == 200 and len(r.content) > 500:
            df = pd.read_csv(io.StringIO(r.text))
            print(f"  Rows: {len(df)}, Columns: {list(df.columns)}")
            
            # Show unique countries
            if "REF_AREA" in df.columns:
                countries = sorted(df["REF_AREA"].unique())
                print(f"  Countries ({len(countries)}): {countries}")
            
            if "OBS_VALUE" in df.columns:
                vals = pd.to_numeric(df["OBS_VALUE"], errors="coerce")
                print(f"  OBS_VALUE range: {vals.min():.4f} to {vals.max():.4f}")
                print(f"  Non-null values: {vals.notna().sum()}/{len(vals)}")
            
            if "TIME_PERIOD" in df.columns:
                years = sorted(df["TIME_PERIOD"].dropna().unique())
                print(f"  Years: {years[0]}-{years[-1]} ({len(years)} years)")
            
            # Save
            fpath = raw_dir / cfg["raw_file"]
            df.to_csv(fpath, index=False)
            print(f"  Saved to {fpath}")
            
            results.append({
                "indicator": ind_key,
                "label": cfg["label"],
                "status": "OK",
                "http_code": r.status_code,
                "rows": len(df),
                "countries": len(countries) if "REF_AREA" in df.columns else 0,
                "year_range": f"{years[0]}-{years[-1]}" if "TIME_PERIOD" in df.columns and len(years) > 0 else "N/A",
            })
        elif r.status_code == 200:
            print(f"  Empty response (size={len(r.content)})")
            results.append({"indicator": ind_key, "status": "EMPTY", "http_code": r.status_code})
        else:
            print(f"  Error: {r.text[:200]}")
            results.append({"indicator": ind_key, "status": "FAIL", "http_code": r.status_code, "error": r.text[:100]})
    except Exception as e:
        print(f"  ERROR: {e}")
        results.append({"indicator": ind_key, "status": "ERROR", "error": str(e)})

print("\n" + "="*60)
print("RESULTS SUMMARY:")
for r in results:
    status = r.get("status", "?")
    ind = r.get("indicator", "?")
    label = r.get("label", "")
    rows = r.get("rows", "")
    countries = r.get("countries", "")
    years = r.get("year_range", "")
    print(f"  [{status}] {ind} ({label}): {rows} rows, {countries} countries, {years}")

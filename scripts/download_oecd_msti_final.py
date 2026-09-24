#!/usr/bin/env python3
"""Download OECD MSTI with correct 6-dimension key format."""

import requests
import pandas as pd
import io
import time
from pathlib import Path

RAW_DIR = Path("data/raw")
COUNTRIES_OECD = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0"
}

BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"


def download_msti_indicator(measure_code, var_name, description):
    """Download one MSTI indicator for all target countries."""
    print(f"\n--- {var_name} ({measure_code}) ---")
    
    # From the wildcard probe, dimensions are:
    # REF_AREA.FREQ.MEASURE.UNIT_MEASURE.PRICE_BASE.TRANSFORMATION
    # FREQ=A (annual), UNIT_MEASURE=PT_B1GQ (% of GDP)
    # PRICE_BASE=_Z, TRANSFORMATION=_Z (for most indicators)
    
    countries = "+".join(COUNTRIES_OECD)
    key = f"{countries}.A.{measure_code}.PT_B1GQ._Z._Z"
    
    params = {
        "startPeriod": "2000",
        "endPeriod": "2024",
        "dimensionAtObservation": "AllDimensions"
    }
    
    try:
        r = requests.get(BASE + "/" + key, params=params, headers=HEADERS, timeout=60)
        print(f"  HTTP {r.status_code}, size={len(r.content):,}")
        
        if r.status_code == 200 and len(r.content) > 500:
            # Parse CSV
            df = pd.read_csv(io.StringIO(r.text))
            print(f"  Columns: {list(df.columns)}")
            print(f"  Rows: {len(df)}")
            
            # Filter to only OBS_VALUE rows
            if "OBS_VALUE" in df.columns and "REF_AREA" in df.columns:
                result = df[["REF_AREA", "TIME_PERIOD", "OBS_VALUE"]].copy()
                result.columns = ["country_iso3", "year", "value"]
                result = result.dropna(subset=["value"])
                
                outfile = RAW_DIR / f"{var_name}.csv"
                result.to_csv(outfile, index=False)
                print(f"  [OK] {len(result)} obs saved to {outfile}")
                print(f"  Countries: {sorted(result['country_iso3'].unique())}")
                return True
            else:
                print(f"  Missing expected columns")
                # Save raw anyway
                outfile = RAW_DIR / f"{var_name}_raw.csv"
                df.to_csv(outfile, index=False)
                return False
        else:
            print(f"  Response: {r.text[:300]}")
            return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def download_msti_berd_industry():
    """Download BERD by industry (P_BERPCT is BERD as % of GDP)."""
    # Also try: P_GERPCT = GERD by sector, P_BERPCT = BERD
    indicators = {
        "gerd_pct_gdp": "P_GERPCT",   # or try P_TOTPT (GERD total)
        "berd_pct_gdp": "P_BERPCT",
    }
    
    results = {}
    for var, measure in indicators.items():
        results[var] = download_msti_indicator(measure, var, f"{measure} as % of GDP")
        time.sleep(2)
    
    return results


if __name__ == "__main__":
    print("=== OECD MSTI Final Download ===")
    
    results = download_msti_berd_industry()
    
    # Also try alternative GERD measures if first failed
    if not results.get("gerd_pct_gdp"):
        print("\n--- Trying alternative GERD measures ---")
        alt_measures = ["P_TOTPT", "P_TOTPCT", "A"]
        for m in alt_measures:
            print(f"\nTrying measure={m} for GERD...")
            ok = download_msti_indicator(m, "gerd_pct_gdp_alt", f"GERD alt ({m})")
            if ok:
                break
            time.sleep(2)
    
    print("\n" + "=" * 60)
    for var, ok in results.items():
        print(f"  {var}: {'OK' if ok else 'FAILED'}")

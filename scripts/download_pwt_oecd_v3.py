#!/usr/bin/env python3
"""Download PWT 11.0 from Dataverse.nl and OECD MSTI with corrected SDMX params."""

import requests
import pandas as pd
import json
import time
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("data/raw")
META_DIR = Path("data/metadata")
COUNTRIES = ["USA", "CHN", "TWN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]


def download_pwt110():
    """Download PWT 11.0 Excel from dataverse.nl."""
    print("=== PWT 11.0 from dataverse.nl ===")
    
    urls = [
        ("https://dataverse.nl/api/access/datafile/554105", "pwt110.xlsx"),
        ("https://dataverse.nl/api/access/datafile/554030", "pwt110.dta"),
    ]
    
    for url, filename in urls:
        try:
            print(f"  Trying {filename}...")
            r = requests.get(url, timeout=120, allow_redirects=True,
                           headers={"User-Agent": "Mozilla/5.0"})
            print(f"    HTTP {r.status_code}, size={len(r.content):,} bytes, "
                  f"ctype={r.headers.get('Content-Type', 'unknown')}")
            
            if r.status_code == 200 and len(r.content) > 50000:
                outfile = RAW_DIR / filename
                with open(outfile, "wb") as f:
                    f.write(r.content)
                print(f"    [OK] Saved {filename} ({len(r.content):,} bytes)")
                
                # Try to load and extract variables
                if filename.endswith(".xlsx"):
                    try:
                        df = pd.read_excel(outfile, sheet_name="Data", nrows=5)
                        print(f"    Columns: {list(df.columns[:20])}")
                        print(f"    Shape hint: {df.shape}")
                    except Exception as e:
                        print(f"    Excel preview error: {e}")
                
                return True
            else:
                print(f"    [FAIL] Too small or HTTP error")
        except Exception as e:
            print(f"    ERROR: {e}")
        time.sleep(2)
    
    return False


def download_oecd_msti_fixed():
    """Download OECD MSTI with corrected SDMX params (startPeriod/endPeriod)."""
    print("\n=== OECD MSTI (fixed SDMX) ===")
    
    headers = {
        "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    base = "https://sdmx.oecd.org/public/rest/v1/data"
    flow = "DSD_MSTI@DF_MSTI"
    
    # Measures: A=GERD, B=BERD; Unit: PT_B1GQ=% of GDP
    measures = {"gerd_pct_gdp": "A", "berd_pct_gdp": "B"}
    countries = "USA+CHN+KOR+JPN+DEU+GBR+ISR+FRA"
    
    results = {}
    for var, measure in measures.items():
        print(f"\n  --- {var} ---")
        
        # Build proper SDMX key: MEASURE.COUNTRY.INDUSTRY.UNIT_OF_MEASURE
        key = f"{measure}.{countries}..PT_B1GQ."
        
        url = f"{base}/{flow}/{key}"
        params = {
            "startPeriod": "2000",
            "endPeriod": "2024",
            "dimensionAtObservation": "AllDimensions",
            "detail": "full"
        }
        
        try:
            r = requests.get(url, params=params, headers=headers, timeout=60)
            print(f"    HTTP {r.status_code}, size={len(r.content):,}")
            
            if r.status_code == 200 and len(r.content) > 200:
                outfile = RAW_DIR / f"{var}_oecd_raw.csv"
                with open(outfile, "wb") as f:
                    f.write(r.content)
                print(f"    [OK] Saved to {outfile}")
                
                # Preview
                content = r.text[:500]
                print(f"    Preview: {content[:200]}")
                results[var] = True
            else:
                print(f"    Response: {r.text[:300]}")
                results[var] = False
                
        except Exception as e:
            print(f"    ERROR: {e}")
            results[var] = False
        
        time.sleep(2)
    
    return results


def download_oecd_tiva():
    """Download OECD TiVA GVC data."""
    print("\n=== OECD TiVA (GVC) ===")
    
    headers = {
        "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    base = "https://sdmx.oecd.org/public/rest/v1/data"
    
    # TiVA flow IDs
    flow_ids = ["DSD_TIVA@DF_TIVA", "OECD.TIVA"]
    
    countries = "USA+CHN+KOR+JPN+DEU+GBR+ISR+FRA"
    
    for flow in flow_ids:
        print(f"\n  Trying flow: {flow}")
        # FVAX: foreign value-added share in exports
        url = f"{base}/{flow}/FVAX.{countries}.../T dol_value"
        params = {
            "startPeriod": "2000",
            "endPeriod": "2024",
            "dimensionAtObservation": "AllDimensions",
        }
        try:
            r = requests.get(url, params=params, headers=headers, timeout=60)
            print(f"    HTTP {r.status_code}, size={len(r.content)}")
            if r.status_code == 200 and len(r.content) > 200:
                outfile = RAW_DIR / "tiva_gvc_raw.csv"
                with open(outfile, "wb") as f:
                    f.write(r.content)
                print(f"    [OK] Saved to {outfile}")
                print(f"    Preview: {r.text[:300]}")
                return True
            else:
                print(f"    Response: {r.text[:200]}")
        except Exception as e:
            print(f"    ERROR: {e}")
        time.sleep(2)
    
    return False


if __name__ == "__main__":
    # PWT
    pwt_ok = download_pwt110()
    
    # OECD MSTI
    oecd_results = download_oecd_msti_fixed()
    
    # TiVA
    tiva_ok = download_oecd_tiva()
    
    # Summary
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"PWT 11.0: {'OK' if pwt_ok else 'FAILED'}")
    for var, ok in oecd_results.items():
        print(f"OECD {var}: {'OK' if ok else 'FAILED'}")
    print(f"OECD TiVA: {'OK' if tiva_ok else 'FAILED'}")

#!/usr/bin/env python3
"""Download OECD MSTI data via the new SDMX API and PWT via FRED."""

import requests
import json
from pathlib import Path

RAW_DIR = Path("data/raw")

def download_oecd_msti_sdmx():
    """Download GERD and BERD from OECD SDMX REST API."""
    print("=== OECD MSTI via SDMX ===")
    
    # OECD new SDMX endpoint
    base = "https://sdmx.oecd.org/public/rest/v1/data"
    
    # Data flow: DSD_MSTI@DF_MSTI, flow key
    # Dimension order: measure, country, industry, unit_of_measure, time
    
    headers = {
        "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    # GERD as % of GDP
    # Key: MSTI_ALL measures: A=GERD, B=BERD
    # Country codes in OECD format: USA, CHN, TWN, KOR, JPN, DEU, GBR, ISR, FRA
    
    measures = {
        "GERD": "A",
        "BERD": "B",
    }
    
    countries = "USA+CHN+KOR+JPN+DEU+GBR+ISR+FRA+TWN"
    
    for name, measure_key in measures.items():
        print(f"\n--- {name} ---")
        # Try various flow IDs
        flow_ids = ["DSD_MSTI@DF_MSTI", "MSTI_ALL", "OECD.STI.STP"]
        
        for flow in flow_ids:
            url = f"{base}/{flow}/{measure_key}.{countries}..PT_B1GQ./?startTime=2000&endTime=2024&dimensionAtObservation=AllDimensions"
            try:
                r = requests.get(url, headers=headers, timeout=30)
                print(f"  Flow={flow}: HTTP {r.status_code}, len={len(r.content)}")
                if r.status_code == 200 and len(r.content) > 100:
                    outfile = RAW_DIR / f"oecd_msti_{name.lower()}_raw.csv"
                    with open(outfile, "wb") as f:
                        f.write(r.content)
                    print(f"  [OK] Saved to {outfile}")
                    print(f"  Preview: {r.text[:300]}")
                    break
                else:
                    print(f"  Preview: {r.text[:200]}")
            except Exception as e:
                print(f"  ERROR: {e}")

def download_pwt_from_fred():
    """Download PWT data from FRED (St. Louis Fed)."""
    print("\n=== PWT from FRED ===")
    
    # FRED has PWT data as individual series
    # rgdpe = Expenditure-side real GDP
    # rgdpo = Output-side real GDP
    # labsh = Labour share
    # tfpna = Total factor productivity (NA)
    
    series_map = {
        "pwt_rgdpe": "RGDPNAXDCUSA",  # placeholder
    }
    
    # Try FRED API without key
    base = "https://fred.stlouisfed.org/graph/fredgraph.csv"
    
    # Direct download of a PWT series from FRED
    params = {"id": "RGDPNAXDCUSA"}
    try:
        r = requests.get(base, params=params, timeout=20)
        print(f"  FRED test: HTTP {r.status_code}, len={len(r.content)}")
        if r.status_code == 200:
            print(f"  Preview: {r.text[:200]}")
    except Exception as e:
        print(f"  ERROR: {e}")

def download_pwt_via_web():
    """Try to find PWT download page content."""
    print("\n=== PWT website probes ===")
    
    urls = [
        "https://www.rug.nl/ggdc/productivity/pwt/",
        "https://www.rug.nl/ggdc/productivity/pwt/pwt110.html",
        "https://cid.ucdavis.edu/data/pwt",
    ]
    
    for url in urls:
        try:
            r = requests.get(url, timeout=20, allow_redirects=True,
                           headers={"User-Agent": "Mozilla/5.0"})
            print(f"  {url}")
            print(f"    HTTP {r.status_code}, len={len(r.content)}")
            if r.status_code == 200:
                # Look for download links
                import re
                links = re.findall(r'href=["\']([^"\']*?(?:\.xlsx|\.dta|\.csv)[^"\']*)["\']', r.text)
                print(f"    Download links: {links}")
        except Exception as e:
            print(f"  {url}: ERROR {e}")

if __name__ == "__main__":
    download_oecd_msti_sdmx()
    download_pwt_from_fred()
    download_pwt_via_web()

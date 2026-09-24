#!/usr/bin/env python3
"""Probe OECD SDMX dataflows and DSD structure, and PWT dataverse redirect."""

import requests
import json

HEADERS_SDMX = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0"
}

HEADERS_HTML = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0"
}


def probe_oecd_dataflows():
    """List OECD SDMX dataflows to find correct MSTI flow ID."""
    print("=== OECD SDMX: list dataflows ===")
    url = "https://sdmx.oecd.org/public/rest/v1/dataflow"
    try:
        r = requests.get(url, headers=HEADERS_SDMX, timeout=30)
        print(f"HTTP {r.status_code}, len={len(r.content)}")
        if r.status_code == 200:
            text = r.text
            # Find MSTI-related flows
            for line in text.split("\n"):
                if "MSTI" in line.upper() or "DF_MSTI" in line.upper():
                    print(f"  MATCH: {line[:200]}")
            # Also save first part
            outfile = "data/raw/oecd_dataflows.xml"
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  Saved full dataflows to {outfile}")
    except Exception as e:
        print(f"ERROR: {e}")


def probe_oecd_msti_dsd():
    """Get MSTI DSD structure to find correct key format."""
    print("\n=== OECD SDMX: MSTI DSD structure ===")
    
    # First find the DSD ID from dataflows
    url = "https://sdmx.oecd.org/public/rest/v1/dataflow/OECD/DF_MSTI?references=children"
    try:
        r = requests.get(url, headers=HEADERS_SDMX, timeout=30)
        print(f"DF_MSTI: HTTP {r.status_code}")
        if r.status_code == 200:
            print(r.text[:1000])
    except Exception as e:
        print(f"ERROR: {e}")
    
    # Try to get MSTI data with 6 dimensions
    # Dimensions might be: MEASURE.COUNTRY.INDUSTRY.UNIT_OF_MEASURE.FREQ.SECTOR
    url2 = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"
    key = "A.USA......PT_B1GQ."
    params = {
        "startPeriod": "2000",
        "endPeriod": "2024",
        "dimensionAtObservation": "AllDimensions"
    }
    try:
        r = requests.get(url2, params=params, headers=HEADERS_SDMX, timeout=30)
        print(f"\n6-dim key test: HTTP {r.status_code}, len={len(r.content)}")
        print(f"  Response: {r.text[:300]}")
    except Exception as e:
        print(f"ERROR: {e}")
    
    # Try with wildcards for unknown dims
    url3 = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"
    key3 = "A.USA*"
    params3 = {
        "startPeriod": "2020",
        "endPeriod": "2023",
        "dimensionAtObservation": "AllDimensions"
    }
    try:
        r = requests.get(url3, params=params3, headers=HEADERS_SDMX, timeout=30)
        print(f"\nWildcard test: HTTP {r.status_code}, len={len(r.content)}")
        if r.status_code == 200 and len(r.content) > 200:
            print(f"  Preview: {r.text[:500]}")
    except Exception as e:
        print(f"ERROR: {e}")


def probe_pwt_redirect():
    """Follow PWT dataverse redirects to find actual download."""
    print("\n=== PWT dataverse redirect probe ===")
    
    url = "https://dataverse.nl/api/access/datafile/554105"
    try:
        r = requests.get(url, timeout=30, allow_redirects=False,
                        headers={"User-Agent": "Mozilla/5.0"})
        print(f"  Status: {r.status_code}")
        print(f"  Location: {r.headers.get('Location', 'N/A')}")
        print(f"  Headers: {dict(r.headers)}")
    except Exception as e:
        print(f"ERROR: {e}")
    
    # Try dataverse API with format
    url2 = "https://dataverse.nl/api/access/datafile/554105?format=original"
    try:
        r = requests.get(url2, timeout=30, allow_redirects=False,
                        headers={"User-Agent": "Mozilla/5.0"})
        print(f"\n  With format param: HTTP {r.status_code}")
        print(f"  Location: {r.headers.get('Location', 'N/A')}")
    except Exception as e:
        print(f"ERROR: {e}")
    
    # Try direct dataverse download
    url3 = "https://dataverse.nl/api/access/data/554105/pwt110.xlsx"
    try:
        r = requests.get(url3, timeout=30, allow_redirects=False,
                        headers={"User-Agent": "Mozilla/5.0"})
        print(f"\n  With filename: HTTP {r.status_code}")
        print(f"  Location: {r.headers.get('Location', 'N/A')}")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    probe_oecd_dataflows()
    probe_oecd_msti_dsd()
    probe_pwt_redirect()

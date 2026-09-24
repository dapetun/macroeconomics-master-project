#!/usr/bin/env python3
"""Probe OECD new Data Explorer API and PWT mirrors."""

import requests

print("=== OECD Data Explorer API probes ===")
# New OECD SDMX endpoint (post-2024 migration)
probes = [
    "https://sdmx.oecd.org/public/rest/v1/dataflow",
    "https://sdmx.oecd.org/public/rest/v1/dataflow/OECD/DF_MSTI?dimension_at_observation=AllDimensions",
]
headers = {"Accept": "application/json", "User-Agent": "Mozilla/5.0"}
for url in probes:
    try:
        r = requests.get(url, headers=headers, timeout=30)
        print("URL:", url[:80])
        print("  HTTP", r.status_code, "len=", len(r.content))
        print("  head:", r.text[:200].replace("\n", " "))
    except Exception as e:
        print("URL:", url[:80], "ERROR:", e)

print()
print("=== PWT mirror probes ===")
pwt_urls = [
    "https://www.rug.nl/ggdc/docs/pwt110.xlsx",
    "https://dataverse.nl/api/access/datafile/354095",
]
for url in pwt_urls:
    try:
        r = requests.get(url, timeout=30, allow_redirects=True)
        print("URL:", url)
        print("  HTTP", r.status_code, "len=", len(r.content),
              "ctype=", r.headers.get("Content-Type"))
    except Exception as e:
        print("URL:", url, "ERROR:", e)

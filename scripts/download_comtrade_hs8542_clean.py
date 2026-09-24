#!/usr/bin/env python3
"""Fetch one consistent UN Comtrade HS8542 annual export series.

World partner (0), export flow (X), and HS code 8542 are fixed for every
observation.  This replaces earlier mixed-response aggregates.
"""
from __future__ import annotations

from pathlib import Path
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import requests


REPORTERS = {"USA": 842, "CHN": 156, "KOR": 410, "JPN": 392, "DEU": 276, "GBR": 826, "ISR": 376, "FRA": 250}
YEARS = [str(y) for y in range(2010, 2025)]
BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
rows = []
selected = [sys.argv[1].upper()] if len(sys.argv) > 1 else list(REPORTERS)
for iso in selected:
    if iso not in REPORTERS:
        raise ValueError(f"Unknown reporter ISO3: {iso}")

def fetch(iso: str, year: str) -> list[dict]:
    """One immutable query; no shared session state across worker threads."""
    params = {"period": year, "reporterCode": REPORTERS[iso], "flowCode": "X", "partnerCode": 0, "cmdCode": "8542", "maxRecords": 10}
    response = requests.get(BASE, params=params, timeout=25)
    response.raise_for_status()
    result = []
    for item in response.json().get("data", []):
        value = item.get("primaryValue")
        if value is not None:
            result.append({"country_iso3": iso, "year": int(item["refYear"]), "value_usd": float(value), "flow_code": "X", "partner_code": 0, "cmd_code": "8542", "classification": item.get("classificationCode"), "source_url": response.url})
    return result

# Network-bound work: bounded to five connections to respect a public preview
# endpoint; each future is joined, so no worker remains after script exit.
with ThreadPoolExecutor(max_workers=5, thread_name_prefix="comtrade") as pool:
    futures = [pool.submit(fetch, iso, year) for iso in selected for year in YEARS]
    for future in as_completed(futures):
        rows.extend(future.result())

target = Path("data/raw/comtrade_hs8542_exports_clean.csv")
existing = pd.read_csv(target) if target.exists() else pd.DataFrame()
out = pd.concat([existing, pd.DataFrame(rows)], ignore_index=True).drop_duplicates(["country_iso3", "year"], keep="last").sort_values(["country_iso3", "year"])
if out.duplicated(["country_iso3", "year"]).any():
    raise RuntimeError("Duplicate reporter-year observations")
out.to_csv(target, index=False)
print(f"wrote {len(out)} observations; {out.year.min()}-{out.year.max()}")

"""Download OECD MSTI GERD/BERD for OECD+China."""
from __future__ import annotations

import hashlib
import io
import json
import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw" / "deep" / "oecd"
OUT.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0",
}
BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"
COUNTRIES = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "CHN",
]

# measure, unit, price_base → output var
SERIES = {
    "gerd_usd_ppp_current": ("G", "USD_PPP", "V"),
    "gerd_usd_ppp_constant": ("G", "USD_PPP", "Q"),
    "gerd_pct_gdp_oecd": ("G", "PT_B1GQ", "_Z"),
    "berd_pct_gdp": ("B", "PT_B1GQ", "_Z"),
}


def fetch_one(country: str, measure: str, unit: str, price_base: str) -> pd.DataFrame | None:
    key = f"{country}.A.{measure}.{unit}.{price_base}._Z"
    url = f"{BASE}/{key}"
    params = {"startPeriod": "2000", "endPeriod": "2024", "dimensionAtObservation": "AllDimensions"}
    for i in range(3):
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=45)
            if r.status_code != 200 or len(r.content) < 200:
                return None
            df = pd.read_csv(io.StringIO(r.text))
            if "TIME_PERIOD" not in df.columns or "OBS_VALUE" not in df.columns:
                return None
            out = df[["REF_AREA", "TIME_PERIOD", "OBS_VALUE"]].copy()
            out.columns = ["country_iso3", "year", "value"]
            out["value"] = pd.to_numeric(out["value"], errors="coerce")
            return out.dropna(subset=["value"])
        except Exception:
            time.sleep(2 * (i + 1))
    return None


def main(force: bool = False) -> None:
    target = OUT / "oecd_long.csv"
    if target.exists() and not force:
        print("exists", target)
        return
    rows = []
    notes = []
    for var, (measure, unit, pb) in SERIES.items():
        n_ok = 0
        for c in COUNTRIES:
            df = fetch_one(c, measure, unit, pb)
            time.sleep(0.25)
            if df is None or df.empty:
                continue
            df = df.copy()
            df["var"] = var
            rows.append(df)
            n_ok += 1
        print(var, "countries", n_ok)
        if var == "gerd_usd_ppp_constant" and n_ok < 10:
            notes.append(
                "gerd_usd_ppp_constant (PRICE_BASE=Q) sparse/missing; "
                "panel builder will deflate current USD PPP with US GDP deflator"
            )
    if not rows:
        raise RuntimeError("No OECD data downloaded")
    out = pd.concat(rows, ignore_index=True)
    out = out.drop_duplicates(["country_iso3", "year", "var"]).sort_values(
        ["var", "country_iso3", "year"]
    )
    out.to_csv(target, index=False)
    man = {
        "source": "OECD MSTI SDMX",
        "base": BASE,
        "download_date": str(date.today()),
        "n_rows": int(len(out)),
        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "series": SERIES,
        "notes": notes,
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print("wrote", target, len(out), notes)


if __name__ == "__main__":
    import sys

    main(force="--force" in sys.argv)

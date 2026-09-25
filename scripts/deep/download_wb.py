"""Download World Bank WDI indicators for OECD+China panel."""
from __future__ import annotations

import hashlib
import json
import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw" / "deep" / "wb"
OUT.mkdir(parents=True, exist_ok=True)

COUNTRIES = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "CHN",
]

INDICATORS = {
    "GB.XPD.RSDV.GD.ZS": "rd_gdp",
    "SP.POP.SCIE.RD.P6": "researchers_pm",
    "IP.JRN.ARTC.SC": "articles",
    "IP.PAT.RESD": "pat_res",
    "IP.PAT.NRES": "pat_nonres",
    "TX.VAL.TECH.MF.ZS": "hitech_share",
    "NV.IND.MANF.ZS": "mva_share",
    "NY.GDP.PCAP.PP.KD": "gdppc_ppp",
    "SP.POP.TOTL": "pop",
    "NE.GDI.FTOT.ZS": "invest_share",
    "NE.TRD.GNFS.ZS": "trade_open",
    "NY.GDP.DEFL.ZS": "gdp_deflator",
}


def get_json(url: str, retries: int = 3) -> list | dict:
    last = None
    for i in range(retries):
        try:
            r = requests.get(url, timeout=90)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(last)


def main(force: bool = False) -> None:
    target = OUT / "wb_long.csv"
    if target.exists() and not force:
        print("exists", target)
        return
    rows = []
    joined = ";".join(COUNTRIES)
    for code, var in INDICATORS.items():
        url = (
            f"https://api.worldbank.org/v2/country/{joined}/indicator/{code}"
            f"?format=json&per_page=20000&date=2000:2024"
        )
        print("fetch", var, code)
        payload = get_json(url)
        data = payload[1] if isinstance(payload, list) and len(payload) > 1 else []
        for x in data or []:
            if x.get("value") is None or not x.get("countryiso3code"):
                continue
            rows.append(
                {
                    "country_iso3": x["countryiso3code"],
                    "year": int(x["date"]),
                    "var": var,
                    "value": float(x["value"]),
                    "indicator": code,
                }
            )
        time.sleep(0.5)
    df = pd.DataFrame(rows).drop_duplicates(["country_iso3", "year", "var"])
    df = df.sort_values(["var", "country_iso3", "year"])
    df.to_csv(target, index=False)
    h = hashlib.sha256(target.read_bytes()).hexdigest()
    man = {
        "source": "World Bank WDI API",
        "url_template": "https://api.worldbank.org/v2/country/{countries}/indicator/{code}",
        "download_date": str(date.today()),
        "n_rows": int(len(df)),
        "sha256": h,
        "indicators": INDICATORS,
        "countries": COUNTRIES,
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print("wrote", target, len(df))


if __name__ == "__main__":
    import sys

    main(force="--force" in sys.argv)

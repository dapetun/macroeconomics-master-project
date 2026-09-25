"""Download UN Comtrade HS8542 / HS8486 / TOTAL for OECD+China (+ Taiwan mirror)."""
from __future__ import annotations

import hashlib
import json
import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw" / "deep" / "comtrade"
OUT.mkdir(parents=True, exist_ok=True)

BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
YEARS = list(range(2010, 2024))
ISO3 = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "CHN",
]
# Extra reporters for Taiwan mirror (imports from partner 490)
MIRROR_EXTRA = ["HKG", "SGP", "MYS", "VNM", "PHL", "THA", "IND"]


def load_reporters() -> dict[str, int]:
    url = "https://comtradeapi.un.org/files/v1/app/reference/Reporters.json"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    data = r.json()
    # structure may be list or dict with results
    rows = data if isinstance(data, list) else data.get("results", data.get("data", []))
    mapping = {}
    for x in rows:
        iso = x.get("reporterCodeIsoAlpha3") or x.get("iso3") or x.get("id")
        code = x.get("reporterCode") or x.get("code")
        if iso and code is not None:
            mapping[str(iso).upper()] = int(code)
    # fallbacks known from API docs / prior probes
    mapping.setdefault("FRA", 251)
    mapping.setdefault("CHE", 757)
    mapping.setdefault("NOR", 579)
    mapping.setdefault("USA", 842)
    mapping.setdefault("CHN", 156)
    return mapping


def get(params: dict, retries: int = 3) -> list[dict]:
    last = None
    for i in range(retries):
        try:
            r = requests.get(BASE, params=params, timeout=120)
            r.raise_for_status()
            js = r.json()
            if js.get("error"):
                raise RuntimeError(js["error"])
            return js.get("data") or []
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    print("FAIL", params, last)
    return []


def rows_from(data: list[dict], flow: str, cmd: str, note: str = "") -> list[dict]:
    out = []
    for item in data:
        val = item.get("primaryValue")
        if val is None:
            continue
        out.append(
            {
                "reporter_code": item.get("reporterCode"),
                "partner_code": item.get("partnerCode"),
                "year": int(item["refYear"]),
                "flow": item.get("flowCode") or flow,
                "cmd": str(item.get("cmdCode") or cmd),
                "value_usd": float(val),
                "classification": item.get("classificationCode"),
                "note": note,
            }
        )
    return out


def main(force: bool = False) -> None:
    world_path = OUT / "comtrade_world_flows.csv"
    chn_path = OUT / "comtrade_china_partners.csv"
    tw_path = OUT / "comtrade_taiwan_mirror.csv"
    if world_path.exists() and chn_path.exists() and tw_path.exists() and not force:
        print("exists comtrade outputs")
        return

    reporters = load_reporters()
    missing = [c for c in ISO3 + MIRROR_EXTRA if c not in reporters]
    if missing:
        print("WARNING missing reporter codes", missing)

    codes = [str(reporters[c]) for c in ISO3 if c in reporters]
    reporter_str = ",".join(codes)

    world_rows = []
    for year in YEARS:
        # HS8542 X+M world partner
        params = {
            "period": str(year),
            "reporterCode": reporter_str,
            "flowCode": "X,M",
            "partnerCode": 0,
            "partner2Code": 0,
            "customsCode": "C00",
            "motCode": 0,
            "cmdCode": "8542",
        }
        data = get(params)
        world_rows.extend(rows_from(data, "", "8542", "world_partner"))
        time.sleep(1.0)
        # TOTAL exports
        params["cmdCode"] = "TOTAL"
        params["flowCode"] = "X"
        data = get(params)
        world_rows.extend(rows_from(data, "X", "TOTAL", "world_partner"))
        time.sleep(1.0)
        # HS8486 X+M
        params["cmdCode"] = "8486"
        params["flowCode"] = "X,M"
        data = get(params)
        world_rows.extend(rows_from(data, "", "8486", "world_partner"))
        time.sleep(1.0)
        print("year", year, "world rows so far", len(world_rows))

    world = pd.DataFrame(world_rows)
    # map reporter code → iso3
    inv = {v: k for k, v in reporters.items()}
    world["country_iso3"] = world["reporter_code"].map(inv)
    world.to_csv(world_path, index=False)

    # China partner breakdown for 8542 and 8486 imports
    chn_rows = []
    for year in YEARS:
        for cmd in ["8542", "8486"]:
            params = {
                "period": str(year),
                "reporterCode": reporters["CHN"],
                "flowCode": "M",
                "partner2Code": 0,
                "customsCode": "C00",
                "motCode": 0,
                "cmdCode": cmd,
                "maxRecords": 1000,
            }
            data = get(params)
            chn_rows.extend(rows_from(data, "M", cmd, "china_partners"))
            time.sleep(1.0)
        print("china partners", year, len(chn_rows))
    chn = pd.DataFrame(chn_rows)
    chn["country_iso3"] = "CHN"
    chn.to_csv(chn_path, index=False)

    # Taiwan mirror: imports from partner 490
    mirror_isos = [c for c in ISO3 + MIRROR_EXTRA if c in reporters]
    mirror_codes = ",".join(str(reporters[c]) for c in mirror_isos)
    tw_rows = []
    for year in YEARS:
        params = {
            "period": str(year),
            "reporterCode": mirror_codes,
            "flowCode": "M",
            "partnerCode": 490,
            "partner2Code": 0,
            "customsCode": "C00",
            "motCode": 0,
            "cmdCode": "8542",
        }
        data = get(params)
        tw_rows.extend(rows_from(data, "M", "8542", "taiwan_mirror_490"))
        time.sleep(1.0)
        print("taiwan mirror", year, len(tw_rows))
    tw = pd.DataFrame(tw_rows)
    tw["country_iso3"] = tw["reporter_code"].map(inv)
    tw.to_csv(tw_path, index=False)

    man = {
        "source": "UN Comtrade preview API",
        "base": BASE,
        "download_date": str(date.today()),
        "files": {
            "comtrade_world_flows.csv": int(len(world)),
            "comtrade_china_partners.csv": int(len(chn)),
            "comtrade_taiwan_mirror.csv": int(len(tw)),
        },
        "sha256": {
            "world": hashlib.sha256(world_path.read_bytes()).hexdigest(),
            "china": hashlib.sha256(chn_path.read_bytes()).hexdigest(),
            "taiwan": hashlib.sha256(tw_path.read_bytes()).hexdigest(),
        },
        "checks_2023_chn": {
            "note": "expect IC imports ~350.1bn, exports ~136.3bn",
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    # sanity 2023
    if not world.empty:
        sub = world[(world["year"] == 2023) & (world["country_iso3"] == "CHN") & (world["cmd"] == "8542")]
        print("CHN 8542 2023", sub[["flow", "value_usd"]].to_string(index=False))
    print("done")


if __name__ == "__main__":
    import sys

    main(force="--force" in sys.argv)

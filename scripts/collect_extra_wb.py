#!/usr/bin/env python3
"""Download extra WB indicators: GERD, researchers, patents."""

import requests
import pandas as pd
import json
import time
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("data/raw")
META_DIR = Path("data/metadata")
COUNTRIES = ["USA", "CHN", "TWN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]

EXTRA = {
    "gerd_pct_gdp": ("GB.XPD.RSDV.GD.ZS", "World Bank WDI",
                     "R&D expenditure (% of GDP) - proxy for GERD"),
    "researchers_per_million": ("SP.POP.SCIE.RD.P6",
                                "World Bank WDI (UNESCO-UIS origin)",
                                "Researchers in R&D per million people"),
    "patents_resident": ("IP.PAT.RESD", "World Bank WDI (WIPO origin)",
                         "Patent applications, residents"),
    "patents_nonresident": ("IP.PAT.NRES", "World Bank WDI (WIPO origin)",
                            "Patent applications, nonresidents"),
}

results = {}
for var, (ind, src, desc) in EXTRA.items():
    base = "https://api.worldbank.org/v2/country"
    url = base + "/" + ";".join(COUNTRIES) + "/indicator/" + ind
    params = {"date": "2000:2024", "format": "json", "per_page": 500}
    try:
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        recs = [
            {"country_iso3": x["countryiso3code"],
             "year": int(x["date"]), "value": x["value"]}
            for x in data[1]
        ]
        df = pd.DataFrame(recs).dropna(subset=["value"])
        df.to_csv(RAW_DIR / (var + ".csv"), index=False)
        print("[OK] %s: %d obs, %s, %s-%s" % (
            var, len(df), sorted(df.country_iso3.unique()),
            df.year.min(), df.year.max()))
        results[var] = "success"
    except Exception as e:
        print("[FAIL] %s: %s" % (var, e))
        results[var] = "failed"
    with open(META_DIR / (var + "_metadata.json"), "w") as f:
        json.dump({"variable": var, "source": src, "indicator": ind,
                   "description": desc,
                   "download_date": datetime.now().isoformat(),
                   "status": results[var]}, f, indent=2)
    time.sleep(1)

print(results)

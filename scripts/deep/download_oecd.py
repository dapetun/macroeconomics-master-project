"""Загрузка OECD MSTI GERD/BERD. / Download OECD MSTI GERD/BERD.

I/O-bound: ThreadPool с лимитом fan-out и общим rate-limit.
I/O-bound: ThreadPool with bounded fan-out and a shared rate limit.
"""
from __future__ import annotations

import hashlib
import io
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep.paths import COUNTRIES, ROOT  # noqa: E402

OUT = ROOT / "data" / "raw" / "deep" / "oecd"
OUT.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
    "User-Agent": "Mozilla/5.0",
}
BASE = "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI"
# Ограничение параллелизма и пауза между запросами / Bound concurrency and inter-request gap
MAX_WORKERS = 4
MIN_INTERVAL_SEC = 0.15

SERIES = {
    "gerd_usd_ppp_current": ("G", "USD_PPP", "V"),
    "gerd_usd_ppp_constant": ("G", "USD_PPP", "Q"),
    "gerd_pct_gdp_oecd": ("G", "PT_B1GQ", "_Z"),
    "berd_pct_gdp": ("B", "PT_B1GQ", "_Z"),
}

_rate_lock = threading.Lock()
_next_allowed = 0.0


def _rate_wait() -> None:
    """Глобальный минимум между HTTP-вызовами. / Global minimum gap between HTTP calls."""
    global _next_allowed
    with _rate_lock:
        now = time.monotonic()
        wait = _next_allowed - now
        if wait > 0:
            time.sleep(wait)
            now = time.monotonic()
        _next_allowed = now + MIN_INTERVAL_SEC


def fetch_one(country: str, measure: str, unit: str, price_base: str) -> pd.DataFrame | None:
    key = f"{country}.A.{measure}.{unit}.{price_base}._Z"
    url = f"{BASE}/{key}"
    params = {"startPeriod": "2000", "endPeriod": "2024", "dimensionAtObservation": "AllDimensions"}
    for i in range(3):
        try:
            _rate_wait()
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


def _fetch_job(args: tuple[str, str, str, str, str]) -> tuple[str, pd.DataFrame | None]:
    var, country, measure, unit, pb = args
    df = fetch_one(country, measure, unit, pb)
    if df is None or df.empty:
        return var, None
    out = df.copy()
    out["var"] = var
    return var, out


def main(force: bool = False) -> None:
    target = OUT / "oecd_long.csv"
    if target.exists() and not force:
        print("exists", target)
        return

    jobs = [
        (var, c, measure, unit, pb)
        for var, (measure, unit, pb) in SERIES.items()
        for c in COUNTRIES
    ]
    rows: list[pd.DataFrame] = []
    ok_by_var = {var: 0 for var in SERIES}
    # Явная отмена/завершение пула через with / Explicit pool lifecycle via context manager
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = [pool.submit(_fetch_job, job) for job in jobs]
        for fut in as_completed(futures):
            var, df = fut.result()
            if df is None:
                continue
            rows.append(df)
            ok_by_var[var] += 1

    for var, n_ok in ok_by_var.items():
        print(var, "countries", n_ok)

    notes = []
    if ok_by_var.get("gerd_usd_ppp_constant", 0) < 10:
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
        "concurrency": {"max_workers": MAX_WORKERS, "min_interval_sec": MIN_INTERVAL_SEC},
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print("wrote", target, len(out), notes)


if __name__ == "__main__":
    main(force="--force" in sys.argv)

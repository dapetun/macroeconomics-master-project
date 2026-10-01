"""Загрузка списков TOP500 (ноябрь 2010–2025). / Download TOP500 November lists 2010–2025."""
from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep.paths import RAW_DEEP, ROOT  # noqa: E402

OUT = RAW_DEEP / "top500"
OUT.mkdir(parents=True, exist_ok=True)

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "Mozilla/5.0 (compatible; macro-deep-research/1.0)"})
retry = Retry(total=3, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
SESSION.mount("https://", HTTPAdapter(max_retries=retry))


def download_list(year: int) -> Path | None:
    for ext in ("xlsx", "xls"):
        url = f"https://top500.org/lists/top500/{year}/11/download/TOP500_{year}11.{ext}"
        path = OUT / f"TOP500_{year}11.{ext}"
        if path.exists() and path.stat().st_size > 10000:
            print(f"  cached {path.name}", flush=True)
            return path
        try:
            print(f"  GET {url}", flush=True)
            r = SESSION.get(url, timeout=60)
            if r.status_code == 404:
                continue
            r.raise_for_status()
            if len(r.content) < 10000:
                continue
            path.write_bytes(r.content)
            print(f"  saved {path.name} {len(r.content)}", flush=True)
            return path
        except Exception as e:
            print(f"  err {ext}: {e}", flush=True)
            time.sleep(2)
    return None


def read_excel_any(path: Path) -> pd.DataFrame:
    for header in range(0, 5):
        try:
            df = pd.read_excel(path, header=header)
            cols = [str(c).strip() for c in df.columns]
            if any(c.lower() == "rank" for c in cols):
                df.columns = cols
                return df
        except Exception:
            continue
    raise RuntimeError(f"Cannot find Rank header in {path}")


def main(force: bool = False) -> None:
    combined = OUT / "top500_all.csv"
    if combined.exists() and not force:
        print("exists", combined, flush=True)
        return
    frames = []
    files = {}
    missing = []
    for year in range(2010, 2026):
        print("year", year, flush=True)
        path = download_list(year)
        time.sleep(1.5)
        if path is None:
            missing.append(year)
            continue
        df = read_excel_any(path)
        df["list_year"] = year
        df["list_month"] = 11
        df["source_file"] = path.name
        frames.append(df)
        files[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        print("  rows", len(df), flush=True)
    if not frames:
        raise RuntimeError("No TOP500 lists downloaded")
    out = pd.concat(frames, ignore_index=True, sort=False)
    out.to_csv(combined, index=False)
    man = {
        "source": "TOP500.org November lists",
        "download_date": str(date.today()),
        "n_rows": int(len(out)),
        "sha256_combined": hashlib.sha256(combined.read_bytes()).hexdigest(),
        "files": files,
        "years_present": sorted(out["list_year"].unique().tolist()),
        "years_missing": missing,
        "root": str(ROOT),
    }
    (OUT / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print("wrote", combined, len(out), "missing", missing, flush=True)


if __name__ == "__main__":
    import sys

    main(force="--force" in sys.argv)

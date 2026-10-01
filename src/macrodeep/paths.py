"""Пути и константы выборки. / Paths and sample constants."""
from __future__ import annotations

from pathlib import Path

# Корень репозитория: src/macrodeep/../.. / Repo root: src/macrodeep/../..
ROOT = Path(__file__).resolve().parents[2]
PANEL_PATH = ROOT / "data" / "deep" / "panel_oecd_chn.csv"
TABLES = ROOT / "results" / "deep" / "tables"
FIGURES = ROOT / "results" / "deep" / "figures"
RAW_DEEP = ROOT / "data" / "raw" / "deep"
REPORTS = ROOT / "reports"

# OECD + Китай, 39 стран / OECD + China, 39 countries
COUNTRIES: list[str] = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "CHN",
]
YEARS = list(range(2000, 2024))

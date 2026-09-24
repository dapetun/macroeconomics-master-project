"""Macro-block radar (min-max across 8 countries) + absolute GERD bar chart.
Does NOT touch M1/PCA.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data_reviewed" / "core_panel_reviewed.csv"
GERD_PPP = ROOT / "data" / "raw" / "oecd_gerd_usd_ppp.csv"
FIG_DIR = ROOT / "data_reviewed" / "figures_reviewed"
TABLE_DIR = ROOT / "data_reviewed" / "tables_reviewed"

COUNTRIES = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]
# (label, column, joint_year preferred)
BLOCKS = [
    ("GERD % GDP", "gerd_pct_gdp", 2023),
    ("Researchers / mn", "researchers_per_million", 2022),
    ("Articles (log)", "scopus_articles", 2023),
    ("Patents resident (log)", "patents_resident", 2021),
    ("MVA % GDP", "mva_pct_gdp", 2021),
    ("Hitech export %", "hitech_export_share", 2023),
    ("GDP pc PPP (log)", "gdp_pc_ppp", 2023),
    ("TFP (ctfp)", "tfp_ctfp", 2023),
]


def joint_year_values(df: pd.DataFrame, col: str, preferred_year: int) -> tuple[int, pd.Series]:
    sub = df[df["country_iso3"].isin(COUNTRIES)][["country_iso3", "year", col]].dropna()
    # prefer preferred_year if >= 4 countries present; else latest year with max coverage
    years = sorted(sub["year"].unique(), reverse=True)
    if preferred_year in years:
        y = preferred_year
        s = sub[sub["year"] == y].set_index("country_iso3")[col]
        if s.notna().sum() >= 4:
            return y, s.reindex(COUNTRIES)
    best_y, best_s, best_n = None, None, -1
    for y in years:
        s = sub[sub["year"] == y].set_index("country_iso3")[col]
        n = int(s.reindex(COUNTRIES).notna().sum())
        if n > best_n:
            best_y, best_s, best_n = y, s.reindex(COUNTRIES), n
    return int(best_y), best_s


def minmax(s: pd.Series) -> pd.Series:
    v = s.astype(float)
    lo, hi = v.min(skipna=True), v.max(skipna=True)
    if pd.isna(lo) or pd.isna(hi) or hi == lo:
        return v * 0.0
    return (v - lo) / (hi - lo)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(PANEL)

    raw_rows = []
    norm = {c: [] for c in COUNTRIES}
    labels = []
    years_used = []

    for label, col, pref_y in BLOCKS:
        y, s = joint_year_values(df, col, pref_y)
        if col in ("scopus_articles", "patents_resident", "gdp_pc_ppp"):
            s_plot = np.log(s.astype(float))
            transform = "log"
        else:
            s_plot = s.astype(float)
            transform = "level"
        s_norm = minmax(s_plot)
        labels.append(label)
        years_used.append(y)
        for c in COUNTRIES:
            raw_rows.append(
                {
                    "block": label,
                    "column": col,
                    "joint_year": y,
                    "transform": transform,
                    "country_iso3": c,
                    "raw_or_log": float(s_plot.get(c)) if pd.notna(s_plot.get(c)) else float("nan"),
                    "minmax_8countries": float(s_norm.get(c)) if pd.notna(s_norm.get(c)) else float("nan"),
                }
            )
            norm[c].append(float(s_norm.get(c)) if pd.notna(s_norm.get(c)) else float("nan"))

    radar_tbl = pd.DataFrame(raw_rows)
    radar_tbl.to_csv(TABLE_DIR / "radar_macro_blocks_minmax.csv", index=False)

    # Radar: USA vs CHN (thick) + optional thin mean of others
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for c, color, lw, alpha in [
        ("USA", "#1f77b4", 2.5, 1.0),
        ("CHN", "#ff7f0e", 2.5, 1.0),
    ]:
        vals = norm[c] + norm[c][:1]
        ax.plot(angles, vals, color=color, linewidth=lw, label=c)
        ax.fill(angles, vals, color=color, alpha=0.12)

    # mean of other 6 as reference
    others = [c for c in COUNTRIES if c not in ("USA", "CHN")]
    mean_vals = []
    for i in range(len(labels)):
        xs = [norm[c][i] for c in others if not np.isnan(norm[c][i])]
        mean_vals.append(float(np.mean(xs)) if xs else float("nan"))
    mean_vals += mean_vals[:1]
    ax.plot(angles, mean_vals, color="gray", linewidth=1.2, linestyle="--", label="mean other 6")

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=8)
    ax.set_ylim(0, 1)
    ax.set_title(
        "Macro TCI-style blocks (min–max across 8 countries)\n"
        "Illustration only — not capability / conversion index; years per spoke in table",
        size=11,
        pad=16,
    )
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
    fig.tight_layout()
    out_radar = FIG_DIR / "F11_radar_macro_blocks.png"
    fig.savefig(out_radar, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Wrote", out_radar)

    # Absolute GERD bar: USA / CHN / KOR for 2010 and latest joint
    gerd = pd.read_csv(GERD_PPP)
    g = gerd[gerd["country_iso3"].isin(["USA", "CHN", "KOR"])]
    wide = g.pivot(index="year", columns="country_iso3", values="value")
    y_end = int(wide.dropna(subset=["USA", "CHN"]).index.max())
    years_bar = [2010, y_end]
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(["USA", "CHN", "KOR"]))
    width = 0.35
    for i, year in enumerate(years_bar):
        vals = [float(wide.loc[year, c]) / 1000.0 for c in ["USA", "CHN", "KOR"]]  # → bn PPP USD
        ax.bar(x + (i - 0.5) * width, vals, width, label=str(year))
    ax.set_xticks(x)
    ax.set_xticklabels(["USA", "CHN", "KOR"])
    ax.set_ylabel("GERD (bn USD PPP, OECD MSTI)")
    ax.set_title(
        f"Absolute GERD volume (OECD mln→bn USD PPP), 2010 vs {y_end}\n"
        "Different vintage from WB GERD % GDP — do not mix arithmetically"
    )
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    out_bar = FIG_DIR / "F12_gerd_absolute_ppp.png"
    fig.savefig(out_bar, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Wrote", out_bar)
    print("Radar years:", list(zip(labels, years_used)))
    print(f"GERD absolute end year {y_end}: USA={wide.loc[y_end,'USA']:.0f} CHN={wide.loc[y_end,'CHN']:.0f} mln PPP")


if __name__ == "__main__":
    main()

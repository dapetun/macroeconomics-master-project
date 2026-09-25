"""Shared helpers for deep-research notebooks and scripts."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# Repo root = notebooks/deep/../..
ROOT = Path(__file__).resolve().parents[2]
PANEL_PATH = ROOT / "data" / "deep" / "panel_oecd_chn.csv"
TABLES = ROOT / "results" / "deep" / "tables"
FIGURES = ROOT / "results" / "deep" / "figures"
RAW_DEEP = ROOT / "data" / "raw" / "deep"

COUNTRIES: list[str] = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "CHN",
]

COLOR_USA = "#1f77b4"
COLOR_CHN = "#d62728"
COLOR_OTHER = "#bbbbbb"


def load_panel(path: Path | None = None) -> pd.DataFrame:
    """Load the OECD+China analysis panel."""
    p = path or PANEL_PATH
    df = pd.read_csv(p)
    df["year"] = df["year"].astype(int)
    return df


def save_table(df: pd.DataFrame, name: str) -> Path:
    TABLES.mkdir(parents=True, exist_ok=True)
    out = TABLES / f"{name}.csv"
    df.to_csv(out, index=False)
    return out


def save_fig(fig: plt.Figure, name: str, dpi: int = 150) -> Path:
    FIGURES.mkdir(parents=True, exist_ok=True)
    out = FIGURES / f"{name}.png"
    fig.savefig(out, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return out


def style_axes(ax: plt.Axes, title: str = "", ylabel: str = "", xlabel: str = "") -> None:
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.25)


def country_color(iso3: str) -> str:
    if iso3 == "USA":
        return COLOR_USA
    if iso3 == "CHN":
        return COLOR_CHN
    return COLOR_OTHER


def twfe(
    df: pd.DataFrame,
    y: str,
    xs: Sequence[str],
    *,
    entity: str = "country_iso3",
    time: str = "year",
    cluster: str | None = "country_iso3",
) -> pd.DataFrame:
    """Two-way fixed effects via OLS with country and year dummies.

    Returns one row per explanatory variable (not FE dummies) with
    coefficient, SE, p-value, 95% CI, N, G.
    """
    use = df[[y, entity, time, *xs]].dropna().copy()
    use[entity] = use[entity].astype(str)
    # year may be int or period label (e.g. 2001-05)
    if pd.api.types.is_numeric_dtype(use[time]):
        use[time] = use[time].astype(int)
    else:
        use[time] = use[time].astype(str)
    rhs = " + ".join(xs)
    formula = f"{y} ~ {rhs} + C({entity}) + C({time})"
    model = smf.ols(formula, data=use)
    if cluster is None:
        res = model.fit(cov_type="HC1")
        g = np.nan
    else:
        groups = use[cluster]
        res = model.fit(cov_type="cluster", cov_kwds={"groups": groups})
        g = int(groups.nunique())
    rows = []
    for x in xs:
        if x not in res.params.index:
            continue
        b = float(res.params[x])
        se = float(res.bse[x])
        p = float(res.pvalues[x])
        ci = res.conf_int().loc[x]
        rows.append(
            {
                "term": x,
                "beta": b,
                "se": se,
                "p": p,
                "ci_lo": float(ci[0]),
                "ci_hi": float(ci[1]),
                "N": int(res.nobs),
                "G": g,
                "r2": float(res.rsquared),
            }
        )
    return pd.DataFrame(rows)


def ols_cluster(
    df: pd.DataFrame,
    formula: str,
    *,
    cluster: str | None = "country_iso3",
) -> object:
    """Fit OLS; optional country-cluster SE. Returns statsmodels result."""
    use = df.copy()
    model = smf.ols(formula, data=use)
    if cluster is None:
        return model.fit(cov_type="HC1")
    return model.fit(cov_type="cluster", cov_kwds={"groups": use[cluster]})


def coef_table(res, terms: Iterable[str], *, G: int | float = np.nan) -> pd.DataFrame:
    rows = []
    for x in terms:
        if x not in res.params.index:
            continue
        ci = res.conf_int().loc[x]
        rows.append(
            {
                "term": x,
                "beta": float(res.params[x]),
                "se": float(res.bse[x]),
                "p": float(res.pvalues[x]),
                "ci_lo": float(ci[0]),
                "ci_hi": float(ci[1]),
                "N": int(res.nobs),
                "G": G,
                "r2": float(res.rsquared),
            }
        )
    return pd.DataFrame(rows)


def within_demean(df: pd.DataFrame, cols: Sequence[str], by: Sequence[str]) -> pd.DataFrame:
    """Subtract group means for listed columns (for within scatter plots)."""
    out = df.copy()
    means = out.groupby(list(by), observed=True)[list(cols)].transform("mean")
    for c in cols:
        out[f"{c}_within"] = out[c] - means[c]
    return out

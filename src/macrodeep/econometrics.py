"""Эконометрические хелперы. / Econometric helpers."""
from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np
import pandas as pd


def _smf():
    """Ленивый import statsmodels (тяжёлый). / Lazy-import heavy statsmodels."""
    import statsmodels.formula.api as smf

    return smf


def twfe(
    df: pd.DataFrame,
    y: str,
    xs: Sequence[str],
    *,
    entity: str = "country_iso3",
    time: str = "year",
    cluster: str | None = "country_iso3",
) -> pd.DataFrame:
    """TWFE через OLS с дамми страны и года. / TWFE via OLS with country and year dummies.

    Одна строка на регрессор (без FE): beta, SE, p, CI, N, G.
    One row per regressor (no FE dummies): beta, SE, p, CI, N, G.
    """
    use = df[[y, entity, time, *xs]].dropna().copy()
    use[entity] = use[entity].astype(str)
    # year — int или метка периода (напр. 2001-05) / year may be int or period label
    if pd.api.types.is_numeric_dtype(use[time]):
        use[time] = use[time].astype(int)
    else:
        use[time] = use[time].astype(str)
    rhs = " + ".join(xs)
    formula = f"{y} ~ {rhs} + C({entity}) + C({time})"
    model = _smf().ols(formula, data=use)
    if cluster is None:
        res = model.fit(cov_type="HC1")
        g = np.nan
    else:
        groups = use[cluster]
        res = model.fit(cov_type="cluster", cov_kwds={"groups": groups})
        g = int(groups.nunique())
    return coef_table(res, xs, G=g)


def twfe_betas(
    df: pd.DataFrame,
    y: str,
    xs: Sequence[str],
    *,
    entity: str = "country_iso3",
    time: str = "year",
    sweeps: int = 40,
) -> dict[str, float]:
    """Точечные TWFE-коэффициенты без SE (для LOO). / Point TWFE betas, no SE (for LOO).

    Двустороннее демеанинг до сходимости ≈ дамми-OLS. / Alternating demeaning ≈ dummy OLS.
    """
    use = df[[y, entity, time, *xs]].dropna()
    yvec = use[y].to_numpy(dtype=float, copy=True)
    xmat = use[list(xs)].to_numpy(dtype=float, copy=True)
    ent = pd.factorize(use[entity], sort=True)[0]
    tim = pd.factorize(use[time], sort=True)[0]
    n_ent = int(ent.max()) + 1
    n_tim = int(tim.max()) + 1

    def _demean(arr: np.ndarray, codes: np.ndarray, n_groups: int) -> None:
        # in-place group demean for 1-D or 2-D (columns independent)
        if arr.ndim == 1:
            sums = np.bincount(codes, weights=arr, minlength=n_groups)
            counts = np.bincount(codes, minlength=n_groups).astype(float)
            counts[counts == 0] = np.nan
            arr -= sums[codes] / counts[codes]
            return
        for j in range(arr.shape[1]):
            sums = np.bincount(codes, weights=arr[:, j], minlength=n_groups)
            counts = np.bincount(codes, minlength=n_groups).astype(float)
            counts[counts == 0] = np.nan
            arr[:, j] -= sums[codes] / counts[codes]

    for _ in range(sweeps):
        _demean(yvec, ent, n_ent)
        _demean(xmat, ent, n_ent)
        _demean(yvec, tim, n_tim)
        _demean(xmat, tim, n_tim)

    beta, *_ = np.linalg.lstsq(xmat, yvec, rcond=None)
    return {name: float(b) for name, b in zip(xs, beta)}


def ols_cluster(
    df: pd.DataFrame,
    formula: str,
    *,
    cluster: str | None = "country_iso3",
):
    """OLS; опционально SE по кластерам стран. / OLS; optional country-cluster SE."""
    model = _smf().ols(formula, data=df)
    if cluster is None:
        return model.fit(cov_type="HC1")
    return model.fit(cov_type="cluster", cov_kwds={"groups": df[cluster]})


def coef_table(res, terms: Iterable[str], *, G: int | float = np.nan) -> pd.DataFrame:
    """Таблица коэффициентов из результата statsmodels. / Coefficient table from a statsmodels result."""
    ci_all = res.conf_int()
    rows = []
    for x in terms:
        if x not in res.params.index:
            continue
        ci = ci_all.loc[x]
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
    """Вычесть групповые средние (within-scatter). / Subtract group means (within scatter)."""
    out = df.copy()
    means = out.groupby(list(by), observed=True)[list(cols)].transform("mean")
    for c in cols:
        out[f"{c}_within"] = out[c] - means[c]
    return out

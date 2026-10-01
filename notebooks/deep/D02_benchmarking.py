# %% [markdown]
# D02 — Отклонение США и Китая от нормы дохода (H1) / USA–China residual norms (H1)

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (
    apply_hse_style,  # noqa: E402
    load_panel, save_table, save_fig, style_axes,
    FIGSIZE, FIGSIZE_TALL, INDICATOR_LABELS, GRAY, FOCUS_SERIES,
    barh_usa_chn,
)

apply_hse_style()

panel = load_panel()
# Показатели профиля H1 / H1 profile indicators
inds = list(INDICATOR_LABELS.keys())
labels = [INDICATOR_LABELS[k] for k in inds]


# %%
def residuals_for(
    k: str,
    df: pd.DataFrame,
    exclude_chn: bool = False,
    rhs: str = "ln_gdppc + ln_pop + C(year)",
) -> pd.DataFrame:
    """Остатки ln(индикатор) от нормы дохода/размера. / Residuals of ln(indicator) vs income/size norm."""
    d = df.dropna(subset=[k, "ln_gdppc", "ln_pop"]).copy()
    d["ln_gdppc2"] = d["ln_gdppc"] ** 2
    d["lnk"] = np.log(d[k].where(d[k] > 0))
    d = d.dropna(subset=["lnk"])
    train = d[d["country_iso3"] != "CHN"] if exclude_chn else d
    res = smf.ols(f"lnk ~ {rhs}", data=train).fit()
    d["resid"] = d["lnk"] - res.predict(d)
    d["pct_above"] = np.exp(d["resid"]) - 1
    d["indicator"] = k
    return d[["country_iso3", "year", "indicator", "resid", "pct_above"]]


all_res = [residuals_for(k, panel, exclude_chn=False) for k in inds]
res_df = pd.concat(all_res, ignore_index=True)
save_table(res_df, "D02_residuals_all")

# Робастность: норма без Китая в оценке / Robustness: norm estimated without China
res_x = pd.concat([residuals_for(k, panel, exclude_chn=True) for k in inds], ignore_index=True)
save_table(res_x, "D02_residuals_norm_without_chn")

# %%
focus = res_df[res_df["country_iso3"].isin(["USA", "CHN"])].copy()
prof = (
    focus[(focus["year"] >= 2019) & (focus["year"] <= 2023)]
    .groupby(["country_iso3", "indicator"])["pct_above"]
    .mean()
    .reset_index()
)
save_table(prof, "D02_profile_2019_2023")

fig, ax = plt.subplots(figsize=FIGSIZE)
usa = prof[prof.country_iso3 == "USA"].set_index("indicator").reindex(inds)["pct_above"] * 100
chn = prof[prof.country_iso3 == "CHN"].set_index("indicator").reindex(inds)["pct_above"] * 100
barh_usa_chn(ax, usa, chn, labels)
style_axes(ax, xlabel="% выше или ниже нормы")
ax.legend()
save_fig(fig, "D02_profile_2019_2023")

# %%
fig, axes = plt.subplots(2, 3, figsize=(6.4, 5.4), sharex=True)
axes = axes.ravel()
for i, k in enumerate(inds):
    ax = axes[i]
    for code, col, lab in FOCUS_SERIES:
        s = focus[(focus.country_iso3 == code) & (focus.indicator == k)].sort_values("year")
        ax.plot(s.year, s.pct_above * 100, color=col, label=lab)
    ax.axhline(0, color=GRAY, lw=0.8)
    style_axes(ax, ylabel=f"{INDICATOR_LABELS[k]}, %")
axes[0].legend()
save_fig(fig, "D02_residual_paths")

# %%
# with_pop совпадает с основной спецификацией выше / with_pop matches the main spec above
VARIANTS = {
    "with_pop": ("ln_gdppc + ln_pop + C(year)", False),
    "without_pop": ("ln_gdppc + C(year)", False),
    "with_pop_norm_without_chn": ("ln_gdppc + ln_pop + C(year)", True),
    "with_pop_quadratic": ("ln_gdppc + ln_gdppc2 + ln_pop + C(year)", False),
}
vrows = []
for vname, (rhs, excl) in VARIANTS.items():
    if vname == "with_pop":
        # Переиспользуем уже посчитанные остатки / Reuse already computed residuals
        r = res_df
    else:
        r = pd.concat(
            [residuals_for(k, panel, exclude_chn=excl, rhs=rhs) for k in inds],
            ignore_index=True,
        )
    r = r[r.country_iso3.isin(["USA", "CHN"]) & r.year.between(2019, 2023)]
    for c, v in r.groupby(["country_iso3", "indicator"])["pct_above"].mean().items():
        country, indicator = c
        vrows.append({"variant": vname, "indicator": indicator, "country_iso3": country, "pct_above": v})
variants = pd.DataFrame(vrows)
save_table(variants, "D02_profile_variants_2019_2023")

fig, axes = plt.subplots(2, 1, figsize=FIGSIZE_TALL, sharex=False)
for ax, vname, title in [
    (axes[0], "with_pop", "Норма: доход и население"),
    (axes[1], "without_pop", "Норма: только доход"),
]:
    sub = variants[variants.variant == vname]
    u = sub[sub.country_iso3 == "USA"].set_index("indicator").reindex(inds)["pct_above"] * 100
    c = sub[sub.country_iso3 == "CHN"].set_index("indicator").reindex(inds)["pct_above"] * 100
    barh_usa_chn(ax, u, c, labels)
    style_axes(ax, xlabel=f"{title}. % выше или ниже нормы, среднее 2019–2023")
axes[0].legend()
save_fig(fig, "D02_profile_with_vs_without_pop")

last = panel[panel.year == 2019]
others = last[~last.country_iso3.isin(["USA", "CHN"])]
support = pd.DataFrame([{
    "ln_pop_CHN": float(last.loc[last.country_iso3 == "CHN", "ln_pop"].iloc[0]),
    "ln_pop_USA": float(last.loc[last.country_iso3 == "USA", "ln_pop"].iloc[0]),
    "ln_pop_max_others": float(others["ln_pop"].max()),
    "ln_gdppc_CHN": float(last.loc[last.country_iso3 == "CHN", "ln_gdppc"].iloc[0]),
    "ln_gdppc_min_others": float(last.loc[last.country_iso3 != "CHN", "ln_gdppc"].min()),
}])
save_table(support, "D02_support_check")

# Квадрат дохода: сводка коэффициента / Income quadratic: coefficient summary
rows = []
for k in inds:
    d = panel.dropna(subset=[k, "ln_gdppc", "ln_pop"]).copy()
    d["lnk"] = np.log(d[k].where(d[k] > 0))
    d = d.dropna(subset=["lnk"])
    d["ln_gdppc2"] = d["ln_gdppc"] ** 2
    r = smf.ols("lnk ~ ln_gdppc + ln_gdppc2 + ln_pop + C(year)", data=d).fit()
    rows.append({"indicator": k, "b_gdppc2": float(r.params["ln_gdppc2"]), "p": float(r.pvalues["ln_gdppc2"])})
save_table(pd.DataFrame(rows), "D02_quadratic_check")
print("D02 done")

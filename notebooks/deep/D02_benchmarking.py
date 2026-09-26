# %% [markdown]
# D02 — Отклонение США и Китая от нормы для уровня дохода (H1)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import load_panel, save_table, save_fig, style_axes, COLOR_USA, COLOR_CHN

panel = load_panel()
indicators = {
    "rd_gdp": "rd_gdp",
    "researchers_pm": "researchers_pm",
    "articles_pm": "articles_pm",
    "pat_res_pm": "pat_res_pm",
    "mva_share": "mva_share",
    "hitech_share": "hitech_share",
}

# %%
def residuals_for(k: str, df: pd.DataFrame, exclude_chn: bool = False,
                  rhs: str = "ln_gdppc + ln_pop + C(year)") -> pd.DataFrame:
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


all_res = []
for k in indicators:
    all_res.append(residuals_for(k, panel, exclude_chn=False))
res_df = pd.concat(all_res, ignore_index=True)
save_table(res_df, "D02_residuals_all")

# robustness without CHN in training
all_res_x = []
for k in indicators:
    all_res_x.append(residuals_for(k, panel, exclude_chn=True))
res_x = pd.concat(all_res_x, ignore_index=True)
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

fig, ax = plt.subplots(figsize=(9, 5))
inds = list(indicators.keys())
ypos = np.arange(len(inds))
w = 0.35
usa = prof[prof.country_iso3 == "USA"].set_index("indicator").reindex(inds)["pct_above"] * 100
chn = prof[prof.country_iso3 == "CHN"].set_index("indicator").reindex(inds)["pct_above"] * 100
ax.barh(ypos - w / 2, usa, w, label="USA", color=COLOR_USA)
ax.barh(ypos + w / 2, chn, w, label="CHN", color=COLOR_CHN)
ax.axvline(0, color="black", lw=0.8)
ax.set_yticks(ypos)
ax.set_yticklabels(inds)
style_axes(ax, title="Отклонение от нормы дохода/размера, среднее 2019–2023 (%)", xlabel="% выше/ниже нормы")
ax.legend()
save_fig(fig, "D02_profile_2019_2023")

# %%
fig, axes = plt.subplots(2, 3, figsize=(12, 6), sharex=True)
axes = axes.ravel()
for i, k in enumerate(inds):
    ax = axes[i]
    for c, col in [("USA", COLOR_USA), ("CHN", COLOR_CHN)]:
        s = focus[(focus.country_iso3 == c) & (focus.indicator == k)].sort_values("year")
        ax.plot(s.year, s.pct_above * 100, color=col, label=c)
    ax.axhline(0, color="gray", lw=0.7)
    style_axes(ax, title=k, ylabel="%")
axes[0].legend(fontsize=8)
fig.suptitle("Пути отклонения от нормы")
save_fig(fig, "D02_residual_paths")

# %%
VARIANTS = {
    "with_pop": ("ln_gdppc + ln_pop + C(year)", False),
    "without_pop": ("ln_gdppc + C(year)", False),
    "with_pop_norm_without_chn": ("ln_gdppc + ln_pop + C(year)", True),
    "with_pop_quadratic": ("ln_gdppc + ln_gdppc2 + ln_pop + C(year)", False),
}
vrows = []
for vname, (rhs, excl) in VARIANTS.items():
    for k in inds:
        r = residuals_for(k, panel, exclude_chn=excl, rhs=rhs)
        r = r[r.country_iso3.isin(["USA", "CHN"]) & r.year.between(2019, 2023)]
        for c, v in r.groupby("country_iso3")["pct_above"].mean().items():
            vrows.append({"variant": vname, "indicator": k, "country_iso3": c, "pct_above": v})
variants = pd.DataFrame(vrows)
save_table(variants, "D02_profile_variants_2019_2023")

fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
for ax, vname, title in [(axes[0], "with_pop", "Норма: доход + население"),
                         (axes[1], "without_pop", "Норма: только доход")]:
    sub = variants[variants.variant == vname]
    u = sub[sub.country_iso3 == "USA"].set_index("indicator").reindex(inds)["pct_above"] * 100
    c = sub[sub.country_iso3 == "CHN"].set_index("indicator").reindex(inds)["pct_above"] * 100
    ax.barh(ypos - w / 2, u, w, label="USA", color=COLOR_USA)
    ax.barh(ypos + w / 2, c, w, label="CHN", color=COLOR_CHN)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_yticks(ypos)
    ax.set_yticklabels(inds)
    style_axes(ax, title=title, xlabel="% выше/ниже нормы, среднее 2019–2023")
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

# quadratic robustness summary
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

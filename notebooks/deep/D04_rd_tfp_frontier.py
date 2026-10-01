# %% [markdown]
# D04 — R&D × отставание от фронтира → рост TFP (H3)
# R&D × distance to frontier → TFP growth (H3)

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (
    apply_hse_style,  # noqa: E402
    load_panel, save_table, save_fig, style_axes, twfe, twfe_betas, ols_cluster, coef_table,
    NAVY, BLUE, COLOR_USA, COLOR_CHN, GRAY, ORANGE, FIGSIZE,
)

apply_hse_style()

panel = load_panel()
d = panel.dropna(subset=["dln_tfp", "rd_c", "gap_c", "rd_gap"]).copy()
xs = ["rd_c", "gap_c", "rd_gap"]

# %%
# Одна оценка основной модели → и таблица, и предельный эффект.
# Fit the main model once → both the coef table and marginal effects.
res = ols_cluster(d, "dln_tfp ~ rd_c + gap_c + rd_gap + C(country_iso3) + C(year)")
main = coef_table(res, xs, G=int(d["country_iso3"].nunique()))
main["spec"] = "main"
print(main)

b1, b3 = float(res.params["rd_c"]), float(res.params["rd_gap"])
cov = res.cov_params().loc[["rd_c", "rd_gap"], ["rd_c", "rd_gap"]].values

gaps = np.linspace(0, 1.2, 25)
# Сетка gap → центрированная шкала (как в rd_c / gap_c). / Gap grid → centered scale.
gap_mean = float(panel["gap_lag1"].mean(skipna=True))
me = []
for g in gaps:
    gc = g - gap_mean
    m = b1 + b3 * gc
    v = cov[0, 0] + (gc ** 2) * cov[1, 1] + 2 * gc * cov[0, 1]
    se = np.sqrt(max(v, 0))
    me.append({"gap": g, "me": m, "se": se, "ci_lo": m - 1.96 * se, "ci_hi": m + 1.96 * se})
me_df = pd.DataFrame(me)
save_table(me_df, "D04_marginal_effect")

fig, ax = plt.subplots(figsize=FIGSIZE)
ax.plot(me_df.gap, me_df.me, color=NAVY)
ax.fill_between(me_df.gap, me_df.ci_lo, me_df.ci_hi, color=BLUE, alpha=0.18)
ax.axhline(0, color=GRAY, lw=0.8)
for lab, gval, col in [("США", 0.0, COLOR_USA), ("Китай, около 2023", 0.75, COLOR_CHN)]:
    ax.axvline(gval, color=col, ls="--", lw=1.4, label=lab)
style_axes(ax, xlabel="отставание от США, gap = −ln(ctfp)", ylabel="наклон")
ax.legend()
save_fig(fig, "D04_marginal_effect")

# %%
# Leave-one-out: только beta3, без SE/формулы / Point beta3 only — skip formula SE path
loo = []
for c in sorted(d.country_iso3.unique()):
    b = twfe_betas(d[d.country_iso3 != c], "dln_tfp", xs)["rd_gap"]
    loo.append({"dropped": c, "beta3": b})
loo_df = pd.DataFrame(loo)
save_table(loo_df, "D04_leave_one_out")
fig, ax = plt.subplots(figsize=(6.4, 4.4))
ax.plot(loo_df.dropped, loo_df.beta3, marker="o", color=NAVY)
ax.axhline(float(main.loc[main.term == "rd_gap", "beta"].iloc[0]), color=ORANGE, ls="--")
plt.xticks(rotation=90, fontsize=8)
style_axes(ax, ylabel="коэффициент")
save_fig(fig, "D04_leave_one_out")

# %%
robust = [main]
# Пятилетние средние + FE периода / Five-year averages with period FE
p5 = (
    d[d.period5 != "other"]
    .groupby(["country_iso3", "period5"], as_index=False)
    .agg(dln_tfp=("dln_tfp", "mean"), rd_c=("rd_c", "mean"), gap_c=("gap_c", "mean"), rd_gap=("rd_gap", "mean"))
    .rename(columns={"period5": "year"})
)
t = twfe(p5, "dln_tfp", xs)
t["spec"] = "five_year"
robust.append(t)

dd = panel.dropna(subset=["dln_lp", *xs])
t = twfe(dd, "dln_lp", xs)
t["spec"] = "dln_lp"
robust.append(t)

for label, subset in [
    ("pre2020", d[d.year < 2020]),
    ("no_chn", d[d.country_iso3 != "CHN"]),
    ("no_far_gap", d[~d.country_iso3.isin(["COL", "MEX", "CRI", "CHL", "TUR"])]),
]:
    t = twfe(subset, "dln_tfp", xs)
    t["spec"] = label
    robust.append(t)

t = twfe(d, "dln_tfp", ["rd_c", "gap_c"])
t["spec"] = "no_interaction"
robust.append(t)

rob = pd.concat(robust, ignore_index=True)
save_table(rob, "D04_robustness")
save_table(main, "D04_main")
print("D04 done")

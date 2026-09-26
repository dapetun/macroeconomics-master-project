# %% [markdown]
# D04 — R&D × отставание от фронтира → рост TFP (H3)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import load_panel, save_table, save_fig, style_axes, twfe

panel = load_panel().copy()
d = panel.dropna(subset=["dln_tfp", "rd_c", "gap_c", "rd_gap"]).copy()

# %%
main = twfe(d, "dln_tfp", ["rd_c", "gap_c", "rd_gap"])
main["spec"] = "main"
print(main)

# Fit full model once for covariance of marginal effects
res = smf.ols(
    "dln_tfp ~ rd_c + gap_c + rd_gap + C(country_iso3) + C(year)", data=d
).fit(cov_type="cluster", cov_kwds={"groups": d["country_iso3"]})
b1, b3 = float(res.params["rd_c"]), float(res.params["rd_gap"])
cov = res.cov_params().loc[["rd_c", "rd_gap"], ["rd_c", "rd_gap"]].values

gaps = np.linspace(0, 1.2, 25)
# effect uses centered gap: convert grid to centered scale
gap_mean = float(panel["gap_lag1"].mean(skipna=True))
me = []
for g in gaps:
    gc = g - gap_mean
    # ME = b1 + b3 * gc  (since rd_c term and interaction with gap_c)
    m = b1 + b3 * gc
    # var = var(b1) + gc^2 var(b3) + 2 gc cov
    v = cov[0, 0] + (gc ** 2) * cov[1, 1] + 2 * gc * cov[0, 1]
    se = np.sqrt(max(v, 0))
    me.append({"gap": g, "me": m, "se": se, "ci_lo": m - 1.96 * se, "ci_hi": m + 1.96 * se})
me_df = pd.DataFrame(me)
save_table(me_df, "D04_marginal_effect")

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(me_df.gap, me_df.me, color="black")
ax.fill_between(me_df.gap, me_df.ci_lo, me_df.ci_hi, alpha=0.2)
ax.axhline(0, color="gray", lw=0.8)
for lab, gval, col in [("USA", 0.0, "#1f77b4"), ("CHN~2023", 0.75, "#d62728")]:
    ax.axvline(gval, color=col, ls="--", lw=1, label=lab)
style_axes(ax, title="Предельный эффект R&D на рост TFP в зависимости от gap", xlabel="gap = -ln(ctfp)", ylabel="п.п. роста TFP на 1 п.п. R&D/GDP")
ax.legend()
save_fig(fig, "D04_marginal_effect")

# %%
# leave-one-out beta3
loo = []
for c in sorted(d.country_iso3.unique()):
    dd = d[d.country_iso3 != c]
    tt = twfe(dd, "dln_tfp", ["rd_c", "gap_c", "rd_gap"])
    b = float(tt.loc[tt.term == "rd_gap", "beta"].iloc[0])
    loo.append({"dropped": c, "beta3": b})
loo_df = pd.DataFrame(loo)
save_table(loo_df, "D04_leave_one_out")
fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(loo_df.dropped, loo_df.beta3, marker="o")
ax.axhline(float(main.loc[main.term == "rd_gap", "beta"].iloc[0]), color="red", ls="--")
plt.xticks(rotation=90, fontsize=7)
style_axes(ax, title="β3 без одной страны", ylabel="beta3")
save_fig(fig, "D04_leave_one_out")

# %%
robust = [main]
# 5-year averages
p5 = (
    d[d.period5 != "other"]
    .groupby(["country_iso3", "period5"], as_index=False)
    .agg(dln_tfp=("dln_tfp", "mean"), rd_c=("rd_c", "mean"), gap_c=("gap_c", "mean"), rd_gap=("rd_gap", "mean"))
)
# use period FE instead of year: rename period5 to year for twfe helper
p5 = p5.rename(columns={"period5": "year"})
t = twfe(p5, "dln_tfp", ["rd_c", "gap_c", "rd_gap"])
t["spec"] = "five_year"
robust.append(t)

for yname, ycol in [("dln_lp", "dln_lp")]:
    dd = panel.dropna(subset=[ycol, "rd_c", "gap_c", "rd_gap"])
    t = twfe(dd, ycol, ["rd_c", "gap_c", "rd_gap"])
    t["spec"] = yname
    robust.append(t)

dd = d[d.year < 2020]
t = twfe(dd, "dln_tfp", ["rd_c", "gap_c", "rd_gap"])
t["spec"] = "pre2020"
robust.append(t)

dd = d[d.country_iso3 != "CHN"]
t = twfe(dd, "dln_tfp", ["rd_c", "gap_c", "rd_gap"])
t["spec"] = "no_chn"
robust.append(t)

far = ["COL", "MEX", "CRI", "CHL", "TUR"]
dd = d[~d.country_iso3.isin(far)]
t = twfe(dd, "dln_tfp", ["rd_c", "gap_c", "rd_gap"])
t["spec"] = "no_far_gap"
robust.append(t)

t = twfe(d, "dln_tfp", ["rd_c", "gap_c"])
t["spec"] = "no_interaction"
robust.append(t)

rob = pd.concat(robust, ignore_index=True)
save_table(rob, "D04_robustness")
save_table(main, "D04_main")
print("D04 done")

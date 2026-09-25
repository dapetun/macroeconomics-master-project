# %% [markdown]
# D03 — Функция производства знаний: R&D → патенты (H2)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import load_panel, save_table, save_fig, style_axes, twfe, within_demean

panel = load_panel().copy()
panel["ln_rd_x_chn"] = panel["ln_rd_ppp_lag1"] * panel["is_chn"]

# %%
specs = []
# main
d = panel.dropna(subset=["ln_pat_res", "ln_rd_ppp_lag1"])
t = twfe(d, "ln_pat_res", ["ln_rd_ppp_lag1"])
t["spec"] = "main_lag1"
specs.append(t)

# + researchers
d2 = panel.dropna(subset=["ln_pat_res", "ln_rd_ppp_lag1", "ln_researchers"])
t2 = twfe(d2, "ln_pat_res", ["ln_rd_ppp_lag1", "ln_researchers"])
t2["spec"] = "plus_researchers"
specs.append(t2)

# China interaction
d3 = panel.dropna(subset=["ln_pat_res", "ln_rd_ppp_lag1"])
t3 = twfe(d3, "ln_pat_res", ["ln_rd_ppp_lag1", "ln_rd_x_chn"])
t3["spec"] = "china_interact"
specs.append(t3)

# robustness variants
for lag, col in [(0, "ln_rd_ppp"), (2, None)]:
    dd = panel.copy()
    if lag == 2:
        dd["ln_rd_ppp_lag2"] = dd.groupby("country_iso3")["ln_rd_ppp"].shift(2)
        col = "ln_rd_ppp_lag2"
    dd = dd.dropna(subset=["ln_pat_res", col])
    tt = twfe(dd, "ln_pat_res", [col])
    tt["spec"] = f"lag{lag}"
    specs.append(tt)

for yvar, name in [("ln_pat_tot", "y_pat_tot"), ("ln_articles", "y_articles")]:
    dd = panel.dropna(subset=[yvar, "ln_rd_ppp_lag1"])
    tt = twfe(dd, yvar, ["ln_rd_ppp_lag1"])
    tt["spec"] = name
    specs.append(tt)

dd = panel[panel.country_iso3 != "CHN"].dropna(subset=["ln_pat_res", "ln_rd_ppp_lag1"])
tt = twfe(dd, "ln_pat_res", ["ln_rd_ppp_lag1"])
tt["spec"] = "no_chn"
specs.append(tt)

dd = panel[panel.year <= 2019].dropna(subset=["ln_pat_res", "ln_rd_ppp_lag1"])
tt = twfe(dd, "ln_pat_res", ["ln_rd_ppp_lag1"])
tt["spec"] = "to_2019"
specs.append(tt)

dd = panel.dropna(subset=["ln_pat_res", "ln_rd_stock_lag1"])
tt = twfe(dd, "ln_pat_res", ["ln_rd_stock_lag1"])
tt["spec"] = "rd_stock"
specs.append(tt)

all_specs = pd.concat(specs, ignore_index=True)
save_table(all_specs, "D03_all_specs")

# %%
# VIF for R&D and researchers
vif_df = d2[["ln_rd_ppp_lag1", "ln_researchers"]].dropna()
X = np.column_stack([np.ones(len(vif_df)), vif_df.values])
vifs = []
for i, name in enumerate(["const", "ln_rd_ppp_lag1", "ln_researchers"]):
    vifs.append({"term": name, "vif": float(variance_inflation_factor(X, i))})
save_table(pd.DataFrame(vifs), "D03_vif")

# coefplot for ln_rd terms
plot = all_specs[all_specs.term.str.contains("ln_rd")].copy()
fig, ax = plt.subplots(figsize=(8, 5))
y = np.arange(len(plot))
ax.errorbar(plot.beta, y, xerr=1.96 * plot.se, fmt="o", color="black")
ax.axvline(0, color="gray")
ax.set_yticks(y)
ax.set_yticklabels(plot.spec + " | " + plot.term, fontsize=8)
style_axes(ax, title="Эластичность патентов по R&D (разные спецификации)", xlabel="beta")
save_fig(fig, "D03_coefplot")

# within scatter
w = within_demean(
    d.dropna(subset=["ln_pat_res", "ln_rd_ppp_lag1"]),
    ["ln_pat_res", "ln_rd_ppp_lag1"],
    ["country_iso3", "year"],
)
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(w["ln_rd_ppp_lag1_within"], w["ln_pat_res_within"], s=8, alpha=0.4)
style_axes(ax, title="Within (после FE страны и года)", xlabel="ln R&D lag within", ylabel="ln patents within")
save_fig(fig, "D03_within_scatter")
print(all_specs[all_specs.spec == "main_lag1"])
print("D03 done")

# %% [markdown]
# D03 — Производство знаний: доля R&D и ВВП → патенты (H2)
# Knowledge production: R&D intensity and GDP → patents (H2)

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (
    apply_hse_style,  # noqa: E402
    load_panel, save_table, save_fig, style_axes, twfe, within_demean, NAVY, GRAY, BLUE,
)

apply_hse_style()

panel = load_panel().sort_values(["country_iso3", "year"]).copy()
panel["ln_rd_gdp_lag1"] = np.log(panel.groupby("country_iso3")["rd_gdp"].shift(1))
panel["ln_gdp_lag1"] = np.log(panel.groupby("country_iso3")["gdp_ppp"].shift(1))
X = ["ln_rd_gdp_lag1", "ln_gdp_lag1"]

# %%
specs = []
d_split = panel.dropna(subset=["ln_pat_res", *X])
t = twfe(d_split, "ln_pat_res", X)
t["spec"] = "main_split_intensity_gdp"
specs.append(t)

dd = panel[panel.country_iso3 != "CHN"].dropna(subset=["ln_pat_res", *X])
tt = twfe(dd, "ln_pat_res", X)
tt["spec"] = "no_chn"
specs.append(tt)

dd = panel.dropna(subset=["ln_articles", *X])
tt = twfe(dd, "ln_articles", X)
tt["spec"] = "y_articles"
specs.append(tt)

all_specs = pd.concat(specs, ignore_index=True)
save_table(all_specs, "D03_all_specs")

# %%
plot = all_specs[all_specs.term == "ln_rd_gdp_lag1"].copy()
spec_labels = {
    "main_split_intensity_gdp": "Основная: патенты",
    "no_chn": "Без Китая: патенты",
    "y_articles": "Статьи",
}
fig, ax = plt.subplots(figsize=(6.4, 3.4))
y = np.arange(len(plot))
ax.errorbar(plot.beta, y, xerr=1.96 * plot.se, fmt="o", color=NAVY, ms=8, capsize=4, elinewidth=1.6)
ax.axvline(0, color=GRAY)
ax.set_yticks(y)
ax.set_yticklabels([spec_labels.get(s, s) for s in plot.spec])
style_axes(ax, xlabel="коэффициент")
save_fig(fig, "D03_coefplot")

w = within_demean(d_split, ["ln_pat_res", "ln_rd_gdp_lag1"], ["country_iso3", "year"])
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.scatter(w["ln_rd_gdp_lag1_within"], w["ln_pat_res_within"], s=22, alpha=0.45, color=BLUE, edgecolors="none")
style_axes(ax, xlabel="логарифм доли R&D, лаг 1 год", ylabel="логарифм патентов")
save_fig(fig, "D03_within_scatter")
print(all_specs)
print("D03 done")

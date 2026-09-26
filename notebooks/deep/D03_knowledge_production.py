# %% [markdown]
# D03 — Функция производства знаний: доля R&D и ВВП → патенты (H2)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import load_panel, save_table, save_fig, style_axes, twfe, within_demean

panel = load_panel().copy()
panel = panel.sort_values(["country_iso3", "year"])
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
fig, ax = plt.subplots(figsize=(8, 3.2))
y = np.arange(len(plot))
ax.errorbar(plot.beta, y, xerr=1.96 * plot.se, fmt="o", color="black")
ax.axvline(0, color="gray")
ax.set_yticks(y)
ax.set_yticklabels(plot.spec, fontsize=9)
style_axes(ax, title="Эластичность по доле R&D (лаг 1), при контроле ВВП", xlabel="beta")
save_fig(fig, "D03_coefplot")

w = within_demean(d_split, ["ln_pat_res", "ln_rd_gdp_lag1"], ["country_iso3", "year"])
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(w["ln_rd_gdp_lag1_within"], w["ln_pat_res_within"], s=8, alpha=0.4)
style_axes(
    ax,
    title="Within: патенты и доля R&D",
    xlabel="ln(доля R&D), лаг 1, within",
    ylabel="ln patents within",
)
save_fig(fig, "D03_within_scatter")
print(all_specs)
print("D03 done")

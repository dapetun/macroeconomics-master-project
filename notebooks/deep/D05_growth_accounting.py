# %% [markdown]
# D05 — Разложение роста по Солоу (H4) / Solow growth accounting (H4)

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (
    apply_hse_style,  # noqa: E402
    load_panel, save_table, save_fig, style_axes, NAVY, BLUE, ORANGE, FOCUS_SERIES,
)

apply_hse_style()

panel = load_panel().sort_values(["country_iso3", "year"]).copy()
g = panel.groupby("country_iso3", group_keys=False)

# Лог-разности факторов / Log-differences of factors
for col, src in [("g_Y", "rgdpna"), ("g_K", "rnna"), ("g_L", "emp"), ("g_h", "hc")]:
    panel[col] = g[src].transform(lambda s: np.log(s).diff())
panel["labsh_avg"] = (panel["labsh"] + g["labsh"].shift(1)) / 2
panel["alpha"] = 1 - panel["labsh_avg"]
panel["contrib_K"] = panel["alpha"] * panel["g_K"]
panel["contrib_Lh"] = (1 - panel["alpha"]) * (panel["g_L"] + panel["g_h"])
panel["g_A"] = panel["g_Y"] - panel["contrib_K"] - panel["contrib_Lh"]
panel["dln_rtfpna"] = g["rtfpna"].transform(lambda s: np.log(s).diff())

# %%
corr = panel[["g_A", "dln_rtfpna"]].dropna().corr().iloc[0, 1]
print("corr g_A vs dln_rtfpna", corr)
save_table(pd.DataFrame([{"corr_gA_dln_rtfpna": corr}]), "D05_tfp_check")

periods = [(2001, 2007), (2008, 2012), (2013, 2019), (2020, 2023)]
countries = ["USA", "CHN", "KOR", "JPN", "DEU"]
rows = []
for c in countries:
    for y0, y1 in periods:
        sub = panel[(panel.country_iso3 == c) & (panel.year >= y0) & (panel.year <= y1)]
        if sub[["g_Y", "contrib_K", "contrib_Lh", "g_A"]].dropna().empty:
            continue
        m = sub[["g_Y", "contrib_K", "contrib_Lh", "g_A"]].mean()
        rows.append({
            "country_iso3": c,
            "period": f"{y0}-{y1}",
            "g_Y": float(m["g_Y"]),
            "contrib_K": float(m["contrib_K"]),
            "contrib_Lh": float(m["contrib_Lh"]),
            "g_A": float(m["g_A"]),
            "tfp_share": float(m["g_A"] / m["g_Y"]) if m["g_Y"] else np.nan,
        })
dec = pd.DataFrame(rows)
for c in ["g_Y", "contrib_K", "contrib_Lh", "g_A"]:
    dec[f"{c}_pp"] = dec[c] * 100
dec["capital_share_of_growth"] = dec["contrib_K"] / dec["g_Y"]
save_table(dec, "D05_decomposition")
save_table(dec[["country_iso3", "period", "tfp_share"]], "D05_tfp_share")

# %%
fig, axes = plt.subplots(1, 2, figsize=(6.4, 4.2), sharey=True)
for ax, (code, _col, title) in zip(axes, FOCUS_SERIES):
    s = dec[dec.country_iso3 == code]
    x = np.arange(len(s))
    ax.bar(x, s.contrib_K * 100, label="капитал", color=NAVY)
    ax.bar(x, s.contrib_Lh * 100, bottom=s.contrib_K * 100, label="труд и образование", color=BLUE)
    ax.bar(
        x,
        s.g_A * 100,
        bottom=(s.contrib_K + s.contrib_Lh) * 100,
        label="производительность",
        color=ORANGE,
    )
    ax.set_xticks(x)
    ax.set_xticklabels(s.period, rotation=25, ha="right")
    style_axes(ax, xlabel=title, ylabel="процентные пункты в год")
axes[0].legend(loc="upper left")
axes[1].legend().remove()
save_fig(fig, "D05_decomposition_bars")
print(dec[dec.country_iso3.isin(["USA", "CHN"])])
print("D05 done")

# %% [markdown]
# D00 — Аудит панели OECD+China / OECD+China panel audit

# %%
from pathlib import Path
import sys

import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (
    apply_hse_style,  # noqa: E402
    ROOT, load_panel, save_table, save_fig, style_axes,
    VAR_LABELS_SHORT, CMAP_NAVY, NAVY, FIGSIZE_SQUARE,
)

apply_hse_style()

panel = load_panel()
print(panel.shape, panel["country_iso3"].nunique(), panel["year"].min(), panel["year"].max())

# %%
key_vars = [
    "rd_gdp", "researchers_pm", "articles", "pat_res", "mva_share", "hitech_share",
    "gdppc_ppp", "rtfpna", "ctfp", "rd_ppp", "dln_tfp", "gap",
]
# Число непустых наблюдений по стране / Non-missing counts by country
cov = panel.groupby("country_iso3")[key_vars].count().reset_index()
save_table(cov, "D00_coverage")
print(cov.set_index("country_iso3")[key_vars].describe().T[["min", "50%", "max"]])

# %%
miss = panel.set_index(["country_iso3", "year"])[key_vars].isna()
heat = miss.groupby("country_iso3").mean()
fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)
im = ax.imshow(heat.values, aspect="auto", cmap=CMAP_NAVY, vmin=0, vmax=1)
ax.set_yticks(range(len(heat.index)))
ax.set_yticklabels(heat.index, fontsize=8)
ax.set_xticks(range(len(heat.columns)))
ax.set_xticklabels([VAR_LABELS_SHORT.get(c, c) for c in heat.columns], rotation=40, ha="right", fontsize=10)
style_axes(ax)
ax.grid(False)
cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
cbar.ax.tick_params(labelsize=10, colors=NAVY)
cbar.outline.set_edgecolor(NAVY)
save_fig(fig, "D00_missing_heatmap")

# %%
# Сверка с панелью 8 стран (legacy). / Compare with 8-country legacy panel.
old = pd.read_csv(ROOT / "data" / "deep" / "legacy" / "core_panel_reviewed.csv")
old = old[old["country_iso3"].isin(["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"])]
rename = {
    "gerd_pct_gdp": "rd_gdp",
    "researchers_per_million": "researchers_pm",
    "scopus_articles": "articles",
    "patents_resident": "pat_res",
    "mva_pct_gdp": "mva_share",
    "hitech_export_share": "hitech_share",
    "tfp_ctfp": "ctfp",
}
old = old.rename(columns={**rename, "gdp_pc_ppp": "gdppc_ppp"})
rows = []
for v in ["rd_gdp", "researchers_pm", "articles", "pat_res", "mva_share", "hitech_share", "gdppc_ppp", "ctfp"]:
    if v not in old.columns or v not in panel.columns:
        rows.append({"var": v, "n": 0, "maxabs": None, "meanabs": None, "note": "column missing"})
        continue
    m = old[["country_iso3", "year", v]].merge(
        panel[["country_iso3", "year", v]], on=["country_iso3", "year"], suffixes=("_old", "_new")
    ).dropna()
    if m.empty:
        continue
    diff = (m[f"{v}_old"] - m[f"{v}_new"]).abs()
    rows.append({"var": v, "n": len(m), "maxabs": float(diff.max()), "meanabs": float(diff.mean())})
cmp = pd.DataFrame(rows)
save_table(cmp, "D00_compare_old_panel")
print(cmp)

# %%
g = panel.groupby("country_iso3")["dln_tfp"].agg(["mean", "std", "count"])
print(g.loc[["USA", "CHN"]])
outliers = panel.loc[panel["dln_tfp"].abs() > 10, ["country_iso3", "year", "dln_tfp"]]
save_table(outliers, "D00_tfp_outliers")
print("outliers", len(outliers))
print("D00 done")

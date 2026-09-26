# %% [markdown]
# D00 — Аудит панели OECD+China

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import load_panel, save_table, save_fig, style_axes, COUNTRIES

panel = load_panel()
print(panel.shape, panel["country_iso3"].nunique(), panel["year"].min(), panel["year"].max())

# %%
key_vars = [
    "rd_gdp", "researchers_pm", "articles", "pat_res", "mva_share", "hitech_share",
    "gdppc_ppp", "rtfpna", "ctfp", "rd_ppp", "dln_tfp", "gap",
]
cov = panel.groupby("country_iso3")[key_vars].apply(lambda d: d.notna().sum()).reset_index()
save_table(cov, "D00_coverage")
print(cov.set_index("country_iso3")[key_vars].describe().T[["min", "50%", "max"]])

# %%
miss = panel.set_index(["country_iso3", "year"])[key_vars].isna()
heat = miss.groupby("country_iso3").mean()
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(heat.values, aspect="auto", cmap="Reds", vmin=0, vmax=1)
ax.set_yticks(range(len(heat.index)))
ax.set_yticklabels(heat.index, fontsize=7)
ax.set_xticks(range(len(heat.columns)))
ax.set_xticklabels(heat.columns, rotation=90, fontsize=8)
style_axes(ax, title="Доля пропусков по странам и переменным")
fig.colorbar(im, ax=ax, fraction=0.03)
save_fig(fig, "D00_missing_heatmap")

# %%
# Bridge to 20pp 8-country panel (kept under data/deep/legacy; full corpus on report-20pp)
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

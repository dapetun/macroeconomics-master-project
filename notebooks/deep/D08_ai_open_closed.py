# %% [markdown]
# D08 — ИИ: снимок notable models (без регрессии открытости)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import save_table, save_fig, style_axes, COLOR_USA, COLOR_CHN

epoch = pd.read_csv(ROOT / "data" / "raw" / "deep" / "epoch" / "notable_ai_models_latest.csv")

# %%
df = epoch.copy()
df["date"] = pd.to_datetime(df["Publication date"], errors="coerce")
df["year"] = df["date"].dt.year
df = df[(df["year"] >= 2015) & (df["year"] <= 2025)].copy()
country = df["Country (of organization)"].fillna("").astype(str)

def country_group(s: str) -> str:
    parts = [p.strip() for p in s.split(",") if p.strip()]
    # collapse duplicates
    uniq = set()
    for p in parts:
        if "United States" in p or p == "USA":
            uniq.add("USA")
        elif "China" in p:
            uniq.add("CHN")
        else:
            uniq.add("OTHER")
    if uniq == {"USA"}:
        return "USA_only"
    if uniq == {"CHN"}:
        return "CHN_only"
    if "USA" in uniq and "CHN" in uniq:
        return "US_CN_joint"
    if "USA" in uniq:
        return "USA_mixed"
    if "CHN" in uniq:
        return "CHN_mixed"
    return "OTHER"

df["cgroup"] = country.map(country_group)

OPEN = {
    "Open weights (unrestricted)",
    "Open weights (non-commercial)",
    "Open weights (restricted use)",
}
CLOSED = {"API access", "Hosted access (no API)", "Unreleased", "Limited access"}
acc = df["Model accessibility"].astype(str)
df["open"] = np.where(acc.isin(OPEN), 1, np.where(acc.isin(CLOSED), 0, np.nan))
df["frontier"] = df.get("Frontier model", pd.Series(index=df.index)).astype(str).str.lower().isin(["true", "yes", "1"])
df["log_compute"] = np.log10(pd.to_numeric(df["Training compute (FLOP)"], errors="coerce"))
org = df["Organization categorization"].fillna("").astype(str)
df["org_type"] = np.where(org.str.contains("Industry") & org.str.contains("Academia"), "mixed",
                   np.where(org.str.contains("Industry"), "Industry",
                   np.where(org.str.contains("Academia"), "Academia", "Other")))
df["domain"] = df["Domain"].fillna("Unknown").astype(str)
df["organization"] = df["Organization"].fillna("Unknown").astype(str)

# %%
desc = (
    df[df.cgroup.isin(["USA_only", "CHN_only"])]
    .groupby(["year", "cgroup"])
    .agg(
        n=("Model", "count"),
        open_share=("open", "mean"),
        n_frontier=("frontier", "sum"),
        max_compute=("log_compute", "max"),
        med_compute=("log_compute", "median"),
    )
    .reset_index()
)
save_table(desc, "D08_descriptives")

fig, ax = plt.subplots(figsize=(8, 4))
for g, col, lab in [("USA_only", COLOR_USA, "USA"), ("CHN_only", COLOR_CHN, "CHN")]:
    s = desc[desc.cgroup == g]
    ax.plot(s.year, s.open_share * 100, color=col, marker="o", label=lab)
style_axes(ax, title="Доля открытых весов среди notable models", ylabel="%")
ax.legend()
save_fig(fig, "D08_open_share")

fig, ax = plt.subplots(figsize=(8, 4))
for g, col, lab in [("USA_only", COLOR_USA, "USA"), ("CHN_only", COLOR_CHN, "CHN")]:
    s = desc[desc.cgroup == g]
    ax.plot(s.year, s.n, color=col, marker="o", label=lab)
style_axes(ax, title="Число notable models", ylabel="count")
ax.legend()
save_fig(fig, "D08_counts_by_country")

fig, ax = plt.subplots(figsize=(8, 4))
for g, col, lab in [("USA_only", COLOR_USA, "USA"), ("CHN_only", COLOR_CHN, "CHN")]:
    s = desc[desc.cgroup == g]
    ax.plot(s.year, s.max_compute, color=col, marker="o", label=lab)
style_axes(ax, title="Макс. log10(training compute)", ylabel="log10 FLOP")
ax.legend()
save_fig(fig, "D08_max_compute")
print(desc.groupby("cgroup")[["n", "open_share"]].mean())
print("D08 done")

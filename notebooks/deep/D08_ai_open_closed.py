# %% [markdown]
# D08 — ИИ: снимок notable models (без регрессии открытости)
# AI: Epoch notable-models snapshot (no openness regression)

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (
    apply_hse_style,  # noqa: E402
    RAW_DEEP, save_table, save_fig, style_axes, FIGSIZE, FOCUS_CGROUP, year_ticks,
)

apply_hse_style()

epoch = pd.read_csv(RAW_DEEP / "epoch" / "notable_ai_models_latest.csv")

# %%
df = epoch.copy()
df["date"] = pd.to_datetime(df["Publication date"], errors="coerce")
df["year"] = df["date"].dt.year
df = df[(df["year"] >= 2015) & (df["year"] <= 2025)].copy()
country = df["Country (of organization)"].fillna("").astype(str)


def country_group(s: str) -> str:
    parts = [p.strip() for p in s.split(",") if p.strip()]
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

# Три однотипных ряда США/Китай / Three parallel USA/China series
for ycol, ylabel, fname, scale in [
    ("open_share", "%", "D08_open_share", 100.0),
    ("n", "число", "D08_counts_by_country", 1.0),
    ("max_compute", "log10", "D08_max_compute", 1.0),
]:
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for g, col, lab in FOCUS_CGROUP:
        s = desc[desc.cgroup == g]
        ax.plot(s.year, s[ycol] * scale, color=col, marker="o", label=lab)
    style_axes(ax, ylabel=ylabel)
    if fname == "D08_open_share":
        year_ticks(ax, range(int(desc["year"].min()), int(desc["year"].max()) + 1), rotation=28)
    ax.legend()
    save_fig(fig, fname)

print(desc.groupby("cgroup")[["n", "open_share"]].mean())
print("D08 done")

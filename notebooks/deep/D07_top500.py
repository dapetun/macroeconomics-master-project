# %% [markdown]
# D07 — TOP500 2010–2025 (H6)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import save_table, save_fig, style_axes, COLOR_USA, COLOR_CHN

raw = pd.read_csv(ROOT / "data" / "raw" / "deep" / "top500" / "top500_all.csv", low_memory=False)

# %%
# Normalize columns
cols = {c: c.strip() for c in raw.columns}
df = raw.rename(columns=cols)
# find rmax column
rmax_col = [c for c in df.columns if "Rmax" in c][0]
country_col = "Country" if "Country" in df.columns else [c for c in df.columns if c.lower() == "country"][0]
accel_col = [c for c in df.columns if "Accelerator" in c and "Co-Processor" in c]
accel_col = accel_col[0] if accel_col else None
proc_col = "Processor" if "Processor" in df.columns else None
seg_col = "Segment" if "Segment" in df.columns else None
first_col = "First Appearance" if "First Appearance" in df.columns else None

df["country"] = df[country_col].astype(str)
df["rmax"] = pd.to_numeric(df[rmax_col], errors="coerce")
# if median suspiciously small for recent years, might be GFlops — scale check
med_2020 = df.loc[df.list_year == 2020, "rmax"].median()
if med_2020 < 100:  # likely GFlop/s
    df["rmax"] = df["rmax"] / 1000.0

# map country names to USA/China/other
def map_c(x: str) -> str:
    x = x.strip()
    if x in {"United States", "USA", "U.S.A.", "U.S."}:
        return "USA"
    if x in {"China", "People's Republic of China"}:
        return "CHN"
    return x

df["iso"] = df["country"].map(map_c)

def arch_row(row) -> str:
    a = str(row[accel_col]) if accel_col else ""
    p = str(row[proc_col]) if proc_col else ""
    text = (a + " " + p).lower()
    if any(k in text for k in ["matrix-2000", "sunway", "phytium", "hygon", "sw26010", "ft-"]):
        return "Chinese_indigenous"
    if "nvidia" in text or "tesla" in text or "a100" in text or "h100" in text or "v100" in text:
        return "NVIDIA"
    if "amd" in text or "instinct" in text or "mi250" in text or "mi300" in text:
        return "AMD"
    if "xeon phi" in text or "knl" in text:
        return "Intel_Phi"
    if a in {"nan", "None", ""} or "none" in a.lower():
        return "No_accelerator"
    return "Other_accel"

df["arch"] = df.apply(arch_row, axis=1)

# %%
agg = (
    df.groupby(["list_year", "iso"])
    .agg(n_systems=("rmax", "size"), rmax_sum=("rmax", "sum"))
    .reset_index()
)
tot = agg.groupby("list_year").agg(n_tot=("n_systems", "sum"), rmax_tot=("rmax_sum", "sum"))
agg = agg.merge(tot, on="list_year")
agg["share_systems"] = agg["n_systems"] / agg["n_tot"]
agg["share_rmax"] = agg["rmax_sum"] / agg["rmax_tot"]
save_table(agg, "D07_shares")

focus = agg[agg.iso.isin(["USA", "CHN"])]
fig, ax = plt.subplots(figsize=(8, 4))
for c, col in [("USA", COLOR_USA), ("CHN", COLOR_CHN)]:
    s = focus[focus.iso == c]
    ax.plot(s.list_year, s.share_systems * 100, color=col, label=f"{c} systems")
    ax.plot(s.list_year, s.share_rmax * 100, color=col, ls="--", label=f"{c} Rmax")
style_axes(ax, title="Доли TOP500: число систем vs мощность", ylabel="%")
ax.legend(fontsize=8)
save_fig(fig, "D07_share_systems_vs_rmax")

# new entries
if first_col:
    df["is_new"] = df[first_col].astype(str).str.contains(df["list_year"].astype(str), regex=False)
    # First Appearance often like 11/2020
    def is_new(row):
        fa = str(row[first_col])
        return str(row["list_year"]) in fa

    df["is_new"] = df.apply(is_new, axis=1)
    neu = df[df.is_new].groupby(["list_year", "iso"]).size().reset_index(name="n_new")
    save_table(neu, "D07_new_entries")
    fig, ax = plt.subplots(figsize=(8, 3.5))
    for c, col in [("USA", COLOR_USA), ("CHN", COLOR_CHN)]:
        s = neu[neu.iso == c]
        ax.plot(s.list_year, s.n_new, color=col, marker="o", label=c)
    style_axes(ax, title="Новые системы в ноябрьском списке", ylabel="count")
    ax.legend()
    save_fig(fig, "D07_new_entries")

# architecture top50
top50 = df[df["Rank"].astype(float) <= 50] if "Rank" in df.columns else df
arch = top50.groupby(["list_year", "iso", "arch"]).size().reset_index(name="n")
save_table(arch, "D07_architecture_top50")
arch_focus = arch[arch.iso.isin(["USA", "CHN"])]
fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, c in zip(axes, ["USA", "CHN"]):
    s = arch_focus[arch_focus.iso == c]
    pivot = s.pivot_table(index="list_year", columns="arch", values="n", aggfunc="sum").fillna(0)
    pivot.plot(kind="bar", stacked=True, ax=ax, legend=(c == "USA"))
    style_axes(ax, title=f"Архитектура топ-50: {c}")
save_fig(fig, "D07_architecture_top50")

# exascale
exa = df[df.rmax >= 1_000_000][["list_year", "iso", "Name" if "Name" in df.columns else country_col, "rmax", "arch"]]
save_table(exa, "D07_exascale_table")

if seg_col:
    seg = df.groupby(["list_year", "iso", seg_col]).size().reset_index(name="n")
    save_table(seg, "D07_segments")

print("D07 done", focus.groupby("iso")["share_systems"].last())

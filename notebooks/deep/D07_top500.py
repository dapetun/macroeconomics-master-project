# %% [markdown]
# D07 — TOP500 2010–2025 (H6) / TOP500 2010–2025 (H6)

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import (  # noqa: E402
    RAW_DEEP, save_table, save_fig, style_axes, SERIES, FIGSIZE,
    FOCUS_SERIES, ARCH_ORDER, ARCH_LABEL, plot_observed, year_ticks,
    pick_accel_column, apply_hse_style,
)

apply_hse_style()
raw = pd.read_csv(RAW_DEEP / "top500" / "top500_all.csv", low_memory=False)

# %%
df = raw.rename(columns={c: c.strip() for c in raw.columns})
country_col = "Country" if "Country" in df.columns else next(c for c in df.columns if c.lower() == "country")
# Имя ускорителя, не «Cores»: иначе Matrix-2000 теряется. / Prefer accelerator name over Cores count.
accel_col = pick_accel_column(df.columns)
proc_col = "Processor" if "Processor" in df.columns else None
seg_col = "Segment" if "Segment" in df.columns else None
first_col = "First Appearance" if "First Appearance" in df.columns else None

df["country"] = df[country_col].astype(str)
gf = pd.to_numeric(df["RMax"], errors="coerce").fillna(pd.to_numeric(df["Rmax"], errors="coerce"))
tf = pd.to_numeric(df["Rmax [TFlop/s]"], errors="coerce")
# 2010–2015: GFlop/s; 2019+: TFlop/s / Early lists in GFlop/s; later in TFlop/s
df["rmax"] = tf.fillna(gf / 1000.0)


def map_c(x: str) -> str:
    x = x.strip()
    if x in {"United States", "USA", "U.S.A.", "U.S."}:
        return "USA"
    if x in {"China", "People's Republic of China"}:
        return "CHN"
    return x


df["iso"] = df["country"].map(map_c)

# Векторная классификация ускорителя / Vectorized accelerator classification
accel = df[accel_col].astype(str) if accel_col else pd.Series("", index=df.index)
proc = df[proc_col].astype(str) if proc_col else pd.Series("", index=df.index)
text = (accel + " " + proc).str.lower()
df["arch"] = np.select(
    [
        text.str.contains("matrix-2000|sunway|phytium|hygon|sw26010|ft-", regex=True),
        text.str.contains("nvidia|tesla|a100|h100|v100", regex=True),
        text.str.contains("amd|instinct|mi250|mi300", regex=True),
        text.str.contains("xeon phi|knl", regex=True),
        accel.isin({"nan", "None", ""}) | accel.str.lower().str.contains("none", regex=False),
    ],
    ["Chinese_indigenous", "NVIDIA", "AMD", "Intel_Phi", "No_accelerator"],
    default="Other_accel",
)

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
fig, ax = plt.subplots(figsize=FIGSIZE)
for code, col, name in FOCUS_SERIES:
    s = focus[focus.iso == code].sort_values("list_year")
    plot_observed(ax, s.list_year, s.share_systems * 100, color=col, marker="o", label=f"{name}, число систем")
    plot_observed(ax, s.list_year, s.share_rmax * 100, color=col, ls="--", marker="s", label=f"{name}, мощность")
style_axes(ax, ylabel="%")
year_ticks(ax, focus.list_year.unique())
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
save_fig(fig, "D07_share_systems_vs_rmax")

# Новые системы: год списка входит в First Appearance / New entries: list year appears in First Appearance
if first_col:
    df["is_new"] = [str(y) in str(fa) for y, fa in zip(df["list_year"], df[first_col])]
    neu = df[df.is_new].groupby(["list_year", "iso"]).size().reset_index(name="n_new")
    save_table(neu, "D07_new_entries")
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for code, col, name in FOCUS_SERIES:
        s = neu[neu.iso == code].sort_values("list_year")
        plot_observed(ax, s.list_year, s.n_new, color=col, marker="o", label=name)
    style_axes(ax, ylabel="число")
    handles, labels = ax.get_legend_handles_labels()
    if labels:
        ax.legend()
    save_fig(fig, "D07_new_entries")

top50 = df[df["Rank"].astype(float) <= 50] if "Rank" in df.columns else df
arch = top50.groupby(["list_year", "iso", "arch"]).size().reset_index(name="n")
save_table(arch, "D07_architecture_top50")
arch_focus = arch[arch.iso.isin(["USA", "CHN"])]
present = [a for a in ARCH_ORDER if a in set(arch_focus["arch"])]
fig, axes = plt.subplots(1, 2, figsize=(6.4, 4.8), sharey=True)
for ax, (code, _col, title) in zip(axes, FOCUS_SERIES):
    s = arch_focus[arch_focus.iso == code]
    pivot = (
        s.pivot_table(index="list_year", columns="arch", values="n", aggfunc="sum")
        .reindex(columns=present)
        .fillna(0)
        .rename(columns=ARCH_LABEL)
    )
    pivot.plot(kind="bar", stacked=True, ax=ax, color=SERIES[: len(present)], legend=False, width=0.8)
    style_axes(ax, title=title, ylabel="число" if code == "USA" else "")
    ax.tick_params(axis="x", labelrotation=25)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.0))
save_fig(fig, "D07_architecture_top50", tight_rect=(0, 0.18, 1, 1))

name_col = "Name" if "Name" in df.columns else country_col
exa = df[df.rmax >= 1_000_000][["list_year", "iso", name_col, "rmax", "arch"]].rename(columns={"rmax": "rmax_tflops"})
save_table(exa, "D07_exascale_table")

if seg_col:
    seg = df.groupby(["list_year", "iso", seg_col]).size().reset_index(name="n")
    save_table(seg, "D07_segments")

print("D07 done", focus.groupby("iso")["share_systems"].last())

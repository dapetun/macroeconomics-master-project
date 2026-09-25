# %% [markdown]
# D08 — ИИ: открытые vs закрытые модели (H7)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

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

# %%
m = df[df.cgroup.isin(["USA_only", "CHN_only"]) & df.open.notna()].copy()
m["is_chn"] = (m.cgroup == "CHN_only").astype(int)
# LPM with FE
res = smf.ols(
    "open ~ is_chn + C(year) + C(domain) + C(org_type)", data=m
).fit(cov_type="cluster", cov_kwds={"groups": m["organization"]})
out = pd.DataFrame([{
    "term": "is_chn",
    "beta": float(res.params["is_chn"]),
    "se": float(res.bse["is_chn"]),
    "p": float(res.pvalues["is_chn"]),
    "N": int(res.nobs),
    "spec": "LPM_main",
}])

# robustness
for name, subset in [
    ("language_only", m[m.domain.str.contains("Language", case=False, na=False)]),
    ("2020_2025", m[m.year >= 2020]),
]:
    if len(subset) < 30:
        continue
    r = smf.ols("open ~ is_chn + C(year) + C(domain) + C(org_type)", data=subset).fit(
        cov_type="cluster", cov_kwds={"groups": subset["organization"]}
    )
    out = pd.concat([out, pd.DataFrame([{
        "term": "is_chn", "beta": float(r.params["is_chn"]), "se": float(r.bse["is_chn"]),
        "p": float(r.pvalues["is_chn"]), "N": int(r.nobs), "spec": name,
    }])], ignore_index=True)

# drop top Chinese open orgs
top_cn = (
    m[(m.is_chn == 1) & (m.open == 1)]
    .groupby("organization").size().sort_values(ascending=False).head(3).index
)
m2 = m[~m.organization.isin(top_cn)]
r = smf.ols("open ~ is_chn + C(year) + C(domain) + C(org_type)", data=m2).fit(
    cov_type="cluster", cov_kwds={"groups": m2["organization"]}
)
out = pd.concat([out, pd.DataFrame([{
    "term": "is_chn", "beta": float(r.params["is_chn"]), "se": float(r.bse["is_chn"]),
    "p": float(r.pvalues["is_chn"]), "N": int(r.nobs), "spec": "drop_top3_cn_open",
}])], ignore_index=True)

save_table(out, "D08_lpm")
fig, ax = plt.subplots(figsize=(7, 3.5))
y = np.arange(len(out))
ax.errorbar(out.beta, y, xerr=1.96 * out.se, fmt="o")
ax.axvline(0, color="gray")
ax.set_yticks(y)
ax.set_yticklabels(out.spec)
style_axes(ax, title="LPM: P(open) и индикатор Китая", xlabel="beta (п.п.)")
save_fig(fig, "D08_lpm_coef")
print(out)
print("D08 done")

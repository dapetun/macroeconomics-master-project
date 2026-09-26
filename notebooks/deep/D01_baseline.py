# %% [markdown]
# D01 — Baseline: воспроизведение M1 и лестница спецификаций

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS, RandomEffects

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import load_panel, save_table, twfe, coef_table

# %%
# Reproduce old M1 on reviewed 8-country panel
old = pd.read_csv(ROOT / "data_reviewed" / "core_panel_reviewed.csv")
old = old.sort_values(["country_iso3", "year"])
old["gerd_lag1"] = old.groupby("country_iso3")["gerd_pct_gdp"].shift(1)
old["lres"] = np.log(old["researchers_per_million"])
est = old.dropna(subset=["tfp_ctfp", "gerd_lag1", "lres"]).copy()
est = est[(est["country_iso3"] != "ISR") & (est["year"] >= 2011) & (est["year"] <= 2023)]
res_old = smf.ols(
    "tfp_ctfp ~ gerd_lag1 + lres + C(country_iso3) + C(year)", data=est
).fit(cov_type="HC1")
m1_rep = coef_table(res_old, ["gerd_lag1", "lres"], G=est["country_iso3"].nunique())
m1_rep["note"] = "replication HC1 on core_panel_reviewed 2011-2023; expect gerd~0.027"
save_table(m1_rep, "D01_m1_replication")
print(m1_rep)

# %%
panel = load_panel().copy()
panel = panel.dropna(subset=["dln_tfp", "rd_gdp_lag1"]).copy()
ladder_rows = []

# (1) old M1 beta already stored
ladder_rows.append({
    "spec": "1_old_M1_ctfp_8countries",
    "y": "ctfp",
    "beta_rd": float(m1_rep.loc[m1_rep.term == "gerd_lag1", "beta"].iloc[0]),
    "se": float(m1_rep.loc[m1_rep.term == "gerd_lag1", "se"].iloc[0]),
    "p": float(m1_rep.loc[m1_rep.term == "gerd_lag1", "p"].iloc[0]),
    "N": int(m1_rep.loc[m1_rep.term == "gerd_lag1", "N"].iloc[0]),
    "G": int(m1_rep.loc[m1_rep.term == "gerd_lag1", "G"].iloc[0]),
})

# (2) pooled ln ctfp
d2 = panel.dropna(subset=["ctfp", "rd_gdp_lag1"]).copy()
d2["ln_ctfp"] = np.log(d2["ctfp"])
r2 = smf.ols("ln_ctfp ~ rd_gdp_lag1", data=d2).fit(
    cov_type="cluster", cov_kwds={"groups": d2["country_iso3"]}
)
ladder_rows.append({
    "spec": "2_pooled_ln_ctfp",
    "y": "ln_ctfp",
    "beta_rd": float(r2.params["rd_gdp_lag1"]),
    "se": float(r2.bse["rd_gdp_lag1"]),
    "p": float(r2.pvalues["rd_gdp_lag1"]),
    "N": int(r2.nobs),
    "G": int(d2["country_iso3"].nunique()),
})

# (3) pooled dln_tfp
r3 = smf.ols("dln_tfp ~ rd_gdp_lag1", data=panel).fit(
    cov_type="cluster", cov_kwds={"groups": panel["country_iso3"]}
)
ladder_rows.append({
    "spec": "3_pooled_dln_tfp",
    "y": "dln_tfp",
    "beta_rd": float(r3.params["rd_gdp_lag1"]),
    "se": float(r3.bse["rd_gdp_lag1"]),
    "p": float(r3.pvalues["rd_gdp_lag1"]),
    "N": int(r3.nobs),
    "G": int(panel["country_iso3"].nunique()),
})

# (4) country FE
r4 = smf.ols("dln_tfp ~ rd_gdp_lag1 + C(country_iso3)", data=panel).fit(
    cov_type="cluster", cov_kwds={"groups": panel["country_iso3"]}
)
ladder_rows.append({
    "spec": "4_country_FE",
    "y": "dln_tfp",
    "beta_rd": float(r4.params["rd_gdp_lag1"]),
    "se": float(r4.bse["rd_gdp_lag1"]),
    "p": float(r4.pvalues["rd_gdp_lag1"]),
    "N": int(r4.nobs),
    "G": int(panel["country_iso3"].nunique()),
})

# (5) TWFE
t5 = twfe(panel, "dln_tfp", ["rd_gdp_lag1"])
ladder_rows.append({
    "spec": "5_TWFE",
    "y": "dln_tfp",
    "beta_rd": float(t5.iloc[0]["beta"]),
    "se": float(t5.iloc[0]["se"]),
    "p": float(t5.iloc[0]["p"]),
    "N": int(t5.iloc[0]["N"]),
    "G": int(t5.iloc[0]["G"]),
})

# (6) TWFE + researchers
d6 = panel.dropna(subset=["ln_researchers"]).copy()
t6 = twfe(d6, "dln_tfp", ["rd_gdp_lag1", "ln_researchers"])
ladder_rows.append({
    "spec": "6_TWFE_plus_researchers",
    "y": "dln_tfp",
    "beta_rd": float(t6.loc[t6.term == "rd_gdp_lag1", "beta"].iloc[0]),
    "se": float(t6.loc[t6.term == "rd_gdp_lag1", "se"].iloc[0]),
    "p": float(t6.loc[t6.term == "rd_gdp_lag1", "p"].iloc[0]),
    "N": int(t6.loc[t6.term == "rd_gdp_lag1", "N"].iloc[0]),
    "G": int(t6.loc[t6.term == "rd_gdp_lag1", "G"].iloc[0]),
})

ladder = pd.DataFrame(ladder_rows)
save_table(ladder, "D01_ladder")
print(ladder)

# %%
# Classical Hausman: FE and RE with the same year dummies, non-robust covariance, 1 df
from scipy import stats

pdf = panel.set_index(["country_iso3", "year"])
exog = pdf[["rd_gdp_lag1"]].copy()
exog["const"] = 1.0
yr = pd.get_dummies(pdf.index.get_level_values("year"), prefix="y", drop_first=True, dtype=float)
yr.index = pdf.index
exog = pd.concat([exog, yr], axis=1)
y = pdf["dln_tfp"]
fe = PanelOLS(y, exog, entity_effects=True).fit()
re = RandomEffects(y, exog).fit()
b_fe, b_re = float(fe.params["rd_gdp_lag1"]), float(re.params["rd_gdp_lag1"])
v_fe, v_re = float(fe.cov.loc["rd_gdp_lag1", "rd_gdp_lag1"]), float(re.cov.loc["rd_gdp_lag1", "rd_gdp_lag1"])
diff_v = v_fe - v_re
hausman_stat = (b_fe - b_re) ** 2 / diff_v if diff_v > 0 else np.nan
haus = pd.DataFrame([{
    "beta_fe": b_fe, "beta_re": b_re, "var_fe": v_fe, "var_re": v_re,
    "hausman_stat": hausman_stat,
    "p_value": float(1 - stats.chi2.cdf(hausman_stat, 1)) if np.isfinite(hausman_stat) else np.nan,
    "note": "classical Hausman, year dummies in both FE and RE, non-robust cov; FE chosen on substantive grounds, not by this test",
}])
save_table(haus, "D01_hausman")
print(haus)
print("D01 done")

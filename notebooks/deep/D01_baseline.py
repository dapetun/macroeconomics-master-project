# %% [markdown]
# D01 — Лестница спецификаций для роста TFP / Specification ladder for TFP growth
#
# Y = рост TFP (`dln_tfp` из `rtfpna`). / Y = TFP growth (`dln_tfp` from `rtfpna`).
# `ctfp` не оценивается: уровень к США, не рост. / `ctfp` is a level vs USA, not growth.

# %%
from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import load_panel, save_table, twfe, ols_cluster  # noqa: E402

# %%
panel = load_panel().dropna(subset=["dln_tfp", "rd_gdp_lag1"]).copy()
ladder_rows = []

r3 = ols_cluster(panel, "dln_tfp ~ rd_gdp_lag1")
ladder_rows.append({
    "spec": "3_pooled_dln_tfp",
    "y": "dln_tfp",
    "beta_rd": float(r3.params["rd_gdp_lag1"]),
    "se": float(r3.bse["rd_gdp_lag1"]),
    "p": float(r3.pvalues["rd_gdp_lag1"]),
    "N": int(r3.nobs),
    "G": int(panel["country_iso3"].nunique()),
})

r4 = ols_cluster(panel, "dln_tfp ~ rd_gdp_lag1 + C(country_iso3)")
ladder_rows.append({
    "spec": "4_country_FE",
    "y": "dln_tfp",
    "beta_rd": float(r4.params["rd_gdp_lag1"]),
    "se": float(r4.bse["rd_gdp_lag1"]),
    "p": float(r4.pvalues["rd_gdp_lag1"]),
    "N": int(r4.nobs),
    "G": int(panel["country_iso3"].nunique()),
})

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
print("D01 done")

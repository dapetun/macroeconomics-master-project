# %% [markdown]
# D10 — Сводка устойчивости

# %%
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "results" / "deep" / "tables"

rows = []

def add(claim, table, term_filter, rule):
    p = T / table
    if not p.exists():
        rows.append({"claim": claim, "table": table, "status": "missing_table", "detail": ""})
        return
    df = pd.read_csv(p)
    rows.append({"claim": claim, "table": table, "status": "present", "detail": rule, "n_rows": len(df)})

add("H1 profile residuals", "D02_profile_2019_2023.csv", None, "sign pattern USA intensity vs CHN scale")
add("H2 split intensity", "D03_all_specs.csv", "main_split_intensity_gdp", "intensity and GDP entered separately")
add("H3 interaction beta3", "D04_robustness.csv", "rd_gap", "sign/significance across robustness")
add("H4 capital vs TFP shares", "D05_tfp_share.csv", None, "CHN TFP share < USA")
add("H5 China net importer", "D06_ic_trade_panel.csv", None, "ic_net<0 all years for CHN")
add("H6 TOP500 shares", "D07_shares.csv", None, "observed November lists only")
add("H7 descriptives only", "D08_descriptives.csv", None, "no regression; Epoch snapshot")

# Auto-evaluate a few
detail = []
# H5
ic = pd.read_csv(T / "D06_ic_trade_panel.csv")
chn = ic[ic.country_iso3 == "CHN"]
detail.append({"claim": "H5", "metric": "share_years_net_importer", "value": float((chn.ic_net < 0).mean())})
# H2
sp = pd.read_csv(T / "D03_all_specs.csv")
for spec in ["main_split_intensity_gdp", "no_chn", "y_articles"]:
    r = sp[(sp.spec == spec) & (sp.term == "ln_rd_gdp_lag1")]
    if len(r):
        detail.append({"claim": "H2", "metric": f"{spec}_ln_rd_gdp_lag1", "value": float(r.beta.iloc[0]), "p": float(r.p.iloc[0])})
# H3
rb = pd.read_csv(T / "D04_robustness.csv")
b3 = rb[(rb.spec == "main") & (rb.term == "rd_gap")]
if len(b3):
    detail.append({"claim": "H3", "metric": "beta3", "value": float(b3.beta.iloc[0]), "p": float(b3.p.iloc[0])})
b3_all = rb[rb.term == "rd_gap"]
detail.append({"claim": "H3", "metric": "n_specs_beta3_negative", "value": int((b3_all.beta < 0).sum()), "p": np.nan})
detail.append({"claim": "H3", "metric": "n_specs_total", "value": int(len(b3_all)), "p": np.nan})
b5 = rb[(rb.spec == "five_year") & (rb.term == "rd_gap")]
if len(b5):
    detail.append({"claim": "H3", "metric": "beta3_five_year", "value": float(b5.beta.iloc[0]), "p": float(b5.p.iloc[0])})
out = pd.DataFrame(rows)
out.to_csv(T / "D10_claims_robustness.csv", index=False)
pd.DataFrame(detail).to_csv(T / "D10_key_numbers.csv", index=False)
print(out)
print(pd.DataFrame(detail))
print("D10 done")

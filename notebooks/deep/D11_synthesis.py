# %% [markdown]
# D11 — Синтез результатов deep-research

# %%
from pathlib import Path
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import save_table

T = ROOT / "results" / "deep" / "tables"

claims = pd.DataFrame([
    {
        "H": "H1",
        "prediction": "CHN scale metrics above norm more than intensity; USA intensity above norm",
        "result": "CHN above norm on all six metrics; patents extreme (+811%); rd_gdp also +91%. USA near/below norm on intensity.",
        "verdict": "частично не согласуется / смешанно",
        "evidence": "D02_profile_2019_2023.csv",
        "type": "описательное",
    },
    {
        "H": "H2",
        "prediction": "b>0 for ln patents on ln R&D lag",
        "result": "beta≈0.995, p≈0.002, N=734, G=39; holds in several robustness specs",
        "verdict": "согласуется",
        "evidence": "D03_all_specs.csv",
        "type": "ассоциативное",
    },
    {
        "H": "H3",
        "prediction": "beta3 = R&D×gap > 0",
        "result": "beta3≈-0.45, p≈0.54; not significant across main robustness",
        "verdict": "не согласуется / неопределённо",
        "evidence": "D04_main.csv / D04_robustness.csv",
        "type": "ассоциативное",
    },
    {
        "H": "H4",
        "prediction": "CHN TFP share of growth < USA",
        "result": "Early periods CHN TFP share higher (e.g. 2001-07: 0.47 vs 0.29); 2020-23 CHN lower (0.30 vs 0.42)",
        "verdict": "частично не согласуется",
        "evidence": "D05_tfp_share.csv",
        "type": "описательное (учёт)",
    },
    {
        "H": "H5",
        "prediction": "CHN net IC importer; TW/KR sources; equipment NLD/JPN/USA",
        "result": "CHN ic_net<0 in 100% of 2010-2023 years; partner sum matches world M",
        "verdict": "согласуется (торговля)",
        "evidence": "D06_ic_trade_panel.csv",
        "type": "описательное",
    },
    {
        "H": "H6",
        "prediction": "CHN TOP500 share rises then falls after ~2019",
        "result": "systems share 0.08(2010)→0.46(2019)→0.08(2025); missing some list years",
        "verdict": "согласуется (при неполных списках)",
        "evidence": "D07_shares.csv",
        "type": "описательное",
    },
    {
        "H": "H7",
        "prediction": "Chinese notable models more often open",
        "result": "LPM is_chn beta≈0.25, p≈0.009; weakens if drop top-3 CN open orgs",
        "verdict": "согласуется (хрупко к составу организаций)",
        "evidence": "D08_lpm.csv",
        "type": "ассоциативное",
    },
])
save_table(claims, "D11_hypothesis_verdicts")

ladder = pd.DataFrame([
    {"level": 1, "claim": "наличие технологии / науки", "USA": "measured/snapshot", "CHN": "measured/snapshot", "strength": "средняя"},
    {"level": 2, "claim": "способность разработать", "USA": "frontier models/compute (Epoch)", "CHN": "open models volume", "strength": "средняя (снимки)"},
    {"level": 3, "claim": "способность производить", "USA": "equipment export (HS8486)", "CHN": "нет fab capacity; net IC importer", "strength": "слабая для fab"},
    {"level": 4, "claim": "масштабирование", "USA": "TOP500 GPU systems", "CHN": "MVA/hitech shares; TOP500 rise-fall", "strength": "средняя"},
    {"level": 5, "claim": "внедрение", "USA": "не измерено", "CHN": "не измерено", "strength": "нет данных"},
    {"level": 6, "claim": "экономический эффект", "USA": "growth accounting TFP share", "CHN": "growth accounting; R&D–TFP link not id.", "strength": "ограниченная"},
    {"level": 7, "claim": "экспорт", "USA": "IC/equipment trade", "CHN": "IC export large but net importer", "strength": "высокая (trade)"},
    {"level": 8, "claim": "долгосрочное преимущество", "USA": "не выводится", "CHN": "не выводится", "strength": "нет"},
])
save_table(ladder, "D11_claim_ladder")
print(claims[["H", "verdict"]].to_string(index=False))
print("D11 done")

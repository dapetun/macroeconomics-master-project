# %% [markdown]
# D11 — Синтез результатов / Synthesis of results

# %%
from pathlib import Path
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import TABLES, save_table  # noqa: E402

T = TABLES

# Preserve prediction/type from previous verdicts (do not rewrite hypotheses)
prev = pd.read_csv(T / "D11_hypothesis_verdicts.csv")
pred = prev.set_index("H")["prediction"].to_dict()
typ = prev.set_index("H")["type"].to_dict()
pred["H2"] = "beta1>0: patents on R&D intensity, controlling for GDP"
pred["H7"] = "not tested; Epoch snapshot of counts and open-weight shares"


def tbl(name):
    return pd.read_csv(T / f"{name}.csv")


def coef(df, spec, term):
    r = df[(df.spec == spec) & (df.term == term)]
    if r.empty:
        raise KeyError(f"{spec}/{term}")
    return float(r.beta.iloc[0]), float(r.p.iloc[0])


# H1
v = tbl("D02_profile_variants_2019_2023")


def dev(c, ind, var):
    return 100 * float(v[(v.country_iso3 == c) & (v.indicator == ind) & (v.variant == var)].pct_above.iloc[0])


chn_main = v[(v.country_iso3 == "CHN") & v.variant.isin(["with_pop", "without_pop"])]
chn_all_above = bool((chn_main.pct_above > 0).all())
usa_flip = np.sign(dev("USA", "rd_gdp", "with_pop")) != np.sign(dev("USA", "rd_gdp", "without_pop"))
h1_verdict = "смешанно; вывод о США зависит от спецификации нормы" if usa_flip else "смешанно"
h1_result = (
    f"CHN выше нормы по {'всем шести' if chn_all_above else 'не всем'} показателям в обоих вариантах нормы "
    f"(rd_gdp: {dev('CHN','rd_gdp','with_pop'):+.0f}% с населением, {dev('CHN','rd_gdp','without_pop'):+.0f}% без населения). "
    f"USA rd_gdp: {dev('USA','rd_gdp','with_pop'):+.0f}% с населением, {dev('USA','rd_gdp','without_pop'):+.0f}% без населения. "
    "Норма для CHN по населению — экстраполяция (D02_support_check)."
)

# H2 — split only (intensity and GDP). Volume R&D is not estimated.
sp = tbl("D03_all_specs")
b_int, p_int = coef(sp, "main_split_intensity_gdp", "ln_rd_gdp_lag1")
b_gdp, p_gdp = coef(sp, "main_split_intensity_gdp", "ln_gdp_lag1")
b_no, p_no = coef(sp, "no_chn", "ln_rd_gdp_lag1")
b_art, p_art = coef(sp, "y_articles", "ln_rd_gdp_lag1")
if b_int > 0 and p_int < 0.05:
    h2_verdict = "согласуется"
elif b_int > 0 and p_int < 0.10:
    h2_verdict = "неопределённо; связь с долей R&D слабая (p<0,10)"
else:
    h2_verdict = "не согласуется"
h2_result = (
    f"Патенты на долю R&D и ВВП (лаг 1): доля R&D β={b_int:.2f}, p={p_int:.3f}; ВВП β={b_gdp:.2f}, p={p_gdp:.3f}. "
    f"Без Китая доля R&D β={b_no:.2f}, p={p_no:.3f}. Статьи на ту же пару: доля R&D β={b_art:.2f}, p={p_art:.3f}."
)

# H3
rb = tbl("D04_robustness")
b3 = rb[rb.term == "rd_gap"]
b_m, p_m = coef(rb, "main", "rd_gap")
b_5, p_5 = coef(rb, "five_year", "rd_gap")
if b_m > 0 and p_m < 0.05:
    h3_verdict = "согласуется"
elif bool((b3.beta < 0).all()):
    h3_verdict = "не согласуется"
else:
    h3_verdict = "неопределённо"
h3_result = (
    f"β3 < 0 в {int((b3.beta < 0).sum())} из {len(b3)} спецификаций (основная {b_m:.2f}, p={p_m:.3f}); "
    f"в пятилетних средних {b_5:.2f}, p={p_5:.3f}. Коэффициент при gap_c не трактуется как догоняющий рост."
)

# H4
dec = tbl("D05_decomposition")
chn4 = dec[dec.country_iso3 == "CHN"].set_index("period")
usa4 = dec[dec.country_iso3 == "USA"].set_index("period")
lower = chn4.tfp_share < usa4.tfp_share
h4_verdict = "согласуется" if lower.all() else ("не согласуется" if not lower.any() else "частично не согласуется")
h4_result = (
    f"Вклады, п.п. в год: TFP CHN {chn4.loc['2001-2007','g_A_pp']:.1f} (2001–07) → {chn4.loc['2020-2023','g_A_pp']:.1f} (2020–23); "
    f"капитал CHN {chn4.contrib_K_pp.min():.1f}–{chn4.contrib_K_pp.max():.1f}; "
    f"USA: капитал {usa4.contrib_K_pp.min():.1f}–{usa4.contrib_K_pp.max():.1f}, TFP {usa4.g_A_pp.min():.1f}–{usa4.g_A_pp.max():.1f}. "
    "Доли TFP неустойчивы при росте около нуля; основное сравнение — в п.п."
)

# H5
ic = tbl("D06_ic_trade_panel")
eqt = tbl("D06_equipment_trade")
reimp = tbl("D06_china_reimport_2023")
src = tbl("D06_china_ic_sources_2023")
chn_ic = ic[ic.country_iso3 == "CHN"]
net_all = bool((chn_ic.ic_net < 0).all())
e23 = eqt[eqt.year == 2023].sort_values("value_usd", ascending=False).reset_index(drop=True)
has_usa = "USA" in set(eqt.country_iso3)
usa_rank = int(e23.index[e23.country_iso3 == "USA"][0]) + 1 if has_usa else None
usa_eq_bn = float(e23.loc[usa_rank - 1, "value_usd"]) / 1e9 if has_usa else None
if not has_usa:
    h5_verdict = "согласуется частично; часть про США не проверена (нет данных Comtrade по США)"
elif net_all and set(e23.country_iso3.head(3)) == {"USA", "NLD", "JPN"}:
    h5_verdict = "согласуется (торговля)"
elif net_all:
    h5_verdict = "согласуется частично (торговля)"
else:
    h5_verdict = "не согласуется"
tw_kr = float(src[src.partner_code.isin([490, 410])].value_usd.sum()) / float(reimp.total_m.iloc[0])
h5_result = (
    f"CHN — чистый импортёр микросхем в {int((chn_ic.ic_net < 0).sum())} из {len(chn_ic)} лет; "
    f"реимпорт (код 156) — {100 * float(reimp.reimport_share.iloc[0]):.0f}% импорта 2023; Тайвань+Корея — {100 * tw_kr:.0f}%. "
    + (f"США — {usa_rank}-е место по экспорту HS8486 в 2023 ({usa_eq_bn:.1f} млрд $). " if has_usa else "")
    + "RCA рассчитан относительно выборки OECD+Китай, не мира."
)

# H6
sh = tbl("D07_shares")
c6 = sh[sh.iso == "CHN"].sort_values("list_year").reset_index(drop=True)
viol = [int(y) for y in c6[c6.share_rmax >= c6.share_systems].list_year]
peak_i = int(c6.share_systems.idxmax())
rise_fall = c6.share_systems.iloc[0] < c6.share_systems.iloc[peak_i] > c6.share_systems.iloc[-1]
h6_verdict = ("согласуется" if not viol else "согласуется частично") if rise_fall else "не согласуется"
h6_result = (
    f"Доля CHN по числу систем: {c6.share_systems.iloc[0]:.2f} ({int(c6.list_year.iloc[0])}) → "
    f"{c6.share_systems.iloc[peak_i]:.2f} ({int(c6.list_year.iloc[peak_i])}) → {c6.share_systems.iloc[-1]:.2f} ({int(c6.list_year.iloc[-1])}). "
    f"Доля по мощности не ниже доли по числу систем в годы: {viol if viol else 'нет'}. "
    "Нет списков 2012, 2016–2018, 2020–2021, 2023; подача систем добровольная."
)

# H7 — descriptive snapshot only. The openness regression is not used.
h7_verdict = "не используется"
h7_result = (
    "Регрессия открытости не используется: она не удерживается без нескольких крупных лабораторий, "
    "а состав базы Epoch нельзя дополнить. Остаются доли и число notable models в D08_descriptives, без коэффициента."
)

claims = pd.DataFrame([
    {
        "H": "H1",
        "prediction": pred["H1"],
        "result": h1_result,
        "verdict": h1_verdict,
        "evidence": "D02_profile_variants_2019_2023.csv; D02_support_check.csv",
        "type": typ["H1"],
    },
    {
        "H": "H2",
        "prediction": pred["H2"],
        "result": h2_result,
        "verdict": h2_verdict,
        "evidence": "D03_all_specs.csv",
        "type": typ["H2"],
    },
    {
        "H": "H3",
        "prediction": pred["H3"],
        "result": h3_result,
        "verdict": h3_verdict,
        "evidence": "D04_robustness.csv; D10_key_numbers.csv",
        "type": typ["H3"],
    },
    {
        "H": "H4",
        "prediction": pred["H4"],
        "result": h4_result,
        "verdict": h4_verdict,
        "evidence": "D05_decomposition.csv",
        "type": typ["H4"],
    },
    {
        "H": "H5",
        "prediction": pred["H5"],
        "result": h5_result,
        "verdict": h5_verdict,
        "evidence": "D06_ic_trade_panel.csv; D06_equipment_trade.csv; D06_china_reimport_2023.csv",
        "type": typ["H5"],
    },
    {
        "H": "H6",
        "prediction": pred["H6"],
        "result": h6_result,
        "verdict": h6_verdict,
        "evidence": "D07_shares.csv; D07_exascale_table.csv",
        "type": typ["H6"],
    },
    {
        "H": "H7",
        "prediction": pred["H7"],
        "result": h7_result,
        "verdict": h7_verdict,
        "evidence": "D08_descriptives.csv",
        "type": "не используется (снимок)",
    },
])
save_table(claims, "D11_hypothesis_verdicts")

# Ladder: keep structure, update USA levels 3, 4, 7 from tables
exa = tbl("D07_exascale_table").drop_duplicates("Name")
usa_rmax24 = 100 * float(sh[(sh.iso == "USA") & (sh.list_year == 2024)].share_rmax.iloc[0])
lvl3_usa = (
    f"экспорт оборудования HS8486: {usa_eq_bn:.1f} млрд $ (2023), {usa_rank}-е место в выборке"
    if has_usa
    else "не измерено: нет данных Comtrade по США"
)
lvl4_usa = (
    f"TOP500: доля мощности {usa_rmax24:.0f}% (2024); эксафлопсных систем в данных: {len(exa)}, "
    f"из них в США: {int((exa.iso == 'USA').sum())}"
)
lvl7_usa = "торговля микросхемами и оборудованием (Comtrade 2010–2023)" if has_usa else "не измерено"

ladder = pd.DataFrame([
    {"level": 1, "claim": "наличие технологии / науки", "USA": "measured/snapshot", "CHN": "measured/snapshot", "strength": "средняя"},
    {"level": 2, "claim": "способность разработать", "USA": "снимок Epoch: frontier и compute", "CHN": "снимок Epoch: число и доля открытых весов, без теста", "strength": "слабая (отбор notable models)"},
    {"level": 3, "claim": "способность производить", "USA": lvl3_usa, "CHN": "нет fab capacity; net IC importer", "strength": "слабая для fab"},
    {"level": 4, "claim": "масштабирование", "USA": lvl4_usa, "CHN": "MVA/hitech shares; TOP500 rise-fall", "strength": "средняя"},
    {"level": 5, "claim": "внедрение", "USA": "не измерено", "CHN": "не измерено", "strength": "нет данных"},
    {"level": 6, "claim": "экономический эффект", "USA": "growth accounting TFP share", "CHN": "growth accounting; R&D–TFP link not id.", "strength": "ограниченная"},
    {"level": 7, "claim": "экспорт", "USA": lvl7_usa, "CHN": "IC export large but net importer", "strength": "высокая (trade)"},
    {"level": 8, "claim": "долгосрочное преимущество", "USA": "не выводится", "CHN": "не выводится", "strength": "нет"},
])
save_table(ladder, "D11_claim_ladder")
print(claims[["H", "verdict"]].to_string(index=False))
print("D11 done")

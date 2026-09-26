# %% [markdown]
# D06 — Полупроводники: торговля, оборудование, Тайвань (H5)

# %%
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import save_table, save_fig, style_axes, COLOR_USA, COLOR_CHN, COUNTRIES

RAW = ROOT / "data" / "raw" / "deep" / "comtrade"
world = pd.read_csv(RAW / "comtrade_world_flows.csv")
chn_p = pd.read_csv(RAW / "comtrade_china_partners.csv")
tw = pd.read_csv(RAW / "comtrade_taiwan_mirror.csv")

# %%
w = world.copy()
w["flow"] = w["flow"].astype(str)
ic = w[(w["cmd"].astype(str) == "8542") & (w["country_iso3"].isin(COUNTRIES))]
tot = w[(w["cmd"].astype(str) == "TOTAL") & (w["flow"] == "X") & (w["country_iso3"].isin(COUNTRIES))]
eq = w[(w["cmd"].astype(str) == "8486") & (w["country_iso3"].isin(COUNTRIES))]

piv = ic.pivot_table(index=["country_iso3", "year"], columns="flow", values="value_usd", aggfunc="sum").reset_index()
piv = piv.rename(columns={"X": "ic_x", "M": "ic_m"})
piv["ic_net"] = piv["ic_x"] - piv["ic_m"]
piv["ic_cover"] = piv["ic_x"] / piv["ic_m"]
tot_x = tot.groupby(["country_iso3", "year"], as_index=False)["value_usd"].sum().rename(columns={"value_usd": "total_x"})
piv = piv.merge(tot_x, on=["country_iso3", "year"], how="left")
piv["ic_share"] = piv["ic_x"] / piv["total_x"]

# RCA relative to the sample (OECD + China), not to world trade
ws = piv.dropna(subset=["ic_x", "total_x"]).groupby("year", as_index=False).agg(
    ic_x_sum=("ic_x", "sum"), total_x_sum=("total_x", "sum")
)
ws["sample_ic_share"] = ws["ic_x_sum"] / ws["total_x_sum"]
piv = piv.merge(ws[["year", "sample_ic_share"]], on="year", how="left")
piv["rca"] = piv["ic_share"] / piv["sample_ic_share"]
save_table(piv, "D06_ic_trade_panel")

# %%
chn = piv[piv.country_iso3 == "CHN"].sort_values("year")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(chn.year, chn.ic_x / 1e9, label="экспорт", color=COLOR_CHN)
ax.plot(chn.year, chn.ic_m / 1e9, label="импорт", color="orange")
ax.plot(chn.year, chn.ic_net / 1e9, label="баланс", color="black", ls="--")
for y in [2022, 2023]:
    ax.axvline(y, color="gray", alpha=0.5, ls=":")
style_axes(ax, title="Китай: торговля микросхемами HS8542 ($ млрд)", ylabel="$ млрд")
ax.legend()
save_fig(fig, "D06_china_ic_x_m")

# %%
# China import sources 2023
src = chn_p[(chn_p.cmd.astype(str) == "8542") & (chn_p.year == 2023)].copy()
total_m_2023 = float(src.loc[src.partner_code == 0, "value_usd"].sum())
reimport_2023 = float(src.loc[src.partner_code == 156, "value_usd"].sum())
save_table(pd.DataFrame([{"year": 2023, "total_m": total_m_2023, "reimport_156": reimport_2023,
                          "reimport_share": reimport_2023 / total_m_2023}]), "D06_china_reimport_2023")
src = src[src.partner_code != 0]
src = src.sort_values("value_usd", ascending=False).head(12)
PARTNERS = {
    490: "Тайвань", 410: "Корея", 392: "Япония", 842: "США", 458: "Малайзия",
    704: "Вьетнам", 344: "Гонконг", 702: "Сингапур", 156: "Китай (реимпорт)",
    608: "Филиппины", 764: "Таиланд", 372: "Ирландия", 276: "Германия",
    360: "Индонезия", 528: "Нидерланды", 699: "Индия", 484: "Мексика", 376: "Израиль",
}
src["partner"] = src["partner_code"].map(lambda x: PARTNERS.get(int(x), str(int(x))))
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(src.partner[::-1], src.value_usd[::-1] / 1e9, color=COLOR_CHN)
style_axes(ax, title="Импорт Китаем HS8542 по партнёрам, 2023, без строки «Мир» ($ млрд)", xlabel="$ млрд")
save_fig(fig, "D06_china_ic_sources_2023")
save_table(src[["partner_code", "partner", "value_usd"]], "D06_china_ic_sources_2023")

# equipment exporters
eqx = eq[eq.flow == "X"].groupby(["country_iso3", "year"], as_index=False)["value_usd"].sum()
eq2023 = eqx[eqx.year == 2023].sort_values("value_usd", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(7, 4))
ax.barh(eq2023.country_iso3[::-1], eq2023.value_usd[::-1] / 1e9)
style_axes(ax, title="Экспортёры оборудования HS8486, 2023", xlabel="$ млрд")
save_fig(fig, "D06_equipment_exporters")
save_table(eqx, "D06_equipment_trade")

eqm_chn = eq[(eq.country_iso3 == "CHN") & (eq.flow == "M")].sort_values("year")
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(eqm_chn.year, eqm_chn.value_usd / 1e9, color=COLOR_CHN)
style_axes(ax, title="Импорт Китаем оборудования HS8486", ylabel="$ млрд")
save_fig(fig, "D06_china_8486_imports")

# Taiwan mirror sum
tw_sum = tw.groupby("year")["value_usd"].sum().reset_index().rename(columns={"value_usd": "mirror_export_tw"})
save_table(tw_sum, "D06_taiwan_mirror")

# chain qualitative table
chain = pd.DataFrame([
    {"stage": "design", "data": "нет ряда", "note": "qual"},
    {"stage": "EDA/IP", "data": "нет ряда", "note": "qual"},
    {"stage": "equipment", "data": "HS8486 trade", "note": "NLD/JPN/USA expected"},
    {"stage": "fabrication", "data": "нет fab capacity; Taiwan via partner 490", "note": "trade≠fab"},
    {"stage": "packaging", "data": "нет", "note": "qual"},
    {"stage": "downstream", "data": "HS8542 + hitech_share", "note": "trade/shares"},
])
save_table(chain, "D06_chain_map")

# sanity: china partner sum vs world M
world_m = piv[(piv.country_iso3 == "CHN") & (piv.year == 2023)]["ic_m"].iloc[0]
partner_sum = chn_p[(chn_p.cmd.astype(str) == "8542") & (chn_p.year == 2023) & (chn_p.partner_code != 0)]["value_usd"].sum()
print("world M", world_m, "partner sum", partner_sum, "ratio", partner_sum / world_m if world_m else None)
print("D06 done")

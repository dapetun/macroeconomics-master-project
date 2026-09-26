"""Build OECD+China analysis panel from deep raw downloads."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw" / "deep"
OUT = ROOT / "data" / "deep"
OUT.mkdir(parents=True, exist_ok=True)

COUNTRIES = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN",
    "KOR", "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT",
    "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "CHN",
]
YEARS = list(range(2000, 2024))
DELTA = 0.15


def wide_from_long(path: Path, value_name: str | None = None) -> pd.DataFrame:
    df = pd.read_csv(path)
    piv = df.pivot_table(
        index=["country_iso3", "year"], columns="var", values="value", aggfunc="first"
    ).reset_index()
    piv.columns.name = None
    return piv


def period5(year: int) -> str:
    if 2001 <= year <= 2005:
        return "2001-05"
    if 2006 <= year <= 2010:
        return "2006-10"
    if 2011 <= year <= 2015:
        return "2011-15"
    if 2016 <= year <= 2019:
        return "2016-19"
    if 2020 <= year <= 2023:
        return "2020-23"
    return "other"


def rd_stock(group: pd.DataFrame) -> pd.Series:
    """Perpetual inventory R&D stock; requires sorted years."""
    g = group.sort_values("year").copy()
    r = g["rd_ppp"].astype(float)
    stock = pd.Series(np.nan, index=g.index, dtype=float)
    # initial: average growth 2000-2004 if available
    early = r[(g["year"] >= 2000) & (g["year"] <= 2004)].dropna()
    if early.empty or early.iloc[0] <= 0:
        return stock
    if len(early) >= 2 and early.iloc[0] > 0:
        growth = (early.iloc[-1] / early.iloc[0]) ** (1 / max(len(early) - 1, 1)) - 1
        growth = max(float(growth), 0.01)
    else:
        growth = 0.05
    s0 = float(early.iloc[0]) / (growth + DELTA)
    prev = None
    for idx, val in r.items():
        if pd.isna(val):
            stock.loc[idx] = np.nan
            prev = None
            continue
        if prev is None:
            # first non-missing
            if g.loc[idx, "year"] <= 2004:
                prev = s0
            else:
                prev = float(val) / (growth + DELTA)
        else:
            prev = (1 - DELTA) * prev + float(val)
        stock.loc[idx] = prev
    return stock


def main() -> None:
    wb = wide_from_long(RAW / "wb" / "wb_long.csv")
    pwt = wide_from_long(RAW / "pwt" / "pwt_long.csv")
    # rename PWT pop to avoid clash
    if "pop" in pwt.columns:
        pwt = pwt.rename(columns={"pop": "pop_pwt"})
    oecd = wide_from_long(RAW / "oecd" / "oecd_long.csv")

    base = pd.MultiIndex.from_product([COUNTRIES, YEARS], names=["country_iso3", "year"])
    panel = pd.DataFrame(index=base).reset_index()

    panel = panel.merge(wb, on=["country_iso3", "year"], how="left")
    panel = panel.merge(pwt, on=["country_iso3", "year"], how="left")
    panel = panel.merge(oecd, on=["country_iso3", "year"], how="left")

    # Prefer WB rd_gdp; fill Switzerland gaps from OECD GERD % GDP if available
    if "gerd_pct_gdp_oecd" in panel.columns:
        panel["rd_gdp"] = panel["rd_gdp"].fillna(panel["gerd_pct_gdp_oecd"])

    # Absolute R&D: OECD absolute sparse for many countries → construct from
    # rd_gdp × GDP (gdppc_ppp × pop). Prefer OECD current PPP where available.
    panel["gdp_ppp"] = panel["gdppc_ppp"] * panel["pop"]
    panel["rd_ppp_constructed"] = (panel["rd_gdp"] / 100.0) * panel["gdp_ppp"]
    oecd_n = int(panel["gerd_usd_ppp_current"].notna().sum()) if "gerd_usd_ppp_current" in panel.columns else 0
    if oecd_n > 500:
        panel["rd_ppp"] = panel["gerd_usd_ppp_current"]
        rd_note = "OECD GERD USD PPP current"
    else:
        panel["rd_ppp"] = panel["rd_ppp_constructed"]
        rd_note = (
            f"Constructed rd_ppp = (rd_gdp/100)*gdppc_ppp*pop "
            f"(OECD absolute only n={oecd_n} cells; see DEEP_DEVIATIONS)"
        )
        Path(ROOT / "DEEP_DEVIATIONS.md").write_text(
            Path(ROOT / "DEEP_DEVIATIONS.md").read_text(encoding="utf-8")
            + f"\n| 2026-09-25 | S4 | rd_ppp constructed from intensity×GDP PPP | OECD MSTI absolute GERD covered few countries (n={oecd_n}) | Levels comparable within WB vintage; not identical to OECD mln USD PPP |\n",
            encoding="utf-8",
        )

    # logs and rates
    for col, out in [
        ("gdppc_ppp", "ln_gdppc"),
        ("pop", "ln_pop"),
        ("rd_ppp", "ln_rd_ppp"),
        ("pat_res", "ln_pat_res"),
        ("articles", "ln_articles"),
        ("researchers_pm", "ln_researchers_pm"),
    ]:
        panel[out] = np.log(panel[col].where(panel[col] > 0))

    panel["pat_tot"] = panel["pat_res"] + panel["pat_nonres"]
    panel["ln_pat_tot"] = np.log(panel["pat_tot"].where(panel["pat_tot"] > 0))
    panel["articles_pm"] = panel["articles"] / (panel["pop"] / 1e6)
    panel["pat_res_pm"] = panel["pat_res"] / (panel["pop"] / 1e6)
    # researchers headcount estimate
    panel["researchers"] = panel["researchers_pm"] * (panel["pop"] / 1e6)
    panel["ln_researchers"] = np.log(panel["researchers"].where(panel["researchers"] > 0))

    panel = panel.sort_values(["country_iso3", "year"])
    g = panel.groupby("country_iso3", group_keys=False)
    panel["dln_tfp"] = g["rtfpna"].transform(lambda s: np.log(s).diff() * 100)
    panel["lp"] = panel["rgdpna"] / panel["emp"]
    panel["dln_lp"] = g["lp"].transform(lambda s: np.log(s).diff() * 100)
    panel["gap"] = -np.log(panel["ctfp"].where(panel["ctfp"] > 0))
    panel["rd_gdp_lag1"] = g["rd_gdp"].shift(1)
    panel["ln_rd_ppp_lag1"] = g["ln_rd_ppp"].shift(1)
    panel["gap_lag1"] = g["gap"].shift(1)

    # R&D stock
    stocks = []
    for c, sub in panel.groupby("country_iso3"):
        s = rd_stock(sub)
        stocks.append(s)
    panel["rd_stock"] = pd.concat(stocks).sort_index()
    panel["ln_rd_stock"] = np.log(panel["rd_stock"].where(panel["rd_stock"] > 0))
    panel["ln_rd_stock_lag1"] = g["ln_rd_stock"].shift(1)

    # centered for interactions
    panel["rd_c"] = panel["rd_gdp_lag1"] - panel["rd_gdp_lag1"].mean(skipna=True)
    panel["gap_c"] = panel["gap_lag1"] - panel["gap_lag1"].mean(skipna=True)
    panel["rd_gap"] = panel["rd_c"] * panel["gap_c"]

    panel["is_chn"] = (panel["country_iso3"] == "CHN").astype(int)
    panel["is_usa"] = (panel["country_iso3"] == "USA").astype(int)
    panel["period5"] = panel["year"].map(period5)

    out_path = OUT / "panel_oecd_chn.csv"
    panel.to_csv(out_path, index=False)

    dictionary = [
        ("country_iso3", "ISO3 country code", "panel", "code", "identity", "OECD+CHN"),
        ("year", "Calendar year", "panel", "year", "identity", "2000-2023"),
        ("rd_gdp", "GERD % GDP", "World Bank / OECD fill", "%", "level", "CHE often biennial"),
        ("rd_ppp", "Оценка объёма R&D = доля R&D в ВВП × ВВП по ППС (не данные OECD)", "расчёт: World Bank rd_gdp × gdppc_ppp × pop", "USD PPP (постоянные цены)", "level", rd_note),
        ("researchers_pm", "Researchers per million", "World Bank", "per mn", "level", "coverage gaps"),
        ("articles", "S&E articles count", "World Bank", "count", "level", "volume not quality"),
        ("pat_res", "Resident patent applications", "World Bank", "count", "office-basis", "not origin"),
        ("rtfpna", "TFP national accounts", "PWT", "index", "level", "growth measure"),
        ("ctfp", "TFP relative to USA", "PWT", "index", "USA≈1", "gap = -ln(ctfp)"),
        ("dln_tfp", "TFP growth", "derived", "%", "Δln rtfpna×100", "noisy annually"),
        ("gap", "Distance to frontier", "derived", "log points", "-ln(ctfp)", "USA≈0"),
        ("rd_stock", "R&D knowledge stock", "derived", "USD PPP", "PIM δ=0.15", "initial condition sensitive"),
    ]
    pd.DataFrame(
        dictionary, columns=["name", "meaning", "source", "unit", "transform", "limitation"]
    ).to_csv(OUT / "data_dictionary_deep.csv", index=False)

    meta = {
        "n_rows": int(len(panel)),
        "n_countries": int(panel["country_iso3"].nunique()),
        "years": f"{panel['year'].min()}-{panel['year'].max()}",
        "rd_ppp_note": rd_note,
        "path": str(out_path.relative_to(ROOT)),
    }
    (OUT / "panel_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))
    print("coverage rd_gdp", panel.groupby("country_iso3")["rd_gdp"].apply(lambda s: s.notna().sum()).describe())


if __name__ == "__main__":
    main()

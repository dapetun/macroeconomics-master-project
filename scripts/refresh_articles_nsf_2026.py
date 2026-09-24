"""Refresh S&E article counts from NSF Indicators 2026 (Fig. 29) through 2024
and bump dual-scale joint years where panel already has newer values (hitech, BERD).
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

# NSF State of U.S. S&E 2026, Figure 29 (Scopus fractional counts; accessed Aug 2025)
# Source: https://ncses.nsf.gov/pubs/nsbsep20261/discovery-r-d-activity-and-research-publications-2
NSF_FIG29 = {
    # year: {iso: value}
    2014: {"WLD": 2193498, "USA": 428049, "DEU": 105528, "GBR": 97901, "CHN": 378661, "IND": 88227, "JPN": 103336},
    2015: {"WLD": 2250669, "USA": 429340, "DEU": 106804, "GBR": 99616, "CHN": 400690, "IND": 94731, "JPN": 100582},
    2016: {"WLD": 2335510, "USA": 431848, "DEU": 108978, "GBR": 100133, "CHN": 429614, "IND": 104549, "JPN": 101145},
    2017: {"WLD": 2425123, "USA": 435539, "DEU": 109828, "GBR": 100980, "CHN": 463411, "IND": 115542, "JPN": 101829},
    2018: {"WLD": 2522582, "USA": 441299, "DEU": 109200, "GBR": 101193, "CHN": 513153, "IND": 123760, "JPN": 102066},
    2019: {"WLD": 2710512, "USA": 442821, "DEU": 110442, "GBR": 102112, "CHN": 608541, "IND": 128410, "JPN": 100232},
    2020: {"WLD": 2873342, "USA": 454221, "DEU": 109515, "GBR": 103482, "CHN": 672772, "IND": 145534, "JPN": 100519},
    2021: {"WLD": 3126671, "USA": 472375, "DEU": 117492, "GBR": 108325, "CHN": 761535, "IND": 173204, "JPN": 106627},
    2022: {"WLD": 3238106, "USA": 448935, "DEU": 112822, "GBR": 102064, "CHN": 891697, "IND": 200839, "JPN": 102670},
    2023: {"WLD": 3285108, "USA": 431338, "DEU": 109086, "GBR": 97459, "CHN": 938945, "IND": 227796, "JPN": 96872},
    2024: {"WLD": 3525866, "USA": 439892, "DEU": 109102, "GBR": 99582, "CHN": 1078580, "IND": 258469, "JPN": 97974},
}
PANEL_ISO = ["USA", "CHN", "DEU", "GBR", "JPN"]  # Fig.29 countries that sit in our 8-country panel


def cagr(v0: float, v1: float, t0: int, t1: int) -> float:
    n = t1 - t0
    if n <= 0 or v0 is None or v1 is None or pd.isna(v0) or pd.isna(v1) or v0 <= 0 or v1 <= 0:
        return float("nan")
    return (v1 / v0) ** (1 / n) - 1


def nsf_long() -> pd.DataFrame:
    rows = []
    for year, mp in NSF_FIG29.items():
        for iso, val in mp.items():
            rows.append(
                {
                    "country_iso3": iso,
                    "year": year,
                    "value": float(val),
                    "unit": "fractional article count",
                    "source": "NSF NCSES State of U.S. Science and Engineering 2026, Figure 29",
                    "source_url": "https://ncses.nsf.gov/pubs/nsbsep20261/discovery-r-d-activity-and-research-publications-2",
                    "notes": "Elsevier Scopus; fractional count; accessed August 2025",
                }
            )
    return pd.DataFrame(rows)


def update_panel_articles(panel: pd.DataFrame, nsf: pd.DataFrame) -> pd.DataFrame:
    out = panel.copy()
    nsf_p = nsf[nsf["country_iso3"].isin(PANEL_ISO)][["country_iso3", "year", "value"]]
    # Ensure 2024 rows exist for panel countries that may lack the year
    years = set(range(int(out["year"].min()), int(out["year"].max()) + 1))
    for iso in PANEL_ISO:
        for year in range(2014, 2025):
            mask = (out["country_iso3"] == iso) & (out["year"] == year)
            val = float(nsf_p[(nsf_p.country_iso3 == iso) & (nsf_p.year == year)]["value"].iloc[0])
            if mask.any():
                out.loc[mask, "scopus_articles"] = val
            else:
                # append thin row
                row = {c: pd.NA for c in out.columns}
                row["country_iso3"] = iso
                row["year"] = year
                row["scopus_articles"] = val
                out = pd.concat([out, pd.DataFrame([row])], ignore_index=True)
    out = out.sort_values(["country_iso3", "year"]).reset_index(drop=True)
    return out


def rebuild_dual_scale(panel: pd.DataFrame) -> pd.DataFrame:
    """Rebuild dual_scale_intensity_volume from panel with refreshed articles/hitech/BERD joints."""

    def joint(col: str) -> tuple[int, float, float]:
        sub = panel[panel["country_iso3"].isin(["USA", "CHN"])][["country_iso3", "year", col]].dropna()
        wide = sub.pivot(index="year", columns="country_iso3", values=col).dropna()
        y = int(wide.index.max())
        return y, float(wide.loc[y, "USA"]), float(wide.loc[y, "CHN"])

    def series_val(iso: str, year: int, col: str) -> float:
        s = panel[(panel.country_iso3 == iso) & (panel.year == year)][col]
        return float(s.iloc[0]) if len(s) and pd.notna(s.iloc[0]) else float("nan")

    def row(var, family, y, usa, chn, t0, t1, note="", force_sign=None):
        ratio = chn / usa if usa else float("nan")
        sign = "CHN_higher" if chn > usa else "USA_higher"
        matches = True
        if force_sign == "USA_higher":
            matches = usa > chn
        elif force_sign == "CHN_higher":
            matches = chn > usa
        return {
            "var": var,
            "scale_family": family,
            "joint_year": y,
            "USA": usa,
            "CHN": chn,
            "CHN_USA_ratio": ratio,
            "gap_sign_level": sign,
            "cagr_t0": float(t0) if t0 is not None else "",
            "cagr_t1": float(t1) if t1 is not None else "",
            "CAGR_USA": cagr(series_val("USA", t0, var), usa, t0, y) if t0 is not None else "",
            "CAGR_CHN": cagr(series_val("CHN", t0, var), chn, t0, y) if t0 is not None else "",
            "note": note,
            "matches_D1_sign": matches,
        }

    rows = []
    # intensity
    y, usa, chn = joint("gerd_pct_gdp")
    rows.append(row("gerd_pct_gdp", "intensity", y, usa, chn, 2010, y, force_sign="USA_higher"))
    y, usa, chn = joint("berd_pct_gdp")
    rows.append(row("berd_pct_gdp", "intensity", y, usa, chn, 2010, y, force_sign="USA_higher"))
    y, usa, chn = joint("researchers_per_million")
    # researchers common CAGR window stays 2010-2017
    rows.append(
        row(
            "researchers_per_million",
            "intensity",
            y,
            usa,
            chn,
            2010,
            2017,
            note="joint year latest mutual; CAGR window 2010-2017 (GBR/panel constraint)",
            force_sign="USA_higher",
        )
    )
    # fix CAGR to use 2017 endpoints not joint year
    r = rows[-1]
    r["cagr_t1"] = 2017.0
    r["CAGR_USA"] = cagr(series_val("USA", 2010, "researchers_per_million"), series_val("USA", 2017, "researchers_per_million"), 2010, 2017)
    r["CAGR_CHN"] = cagr(series_val("CHN", 2010, "researchers_per_million"), series_val("CHN", 2017, "researchers_per_million"), 2010, 2017)

    # articles — NSF-refreshed
    y, usa, chn = joint("scopus_articles")
    rows.append(
        row(
            "scopus_articles",
            "volume",
            y,
            usa,
            chn,
            2010,
            y,
            note="2014-2024 from NSF Indicators 2026 Fig.29; pre-2014 World Bank WDI vintage",
            force_sign="CHN_higher",
        )
    )

    y, usa, chn = joint("patents_resident")
    rows.append(row("patents_resident", "volume", y, usa, chn, 2010, y, force_sign="CHN_higher"))
    y, usa, chn = joint("patents_total_office")
    rows.append(row("patents_total_office", "volume", y, usa, chn, 2010, y, force_sign="CHN_higher"))
    y, usa, chn = joint("mva_pct_gdp")
    rows.append(row("mva_pct_gdp", "share", y, usa, chn, 2010, y, force_sign="CHN_higher"))
    y, usa, chn = joint("hitech_export_share")
    rows.append(row("hitech_export_share", "share", y, usa, chn, 2010, y, force_sign="CHN_higher"))

    # HS8542: clean file is USA-only after quarantine; use full exports for USA–CHN joint
    hs_path = ROOT / "data" / "raw" / "comtrade_hs8542_exports.csv"
    hs = pd.read_csv(hs_path)
    val_col = "value_usd" if "value_usd" in hs.columns else [c for c in hs.columns if "value" in c.lower()][0]
    hs_sub = hs[hs["country_iso3"].isin(["USA", "CHN"])][["country_iso3", "year", val_col]].dropna()
    hs_sub = hs_sub.rename(columns={val_col: "value_usd"})
    wide = hs_sub.pivot(index="year", columns="country_iso3", values="value_usd")
    if "USA" in wide.columns and "CHN" in wide.columns:
        both = wide[["USA", "CHN"]].dropna()
        if len(both):
            y = int(both.index.max())
            usa, chn = float(both.loc[y, "USA"]), float(both.loc[y, "CHN"])
            rows.append(
                {
                    "var": "semi_exports_hs8542",
                    "scale_family": "volume_nominal",
                    "joint_year": y,
                    "USA": usa,
                    "CHN": chn,
                    "CHN_USA_ratio": chn / usa,
                    "gap_sign_level": "CHN_higher" if chn > usa else "USA_higher",
                    "cagr_t0": "",
                    "cagr_t1": "",
                    "CAGR_USA": "",
                    "CAGR_CHN": "",
                    "note": "Comtrade HS8542 from exports.csv (clean is USA-only); ≠ fab; joint by mutual year",
                    "matches_D1_sign": chn > usa,
                }
            )

    # dual-window articles CAGR rows
    peak_usa_year = int(
        panel[(panel.country_iso3 == "USA") & panel.scopus_articles.notna()]
        .sort_values("scopus_articles", ascending=False)
        .iloc[0]["year"]
    )
    peak_usa_val = float(
        panel[(panel.country_iso3 == "USA") & (panel.year == peak_usa_year)]["scopus_articles"].iloc[0]
    )
    for end in (2021, 2024):
        usa_e = series_val("USA", end, "scopus_articles")
        chn_e = series_val("CHN", end, "scopus_articles")
        usa0 = series_val("USA", 2010, "scopus_articles")
        chn0 = series_val("CHN", 2010, "scopus_articles")
        rows.append(
            {
                "var": "scopus_articles_CAGR_only",
                "scale_family": "volume",
                "joint_year": end,
                "USA": usa_e,
                "CHN": chn_e,
                "CHN_USA_ratio": chn_e / usa_e,
                "gap_sign_level": "CHN_higher",
                "cagr_t0": 2010.0,
                "cagr_t1": float(end),
                "CAGR_USA": cagr(usa0, usa_e, 2010, end),
                "CAGR_CHN": cagr(chn0, chn_e, 2010, end),
                "note": f"dual-window; endpoint {end}; peak USA {peak_usa_year}={peak_usa_val:.0f}; NSF 2014-2024",
                "matches_D1_sign": True,
            }
        )

    return pd.DataFrame(rows)


def write_articles_cagr(panel: pd.DataFrame) -> pd.DataFrame:
    peak_usa_year = int(
        panel[(panel.country_iso3 == "USA") & panel.scopus_articles.notna()]
        .sort_values("scopus_articles", ascending=False)
        .iloc[0]["year"]
    )
    peak_usa_val = float(
        panel[(panel.country_iso3 == "USA") & (panel.year == peak_usa_year)]["scopus_articles"].iloc[0]
    )
    rows = []
    for iso in ("USA", "CHN"):
        for t1 in (2021, 2024):
            v0 = float(panel[(panel.country_iso3 == iso) & (panel.year == 2010)]["scopus_articles"].iloc[0])
            v1 = float(panel[(panel.country_iso3 == iso) & (panel.year == t1)]["scopus_articles"].iloc[0])
            rows.append(
                {
                    "var": "scopus_articles",
                    "country": iso,
                    "window_t0": 2010,
                    "window_t1": t1,
                    "v0": v0,
                    "v1": v1,
                    "CAGR": cagr(v0, v1, 2010, t1),
                    "peak_year": peak_usa_year if iso == "USA" else "",
                    "peak_value": peak_usa_val if iso == "USA" else "",
                    "note": "dual-window; 2014-2024 NSF Indicators 2026 Fig.29; 2010 from prior WDI vintage retained",
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    nsf = nsf_long()
    out_nsf = ROOT / "data" / "raw" / "nsf_se_articles_indicators2026.csv"
    nsf.to_csv(out_nsf, index=False)
    print("wrote", out_nsf.relative_to(ROOT), "rows", len(nsf))

    panel_path = ROOT / "data_reviewed" / "core_panel_reviewed.csv"
    panel = pd.read_csv(panel_path)
    panel2 = update_panel_articles(panel, nsf)
    panel2.to_csv(panel_path, index=False)
    print("updated", panel_path.relative_to(ROOT))

    # also refresh long raw articles for panel countries 2014-2024
    raw_path = ROOT / "data" / "raw" / "scopus_articles.csv"
    raw = pd.read_csv(raw_path)
    nsf_p = nsf[nsf.country_iso3.isin(PANEL_ISO)][["country_iso3", "year", "value"]]
    raw = raw[~((raw.country_iso3.isin(PANEL_ISO)) & (raw.year.between(2014, 2024)))]
    raw = pd.concat([raw, nsf_p], ignore_index=True).sort_values(["country_iso3", "year"])
    raw.to_csv(raw_path, index=False)
    print("updated", raw_path.relative_to(ROOT))

    dual = rebuild_dual_scale(panel2)
    dual_path = ROOT / "data_reviewed" / "tables_reviewed" / "dual_scale_intensity_volume.csv"
    dual.to_csv(dual_path, index=False)
    print("wrote", dual_path.relative_to(ROOT))

    art = write_articles_cagr(panel2)
    art_path = ROOT / "data_reviewed" / "tables_reviewed" / "articles_cagr_dual_window.csv"
    art.to_csv(art_path, index=False)
    print("wrote", art_path.relative_to(ROOT))

    # crossover check
    w = (
        panel2[panel2.country_iso3.isin(["USA", "CHN"])][["year", "country_iso3", "scopus_articles"]]
        .dropna()
        .pivot(index="year", columns="country_iso3", values="scopus_articles")
        .dropna()
    )
    last_usa = int(w.loc[w["USA"] >= w["CHN"]].index.max())
    first_chn = int(w.loc[w["CHN"] > w["USA"]].index.min())
    print("crossover: last USA>=CHN", last_usa, "first CHN>USA", first_chn)
    print("2024 USA/CHN", float(w.loc[2024, "USA"]), float(w.loc[2024, "CHN"]))
    print("hitech joint", dual.loc[dual["var"] == "hitech_export_share", ["joint_year", "USA", "CHN"]].to_string(index=False))
    print("articles joint", dual.loc[dual["var"] == "scopus_articles", ["joint_year", "USA", "CHN"]].to_string(index=False))
    print("berd joint", dual.loc[dual["var"] == "berd_pct_gdp", ["joint_year", "USA", "CHN"]].to_string(index=False))
    print("hs8542", dual.loc[dual["var"] == "semi_exports_hs8542", ["joint_year", "USA", "CHN"]].to_string(index=False))


if __name__ == "__main__":
    main()

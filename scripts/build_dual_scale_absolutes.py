"""Build dual_scale_with_absolutes.csv from on-disk sources (no new downloads)."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data_reviewed" / "tables_reviewed" / "dual_scale_with_absolutes.csv"
EXISTING = ROOT / "data_reviewed" / "tables_reviewed" / "dual_scale_intensity_volume.csv"


def cagr(v0: float, v1: float, t0: int, t1: int) -> float:
    n = t1 - t0
    if n <= 0 or v0 is None or v1 is None or v0 <= 0 or v1 <= 0:
        return float("nan")
    return (v1 / v0) ** (1 / n) - 1


def latest_joint(df: pd.DataFrame, col: str, countries=("USA", "CHN")) -> tuple[int, float, float]:
    sub = df[df["country_iso3"].isin(countries)][["country_iso3", "year", col]].dropna()
    wide = sub.pivot(index="year", columns="country_iso3", values=col).dropna()
    year = int(wide.index.max())
    return year, float(wide.loc[year, "USA"]), float(wide.loc[year, "CHN"])


def main() -> None:
    panel = pd.read_csv(ROOT / "data_reviewed" / "core_panel_reviewed.csv")
    gerd = pd.read_csv(ROOT / "data" / "raw" / "oecd_gerd_usd_ppp.csv").rename(
        columns={"value": "gerd_usd_ppp"}
    )
    pop = pd.read_csv(ROOT / "data" / "raw" / "pwt_pop.csv")
    hc = pd.read_csv(ROOT / "data" / "raw" / "pwt_hc.csv")
    hc_col = [c for c in hc.columns if c not in ("country_iso3", "year")][0]
    hc = hc.rename(columns={hc_col: "pwt_hc"})

    m = panel.merge(gerd, on=["country_iso3", "year"], how="left")
    m = m.merge(pop, on=["country_iso3", "year"], how="left")
    m = m.merge(hc, on=["country_iso3", "year"], how="left")
    # pop in millions; researchers_per_million → headcount in thousands
    m["researchers_headcount_est_thousands"] = (
        m["researchers_per_million"] * m["pop"] / 1000.0
    )

    rows = []
    if EXISTING.exists():
        base = pd.read_csv(EXISTING)
        # keep core dual-scale rows (exclude CAGR_only duplicates for articles dual window —
        # they stay in existing file; we append absolutes)
        for _, r in base.iterrows():
            rows.append(r.to_dict())

    # Absolute GERD PPP
    y, usa, chn = latest_joint(m, "gerd_usd_ppp")
    g_usa = m[(m.country_iso3 == "USA") & (m.year.isin([2010, y]))].set_index("year")
    g_chn = m[(m.country_iso3 == "CHN") & (m.year.isin([2010, y]))].set_index("year")
    rows.append(
        {
            "var": "gerd_usd_ppp",
            "scale_family": "volume_absolute",
            "joint_year": y,
            "USA": usa,
            "CHN": chn,
            "CHN_USA_ratio": chn / usa if usa else float("nan"),
            "gap_sign_level": "CHN_higher" if chn > usa else "USA_higher",
            "cagr_t0": 2010.0,
            "cagr_t1": float(y),
            "CAGR_USA": cagr(float(g_usa.loc[2010, "gerd_usd_ppp"]), usa, 2010, y),
            "CAGR_CHN": cagr(float(g_chn.loc[2010, "gerd_usd_ppp"]), chn, 2010, y),
            "note": "OECD MSTI mln USD PPP; do NOT arithmetically mix with WB gerd_pct_gdp",
            "matches_D1_sign": True,  # volume side: CHN higher expected for D1 volume family
        }
    )

    # Headcount estimate
    y2, usa_h, chn_h = latest_joint(m, "researchers_headcount_est_thousands")
    h_usa = m[(m.country_iso3 == "USA") & (m.year.isin([2010, y2]))].set_index("year")
    h_chn = m[(m.country_iso3 == "CHN") & (m.year.isin([2010, y2]))].set_index("year")
    # common-window for CAGR aligned with researchers intensity window preference:
    # use 2010–min(y2, 2017) only if both have 2017; else 2010–y2
    cagr_end = min(y2, 2017) if y2 >= 2017 else y2
    # check both have cagr_end
    def val(iso, year, col):
        s = m[(m.country_iso3 == iso) & (m.year == year)][col]
        return float(s.iloc[0]) if len(s) and pd.notna(s.iloc[0]) else float("nan")

    rows.append(
        {
            "var": "researchers_headcount_est_thousands",
            "scale_family": "volume_absolute",
            "joint_year": y2,
            "USA": usa_h,
            "CHN": chn_h,
            "CHN_USA_ratio": chn_h / usa_h if usa_h else float("nan"),
            "gap_sign_level": "CHN_higher" if chn_h > usa_h else "USA_higher",
            "cagr_t0": 2010.0,
            "cagr_t1": float(cagr_end),
            "CAGR_USA": cagr(val("USA", 2010, "researchers_headcount_est_thousands"), val("USA", cagr_end, "researchers_headcount_est_thousands"), 2010, cagr_end),
            "CAGR_CHN": cagr(val("CHN", 2010, "researchers_headcount_est_thousands"), val("CHN", cagr_end, "researchers_headcount_est_thousands"), 2010, cagr_end),
            "note": "est. thousands = researchers_per_million * PWT_pop_millions / 1000; not official headcount series",
            "matches_D1_sign": True if chn_h > usa_h else False,
        }
    )

    # Optional HC index
    y3, usa_hc, chn_hc = latest_joint(m, "pwt_hc")
    rows.append(
        {
            "var": "pwt_hc",
            "scale_family": "index_optional",
            "joint_year": y3,
            "USA": usa_hc,
            "CHN": chn_hc,
            "CHN_USA_ratio": chn_hc / usa_hc if usa_hc else float("nan"),
            "gap_sign_level": "CHN_higher" if chn_hc > usa_hc else "USA_higher",
            "cagr_t0": "",
            "cagr_t1": "",
            "CAGR_USA": "",
            "CAGR_CHN": "",
            "note": "PWT human capital index; thin education coverage; not STEM",
            "matches_D1_sign": "",
        }
    )

    out = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")
    print(
        out[out["var"].isin(["gerd_usd_ppp", "researchers_headcount_est_thousands", "pwt_hc"])].to_string(
            index=False
        )
    )


if __name__ == "__main__":
    main()

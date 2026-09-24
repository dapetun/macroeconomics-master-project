#!/usr/bin/env python3
"""QuantitativeAgent Level-1 refresh + one PCA repair cycle (Approved Method Set).

Reads data_reviewed/core_panel_reviewed.csv (+ tech for HS8542).
Writes tables under data_reviewed/tables_reviewed/ and PCA repair under results/.
Regenerates worst-offender figure titles (F1, F3, F4) with neutral language.
Does NOT overwrite regression_results_final.csv or old broken pca_loadings.csv
as "authoritative" — repair artefacts get explicit names.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data_reviewed" / "core_panel_reviewed.csv"
TECH = ROOT / "data_reviewed" / "tech_panel_reviewed.csv"
OUT_TAB = ROOT / "data_reviewed" / "tables_reviewed"
OUT_RES = ROOT / "results"
OUT_FIG = ROOT / "figures"
OUT_FIG_REV = ROOT / "data_reviewed" / "figures_reviewed"

OUT_TAB.mkdir(parents=True, exist_ok=True)
OUT_RES.mkdir(parents=True, exist_ok=True)
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_FIG_REV.mkdir(parents=True, exist_ok=True)

COUNTRIES = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]
LAB = {
    "USA": "USA",
    "CHN": "China",
    "KOR": "Korea",
    "JPN": "Japan",
    "DEU": "Germany",
    "GBR": "UK",
    "ISR": "Israel",
    "FRA": "France",
}

plt.rcParams.update(
    {"figure.dpi": 150, "axes.grid": True, "grid.alpha": 0.3, "font.size": 9}
)


def cagr(v0, v1, n):
    if n <= 0 or not np.isfinite(v0) or not np.isfinite(v1) or v0 <= 0 or v1 <= 0:
        return np.nan
    return (v1 / v0) ** (1 / n) - 1


def latest_joint_year(df: pd.DataFrame, var: str) -> int | None:
    sub = df[["country_iso3", "year", var]].dropna()
    if sub.empty:
        return None
    # year present for both USA and CHN
    for y in sorted(sub.year.unique(), reverse=True):
        ys = set(sub.loc[sub.year == y, "country_iso3"])
        if {"USA", "CHN"}.issubset(ys):
            return int(y)
    return None


def load_panel() -> pd.DataFrame:
    core = pd.read_csv(PANEL)
    if TECH.exists():
        tech = pd.read_csv(TECH)
        cols = [c for c in ["country_iso3", "year", "semi_exports_hs8542"] if c in tech.columns]
        if "semi_exports_hs8542" in cols:
            core = core.merge(tech[cols], on=["country_iso3", "year"], how="left")
    return core.sort_values(["country_iso3", "year"]).reset_index(drop=True)


def build_dual_scale(df: pd.DataFrame) -> pd.DataFrame:
    """Central D1 descriptive table: intensity vs volume/share, year on every row.

    Joint years HARD-BOUND to DATA_CANON.md (not auto-max year if 2024 exists).
    """
    # (var, scale, joint_year_canon, cagr_t0, cagr_t1)
    specs = [
        ("gerd_pct_gdp", "intensity", 2023, 2010, 2023),
        ("berd_pct_gdp", "intensity", 2023, 2010, 2023),
        ("researchers_per_million", "intensity", 2022, 2010, 2017),
        ("scopus_articles", "volume", 2023, 2010, 2023),  # dual window handled separately
        ("patents_resident", "volume", 2021, 2010, 2021),
        ("patents_total_office", "volume", 2021, 2010, 2021),
        ("mva_pct_gdp", "share", 2021, 2010, 2021),
        ("hitech_export_share", "share", 2023, 2010, 2023),
        ("semi_exports_hs8542", "volume_nominal", 2023, None, None),
    ]
    us = df[df.country_iso3 == "USA"].set_index("year")
    cn = df[df.country_iso3 == "CHN"].set_index("year")
    rows = []
    for var, scale, jy, t0, t1 in specs:
        if var not in df.columns:
            continue
        if jy is None:
            jy = latest_joint_year(df, var)
        if jy is None:
            continue
        # Prefer canon year; if missing, fall back to latest joint with note
        note = ""
        if jy not in us.index or pd.isna(us.loc[jy, var]) or jy not in cn.index or pd.isna(cn.loc[jy, var]):
            alt = latest_joint_year(df, var)
            note = f"canon joint {jy} missing; fell back to {alt}"
            jy = alt
            if jy is None:
                continue
        usa = float(us.loc[jy, var]) if jy in us.index and pd.notna(us.loc[jy, var]) else np.nan
        chn = float(cn.loc[jy, var]) if jy in cn.index and pd.notna(cn.loc[jy, var]) else np.nan
        ratio = chn / usa if np.isfinite(usa) and usa != 0 and np.isfinite(chn) else np.nan
        if np.isfinite(ratio):
            who = "USA_higher" if ratio < 1 else ("CHN_higher" if ratio > 1 else "equal")
        else:
            who = "NA"
        # CAGR common window
        cagr_usa = cagr_chn = np.nan
        if t0 is not None and t1 is not None:
            try:
                cagr_usa = cagr(float(us.loc[t0, var]), float(us.loc[t1, var]), t1 - t0)
                cagr_chn = cagr(float(cn.loc[t0, var]), float(cn.loc[t1, var]), t1 - t0)
            except Exception:
                pass
        rows.append(
            {
                "var": var,
                "scale_family": scale,
                "joint_year": jy,
                "USA": usa,
                "CHN": chn,
                "CHN_USA_ratio": ratio,
                "gap_sign_level": who,
                "cagr_t0": t0,
                "cagr_t1": t1,
                "CAGR_USA": cagr_usa,
                "CAGR_CHN": cagr_chn,
                "note": note,
            }
        )
    # Articles dual-window rows (explicit)
    for t1, note in [(2021, "dual-window; USA peak year endpoint"), (2023, "dual-window; full analysis horizon")]:
        usa0, usa1 = float(us.loc[2010, "scopus_articles"]), float(us.loc[t1, "scopus_articles"])
        chn0, chn1 = float(cn.loc[2010, "scopus_articles"]), float(cn.loc[t1, "scopus_articles"])
        rows.append(
            {
                "var": "scopus_articles_CAGR_only",
                "scale_family": "volume",
                "joint_year": t1,
                "USA": usa1,
                "CHN": chn1,
                "CHN_USA_ratio": chn1 / usa1,
                "gap_sign_level": "CHN_higher",
                "cagr_t0": 2010,
                "cagr_t1": t1,
                "CAGR_USA": cagr(usa0, usa1, t1 - 2010),
                "CAGR_CHN": cagr(chn0, chn1, t1 - 2010),
                "note": note + "; peak USA 2021=471378",
            }
        )
    out = pd.DataFrame(rows)
    # D1 check column: intensity should be USA_higher; volume/share CHN_higher
    def d1_ok(r):
        if r["scale_family"] == "intensity":
            return r["gap_sign_level"] == "USA_higher"
        if r["scale_family"] in ("volume", "share", "volume_nominal"):
            if r["var"].startswith("scopus_articles_CAGR"):
                return True  # growth rows
            return r["gap_sign_level"] == "CHN_higher"
        return np.nan

    out["matches_D1_sign"] = out.apply(d1_ok, axis=1)
    return out


def pca_fit(X: np.ndarray):
    """Column-standardize then SVD PCA. Returns loadings (p x k), var_exp, scores."""
    mu = X.mean(axis=0)
    sd = X.std(axis=0, ddof=1)
    sd = np.where(sd == 0, 1.0, sd)
    Z = (X - mu) / sd
    U, S, Vt = np.linalg.svd(Z, full_matrices=False)
    loadings = Vt.T  # p x k
    scores = Z @ loadings
    var = S**2
    varexp = var / var.sum()
    return loadings, varexp, scores, Z.shape[0]


def run_pca_variant(df: pd.DataFrame, variant: str) -> dict:
    win = df[(df.year >= 2010) & (df.year <= 2023)].copy()
    meta = {"variant": variant}

    if variant == "a_intensity":
        # intensity-only: GERD%, BERD%, researchers per million (no article counts)
        cols = ["gerd_pct_gdp", "berd_pct_gdp", "researchers_per_million"]
        labels = ["gerd_pct_gdp", "berd_pct_gdp", "researchers_per_million"]
        cc = win.dropna(subset=cols).copy()
        X = cc[cols].to_numpy(float)
        expected_sign = +1  # higher activity → positive loading

    elif variant == "b_logged_volumes":
        cc = win.copy()
        cc["log_articles"] = np.log(cc["scopus_articles"])
        cc["log_patents_resident"] = np.log(cc["patents_resident"])
        cc["log_patents_total"] = np.log(cc["patents_total_office"])
        labels = ["log_articles", "log_patents_resident", "log_patents_total"]
        cc = cc.dropna(subset=labels)
        X = cc[labels].to_numpy(float)
        expected_sign = +1

    elif variant == "c_within_z_intensity":
        # within-country z-score of intensity vars (same scale family)
        cols = ["gerd_pct_gdp", "berd_pct_gdp", "researchers_per_million"]
        labels = [f"wz_{c}" for c in cols]
        cc = win.dropna(subset=cols).copy()
        for c, lab in zip(cols, labels):
            g = cc.groupby("country_iso3")[c]
            cc[lab] = (cc[c] - g.transform("mean")) / g.transform("std")
        cc = cc.dropna(subset=labels)
        X = cc[labels].to_numpy(float)
        expected_sign = +1
        labels = labels

    else:
        raise ValueError(variant)

    if len(X) < 20:
        meta.update({"status": "FAIL", "reason": f"n too small ({len(X)})"})
        return meta

    loadings, varexp, scores, n = pca_fit(X)
    pc1 = loadings[:, 0]
    # Flip so mean loading > 0 for interpretability
    if np.nanmean(pc1) < 0:
        pc1 = -pc1
        scores[:, 0] = -scores[:, 0]

    signs = np.sign(pc1)
    same_sign = np.all(signs == expected_sign) or np.all(signs == -expected_sign)
    # After flip toward positive mean, expect all positive
    all_positive = np.all(pc1 > 0)
    gate = bool(all_positive)

    years = sorted(cc["year"].unique())
    meta.update(
        {
            "n": int(n),
            "year_min": int(min(years)),
            "year_max": int(max(years)),
            "n_countries": int(cc["country_iso3"].nunique()),
            "var_exp_pc1": float(varexp[0]),
            "var_exp_pc2": float(varexp[1]) if len(varexp) > 1 else np.nan,
            "loadings": {lab: float(pc1[i]) for i, lab in enumerate(labels)},
            "all_same_expected_sign": gate,
            "gate": "PASS" if gate else "FAIL",
            "labels": labels,
            "varexp": varexp,
            "pc1_loadings_vec": pc1,
        }
    )
    # save artefacts
    load_df = pd.DataFrame(
        {
            "variable": labels,
            "PC1_loading": pc1,
            "PC2_loading": loadings[:, 1] if loadings.shape[1] > 1 else np.nan,
        }
    )
    # keep orientation consistent with flipped pc1 for PC2? leave raw PC2 from original SVD
    # Rebuild with flipped PC1 only in load_df
    load_path = OUT_RES / f"pca_repair_{variant}_loadings.csv"
    load_df.to_csv(load_path, index=False)
    var_df = pd.DataFrame(
        {"PC": list(range(1, len(varexp) + 1)), "var_exp": varexp}
    )
    var_df.to_csv(OUT_RES / f"pca_repair_{variant}_variance.csv", index=False)
    meta["loadings_file"] = str(load_path.relative_to(ROOT))
    meta["variance_file"] = str((OUT_RES / f"pca_repair_{variant}_variance.csv").relative_to(ROOT))
    return meta


def regenerate_key_figures(df: pd.DataFrame) -> None:
    """Neutral titles; year range on axes. Overwrites figures/F1–F7 worst offenders; F10 untouched."""
    win = df[(df.year >= 2010) & (df.year <= 2023)].copy()

    def savefig(p):
        plt.tight_layout()
        plt.savefig(p, bbox_inches="tight")
        plt.close()

    # F1 GERD — remove "converges"
    plt.figure(figsize=(7, 4))
    for c in COUNTRIES:
        s = win[win.country_iso3 == c].sort_values("year")
        lw = 2.4 if c in ("USA", "CHN") else 1.1
        plt.plot(s.year, s.gerd_pct_gdp, label=LAB[c], linewidth=lw)
    plt.ylabel("GERD (% GDP)")
    plt.title("GERD intensity (% GDP), 2010–2023: levels and trends by country")
    plt.legend(ncol=4, fontsize=7)
    plt.xlim(2010, 2023)
    savefig(OUT_FIG / "F1_gerd_trends.png")

    # F2 researchers — joint year 2022 note; GBR ends 2017
    plt.figure(figsize=(7, 4))
    for c in COUNTRIES:
        s = win[win.country_iso3 == c].sort_values("year")
        lw = 2.4 if c in ("USA", "CHN") else 1.1
        plt.plot(s.year, s.researchers_per_million, label=LAB[c], linewidth=lw)
    plt.ylabel("Researchers per million")
    plt.title(
        "Researchers per million, 2010–2023 (joint US–CN level year 2022; GBR ends 2017; ISR missing)"
    )
    plt.legend(ncol=4, fontsize=7)
    plt.xlim(2010, 2023)
    savefig(OUT_FIG / "F2_researchers.png")

    # F3 articles — remove "overtook"; mark USA peak 2021
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    for c in ("USA", "CHN"):
        s = win[win.country_iso3 == c].sort_values("year")
        ax[0].plot(s.year, s.scopus_articles / 1000, label=LAB[c], linewidth=2.2)
    ax[0].axvline(2021, color="gray", ls="--", lw=1, alpha=0.7, label="USA peak 2021")
    ax[0].set_ylabel("Articles (thousands)")
    ax[0].set_title("Scopus article counts (volume), 2010–2023")
    ax[0].legend(fontsize=7)
    ax[0].set_xlim(2010, 2023)
    us = win[win.country_iso3 == "USA"].set_index("year")["scopus_articles"]
    cn = win[win.country_iso3 == "CHN"].set_index("year")["scopus_articles"]
    common = us.index.intersection(cn.index)
    ax[1].plot(common, (cn.loc[common] / us.loc[common]).values, color="C2", lw=2)
    ax[1].axhline(1, color="k", lw=0.8)
    ax[1].set_title("CHN/USA article-count ratio by year")
    ax[1].set_xlim(2010, 2023)
    ax[1].set_ylabel("CHN / USA")
    savefig(OUT_FIG / "F3_articles_crossover.png")

    # F4 patents
    plt.figure(figsize=(7, 4))
    for c in ("USA", "CHN", "JPN", "KOR"):
        s = win[win.country_iso3 == c].sort_values("year")
        s = s.dropna(subset=["patents_resident"])
        plt.semilogy(
            s.year,
            s.patents_resident,
            label=LAB[c],
            linewidth=2 if c in ("USA", "CHN") else 1.1,
        )
    plt.ylabel("Resident patent applications (log scale)")
    plt.title("Patent counts (office-basis resident), 2010–2021 — quantity, not quality")
    plt.legend(fontsize=7)
    plt.xlim(2010, 2021)
    savefig(OUT_FIG / "F4_patents_log.png")

    # F5 MVA — explicit years
    plt.figure(figsize=(7, 4))
    for c in COUNTRIES:
        s = win[win.country_iso3 == c].sort_values("year")
        lw = 2.4 if c in ("USA", "CHN") else 1.1
        plt.plot(s.year, s.mva_pct_gdp, label=LAB[c], linewidth=lw)
    plt.ylabel("MVA (% GDP)")
    plt.title("Manufacturing value added (% GDP), 2010–2021 joint window (USA/CHN levels ~2021)")
    plt.legend(ncol=4, fontsize=7)
    plt.xlim(2010, 2023)
    savefig(OUT_FIG / "F5_mva_share.png")

    # F6 hitech — vertical lines = markers only
    plt.figure(figsize=(7, 4))
    for c in COUNTRIES:
        s = win[win.country_iso3 == c].sort_values("year")
        lw = 2.4 if c in ("USA", "CHN") else 1.1
        plt.plot(s.year, s.hitech_export_share, label=LAB[c], linewidth=lw)
    plt.axvline(2022.6, color="gray", ls="--", lw=1, alpha=0.8)
    plt.text(2022.7, 32, "CHIPS/BIS\n(markers only)", fontsize=6, color="gray")
    plt.ylabel("High-tech exports (% mfg exports)")
    plt.title("High-tech export share (% manuf. exports), 2010–2023 — broad basket, not semis-only")
    plt.legend(ncol=4, fontsize=7)
    plt.xlim(2010, 2023)
    savefig(OUT_FIG / "F6_hitech_exports.png")

    # F7 TFP
    plt.figure(figsize=(7, 4))
    for c in [x for x in COUNTRIES if x != "USA"]:
        s = win[win.country_iso3 == c].sort_values("year")
        plt.plot(s.year, s.tfp_ctfp, label=LAB[c], linewidth=1.4)
    plt.axhline(1, color="black", ls="-", lw=1.2, label="USA = 1.00 (by construction)")
    plt.ylabel("TFP level (PWT ctfp, USA=1 each year)")
    plt.title("Aggregate TFP levels, 2010–2023 (USA=1 by construction; macro proxy, not tech-TFP)")
    plt.legend(ncol=4, fontsize=7)
    plt.xlim(2010, 2023)
    savefig(OUT_FIG / "F7_tfp_levels.png")


def write_appendix_pc1_figure(df: pd.DataFrame, variant_meta: dict) -> None:
    """Descriptive PC1 time series only — NOT TFP scatter; replaces role of F10 in appendix."""
    if not variant_meta or variant_meta.get("gate") != "PASS":
        return
    win = df[(df.year >= 2010) & (df.year <= 2023)].copy()
    cols = ["gerd_pct_gdp", "berd_pct_gdp", "researchers_per_million"]
    cc = win.dropna(subset=cols).copy()
    X = cc[cols].to_numpy(float)
    loadings, varexp, scores, n = pca_fit(X)
    pc1 = loadings[:, 0]
    if np.nanmean(pc1) < 0:
        pc1 = -pc1
        scores[:, 0] = -scores[:, 0]
    cc = cc.copy()
    cc["pc1_intensity"] = scores[:, 0]
    cc[["country_iso3", "year", "pc1_intensity"]].to_csv(
        OUT_RES / "pca_repair_a_intensity_scores.csv", index=False
    )
    plt.figure(figsize=(7, 4))
    for c in COUNTRIES:
        s = cc[cc.country_iso3 == c].sort_values("year")
        if s.empty:
            continue
        lw = 2.4 if c in ("USA", "CHN") else 1.1
        plt.plot(s.year, s.pc1_intensity, label=LAB[c], linewidth=lw)
    plt.ylabel("PC1 (intensity-only, standardized inputs)")
    plt.title(
        f"Appendix: intensity PC1 (GERD, BERD, researchers/mn), 2010–2023; "
        f"var≈{varexp[0]*100:.0f}%, n={n} — descriptive index, not TFP cause"
    )
    plt.legend(ncol=4, fontsize=7)
    plt.xlim(2010, 2023)
    plt.tight_layout()
    out = OUT_FIG_REV / "F10_appendix_pc1_intensity_ONLY.png"
    plt.savefig(out, bbox_inches="tight")
    plt.close()
    # Do NOT overwrite figures/F10 — leave old DO NOT USE in place



def main():
    df = load_panel()

    dual = build_dual_scale(df)
    dual_path = OUT_TAB / "dual_scale_intensity_volume.csv"
    dual.to_csv(dual_path, index=False)

    # Compact US–CN D1 summary
    summary = dual[~dual["var"].str.contains("CAGR_only")].copy()
    summary_path = OUT_TAB / "dual_scale_D1_summary.csv"
    summary[
        [
            "var",
            "scale_family",
            "joint_year",
            "USA",
            "CHN",
            "CHN_USA_ratio",
            "gap_sign_level",
            "matches_D1_sign",
            "cagr_t0",
            "cagr_t1",
            "CAGR_USA",
            "CAGR_CHN",
        ]
    ].to_csv(summary_path, index=False)

    # PCA repair cycle: try a, then b, then c until pass
    results = []
    chosen = None
    for v in ("a_intensity", "b_logged_volumes", "c_within_z_intensity"):
        r = run_pca_variant(df, v)
        results.append(r)
        print(
            f"PCA {v}: gate={r.get('gate')} n={r.get('n')} "
            f"var_exp_pc1={r.get('var_exp_pc1')} loadings={r.get('loadings')}"
        )
        if r.get("gate") == "PASS" and chosen is None:
            chosen = r

    gate_rows = []
    for r in results:
        gate_rows.append(
            {
                "variant": r["variant"],
                "gate": r.get("gate"),
                "n": r.get("n"),
                "year_min": r.get("year_min"),
                "year_max": r.get("year_max"),
                "n_countries": r.get("n_countries"),
                "var_exp_pc1": r.get("var_exp_pc1"),
                "loadings_json": str(r.get("loadings")),
                "selected": chosen is not None and r["variant"] == chosen["variant"],
            }
        )
    gate_df = pd.DataFrame(gate_rows)
    gate_df.to_csv(OUT_RES / "pca_repair_gate_summary.csv", index=False)

    verdict_path = OUT_RES / "pca_repair_verdict.txt"
    if chosen:
        verdict_path.write_text(
            f"PASS\nvariant={chosen['variant']}\n"
            f"n={chosen['n']} years={chosen['year_min']}-{chosen['year_max']}\n"
            f"var_exp_pc1={chosen['var_exp_pc1']:.4f}\n"
            f"loadings={chosen['loadings']}\n"
            f"M2=OPTIONAL_SECONDARY_ONLY\n"
            f"old_pca_loadings.csv=DO_NOT_USE\n",
            encoding="utf-8",
        )
        # Write canonical repair loadings pointer
        rep = pd.read_csv(ROOT / chosen["loadings_file"])
        rep.to_csv(OUT_RES / "pca_repair_selected_loadings.csv", index=False)
        pd.DataFrame(
            {
                "PC": list(range(1, len(chosen["varexp"]) + 1)),
                "var_exp": chosen["varexp"],
            }
        ).to_csv(OUT_RES / "pca_repair_selected_variance.csv", index=False)
    else:
        verdict_path.write_text(
            "FAIL\nall variants a/b/c failed success gate OR none selected\n"
            "DROP PCA from argument\n"
            "see PCA_WHY_FAILED.md\n"
            "F10=DO_NOT_USE\n"
            "M2=DO_NOT_FORCE\n",
            encoding="utf-8",
        )

    regenerate_key_figures(df)
    if chosen:
        write_appendix_pc1_figure(df, chosen)
    print("Wrote", dual_path)
    print("PCA chosen:", None if chosen is None else chosen["variant"], chosen and chosen.get("gate"))
    print("D1 level support rates:\n", dual.groupby("scale_family")["matches_D1_sign"].mean())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the reproducible minimum US-China technology dataset and QA artefacts.

Only source files already present in data/raw are used for the core panel.  A
TOP500 November snapshot is downloaded from the official list pages when
available.  Rows with an unresolved source-definition problem are retained in
raw data but excluded from cleaned analytical panels.
"""
from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
META = ROOT / "data" / "metadata"
REPORTS = ROOT / "reports"
COUNTRIES = ["USA", "CHN", "KOR", "JPN", "DEU", "GBR", "ISR", "FRA"]
YEARS = list(range(2000, 2025))
TODAY = date.today().isoformat()


def read_series(filename: str, value_col: str = "value", out_name: str | None = None) -> pd.DataFrame:
    path = RAW / filename
    if not path.exists():
        return pd.DataFrame(columns=["country_iso3", "year", out_name or value_col])
    df = pd.read_csv(path)
    if value_col not in df.columns:
        return pd.DataFrame(columns=["country_iso3", "year", out_name or value_col])
    df = df[["country_iso3", "year", value_col]].copy()
    df["country_iso3"] = df["country_iso3"].replace({"CN": "CHN", "US": "USA", "KR": "KOR", "JP": "JPN", "DE": "DEU", "GB": "GBR", "IL": "ISR", "FR": "FRA"})
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
    df = df[df.country_iso3.isin(COUNTRIES) & df.year.isin(YEARS)].drop_duplicates(["country_iso3", "year"])
    return df.rename(columns={value_col: out_name or value_col})


def build_top500() -> tuple[pd.DataFrame, str]:
    """Download Nov. list pages; return a country count series and outcome note.

    TOP500's HTML is the official publication.  We deliberately use only the
    November release so an annual observation has a stable reference date.
    """
    target = RAW / "hpc_top500_systems.csv"
    if target.exists():
        return pd.read_csv(target), "existing official TOP500 extract reused"
    if os.environ.get("SKIP_TOP500") == "1":
        return pd.DataFrame(), "not collected in this run; TOP500 HTML extraction requires a separate validated download"
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError as exc:
        return pd.DataFrame(), f"not collected: {exc}"
    aliases = {"United States": "USA", "China": "CHN", "South Korea": "KOR", "Japan": "JPN", "Germany": "DEU", "United Kingdom": "GBR", "Israel": "ISR", "France": "FRA"}
    records = []
    headers = {"User-Agent": "Mozilla/5.0 (research data collection; contact: reproducibility)"}
    try:
        for year in range(2010, 2025):
            frames = []
            base_url = f"https://www.top500.org/lists/top500/list/{year}/11/"
            # Each official list is paginated into five tables of 100 systems.
            for page in range(1, 6):
                url = base_url if page == 1 else f"{base_url}?page={page}"
                response = requests.get(url, headers=headers, timeout=45)
                response.raise_for_status()
                tables = pd.read_html(response.text)
                table = max(tables, key=len)
                if len(table) != 100 or "System" not in table.columns:
                    raise ValueError(f"unexpected table for {year}, page {page}")
                frames.append(table)
            table = pd.concat(frames, ignore_index=True)
            # Country is embedded as the final part of TOP500's 'System' display
            # cell, rather than exposed as an HTML column.
            country = pd.Series(index=table.index, dtype="object")
            text = table["System"].astype(str).str.strip()
            for label, iso in aliases.items():
                country.loc[text.str.endswith(label)] = iso
            matched = country.notna().sum()
            if matched < 400:
                raise ValueError(f"only {matched} country labels identified for {year}")
            table["country_iso3"] = country
            table["rmax_tflops"] = pd.to_numeric(table["Rmax (TFlop/s)"].astype(str).str.replace(",", "", regex=False), errors="coerce")
            agg = table.dropna(subset=["country_iso3"]).groupby("country_iso3").agg(value=("country_iso3", "size"), rmax_tflops=("rmax_tflops", "sum"))
            for country, row in agg.iterrows():
                records.append({"country_iso3": country, "year": year, "value": int(row.value), "rmax_tflops": row.rmax_tflops, "snapshot": "November", "source_url": base_url})
        output = pd.DataFrame(records).sort_values(["country_iso3", "year"])
        output.to_csv(target, index=False)
        return output, "downloaded official November lists 2010-2024"
    except Exception as exc:
        return pd.DataFrame(), f"not collected: {type(exc).__name__}: {exc}"


def audit_series(name: str, df: pd.DataFrame, status: str, caveat: str) -> dict:
    value = df[name] if name in df else pd.Series(dtype=float)
    nonmissing = int(value.notna().sum())
    duplicate = int(df.duplicated(["country_iso3", "year"]).sum())
    jumps = []
    for country, group in df[["country_iso3", "year", name]].dropna().groupby("country_iso3"):
        group = group.sort_values("year")
        pct = group[name].pct_change()
        for _, row in group.loc[pct.abs() > 1.0].iterrows():
            jumps.append(f"{country}-{int(row.year)}")
    return {"variable": name, "status": status, "nonmissing": nonmissing,
            "expected": len(COUNTRIES) * len(YEARS), "missing_pct": round(100 * (1 - nonmissing / (len(COUNTRIES) * len(YEARS))), 1),
            "duplicate_country_year": duplicate, "suspicious_jumps_gt100pct": "; ".join(jumps[:12]) or "none", "caveat": caveat}


def main() -> None:
    PROCESSED.mkdir(parents=True, exist_ok=True); META.mkdir(parents=True, exist_ok=True); REPORTS.mkdir(parents=True, exist_ok=True)
    base = pd.MultiIndex.from_product([COUNTRIES, YEARS], names=["country_iso3", "year"]).to_frame(index=False)

    specs = [
        ("gerd_pct_gdp", "gerd_pct_gdp.csv", "value", "VALID WITH CAVEAT", "WB WDI series, chiefly UNESCO-derived; use latest vintage only; China GDP revisions affect ratio."),
        ("researchers_per_million", "researchers_per_million.csv", "value", "VALID WITH CAVEAT", "UNESCO/WDI coverage is intermittent; headcount/FTE treatment may differ by national reporting."),
        ("scopus_articles", "scopus_articles.csv", "value", "VALID WITH CAVEAT", "WDI scientific-and-technical articles, not field-specific Scopus counts; volume, not impact."),
        ("patents_resident", "patents_resident.csv", "value", "VALID WITH CAVEAT", "Resident applications (WIPO origin via WDI), not quality-adjusted; do not interpret quantity as quality."),
        ("mva_pct_gdp", "mva_pct_gdp.csv", "value", "VALID", "Manufacturing value added as % GDP; macro manufacturing structure, not semiconductor capacity."),
        ("hitech_export_share", "hitech_export_share.csv", "value", "VALID WITH CAVEAT", "WDI high-tech basket; definition/revision break flagged by World Bank (SITC Rev.4 update); China processing trade caveat."),
        ("gdp_pc_ppp", "gdp_pc_ppp.csv", "value", "VALID WITH CAVEAT", "WDI constant PPP dollars; kept for normalization only; compare within a single WDI vintage."),
        ("tfp_ctfp", "pwt_ctfp.csv", "ctfp", "VALID WITH CAVEAT", "PWT aggregate TFP at constant PPPs; macro context only, not technology-sector productivity."),
        ("berd_pct_gdp", "oecd_berd_pct_gdp.csv", "value", "VALID WITH CAVEAT", "OECD MSTI business R&D intensity; no Taiwan observation in this extraction."),
    ]
    raw_frames = {}
    quality = []
    panel = base.copy()
    for name, filename, value_col, status, caveat in specs:
        s = read_series(filename, value_col, name)
        raw_frames[name] = s
        panel = panel.merge(s, on=["country_iso3", "year"], how="left", validate="one_to_one")
        quality.append(audit_series(name, panel[["country_iso3", "year", name]], status, caveat))

    # Semiconductor trade: existing raw contains aggregation warnings.  Retain only
    # country-years whose source response was one record; multi-record sums do not
    # establish a single reporter/flow/product definition and are quarantined.
    clean_comtrade = RAW / "comtrade_hs8542_exports_clean.csv"
    semi_raw = pd.read_csv(clean_comtrade) if clean_comtrade.exists() else (pd.read_csv(RAW / "comtrade_hs8542_exports.csv") if (RAW / "comtrade_hs8542_exports.csv").exists() else pd.DataFrame())
    if not semi_raw.empty and clean_comtrade.exists():
        semi_clean = semi_raw[(semi_raw.country_iso3.isin(COUNTRIES)) & (semi_raw.year.isin(YEARS))].copy()
        semi_clean = semi_clean.rename(columns={"value_usd": "semi_exports_hs8542"})[["country_iso3", "year", "semi_exports_hs8542"]]
    elif not semi_raw.empty:
        semi_raw["country_iso3"] = semi_raw.country_iso3.replace({"CN": "CHN"})
        semi_clean = semi_raw[(semi_raw.country_iso3.isin(COUNTRIES)) & (semi_raw.year.isin(YEARS)) & (semi_raw.num_records == 1)].copy()
        semi_clean = semi_clean.rename(columns={"value_usd": "semi_exports_hs8542"})[["country_iso3", "year", "semi_exports_hs8542"]]
    else:
        semi_clean = pd.DataFrame(columns=["country_iso3", "year", "semi_exports_hs8542"])
    tech = base.merge(semi_clean, on=["country_iso3", "year"], how="left", validate="one_to_one")
    semi_note = "UN Comtrade HS8542 nominal USD exports; USA and China come from a fixed-parameter official API pull (world partner, export flow). Other countries use only unambiguous one-record legacy responses. Trade is not fab capacity; re-exports/processing trade remain material." if clean_comtrade.exists() else "UN Comtrade HS8542 nominal USD exports; only unambiguous one-record responses retained. Trade is not fab capacity; re-exports/processing trade remain material."
    quality.append(audit_series("semi_exports_hs8542", tech, "VALID WITH CAVEAT", semi_note))

    hpc, hpc_note = build_top500()
    if not hpc.empty:
        hpc = hpc[["country_iso3", "year", "value", "rmax_tflops"]].rename(columns={"value": "hpc_top500_systems", "rmax_tflops": "hpc_top500_rmax_tflops"})
        tech = tech.merge(hpc, on=["country_iso3", "year"], how="left", validate="one_to_one")
        quality.append(audit_series("hpc_top500_systems", tech, "VALID WITH CAVEAT", "Official TOP500 November snapshot; listed systems, not cloud AI compute; site country differs from ownership."))
        quality.append(audit_series("hpc_top500_rmax_tflops", tech, "VALID WITH CAVEAT", "Sum of official TOP500 Rmax values in TFlop/s, November snapshot; listed systems only, not cloud AI compute."))
    else:
        tech["hpc_top500_systems"] = np.nan
        tech["hpc_top500_rmax_tflops"] = np.nan
        quality.append(audit_series("hpc_top500_systems", tech, "MISSING", hpc_note))
        quality.append(audit_series("hpc_top500_rmax_tflops", tech, "MISSING", hpc_note))

    # No reproducibly machine-readable Stanford country-year publication/citation
    # extract or EPO-OECD country-year quantum table is in the workspace.  Do not
    # manufacture values from chart reading.
    for col, note in [
        ("ai_publications_count", "MISSING: Stanford AI Index report/tool is identified, but no audited country-year raw export is stored. Do not substitute generic article counts."),
        ("ai_citations_impact", "MISSING: no consistently defined country-year impact series stored."),
        ("ai_private_investment_usd_bn", "MISSING: proprietary deal coverage and China undercoverage make an unverified substitute unsuitable."),
        ("ai_notable_models", "MISSING: available report snapshots are not a historical country-year panel."),
        ("quantum_ipf_count", "MISSING: EPO-OECD report is comparable but extraction from charts was not performed; no synthetic reconstruction."),
        ("quantum_publications", "MISSING: no audited country-year extract."),
    ]:
        tech[col] = np.nan
        quality.append(audit_series(col, tech, "MISSING", note))

    panel.to_csv(PROCESSED / "core_panel.csv", index=False)
    tech.to_csv(PROCESSED / "tech_panel.csv", index=False)
    pd.DataFrame(quality).to_csv(PROCESSED / "indicator_quality.csv", index=False)

    dictionary = pd.DataFrame([
        ["gerd_pct_gdp", "R&D expenditure (% GDP)", "RD", "% GDP", "World Bank WDI", "GB.XPD.RSDV.GD.ZS", "2000-2024", "VALID WITH CAVEAT"],
        ["researchers_per_million", "Researchers in R&D", "HC", "per million people", "World Bank WDI / UNESCO UIS", "SP.POP.SCIE.RD.P6", "2000-2024", "VALID WITH CAVEAT"],
        ["scopus_articles", "Scientific and technical journal articles", "S", "count", "World Bank WDI", "IP.JRN.ARTC.SC", "2000-2024", "VALID WITH CAVEAT"],
        ["patents_resident", "Resident patent applications", "INN", "count", "World Bank WDI / WIPO", "IP.PAT.RESD", "2000-2024", "VALID WITH CAVEAT"],
        ["mva_pct_gdp", "Manufacturing value added", "PRD", "% GDP", "World Bank WDI", "NV.IND.MANF.ZS", "2000-2024", "VALID"],
        ["hitech_export_share", "High-tech exports", "ADE", "% manufactured exports", "World Bank WDI / UN Comtrade", "TX.VAL.TECH.MF.ZS", "2000-2024", "VALID WITH CAVEAT"],
        ["gdp_pc_ppp", "GDP per capita, PPP constant", "Macro", "constant international $", "World Bank WDI", "NY.GDP.PCAP.PP.KD", "2000-2024", "VALID WITH CAVEAT"],
        ["tfp_ctfp", "TFP at constant PPPs", "Productivity", "index", "Penn World Table mirror", "ctfp", "2000-2023", "VALID WITH CAVEAT"],
        ["berd_pct_gdp", "Business R&D expenditure", "FIN", "% GDP", "OECD MSTI", "MSTI measure B", "2000-2024", "VALID WITH CAVEAT"],
        ["semi_exports_hs8542", "Integrated-circuit exports", "ADE/PRD", "current USD", "UN Comtrade", "HS 8542", "2010-2023", "VALID WITH CAVEAT"],
        ["hpc_top500_systems", "TOP500 systems", "PRD", "count", "TOP500", "November list", "2010-2024", "VALID WITH CAVEAT" if not hpc.empty else "MISSING"],
        ["hpc_top500_rmax_tflops", "TOP500 aggregate Rmax", "PRD", "TFlop/s", "TOP500", "November list", "2010-2024", "VALID WITH CAVEAT" if not hpc.empty else "MISSING"],
        ["ai_publications_count", "AI publications", "S/INN", "count", "Stanford AI Index", "publication metric", "2010-2024", "MISSING"],
        ["ai_citations_impact", "AI citation impact", "S/INN", "index/count", "Stanford AI Index", "impact metric", "2010-2024", "MISSING"],
        ["ai_private_investment_usd_bn", "AI private investment", "FIN/COM", "USD billions", "Stanford AI Index", "private investment", "2013-2024", "MISSING"],
        ["ai_notable_models", "Notable AI models", "INN/COM", "count", "Stanford AI Index", "notable models", "snapshot", "MISSING"],
        ["quantum_ipf_count", "Quantum international patent families", "S/INN", "fractional families", "EPO-OECD", "quantum IPF", "2005-2024", "MISSING"],
        ["quantum_publications", "Quantum publications", "S", "count", "EPO-OECD", "publication metric", "partial", "MISSING"],
    ], columns=["variable", "label", "tci_block", "unit", "source", "source_series", "intended_period", "comparability_status"])
    dictionary.to_csv(META / "data_dictionary.csv", index=False)

    registry = pd.DataFrame([
        ["World Bank WDI", "https://api.worldbank.org/v2/", "2026-09-12", "core raw files", "fresh as downloaded; provider vintage not independently archived", "WDI country-series API"],
        ["OECD MSTI", "https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI", "2026-09-13", "oecd_berd_pct_gdp.csv", "freshness verified by stored extraction date", "annual SDMX, measure B / % GDP"],
        ["Penn World Table", "https://raw.githubusercontent.com/open-numbers/ddf--pwt--penn_world_table/", "2026-09-13", "pwt_ctfp.csv", "mirror provenance; version must be rechecked before publication", "country-year CSV mirror"],
        ["UN Comtrade", "https://comtradeplus.un.org/", "2026-09-13", "comtrade_hs8542_exports.csv", "2023 latest retained in raw", "HS8542 export responses; multi-record rows quarantined"],
        ["TOP500", "https://www.top500.org/lists/top500/", TODAY, "hpc_top500_systems.csv", hpc_note, "November annual snapshot"],
        ["Stanford AI Index", "https://hai.stanford.edu/ai-index/2025-ai-index-report", TODAY, "not downloaded", "source identified, no audited raw extract", "do not use until raw export is archived"],
        ["EPO-OECD quantum", "https://www.oecd.org/en/publications/mapping-the-global-quantum-ecosystem_010c37da-en.html", TODAY, "not downloaded", "source identified, no audited country-year raw extract", "do not chart-digitise without review"],
    ], columns=["source", "url", "access_or_download_date", "local_artifact", "freshness_status", "method_or_scope"])
    registry.to_csv(META / "source_registry.csv", index=False)

    q = pd.DataFrame(quality)
    valid = q[q.status.str.startswith("VALID")].variable.tolist()
    semi_rule = "UN Comtrade HS8542 USA and China rows are a fixed-parameter API pull (world partner, export flow, HS8542); earlier multi-record rows remain quarantined. Comparator legacy rows with `num_records > 1` remain excluded." if clean_comtrade.exists() else "UN Comtrade HS8542 rows with `num_records > 1` are quarantined from the cleaned panel because the stored extract does not prove a single consistent aggregation. This affects China in 2015-2017 and several comparator years."
    semi_ready = "HS8542 is a complete USA-China descriptive trend from one official API definition; comparator coverage remains incomplete." if clean_comtrade.exists() else "HS8542 requires a new, single-definition Comtrade pull for a complete US-China trend."
    report = ["# Data quality report", "", f"Generated: {TODAY}. Analytical country set: {', '.join(COUNTRIES)}. Core panel grid: {len(base)} country-year rows (2000-2024).", "", "## Results", "", q.to_markdown(index=False), "", "## Dataset rules", "", "- Raw source files are preserved unchanged in `data/raw/`.", "- `core_panel.csv` is a country × year wide panel. No interpolation, backfilling, or cross-source replacement was applied.", "- `tech_panel.csv` contains only audited semiconductor/HPC observations; unavailable AI and quantum fields remain null by design.", "- " + semi_rule, "- PWT TFP is a macro proxy, not an estimate of technology-specific productivity. It must not be used to attribute productivity changes to AI, semiconductors, HPC, or quantum.", "- High-tech exports use a broad commodity basket and should not be treated as a semiconductor or AI-export measure. The documented WDI classification update is a potential series break.", "", "## Ready for analysis", "", "Ready, subject to the listed caveats: " + ", ".join(valid) + ".", "", "Not ready for econometric use: AI publications/citations/investment/frontier models and quantum series (all missing); " + semi_ready, "", "## Cross-country comparability", "", "USA and China are comparable within each retained provider series, not across differently defined indicators. The principal country-specific risks are China processing trade (exports), China GDP revisions (ratios), national R&D-personnel reporting practices, patent-quality composition, and TOP500 coverage of listed on-premise systems rather than cloud compute."]
    (REPORTS / "data_quality_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Built {PROCESSED / 'core_panel.csv'} and {PROCESSED / 'tech_panel.csv'}")


if __name__ == "__main__":
    main()

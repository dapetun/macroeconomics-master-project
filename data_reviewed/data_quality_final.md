# Data Quality Final Review (independent reviewer)

Date: 2026-09-14. Scope: **quantitative data preparation only**. No new technology-leadership conclusions are drawn. Original files under `data/`, `results/`, `figures/`, `reports/`, `scripts/` were left untouched; all reviewed artefacts are under `data_reviewed/`.

Method: re-read every raw file to processed panel to results/figures link; recomputed missingness, joins, definitions, transformations, and effective samples. Builder: `scripts/build_reviewed_dataset.py` (no imputation, no backfill, no cross-source replacement).

Panel geometry: 8 countries (USA, CHN, KOR, JPN, DEU, GBR, ISR, FRA) x 2000-2024 = **200 rows**. Analysis window used by `analysis_agent4.py` is 2010-2023 (14 years, 112 cells).

## 1. Verdicts

### Ready with caveats (10 + 1 reviewed addition)

| Variable | Raw file | Kept / 200 | Missing pattern (source-driven) | Corrected definition | Severity |
|---|---|---|---|---|---|
| `gerd_pct_gdp` | `gerd_pct_gdp.csv` (WB `GB.XPD.RSDV.GD.ZS`, UNESCO-derived) | 192 | all-2024 (raw ends 2023) | R&D expenditure % GDP; **not** OECD MSTI; China NBS GDP revisions affect denominator | LOW |
| `researchers_per_million` | `researchers_per_million.csv` (WDI `SP.POP.SCIE.RD.P6`, UNESCO-UIS) | 161 | ISR 25/25 missing (no WB record); GBR ends 2017 (2018-24 missing); USA ends 2022; all-2024 missing | Headcount/FTE practice differs; per-million denominator favours small populations | HIGH for ISR/GBR comparisons |
| `scopus_articles` | `scopus_articles.csv` (WDI `IP.JRN.ARTC.SC`) | 192 | all-2024 | **Fractional-count S&E volume** (decimals observed), NSF-derived; volume not impact; not field/AI-specific | MEDIUM |
| `patents_resident` | `patents_resident.csv` (WDI `IP.PAT.RESD`) | 176 | 2022-24 all missing (raw 2000-2021) | **Resident filings AT national office (office basis), NOT WIPO origin** despite old label; counts not quality; CN 2021 subsidy-peak composition | HIGH for level comparisons |
| `patents_total_office` (reviewed addition) | resident + `patents_nonresident.csv` (perfect 176/176 join, same 2000-2021) | 176 | same as above | Total office filings (office basis); still counts not quality. 2021 CHN/USA: resident-only 5.44x vs office-total **2.68x** — resident-only overstates gap | MEDIUM (fixes part of bias) |
| `mva_pct_gdp` | `mva_pct_gdp.csv` (WDI `NV.IND.MANF.ZS`) | 193 | CHN 2000-03 + USA 2022-24 missing in raw | Share of GDP, **not absolute scale**; macro manufacturing, not semi capacity | MEDIUM |
| `hitech_export_share` | `hitech_export_share.csv` (WDI `TX.VAL.TECH.MF.ZS`) | 144 | 2000-06 all missing (series starts 2007) | Broad high-tech basket; **SITC Rev.4 break + ISR 7.6% (2007)->17.1% (2008)->23.4% (2009) instability**; CHN processing-trade bias | HIGH for early-year trends |
| `gdp_pc_ppp` | `gdp_pc_ppp.csv` (WDI `NY.GDP.PCAP.PP.KD`, constant 2017 intl-$) | 200 | none (2024 present; treat as preliminary) | Single Sep-2026 vintage; normalization only | LOW |
| `tfp_ctfp` | `pwt_ctfp.csv` (PWT mirror, `ctfp`) | 192 | all-2024 | **USA = 1.000 every year by construction** (verified 1994-2023). CHN 0.395 (2010) -> 0.471 (2023) reads ONLY as gap to contemporaneous frontier. Macro TFP, not tech-TFP | HIGH if USA trend estimated |
| `berd_pct_gdp` | `oecd_berd_pct_gdp.csv` (OECD MSTI `P_BERPCT`) | 200 | none | **BERD PERFORMED % GDP, NOT business-financed** (F9 old title wrong). Different provider/vintage from WB GERD: **ISR BERD>GERD 2021-23** (2023: 6.50 > 6.35) proves no decomposition; never compute GERD-BERD | HIGH for finance-mix use |
| `semi_exports_hs8542` | `comtrade_hs8542_exports.csv` (legacy; values unchanged) | 75 kept / 125 missing | 2000-09 out of window by design; CHN 2015-17 quarantined (157/170/160 records); DEU 0 kept (all multi-record 10/10/5/6); FRA 0 (no response); GBR 8 kept (2010-16+2018) | Nominal USD HS8542, **mixed HS revisions** (USA clean pull shows H3 2010-11 / H4 2012-16 / H5 2017-21 / H6 2022-24); re-export/processing bias; CHN 2012-13 +63%/+63%, KOR 2016-17 +65% spikes retained-but-flagged; trade value not fab capacity | HIGH; comparator-incomplete |

### Excluded — not ready for econometric use (all 100% missing in panels; correctly left as NaN)

`hpc_top500_systems`, `hpc_top500_rmax_tflops` (no audited TOP500 country-year extract in workspace), `ai_publications_count`, `ai_citations_impact`, `ai_private_investment_usd_bn`, `ai_notable_models` (Stanford HTML folder present, no audited country-year export; generic article counts must not substitute), `quantum_ipf_count`, `quantum_publications` (EPO-OECD source identified, no chart-digitised extraction), plus `gvc_foreign_va_share` / VC investment (planned in data_map, never collected — no raw file, no panel column; must not appear in results).

## 2. Lineage issue fixed by documentation (not by value edits)

`data/raw/comtrade_hs8542_exports_clean.csv` is USA-only (15 rows, 2010-2024) from a fixed-parameter API pull (world partner, export flow). `data/processed/tech_panel.csv` (75 kept rows: USA/CHN/KOR/JPN/GBR/ISR) was built from the legacy file under the `num_records==1` rule, **not** from the clean file — the build script's `if clean exists use clean-only` branch would produce a USA-only panel and does not reproduce the stored panel. The partial clean file is therefore a stale parallel artefact, not the panel's source. Reviewed panel keeps the 75 legacy values unchanged and adds `semi_status` per country-year (`retained_one_record` / `quarantined_multi_record` / `missing_no_response`; map in `tables_reviewed/semi_quarantine_map.csv`). A complete single-definition multi-reporter Comtrade re-pull is still required before any comparator-level semi trend claim; until then DEU/FRA semi are unusable and CHN 2015-17 is a hard gap.

## 3. Transformations / calculations audit (published outputs)

- **D1 snapshot** (`descriptive_snapshot_US_CHN.csv`): correctly shows NaN for jointly-missing 2023 cells (patents 2023, researchers USA 2023, MVA USA 2023, semi CHN 2015). Fix provided: `tables_reviewed/descriptive_snapshot_latest_joint.csv` (latest jointly-available year per variable; e.g. researchers 2022 ratio 0.375, patents 2021 resident 5.44 vs office-total 2.68, MVA 2021).
- **D2 CAGR** (`descriptive_cagr.csv`): mathematically correct from endpoints but **incomparable windows** for researchers (GBR 2010-17 vs others 2010-23/22), MVA (USA 2010-21 vs others 2010-23), semi (GBR 2010-18 vs others 2010-23; CHN interior gap ignored), TFP USA 0 by construction. Fix provided: `tables_reviewed/descriptive_cagr_common_window.csv` with balanced windows (researchers 2010-17, patents/total 2010-21, MVA 2010-21, rest 2010-23; TFP USA excluded from ranking).
- **D3 slopes/convergence**: same unbalanced-window problem (GBR researchers n=8 vs others n=13-14; ISR absent); TFP USA slope is 0 by construction and pooled CHN-minus-USA TFP slope inherits the normalization. Use only with balanced-window note; do not rank USA TFP trend.
- **D4 conversion ratios**: units mix fractional articles with headcount/FTE researchers and subsidy-peak patent counts; descriptive only, not a rating.
- **Pooled correlations** (`correlations_pooled.csv`, `correlations_tfp_inputs.csv`): pooled across countries/years with trends; descriptive only, not causal.
- **M1 FE** (TFP on lagged GERD + log researchers, country+year FE, HC1): effective **n=84** (CHN/DEU/FRA/JPN/KOR 13, USA 12, GBR 7, **ISR 0**); 2011-2023 (2010 lost to lag; 2024 all-missing). Slopes identified off non-USA within-variation (USA TFP constant); k ~ 2 + 7 country + 12 year dummies leaves small residual df — SEs fragile. `tables_reviewed/model1_effective_n.csv`.
- **PCA + M2**: complete-case n=**91** (all 14 except GBR 8, USA 13, **ISR 0**); PC1 loadings estimated without ISR; lag loses another year. `tables_reviewed/pca_effective_n.csv`. Existing `key_findings.csv` already marks M2/PC1 "DO NOT USE / incoherent" — endorsed.
- **Event pre/post** (2020-21 vs 2022-23, n=2/cell): nominal USD + H5->H6 break inside window + processing bias; descriptive only (already labelled "not causal" — endorsed).
- **F2 researchers**: ISR absent line + GBR stop 2017 + USA stop 2022 are source facts; keep title note.
- **F7 TFP**: USA=1 line correctly labelled "by construction" — endorsed; do not add USA slope.
- **F8 semi**: published loop includes DEU (0 retained obs → empty legend entry) and connects over the CHN 2015-17 gap region. Fixed figure drops DEU/FRA and annotates HS revisions + quarantine (`figures_reviewed/F8_semi_exports_FIXED.png`).
- **F9 BERD**: published title "Business-financed R&D" is factually wrong for P_BERPCT. Fixed figure retitles to "BERD PERFORMED" and notes ISR BERD>GERD vintage mix (`figures_reviewed/F9_berd_mix_FIXED.png`).

## 4. Effective-sample summary (2010-2023 window)

GERD/BERD/scopus/GDP/TFP: full 14 per country (TFP USA constant). Researchers: USA 13, CHN/KOR/JPN/DEU/FRA 14, GBR 8, ISR 0. Patents (res + total): 2010-2021, 12 per country. MVA: USA 12 (to 2021), others 14. Hitech: 14 per country (2010+). Semi retained: USA/KOR/JPN/ISR 14, CHN 11, GBR 8, DEU/FRA 0.

## 5. Cross-country comparability risks (data-level)

WB-GERD vs OECD-BERD vintage mix (ISR inversion); office-basis patents (USA nonresidents > residents vs CHN opposite); fractional S&E articles vs headcount researchers; 2017-PPP single vintage with preliminary 2024; PWT official-GDP basis for CHN TFP; SITC basket + processing trade; HS-revision + re-export semi values; per-million denominator favouring small populations.

## 6. Conclusion

Core panel is usable **only** within the caveats and effective samples above; semi is a USA-CHN-KOR-JPN-ISR descriptive series with a CHN 2015-17 hard gap and no DEU/FRA; AI/HPC/quantum/GVC/VC are excluded. All fixes applied are in `data_changes.md`; no values were imputed and no leadership finding was added or altered.

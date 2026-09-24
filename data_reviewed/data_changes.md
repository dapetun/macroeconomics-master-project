# Data Changes Log (independent Data Quality Reviewer)

Date: 2026-09-14. Originals untouched (`data/`, `results/`, `figures/`, `reports/`, `scripts/` except the new builder below). All outputs are new files under `data_reviewed/`. No imputation, no backfilling, no cross-source replacement, no new leadership conclusions.

## 1. New builder

- `scripts/build_reviewed_dataset.py` (new): rebuilds reviewed panels strictly from stored `data/raw/` with the documented legacy rules. Rerun: `python3 scripts/build_reviewed_dataset.py`. Verified output: `core_panel_reviewed.csv (200, 12)`, `tech_panel_reviewed.csv (200, 12)`, M1 n=84, PCA n=91.

## 2. Panels

- `data_reviewed/core_panel_reviewed.csv`: 200-row base grid; all 9 core values **byte-identical to processed panel** (no edits). **Added** `patents_total_office` = resident + nonresident (perfect 176/176 office-basis join, 2000-2021; e.g. 2021 CHN 1,585,663 / USA 591,473; CHN/USA 2.68x vs resident-only 5.44x). Added to stop resident-only level comparisons.
- `data_reviewed/tech_panel_reviewed.csv`: `semi_exports_hs8542` values **unchanged** (75 retained). **Added** `semi_status` per row (`retained_one_record` / `quarantined_multi_record` / `missing_no_response`). AI/HPC/quantum columns kept all-NaN (excluded by design).
- `data_reviewed/indicator_quality_reviewed.csv`, `data_reviewed/data_dictionary_reviewed.csv`: corrected definitions — BERD **performed** (P_BERPCT, not financed); patents **office-basis resident** (not origin); articles **fractional S&E volume**; GDP **constant-2017 single vintage**; TFP **USA=1/yr construction**; hitech **basket + SITC break**; MVA **share not scale**; semi **nominal + HS H3-H6 + quarantine**; AI/HPC/quantum/GVC/VC **excluded**.

## 3. Tables (all new, originals unchanged)

- `tables_reviewed/semi_quarantine_map.csv`: every 2010-2023 country-year with its semi status (documents CHN 2015-17, DEU all-quarantined, FRA all-no-response, GBR partial).
- `tables_reviewed/effective_samples_2010_2023.csv`: kept-observation counts + t0/t1 per variable x country (documents ISR researchers 0, GBR researchers 8 to 2017, USA researchers 13 to 2022, patents 2000-2021, MVA USA to 2021).
- `tables_reviewed/descriptive_cagr_common_window.csv`: balanced-window CAGRs fixing the published incomparable windows (researchers 2010-17; patents/total + MVA 2010-21; rest 2010-23; TFP USA not ranked).
- `tables_reviewed/descriptive_snapshot_latest_joint.csv`: latest jointly-available US-CHN year per variable with both resident (5.44x, 2021) and office-total (2.68x, 2021) patent ratios.
- `tables_reviewed/model1_effective_n.csv` (n=84; ISR 0, GBR 7, USA 12, others 13) and `tables_reviewed/pca_effective_n.csv` (n=91; ISR 0, GBR 8, USA 13, others 14).

## 4. Figures (new fixed copies; originals untouched)

- `figures_reviewed/F8_semi_exports_FIXED.png`: drops DEU/FRA empty series; annotates CHN 2015-17 quarantine and HS H3/H4/H5/H6 span.
- `figures_reviewed/F9_berd_mix_FIXED.png`: retitles to "BERD PERFORMED (% GDP; OECD MSTI P_BERPCT)" and notes ISR BERD>GERD (2023: 6.50 > 6.35) vintage mix.

## 5. Label/interpretation corrections applied (docs only, no value edits)

BERD financed→performed; patents origin→office resident (+ office total provided); Scopus generic→fractional S&E volume; GDP unspecified→2017-vintage preliminary-2024; TFP trend→USA-constant construction with restricted use; hitech clean trend→basket + break; MVA scale→share; semi single series→quarantined/incomplete with HS breaks; CAGR/snapshot/slope tables→effective-window notes; M1/M2→effective-N + ISR-excluded + small-df notes; event pre/post→nominal + break + n=2/cell descriptive-only (already labelled not causal).

## 6. Excluded as unreliable (no substitute constructed)

HPC systems/Rmax, all four AI series, both quantum series (100% missing, no audited extract — Stanford HTML and EPO-OECD sources identified but not extracted; no chart digitisation, no generic substitution); GVC foreign-VA share and VC investment (planned, never collected). Partial clean Comtrade USA-only file left in place but documented as **not** the panel's source (stale parallel artefact); no re-pull attempted.

## 7. Expressly NOT changed

`data/raw/*`, `data/processed/*`, `data/metadata/*`, `results/*.csv`, `figures/*.png`, `reports/*.md`, `scripts/analysis_agent4.py` and other collectors: values, code, and report texts unchanged by this review.

## 8. Verification run

Recomputed missingness per variable/country, USA=1.000 TFP column, BERD−GERD>0 ISR rows (2021-23), resident vs office-total 2021 ratios (5.44 vs 2.68), M1/PCA group counts, CAGR endpoint audit, legacy-vs-clean Comtrade row audit (75 retained incl. CHN 11 / GBR 8 / DEU 0 / FRA 0; clean USA-only 15 rows with H3/H4/H5/H6 column), and figure rebuild — all reproduced in the reviewed artefacts above.

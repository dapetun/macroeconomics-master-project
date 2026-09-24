# Data quality report

Generated: 2026-09-13. Analytical country set: USA, CHN, KOR, JPN, DEU, GBR, ISR, FRA. Core panel grid: 200 country-year rows (2000-2024).

## Results

| variable                     | status            |   nonmissing |   expected |   missing_pct |   duplicate_country_year | suspicious_jumps_gt100pct   | caveat                                                                                                                                                          |
|:-----------------------------|:------------------|-------------:|-----------:|--------------:|-------------------------:|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gerd_pct_gdp                 | VALID WITH CAVEAT |          192 |        200 |           4   |                        0 | none                        | WB WDI series, chiefly UNESCO-derived; use latest vintage only; China GDP revisions affect ratio.                                                               |
| researchers_per_million      | VALID WITH CAVEAT |          161 |        200 |          19.5 |                        0 | none                        | UNESCO/WDI coverage is intermittent; headcount/FTE treatment may differ by national reporting.                                                                  |
| scopus_articles              | VALID WITH CAVEAT |          192 |        200 |           4   |                        0 | none                        | WDI scientific-and-technical articles, not field-specific Scopus counts; volume, not impact.                                                                    |
| patents_resident             | VALID WITH CAVEAT |          176 |        200 |          12   |                        0 | none                        | Resident applications (WIPO origin via WDI), not quality-adjusted; do not interpret quantity as quality.                                                        |
| mva_pct_gdp                  | VALID             |          193 |        200 |           3.5 |                        0 | none                        | Manufacturing value added as % GDP; macro manufacturing structure, not semiconductor capacity.                                                                  |
| hitech_export_share          | VALID WITH CAVEAT |          144 |        200 |          28   |                        0 | ISR-2008                    | WDI high-tech basket; definition/revision break flagged by World Bank (SITC Rev.4 update); China processing trade caveat.                                       |
| gdp_pc_ppp                   | VALID WITH CAVEAT |          200 |        200 |           0   |                        0 | none                        | WDI constant PPP dollars; kept for normalization only; compare within a single WDI vintage.                                                                     |
| tfp_ctfp                     | VALID WITH CAVEAT |          192 |        200 |           4   |                        0 | none                        | PWT aggregate TFP at constant PPPs; macro context only, not technology-sector productivity.                                                                     |
| berd_pct_gdp                 | VALID WITH CAVEAT |          200 |        200 |           0   |                        0 | none                        | OECD MSTI business R&D intensity; no Taiwan observation in this extraction.                                                                                     |
| semi_exports_hs8542          | VALID WITH CAVEAT |           75 |        200 |          62.5 |                        0 | none                        | UN Comtrade HS8542 nominal USD exports; only unambiguous one-record responses retained. Trade is not fab capacity; re-exports/processing trade remain material. |
| hpc_top500_systems           | MISSING           |            0 |        200 |         100   |                        0 | none                        | not collected: KeyError: 'Rmax (TFlop/s)'                                                                                                                       |
| hpc_top500_rmax_tflops       | MISSING           |            0 |        200 |         100   |                        0 | none                        | not collected: KeyError: 'Rmax (TFlop/s)'                                                                                                                       |
| ai_publications_count        | MISSING           |            0 |        200 |         100   |                        0 | none                        | MISSING: Stanford AI Index report/tool is identified, but no audited country-year raw export is stored. Do not substitute generic article counts.               |
| ai_citations_impact          | MISSING           |            0 |        200 |         100   |                        0 | none                        | MISSING: no consistently defined country-year impact series stored.                                                                                             |
| ai_private_investment_usd_bn | MISSING           |            0 |        200 |         100   |                        0 | none                        | MISSING: proprietary deal coverage and China undercoverage make an unverified substitute unsuitable.                                                            |
| ai_notable_models            | MISSING           |            0 |        200 |         100   |                        0 | none                        | MISSING: available report snapshots are not a historical country-year panel.                                                                                    |
| quantum_ipf_count            | MISSING           |            0 |        200 |         100   |                        0 | none                        | MISSING: EPO-OECD report is comparable but extraction from charts was not performed; no synthetic reconstruction.                                               |
| quantum_publications         | MISSING           |            0 |        200 |         100   |                        0 | none                        | MISSING: no audited country-year extract.                                                                                                                       |

## Dataset rules

- Raw source files are preserved unchanged in `data/raw/`.
- `core_panel.csv` is a country × year wide panel. No interpolation, backfilling, or cross-source replacement was applied.
- `tech_panel.csv` contains only audited semiconductor/HPC observations; unavailable AI and quantum fields remain null by design.
- UN Comtrade HS8542 rows with `num_records > 1` are quarantined from the cleaned panel because the stored extract does not prove a single consistent aggregation. This affects China in 2015-2017 and several comparator years.
- PWT TFP is a macro proxy, not an estimate of technology-specific productivity. It must not be used to attribute productivity changes to AI, semiconductors, HPC, or quantum.
- High-tech exports use a broad commodity basket and should not be treated as a semiconductor or AI-export measure. The documented WDI classification update is a potential series break.

## Ready for analysis

Ready, subject to the listed caveats: gerd_pct_gdp, researchers_per_million, scopus_articles, patents_resident, mva_pct_gdp, hitech_export_share, gdp_pc_ppp, tfp_ctfp, berd_pct_gdp, semi_exports_hs8542.

Not ready for econometric use: AI publications/citations/investment/frontier models and quantum series (all missing); HS8542 requires a new, single-definition Comtrade pull for a complete US-China trend.

## Cross-country comparability

USA and China are comparable within each retained provider series, not across differently defined indicators. The principal country-specific risks are China processing trade (exports, including re-exports via HK/SG), China GDP revisions (ratios), national R&D-personnel reporting practices (FTE/headcount), patent-quality composition (CN subsidies peaked 2021), MVA % GDP as share not absolute output, and TOP500 coverage of listed on-premise systems rather than cloud compute. **High-tech exports use SITC Rev.4 (break Oct 2024, 28% missing) — trend over break is invalid.**
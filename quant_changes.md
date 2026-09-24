# Quant Changes Log

## 1. Descriptives
- Verified `descriptive_snapshot_US_CHN.csv` values byte-exact (GERD 2023 3.44716/2.57729 r=0.748;
  articles 430843/932712 r=2.165; patents resident 2021 262244/1426644 r=5.440x).
- **Fix:** forbid ratios with NaN side; add latest-joint-year column: researchers 2022 0.375x
  (not 2023 NaN); patents 2021 resident 5.44x **+ total-office 2.68x** (591473/1585663);
  MVA 2021 2.53x share-only; GDPpc absolute gap $49321→$51664 alongside 0.305x; TFP USA=1.0 all years.

## 2. Growth rates
- Recomputed: USA researchers 2.56%/yr is 2010–2022, CHN 6.77% is 2010–2023 — incomparable spans.
- **Fix:** `descriptive_cagr.csv` to show common-window 2010–2021 only (articles 1.33 vs 8.51;
  patents 0.73 vs 15.47; MVA −1.11 vs −1.40) with (start,end,n); label any truncated series.

## 3. Ratios
- Patents: cite 2.68x (total) with 5.44x (resident), never alone. Researchers: "intensity,
  denominator artefact". MVA: "composition, not scale". BERD: "~77% both" + performed-not-financed.
  IC: "nominal, re-export-inclusive". **Excluded** `conversion_ratios.csv` (unit-mixed). GDPpc: pair
  ratio with absolute gap.

## 4. Correlations
- Replicated pooled matrix (GERD–TFP −0.086 etc.). Within r flips (≈+0.03 full panel).
- **Fix:** `correlations_pooled.csv` marked DO NOT USE for inference; within/two-way only, descriptive.

## 5. Graphs
- F1–F4,F6,F7 endorsed with caveat annotations (SITC break, resident-only, volume-not-impact, USA=1).
- F5: caption "USA ends 2021; no 2023 comparison". F8/F9 data_reviewed fixes endorsed (gap broken,
  DEU/FRA omitted, performed-title, ISR BERD>GERD artefact annotated). **F10 excluded** (M2).

## 6. Regression specs
- Replicated M1 β=0.02746 HC1 p=0.059 CI incl. 0; θ=0.05629. FE-only R²=0.727→full 0.992.
- **Fix:** `regression_results_final.csv` authoritative; old HC1-only table superseded; M2 row excluded.

## 7. Fixed effects
- Documented USA zero-variance anchor (drop-USA β→0.0329), GBR 7 rows, 18 dummies/84 obs.
- Text: "absorbs traits/shocks, not identification".

## 8. Lags
- Lag0 β=0.0125 p=0.418; lag1 0.0275 p=0.059; lag2 0.0525 p=0.001.
- **Fix:** all lags shown as sensitivity; lag-1 not headlined as structural.

## 9. Controls
- corr(GERD,lres)=0.71 documented; sparse spec kept deliberately; "conditional association" label.

## 10. Sample size
- Stamp everywhere: M1 n=84 K=20 df=64 G=7 (ISR0 GBR7 USA12); PCA n=91; events n=2 (no SEs).

## 11. Missing data
- No imputation (endorsed); propagate "ISR absent; USA 2022–23 missing; patents/MVA end 2021;
  semi quarantined" into F2/F4/F5 captions.

## 12. Outliers
- Retained CHN +63% 12–13, KOR +65% 16–17, ISR hitech jump as flagged quarantined points.
- **Fix:** drop-one sensitivity rows in final CSV (β 0.019–0.049).

## 13. Interpretation
- β magnitude check (+19pp GERD to close gap = absurd) added; M2 sign never interpreted.

## 14. Uncertainty
- Primary interval now country-cluster: β [−0.048,0.103] p=0.409 (t_6); HC1 shown secondary;
  AR(1) 0.32–0.90 documented; no stars on β.

## 15. Causal language
- Endorsed purge; allow-list: associated / conditional correlation / descriptive /
  not distinguishable from zero. H1–H4 stay mixed/weak/inconclusive.

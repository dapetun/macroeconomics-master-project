# Quantitative Review — US–CHN Tech Rivalry (2010–2023, 8 countries)

> **DATA CANON note (2026-09-20, DataCanonAgent).** GBR researchers end year = **2017** (не 2019).  
> Articles CAGR: оба окна 2010–2021 и 2010–2023 + пик USA 2021 — см. `DATA_CANON.md`.  
> Числа/методы M1–PCA — зона QuantitativeAgent; этот файл остаётся audit-trail.

Independent recomputation from `data_reviewed/core_panel_reviewed.csv` + `tech_panel_reviewed.csv`.
All numbers below were recomputed; prior text fixes (USA=1, denominator artefacts, MVA share≠scale,
BERD≈77% both, H1/H4 inflated, M1 CI-includes-0, no causal verbs, 2021 patent peak, SITC break,
IC nominal, n=2 events, matrix `?`, GDPpc absolute gap, KOR proxies) are **endorsed** and extended.

Effective samples (confirmed): M1 **n=84, K=20, df=64, G=7 countries**
(CHN13 DEU13 FRA13 GBR7 JPN13 KOR13 USA12; ISR 0). PCA n=91. Semi retained n=75
(CHN 11 with 2015–17 gap; DEU/FRA 0; GBR 8).

---

## 1. Descriptive statistics — VERDICT: endorsed with mandatory year-alignment fix

Recomputed snapshot matches `descriptive_snapshot_US_CHN.csv` exactly (e.g. 2023 GERD USA 3.44716,
CHN 2.57729 ratio 0.748; articles 430843 vs 932712 ratio 2.165; 2021 patents resident 262244 vs
1426644 ratio **5.440x**; patents total-office 591473 vs 1585663 ratio **2.681x**).

**Problem:** 2023-column comparisons mix observed with NaN: researchers USA NaN vs CHN 2107.27;
patents NaN/NaN; MVA NaN vs 25.01. Any "2023 ratio" for those rows is undefined, and the MVA
time-series figure compares CHN-2023 against a USA line that ends in 2021.
**Impacted:** `descriptive_snapshot_US_CHN.csv`, F2/F4/F5, synthesis §D1.
**Fix applied:** report **latest-joint-year** alongside calendar-2023:
researchers 2022 USA 4937.49 vs CHN 1849.24 (0.375x); patents resident 2021 5.44x **and**
total-office 2021 **2.68x** (resident-only overstates gap ~2x); MVA 2021 USA 10.53% vs CHN 26.62%
(2.53x — share only, not scale); hitech 2023 21.85% vs 26.57% (1.22x, SITC break, re-exports);
GDPpc 2023 $74352 vs $22687 (0.305x, **absolute gap widened $49321→$51664**); TFP USA 1.0 every
year 2000–2023 (construction) vs CHN 0.471.
**Risk/Recommendation:** never print a ratio with a NaN side; use joint-year table (done in §D1 fix).

## 2. Growth rates — VERDICT: problematic windows, corrected

Published CAGRs use incomparable spans: USA researchers 2010–2022 (2.56%/yr, n=12) vs CHN
2010–2023 (6.77%/yr, n=13); patents/MVA stop at 2021 for USA but text invites 2023 reads.
Recomputed common-window 2010–2021: articles USA 1.33%/yr vs CHN 8.51%/yr; patents resident
USA 0.73%/yr vs CHN 15.47%/yr; MVA share USA −1.11%/yr vs CHN −1.40%/yr (both **falling shares**);
GERD 2010–2023 USA 1.86%/yr vs CHN 3.33%/yr.
**Impacted:** `descriptive_cagr.csv`, synthesis §D2. **Fix:** publish only common-window CAGRs
with explicit (start,end,n); label USA-researcher CAGR "2010–2022 (USA latest)" if shown.

## 3. Ratios — VERDICT: several mechanically misleading, fixed by dual reporting / exclusion

- **Patents 5.44x:** resident-only. Total-office 2021 = **2.68x**. Resident gap reflects office
  home-bias + subsidies, not pure inventive output. Fix: always pair both; never cite 5.44x alone.
- **Researchers per-million:** CHN 0.375x (2022 joint) is a denominator artefact — 1.4bn population.
  Absolute headcount gap is far smaller; fix: label "intensity, not headcount; penultimate-year".
- **MVA % GDP (2.53x):** share, not scale/leadership. USA share fell (11.91→10.53%) while real
  manufacturing value-added grew; CHN share fell faster (31.07→26.62%). Fix: "composition, not scale".
- **BERD "gap":** 2023 BERD USA 2.658 vs CHN 2.003 (0.754x) and BERD/GERD ≈77% **both**
  (USA 77.1%, CHN 77.7%) — business funds the same share; the gap is the GERD gap, not behaviour.
  Also BERD is **performed** in firms, not financed (F9 title fix endorsed).
- **IC trade values:** nominal USD, include re-exports/transfer pricing; CHN 2021 spike +65%
  KOR 2017 +65% are partly price/classification. Fix: "nominal, re-export-inclusive".
- **Conversion ratios** (patents/researcher, articles/GERD): mix counts÷intensities with different
  denominators/years — mechanically constructed. **Excluded** (`conversion_ratios.csv` DO NOT USE).
- **GDPpc 0.305x:** ratio convergence with **absolute divergence** (+$2,343). Both must appear.

## 4. Correlations — VERDICT: pooled table excluded; within-only, weak

`correlations_pooled.csv` recomputed exactly (e.g. GERD–TFP −0.086, patents–TFP −0.636,
MVA–TFP −0.693, GDPpc–TFP +0.908). These are **compositional artefacts** (Simpson): pooled
GERD–TFP r=−0.086 flips to within-country r≈+0.03 (full panel) / +0.24 (M1 subsample, lagged);
pooled researcher–TFP +0.275 vs two-way-demeaned lres–TFP +0.51 vs GERD +0.15 — unstable by
demeaning/sample. Cross-country levels confound development stage with efficiency.
**Fix:** mark pooled matrix **DO NOT USE for inference**; if any correlation is shown, show
within/two-way-demeaned with N and "descriptive, no causal reading". GDPpc–TFP 0.91 is
accounting-adjacent (both embed income), not evidence.

## 5. Graphs (F1–F10) — VERDICT: F1–F7 endorsed with caveats; F8/F9 fixes endorsed; F10 excluded

- F1 GERD: OK — KOR/ISR lead; parallel CHN rise. Add: "intensity, CHN from lower base".
- F2 researchers: line correctly breaks (ISR absent, GBR ends **2017**, USA ends 2022). Keep
  "ISR missing; unbalanced windows; per-million denominator" annotation; do not interpolate.
- F3 articles crossover 2020–21: OK as **volume**; add "counts, not citations/impact".
- F4 patents (log, 2010–21): OK window; must annotate "resident-only; total-office gap 2.68x,
  peak year 2021, no post-2021 data".
- F5 MVA: line honestly stops (USA 2021). Text/legend must not compare CHN-2023 to USA-2021;
  prefer common-window 2010–2021 panel or explicit "USA 2022–23 missing".
- F6 hitech: keep SITC Rev.4 break + re-export caveat.
- F7 TFP: USA=1 construction label endorsed — the flat USA line is definitional.
- F8 semiconductors: **data_reviewed fix endorsed** (DEU/FRA omitted as no data, CHN 2015–17 gap
  shown broken, quarantine flag `semi_status`). Raw CHN +63% 2012→13 (29.6→87.9bn) and KOR +65%
  2016→17 are retained-but-flagged outliers, not trends. Never connect across the gap.
- F9 BERD: **title fix endorsed** ("performed", not "financed"); ISR BERD>GERD 2021–23 is a
  source/method artefact (5.82>5.76, 6.22>6.18, 6.50>6.35) — annotate, do not interpret as >100%.
- F10 PCA scatter: **EXCLUDED** — pooled r is decorative; PC1 loadings incoherent (see §7).

## 6. Regression specs — VERDICT: M1 retained as descriptive-only with corrected SEs; M2 excluded

Replicated LSDV (country+year FE): M1 β_GERDlag1=**0.02746** HC1 SE 0.01427 t=1.92
**p=0.059 95% CI [−0.0005, 0.0554]**; θ_lres=0.05629 SE 0.00429 t=13.1. n=84 K=20 df=64.
FE-only R²=0.727, full R²=0.992 (incremental 0.265 — regressors add fit but on 64 df with
serial errors). Pooled OLS without FE flips GERD sign (**−0.207**) — result is FE-dependent.
`regression_results_final.csv` is now authoritative; old `regression_results.csv` HC1-only
p-values are superseded (M2 row deleted there conceptually).

## 7. Fixed effects — VERDICT: necessary but load-bearing; USA anchor is a zero-variance unit

Country+year FE absorb level differences and common shocks, which is why pooled −0.21 becomes
+0.03. Cost: 18 dummies on 84 obs; USA TFP=1.0 all 24 years contributes **zero within variation**
in y yet consumes a dummy and 12 rows — dropping USA raises β to 0.0329. GBR contributes only
7 rows. FE do not solve reverse causality (richer→spends more), omitted variables (openness,
human capital stock, institutions, cycle), or measurement error. Report FE as "controls for
time-invariant country traits and common yearly shocks, not causal identification".

## 8. Lag structure — VERDICT: unjustified and fragile

Only GERD lagged once; lres contemporaneous; no dynamics/HAC. Sensitivity: contemporaneous
GERD β=0.0125 p=0.418; lag-1 β=0.0275 p=0.059; lag-2 β=0.0525 p=0.001. Significance is a
function of lag choice. No theory/serial-correlation argument was given for lag-1. Fix: present
all three lags as sensitivity; do not headline the "best" lag; use HAC/cluster SEs given AR(1).

## 9. Controls — VERDICT: sparse and collinear; no causal reading

Only log-researchers alongside GERD. corr(gerd_lag1, lres)=**0.71** (VIF≈2) — overlapping
intensity margins; θ captures scale+development, not a clean channel. Missing: GDPpc level,
openness, schooling stock, IP regime, cycle, sector mix. Adding GDPpc would soak TFP (r=0.91)
— reason to **not** over-control, and reason to admit the two-regressor model is descriptive.
No bad-control fix is credible at n=84/G=7; keep sparse spec, label "conditional association".

## 10. Sample size — VERDICT: tiny; asymptotics do not apply

M1: 84 rows → 20 parameters → 64 df; **7 clusters** (ISR excluded entirely, GBR 7, USA 12).
HC1 t/p assume independence that AR(1) 0.32–0.90 refutes. Country-clustered SE (CR1, t_6):
SE_β=0.0310 **p=0.409 CI [−0.048, 0.103]**; SE_θ=0.0079 p<0.001. With G=7 even cluster SEs are
unreliable (report with "G=7, use with caution"). M2 n=91 same problem. Events n=2 → no SEs,
pre/post only. Fix: every table/figure/text states n/K/df/G; no stars without cluster note.

## 11. Missing data — VERDICT: handled honestly after data review; propagate labels

ISR researchers 0/14 (M1 silently drops ISR — state it); GBR researchers end **2017**
(8 obs in 2010–2017 common window; M1 n=7 after lag); USA researchers end 2022;
patents/MVA end 2021 (USA); semi: DEU/FRA 0 kept-rows, CHN 2015–17 gap, GBR 8;
AI/HPC/quantum ~100% missing → correctly excluded from models. No imputation was
done (endorsed). Remaining fix: F5/F2 captions must carry "USA 2022–23 missing; ISR absent"
so readers never compare a line's endpoint to another country's later point.

## 12. Outliers/leverage — VERDICT: flagged, not trimmed; sensitivity required

CHN semi 2012–13 +63%/yr spike; KOR semi +65% 2016→17; ISR hitech 2020 jump 21.5→33.8%;
CHN patents +17%/yr 2010–21 vs USA +0.7%; all retained (no trimming endorsed) but quarantined
via `semi_status`. Drop-one sensitivity: drop-CHN β=0.0189 (HC1 p=0.157); drop-KOR β=0.0487
(HC1 p=0.017); drop-GBR β=0.0405; balanced 2011–21 β=0.0353 — any single country moves β by
±30–75%. Largest LSDV residuals: GBR-2011 +0.036, DEU-2022 +0.033, DEU-2011 −0.045. Fix: keep
all points, report drop-one table (`regression_results_final.csv` sensitivity rows), never
headline a specification that hinges on one country.

## 13. Interpretation — VERDICT: association only; prior causal-verb purge endorsed

Correct reading: "In 84 country-years with data, a 1pp higher GERD/GDP last year is associated
with +0.027 TFP points conditional on country, year, and researcher intensity — **HC1 CI
includes 0; cluster CI wide; not distinguishable from no association; reverse causality and
omitted variables remain**." Economic magnitude check: closing CHN–USA TFP gap (0.53) via β
alone needs +19pp GERD/GDP — absurd, confirming β is not a policy multiplier. θ_lres=+0.056
per log point (≈+0.005 TFP per +10% researchers) is likewise descriptive. M2's negative PC1
sign must never be interpreted ("more tech lowers TFP" is a construction artefact).

## 14. Uncertainty — VERDICT: previously understated; corrected intervals are the headline

Publish **both** HC1 and country-cluster intervals; cluster is primary despite G=7 caveat:
β HC1 [−0.001, 0.055] p=0.059 vs cluster [−0.048, 0.103] p=0.409. Serial correlation
(AR1 0.68–0.90 in 5/7 countries), multicollinearity (0.71), lag mining, and single-country
sensitivity all widen true uncertainty beyond printed SEs. No significance stars on β; θ's
t=13.1→cluster t=7.1 must carry "G=7" warning. Event study: no CIs (n=2).

## 15. Causal language — VERDICT: purge endorsed; allow-list enforced

No "effect/impact/drives/boosts/returns to R&D" for M1/M2/correlations/trends. Allowed:
"associated", "conditional correlation", "descriptive", "consistent with", "not distinguishable
from zero". Fixed-effect and lagged-x language ("holding country and year constant", "preceding
year") must not imply identification. All H1–H4 verdicts stay at "mixed/weak/inconclusive" or
"descriptive catch-up in volumes, not demonstrated efficiency advantage".

---

### Files

- `regression_results_final.csv` — authoritative: M1 retained descriptive-only with HC1 +
  country-cluster SEs; lag/drop-one sensitivities; M2 marked EXCLUDED_DO_NOT_USE.
- Old `results/regression_results.csv`, `model2_*`, `correlations_pooled.csv`,
  `conversion_ratios.csv`, F10 data (`pca_*`, `trend_slopes_convergence.csv` where pooled)
  are superseded for inference; keep on disk but never cite as evidence.

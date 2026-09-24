# QuantitativeAgent — changelog

**Дата:** 2026-09-20  
**Brief:** ORCHESTRATION_PLAN.md §9.3  
**Binding:** `APPROVED_METHOD_SET.md` (не изменялся)  
**Зависимости:** ResearchDesign DONE; DataCanon DONE  
**Не делалось:** DiD/IV/GMM/ML/k-means/EN/FA; TWN panel; State B pulls; force M2; lag/HAC shopping; claim M1 answers RQ; edit tech matrix

---

## Change log table

| Change | Reason | Evidence | Files affected | Downstream impact |
|--------|--------|----------|----------------|-------------------|
| Dual-scale Level 1 table (D1) | Центральный descriptive result intensity vs volume/share; joint year на каждой строке; articles dual-window | Все intensity → USA_higher; volume/share → CHN_higher; CAGR windows per DATA_CANON | `data_reviewed/tables_reviewed/dual_scale_intensity_volume.csv`, `dual_scale_D1_summary.csv` (**created**); `scripts/quant_level1_pca_refresh.py` | Synthesis цитирует dual-scale для D1 |
| Articles dual-window в dual-scale | Canon: оба окна + peak USA 2021 | USA CAGR 1.33% (→2021) vs 0.43% (→2023); peak 471378 | rows in dual_scale + existing `articles_cagr_dual_window.csv` | Не цитировать одно окно как единственное |
| M1 interpretation note | Keep authoritative numbers; secondary/appendix; cluster CI includes 0 | β_GERD=0.02746; HC1 p=0.059; cluster p=0.409; n=84; G=7 | `M1_INTERPRETATION.md` (**created**) | Synthesis: M1 не в executive RQ answer |
| PCA repair cycle a/b/c | Broken mixed-scale PCA; protocol one attempt | (a) all loadings >0; var_exp PC1≈90.7%; n=91; years 2010–2023; G=7 | `results/pca_repair_*`; `PCA_REPAIR_PASS.md`; appendix fig | PC1 descriptive OK; M2 **not** run; old F10/M2 still excluded |
| DO_NOT_USE quant list | Drop conversion / pooled inference / event-as-effect from argument | Approved Set Not approved | `DO_NOT_USE_QUANT.md` (**created**) | Synthesis allow-list enforcement |
| Figure title fixes | Remove converges/overtook/finance-mix causal tone | Regenerated F1–F7; F8/F9 FIXED kept; F10 old excluded | `FIGURE_TITLE_FIXES.md`; `figures/F1–F7.png`; `figures_reviewed/F10_appendix_pc1_intensity_ONLY.png` | Cite new titles / FIXED F8/F9 |

---

## PCA gate verdict

| Item | Value |
|------|-------|
| **Verdict** | **PASS** |
| **Selected variant** | **(a) intensity-only** (GERD %, BERD %, researchers per million) |
| Also passed (not selected) | (b) logged volumes; (c) within-z intensity |
| M2 | **Not run** (optional secondary only; no tech→TFP claim) |
| Old `pca_loadings.csv` / F10 scatter / M2 γ | **DO NOT USE** |

---

## Key conclusions (confidence)

| Conclusion | Label |
|------------|-------|
| Level-1 dual-scale signs **consistent with** D1 (intensity USA_higher; volume/share CHN_higher) with explicit joint years; not a SUPPORTED verdict | **CONFIRMED** |
| Articles dual-window + USA peak 2021 required for growth comparisons | **CONFIRMED** |
| M1 is within-country associational; cluster CI includes 0 → not an effect finding; not RQ answer | **CONFIRMED** |
| PCA (a) passes same-sign gate; interpretable as intensity factor | **CONFIRMED** |
| M2 not needed for State A argument after PCA pass | **LIKELY** (optional; left unused) |
| Regenerated F1–F7 titles fully neutralize all legacy language in figure files | **LIKELY** (titles fixed; body prose elsewhere may still quote old titles) |
| F8/F9 FIXED remain preferred over originals | **CONFIRMED** (DataCanon / prior review) |
| Full corpus free of conversion/pooled-as-inference citations | **NEEDS_REVIEW** (Synthesis) |

---

## Acceptance checklist

- [x] Level 1 answers D1 (dual-scale + joint-year + dual-window articles)
- [x] M1 secondary with caveats (`M1_INTERPRETATION.md`)
- [x] PCA PASS documented (variant a) OR fail+drop — **PASS**
- [x] Unapproved methods documented as DO NOT USE
- [x] Figure title fixes listed + worst offenders regenerated
- [x] No PROPOSED_METHOD_CHANGE needed (no method outside Approved Set)

---

## HANDOFF → SynthesisAgent

### Canonical Level 1 (cite these)

1. `data_reviewed/tables_reviewed/dual_scale_intensity_volume.csv` — **центральный D1 result**
2. `data_reviewed/tables_reviewed/descriptive_snapshot_latest_joint.csv` — joint-year levels (DataCanon)
3. `data_reviewed/tables_reviewed/descriptive_cagr_common_window.csv` — common-window CAGR
4. `data_reviewed/tables_reviewed/articles_cagr_dual_window.csv` — articles **оба** окна + peak
5. `DATA_CANON.md` / `RQ_FREEZE.md` — windows & D1 wording

### M1

- Numbers: `regression_results_final.csv` only  
- Interpretation / placement: `M1_INTERPRETATION.md`  
- **Не** ответ на Frozen RQ

### PCA status

- **PASS (a) intensity-only** — see `PCA_REPAIR_PASS.md`  
- Loadings/variance: `results/pca_repair_selected_*.csv` / `pca_repair_a_intensity_*.csv`  
- Appendix fig: `data_reviewed/figures_reviewed/F10_appendix_pc1_intensity_ONLY.png`  
- Old `results/pca_loadings.csv`, M2, `figures/F10_pca_tfp_scatter.png` → **DO NOT USE**  
- M2 **not** in argument unless Synthesis explicitly wants optional secondary with USA TFP=1 caveat

### Drop / language

- `DO_NOT_USE_QUANT.md`  
- `FIGURE_TITLE_FIXES.md`  
- Allow-list: associated / descriptive / not measured — no winner, no org→conversion causality

### Parallel

- TechMatrixAgent owns 8×4 occupancy / semis / TWN hole — Quant did not edit tech matrix files.

*Конец QuantitativeAgent_changelog.md.*

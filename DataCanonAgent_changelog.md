# DataCanonAgent — changelog

**Дата:** 2026-09-20  
**Brief:** ORCHESTRATION_PLAN.md §9.2  
**Зависимость:** ResearchDesignAgent DONE (`RQ_FREEZE.md`, `ResearchDesignAgent_changelog.md`)  
**Не делалось:** импутация; TWN panel; TOP500/AI Index; пересчёт M1/PCA; rewrite `final_project.md`; изменение `APPROVED_METHOD_SET.md`; удаление raw/results.

---

## Change log table

| Change | Reason | Evidence | Files affected | Downstream impact |
|--------|--------|----------|----------------|-------------------|
| Создан `DATA_CANON.md` | Единая точка канона: dual-window articles, joint-year, BERD PERFORMED, GBR 2017, patents pair, FRA≠TWN | Recompute from `core_panel_reviewed.csv`; `data_quality_final.md`; `RQ_FREEZE.md` D1 | `DATA_CANON.md` (**created**) | Quant/Tech/Synthesis читают канон отсюда |
| Canon CSV articles dual-window | Articles 2010–21 vs 2010–23 оба верны; пик USA 2021 | USA 1.33%/8.51% (→2021); 0.43%/8.90% (→2023); peak 471378 @2021 | `data_reviewed/tables_reviewed/articles_cagr_dual_window.csv` (**created**) | Level 1 refresh цитирует оба окна |
| Выровнен `data/metadata/data_dictionary.csv` | BERD wording; HPC «VALID» при 0 значений; нет patents_total_office; GBR note | `data_dictionary_reviewed.csv`; PROJECT_STATE §17 | `data/metadata/data_dictionary.csv` | Metadata не расходится с reviewed |
| GBR ends 2019 → **2017** в `quant_reviewed.md` | Stale error vs panel | GBR max year researchers = 2017; n=8 in 2010–17 | `quant_reviewed.md` §5 F2, §11 + DATA CANON note | Не цитировать 2019 |
| Усилен DO NOT CITE на `remaining_risks.md` | 77%; H1 partial; «cluster SE невозможны» | cluster SE в `regression_results_final.csv` (p≈0.409); final_project отозвал 77%/partial | `remaining_risks.md` | Synthesis не берёт stale risks |
| Усилен DO NOT CITE на `reports/final_synthesis.md` | H1/H4 partial; 77%; cluster «невозможны»; single-window articles | PROJECT_STATE §17; ResearchDesign watermark уже был — усилен | `reports/final_synthesis.md` | Audit-trail only |
| DATA CANON banner на `technology_cases_final.md` | business-financed; 77%; cluster «невозможны» | Grep тела | `technology_cases_final.md` | TechMatrix не цитирует finance/77% |
| SUPERSEDED panel note на `data_map.md` | Design TWN vs actual FRA | Panel roster; PROJECT_STATE contradiction | `data_map.md` | Не расширять TWN |
| maxabs processed↔reviewed | Проверка согласованности | Shared cols maxabs = **0.0**; only-in-reviewed: `patents_total_office` | записано здесь | Processed OK как mirror shared cols |

---

## Answers to §9.2 QUESTIONS

**Какие metadata files ещё расходятся с reviewed dictionary?**

| File | Статус после DataCanon |
|------|------------------------|
| `data/metadata/data_dictionary.csv` | **Выровнен** (BERD PERFORMED; HPC/AI/quantum MISSING; patents_total_office added; GBR 2017 in researchers label) |
| `data_reviewed/data_dictionary_reviewed.csv` | Уже был каноничен — **не менялся** |
| `data_map.md` | Planned intent (TWN) — **banner only**; тело не rewrite |
| `indicator_quality_reviewed.csv` | Уже согласован с quality_final — OK |

---

## Key conclusions (confidence)

| Conclusion | Label |
|------------|-------|
| Articles CAGR dual-window + USA peak 2021 documented; neither window sole canon | **CONFIRMED** (recomputed from reviewed panel) |
| GBR researchers end = 2017 | **CONFIRMED** |
| BERD = PERFORMED (P_BERPCT), not finance mix; 77% revoked for citation | **CONFIRMED** |
| Patents pair resident+total mandatory in canon tables | **CONFIRMED** |
| Panel = FRA not TWN; no expansion | **CONFIRMED** |
| processed vs reviewed maxabs shared cols = 0 | **CONFIRMED** |
| Stale risk/synthesis files sufficiently bannered for Synthesis | **LIKELY** |
| Все prose-места с «GBR 2019» пойманы | **LIKELY** (grep; quant_reviewed fixed; logic/final already 2017) |
| Полный corpus PDF/notebooks без «77%/H1 partial» | **UNCERTAIN** (баннеры на known offenders; не полный rewrite) |
| Нужен ли update PROJECT_STATE §17 «articles UNRESOLVED» → dual-window resolved | **NEEDS_REVIEW** (владелец карты: parent / Synthesis; канон уже в DATA_CANON) |

---

## Acceptance checklist

- [x] Dual-window articles documented (`DATA_CANON.md` + CSV)
- [x] GBR = 2017
- [x] BERD = PERFORMED
- [x] Stale risk files bannered (strengthened DO NOT CITE)
- [x] Changelog complete
- [x] No imputation / no TWN / no TOP500 / no M1-PCA recalc / no final_project body / no APPROVED_METHOD_SET change

---

## HANDOFF

### → QuantitativeAgent

**Читать (авторитетно):**
1. `DATA_CANON.md`
2. `data_reviewed/tables_reviewed/articles_cagr_dual_window.csv`
3. `data_reviewed/tables_reviewed/descriptive_snapshot_latest_joint.csv`
4. `data_reviewed/tables_reviewed/descriptive_cagr_common_window.csv`
5. `data_reviewed/core_panel_reviewed.csv`
6. `RQ_FREEZE.md` (D1 dual-scale / dual-window articles)
7. `APPROVED_METHOD_SET.md` (не менять)

**Авторитетные числа:**
- Articles CAGR: **оба** 2010–2021 (USA 1.33%, CHN 8.51%) **и** 2010–2023 (USA 0.43%, CHN 8.90%) + peak USA **2021**
- Joint-year snapshot из `descriptive_snapshot_latest_joint.csv`
- BERD labels: PERFORMED only
- GBR researchers: end **2017**
- Patents: всегда пара resident + total_office
- M1/PCA: **не пересчитывать в DataCanon**; Quant владеет refresh/caveats

**Не цитировать:** `remaining_risks.md`, `reports/final_synthesis.md` (числа/вердикты), единственное articles-окно без пары.

### → TechMatrixAgent

**Читать:**
1. `DATA_CANON.md` (§6 FRA≠TWN; §7 AI/HPC/quantum MISSING)
2. `RQ_FREEZE.md` D2 (missingness-as-result)
3. `data_reviewed/tech_panel_reviewed.csv` + `semi_quarantine_map.csv`
4. `technology_cases_final.md` (**только** с баннерами; не 77%/business-financed)

**Правила:** TWN = qualitative hole, не panel row; AI/HPC/quantum = `?`; semis trade≠fab; не тянуть TOP500/AI Index в этом проходе.

*Конец DataCanonAgent_changelog.md.*

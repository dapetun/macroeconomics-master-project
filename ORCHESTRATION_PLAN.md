# ORCHESTRATION PLAN

**Дата:** 2026-09-20  
**Роль:** Method-set recorder + orchestration planner  
**Статус:** Ready for parent orchestrator. **Агенты ещё не запускались.**  
**Binding inputs:** решения автора (Target State A; M1 keep secondary; PCA repair; D1–D2; TWN hole+qual; allow-list KEEP) + `APPROVED_METHOD_SET.md`  
**Не делать в этом файле:** запуск субагентов, пересчёт анализа, rewrite тела `final_project.md`.

---

## 1. Current State

Учебный магистерский проект US–CN tech chain. На диске:

| Слой | Состояние |
|------|-----------|
| Синтез | `final_project.md` (2026-09-16) — актуальный после adversarial; RQ уже сужен до descriptive §1.2 |
| Карта | `PROJECT_STATE.md` (2026-09-20); диагноз `DIAGNOSIS_AND_METHODOLOGY.md` (proposal only → теперь superseded approval'ом) |
| Данные | 8 стран (FRA, не TWN) × 200 строк; ~10 macro vars; semis trade 75; AI/HPC/quantum = 100% NaN |
| Quant | Level 1 descriptives + M1 TWFE (β_GERD=0.02746; HC1 p=0.059; cluster p=0.409; n=84) + broken PCA/M2 EXCLUDED |
| Гипотезы | H1–H6 все Not tested; таблица синхронизирована `reports/hypothesis_table.md` |
| Tech | Четыре раздела + qual; нет единой заполненной 8×4 occupancy matrix |
| Methods approval | **`APPROVED_METHOD_SET.md` только что создан** — Phase 0 lock |

Главный уже зафиксированный descriptive паттерн: intensity↑ USA vs volume/share↑ CHN = арифметика знаменателей, не «модель»; механизмы NOT IDENTIFIED; no winner.

---

## 2. Main Problems

1. **RQ drift risk:** working topic / `research_design.md` всё ещё читаются как causal «организация→конверсия»; обложка должна остаться Frozen RQ.
2. **H1–H6 vs evidence:** полный causal set не тестируем; нужны D1–D2 вместо иллюзии «ещё дотестируем».
3. **Stale artefacts:** `remaining_risks.md`, часть `reports/*`, `technology_cases_final.md`, titles F1/F9 originals, articles CAGR dual-window conflict, GBR «2019» в старых текстах.
4. **Broken PCA** оставлен на диске — риск misuse; нужен repair-or-drop по gate.
5. **M1 рядом с productivity** создаёт иллюзию моста к RQ — нужно жёсткое secondary/appendix placement.
6. **4 tech ≈ четыре эссе** без одной occupancy matrix; TWN hole не формализован как решение.
7. **Language risk:** соблазн «USA converts / China scales» как вывод — allow-list KEEP.

---

## 3. Target State

Один coherent аргумент (State A):

> В 2010–2023 (фактические окна) США и Китай расходятся по **типу измерения** вдоль TCI: intensity R&D/HC vs volume/share поздних блоков. Это описание метрик + явная карта дыр, не модель конверсии и не winner. Четыре tech — **одна** 8×4 матрица (`measured`/`?`/`qual`); количественно заполнен semis-trade. AI/HPC/quantum = `?`. TWN = data hole + короткая foundry note. M1 — appendix associational. PCA — repair или drop. Экономический эффект (TFP/GDP) отдельно; механизмы **NOT IDENTIFIED**.

---

## 4. Required Changes

| # | Change | Owner agent |
|---|--------|-------------|
| 1 | Freeze RQ; watermark stale RQ claims; archive H1–H6; insert D1–D2 | ResearchDesignAgent |
| 2 | Canon: articles dual-window CAGR; joint-year labels; BERD PERFORMED; GBR researchers end **2017**; dictionary fixes; SUPERSEDED banners | DataCanonAgent |
| 3 | Level 1 refresh; M1 keep+caveats; PCA repair protocol; drop conversion/pooled/event-effects; fix figure titles | QuantitativeAgent |
| 4 | One 8×4 matrix; semis+TWN qual hole; AI/HPC/quantum `?`; unify cases | TechMatrixAgent |
| 5 | One argument; allow-list; no winner; mechanism NOT IDENTIFIED | SynthesisAgent |
| 6 | Adversarial pass last | AdversarialReviewer |

**Не требуется:** новый TOP500/AI Index; TWN panel; DiD/IV/ML; четыре tech-агента.

---

## 5. Methodology Options

Полная таблица опций — в `DIAGNOSIS_AND_METHODOLOGY.md` §12.  
**Утверждённый набор** — только `APPROVED_METHOD_SET.md` (Core / Optional / Not approved / Substitutes).

Кратко:

- **Core = Level 1 descriptive** (snapshot, CAGR, dual-scale, occupancy, figures, allow-list, missingness).
- **Optional = M1 appendix + PCA repair-gated + slopes without p + within-corr + macro radar.**
- **Not approved =** conversion, pooled inference, event-as-effect, DiD/IV/ML/FA/k-means/EN, State B collection, TWN expansion.

---

## 6. Approved Method Set (status copy)

Источник истины: **`APPROVED_METHOD_SET.md`**. Статус: **APPROVED 2026-09-20**.

```text
Core: joint-year + ratios; common-window CAGR (articles dual-window+peak);
      dual-scale; TCI occupancy 8×4; F1–F7 + FIXED F8/F9 neutral titles;
      semis trade≠fab; AI/HPC/quantum `?`; allow-list; missingness-as-result

Optional: M1 TWFE secondary/appendix (HC1+cluster); PCA repair if gate passes
          (+ optional M2 secondary only); slopes w/o p; within-corr; macro radar;
          M1 fragility table (no lag shopping)

Not approved: broken PCA/M2/F10 as evidence; conversion; pooled inference;
              event-as-effect; TCI-as-H1-test; H3/H5 regs; k-means/EN/DiD/IV/
              GMM/SEM/Bayesian/VAR/ML; FA default; TOP500/AI Index pull;
              TWN panel; winner; causal org→conversion

Possible substitutes: CAGR↔slope; occupancy/dual-scale↔conversion index;
                      qual TWN↔panel; within-corr↔pooled; FE appendix↔causal claim;
                      intensity-or-volume PCA↔mixed PCA; dates↔DiD
```

---

## 7. Dependency Graph

```
[Phase 0] APPROVED_METHOD_SET.md ── LOCKED
                │
                ▼
        ResearchDesignAgent (RQ + D1–D2 + H archive + watermarks)
                │
        ┌───────┴───────────────┐
        ▼                       ▼
 DataCanonAgent          (может стартовать почти сразу после design freeze;
        │                 watermark stale может частично параллельно)
        │
        ├──────────────────────► TechMatrixAgent
        │                         (нужны canon labels + Frozen RQ;
        │                          не ждёт quant results кроме joint numbers)
        ▼
 QuantitativeAgent  ◄── HARD BIND to Approved Method Set
        │
        └──────────► SynthesisAgent (ждёт Design + DataCanon + Quant + TechMatrix)
                            │
                            ▼
                     AdversarialReviewer (LAST)
```

| Edge | Type |
|------|------|
| Method Set → all agents | **MUST WAIT** (done) |
| Design → DataCanon / TechMatrix / Quant | sequential soft (canon of RQ/D) |
| DataCanon ∥ early TechMatrix draft | **parallel OK** after Design |
| Quant ∥ TechMatrix | **parallel OK** after DataCanon labels stable |
| Synthesis | sequential after four upstream |
| Adversarial | sequential last |

---

## 8. Agent Architecture

| Agent | Responsibility | Inputs | Outputs | Dependencies | Parallel? |
|-------|----------------|--------|---------|--------------|-----------|
| **ResearchDesignAgent** | Freeze descriptive RQ; D1–D2; archive H1–H6; watermark stale RQ | `APPROVED_METHOD_SET.md`, `final_project.md` §1–2, `research_design.md`, `reports/hypothesis_table.md` | RQ freeze note; updated hypothesis table (D1–D2 + H archive); watermarks; `ResearchDesignAgent_changelog.md` | Method Set | No (first) |
| **DataCanonAgent** | Articles dual-window; joint-year; BERD PERFORMED; GBR 2017; dictionary; SUPERSEDED banners | panels, `data_quality_final.md`, stale MD list from PROJECT_STATE §17 | Canon CSV/notes; SUPERSEDED banners; `DataCanonAgent_changelog.md` | Design (RQ freeze) | Yes with TechMatrix after Design |
| **QuantitativeAgent** | Level 1 refresh; M1 caveats; PCA repair gate; drop bad methods; figure titles | Approved Set, reviewed panels, `regression_results_final.csv`, `pca_loadings.csv` | Updated Level 1 tables/figs notes; PCA pass/fail report; optional M2 only if pass; `QuantitativeAgent_changelog.md`; maybe `PROPOSED_METHOD_CHANGE.md` | Design + DataCanon | Yes with TechMatrix |
| **TechMatrixAgent** | One 8×4 occupancy; semis+TWN qual; `?` for AI/HPC/quantum; unify cases | Frozen RQ, canon labels, `final_project.md` §6, tech_panel | Occupancy matrix MD/CSV; unified tech section draft; `TechMatrixAgent_changelog.md` | Design + DataCanon | Yes with Quant |
| **SynthesisAgent** | One argument; allow-list; no winner; NOT IDENTIFIED | All upstream outputs + `final_project.md` | Integrated thesis update plan / patched synthesis; `SynthesisAgent_changelog.md` | All four above | No |
| **AdversarialReviewer** | Attack overclaims, method creep, language, stale cites | Synthesis + changelogs + Approved Set | Adversarial report + required fixes list; `AdversarialReviewer_changelog.md` | Synthesis | No (last) |

**Не создаём:** ML agent, DiD agent, 4 separate tech-case agents, literature-novelty agent, econometrics expander.

---

## 9. Detailed Agent Briefs

---

### 9.1 ResearchDesignAgent

**ROLE**  
Заморозить отвечаемый descriptive RQ; переписать рабочие гипотезы в D1–D2; архивировать H1–H6 как untested design; пометить устаревшие RQ-claims.

**CONTEXT**  
Target State A. Автор отклонил широкий causal RQ. `final_project.md` §1.2 уже содержит правильную формулировку — её нужно сделать **единственной** обложечной и провести по hypothesis layer.

**INPUTS**  
- `APPROVED_METHOD_SET.md`  
- `final_project.md` §1–2, §10  
- `research_design.md` §A–C  
- `reports/hypothesis_table.md`  
- `research_logic_final.md` (сужение RQ)

**TASK**  
1. Зафиксировать Frozen RQ **дословно** из Approved Set / `final_project.md` §1.2.  
2. Вставить D1 и D2 (точные формулировки из Approved Set).  
3. H1–H6: статус «archived design / not tested»; запрет SUPPORTED/PARTIAL.  
4. Watermark / баннеры на файлах, которые всё ещё продвигают полный RQ или H-verdicts (минимум: указать список + правки в `hypothesis_table.md`).  
5. Changelog с метками уверенности.

**QUESTIONS** (ответить в changelog, не блоковать)  
- Где ещё в репо «живой» старый RQ?  
- Нужен ли отдельный `RQ_FREEZE.md` или достаточно правок hypothesis_table + баннеров?

**WHAT TO CHECK**  
- Нет ли в D1/D2 каузальных organization→conversion claims.  
- Согласованы ли D1–D2 с intensity-vs-volume и missingness.

**WHAT TO CHANGE**  
- `reports/hypothesis_table.md` (D1–D2 + archive H).  
- Короткие баннеры/заметки на design-facing файлах по списку.  
- `ResearchDesignAgent_changelog.md`.

**WHAT NOT TO DO**  
- Не переписывать тело всего `final_project.md` (это Synthesis).  
- Не объявлять H1–H6 протестированными.  
- Не открывать State B / новый сбор данных.  
- Не менять Approved Method Set.

**DEPENDENCIES**  
Только Method Set (готов).

**OUTPUTS**  
- Обновлённая hypothesis table  
- Список watermarked files  
- `ResearchDesignAgent_changelog.md` (таблица Change|Reason|Evidence|Files|Downstream + CONFIRMED/LIKELY/UNCERTAIN/NEEDS_REVIEW)

**ACCEPTANCE**  
- Frozen RQ verbatim в changelog и hypothesis docs.  
- D1–D2 measurable, non-causal.  
- H1–H6 явно archived/not tested.

**HANDOFF**  
→ DataCanonAgent, TechMatrixAgent, QuantitativeAgent могут стартовать.

---

### 9.2 DataCanonAgent

**ROLE**  
Зафиксировать канон данных/подписей; устранить известные label/window contradictions; SUPERSEDED на stale files.

**CONTEXT**  
Articles CAGR 2010–21 vs 2010–23 — оба верны арифметически; канон = **оба + пик USA 2021**. BERD = PERFORMED. GBR researchers end = **2017**. TWN не в панели.

**INPUTS**  
- `data_reviewed/*`, `data/metadata/data_dictionary.csv`  
- `data_quality_final.md`, `PROJECT_STATE.md` §17  
- Outputs ResearchDesignAgent

**TASK**  
1. Canon CSV/note: articles CAGR оба окна + peak 2021.  
2. Joint-year labels на snapshot.  
3. BERD PERFORMED везде в канон-словаре.  
4. GBR end year 2017 (починить stale «2019»).  
5. SUPERSEDED banners: `remaining_risks.md`, `reports/final_synthesis.md`, др. из PROJECT_STATE.  
6. Changelog.

**QUESTIONS**  
- Какие metadata files ещё расходятся с reviewed dictionary?

**WHAT TO CHECK**  
- maxabs processed vs reviewed на shared cols (ожидание 0).  
- Patents pair resident+total mandatory в любых канон-таблицах.

**WHAT TO CHANGE**  
- Canon tables / dictionary fixes / SUPERSEDED banners.  
- `DataCanonAgent_changelog.md`.

**WHAT NOT TO DO**  
- Не импутировать missing; не добавлять TWN; не тянуть TOP500/AI Index.  
- Не пересчитывать M1 (это Quant).  
- Не удалять raw/results (только баннеры / не цитировать).

**DEPENDENCIES**  
ResearchDesignAgent (RQ freeze).

**OUTPUTS**  
- Canon artefacts + banners  
- `DataCanonAgent_changelog.md`

**ACCEPTANCE**  
- Dual-window articles documented; GBR=2017; BERD=PERFORMED; stale files bannered.

**HANDOFF**  
→ QuantitativeAgent + TechMatrixAgent.

---

### 9.3 QuantitativeAgent

**ROLE**  
Обновить Level 1 под Frozen RQ; сохранить M1 с правильной интерпретацией; один PCA repair attempt по protocol; убрать из аргумента неapproved методы.

**CONTEXT**  
Hard-constrained to **`APPROVED_METHOD_SET.md`**. M1 numbers authoritative. Old PCA: articles loading ≈ −0.36; M2 γ ≈ −0.118 — broken.

**INPUTS**  
- `APPROVED_METHOD_SET.md` (обязательно)  
- `data_reviewed/core_panel_reviewed.csv`, tables_reviewed  
- `regression_results_final.csv`, `results/pca_loadings.csv`  
- DataCanon outputs  
- `scripts/analysis_agent4.py` (reference; менять минимально и только под approved)

**TASK**  
1. Level 1 core refresh: joint-year, common-window CAGR (articles dual), dual-scale intensity vs volume.  
2. M1: keep; report HC1+cluster; interpret as within-country associational; CI cluster includes 0 → not an effect finding; placement appendix/secondary.  
3. PCA repair per protocol (intensity-only OR volume-only OR within-z); apply success gate; else DROP + appendix «why failed».  
4. If PCA passes: M2 optional secondary only; USA TFP=1 mandatory; no causality.  
5. DROP from argument: conversion, pooled inference, event-as-effect.  
6. Fix figure titles (esp. causal/convergence language).  
7. If blocked methodologically → `PROPOSED_METHOD_CHANGE.md` (не молча расширять set).

**QUESTIONS**  
- Какой из вариантов PCA (a/b/c) проходит gate на фактических данных?  
- Нужен ли новый appendix figure вместо F10?

**WHAT TO CHECK**  
- n, years, loadings signs, var explained.  
- Не смешаны ли GERD% и raw counts.  
- M1: не делать lag shopping / HAC для значимости.

**WHAT TO CHANGE**  
- Level 1 outputs / PCA repair artefacts / title fixes.  
- `QuantitativeAgent_changelog.md`  
- Optionally `PROPOSED_METHOD_CHANGE.md`

**WHAT NOT TO DO**  
- **Любые unapproved methods** (DiD, IV, GMM, ML, k-means, EN, FA default, State B pulls).  
- Force M2 after failed gate.  
- Claim tech→TFP or answer RQ with M1.  
- Expand TWN panel.

**DEPENDENCIES**  
Design + DataCanon. Parallel with TechMatrix OK.

**OUTPUTS**  
- Refreshed Level 1 + M1 placement note + PCA gate report  
- `QuantitativeAgent_changelog.md`

**ACCEPTANCE**  
- Level 1 отвечает D1; missingness numbers прозрачны.  
- M1 secondary with correct caveats.  
- PCA: pass documented OR fail+drop.  
- No unapproved method in outputs.

**HANDOFF**  
→ SynthesisAgent (with TechMatrix).

---

### 9.4 TechMatrixAgent

**ROLE**  
Свести 4 tech к **одной** 8×4 occupancy matrix; semis trade + TWN foundry qual hole; AI/HPC/quantum = `?`; убрать формат «четыре эссе».

**CONTEXT**  
State A: no new tech series. Taiwan = explicit hole + ~1 page qual foundry note. Allow-list: no leadership verdicts without measured cells.

**INPUTS**  
- Frozen RQ, D2  
- `final_project.md` §6  
- `tech_panel_reviewed.csv`, semi quarantine map  
- DataCanon labels

**TASK**  
1. Build occupancy matrix: rows = S,HC,RD,FIN,INN,COM,PRD,ADE; cols = AI, semis, HPC, quantum; cells = measured proxy / `?` / qual marker.  
2. Semis: HS8542 + ≠fab; short TWN foundry qualitative note (no panel expansion).  
3. AI/HPC/quantum: `?` (no TOP500/AI Index collection).  
4. Unify narrative into one framework section (not four independent essays).  
5. Changelog.

**QUESTIONS**  
- Какие qual markers допустимы без upgrade в `+`?

**WHAT TO CHECK**  
- Нет winner / fab claims from trade.  
- FIN/COM empty marked `?`.  
- TWN hole explicit.

**WHAT TO CHANGE**  
- Matrix artefact + unified tech draft.  
- `TechMatrixAgent_changelog.md`

**WHAT NOT TO DO**  
- Collect new series; expand TWN; four separate case agents’ style verdicts; grade `+` on expert-only cells.

**DEPENDENCIES**  
Design + DataCanon. Parallel with Quant OK.

**OUTPUTS**  
- 8×4 matrix + TWN note + unified tech text  
- `TechMatrixAgent_changelog.md`

**ACCEPTANCE**  
- One matrix; three tech columns mostly `?`; semis measured only where trade/macro exists; TWN hole documented.

**HANDOFF**  
→ SynthesisAgent.

---

### 9.5 SynthesisAgent

**ROLE**  
Собрать один coherent аргумент под Frozen RQ; enforce allow-list; no winner; mechanism NOT IDENTIFIED.

**CONTEXT**  
Priority stack: Frozen RQ + Approved Methods + upstream changelogs. `final_project.md` — база для интеграции, не для возврата старого causal thesis.

**INPUTS**  
- All upstream outputs + changelogs  
- `APPROVED_METHOD_SET.md`  
- `final_project.md`, `defense_risks.md`

**TASK**  
1. Один narrative arc: measurable gaps (D1) → holes (D2) → semis matrix stress-test → M1 secondary only → conclusions §10-style.  
2. Purge «USA converts / China scales» as conclusion.  
3. Mechanisms section = NOT IDENTIFIED.  
4. Cite canon numbers only; no stale reports as verdicts.  
5. Changelog.

**QUESTIONS**  
- Где M1 упоминать в main vs appendix для защиты?

**WHAT TO CHECK**  
- Allow-list compliance; years on figures; patents pair; HS H3/H6 caveat; no H-verdicts.

**WHAT TO CHANGE**  
- Integrated synthesis (update `final_project.md` or successor only as tasked by parent).  
- `SynthesisAgent_changelog.md`

**WHAT NOT TO DO**  
- Reopen State B; add unapproved methods; declare winner; restore H1 partial; treat M1/PCA as RQ answer.

**DEPENDENCIES**  
Design + DataCanon + Quant + TechMatrix.

**OUTPUTS**  
- Coherent thesis artefact  
- `SynthesisAgent_changelog.md`

**ACCEPTANCE**  
- Answers Frozen RQ; D1–D2 explicit; allow-list held; no winner; mechanisms NOT IDENTIFIED; methods match Approved Set.

**HANDOFF**  
→ AdversarialReviewer.

---

### 9.6 AdversarialReviewer

**ROLE**  
Последний скептический проход после интеграции: overclaim, method creep, language, stale citations, PCA/M1 misuse.

**CONTEXT**  
Запускается **только после** Synthesis. Не предлагает DiD/IV/ML «чтобы усилить».

**INPUTS**  
- Synthesis output  
- All `*_changelog.md`  
- `APPROVED_METHOD_SET.md`  
- `defense_risks.md`

**TASK**  
1. Attack: causal verbs; winner; conversion claims; M1 as effect; PCA without gate; stale file cites; missing years; trade=fab; TWN ignored.  
2. Classify findings HIGH/MEDIUM/LOW.  
3. Require fixes list for parent (не silent rewrite всего репо beyond brief).  
4. Changelog.

**QUESTIONS**  
- Остались ли пути цитирования SUPERSEDED files?

**WHAT TO CHECK**  
- Method Set compliance end-to-end.  
- D1/D2 not upgraded to causal H.

**WHAT TO CHANGE**  
- Adversarial report + fix list.  
- `AdversarialReviewer_changelog.md`

**WHAT NOT TO DO**  
- Invent new methods; reopen data collection; regrade H1–H6 as supported.

**DEPENDENCIES**  
SynthesisAgent complete.

**OUTPUTS**  
- Adversarial report  
- `AdversarialReviewer_changelog.md`

**ACCEPTANCE**  
- All HIGH issues listed with file pointers; no unresolved method creep without flag.

**HANDOFF**  
→ Parent / author (defense readiness).

---

### Changelog schema (все агенты)

Каждый `*_changelog.md` обязан содержать таблицу:

| Change | Reason | Evidence | Files | Downstream | Confidence |
|--------|--------|----------|-------|------------|------------|
| … | … | … | … | … | CONFIRMED / LIKELY / UNCERTAIN / NEEDS_REVIEW |

---

## 10. Execution Plan

**Важно:** агенты **ещё не запускались**. Parent запускает их **после** существования этого файла и `APPROVED_METHOD_SET.md`.

### Phase 0 — Methods locked (DONE when these files exist)

- [x] `APPROVED_METHOD_SET.md`  
- [x] `ORCHESTRATION_PLAN.md`  
- [ ] Parent confirms no reopen of State B / TWN panel / method creep

### Phase 1 — Design freeze

1. Launch **ResearchDesignAgent** (solo).  
2. Gate: Frozen RQ + D1–D2 + H archive accepted.

### Phase 2 — Canon + parallel content

3. Launch **DataCanonAgent**.  
4. After DataCanon acceptance (or after Design if only banners pending): launch **in parallel**:  
   - **QuantitativeAgent**  
   - **TechMatrixAgent**  
5. Gate: PCA gate documented; occupancy matrix exists; no unapproved methods.

### Phase 3 — Integration

6. Launch **SynthesisAgent**.  
7. Gate: single argument; allow-list; NOT IDENTIFIED.

### Phase 4 — Adversarial (last)

8. Launch **AdversarialReviewer**.  
9. Parent triage HIGH fixes → optional micro-passes (не новый agent zoo).

### Recommended launch order / parallel groups

| Step | Agents | Mode |
|------|--------|------|
| 0 | — | Files locked |
| 1 | ResearchDesignAgent | sequential |
| 2a | DataCanonAgent | sequential |
| 2b | QuantitativeAgent + TechMatrixAgent | **parallel** |
| 3 | SynthesisAgent | sequential |
| 4 | AdversarialReviewer | sequential last |

---

## 11. Risks

| Risk | Mitigation |
|------|------------|
| RQ drift back to causal conversion | Watermarks + Synthesis allow-list + Adversarial |
| PCA forced despite failed gate | Quant hard rule + Adversarial check |
| M1 read as RQ answer | Appendix placement + language rules |
| Stale files cited | DataCanon SUPERSEDED + Adversarial |
| Scope creep State B / TWN panel | Approved Set CLOSED flags |
| «USA converts / China scales» sneaks back | Allow-list KEEP; Adversarial language audit |
| Articles window cherry-pick | Dual-window canon mandatory |
| Parent launches agents out of order | Dependency graph §7–8 |

---

## 12. Definition of Done

Проект в Target State A считается orchestrationally done, когда:

1. Frozen RQ — единственный отвечаемый вопрос во всех актуальных thesis-facing docs.  
2. D1 и D2 сформулированы и согласованы с Level 1 + occupancy matrix.  
3. H1–H6 archived as untested; no SUPPORTED/PARTIAL.  
4. Level 1 canon включает dual-window articles + peak 2021; BERD PERFORMED; GBR 2017.  
5. M1 retained only as secondary/appendix associational; cluster CI∋0 respected.  
6. PCA: gate pass documented **или** dropped with «why failed» appendix — no silent M2.  
7. One 8×4 matrix; AI/HPC/quantum `?`; TWN hole + qual note; no four-essay structure.  
8. Synthesis: no winner; mechanisms NOT IDENTIFIED; allow-list held.  
9. Adversarial HIGH issues closed or explicitly accepted by author.  
10. All six `*_changelog.md` exist with confidence labels.  
11. No unapproved methods introduced.  
12. No claim that agents in this plan already ran before parent launch.

---

*Конец ORCHESTRATION_PLAN.md. Parent orchestrator: launch Phase 1 ResearchDesignAgent next.*

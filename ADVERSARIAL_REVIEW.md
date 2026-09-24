# Adversarial Review — State A (после Synthesis)

**Дата:** 2026-09-20  
**Агент:** AdversarialReviewer (ORCHESTRATION_PLAN.md §9.6)  
**Объект:** интеграция после SynthesisAgent; канон = `APPROVED_METHOD_SET.md`  
**Не делалось:** DiD/IV/ML; reopen State B; regrade H1–H6; redesign тезиса

---

## Executive verdict

**READY WITH FIXES** (не «defense-ready» без parent triage; не «not ready»).

Тело `final_project.md` (синтез 2026-09-20) в целом держит Frozen RQ, D1–D2, allow-list, no winner, mechanisms NOT IDENTIFIED, HS8542≠fab, TWN hole, dual-window articles, M1/PCA как secondary. **Главный риск защиты — не переписывание аргумента, а устаревший корпус и ложные «authority» пути** (`PROJECT_STATE.md`, `reports/tech_cases_comparison.md` «одна строка для доклада», SUPERSEDED-тела с H1-partial/77%). Хирургические правки в тезисе (преамбула DO NOT CITE, §5.3 θ_lres, §8 anti-winner, App A/B) применены в этом проходе; остальное — checklist для parent/author.

---

## Findings table

| ID | Severity | Issue | Evidence (file + pointer) | Required fix | Owner |
|----|----------|-------|---------------------------|--------------|-------|
| **ADV-H01** | **HIGH** | `PROJECT_STATE.md` — устаревшая иерархия и снимок: `final_project.md` как **2026-09-16**; нет `RQ_FREEZE` / `APPROVED_METHOD_SET` / `DATA_CANON` / D1–D2 / dual-scale / occupancy; гипотезы всё ещё «H1–H6»; этап «adversarial завершён» относится к старому проходу | `PROJECT_STATE.md` §§ «ИЕРАРХИЯ» п.1, Executive Summary «Гипотезы», «Этап» | Обновить иерархию и executive snapshot под State A 2026-09-20; указать этот adversarial report | Parent |
| **ADV-H02** | **HIGH** | Живая «одна строка для доклада» с запрещёнными глаголами «США **превращают**… Китай — … масштаб…» + H1-partial / finance-модель в том же файле | `reports/tech_cases_comparison.md` L149; также L141–144 (H1/H4 partial) | Усилить баннер: **DO NOT CITE one-liner**; удалить/зачеркнуть L149 или заменить allow-list фразой; в баннере **не** указывать `technology_cases_final.md` как «актуальное» | Author / parent |
| **ADV-H03** | **HIGH** | Баннер `tech_cases_comparison` шлёт читателя в `technology_cases_final.md`, который сам SUPERSEDED (77%, business-financed, cluster «невозможны») | `reports/tech_cases_comparison.md` L6–9; `technology_cases_final.md` L14–17 | Исправить pointer баннера → `final_project.md` + `tech_occupancy_matrix.md` | Author |
| **ADV-H04** | **HIGH** | Асимметрия caveats M1: β_GERD осторожно, θ_lres с p≈0 без равной оговорки → устная ловушка «кадры → TFP» | Было: `final_project.md` §5.3 до фикса; таблица lres ≈0 | **[APPLIED]** §5.3 + App A: θ_lres = ассоциация, не causal, не RQ | Adversarial (done); author verify oral script |
| **ADV-H05** | **HIGH** | Неполный DO NOT CITE: отсутствовали `tech_cases_comparison` / `analysis_report`; `PROJECT_STATE` мог читаться как authority поверх Frozen RQ | Было: преамбула `final_project.md` L9 | **[APPLIED]** расширен DO NOT CITE + явный отказ от стека `PROJECT_STATE` | Adversarial (done); parent still refresh PROJECT_STATE |
| **ADV-M01** | **MEDIUM** | Язык «D1 **supported**» в Quant changelog + колонка CSV `supports_D1_level` → дрейф к вердикту SUPPORTED (запрещён для H; рискован для D) | `QuantitativeAgent_changelog.md` L40; `dual_scale_intensity_volume.csv` header `supports_D1_level` | Переименовать колонку → `matches_D1_sign` / `consistent_with_D1`; в changelog: «Level-1 pattern consistent with D1», не «supported» | Author / Quant micro |
| **ADV-M02** | **MEDIUM** | SUPERSEDED-файлы **bannered, но тела ядовиты** (H1 partial, 77%, «cluster SE невозможны») — риск copy-paste в слайды | `remaining_risks.md` L31, L39, L53; `reports/final_synthesis.md` L94; `technology_cases_final.md` L73 | Не переписывать корпуса целиком; на защите пользоваться только `final_project` / `defense_risks`; опционально strikethrough ключевых строк | Author |
| **ADV-M03** | **MEDIUM** | Narrative arc §0 шаги 5–6 ставят M1/PCA в «карту аргумента» → структурное повышение Optional | `final_project.md` §0 rows 5–6 | В защите: RQ закрывают шаги 1–4+7; M1/PCA = «если спросят про регрессию» | Author (oral) |
| **ADV-M04** | **MEDIUM** | §8 таблица по стадиям легко читается как «кто сильнее на этапе» | `final_project.md` §8 | **[APPLIED]** anti-winner note над таблицей; oral: «это знаменатели, не grades» | Adversarial (done) |
| **ADV-M05** | **MEDIUM** | Старый `figures/F10_pca_tfp_scatter.png` лежит рядом с рабочими F1–F7; риск случайного слайда | `figures/F10_pca_tfp_scatter.png` vs `figures_reviewed/F10_appendix_pc1_intensity_ONLY.png` | В презентации только appendix PC1 **или** не показывать F10; подпись «не vs TFP» | Author |
| **ADV-M06** | **MEDIUM** | `hypothesis_table.md` всё ещё говорит, что ResearchDesign не запускал Level 1 (устарело после Quant/Synthesis) | `reports/hypothesis_table.md` L18 | Одна строка: Level-1 signs consistent with D1 (Synthesis); вердикт SUPPORTED **по-прежнему не ставится** | Author |
| **ADV-M07** | **MEDIUM** | App G / TWN note упоминают концентрацию frontier-узлов NL/JP/TW/KR — qual OK, но устно может звучать как finding | `final_project.md` App G; `TWN_FOUNDRY_QUAL_NOTE.md` | Держать формулу «structural caveat, не измеренный share» | Author (oral) |
| **ADV-L01** | **LOW** | «Intensity-фактор» могло путаться с FA | Было App B | **[APPLIED]** → intensity-индекс + «не FA» | Adversarial (done) |
| **ADV-L02** | **LOW** | Плотный абзац 2010-якорей в §5.1 без табличной разметки годов на каждом токене | `final_project.md` §5.1 L193 | Оставить; при цитировании всегда тянуть из dual-scale/snapshot | Author |
| **ADV-L03** | **LOW** | Старый `final_changelog.md` (2026-09-16) может казаться «последним adversarial» | `final_changelog.md` header | Pointer: актуальный = этот файл + `REQUIRED_FIXES.md` | Parent |

---

## Attack checklist (14) — результат

| # | Attack | Verdict on thesis body |
|---|--------|------------------------|
| 1 | Causal verbs / org→conversion restored? | **PASS** (запрещены; §7 NOT IDENTIFIED). **FAIL corpus:** tech_cases L149 |
| 2 | Winner / «USA converts, China scales»? | **PASS** thesis; **FAIL** stale one-liner |
| 3 | Conversion ratios / pooled corr as inference? | **PASS** (DO_NOT_USE; §3.3) |
| 4 | M1 as effect / RQ answer? | **PASS** с оговорками; **trap** θ_lres — mitigated |
| 5 | PCA without gate / old PCA / M2 capability→TFP? | **PASS** (repair PASS a; M2 not run; old DO NOT USE) |
| 6 | Stale SUPERSEDED cited as authority? | **PASS** thesis DO NOT CITE; **FAIL** PROJECT_STATE hierarchy + broken banner pointer |
| 7 | Missing years on key numbers? | **PASS** dual-scale / §10 |
| 8 | HS8542 as fab/node leadership? | **PASS** (§6.2) |
| 9 | TWN ignored; FRA as foundry substitute? | **PASS** (§6.3; TWN note) |
| 10 | AI/HPC/quantum filled with general macro? | **PASS** (30×`?`; §6.4) |
| 11 | D1/D2 → causal H; H1–H6 SUPPORTED? | **PASS** thesis; **WATCH** CSV/changelog «supported» |
| 12 | Method Set creep? | **PASS** (нет DiD/IV/ML/State B). Soft language creep only |
| 13 | Dual-scale as stage winners? | **MITIGATED** (§8 note) |
| 14 | Articles only one CAGR window? | **PASS** (оба окна + peak 2021) |

---

## Method Set compliance summary

| Layer | Status |
|-------|--------|
| Core (joint-year, dual CAGR articles, dual-scale, occupancy, allow-list, semis≠fab, TWN hole) | **Compliant** in `final_project.md` |
| Optional M1 / PCA repair (a) | **Compliant placement**; caveats present after ADV-H04 |
| Not approved (conversion, pooled inference, event-as-effect, old PCA/M2, DiD/IV/ML, TWN expand, winner, causal org→conversion) | **Not reintroduced** in thesis argument |
| Soft creep | «D1 supported» / `supports_D1_level` — **flagged** (ADV-M01), не новый метод |
| `PROPOSED_METHOD_CHANGE.md` | Не требуется (creep языковой, не методологический) |

---

## Allow-list / causality audit

| Check | Result |
|-------|--------|
| Allow-list в преамбуле | Present |
| §7 Mechanisms | All **NOT IDENTIFIED** |
| «Превращают / конвертируют / масштабирует» как вывод тезиса | Absent in `final_project` conclusion |
| M1 language | Associational; cluster CI∋0 for GERD; θ_lres caveat **added** |
| PCA language | Descriptive intensity index; not capability→TFP; M2 unused |
| D1/D2 | Descriptive; no SUPPORTED label in thesis |
| H1–H6 | Archived / not tested; no SUPPORTED restore |

---

## What is actually strong (preserve)

1. **Frozen RQ + D1 dual-scale** с явными joint years и **обоими** articles CAGR windows + peak USA 2021.  
2. **D2 occupancy 8×4** (1 measured / 1 qual / 30 `?`) — missingness как часть ответа.  
3. **Semis discipline:** HS8542 ≠ fab; CHIPS/BIS markers only; TWN qual hole; FRA ≠ substitute.  
4. **Mechanisms NOT IDENTIFIED** + явный no winner.  
5. **Canon labels:** BERD PERFORMED; GBR researchers →2017; patents resident+total-office pair; cluster SE reported.  
6. **PCA honesty:** old broken excluded; repair (a) documented; M2 not forced.

---

## Defense-readiness

| Criterion | Status |
|-----------|--------|
| Single coherent thesis answers Frozen RQ | Yes |
| Allow-list / no winner / NOT IDENTIFIED | Yes (thesis) |
| Methods = Approved Set | Yes |
| Corpus citation hygiene | **No** until ADV-H01–H03 closed |
| Oral trap M1 θ_lres / §8 misread | Mitigated in text; rehearse |

**Вердикт:** **ready with fixes** → parent применяет `REQUIRED_FIXES.md` (особенно PROJECT_STATE + tech_cases one-liner), затем можно считать defense-ready для State A.

---

## Handoff

→ **Parent / author** (`REQUIRED_FIXES.md`).  
Артефакты: этот файл; `REQUIRED_FIXES.md`; `AdversarialReviewer_changelog.md`.

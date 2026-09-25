# PROJECT_STATE.md — снимок состояния проекта (оркестрация 2026-09-20)


> **deep-research (2026-09-25):** на этой ветке действуют DEEP_RESEARCH_PLAN.md, DEEP_RQ_AND_HYPOTHESES.md, DEEP_LITERATURE_NOTES.md, DEEP_RESULTS.md. Старые RQ_FREEZE / APPROVED_METHOD_SET — для ветки report-20pp.

**Дата refresh:** 2026-09-22 (Cover original theme: covering RQ, абсолюты, snapshots, radar)  
**Тема:** «Путь развития США vs путь развития Китая: технологическое соперничество от фундаментальной науки до внедрения»  
**Тип:** учебное исследовательское исследование магистерской программы  
**Target State:** A + narrow tech snapshots (exploratory)

**Текущий тезис:** `final_project.md` (2026-09-22). Covering RQ и D1–D2 — `RQ_FREEZE.md`.  
**Не** объявлять winner; механизмы NOT IDENTIFIED. M1/PCA — appendix only / не доклад.

**Этот файл — навигатор, не authority поверх Frozen RQ.** При расхождении с `RQ_FREEZE.md` / `APPROVED_METHOD_SET.md` / `DATA_CANON.md` / `final_project.md` побеждают канон-файлы.

---

## ИЕРАРХИЯ АКТУАЛЬНЫХ ДОКУМЕНТОВ (2026-09-22)

При любом расхождении приоритет:

1. **`RQ_FREEZE.md`** — Covering RQ; D1–D2; snapshot ≠ measured; H1–H6 archived  
2. **`APPROVED_METHOD_SET.md`** — Core + absolute GERD/headcount + radar + narrow snapshots  
3. **`DATA_CANON.md`** + **`SNAPSHOT_SOURCE_LEDGER.md`** — числа, окна, снимки  
4. **`final_project.md`** (2026-09-22) — текущий тезис  
5. Dual-scale / occupancy: `dual_scale_with_absolutes.csv`, `tech_occupancy_matrix.md`, `tech_framework_unified.md`  
6. Figures: F1–F7; FIXED F8/F9; **F11 radar**; **F12 abs GERD**; old F10 excluded  
7. Defense: `defense_risks.md`  
8. M1 numbers (appendix only): `regression_results_final.csv`

**SUPERSEDED / DO NOT CITE as authority (файлы на диске сохранены):**

| Файл | Почему не authority |
|------|---------------------|
| `project_final.md` | Заменён `final_project.md` |
| `remaining_risks.md` | Stale (H1-partial / 77% language) |
| `reports/final_synthesis.md` | Old H-partial / stronger thesis |
| `reports/tech_cases_comparison.md` | Archive; one-liner neutralized; body still H-partial |
| `reports/analysis_report.md` | Pre-review analysis |
| `technology_cases_final.md` | Bannered; 77% / business-financed / cluster myths |
| `results/regression_results.csv`, `model2_*`, old mixed `pca_*`, `conversion_ratios.csv`, `correlations_pooled.csv` | DO NOT USE for inference |
| `figures/F10_pca_tfp_scatter.png` | EXCLUDED; if PCA: only `figures_reviewed/F10_appendix_pc1_intensity_ONLY.png` |
| `final_changelog.md` (2026-09-16) | **Не** последний adversarial; актуальный = `ADVERSARIAL_REVIEW.md` |
| Старый снимок PROJECT_STATE до этого refresh | Иерархия 2026-09-16 устарела |

**Панели данных:** `data_reviewed/core_panel_reviewed.csv`, `tech_panel_reviewed.csv` (предпочтительны); originals в `data/processed/`.

---

## 1. EXECUTIVE SUMMARY

| Элемент | Состояние |
|---------|-----------|
| **Тема** | США vs Китай: технологическое соперничество от фундаментальной науки до внедрения |
| **Исходный RQ (design history)** | Модели превращения ресурсов в результаты + tech-устойчивость по 4 технологиям — **не отвечаем** данными State A |
| **Frozen RQ (текущий)** | Различия уровней/трендов US–CN в измеримой macro-цепочке при фактических окнах + какие звенья TCI нельзя оценить (`RQ_FREEZE.md`) |
| **Основная идея** | Dual-scale intensity vs volume/share (D1) + occupancy missingness-as-result (D2); no overall/domain winner; mechanisms NOT IDENTIFIED |
| **Гипотезы** | **D1–D2** = current descriptive; **H1–H6** = archived design / not tested (SUPPORTED/PARTIAL/REJECTED **запрещены**) |
| **Технологии** | AI; semis; HPC; quantum — occupancy **1 measured / 1 qual / 30 `?`** |
| **Методы (Approved)** | **Core:** joint-year, dual CAGR articles, dual-scale, occupancy 8×4, allow-list, HS8542≠fab, TWN hole. **Optional:** M1 appendix (associational; cluster CI∋0); PCA repair **PASS (a) intensity-only** appendix; M2 **not run**. **Not approved:** conversion ratios, pooled-as-inference, DiD/IV/ML, State B pulls, winner, causal org→conversion |
| **Данные** | 8 стран (USA, CHN, KOR, JPN, DEU, GBR, ISR, FRA) × 2000–2024; analysis 2010–2023; AI/HPC/quantum/GVC/VC/fab — missing |
| **Этап** | Synthesis DONE; AdversarialReviewer DONE (**READY WITH FIXES**, 2026-09-20) → `ADVERSARIAL_REVIEW.md`; HIGH path-fixes applied (`FIXES_APPLIED.md`); residual MEDIUM/LOW = author oral/slides |
| **Считается завершённым (deliverables)** | Frozen RQ/methods/canon; dual-scale; occupancy; `final_project.md`; M1/PCA docs; defense_risks |
| **Незавершённое / не делать** | State B (TOP500/AI Index/TWN panel); H1–H6 tests; DiD/IV/ML; TCI composite as H1 test; presentation slides (author) |

**Главный вывод (`final_project.md` §10):** dual-scale D1 (intensity↑ USA, volume/share↑ CHN) = знаменательная арифметика, не organization model; D2 holes = часть ответа; механизмы NOT IDENTIFIED; HS8542≠fab; TWN qual hole; M1/PCA не отвечают на RQ.

---

## 2. PROJECT TIMELINE

Информация восстановлена по датированным MD/changelog. Нумерация агентов — логическая (явных ID «Agent N» в файлах не везде).

### Этап 0 / Research Design Agent — 2026-09-12

| Поле | Содержание |
|------|------------|
| **Задача** | Blueprint исследования |
| **Получил** | NOT FOUND (старт) |
| **Сделал** | RQ, H1–H6, TCI 8 блоков, 3 метода, 4 tech-кейса, лимиты, Phase 0–5 |
| **Решения** | Без IV/DiD/causal ML; 8–10 стран; max 15 indicators; не объявлять winner |
| **Создал** | `research_design.md` (v1.0) |
| **Проблемы** | Риск перегруза (15 indicators × 4 fields) |
| **Исправил** | — |
| **Оставил** | План сбора field-specific / STEM / SEMI / TOP500 / AI Index |

### Этап 1 / Data Map Agent — 2026-09-12

| Поле | Содержание |
|------|------------|
| **Задача** | Операционализация показателей |
| **Получил** | `research_design.md` |
| **Сделал** | Сократил до 12 core + tech modules; MVD=10; источники с URL |
| **Решения** | STEM убран; field pubs → 1 агрегат; VC→SHOULD; SEMI fab→trade+qual; Elastic Net optional |
| **Создал** | `data_map.md` |
| **Проблемы** | Платные SEMI/PitchBook; CN VC opaque |
| **Исправил** | Proxies / priority flags |
| **Оставил** | TWN в плане comparators; labour productivity MUST; GVC SHOULD; AI/HPC/quantum MUST для кейсов |

### Этап 2 / Data Collection — ~2026-09-12…13

| Поле | Содержание |
|------|------------|
| **Задача** | Сбор raw → processed |
| **Получил** | `data_map.md` |
| **Сделал** | WB WDI bulk; OECD BERD; PWT ctfp mirror; Comtrade HS8542; patents resident+nonresident; Stanford HTML (не CSV) |
| **Решения** | Панель: USA,CHN,KOR,JPN,DEU,GBR,ISR,**FRA** (не TWN); GERD из WB, не OECD MSTI; patents из WDI office-basis |
| **Создал** | `data/raw/*`, `data/processed/core_panel.csv`, `tech_panel.csv`, `scripts/collect_*.py`, `download_*.py`, `probe_*.py`, `notebooks/01_collect_core_data.py`, metadata JSON/CSV |
| **Проблемы** | TOP500 KeyError `'Rmax (TFlop/s)'`; AI/quantum не извлечены; Comtrade multi-record CHN/DEU; clean Comtrade USA-only |
| **Исправил** | Частично: quarantine rule `num_records==1` для semis |
| **Оставил** | AI/HPC/quantum NaN; GVC/VC/labor_prod не собраны; TWN отсутствует |

### Этап 3 / Analysis Agent 4 — ~2026-09-13

| Поле | Содержание |
|------|------------|
| **Задача** | Quantitative + 2 FE models + PCA |
| **Получил** | processed panels |
| **Сделал** | Snapshot, CAGR, slopes, conversion ratios, correlations, M1, PCA+M2, events, F1–F10, reports |
| **Решения** | Лимит 2 моделей; LSDV HC1; PCA 4 vars → TechPC1 |
| **Создал** | `scripts/analysis_agent4.py`, `results/*.csv`, `figures/F1–F10.png`, `reports/analysis_report.md`, `data_quality_report.md`, `tech_cases_comparison.md`, `final_synthesis.md`, ранний `hypothesis_table.md` |
| **Проблемы** | Несопоставимые CAGR-окна; NaN-ratios; M2 wrong sign; causal language; H1/H4 «partial» без TCI |
| **Исправил** | — (на этом этапе) |
| **Оставил** | Все проблемы интерпретации для ревьюеров |

### Этап 4 / Project Revision (критика интерпретации) — 2026-09-14

| Поле | Содержание |
|------|------------|
| **Задача** | 15 проблем (8 HIGH, 7 MEDIUM) — текстовые правки |
| **Получил** | reports + results |
| **Сделал** | Дисклеймеры USA=1, intensity/volume, MVA share, BERD 77%, H1/H4 inflate, M1 CI∋0, causal purge |
| **Создал** | `project_revision.md`, `remaining_risks.md`; правки в `reports/*` |
| **Проблемы** | Structural data gaps остаются |
| **Исправил** | Интерпретационные HIGH/MEDIUM в reports |
| **Оставил** | Missing tech panels; малая N; USA=1 |

### Этап 5 / Data Quality Reviewer — 2026-09-14

| Поле | Содержание |
|------|------------|
| **Задача** | Независимый аудит данных |
| **Получил** | raw/processed/results |
| **Сделал** | Reviewed panels; joint-year/common-window tables; F8/F9 FIXED; corrected labels (BERD PERFORMED; patents office; etc.) |
| **Создал** | `data_reviewed/*`, `scripts/build_reviewed_dataset.py`, `data_changes.md`, `data_quality_final.md` |
| **Проблемы** | BERD≠financed; patents≠origin; HS revisions; Comtrade lineage |
| **Исправил** | Документация + reviewed artefacts (оригиналы не тронуты) |
| **Оставил** | Need single-definition Comtrade re-pull; AI/HPC/quantum still missing |

### Этап 6 / Quant Reviewer — 2026-09-14

| Поле | Содержание |
|------|------------|
| **Задача** | Пересчёт количественного слоя |
| **Получил** | data_reviewed |
| **Сделал** | Подтвердил числа; M1 cluster SE; M2 exclude; lag/drop-one sensitivities |
| **Создал** | `quant_reviewed.md`, `quant_changes.md`, `regression_results_final.csv` |
| **Проблемы** | GBR «ends 2019» в тексте (позже исправлено на 2017); H1–H4 «mixed/weak» |
| **Исправил** | SE/CI/uncertainty; exclusion M2 |
| **Оставил** | Conflict с logic по вердиктам H (позже ужесточены) |

### Этап 7 / Technology Case Reviewer — 2026-09-14

| Поле | Содержание |
|------|------------|
| **Задача** | Tech cases AI/semis/HPC/quantum |
| **Получил** | reports + data_map + results |
| **Сделал** | Scope matrix; `?` для missing; [expert assessment]; 9 подмен |
| **Создал** | `technology_cases_final.md`, `technology_changes.md` |
| **Проблемы** | Ещё держал BERD «business-financed» и паритет 77% как антитезис; H1/H4 «partial» в синтезе |
| **Исправил** | Часть overclaims |
| **Оставил** | Конфликты с logic (паритет 77%; partial H) |

### Этап 8 / Research Logic Agent — 2026-09-14

| Поле | Содержание |
|------|------------|
| **Задача** | Логическая цепочка RQ→H→data→conclusion |
| **Получил** | все reviewed слои |
| **Сделал** | Сузил RQ; отозвал H1/H4 partial; отозвал FIN-паритет 77%; минимальный thesis; геополитика вне findings |
| **Создал** | `research_logic_final.md`, `logic_changes.md` |
| **Проблемы** | Разрывы цепи (см. §0 logic file) |
| **Исправил** | Интерпретационная логика |
| **Оставил** | Structural gaps |

### Этап 9 / Integration Agent — 2026-09-16

| Поле | Содержание |
|------|------------|
| **Задача** | Единый `project_final.md` |
| **Получил** | все слои + changelogs |
| **Сделал** | Интеграция с приоритетом logic; consistency check цифр |
| **Создал** | `project_final.md`, `integration_changelog.md` |
| **Проблемы** | Конфликты Q15 vs logic — в пользу logic |
| **Исправил** | Единый документ |
| **Оставил** | Adversarial gaps (см. final_changelog) |

### Этап 10 / Adversarial Review — 2026-09-16

| Поле | Содержание |
|------|------------|
| **Задача** | Скептический разбор `project_final.md` |
| **Получил** | `project_final.md` |
| **Сделал** | Исправил HIGH: HS ratio H3/H6; slope p-values disclaimer; years на каждой цифре; `?` вместо `+` для qual; геополитика из conclusion |
| **Создал** | `final_project.md`, `final_changelog.md`, `defense_risks.md` |
| **Проблемы** | См. residual risks в final_changelog |
| **Исправил** | Все HIGH + нужные MEDIUM из adversarial list |
| **Оставил** | Naive slopes; missing tech pulls; G=7 cluster fragile |

### Этап 11 / Hypothesis table sync — 2026-09-19

| Поле | Содержание |
|------|------------|
| **Задача** | Синхронизация таблицы гипотез |
| **Создал/обновил** | `reports/hypothesis_table.md` (дата 2026-09-19; источник `final_project.md` §2) |
| **Также** | Предыдущий `PROJECT_STATE.md` (2026-09-19) — краткий снимок; **настоящий файл его заменяет** |

**Неполная информация:** точные имена/промпты отдельных агентов сбора данных; кто именно запускал TOP500 (только KeyError в registry); даты коммитов git — **STATUS UNCLEAR / NOT CHECKED in this audit** (git не аудировался как источник истины).

---

## 3. CURRENT RESEARCH QUESTION

### Текущая формулировка (отвечаемая) — `final_project.md` §1.2

> Какие различия уровней и трендов US–CN наблюдаются в измеримой macro-цепочке в рамке 2010–2023 при фактических окнах: GERD/BERD/статьи/GDP/TFP 2010–2023, researchers joint 2022 / common 2010–2017, патенты 2010–2021, MVA joint 2021 / common 2010–2021, hitech 2010–2023, HS8542-стоимости с разрывами — и какие звенья TCI в принципе нельзя оценить имеющимися данными?

### Исходная формулировка — `research_design.md` §A / `final_project.md` §1.1

> Как различаются модели технологического развития США и Китая в превращении научно-исследовательских и производственных ресурсов в технологические результаты — и на каких этапах цепочки эти различия наиболее устойчивы для четырёх стратегических технологий?

### Почему изменена

Зафиксировано в `research_logic_final.md` §1 и `final_project.md` §1: вторая половина RQ требует 4 tech-панелей и `tci_scores.csv` (не построены). Полный RQ **неотвечаем** данными проекта; ответ на полный RQ был бы переутверждением.

### Что реально исследуется сейчас

- Macro-цепочка: GERD, BERD PERFORMED, researchers/млн, articles volume, patents counts (office), MVA share, hitech share, HS8542 nominal, GDP pc, TFP macro  
- Semiconductors — только trade/macro  
- AI / HPC / quantum — mapping + `?` / [expert assessment]  
- Ассоциация GERD↔TFP (M1), не causality  

### Явно не отвечают (`final_project.md` §1.3)

tech-зависимость H1; H2/H3/H5/H6 tests; causal conversion; overall winner.

---

## 4. CURRENT HYPOTHESES

Источник вердиктов: `final_project.md` §2 / `reports/hypothesis_table.md` (2026-09-19).  
Статусы **не** SUPPORTED/PARTIALLY/REJECTED в смысле подтверждения — все **Not tested / Insufficient**.

| ID | Hypothesis | What it predicts | How it is tested (preregistered) | Evidence (actual) | Current status |
|----|------------|------------------|----------------------------------|-------------------|----------------|
| **H1** | США и Китай — разный профиль сильных/слабых звеньев; смещение зависит от технологии | Gap US–CN по этапам различается между AI/semis/HPC/quantum | TCI-профиль 8–10 этапов × 4 tech; стабильность паттерна | `tci_scores.csv` **отсутствует**; 3/4 tech missing; semis только trade. Дескриптивно: intensity↑ USA, volume/share↑ CHN — **разные измерения / denominators**, не поддержка H1 | **Not tested as preregistered.** Старое «partially supported (macro)» **отозвано** |
| **H2** | Зрелость технологии определяет узкое звено | Semis→PRD; quantum→S/RD; AI/HPC промежуточно | Stage-gap × 4; rank-corr зрелости vs этапа | 1 частичный кейс; **нет независимого maturity measure** (circular risk). Qual-coherence ≠ evidence | **Insufficient / not tested** |
| **H3** | Finance mix связан с профилем цепочки | Private→INN/COM; state→PRD/scaling | Cross-country regression finance→outputs | Регрессия **не запускалась**; finance mix **unmeasured** (BERD=PERFORMED P_BERPCT ≠ financed; ISR BERD>GERD 2021–23). BERD/GERD~77% **отозван** как за и против. Pooled r≈0.16 DO NOT USE | **Not tested; finance mix unmeasured** |
| **H4** | Различие частично в конверсии, не только во входах | При контроле R&D/HC gap patents/pubs < capacity/export | Output/input ratios по этапам | `conversion_ratios.csv` **EXCLUDED** (counts÷intensities, разные знаменатели/годы). Гетерогенность разрывов — не тест конверсии. «Partial» **отозван** | **Not tested as preregistered** |
| **H5** | Export/market share зрелых tech сильнее предсказываются production, чем science | Production-only R² > science-only | Lagged regression export ~ science vs production | Export-регрессии **нет**. Pooled MVA–hitech 0.40 > articles–hitech 0.12 — between-bias, DO NOT USE | **Insufficient / not tested** |
| **H6** | Innovation–commercialization gap систематически различается | Gap-index US≠CN и ≠across tech | Gap-index по кейсам | COM **пуст**; gap-index не построен | **Insufficient / not tested** |

**Проблемы проверки (все H):** missing tech panels; COM empty; FIN unmeasured; conversion excluded; no H3/H5 models; circular maturity for H2.

**Итог классификации проекта:** полностью поддержана — 0; частично — 0; отвергнута сильно — 0.

---

## 5. ANALYTICAL FRAMEWORK

**TCI — Technology Chain Index** (`research_design.md` §D; operationalized in `final_project.md` §3–4).

| Stage | Что пытаются измерить | Показатели в панели | Источники | Quant/Qual | Предполагаемый вывод | Что реально измерено |
|-------|----------------------|---------------------|-----------|------------|----------------------|----------------------|
| **S Science** | Фундаментальная база | `scopus_articles` | WB IP.JRN.ARTC.SC | Quant (volume) | Science gap | Fractional S&E **volume**, не field/AI, не impact |
| **HC Human capital** | Кадры R&D | `researchers_per_million` | UNESCO UIS / WB | Quant (intensity) | HC gap | Per-million; ISR 0; GBR–2017; USA–2022; не качество |
| **RD R&D** | Ресурсы исследований | `gerd_pct_gdp` | WB GB.XPD.RSDV.GD.ZS (не OECD MSTI) | Quant | RD intensity | % GDP; CN GDP revisions |
| **FIN Finance** | Структура финансирования | `berd_pct_gdp` | OECD MSTI P_BERPCT | Quant mislabeled | Finance mix для H3 | **PERFORMED intensity**, не financed mix; FIN stage = **`?`** |
| **INN Innovation** | Патенты/прорывы | `patents_resident`, `patents_total_office` | WB IP.PAT.RESD (+nonres) | Quant counts | Innovation gap | Office-basis to 2021; not quality; CN subsidy peak |
| **COM Commercialization** | Startups/licenses/revenue/adoption | — | Planned AI private $, notable models | **Empty** | COM gap H6 | **NOTHING** |
| **PRD Production+scaling** | Мощности, выпуск | `mva_pct_gdp`; planned TOP500, SEMI fab | WB NV.IND.MANF.ZS | Quant share + missing tech | Production advantage | Macro **share** only; fab **`?`** |
| **ADE Adoption+export** | Внедрение, trade | `hitech_export_share`, `semi_exports_hs8542`; planned GVC | WB / Comtrade | Quant trade | Export presence | Trade/shares; **adoption not measured**; GVC missing |
| **Productivity** | Экономический эффект | `tfp_ctfp`, `gdp_pc_ppp` | PWT ctfp; WB PPP | Quant macro | Macro outcome | Aggregate TFP (USA=1 construction); not tech-TFP |

**Слабые / отсутствующие звенья:** COM (пусто); FIN (неизмерима как mix); ADE adoption; tech-specific S/INN/PRD для AI/HPC/quantum; fab capacity; GVC; labor productivity (planned MUST, not collected); TCI composite index (не построен).

**Три слоя (design):** (1) descriptive gap — **выполнен** с joint-year/common-window; (2) conversion — **запрещён** (ratios excluded); (3) cross-country pattern H3/H5 — **не выполнен** (кроме M1 на TFP).

---

## 6. DATA MAP

Панель: 8×25 = 200 country-years (2000–2024). Analysis window 2010–2023.

| Variable | Definition | Source | Years (effective) | Countries | Unit | Transformation | Purpose | Chain stage | Priority (data_map) | Reliability | Caveats |
|----------|------------|--------|-------------------|-----------|------|----------------|---------|-------------|---------------------|-------------|---------|
| `gdp_pc_ppp` | GDP pc PPP constant 2017 intl-$ | WB NY.GDP.PCAP.PP.KD | 2000–2024 (2024 prelim) | 8/8 | 2017 intl-$ | level | Macro normalize | Productivity | MUST | HIGH | Single vintage Sep-2026 |
| `gdp_real_growth` | Real GDP growth % | WB NY.GDP.MKTP.KD.ZG | raw exists | — | % | — | Trend context | Productivity | SHOULD | HIGH | **В панели/анализе почти не используется** |
| `labour_productivity_gdph` | GDP per hour | OECD GDPHRS | — | — | USD PPP/h | — | Productivity | Productivity | MUST in map | MED-HIGH | **PLANNED, NOT COLLECTED** |
| `tfp_ctfp` | TFP at constant PPPs | PWT mirror `ctfp` | 2000–2023 | 8 (USA const) | index | USA=1 by construction | Macro outcome / M1 y | Productivity | SHOULD | MEDIUM | **Not tech-TFP**; USA flat |
| `gerd_pct_gdp` | GERD % GDP | WB GB.XPD.RSDV.GD.ZS | →2023 | 8 | % GDP | level | RD input / M1 x | RD | MUST | HIGH | Not OECD MSTI; CN GDP denom |
| `berd_pct_gdp` | BERD **PERFORMED** % GDP | OECD MSTI P_BERPCT | full | 8 | % GDP | level | Was FIN mix | FIN/RD | MUST | HIGH | **≠ financed**; vintage ≠ WB GERD |
| `researchers_per_million` | Researchers FTE?/mn | UIS/WB SP.POP.SCIE.RD.P6 | uneven | ISR 0; GBR→2017; USA→2022 | per mn | log in M1 | HC | HC | MUST | HIGH | Intensity; FTE/headcount |
| `scopus_articles` | Fractional S&E articles | WB IP.JRN.ARTC.SC | →2023 | 8 | count | log in PCA | Science volume | S/INN | MUST | MED-HIGH | Not impact; not AI-field |
| `patents_resident` | Resident filings **at office** | WB IP.PAT.RESD | 2000–2021 | 8 | count | — | INN counts | INN | MUST | MEDIUM | Not WIPO origin; subsidy peak 2021 |
| `patents_total_office` | Resident+nonresident | derived | 2000–2021 | 8 | count | sum | Bias check | INN | reviewed add | MEDIUM | Pair with resident |
| `mva_pct_gdp` | Mfg VA % GDP | WB NV.IND.MANF.ZS | USA→2021 | 8 | % GDP | — | PRD macro | PRD | MUST | MED-HIGH | Share≠scale≠fab |
| `hitech_export_share` | HT % mfg exports | WB TX.VAL.TECH.MF.ZS | from 2007 | 8 | % | — | ADE | ADE | MUST | MEDIUM | SITC Rev.4 break; processing |
| `gvc_foreign_va_share` | Foreign VA in exports | OECD TiVA | — | — | % | — | GVC | ADE | SHOULD | MED-HIGH | **NOT COLLECTED** |
| `semi_exports_hs8542` | IC exports HS8542 | UN Comtrade legacy | retained 75 | DEU/FRA 0; CHN gap 2015–17 | USD | quarantine | Semis ADE | ADE/PRD | MUST* | HIGH values | Nominal; HS H3–H6; ≠fab |
| `hpc_top500_systems` | TOP500 count | TOP500 | — | — | count | — | HPC PRD | PRD | MUST* | HIGH if collected | **100% MISSING (KeyError)** |
| `hpc_top500_rmax_tflops` | Aggregate Rmax | TOP500 | — | — | TFlop/s | — | HPC | PRD | SHOULD | HIGH if | **MISSING** |
| `ai_publications_count` | AI pubs | Stanford AI Index | — | — | count | — | AI S | S | MUST* | MEDIUM | **MISSING** (HTML only) |
| `ai_citations_impact` | AI citations | Stanford | — | — | — | — | AI | S | — | — | **MISSING** |
| `ai_private_investment_usd_bn` | AI private $ | Stanford | — | — | USD bn | — | FIN/COM | FIN | SHOULD | MED-LOW CN | **MISSING** |
| `ai_notable_models` | Notable models | Stanford | snapshot | — | count | — | COM | COM | OPTIONAL | MEDIUM | **MISSING as series** |
| `quantum_ipf_count` | Quantum IPF | EPO–OECD 2025 | — | — | IPF | — | Quantum | S/INN | SHOULD | MEDIUM | **MISSING** (no extract) |
| `quantum_publications` | Quantum pubs | EPO–OECD | — | — | count | — | Quantum | S | OPTIONAL | MEDIUM | **MISSING** |
| VC / PitchBook | Private VC | — | — | — | — | — | FIN/COM | FIN | SHOULD→down | — | **NOT COLLECTED** |
| SEMI fab / nodes | Capacity share | SEMI | — | — | — | — | PRD | PRD | replaced | — | **Qual only** |
| STEM graduates | Human capital | UNESCO | — | — | — | — | HC | HC | **REMOVED** in data_map | — | Consciously excluded |
| Field-specific pubs×4 | Science by field | Scopus | — | — | — | — | S | S | **REMOVED** | — | → 1 aggregate |
| Government R&D separate | Public R&D | OECD | — | — | — | — | FIN | FIN | **MERGED** into GERD+BERD plan | — | Not separate series |

\*MUST for corresponding tech case.

**Policy events (narrative only, not DiD):** MiC2025 (2015); Micius/quantum (2016); Dual Circulation (2020); US NQI (2018); CHIPS Act (2022-08); BIS Oct22/Oct23; EU Chips Act; K-Chips — см. `data_map.md` §3.

---

## 7. DATA QUALITY

### Обзор проблем

| Variable | Problem | Severity | Current treatment | Consequence |
|----------|---------|----------|-------------------|-------------|
| `tfp_ctfp` | USA=1.000 every year 1994–2023 construction | HIGH if USA trend | Document; exclude USA TFP slope; M1 drop-USA sensitivity | Zero within-y for USA; FE-heavy R² |
| `berd_pct_gdp` | Labeled financed; actually PERFORMED; ISR BERD>GERD 2021–23 | HIGH for H3 | Relabel; never GERD−BERD; FIN=`?` | H3 unmeasurable |
| `patents_resident` | Labeled origin; actually office resident; 2021 CN subsidy peak | HIGH for levels | Pair with total-office 2.68x; window to 2021 | 5.44x alone overstates |
| `researchers_per_million` | ISR 0; GBR ends **2017**; USA ends 2022; FTE/headcount | HIGH for comparisons | Common-window 2010–2017; no interpolate | Unbalanced; intensity artefact |
| `hitech_export_share` | Series from 2007; SITC Rev.4 break Oct 2024 (~28% missing noted) | HIGH for early trends | Caveat; trend over break invalid | Cannot interpret long trend cleanly |
| `semi_exports_hs8542` | HS H3–H6 mixed; CHN 2015–17 quarantine; DEU/FRA 0; spikes; clean file USA-only stale | HIGH | `semi_status`; FIXED F8; no fab claims; 3.13x not like-for-like | Semis case descriptive only |
| `mva_pct_gdp` | Share misread as scale; USA 2022–24 missing | MEDIUM | Label share; joint-year 2021 | No fab/absolute MVA |
| `scopus_articles` | Volume≠impact; not AI-specific | MEDIUM | Volume-only language | No science leadership claim |
| `gerd_pct_gdp` | WB not OECD; CN GDP revisions | LOW–MED | Caveat | Ratio sensitive to denom |
| `gdp_pc_ppp` | 2024 preliminary | LOW | Note | Minor |
| Conversion ratios | Counts÷intensities mismatched | HIGH if used | **EXCLUDED DO NOT USE** | No conversion ranking |
| Pooled correlations | Simpson / composition | HIGH if used | **DO NOT USE for inference** | Sign flips within |
| M2 / PCA PC1 | Incoherent loadings; wrong sign γ | HIGH | **EXCLUDED**; F10 out | No tech index |
| AI/HPC/quantum | 100% missing | HIGH for tech RQ | `?` / insufficient | Full RQ unanswerable |
| GVC / VC / labor prod | Never collected | MEDIUM–HIGH for design | Mark excluded | Gaps in ADE/FIN/productivity |
| Missing values | Patterned by source (not MCAR) | — | Listwise in M1; no imputation | n=84; ISR dropped |
| Duplicates | NOT FOUND as data bug | — | — | — |
| Outliers | CHN semi +63% 2012–13; KOR +65% 2016–17; ISR hitech jumps | MEDIUM | Retained-but-flagged | Spikes ≠ trends |
| Structural breaks | SITC; HS revisions; CN GDP | HIGH | Document | Trend contamination |
| Interpolations | None | — | No impute (endorsed) | — |
| Estimated values | NOT FOUND beyond PWT construction | — | — | — |

**Статусы обработки:** многие проблемы **обнаружены и исправлены в текстах/reviewed tables**; значения raw/processed **не пересчитывались заново** (кроме reviewed add-ons). Проблемы tech-missing / USA=1 / small N — **оставлены** (structural). Показатели AI/HPC/quantum/GVC — **признаны непригодными / excluded**.

---

## 8. SOURCES

| Name | Organization | URL (as in project) | Data used | Claims supported | Period | Primary/Secondary | Reliability | Limitations |
|------|--------------|---------------------|-----------|------------------|--------|-------------------|-------------|-------------|
| World Bank WDI | World Bank | https://api.worldbank.org/v2/ ; indicator pages in data_map | GERD, researchers, articles, patents, MVA, hitech, GDP pc, growth | Macro chain descriptives | varies | Secondary | HIGH (macro) | CN revisions; patent office basis; SITC break |
| OECD MSTI | OECD | https://sdmx.oecd.org/.../DSD_MSTI@DF_MSTI | BERD PERFORMED % GDP; also raw USD PPP files | BERD levels (not finance mix) | 2000–2024 | Secondary | HIGH | ≠ WB GERD vintage |
| Penn World Table (mirror) | GGDC / open-numbers mirror | https://raw.githubusercontent.com/open-numbers/ddf--pwt--penn_world_table/ ; rug.nl in data_map | `ctfp`; also emp/hc/pop/rgdp* raw | TFP levels; M1 y | →2023 | Secondary | MEDIUM | USA=1 construction; not sectoral |
| UN Comtrade | UNSD | https://comtradeplus.un.org/ | HS8542 exports | Semis trade values | 2010–2024 partial | Primary trade | HIGH for values | Multi-record; HS rev; re-exports |
| WIPO (via WB) | WIPO | https://www3.wipo.int/ipstats/ (planned); actual via WB | Patents | Counts | →2021 | Secondary | MEDIUM | Quantity≠quality |
| UNESCO UIS | UNESCO | via WB / databrowser | Researchers | HC intensity | uneven | Secondary | HIGH | Coverage gaps |
| TOP500 | TOP500.org | https://www.top500.org/lists/top500/ | — | — | — | Primary | HIGH if collected | **Not collected (KeyError)** |
| Stanford AI Index | Stanford HAI | https://hai.stanford.edu/ai-index/... ; arxiv 2504.07139 | HTML folders only | — | — | Secondary composite | MEDIUM | **No audited CSV** |
| EPO–OECD Quantum | EPO/OECD | https://www.oecd.org/en/publications/mapping-the-global-quantum-ecosystem_010c37da-en.html | — | — | 2005–2024 planned | Secondary | MEDIUM | **No extract** |
| OECD TiVA | OECD | data-explorer TiVA URL in data_map | — | — | — | Secondary | MED-HIGH | **Not collected** |
| OECD Productivity | OECD | GDPHRS URL in data_map | — | — | — | Secondary | MED-HIGH | **Not collected** |
| NBS China | NBS | stats.gov.cn communiqué URL in data_map | Cross-check GERD narrative | — | 2024 | Primary | — | Mentioned, not panel source |
| Policy docs | Congress, BIS, State Council, etc. | various in data_map §3 | Event dates | Markers only | — | Primary | — | Not causal evidence |

**Правило аудита:** URL выше взяты **только из файлов проекта**; не выдумывались.

---

## 9. QUANTITATIVE ANALYSIS

### 9.1 Descriptive snapshot (joint-year)

- **Вопрос:** уровни USA vs CHN  
- **Источник авторитета:** `data_reviewed/tables_reviewed/descriptive_snapshot_latest_joint.csv`  
- **Ключевые значения:** см. §15 / §14  

### 9.2 CAGR common-window

- **Файл:** `descriptive_cagr_common_window.csv`  
- **Правило:** researchers 2010–2017; patents/MVA 2010–2021; else 2010–2023  
- **Примеры:** GERD USA 1.86%/yr vs CHN 3.33%; articles 2010–2023 CSV: USA ~0.43% vs CHN ~8.90% — **CONFLICTING** с текстом `final_project` «articles 2010–2021 USA 1.33% vs CHN 8.51%» (разные окна)  
- **Старые** `descriptive_cagr.csv` — несравнимые окна; DO NOT USE без пометки  

### 9.3 Trend slopes

- **Файл:** `results/trend_slopes_convergence.csv`  
- **Метод:** OLS `Y = a + b·(t−2010)`; DIFF interaction  
- **Статус:** naive SE/p; AR(1) ignored; **ориентир only** (`final_project` §3, §5.2)  
- **Примеры из final_project:** GERD slope diff naive p=0.29; articles slope diff naive p<0.001; MVA share both falling; GDP pc slopes +$1099 vs +$933, diff naive p=0.01; TFP CHN ~+0.0063/yr  

### 9.4 Conversion ratios — EXCLUDED

- **Файл:** `results/conversion_ratios.csv` — DO NOT USE  
- **Причина:** mismatched denominators/years  

### 9.5 Correlations — pooled EXCLUDED

- **Файлы:** `correlations_pooled.csv`, `correlations_tfp_inputs.csv`  
- **Пример артефакта:** pooled GERD–TFP −0.086 vs within ~+0.03 / +0.24  
- **GDPpc–TFP +0.91:** accounting-adjacent, not evidence  

### 9.6 Event CHIPS/BIS pre-post

- **Файл:** `event_CHIPS_BIS_prepost.csv`  
- **Метод:** mean 2020–21 vs 2022–23, n=2/cell, no SE  
- **Результаты:** IC USA −1.91%, CHN +7.24%; hitech USA share 19.70→21.21 (+1.51 pp; CSV `change_pct` +7.69% is % change of share); CHN hitech 30.75→27.17 (−3.58 pp; CSV −11.65%)  
- **Интерпретация проекта:** vertical lines «не эффект»; confounders  

### 9.7 M1 — см. §10

### 9.8 PCA/M2 — см. §11 (excluded)

---

## 10. ECONOMETRIC MODELS

### Model M1 (RETAINED_AS_DESCRIPTIVE_ONLY)

**Спецификация:**

\[
\mathrm{TFP}_{it} = \alpha_i + \delta_t + \beta\,\mathrm{GERD}_{i,t-1} + \theta\,\log(\mathrm{researchers\_per\_million})_{it} + \varepsilon_{it}
\]

LSDV (country FE + year FE). HC1 robust SE + country-cluster SE.  
Авторитет: `regression_results_final.csv`. Код: `scripts/analysis_agent4.py` (исходный HC1); cluster — в quant review.

#### Variables

| Symbol | Variable | Notes |
|--------|----------|-------|
| TFP | `tfp_ctfp` | USA=1 every year |
| GERD lag1 | `gerd_pct_gdp` t−1 | % GDP |
| lres | log(`researchers_per_million`) | contemporaneous |

#### Sample

- Countries with data: CHN, DEU, FRA, JPN, KOR (13 each); USA 12; GBR 7; **ISR 0**  
- Years: 2011–2023 (2010 lost to lag)  
- **N=84, K=20, df=64, G=7**  
- Window note: analysis frame 2010–2023  

#### Estimation

- FE: country + year  
- Lag: GERD only lag-1 (not theoretically justified; sensitivities lag0/lag2)  
- SE: HC1 and cluster (t critical with G−1=6)  

#### Results (authoritative)

| Term | β | SE_HC1 | p_HC1 | CI_HC1 | SE_cluster | p_cluster | CI_cluster |
|------|---|--------|-------|--------|------------|-----------|------------|
| gerd_lag1 | **0.02746** | 0.01427 | **0.059** | [−0.00051, 0.05543] | 0.03100 | **0.409** | [−0.04833, 0.10325] |
| lres | **0.05629** | 0.00429 | ~0 | [0.04787, 0.06470] | 0.00792 | ~0 | [0.03690, 0.07567] |

Также (из final_project / quant_reviewed): FE-only R²≈0.727; full R²≈0.992; corr(gerd_lag1,lres)=0.71; AR(1) resid 0.32–0.90.

**Sensitivities:**

| Spec | β_GERD | p_HC1 | N |
|------|--------|-------|---|
| lag0 contemp | 0.01250 | 0.418 | 91 |
| lag2 | 0.05250 | 0.001 | 77 |
| drop USA | 0.03290 | 0.038 | 72 |
| drop CHN | 0.01890 | 0.157 | 71 |
| drop KOR | 0.04870 | 0.017 | 71 |
| 2011–2021 | 0.03530 | 0.024 | 66 |
| pooled OLS no FE | **−0.207** | — | — |

#### Interpretation (project’s)

Единственная допустимая: условная ассоциация; HC1 CI includes 0; cluster wider; not distinguishable from zero at conventional 5%; not causal; magnitude: closing 0.53 TFP gap would need ~+19 pp GERD — absurd as multiplier. Tech attribution forbidden.

#### Limitations (documented)

endogeneity / reverse causality; omitted variables; small G=7; USA zero within-y; measurement error CN; lag mining; multicollinearity; serial correlation → HC1 understates uncertainty; no HAC.

---

### Model M2 (EXCLUDED_DO_NOT_USE)

**Спецификация:** TFP on TechPC1 lag1 + FE  

**PCA inputs:** gerd, berd, log researchers, log articles  
**Loadings PC1:** gerd +0.554; berd +0.528; logRes +0.533; logArticles **−0.360**  
**Var exp PC1:** 0.699  

**Result:** γ = **−0.11796** (wrong sign artefact)  
**Status:** EXCLUDED; F10 excluded  
**N PCA:** 91  

---

## 11. ML / PCA / OTHER METHODS

| Method | Status | Purpose | Data | Params / construction | Results | Interpretation | Limitations |
|--------|--------|---------|------|----------------------|---------|-----------------|-------------|
| **PCA → TechPC1** | Implemented then **EXCLUDED** | Capability index for M2 | 4 vars above | Complete-case; n=91 | PC1 69.9% var; incoherent signs | DO NOT USE | Mixes intensity+counts |
| **M2 FE on PC1** | EXCLUDED | Link «tech»→TFP | PC1 | Same FE | γ=−0.118 | Artefact | Wrong sign |
| **TCI index min-max/z** | **NOT STARTED** | H1 test | — | Planned in design | `tci_scores.csv` absent | — | Blocker for H1 |
| **K-means** | **NOT STARTED** | Optional clustering | — | design optional | — | — | — |
| **Elastic Net / Lasso** | **NOT STARTED** | Optional | — | design optional | — | — | — |
| **Normalization for TCI** | Not done | — | — | — | — | — | — |
| **Conversion ratios** | Built then excluded | H4 | mismatched | — | CSV exists | DO NOT USE | Denominator artefact |

Deep learning / causal ML / NLP: сознательно **не используются** (design).

---

## 12. TECHNOLOGY CASES

Источник актуальных вердиктов: `final_project.md` §6 (приоритет над `technology_cases_final.md` там, где конфликт — особенно grades `+` и паритет 77%).

### AI

| Stage | USA | China | Evidence | Confidence |
|-------|-----|-------|----------|------------|
| S (general articles) | ~ (ниже volume с ~2020) | + volume 2.17x (2023) | snapshot | MEDIUM volumes; **not AI** |
| HC/RD inputs general | + intensities | ~ lower levels | GERD/BERD/researchers | HIGH-MEDIUM intensity |
| FIN AI private $ | ?/H? | ?/H? | MISSING | Insufficient |
| INN general patents | ~ | + counts (pair 5.44/2.68, 2021) | snapshot | MEDIUM counts |
| COM frontier/adoption | ? | ? | MISSING | Insufficient |
| Bottleneck | ?/H? INN→PRD + allied compute | ?/H? frontier compute / impact | expert assessment | LOW |
| Economic effect AI→TFP | not tested | not tested | aggregate TFP only | Forbidden attribution |

### Semiconductors

| Stage | USA | China | Evidence | Confidence |
|-------|-----|-------|----------|------------|
| Design/IP | ?/H? | ?/H? | expert | LOW-MED |
| EDA | ?/H? | ?/H? dependence | expert; BIS markers | LOW |
| Equipment/EUV | ?/H? (EUV lever **allies NL/JP**) | ?/H? | expert | LOW-MED |
| Advanced fab | ?/H? | ?/H? | TWN/KOR outside panel | LOW |
| Mature/packaging | ? | ?/H? | MVA/IC **not** node evidence | LOW for nodes |
| Downstream | ?/H? | ?/H? | hitech w/ break | LOW-MED |
| ADE HS8542 | ~ $43.6bn (2023 H6) | + $136.4bn; 3.13x H6 vs H3 | Comtrade | MEDIUM values; ≠fab |
| Third countries | structural misspecification without TW/KR/NL/JP | same | qual | Insufficient as finding |

### HPC / Compute

| Type | USA | China | Evidence | Confidence |
|------|-----|-------|----------|------------|
| Supercomputing TOP500 | ? | ? | 100% MISSING | Insufficient |
| AI compute (hyperscale) | ? | ? | not in panel; ≠TOP500 | Insufficient |
| Commercial infra | ? | ? | missing | Insufficient |

Различать: Linpack Rmax ≠ AI workload ≠ cloud.

### Quantum

| Subfield | USA | China | Evidence | Confidence |
|----------|-----|-------|----------|------------|
| Computing | ?/H? | ?/H? | missing IPF | Insufficient |
| Communication | ?/H? | ?/H? Micius marker 2016 | policy marker | LOW |
| Sensing | mention only | mention only | none | — |
| Research/funding | ? | ? | NQI/programs markers | Insufficient |
| Commercialization / macro effect | **not measured** (старое «≈0» = assumption, not estimate — `final_project` TECH-4) | same | — | Insufficient |

---

## 13. ECONOMIC MECHANISMS

| Technology / input | → mechanism (claimed in design) | → economic variable | Expected effect | Evidence status | Empirical/conceptual | Strength | Limitations |
|--------------------|----------------------------------|---------------------|-----------------|-----------------|----------------------|----------|-------------|
| R&D (GERD) | innovation/productivity | TFP | positive | M1 association CI∋0 | Empirical weak | **None as mechanism** | endogeneity, lag, small N |
| Finance mix | INN/COM vs PRD | stage outputs | H3 | **Unmeasured** | Conceptual | None | BERD PERFORMED |
| S/INN volumes | → PRD scaling | MVA/IC | China scale | Qual only | Conceptual | Weak | no fab series |
| PRD | → export | hitech/IC | H5 | No regression | Conceptual | None | breaks, between corr |
| INN | → COM | revenue/adoption | H6 | COM empty | Conceptual | None | — |
| Upstream EDA/EUV/IP | → rents/leverage | prices/margins | geo leverage | **Not claimed as measured** | Conceptual | None | no price data |
| AI diffusion | manufacturing/downstream | productivity | — | Missing adoption | Conceptual | None | — |
| HPC peak | → usable compute | capability | — | Missing | Conceptual | None | — |
| Quantum options | → future COM | — | — | Not measured | Conceptual | None | — |
| Semiconductor bottleneck | production constraint | capacity/trade/geo | — | Qual + trade proxies | Mixed | Weak | trade≠fab |

**Итог проекта (`final_project` §7):** измеримы различия уровней/трендов метрик; стрелки «→» между звеньями — недоказанные предположения.

---

## 14. CURRENT FINDINGS

Каждый claim отдельно (из `final_project.md` / reviewed tables). Confidence — как в проекте.

| # | Exact claim | Evidence | Source | Q/Qual | H | Confidence | Caveats |
|---|-------------|----------|--------|-------|---|------------|---------|
| 1 | GERD 2023: USA 3.45 vs CHN 2.58 (ratio 0.748) | joint snapshot | descriptive_snapshot_latest_joint | Q | — | HIGH intensity | CN GDP revisions |
| 2 | BERD PERFORMED 2023: 2.66 vs 2.00 (0.754) | snapshot | same | Q | H3 | HIGH as level | Not finance model |
| 3 | Researchers/mn joint-2022: 4937 vs 1849 (0.375x) | snapshot | same | Q | — | MED-HIGH intensity | Denominator; not headcount |
| 4 | Articles 2023: 430843 vs 932712 (2.165x); crossover ~2020 | snapshot/trends | same + slopes | Q | — | MEDIUM volume | ≠impact; ≠AI |
| 5 | Patents 2021 resident 5.44x **and** total-office 2.68x | snapshot pair | same | Q | — | MEDIUM counts | Peak subsidies; office bias |
| 6 | MVA share joint-2021: 10.53% vs 26.62% (2.53x); both falling 2010–2021 | snapshot+CAGR | same + common CAGR | Q | — | MED-HIGH shares | ≠absolute ≠fab |
| 7 | Hitech 2023: 21.85% vs 26.57%; gap 9.5→4.7 pp 2010→2023 | snapshot | same | Q | — | MEDIUM | SITC break |
| 8 | IC 2023: $43.6bn vs $136.4bn (3.13x); 2010 $37.7 vs $29.6 (0.79) | Comtrade | snapshot | Q | — | MEDIUM values | H6 vs H3; ≠fab |
| 9 | GDP pc 2023: $74352 vs $22687 (0.305); abs gap $49321→$51664 | snapshot | same | Q | — | HIGH | Ratio≠level convergence |
| 10 | TFP 2023: USA 1.0 construction; CHN 0.471 (from 0.395) | PWT | same | Q | — | MEDIUM levels | Not tech-TFP |
| 11 | GERD growth parallel; slope diff naive p=0.29 | slopes | final_project §5.2 | Q | — | Orientative | Naive SE |
| 12 | M1 β_GERD=0.0275; HC1 CI includes 0; cluster p=0.409 | regression_results_final | M1 | Q | — | Association only | Fragile |
| 13 | H1–H6 not tested as preregistered | missing tests | §2 | Meta | all | — | — |
| 14 | FIN structure unmeasured | BERD definition + ISR inversion | data_quality_final | Meta | H3 | — | — |
| 15 | AI/HPC/quantum insufficient for US–CN verdicts | 100% missing | §6 | Qual | H1/H2 | Insufficient | — |
| 16 | Intensity vs volume pattern is denominator arithmetic, not model discovery | logic §3.4 | research_logic / final | Interpretive | H1 | — | Circular if overclaimed |
| 17 | CHIPS/BIS effects not estimated | event n=2 | event CSV | Q descriptive | — | — | Not causal |
| 18 | M2/PCA/conversion/pooled corr not usable | reviews | quant_reviewed | Meta | — | — | DO NOT USE |

Отрицательные / null findings сохранены: M1 неотличима от нуля; ни одна H не поддержана; tech cases без вердиктов.

---

## 15. CURRENT USA VS CHINA COMPARISON

Актуальная матрица: `final_project.md` §8.

| Dimension | USA | China | Evidence | Confidence |
|-----------|-----|-------|----------|------------|
| Science (article volume) | ~ below since ~2020 | + 2.17x 2023 | snapshot | MEDIUM; ≠leadership |
| Human capital (res/mn) | + 4937 vs 1849 joint-2022 | ~ | snapshot | MED-HIGH intensity |
| R&D GERD% | + 3.45 vs 2.58 2023 | ~ | snapshot/trend | HIGH intensity |
| Financing structure | ? | ? | unmeasured | Insufficient |
| Innovation patents counts | ~ | + 5.44/2.68 pair 2021 | snapshot | MEDIUM counts |
| Commercialization | ? | ? | empty | Insufficient |
| Manufacturing MVA share | lower 10.5% j-2021 | higher 26.6% | snapshot | MED-HIGH share |
| Fab / mature nodes | ? | ? | no SEMI | Insufficient |
| Scaling (tech) | ? | ? | — | Insufficient |
| Adoption | ? | ? | — | Insufficient |
| Exports hitech | ~ 21.8% | + 26.6% | snapshot | MEDIUM; break |
| Exports IC HS8542 | ~ $43.6bn | + $136.4bn | Comtrade | MEDIUM; ≠fab |
| GVC | ? | ? | not collected | Insufficient |
| AI | ? (specific) | ? | missing | Insufficient |
| Semiconductors (capability) | ? stages | ? stages | trade+qual | Mixed |
| HPC | ? | ? | missing | Insufficient |
| Quantum | ? | ? | missing | Insufficient |
| Productivity TFP | 1.0 construction | 0.47 catch-up levels | PWT+M1 | MEDIUM levels |
| GDP pc | $74.4k | $22.7k; abs gap up | WB | HIGH |

---

## 16. WHAT HAS ALREADY BEEN CRITICIZED

Сводка по `project_revision.md`, `data_changes.md`, `quant_changes.md`/`quant_reviewed.md`, `technology_changes.md`, `logic_changes.md`, `integration_changelog.md`, `final_changelog.md`.

### A. Project revision (2026-09-14) — 8 HIGH + 7 MEDIUM

| Source | Claim/problem | Severity | Fixed? | How | Remaining |
|--------|---------------|----------|--------|-----|-----------|
| project_revision #1 | TFP USA=1 interpreted as trend | HIGH | Yes (text) | Disclaimer construction | Structural USA=1 |
| #2 | Intensity vs volume as finding | HIGH | Yes | Denominator artefact language | Pattern still described carefully |
| #3 | MVA share as scale | HIGH | Yes | Share-only | No absolute MVA |
| #4 | Researchers per-million flipped | HIGH | Yes | Label intensity | Absolute heads claim later **deleted** (logic) |
| #5 | BERD contradicts private-model claim | HIGH | Partial→later superseded | Initially «77% both» | Logic: 77% **revoked entirely** |
| #6 | H1/H4 inflated | HIGH | Yes then strengthened | partial→not tested | — |
| #7 | M1 overinterpreted | HIGH | Yes | CI∋0; R² FE | Still fragile |
| #8 | Causal verbs | HIGH | Yes | Allow-list | Watch regressions |
| #9–15 | Patent peak; SITC; IC nominal; events n=2; matrix +/−; GDP gap; KOR proxies | MEDIUM | Yes in reports | Caveats | Structural |

### B. Data quality review

BERD financed→PERFORMED; patents origin→office; articles fractional; GDP vintage; TFP construction; hitech break; MVA share; semi quarantine/HS; joint-year/common-window tables; F8/F9 FIXED; Comtrade clean stale.

### C. Quant review

Pooled corr exclude; M2 exclude; cluster SE; lag fragility; drop-one; G=7 warning; causal purge. Residual: wrote «GBR ends 2019» (**error**, corrected to 2017 by logic); H verdicts «mixed/weak» later **overridden** to not tested.

### D. Technology review

Overclaims on AI leadership; trade=fab; grades without data; etc. Residual: still used business-financed + 77% antithesis + H1/H4 partial in synthesis — **overridden by logic/final**.

### E. Logic review (H1–H10, M1–M10)

RQ unanswerable; H1/H4 partial revoked; FIN unmeasured; intensity circular; trade→fab; predecided thesis; geopolitics as findings; heads without calc deleted; CAGR windows; GBR 2017; causal verbs; KOR headlining; HS revisions; H2 circular; CHIPS lines; COM empty arrows; TFP catch-up as tech.

### F. Integration

Accepted data/quant/tech/logic with conflict resolutions favoring logic+data quality.

### G. Adversarial (`final_changelog.md`)

| ID | Problem | Sev | Fixed in final_project? |
|----|---------|-----|-------------------------|
| RQ-1 | 2010–2023 without actual windows | MED | Yes |
| RQ-2 | Meta-question on missing | LOW | Kept with discipline |
| H-1 | Pooled r=0.16 as fact | MED | Marked DO NOT USE example |
| H-2 | Coherence as soft support | LOW | Kept with disclaimer |
| D-1 | HS 3.13x mixes revisions | HIGH | H3/H6 caveat everywhere |
| D-2 | Bare incomparable CAGRs | MED | Removed bare pairs |
| M-1 | Slope p as tests | HIGH | Naive disclaimer |
| M-2 | USA «consumes» rows wording | MED | Reformulated |
| M-3 | K=20 / within-r ambiguity | LOW | Expanded |
| Q-1 | Mixed years in thesis | HIGH | Years on each figure |
| Q-2 | Slopes vs endpoints | LOW | Labeled |
| TECH-1 | `+` for expert assessment | HIGH | `?/H?` |
| TECH-2 | MVA/IC as bottleneck evidence | HIGH | Removed parentheticals |
| TECH-3 | KOR CAGR as fab | MED | Removed |
| TECH-4 | Quantum effect ≈0 | MED | «Not measured» |
| TECH-5 | Speculative TOP500 HIGH confidence | LOW | Softened |
| E-1/E-2 | Mechanism titles / catch-up wording | LOW | Renamed/clarified |
| C-1 | Geopolitics in conclusion | HIGH | Moved to Appendix G |

---

## 17. KNOWN CONTRADICTIONS

| Issue | Source A | Source B | Contradiction | Resolution |
|-------|----------|----------|---------------|------------|
| Document authority | `reports/final_synthesis.md` (old H partial, stronger thesis) | `final_project.md` | Different verdicts/thesis | **Resolved:** final_project wins |
| H1/H4 status | Old reports / technology_cases_final synthesis «partial» | final_project / hypothesis_table 2026-09-19 | partial vs not tested | **Resolved:** not tested |
| BERD definition | data_map / technology_cases «business-financed»; F9 title | data_quality_final / final_project PERFORMED | financed vs performed | **Resolved:** PERFORMED |
| BERD/GERD ~77% | project_revision, technology_cases, remaining_risks as evidence against finance narrative | research_logic / final_project | Use as disproof vs **revoked entirely** | **Resolved:** revoked (neither for nor against) |
| GBR researchers end year | quant_reviewed «ends 2019» | data_quality_final / logic «ends 2017» | 2019 vs 2017 | **Resolved:** **2017** |
| Comparators | research_design/data_map: **TWN** in 8 | Actual panel: **FRA**, no TWN | Taiwan missing | **UNRESOLVED as design vs data** (FRA substituted; not documented as formal decision in one place) |
| Articles CAGR window | final_project §5.2: 2010–2021 1.33% vs 8.51% | descriptive_cagr_common_window: 2010–2023 ~0.43% vs ~8.90% | Different windows/numbers | **UNRESOLVED** which common-window for articles is canonical |
| MVA CHN level in prose | Sometimes 25.0% (2023) | Joint-year 26.62% (2021) | Different years | **Resolved in final:** use joint-2021 for ratios; 2023 only with label |
| Patents gap | key_findings / old texts 5.44 only | reviewed pair 5.44+2.68 | Single vs pair | **Resolved:** pair mandatory |
| Event hitech USA | «+1.5 pp» in prose | CSV change_pct +7.69 | pp vs % change of share | **Resolved if careful:** +1.5 pp is correct reading of levels |
| USA TFP years | Some texts «2000–2023» | Verified 1994–2023 construction | Start year of verification | Minor; construction holds |
| project_final vs final_project | Two finals | Adversarial edits | Nearly same + fixes | **Resolved:** final_project current |
| remaining_risks still lists 77% and H1 partial language | remaining_risks.md | final_project | Stale residual risk file | **UNRESOLVED file drift** — treat remaining_risks as partially stale |
| data_dictionary.csv berd label | «Business R&D expenditure» | reviewed dictionary PERFORMED | Label drift in `data/metadata` | **UNRESOLVED in original metadata** (reviewed CSV correct) |
| HPC columns in data_dictionary | VALID WITH CAVEAT | Actually MISSING | Status wrong in old dictionary | **Resolved in reviewed** indicator_quality |
| Clean Comtrade vs panel | clean USA-only | tech_panel 75 from legacy | Lineage confusion | **Resolved by documentation:** legacy is source |
| Quant Q15 vs Logic H | mixed/weak H | not tested | Verdict language | **Resolved:** logic/final |

---

## 18. UNRESOLVED PROBLEMS

### HIGH

1. Полный RQ и H1 tech-dependence **не тестируемы** без 4 tech-панелей + TCI.  
2. AI / HPC / quantum **100% missing**.  
3. COM block empty → H6 impossible.  
4. Finance mix unmeasured → H3 impossible.  
5. M1 not distinguishable from zero; identification weak (endogeneity, G=7, USA=1).  
6. Semis: trade≠fab; HS revision mix; DEU/FRA missing; CHN 2015–17 gap.  
7. Design included TWN; panel has FRA — third-country semis story incomplete in data.  
8. Conversion / pooled / M2 artefacts still on disk — risk of misuse by future agent.

### MEDIUM

1. Patents only to 2021; subsidy peak.  
2. Researchers unbalanced (ISR/GBR/USA).  
3. Hitech SITC break.  
4. No labor productivity / TiVA / VC series.  
5. Slopes SE naive (no HAC).  
6. Articles common-window number conflict (2010–21 vs 2010–23 texts/CSV).  
7. `remaining_risks.md` / some `reports/*` / `technology_cases_final.md` partially stale vs `final_project.md`.  
8. Old figures F8/F9/F10 still present alongside FIXED/excluded.

### LOW

1. Metadata label drift (`data/metadata/data_dictionary.csv`).  
2. gdp_real_growth collected but little used.  
3. Multiple probe/download scripts clutter.  
4. Previous PROJECT_STATE shortened some nuances.  
5. Presentation / slides NOT FOUND.

---

## 19. CURRENT PROJECT STRUCTURE

```
Macroeconomics-master-project/
├── PROJECT_STATE.md              ← этот аудит (актуальный снимок)
├── research_design.md            ← design v1.0 (2026-09-12)
├── data_map.md                   ← data map v1.0 (2026-09-12)
├── final_project.md              ← ★ CURRENT FINAL REPORT
├── final_changelog.md
├── project_final.md              ← superseded by final_project
├── research_logic_final.md
├── logic_changes.md
├── integration_changelog.md
├── quant_reviewed.md
├── quant_changes.md
├── technology_cases_final.md
├── technology_changes.md
├── project_revision.md
├── remaining_risks.md            ← partially stale
├── defense_risks.md
├── regression_results_final.csv  ← ★ M1 authority
├── data/
│   ├── raw/                      ← WB, OECD, PWT, Comtrade, patents, Stanford HTML…
│   ├── processed/                ← core_panel.csv, tech_panel.csv, indicator_quality.csv
│   └── metadata/                 ← dictionaries, source_registry, sources*.json
├── data_reviewed/                ← ★ reviewed panels + quality docs + FIXED figs
│   ├── core_panel_reviewed.csv
│   ├── tech_panel_reviewed.csv
│   ├── data_quality_final.md
│   ├── data_changes.md
│   ├── figures_reviewed/F8_*.png, F9_*.png
│   └── tables_reviewed/*.csv
├── results/                      ← Agent4 outputs (many DO NOT USE for inference)
├── figures/                      ← F1–F10 (F8/F9 originals superseded; F10 excluded)
├── reports/                      ← audit trail; hypothesis_table.md synced 2026-09-19
├── scripts/                      ← collect/download/probe/analysis/build_reviewed
└── notebooks/01_collect_core_data.py
```

**Важные файлы — назначение / статус / актуальность / зависимости:**

| File | Purpose | Status | Current? | Depends on |
|------|---------|--------|----------|------------|
| final_project.md | Unified conclusions | Complete post-adversarial | **YES primary** | all reviewed layers |
| research_design.md | Preregistered plan | Frozen design | YES for H definitions | — |
| data_map.md | Planned indicators | Frozen plan | YES for intent; NOT for actual BERD/patent labels | research_design |
| data_reviewed/core_panel_reviewed.csv | Analysis panel | Ready w/ caveats | YES values | data/raw |
| regression_results_final.csv | M1 numbers | Authoritative | YES | reviewed panel + quant |
| technology_cases_final.md | Tech detail | Mostly; grades superseded where conflict | Secondary to final §6 | results, data_map |
| reports/final_synthesis.md | Old synthesis | Superseded | NO for verdicts | — |
| tci_scores.csv | TCI index | **ABSENT** | — | — |
| figures_reviewed/F8,F9 | Corrected plots | Authoritative for F8/F9 | YES | reviewed tech/core |

---

## 20. WHAT IS ACTUALLY COMPLETE

| Element | Status |
|---------|--------|
| research design | **COMPLETE** |
| data map | **COMPLETE** (plan) |
| data collection | **MOSTLY COMPLETE** for macro core; tech incomplete |
| data validation | **MOSTLY COMPLETE** (reviewed layer) |
| descriptive analysis | **MOSTLY COMPLETE** (with window fixes) |
| econometrics | **MOSTLY COMPLETE** for M1 only; H3/H5 **NOT STARTED** |
| PCA/ML index | **COMPLETE then EXCLUDED** / TCI **NOT STARTED** |
| AI case | **MOSTLY COMPLETE** as insufficiency writeup |
| semiconductors | **MOSTLY COMPLETE** (trade+qual) |
| HPC | **MOSTLY COMPLETE** as insufficiency writeup |
| quantum | **MOSTLY COMPLETE** as insufficiency writeup |
| synthesis | **COMPLETE** (`final_project.md`) |
| presentation | **NOT STARTED** / NOT FOUND |
| report (final md) | **COMPLETE** |
| hypothesis tests preregistered | **NOT STARTED** (documented as not tested) |

---

## 21. CURRENT OUTPUTS

| Output | File(s) | Status |
|--------|---------|--------|
| Final report | `final_project.md` | Current |
| Hypothesis table | `reports/hypothesis_table.md` | Synced 2026-09-19 |
| Defense Q&A | `defense_risks.md` | Current |
| M1 results | `regression_results_final.csv` | Authoritative |
| Joint snapshot | `data_reviewed/tables_reviewed/descriptive_snapshot_latest_joint.csv` | Use this |
| Common CAGR | `.../descriptive_cagr_common_window.csv` | Use this |
| Old snapshot/CAGR | `results/descriptive_*.csv` | Superseded for comparisons |
| Key findings crib | `results/key_findings.csv` | Handy but check pair patents / exclusions |
| Event table | `results/event_CHIPS_BIS_prepost.csv` | Descriptive only |
| Figures F1–F7 | `figures/*.png` | Endorsed w/ caveats in text |
| Figures F8/F9 | `data_reviewed/figures_reviewed/*_FIXED.png` | Authoritative |
| Figure F10 | `figures/F10_*.png` | EXCLUDED |
| Panels | processed + reviewed | Reviewed preferred |
| Notebooks | `notebooks/01_collect_core_data.py` | Collection helper (script-like) |
| Draft conclusions | embedded in final_project §10 | Current |
| PowerPoint / PDF report | NOT FOUND | — |

---

## 22. DEPENDENCIES

```
research_design.md
    → data_map.md
        → data/raw/*  (WB, OECD, PWT, Comtrade, patents, HTML stubs)
            → data/processed/core_panel.csv + tech_panel.csv
                → scripts/analysis_agent4.py
                    → results/*.csv + figures/F1–F10 + reports/*
            → scripts/build_reviewed_dataset.py
                → data_reviewed/core_panel_reviewed.csv
                  + tech_panel_reviewed.csv (+ patents_total_office, semi_status)
                    → tables_reviewed (joint snapshot, common CAGR, effective N)
                    → figures_reviewed F8/F9 FIXED
                    → quant_reviewed.md → regression_results_final.csv
                → data_quality_final.md
            → technology_cases_final.md (uses results + quality)
            → research_logic_final.md (uses all reviewed)
                → project_final.md
                    → final_project.md (+ adversarial)
                        → reports/hypothesis_table.md (2026-09-19)
                        → defense_risks.md
```

**Если изменить X, пересчитать Y:**

| Change | Forces recompute |
|--------|------------------|
| raw GERD/researchers/TFP | core panel → M1 → thesis language on β |
| Comtrade re-pull | tech panel → F8 → semis claims → event table |
| Add AI/HPC/quantum CSV | tech panel → cases → H1/H2 possibility → RQ scope |
| Fix BERD to true financed same vintage | FIN cell → H3 feasibility |
| Build TCI | new scores → H1 test → possibly rewrite §10 |
| Drop/add countries | all FE N/G → M1 |

---

## 23. CURRENT FINAL ARGUMENT

Как сейчас делает проект (`final_project.md`):

1. **Starting problem:** US–CN tech rivalry along science→deployment chain; need to know *where* paths diverge, not who wins.  
2. **Research question:** Narrowed to measurable macro gaps/trends + what cannot be measured.  
3. **Hypotheses:** H1–H6 preregistered; all **not tested**; observations do not upgrade verdicts.  
4. **Evidence:** Joint-year levels and common-window trends on intensities vs volumes/shares; carefully caveated semis trade.  
5. **Technology cases:** Semis = trade + expert stage map with `?`; AI/HPC/quantum = insufficient.  
6. **Quantitative evidence:** Descriptives + fragile M1 association GERD↔TFP (CI includes 0); M2/PCA excluded.  
7. **Economic mechanisms:** Explicitly **not identified**; arrows are hypotheses.  
8. **Final conclusion:** Description of metric asymmetries (denominator arithmetic), weak/null GERD–TFP link, no tech-dependence proof, no winner, no causal conversion story.

---

## 24. IMPORTANT THINGS NOT TO LOSE

- **Definitions:** BERD = PERFORMED (P_BERPCT); patents = office-basis; articles = fractional volume; TFP USA=1 construction; MVA = share; HS8542 = nominal with H3–H6.  
- **Allow-list language:** ассоциировано / условная корреляция / дескриптивно / неотличимо от нуля / не измерено / не тестируемо.  
- **Priority stack:** final_project > logic > regression_results_final > data_quality_final > quant/tech > reports.  
- **Never cite alone:** patents 5.44x; IC 3.13x without H3/H6; BERD/GERD 77%; pooled correlations; conversion ratios; M2; F10.  
- **Joint-year rule:** never ratio with NaN side.  
- **Common-window rule:** researchers 2010–2017; patents/MVA 2010–2021.  
- **Excluded indicators:** STEM; field×4 pubs; TWN (de facto); labor productivity; GVC; VC; SEMI fab quant.  
- **Excluded methods:** IV, DiD, synthetic control, causal ML, ranking conversion efficiency.  
- **Comtrade lineage:** panel from **legacy** multi-response filtered `num_records==1`, not clean USA-only file.  
- **Unresolved contradictions:** articles CAGR window; remaining_risks drift; TWN vs FRA.  
- **Event n=2:** not CHIPS/BIS effects.  
- **Appendix G:** geopolitics not findings.  
- **Preregistration discipline:** descriptive coherence ≠ hypothesis support.

---

## 25. QUESTIONS THAT THE CURRENT PROJECT CANNOT ANSWER

- Полный RQ о tech-specific устойчивых узких местах по 4 технологиям.  
- H1 tech-dependence; H2 maturity→bottleneck (no independent maturity).  
- H3 finance→outputs; H5 production vs science for exports; H6 INN–COM gap.  
- Causal effect of R&D on productivity / of CHIPS/BIS / of industrial policy.  
- Who leads in AI / HPC / quantum (panel).  
- Fab capacity, EDA/EUV shares, advanced-node leadership (quant).  
- Commercialization performance (startups, licenses, adoption, revenue).  
- GVC foreign-VA structure.  
- Sectoral / tech-TFP contribution to growth.  
- Whether US or CN «model» is more efficient at conversion.  
- Absolute manufacturing scale from MVA shares alone.  
- Quality-adjusted science/innovation leadership (citations, triadic/PCT).  

---

## 26. AUDIT METADATA

| Field | Value |
|-------|-------|
| Audit date | **2026-09-20** |
| Files surveyed (approx.) | **~124** project files (excluding `.codex` rules); deep-read of all major MD/CSV outputs |
| Datasets / CSV | **~55** CSV files |
| Notebooks/scripts | **1** notebook-style collector + **~17** Python scripts |
| Figures | **10** in `figures/` + **2** FIXED in `data_reviewed/figures_reviewed/` |
| Materials unavailable | Live re-download of WB/OECD/TOP500/AI Index; git history not used as authority; agent chat transcripts not exhaustively re-read (folder noted but not primary evidence) |
| Could not fully verify | Exact reproduction of every Agent4 figure pixel; Stanford HTML contents beyond «present»; whether `project_final` ≡ `final_project` byte-diff beyond changelog claims (changelog taken as record of adversarial edits) |
| Needs extra verification by next agent | Articles CAGR window conflict; re-run `build_reviewed_dataset.py` + M1 if touching data; confirm FRA-vs-TWN decision rationale; refresh stale `remaining_risks.md` against `final_project.md` if used |

**Audit constraint honored:** no project fixes, no new research, no hypothesis re-grading beyond documenting existing statuses, no external facts invented.

---

*Конец PROJECT_STATE.md (refresh 2026-09-20). Начать с иерархии выше + `RQ_FREEZE.md` / `APPROVED_METHOD_SET.md` / `DATA_CANON.md` / `final_project.md`. Adversarial: `ADVERSARIAL_REVIEW.md`. Fixes: `FIXES_APPLIED.md`. §§ ниже — исторический audit trail; не перекрывают Frozen RQ.*

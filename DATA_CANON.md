# DATA CANON — канон данных и подписей

**Дата:** 2026-09-20; **refresh:** 2026-09-22 (абсолюты + snapshots + articles crossover)  
**Агент:** DataCanonAgent / ScopeKeeper refresh  
**Статус:** Binding для QuantitativeAgent / TechMatrixAgent / SynthesisAgent  
**Панель:** 8 стран — USA, CHN, KOR, JPN, DEU, GBR, ISR, **FRA** (не TWN) × 2000–2024  
**Авторитетные значения:** `data_reviewed/*` (esp. `core_panel_reviewed.csv`, `tables_reviewed/*`); snapshots в `data/raw/snapshots/`

---

## 0. Articles volume crossover (канон)

| Факт | Значение |
|------|----------|
| Последний год USA > CHN по `scopus_articles` | **2016** (USA 431 808; CHN 430 350) |
| Первый год CHN > USA | **2017** (USA 435 377; CHN 464 154) |
| **Запрещено** | формулировка «кроссовер ~2020» |

Источник: `data_reviewed/core_panel_reviewed.csv`; график F3.

---

## 1. Articles CAGR — dual-window + peak (канон)

**Ни одно окно само по себе не является единственным каноническим числом.**  
Оба окна арифметически верны; разница USA объясняется пиком 2021 и спадом 2021→2023.

| Window | USA CAGR | CHN CAGR | Источник |
|--------|----------|----------|----------|
| **2010–2021** | **1.33%/yr** | **8.51%/yr** | `core_panel_reviewed.csv` (endpoint CAGR) |
| **2010–2023** | **0.43%/yr** | **8.90%/yr** | то же + `descriptive_cagr_common_window.csv` |

**Пик USA:** 2021, `scopus_articles` = 471 378 (далее 2022: 447 539; 2023: 430 843).

Канон-CSV: `data_reviewed/tables_reviewed/articles_cagr_dual_window.csv`.

**Правило цитирования:** всегда указывать окно `(t0,t1)` рядом с числом; при сравнении US–CN growth допустимо показывать **оба** окна или явно выбрать одно с обоснованием (пик / полный горизонт анализа).

---

## 2. Joint-year labels (snapshot)

Срезы уровней — только по **latest jointly available year** на переменную (не «все в 2023»).

| Variable | Joint year | Канон-таблица |
|----------|------------|---------------|
| GERD, BERD, articles, hitech, GDP pc, TFP, semi (retained) | **2023** | `descriptive_snapshot_latest_joint.csv` |
| researchers_per_million | **2022** | то же (USA 2023 n/a) |
| patents_resident **и** patents_total_office | **2021** | то же (пара обязательна) |
| mva_pct_gdp | **2021** | то же (USA 2022–23 n/a) |

Common-window CAGR (balanced endpoints): researchers **2010–2017**; patents **2010–2021**; MVA **2010–2021**; остальные core (кроме semi caveats) **2010–2023** — см. `descriptive_cagr_common_window.csv`.

---

## 3. BERD = PERFORMED % GDP

| Правило | Деталь |
|---------|--------|
| Определение | `berd_pct_gdp` = OECD MSTI **`P_BERPCT`** — **BERD PERFORMED % GDP** |
| Не путать | ≠ business-**financed** / finance mix / доля частного финансирования |
| Следствие | FIN-mix **unmeasured**; BERD/GERD ~77% **отозван** (ни за, ни против finance-нарратива) |
| Vintage | ≠ WB GERD; ISR BERD>GERD 2021–23 — артефакт винтажа, не «>100% finance» |

---

## 4. GBR researchers end year = **2017**

| Факт | Значение |
|------|----------|
| Последний non-missing GBR `researchers_per_million` | **2017** |
| n в окне 2010–2017 | **8** |
| M1 после lag | GBR **7** obs (2011–2017) |
| **Ошибка** | формулировки «GBR ends **2019**» — **неверны**; не цитировать |

Подтверждено: `data_quality_final.md`, `effective_samples_2010_2023.csv`, панель.

---

## 5. Patents — пара resident + total office

В любой канон-таблице / dual-scale / snapshot:

- `patents_resident` (office-basis, WDI `IP.PAT.RESD`)
- `patents_total_office` (resident + nonresident; reviewed addition)

**Запрещено** цитировать только 5.44× (resident 2021) без пары 2.68× (office-total 2021).  
Counts ≠ quality; 2021 = пик субсидий CN.

---

## 6. Панель: FRA, не TWN

| Решение | Статус |
|---------|--------|
| 8-я страна в панели | **FRA** |
| TWN | **не в панели**; не добавлять; не импутировать; TechMatrix — qualitative hole / foundry note |

---

## 7. Missing tech columns vs thin snapshots

`hpc_top500_*`, `ai_*`, `quantum_*` в **панели** = **MISSING** (100% NaN) — статус словаря **MISSING**.

**Разрешено (2026-09-22):** точечные CSV-снимки в `data/raw/snapshots/` со статусом occupancy **`snapshot`** (не `measured`):

| Файл | Домен |
|------|--------|
| `top500_snapshot.csv` | HPC |
| `ai_index_snapshot.csv` | AI |
| `quantum_epo_oecd_snapshot.csv` | Quantum |

Полный State B panel pull по-прежнему **закрыт**. Ledger: `SNAPSHOT_SOURCE_LEDGER.md`.

---

## 7b. Absolute scale (reuse from disk)

| Indicator | Source | Unit | Joint-year rule | Caveat |
|-----------|--------|------|-----------------|--------|
| `gerd_usd_ppp` | `data/raw/oecd_gerd_usd_ppp.csv` (OECD MSTI) | **млн USD PPP** | latest joint USA–CHN (обычно 2023/2024) | **Не** комбинировать арифметически с WB `gerd_pct_gdp` (разные винтажи) |
| `researchers_headcount_est` | `researchers_per_million` × `pwt_pop` | **тыс. чел.** (оценка) | joint year где есть оба (USA часто 2022) | `pop` в PWT = **миллионы**; формула: `res_per_mn × pop_mn / 1000` |
| `pwt_hc` (optional) | `data/raw/pwt_hc.csv` | индекс | joint year | Не STEM graduates |

Канон-таблица: `data_reviewed/tables_reviewed/dual_scale_with_absolutes.csv`.

---

## 8. Processed vs reviewed

На shared columns `data/processed/core_panel.csv` ↔ `data_reviewed/core_panel_reviewed.csv`:  
**maxabs ≈ 0** (CONFIRMED 2026-09-20).  
Единственная доп. колонка reviewed: `patents_total_office`.

---

## 9. Что не цитировать из stale-файлов

| Артефакт | Проблема |
|----------|----------|
| `remaining_risks.md` | 77%; H1 partial; «cluster SE невозможны» (cluster SE **посчитаны**, p≈0.409) |
| `reports/final_synthesis.md` | H1/H4 partial; 77%; cluster «невозможны» |
| `technology_cases_final.md` | business-financed; 77%; H1 partial |
| `quant_reviewed.md` (до фикса DataCanon) | «GBR ends 2019» |

Актуальный синтез: `final_project.md`. RQ/гипотезы: `RQ_FREEZE.md`, `reports/hypothesis_table.md`.

---

## Pointers

| Файл | Роль |
|------|------|
| `data_reviewed/core_panel_reviewed.csv` | Числовой канон панели |
| `data_reviewed/tables_reviewed/*` | Joint snapshot, common CAGR, dual-window articles |
| `data_reviewed/data_dictionary_reviewed.csv` | Предпочтительные labels |
| `data/metadata/data_dictionary.csv` | Выровнен DataCanon (BERD PERFORMED; HPC MISSING) |
| `data_reviewed/data_quality_final.md` | Качество / caveats |
| `RQ_FREEZE.md` | Frozen RQ + D1–D2 |
| `APPROVED_METHOD_SET.md` | Методы (не менять) |

*Конец DATA_CANON.md.*

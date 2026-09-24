# DATA CANON — канон данных и подписей

**Дата:** 2026-09-20; **refresh:** 2026-09-24 (NSF Indicators 2026 articles → 2024; hitech/BERD joint 2024)  
**Агент:** DataCanonAgent / ScopeKeeper refresh  
**Статус:** Binding для QuantitativeAgent / TechMatrixAgent / SynthesisAgent  
**Панель:** 8 стран — USA, CHN, KOR, JPN, DEU, GBR, ISR, **FRA** (не TWN) × 2000–2024  
**Авторитетные значения:** `data_reviewed/*`; snapshots в `data/raw/snapshots/`; статьи 2014–2024 (USA/CHN/DEU/GBR/JPN) — `data/raw/nsf_se_articles_indicators2026.csv`

---

## 0. Articles volume crossover (канон)

| Факт | Значение |
|------|----------|
| Последний год USA ≥ CHN по `scopus_articles` | **2016** (NSF 2026: USA 431 848; CHN 429 614) |
| Первый год CHN > USA | **2017** (NSF 2026: USA 435 539; CHN 463 411) |
| Уровни **2024** | USA **439 892**; CHN **1 078 580** (≈2.45×) |
| Пик USA | **2021** = **472 375** (NSF) |
| **Запрещено** | формулировка «кроссовер ~2020» |

Источник: NSF *State of U.S. Science and Engineering 2026*, Figure 29 (Scopus fractional count; accessed Aug 2025). Вшито в панель для USA/CHN/DEU/GBR/JPN на 2014–2024. До 2014 и страны KOR/ISR/FRA — прежний World Bank WDI vintage.

---

## 1. Articles CAGR — dual-window + peak (канон)

**Ни одно окно само по себе не является единственным каноническим числом.**  
Разница USA объясняется пиком 2021 и спадом после него.

| Window | USA CAGR | CHN CAGR | Источник |
|--------|----------|----------|----------|
| **2010–2021** | **~1.35%/yr** | **~8.58%/yr** | `articles_cagr_dual_window.csv` |
| **2010–2024** | **~0.55%/yr** | **~9.37%/yr** | то же |

Канон-CSV: `data_reviewed/tables_reviewed/articles_cagr_dual_window.csv`.

**Правило цитирования:** всегда указывать окно `(t0,t1)` рядом с числом.

---

## 2. Joint-year labels (snapshot)

Срезы уровней — только по **latest jointly available year** на переменную (не «все в 2024»).

| Variable | Joint year | Канон-таблица |
|----------|------------|---------------|
| GERD % GDP, TFP | **2023** | `descriptive_snapshot_latest_joint.csv` |
| BERD %, articles, hitech, GDP pc | **2024** | то же |
| researchers_per_million | **2022** | то же (USA 2023 n/a) |
| patents_resident **и** patents_total_office | **2021** | то же (WB новее не отдаёт) |
| mva_pct_gdp | **2021** | то же (USA 2022–24 n/a) |
| HS8542 | **2023** | mutual USA–CHN |

Common-window CAGR: researchers **2010–2017**; patents/MVA **2010–2021**; articles dual **2010–2021** и **2010–2024**; GERD% **2010–2023**; BERD/hitech **2010–2024**.

### 2b. Freshness rule (2026-09-24)

Не требовать единый календарный 2025/2026. Брать последний сопоставимый joint-year по показателю. Не смешивать винтажи без пометки. Не добивать дыры (патенты после 2021; HS8542 без пары CHN после 2023).
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

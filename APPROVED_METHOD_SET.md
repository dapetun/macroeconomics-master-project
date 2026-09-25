# APPROVED METHOD SET


> **На ветке deep-research** методы задаёт DEEP_RESEARCH_PLAN.md / DEEP_RQ_AND_HYPOTHESES.md.

**Дата утверждения:** 2026-09-20; **refresh:** 2026-09-24 (ветка `report-20pp`, 20-страничный отчёт)  
**Статус:** **APPROVED**  
**Target State:** A — честная измеримая карта + тонкие tech-snapshots  
**Авторитет чисел:** `data_reviewed/tables_reviewed/*` (Level 1 + absolutes); `data/raw/snapshots/*` (exploratory); `regression_results_final.csv` (M1 appendix only); пересчёт в `notebooks/`

---

```text
APPROVED METHODS — 20-page report core

Core (methods 1–5, 9, 12, 18):
- 1 Joint-year levels + ratios (год на каждой цифре; запрет ratio с NaN-стороной)
- 2 Common-window CAGR с явными (start, end, n)
- 3 Articles: ОБА окна CAGR 2010–2021 и 2010–2023 + пик USA 2021; crossover 2016–2017
- 4 Separate OLS trend lines per country (articles = a + b × year)
- 5 Pooled two-country OLS with year × China interaction (d = slope difference)
- Dual-scale table: intensity vs volume/share + АБСОЛЮТНЫЙ GERD PPP и headcount researchers
- 9 PCA intensity-only (GERD%, BERD%, researchers/mn): variance share + loadings; NOT capability index
- 12 Within-country correlations — descriptive association only
- 18 Point snapshots: TOP500, Stanford AI Index, EPO–OECD quantum
- Semis caveat: HS8542 ≠ fab; TWN = qual hole (½ page max)
- Allow-list языка
- Графики F1–F7 + FIXED F8/F9 + F12; нейтральные заголовки

Appendix only:
- 14 / M1 TWFE: cluster CI для GERD включает 0; не ответ на RQ
- Fragility table M1 — as-is

NOT in report (removed 2026-09-24):
- Method 8 equal-weight z-index
- Method 11 hierarchical / k-means clustering
- Method 13 first-difference regression
- Radar F11 (was illustration for method 8)

Not approved:
- Старый PCA/M2/F10 как evidence (кроме intensity PCA repair как method 9)
- Conversion ratios / ranking конверсии
- Pooled correlations как inference
- Event CHIPS/BIS как эффект
- TCI composite как тест H1; H3/H5 regressions
- K-means, Elastic Net, DiD, IV, SC, GMM, SEM, Bayesian, VAR/VECM, causal ML
- Полный 2010–2025 TOP500 panel / полный AI Index time series / SEMI fab paid / TiVA / STEM / PitchBook
- Расширение панели на TWN; winner; causal org→conversion→TFP
- Повышение snapshot → measured без нового ряда
```

---

## Covering RQ (exact wording)

> Как по сопоставимым показателям 2010–2023 годов различаются пути США и Китая вдоль цепочки от науки до экспорта, если смотреть отдельно интенсивность (доля в ВВП, исследователи на миллион) и объём (абсолютные расходы, численность, статьи, патенты, доли производства и экспорта)? Что по искусственному интеллекту, суперкомпьютерам и квантовым технологиям показывают доступные точечные снимки на конкретные годы?

Технические окна данных — в `DATA_CANON.md` / `RQ_FREEZE.md` (спецификация, не обложка).

**Не отвечаем:** causal H1–H6 tests; overall winner; fab-лидерство из trade.

---

## Две descriptive hypotheses (D1, D2)

Вердикты SUPPORTED/PARTIAL/REJECTED **запрещены**.

### D1 — Intensity vs volume

Как в `RQ_FREEZE.md`: противоположные знаки intensity vs volume/share при выбранных шкалах; абсолютный GERD PPP / headcount — дополнительный volume-слой (может перевернуть знак относительно intensity).

### D2 — Missingness / thin coverage

Ряды без panel = `?`; точечные внешние выписки = `snapshot` (exploratory); TWN foundry = `qual`. Не «неизмеримо в принципе». В 20-страничном отчёте D2 **не** центр сюжета (максимум ½ страницы occupancy).

---

## Absolute scale rules

| Indicator | Source file | Unit | Formula / note |
|-----------|-------------|------|----------------|
| `gerd_usd_ppp` | `data/raw/oecd_gerd_usd_ppp.csv` | млн USD PPP (OECD MSTI) | **Не** вычитать из / делить на WB `gerd_pct_gdp` — разные винтажи |
| `researchers_headcount_est` | panel × `pwt_pop.csv` | тыс. человек (оценка) | `researchers_per_million × pop_millions / 1000`; pop в PWT = **миллионы** |
| `pwt_hc` (optional) | `data/raw/pwt_hc.csv` | индекс HC (PWT) | Тонкое покрытие «образование»; не STEM |

---

## Method 4 vs method 5

- **Method 4:** две отдельные прямые (США отдельно, Китай отдельно). Сравнение наклонов — глазами.
- **Method 5:** одна регрессия `y = a + b·year + c·China + d·(year×China)`. Коэффициент `d` — насколько наклон Китая отличается от наклона США. Если доверительный интервал для `d` не содержит ноль, разница наклонов в этой спецификации статистически отличима от нуля. Это **описание двух прямых**, не каузальный эффект политики.

Рекомендуемые ряды для 4+5: `scopus_articles` и `gerd_pct_gdp` (не больше двух рядов в основном тексте).

---

## PCA (method 9)

Intensity-only: `gerd_pct_gdp`, `berd_pct_gdp`, `researchers_per_million`.  
Ссылка на ремонт: `results/pca_repair_a_intensity_*.csv`, ~90.7% на первой компоненте.  
Язык: «сжатие сонаправленных рядов интенсивности», **не** «индекс способностей / технологической мощи».

---

## M1 / TWFE (method 14, appendix)

M1 — **appendix only**, не в narrative arc. Числа: `regression_results_final.csv`, `M1_INTERPRETATION.md`.  
Честная фраза: при кластерных стандартных ошибках доверительный интервал коэффициента GERD включает ноль. USA TFP = 1 by construction (PWT `ctfp`).

---

## Taiwan / allow-list

- TWN: qualitative hole; **NO** panel expansion; FRA ≠ foundry substitute.
- Allow-list: «ассоциировано», «условная корреляция», «дескриптивно», «неотличимо от нуля», «не измерено в этой работе», «снимок / exploratory».
- Запрещено: winner; «США превращают / Китай масштабирует» как механизм; causal verbs; leadership без measured/snapshot evidence; «неизмеримо в принципе»; SUPPORTED.

---

## Scope freeze

| Item | Decision |
|------|----------|
| Target State | **A** + narrow snapshot exception |
| Full State B panel pull | **CLOSED** |
| Point snapshots TOP500/AI/quantum | **ALLOWED** (CSV + ledger; exploratory) |
| H1–H6 | Archived / not tested |
| Methods 1–5, 9, 12, 18 | **Core report** |
| Methods 8, 11, 13 | **Removed** |
| M1 (14) | Appendix only |
| Radar F11 | Not in report |
| Notebooks | `notebooks/01` … `05` on branch `report-20pp` |

*Конец APPROVED_METHOD_SET.md.*

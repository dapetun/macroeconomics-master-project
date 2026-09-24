# APPROVED METHOD SET

**Дата утверждения:** 2026-09-20; **refresh:** 2026-09-22 (абсолюты + snapshot + radar)  
**Статус:** **APPROVED** (решения автора по плану Cover original theme)  
**Target State:** A — честная измеримая карта + тонкие tech-snapshots  
**Авторитет чисел:** `data_reviewed/tables_reviewed/*` (Level 1 + absolutes); `data/raw/snapshots/*` (exploratory); `regression_results_final.csv` (M1 appendix only)

---

```text
APPROVED METHODS

Core:
- Joint-year snapshot + ratios (год на каждой цифре; запрет ratio с NaN-стороной)
- Common-window CAGR с явными (start, end, n); для articles — ОБА окна 2010–2021 и 2010–2023 + пик USA 2021
- Dual-scale table: intensity vs volume/share + АБСОЛЮТНЫЙ GERD PPP и headcount researchers
- TCI occupancy 8×4: measured / snapshot / ? / qual — НЕ индекс-тест H1
- Графики F1–F7 + FIXED F8/F9; нейтральные заголовки
- Паутинная (radar) min–max по измеримым MACRO-блокам (8 стран панели; не 4 tech; не capability index)
- Semis: HS8542 + semi_status + ≠fab; TWN = qual hole
- Allow-list языка; карта ограничений данных как часть ответа
- Статьи crossover: 2016–2017 (не «~2020»)

Optional (не в докладе / не ответ на RQ):
- M1 TWFE: appendix only; cluster CI для GERD включает 0
- PCA repair (a) intensity-only: appendix only; M2 не запускать
- Naive OLS slopes без p как теста
- Within-country correlations — дескриптивно
- Fragility table M1 — as-is

Narrow snapshot exception (НЕ reopen State B full panel):
- TOP500: 1–2 момента времени (systems count; optional Rmax sum) → status snapshot
- Stanford AI Index: 2–3 числа (pubs / private $ / notable models) → snapshot
- EPO–OECD quantum: 1–2 числа (IPF; optional pubs) → snapshot
- Каждая строка CSV: country, year, indicator, value, unit, source, page/figure

Not approved:
- Старый PCA/M2/F10 как evidence
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

> Как по сопоставимым показателям 2010–2023 годов различаются пути США и Китая вдоль цепочки «наука → кадры → исследования → финансирование → инновации → коммерциализация → производство → масштабирование → внедрение → экспорт → экономический эффект» — и что из этой цепочки для искусственного интеллекта, полупроводников, суперкомпьютеров и квантовых технологий можно показать только снимком или качественно?

Технические окна данных — в `DATA_CANON.md` / `RQ_FREEZE.md` (спецификация, не обложка).

**Не отвечаем:** causal H1–H6 tests; overall winner; fab-лидерство из trade.

---

## Две descriptive hypotheses (D1, D2)

Вердикты SUPPORTED/PARTIAL/REJECTED **запрещены**.

### D1 — Intensity vs volume

Как в `RQ_FREEZE.md`: противоположные знаки intensity vs volume/share при выбранных шкалах; абсолютный GERD PPP / headcount — дополнительный volume-слой (может перевернуть знак относительно intensity).

### D2 — Missingness / thin coverage

Ряды без panel = `?`; точечные внешние выписки = `snapshot` (exploratory); TWN foundry = `qual`. Не «неизмеримо в принципе».

---

## Absolute scale rules

| Indicator | Source file | Unit | Formula / note |
|-----------|-------------|------|----------------|
| `gerd_usd_ppp` | `data/raw/oecd_gerd_usd_ppp.csv` | млн USD PPP (OECD MSTI) | **Не** вычитать из / делить на WB `gerd_pct_gdp` — разные винтажи |
| `researchers_headcount_est` | panel × `pwt_pop.csv` | тыс. человек (оценка) | `researchers_per_million × pop_millions / 1000`; pop в PWT = **миллионы** |
| `pwt_hc` (optional) | `data/raw/pwt_hc.csv` | индекс HC (PWT) | Тонкое покрытие «образование»; не STEM |

---

## Radar (macro blocks only)

- Блоки: выбираются из измеримых macro (напр. GERD%, researchers/mn, articles, patents_resident, MVA%, hitech%, GDP pc, TFP).
- Нормализация: **min–max по 8 странам панели** в joint year (не USA–CN only → 0/1).
- Подпись: «иллюстрация измеримых макроблоков», **не** capability / conversion index / H1 test.
- Tech snapshots **не** входят в radar.

---

## TWFE / PCA (без изменений роли)

M1 и PCA repair (a) — **appendix only**, не в narrative arc доклада. Числа: `regression_results_final.csv`, `PCA_REPAIR_PASS.md`. M2 не запускать.

---

## Taiwan / allow-list

- TWN: qualitative hole; **NO** panel expansion; FRA ≠ foundry substitute.
- Allow-list: «ассоциировано», «условная корреляция», «дескриптивно», «неотличимо от нуля», «не измерено в этой работе», «снимок / exploratory».
- Запрещено: winner; «США превращают / Китай масштабирует» как механизм; causal verbs; leadership без measured/snapshot evidence; «неизмеримо в принципе».

---

## Scope freeze

| Item | Decision |
|------|----------|
| Target State | **A** + narrow snapshot exception |
| Full State B panel pull | **CLOSED** |
| Point snapshots TOP500/AI/quantum | **ALLOWED** (CSV + ledger; exploratory) |
| H1–H6 | Archived / not tested |
| M1 / PCA | Appendix; не доклад |
| Radar | Core illustration (macro only) |
| 4 tech | One occupancy matrix + thin cards |

*Конец APPROVED_METHOD_SET.md.*

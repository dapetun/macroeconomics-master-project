# Research Design Blueprint

> Учебное исследование: «Путь развития США vs Китай — технологическое соперничество от фундаментальной науки до внедрения»  
> Технологии-кейсы: AI, полупроводники, суперкомпьютеры, квантовые технологии  
> Горизонт: ~4 недели, преимущественно выходные

> **SUPERSEDED / ARCHIVE (2026-09-20, ResearchDesignAgent).**  
> §A (полный causal RQ) и §B–C (H1–H6) — **design history**, не обложка и не текущий hypothesis layer.  
> Актуальные: Frozen RQ + D1–D2 → `RQ_FREEZE.md`; методы → `APPROVED_METHOD_SET.md`; таблица → `reports/hypothesis_table.md`.  
> H1–H6 = **archived design / not tested**; вердикты SUPPORTED/PARTIAL/REJECTED запрещены. Тело файла не переписывалось.

---

## A. Final research question

**Как различаются модели технологического развития США и Китая в превращении научно-исследовательских и производственных ресурсов в технологические результаты — и на каких этапах цепочки (science → … → productivity) эти различия наиболее устойчивы для четырёх стратегических технологий?**

Уточнение: вопрос **не** «кто сильнее», а **где и как** расходятся пути, **какие этапы** являются узкими местами, и **зависят ли** эти узкие места от зрелости технологии.

---

## B. Main hypothesis (H1)

**H1 (модель акцента):** США и Китай демонстрируют **разный профиль сильных и слабых звеньев** вдоль единой цепочки: при сопоставимых или сопоставимых по порядку величины входах (R&D, human capital) **относительное преимущество** смещается к ранним стадиям (science → innovation) в одной стране и к поздним (production → scaling → export) — в другой, но **направление и величина смещения зависят от технологии**, а не универсальны.

*Проверка:* индексный профиль по 8–10 этапам × 4 технологии; сравнение gap US–CN и стабильность паттерна между кейсами.

---

## C. Supporting hypotheses

| ID | Гипотеза | Краткая проверка |
|----|----------|------------------|
| **H2** | **Зрелость технологии определяет «узкое звено»:** для зрелых (semis) критичны production/scaling; для ранних (quantum) — science/R&D; AI и HPC — промежуточный профиль | Сравнение stage-gap между 4 кейсами; rank correlation зрелости vs доминирующего этапа |
| **H3** | **Структура финансирования связана с профилем цепочки:** доля частного VC/частного R&D коррелирует с innovation/commercialization; доля государственного/направленного — с production/scaling (в выборке 8–10 стран) | Cross-country regression: finance mix → stage outputs |
| **H4** | **Различие US–CN частично в «конверсии», а не только во «входах»:** при контроле R&D и HC разрыв в patents/publications меньше, чем в manufacturing capacity / export share | Ratio-анализ: output/input по этапам |
| **H5** | **Export и market share зрелых технологий сильнее предсказываются production/scaling-индикаторами, чем science-индикаторами** | Regression с lags; сравнение R² моделей «science-only» vs «production-only» |
| **H6** | **Innovation–commercialization gap** (patents/publications vs revenue/capacity/adoption) **систематически различается между странами** и **не одинаков по технологиям** | Gap-index US vs CN по каждому кейсу |

*Не более 6 гипотез; H1 — центральная, H2–H6 — supporting.*

---

## D. Analytical framework

### D.1. Единая схема: **TCI — Technology Chain Index**

Одна матрица для всех 4 технологий:

```
Страна c × Технология t × Этап s × Год (где есть данные)
```

**8 операционализируемых блоков цепочки** (объединение смежных этапов из полной цепочки):

| Блок | Этапы цепочки | Смысл |
|------|---------------|-------|
| S | science | фундаментальная база |
| HC | human capital | кадры |
| RD | R&D | ресурсы исследований |
| FIN | finance | структура финансирования |
| INN | innovation | патенты, публикации, прорывы |
| COM | commercialization | стартапы, лицензии, revenue (где есть) |
| PRD | production + scaling | мощности, выпуск, TOP500, fab capacity |
| ADE | adoption + export | внедрение, trade, market share |

*Productivity — отдельно: только качественно + 1–2 макро-прокси (см. раздел E).*

### D.2. Три слоя анализа (один framework, три уровня)

1. **Descriptive gap layer:** US vs CN — абсолютные значения, ratios, gaps по блокам S…ADE для каждого t.
2. **Conversion layer:** output/input ratios между соседними блоками (напр. INN/RD, PRD/INN, ADE/PRD) — «эффективность перехода».
3. **Cross-country pattern layer:** 8–10 стран — проверка H3, H5 (ассоциативные связи, не causal claims).

### D.3. Роль технологий-кейсов (не 4 отдельных исследования)

| Кейс | Роль в framework | «Stress test» |
|------|------------------|---------------|
| **Полупроводники** | зрелая, capital-intensive, глобальная цепочка | production/scaling vs science |
| **AI** | быстрые циклы, dual public-private | innovation/commercialization vs adoption |
| **Суперкомпьюters** | state-led, dual-use, measurable (TOP500) | finance + PRD vs COM |
| **Квант** | ранняя стадия, science-heavy | science/R&D bottleneck |

**Вывод по кейсу** → вклад в общий паттерн H1/H2, а не отдельный вердикт «US vs CN в AI».

### D.4. Набор стран

| Уровень | Страны | Зачем |
|---------|--------|-------|
| **Ядро** | USA, China | главное сравнение, time series 2010–2023 |
| **Комparators (6–8)** | Taiwan, South Korea, Japan, Germany, UK, Israel, (+ EU aggregate или France) | cross-country regressions; контекст «не бинарного» мира |
| **Не включать** | >15 стран | избыточно для срока |

*Две страны недостаточны для panel FE по US–CN alone — comparators обязательны для H3, H5.*

---

## E. Core indicators (10–15)

### Обязательный минимум (15 показателей)

| # | Индикатор | Блок | Источник (типовой) | US/CN/Both |
|---|-----------|------|-------------------|------------|
| 1 | GERD (% GDP) | RD | OECD MSTI / World Bank | Both + comparators |
| 2 | Government R&D (% GDP) | RD/FIN | OECD, NSF, NBS China | Both |
| 3 | Researchers per million | HC | UNESCO / OECD | Both |
| 4 | STEM graduates (или tertiary STEM share) | HC | UNESCO / national | Both |
| 5 | Field-specific publications (top quartile) | S/INN | Scopus/WoS aggregates, OECD | Both, по 4 полям |
| 6 | Field-specific patents (triadic или USPTO/EPO family) | INN | WIPO, USPTO | Both |
| 7 | VC investment in sector (где доступно) | FIN/COM | PitchBook/CB Insights proxies; для CN — частично qualitative | US + partial CN |
| 8 | Semiconductor: manufacturing capacity / share advanced nodes | PRD | SEMI, industry reports | Both + TW/KR |
| 9 | Semiconductor: export value / import dependency | ADE | UN Comtrade, USITC | Both |
| 10 | AI: compute capacity proxy (TOP500 + cloud — осторожно) | PRD | TOP500, partial | Both |
| 11 | TOP500 supercomputer count & aggregate performance (Rmax) | PRD | TOP500.org | Both |
| 12 | Quantum: publication/patent counts + public funding | S/RD | Scopus, WIPO, national programs | Both |
| 13 | High-tech exports (% manufactured exports) | ADE | World Bank / OECD STAN | Both + comparators |
| 14 | TFP growth or high-tech sector VA growth (1 макро-прокси) | productivity | Penn World Table / national stats | Quali-quant |
| 15 | Finance mix: private vs public R&D share | FIN | OECD | Both + comparators |

### Технология-специфичные (внутри тех же блоков, не новые «оси»)

- **AI:** AI patent share, AI-related VC (US), adoption proxy (e.g. AI hiring / GitHub — только если быстро доступно).
- **Semis:** fab count, lithography dependency (qualitative + 1–2 числа).
- **HPC:** TOP500 — уже #11.
- **Quantum:** qubit milestones — **qualitative timeline**, не количественный ряд.

---

## F. Econometric strategy

**Принцип:** 2–3 метода, объяснимых на защите; без IV / synthetic control / causal ML.

### F1. Index construction + gap decomposition (обязательно)

- Нормализация показателей (min-max или z-score внутри блока).
- TCI profile per (country, technology).
- US–CN gap и conversion ratios — основа для H1, H2, H4, H6.

### F2. Pooled OLS / random-effects panel (8–10 стран, 2010–2022)

```
ExportShare_or_Production_it = β0 + β1·Science_it + β2·Production_it + β3·FinanceMix_it
                               + γ·Tech_dummies + δ·Year_FE + ε_it
```

- Цель: H3, H5 — **ассоциации**, не causality.
- Robust SE; log-log где уместно.
- Честно: endogeneity, малая N → «exploratory cross-country evidence».

### F3. Country-pair trend comparison (US vs CN, 2010–2023)

- OLS на временных рядах ключевых индикаторов: `Y_t = α + β·t + ε_t` для US и CN отдельно.
- Сравнение slopes (convergence/divergence) — для 5–6 core indicators.
- Простой Chow test или dummy interaction `t × US` в pooled 2-country series.

**Не использовать:** IV, DiD без чёткого shock, synthetic control, VAR с 2 странами.

---

## G. Optional ML (максимум 1–2)

**ML не обязателен.** Добавлять только если улучшает наглядность.

| Метод | Зачем | Ограничение |
|-------|-------|-------------|
| **K-means clustering** (k=3–4) | группировка стран по TCI-профилю; визуализация «типов моделей» | интерпретация > prediction |
| **Elastic Net / Lasso** (опционально) | отбор из 10–15 predictors для export/production в cross-country sample | только если OLS нестабилен; report coefficients, не «black box» |

**Не использовать:** deep learning, causal ML, NLP на полных corpora, forecasting.

---

## H. Technology-case logic

```
                    ┌─────────────────────────────────────┐
                    │     Unified TCI Framework (S→ADE)    │
                    └─────────────────────────────────────┘
                                      │
        ┌──────────────┬──────────────┼──────────────┬──────────────┐
        ▼              ▼              ▼              ▼              │
   Semiconductors      AI          Supercomputers   Quantum          │
   (mature PRD)   (fast INN/COM)  (state PRD)    (early S/RD)       │
        │              │              │              │              │
        └──────────────┴──────────────┴──────────────┴──────────────┘
                                      │
                         Synthesis: H1 + H2 pattern
                         «Где US/CN расходятся и почему
                          (механизмы — qualitatively)»
```

**Порядок работы следующего агента:**

1. Собрать 15 core indicators для US, CN, comparators.
2. Построить TCI matrices (4 tech × 2 core countries).
3. Gap + conversion analysis → H1, H4, H6.
4. Cross-country regression → H3, H5.
5. Qualitative layer для COM, части FIN, productivity.
6. Синтез: **technology-dependent divergence**, не overall winner.

---

## I. Main risks and limitations

| Риск | М mitigation |
|------|----------------|
| Данные CN неполны / несопоставимы | triangulation; ranges; OECD+official; явно маркировать uncertainty |
| 2 страны → слабая inference | comparators для regressions; US–CN = descriptive + trends |
| 4 tech × много этапов → перегруз | жёсткий лимит 15 indicators; 8 блоков, не 11 отдельных |
| Patents ≠ innovation | использовать publications + patents; qualitatively discuss |
| Causal language | только associative; policy shocks — narrative, не DiD |
| Commercialization data scarce | qualitative case snippets (1–2 страницы суммарно) |
| AI/quantum hype | focus on measurable proxies; avoid firm-level deep dive |

---

## J. Что сознательно НЕ исследуем

- Полноценная оценка **total factor productivity** по секторам с decomposition.
- **Firm-level** microeconometrics (Apple, TSMC, Huawei и т.д.) — только иллюстративные примеры.
- **Causal impact** CHIPS Act, export controls, Made in China 2025.
- **Military/security** dimension beyond brief qual note for HPC/semis.
- **Detailed supply chain** graph (upstream equipment, rare earths).
- **Culture/institutions index** как отдельная большая глава.
- **Exhaustive literature review** — только 5–10 ключевых источников.
- **Real-time 2024–2025 frontier** (e.g. latest LLM leaderboard) — snapshot, не динамика.
- **4 отдельных отчёта** по технологиям.
- **Winner declaration** USA vs China.

---

## Quantitative vs Qualitative — сводка

| Можно количественно (core) | Преимущественно качественно |
|-----------------------------|----------------------------|
| S, HC, RD (aggregates) | Mechanisms industrial policy |
| INN (patents, publications) | Commercialization pathways |
| PRD semis/HPC (capacity, TOP500) | Technology transfer, espionage debate |
| ADE (trade, high-tech export share) | Geopolitical decoupling effects |
| FIN mix (partial) | VC/IPO pipeline details CN |
| Gap/conversion indices | Productivity attribution to tech |
| Cross-country associations | Adoption at user/firm level |
| Trend slopes US vs CN | Quantum «breakthrough» claims |

---

## Спорные исходные тезисы (требуют проверки, не принимать как факт)

1. **«Китай = manufacturing/scaling, США = science/innovation»** — проверить H1/H4; может не hold для AI publications или quantum funding.
2. **«Государственная модель эффективна для догоняющего scaling»** — partial support only for mature tech; test via PRD vs FIN.
3. **«Decoupling критично бьёт по CN semis»** — qual + trade/capacity trends; не causal.
4. **«AI — особый кейс: data/adoption advantage CN»** — data often proprietary; verify only measurable proxies.
5. **«Квант — чисто американское лидерство»** — likely early-stage noise; compare publication/funding, not media claims.
6. **«Human capital: CN quantity, US quality»** — HC indicators mostly quantity; quality — qualitative with citation/top-paper share as partial quant.
7. **«Патенты = инновационное лидерство»** — explicit critique in design.

---

## Blueprint для следующего агента

### Phase 0 — Setup (½ дня)
- [ ] Создать структуру `data/raw`, `data/processed`, `notebooks/` или `src/analysis/`
- [ ] Зафиксировать список 15 indicators + источники в `indicators.yaml` или таблице
- [ ] Определить comparators: TW, KR, JP, DE, UK, IL (+ EU или FR)

### Phase 1 — Data collection (2–3 выходных дня)
- [ ] Скачать OECD MSTI, World Bank, UN Comtrade, TOP500, WIPO patent aggregates
- [ ] US: NSF; CN: NBS / MIIT where available
- [ ] Field-specific publication counts (4 fields) — один согласованный источник
- [ ] Не собирать лишнее; пропуски документировать

### Phase 2 — TCI construction (1 выходной день)
- [ ] Нормализация → block scores → technology profiles
- [ ] US–CN gap tables + conversion ratios
- [ ] Figures: radar/bar charts по 4 tech

### Phase 3 — Econometrics (1 выходной день)
- [ ] Pooled OLS: H3, H5 (8–10 countries)
- [ ] Trend OLS: US vs CN slopes, 5–6 key series
- [ ] Таблицы с robust SE; без causal language

### Phase 4 — Qualitative layer (1 выходной день)
- [ ] 2–3 страницы: COM, productivity, policy mechanisms per weak data stages
- [ ] Спорные тезисы — явно «supported / partial / not supported / insufficient data»

### Phase 5 — Synthesis (½ дня)
- [ ] Ответ на final RQ
- [ ] H1–H6: verdict table
- [ ] Limitations paragraph
- [ ] **Не** объявлять overall winner

### Deliverables
- `research_design.md` (этот файл)
- `data/processed/tci_scores.csv`
- `figures/` — 4–6 графиков
- `analysis/` — скрипты воспроизводимости
- Draft report outline (не полный литературный текст)

### Decision rules
- Если indicator недоступен >2 недели работы → заменить ближайшим proxy из таблицы E.
- Если regression unstable (N<8) → report descriptive + correlation only.
- ML только если Phase 3 завершена досрочно.

---

*Version: 1.0 | Agent: research-design | Date: 2026-09-12*

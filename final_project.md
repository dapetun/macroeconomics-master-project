# Final Project — США vs Китай: от науки до внедрения (макроцепочка + тонкие tech-снимки)

**Тема обложки:** Путь развития США vs путь развития Китая: технологическое соперничество от фундаментальной науки до внедрения.

**Дата синтеза:** 2026-09-22 (Cover original theme pass).  
**Статус:** единый тезис State A + narrow snapshots (exploratory).

**Приоритет при расхождении:**  
`RQ_FREEZE.md` / `APPROVED_METHOD_SET.md` / `DATA_CANON.md` / `SNAPSHOT_SOURCE_LEDGER.md` > этот файл > `dual_scale_with_absolutes.csv` / `tech_occupancy_matrix.md` > `regression_results_final.csv` (только appendix M1).

**DO NOT CITE как authority:** `remaining_risks.md`, `reports/final_synthesis.md`, `reports/tech_cases_comparison.md`, `reports/analysis_report.md`, `technology_cases_final.md`.

**Панель:** USA, CHN + KOR, JPN, DEU, GBR, ISR, **FRA** (не TWN).  
**Allow-list:** «ассоциировано», «условная корреляция», «дескриптивно», «неотличимо от нуля», «не измерено в этой работе», «снимок / exploratory».  
**Запрещено:** overall winner; «США превращают / Китай масштабирует» как механизм; causal org→conversion→TFP; fab из trade; «неизмеримо в принципе».

---

## 0. Narrative arc (доклад 10–12 мин)

| Шаг | Содержание | Где |
|-----|------------|-----|
| 1 | Covering RQ + тема | §1 |
| 2 | D1 dual-scale + **абсолюты** (GERD PPP, headcount) | §2, §5 |
| 3 | Паутина макроблоков (иллюстрация) | §5.4 |
| 4 | Четыре технологии: occupancy + тонкие снимки | §6 |
| 5 | Semis ≠ fab; TWN hole | §6.2–6.3 |
| 6 | Механизмы NOT IDENTIFIED; no winner | §7, §10 |
| — | M1/PCA только если спросят | Прил. A–B |

---

## 1. Research question

### 1.1. Covering RQ (обложка)

> Как по сопоставимым показателям 2010–2023 годов различаются пути США и Китая вдоль цепочки «наука → кадры → исследования → финансирование → инновации → коммерциализация → производство → масштабирование → внедрение → экспорт → экономический эффект» — и что из этой цепочки для искусственного интеллекта, полупроводников, суперкомпьютеров и квантовых технологий можно показать только снимком или качественно?

### 1.2. Технические окна (не обложка)

GERD/BERD/статьи/GDP/TFP 2010–2023; researchers joint 2022 / common 2010–2017; патенты 2010–2021; MVA joint 2021 / common 2010–2021; hitech 2010–2023; HS8542 с разрывами; абсолютный GERD PPP joint **2024**; headcount researchers joint **2022**. Каждая цифра — с явным годом.

### 1.3. Не отвечаем

H1–H6 как preregistered тесты; каузальный механизм конверсии; overall winner; fab-лидерство из trade; tech→TFP attribution.

Исходный causal RQ из `research_design.md` §A — **архив design history**.

---

## 2. Hypotheses: D1–D2 + архив H1–H6

Вердикты SUPPORTED / PARTIAL / REJECTED **запрещены**.

### 2.1. D1 — Intensity vs volume

При выбранных шкалах: intensity-входы (GERD%, BERD PERFORMED%, researchers/mn) → США выше; volume/share (статьи, патенты парой, MVA%, hitech%, HS8542) → Китай выше. Это **арифметика шкал**, не две модели организации.

**Абсолютный слой (дополнение):** GERD в млн USD PPP (**2024**) и оценка численности исследователей (**2022**) — Китай выше по объёму. Это не опровергает D1 intensity, а показывает другой знаменатель. Таблица: `dual_scale_with_absolutes.csv`.

### 2.2. D2 — Missingness / thin coverage

Без сопоставимого **ряда**: FIN-mix, COM (кроме тонкого AI snapshot), fab/node, TWN foundry quant. AI/HPC/quantum имеют **`snapshot`** (exploratory), не `measured`. Отсутствие ряда = ограничение **этой** работы, не «неизмеримо в мире».

### 2.3. H1–H6

**Archived design / not tested.** Снимки не повышают их до SUPPORTED.

---

## 3. Methodology

**Core:** joint-year; common-window CAGR (статьи — оба окна); dual-scale + абсолюты; occupancy `measured`/`snapshot`/`qual`/`?`; F1–F7 + FIXED F8/F9; **F11 radar** (macro min–max по 8 странам); **F12** абсолютный GERD; allow-list.

**Не в докладе:** M1 TWFE; PCA (даже repair).  
**Not approved:** conversion ratios; pooled corr inference; DiD/IV/ML; TWN panel; winner.

---

## 4. Data (краткий канон)

| Правило | Деталь |
|---------|--------|
| Articles CAGR | Оба окна 2010–2021 и 2010–2023; пик USA 2021 |
| Articles crossover | **2016** последний USA>CHN; **2017** первый CHN>USA — не «~2020» |
| BERD | PERFORMED % GDP; ≠ finance mix |
| Patents | Пара resident + total-office |
| Absolutes | OECD GERD PPP ≠ WB GERD%; headcount = res/mn × PWT pop (млн) / 1000 |
| Snapshots | `data/raw/snapshots/*` + `SNAPSHOT_SOURCE_LEDGER.md` |

---

## 5. Quantitative findings

### 5.0. Dual-scale + абсолюты (центральный D1)

Источник: `dual_scale_intensity_volume.csv` + `dual_scale_with_absolutes.csv`.

| Метрика | Шкала | Year | USA | CHN | Знак |
|---------|-------|------|-----|-----|------|
| GERD % GDP | intensity | 2023 | 3.45 | 2.58 | USA↑ |
| BERD PERFORMED % | intensity | 2023 | 2.66 | 2.00 | USA↑ |
| Researchers / mn | intensity | 2022 | 4937 | 1849 | USA↑ |
| **GERD USD PPP (млн)** | **volume abs.** | **2024** | **1 009 275** | **1 028 344** | **CHN↑** (~1.02×) |
| **Researchers headcount est. (тыс.)** | **volume abs.** | **2022** | **~1 686** | **~2 635** | **CHN↑** (~1.56×) |
| Articles | volume | 2023 | 430 843 | 932 712 | CHN↑ |
| Patents resident / total office | volume | 2021 | 262k / 591k | 1 427k / 1 586k | CHN↑ (5.44× / 2.68×) |
| MVA % GDP | share | 2021 | 10.53 | 26.62 | CHN↑ |
| Hitech export % | share | 2023 | 21.85 | 26.57 | CHN↑ |
| HS8542 exports | volume nom. | 2023 | $43.6 bn | $136.4 bn | CHN↑ (≠fab) |
| PWT HC (optional) | index | 2023 | 3.83 | 2.75 | USA↑ |

**Articles dual-window CAGR:** 2010–2021 USA 1.33% / CHN 8.51%; 2010–2023 USA 0.43% / CHN 8.90%.  
**GERD PPP CAGR 2010–2024:** USA ~6.7%/yr; CHN ~11.9%/yr (объём догоняет/обгоняет при более низкой intensity).

**Чтение:** противоположные знаки intensity vs counts/shares = выбранные шкалы. Абсолютный GERD/кадры показывают, что «США выше по R&D» верно для **доли ВВП**, но не для **объёма PPP** в 2024.

### 5.1. Темпы (кратко)

GERD% 2010–2023: USA 1.86%/yr vs CHN 3.33%/yr. MVA-доли **обе** падают. GDP pc: абсолютный разрыв вырос. TFP CHN 0.40→0.47 при USA=1 by construction.

### 5.2. M1 / PCA — не в основной линии

См. Приложения A–B. В докладе не показывать.

### 5.3. Графики

F1–F7; FIXED F8/F9; **F11** radar; **F12** абсолютный GERD. Старый F10 DO NOT USE.

### 5.4. Radar (иллюстрация)

`F11_radar_macro_blocks.png`: min–max по 8 странам для GERD%, researchers/mn, log articles, log patents, MVA%, hitech%, log GDP pc, TFP. **Не** capability index и не тест H1. Таблица: `radar_macro_blocks_minmax.csv`.

---

## 6. Technology layer

Occupancy: `tech_occupancy_matrix.md` — **1 measured / 9 snapshot / 1 qual / 21 ?**.  
Карточки: `tech_framework_unified.md` §7.

### 6.1. AI (snapshot, exploratory)

| Показатель | USA | CHN | Year | Источник |
|------------|-----|-----|------|----------|
| Доля AI-публикаций (CS) | 9.2% | 23.2% | 2023 | AI Index Fig 1.1.6 |
| Доля AI-цитат | 13.0% | 22.6% | 2023 | Fig 1.1.7 |
| Private AI investment | $109.1 bn | $9.3 bn | 2024 | Economy / highlight |
| Notable models | 40 | 15 | 2024 | Fig 1.3.1 |
| AI patent grants share | 14.2% | 69.7% | 2023 | Fig 1.2.3 |

Volume/share Китай↑ на pubs/patents; private $ и notable models — США↑. **Не** finance-mix GERD; **не** adoption в отраслях; **не** TFP.

### 6.2. Semiconductors

Measured ADE: HS8542 2023 USA $43.6 bn vs CHN $136.4 bn; ≠ fab; H6 vs H3; quarantine 2015–17.  
PRD: `qual` TWN hole; FRA ≠ foundry substitute. CHIPS/BIS = markers only.

### 6.3. HPC (snapshot)

TOP500 systems: Nov **2015** USA 199 / CHN 109; Nov **2025** USA 171 / CHN 40 (Japan 43, Germany 40).  
**Явно:** Linpack list ≠ cloud AI training compute.

### 6.4. Quantum (snapshot)

IPF 2005–2024: USA **3330**, CHN **947** (EPO-OECD Fig 3.3.1B); Китай выше по national-only families. US IPF share 41%→31% (E4). Funding ~60% to US firms (E6). COM / макроэффект **не измерены**.

---

## 7. Mechanisms: NOT IDENTIFIED

| Кандидат | Статус |
|----------|--------|
| Организация → конверсия | NOT IDENTIFIED |
| Finance mix → outputs | NOT IDENTIFIED (BERD=PERFORMED; AI private $ ≠ mix) |
| GERD → TFP causal | NOT IDENTIFIED (M1 appendix; cluster CI∋0) |
| Tech domain → TFP/GDP | NOT IDENTIFIED |
| Trade → fab leadership | NOT IDENTIFIED |

Измеримо: где расходятся уровни/тренды/снимки. Не измеримо: насколько одно звено **вызывает** другое.

---

## 8. Comparative map (не stage winners)

| Stage | Измеримое / снимок | Caveat |
|-------|-------------------|--------|
| S | Articles CHN↑; AI pubs share CHN↑; quantum IPF USA↑ | Volume ≠ impact |
| HC | Res/mn USA↑; headcount est. CHN↑; PWT HC USA↑ | Разные шкалы |
| RD | GERD% USA↑; GERD PPP 2024 CHN↑ слегка | Intensity vs volume |
| FIN | `?` mix; AI private $ USA↑ snapshot | Не H3 |
| INN | Patents CHN↑; AI patents share CHN↑; quantum IPF USA↑ | Counts |
| COM | Notable models USA↑ thin; else `?` | Не внедрение |
| PRD | MVA% CHN↑; TOP500 USA↑; fab `qual`/`?` | Share ≠ fab |
| ADE | Hitech% / HS8542 CHN↑ | Trade ≠ fab |
| Productivity | TFP / GDP pc USA↑ | Macro; not tech-TFP |

**Overall winner: не объявляется.**

---

## 9. Limitations

- Snapshots exploratory; не полные ряды.
- AI Index / TOP500 / EPO-OECD — внешние определения; CN private $ слабость.
- Semis trade ≠ fab; без TWN misspecification.
- USA TFP=1 construction; M1 fragile.
- Архивные файлы ядовиты — не открывать на защите.

---

## 10. Conclusion

**Ответ на covering RQ:** вдоль измеримой макроцепочки при выбранных шкалах США выше по **intensity** входов, Китай — по **объёмам/долям** поздних блоков (D1); абсолютный GERD PPP и численность исследователей показывают обратный знак по **объёму**. По четырём технологиям: semis — trade + TWN hole; AI/HPC/quantum — тонкие снимки (публикации/инвестиции/модели; TOP500; quantum IPF), без полного ряда и без winner. Механизмы **NOT IDENTIFIED**.

**Слайдовый каркас:** вопрос → dual-scale+абсолюты → F11/F12 → occupancy 4 tech → что не утверждаем.

---

## Приложение A. M1 (только если спросят)

β_GERDlag1=0.02746; cluster p≈0.409; n=84; G=7. Ассоциация, не эффект, не ответ на RQ. `M1_INTERPRETATION.md`.

## Приложение B. PCA

Repair (a) intensity-only — appendix only; старый F10/M2 DO NOT USE. Не показывать в докладе.

## Приложение G. Геополитика

Не findings. BIS/CHIPS/MiC = markers. EUV/foundry доли не в панели.

## Приложение H. Defense slide outline (10–12 мин)

1. Тема + covering RQ  
2. Данные / окна / allow-list  
3. Таблица dual-scale + абсолюты (1 слайд)  
4. F1 или F12 + F3 (статьи; crossover 2016–17)  
5. F11 radar (подпись: иллюстрация)  
6. Occupancy 8×4 + 4 snapshot bullets  
7. Semis: HS8542 ≠ fab; TWN  
8. Вывод: no winner; mechanisms not identified; что дальше не делать  

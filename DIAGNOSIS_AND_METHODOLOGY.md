# DIAGNOSIS AND METHODOLOGY

**Дата:** 2026-09-20  
**Роль:** diagnostic worker (диагностика + варианты методов; **не** утверждение Approved Method Set)  
**Статус документа:** предложение для решения автора. Ни один метод ниже не считается утверждённым.  
**Критерий:** максимум исследовательской ценности на единицу сложности; учебная магистерская работа, не journal article.

> **PROPOSAL ONLY / SUPERSEDED for approval (2026-09-20, ResearchDesignAgent watermark).**  
> Этот файл = диагностическое предложение. **Утверждение методов — только** `APPROVED_METHOD_SET.md`.  
> Working causal RQ в §1 («организация → конверсия…») — **не обложка**. Frozen RQ + D1–D2: `RQ_FREEZE.md`.  
> H1–H6 = archived design / not tested (`reports/hypothesis_table.md`). Тело файла не переписывалось.

Типы утверждений помечены: **[observation]** / **[idea]** / **[assumption]** / **[prediction]** / **[located evidence]** / **[decision pending]**.

---

## 1. Scope and safety / educational boundary

| Поле | Содержание |
|------|------------|
| Владелец решения | Даниил (автор); агент не утверждает методы |
| Назначение | учебное исследование магистратуры |
| Тема (working) | «Путь развития США vs путь развития Китая: технологическое соперничество от фундаментальной науки до внедрения» |
| RQ (working) | как различия в организации технологического развития США и Китая влияют на способность конвертировать S&T-ресурсы в промышленное производство, масштабирование технологий и экономические преимущества |
| 4 домена | AI, полупроводники, HPC/суперкомпьютеры, quantum — **в одном framework**, не четыре эссе |
| Не входит | IV, synthetic control, GMM, SEM, Bayesian, VAR/VECM, causal ML/DL, XGBoost/RF «для вида», сложные сети/NLP; объявление winner; novelty-claims по bounded search; фабрикация цитат/данных |
| Dual-use | описания режимов контроля (BIS/CHIPS) — только как **даты-маркеры**, без operational detail |
| Литература | в этом проходе **не** делался academic literature search. Поиск skills: см. §17. Формула: «not located within search boundary», не «never studied» |

**[decision pending]** Заморозить один RQ (узкий измеримый *или* широкий + минимальный добор tech-рядов). Держать оба сразу — путь к переутверждению.

---

## 2. Frozen observation (что проект **фактически** содержит)

**[observation]** Зафиксировано до интерпретации. Источники: файлы на диске, 2026-09-20.

### 2.1. Артефакты

| Класс | Что есть | Путь |
|-------|----------|------|
| Карта | `PROJECT_STATE.md` (2026-09-20) | корень |
| Дизайн | RQ, H1–H6, TCI 8 блоков, запрет IV/DiD | `research_design.md` |
| Карта данных | план 12 core + tech modules | `data_map.md` |
| Финальный синтез | после adversarial review | `final_project.md` (2026-09-16) |
| Логика | сужение RQ; H not tested | `research_logic_final.md` |
| Панель macro | 8×25 = 200 строк, 2000–2024 | `data/processed/core_panel.csv` = значения `data_reviewed/core_panel_reviewed.csv` (maxabs=0 на shared cols) |
| Tech-панель | 200 строк; semi 75 non-null; AI/HPC/quantum = 0 | `data/processed/tech_panel.csv`, `data_reviewed/tech_panel_reviewed.csv` |
| Числа M1 | LSDV FE + HC1 + cluster | `regression_results_final.csv` |
| Дескриптивы | joint-year + common-window CAGR | `data_reviewed/tables_reviewed/*.csv` |
| Код анализа | descriptives + 2 FE + PCA, без statsmodels | `scripts/analysis_agent4.py` |
| Графики | F1–F10 originals; F8/F9 FIXED | `figures/*.png` (10 файлов); `data_reviewed/figures_reviewed/*_FIXED.png` (2) |
| Кейсы | AI/semis/HPC/quantum writeups | `technology_cases_final.md`; актуальные вердикты — `final_project.md` §6 |
| Гипотезы | таблица синхронизирована | `reports/hypothesis_table.md` (2026-09-19) |
| Презентация / PDF / pptx | **NOT FOUND** | — |
| `tci_scores.csv` | **ABSENT** | — |
| Обзор литературы (глава) | **NOT FOUND** | design §J: «только 5–10 ключевых источников», не exhaustive |

**Страны в панели [located evidence]:** USA, CHN, KOR, JPN, DEU, GBR, ISR, **FRA**. **TWN нет.**

**Скрипты:** 17 в `scripts/` + `notebooks/01_collect_core_data.py`. Много probe/download-черновиков OECD/PWT.

### 2.2. Измеримые ряды (core)

**[located evidence]** Joint-year snapshot `descriptive_snapshot_latest_joint.csv`:

| Блок | Var | Joint-year | USA | CHN | Ratio CHN/USA |
|------|-----|------------|-----|-----|---------------|
| RD | GERD % GDP | 2023 | 3.45 | 2.58 | 0.75 |
| FIN/RD | BERD PERFORMED % GDP | 2023 | 2.66 | 2.00 | 0.75 |
| HC | researchers / млн | 2022 | 4937 | 1849 | 0.375 |
| S | articles volume | 2023 | 430843 | 932712 | 2.17 |
| INN | patents resident (office) | 2021 | 262244 | 1426644 | 5.44 |
| INN | patents total office | 2021 | 591473 | 1585663 | 2.68 |
| PRD | MVA % GDP | 2021 | 10.53 | 26.62 | 2.53 |
| ADE | hitech export share | 2023 | 21.85 | 26.57 | 1.22 |
| ADE | HS8542 USD | 2023 | 43.6 bn | 136.4 bn | 3.13 |
| Prod. | GDP pc PPP | 2023 | 74352 | 22687 | 0.305 |
| Prod. | TFP ctfp | 2023 | 1.0 (construction) | 0.471 | 0.47 |

**Пустые блоки:** COM (нет колонки); FIN-mix (BERD ≠ financed); AI/HPC/quantum 100% NaN; GVC/VC/labor productivity не собраны; STEM и field-pubs сознательно убраны в `data_map.md`.

### 2.3. Что посчитано количественно

**[observation]** В `scripts/analysis_agent4.py` и `results/`:

1. Snapshot уровней (старый `results/descriptive_snapshot_US_CHN.csv` — смешанные годы; **не авторитет**).
2. CAGR на фактических окнах страны (**несравнимо** между странами для researchers).
3. Naive OLS slopes `Y = a + b(t−2010)` + interaction DIFF.
4. Conversion ratios counts÷intensities — **EXCLUDED**.
5. Pooled Pearson — **DO NOT USE for inference**.
6. M1: `TFP ~ GERD_lag1 + log(researchers)` + country FE + year FE, n=84, G=7.
7. PCA 4 vars → TechPC1 (loadings: articles **−0.36**) + M2 TFP~PC1, γ=−0.118 — **EXCLUDED**.
8. Event means 2020–21 vs 2022–23, n=2/ячейка.

**[observation]** H1–H6: ни одна не протестирована как preregistered. Вердикты SUPPORTED/PARTIAL/REJECTED **не ставятся**.

---

## 3. PROJECT_STATE.md vs reality

Карта в целом **согласована** с диском по панелям, M1, missing tech, H-статусам, FRA vs TWN. Ниже — расхождения и подтверждения.

| # | Утверждение PROJECT_STATE | Факт на диске | Вердикт |
|---|---------------------------|---------------|---------|
| 1 | figures F1–F10 + 2 FIXED | 10 png в `figures/` + 2 FIXED; размеры >0 | **Согласовано.** (индексатор IDE png не видел; shell видит) |
| 2 | core values identical processed vs reviewed | python maxabs=0 на 11 shared cols; reviewed + `patents_total_office` | **Согласовано** |
| 3 | 200 строк, 8 стран, FRA not TWN | 200; unique ISO3 = CHN DEU FRA GBR ISR JPN KOR USA | **Согласовано** |
| 4 | AI/HPC/quantum 100% missing | tech_panel non-null: hpc/ai/quantum = 0; Stanford = Google Drive HTML, не CSV | **Согласовано** |
| 5 | semi retained 75 | `semi_exports_hs8542` non-null = 75 | **Согласовано** |
| 6 | M1 β=0.02746, p_HC1=0.059, cluster p=0.409, n=84 | `regression_results_final.csv` + `model1_tfp_gerd_hc_FE_coef.csv` | **Согласовано** |
| 7 | PCA PC1 69.9%, articles loading −0.36, M2 γ=−0.118 | `pca_variance.csv` 0.699; `pca_loadings.csv` −0.360; final csv −0.11796 | **Согласовано** |
| 8 | ISR BERD>GERD 2023 | GERD 6.346, BERD 6.504 | **Согласовано** |
| 9 | GBR researchers ends 2017 | `effective_samples`: GBR n=8, t1=2017 | **Согласовано** как факт данных |
| 10 | Articles CAGR conflict 2010–21 vs 2010–23 | **Оба окна арифметически верны** (см. ниже) | **Подтверждён нерешённый конфликт канона** |
| 11 | `remaining_risks.md` stale (77%, H1 partial) | файл 2026-09-14, §1 ещё «BERD/GERD ~77%»; §3 «H1 partially supported» | **Подтверждено** |
| 12 | `data_dictionary.csv` BERD «Business R&D»; HPC VALID | словарь: `berd` = «Business R&D expenditure»; HPC `VALID WITH CAVEAT` при 0 значений | **Подтверждено** |
| 13 | TWN в design, FRA в панели | `research_design.md` / `data_map.md`: TWN в 8; панель FRA | **Подтверждено, UNRESOLVED как формальное решение** |
| 14 | ~17 scripts + 1 notebook | 17 py в `scripts/` + 1 notebook | **Согласовано** |
| 15 | `quant_reviewed.md` «GBR ends 2019» — ошибка, канон 2017 | `quant_reviewed.md` §5 F2 всё ещё «GBR ends 2019» | **Файл не починен; PROJECT_STATE это знает** |
| 16 | cluster SE «невозможны» в remaining_risks | cluster SE **посчитаны** в `regression_results_final.csv` | **Stale remaining_risks** vs актуальный quant |
| 17 | F1 «endorsed with caveats» | код F1 title: *«China converges toward US level»* при slope diff naive p=0.29 | **Не в таблице противоречий STATE; это дефект оригинального графика** |

### 3.1. Articles CAGR — не «ошибка CSV», а выбор окна, который меняет сюжет

**[located evidence]** Пересчёт из `core_panel.csv`:

| Окно | USA CAGR | CHN CAGR | Источник текста |
|------|----------|----------|-----------------|
| 2010–2021 (n=12) | **1.33%** | **8.51%** | `final_project.md` §5.2; `quant_reviewed.md` §2 |
| 2010–2023 (n=14) | **0.43%** | **8.90%** | `descriptive_cagr_common_window.csv` |

USA articles: 2010=407406 → **2021=471378 (пик)** → 2023=430843. Окно 2010–23 прячет спад после пика. **[assumption]** Выбор 2010–21, вероятно, «выровнять с патентами», но для articles покрытие полное до 2023.

**[decision pending]** Канон: показывать **оба окна + пик 2021**, не выбирать одно число.

---

## 4. Research logic diagnosis

### 4.1. Два RQ

| | Исходный (`research_design.md` §A) | Отвечаемый (`final_project.md` §1.2) |
|--|-------------------------------------|--------------------------------------|
| Вопрос | модели конверсии + устойчивость узких мест **по 4 технологиям** | различия **уровней/трендов** измеримой macro-цепочки + какие звенья **нельзя** оценить |
| Данные | требуют 4 tech-панели + TCI | есть ~10 macro vars + semi-trade |
| Риск | неотвечаем → переутверждение | отвечаем, но **ужеже working topic** |

**[observation]** Working RQ оркестратора («как организация влияет на конверсию в производство/scaling/экономические преимущества») — **каузальный/механистический**. Панель даёт **дескриптивные ассоциации уровней**. Стрелки «организация → конверсия → TFP» **не идентифицированы** (`final_project.md` §7, §10).

### 4.2. Слишком широко?

**[idea]** Да, если целиться в полный chain × 4 tech × finance mix × conversion efficiency × causal economic effect.  
**[idea]** Нет, если честно сузить до: (i) карта измеримых US–CN gaps; (ii) явная карта **дыр**; (iii) 4 tech как qualitative stress-test **одной** матрицы TCI.

### 4.3. Сравнение слишком descriptive?

**[observation]** Да — и это **не дефект**, если descriptive объявлен целью. Дефект — оставлять H1–H6 как будто их ещё «дотестируют» сложными моделями без данных.

### 4.4. Есть ли механизм technology → economic effect?

**[observation]** Нет идентифицированного механизма. M1 — условная ассоциация GERD↔агрегатный TFP, CI включает 0, USA TFP=1 by construction, G=7, лаг не обоснован. Tech-attribution запрещён самим проектом.

**Тип целевого утверждения сейчас:** descriptive (+ слабо associational для M1).  
**Тип working RQ:** causal/mechanistic.  
**Разрыв** — главная логическая проблема.

---

## 5. Data diagnosis (keep / drop / missing)

### KEEP (ядро Level 1)

| Переменная | Почему | Оговорка |
|------------|--------|----------|
| `gerd_pct_gdp` | RD-интенсивность, полное окно 2010–23 | WB≠OECD; CN GDP denom |
| `berd_pct_gdp` | **уровень** PERFORMED, бенчмарк KOR/ISR | **не** finance mix |
| `researchers_per_million` | HC intensity | ISR 0; GBR–2017; USA–2022; per-million bias |
| `scopus_articles` | S volume | ≠impact, ≠AI |
| `patents_resident` **парой с** `patents_total_office` | INN counts | office, до 2021, CN subsidy peak |
| `mva_pct_gdp` | PRD **share** | ≠scale ≠fab; USA до 2021 |
| `hitech_export_share` | ADE share | SITC break; processing |
| `gdp_pc_ppp` | масштаб/нормализация | 2024 prelim |
| `semi_exports_hs8542` + `semi_status` | единственный tech-след | номинал, H3–H6, quarantine, ≠fab |

### KEEP WITH HEAVY RESTRICTION

| `tfp_ctfp` | только уровни gap к frontier; **не** USA-trend; **не** tech-TFP. Кандидат в appendix, не в ядро RQ. |

### DROP / DO NOT USE FOR INFERENCE (файлы оставить в архиве, не в thesis-теле)

| Объект | Почему |
|--------|--------|
| `conversion_ratios.csv` | counts÷intensities, разные знаменатели |
| `correlations_pooled.csv` | Simpson; GERD–TFP pooled −0.086 vs within >0 |
| `pca_*`, `model2_*`, F10 | incoherent loadings + wrong sign |
| `results/descriptive_cagr.csv` как сопоставимые | researchers USA 2010–22 vs CHN 2010–23 |
| `results/descriptive_snapshot_US_CHN.csv` 2023-колонка | NaN-стороны |
| `comtrade_hs8542_exports_clean.csv` как панель | USA-only, не источник tech_panel |
| `gdp_real_growth` raw | собран, в панели нет, почти не используется — не тащить «для полноты» |
| HPC/AI/quantum NaN-колонки в регрессиях | 100% missing |

### MISSING — решать отдельно (не «добрать всё»)

| Ряд | Нужен ли для Target State A (узкий RQ)? | Для Target State B (широкий RQ)? |
|-----|------------------------------------------|----------------------------------|
| TOP500 count+Rmax | нет | **да, 1 ряд** для HPC-кейса |
| Stanford AI Index CSV (pubs и/или private $) | нет | **да, 1–2 ряда** |
| EPO–OECD quantum IPF | нет | опционально 1 ряд |
| SEMI fab / nodes | нет (платно) | qual остаётся |
| Finance mix (financed, один vintage) | нет | иначе H3 хоронить |
| Labor productivity OECD GDPHRS | замена TFP? | optional |
| TiVA GVC | нет | H5/ADE |
| TWN в панели | нет для macro | **да для semis** |
| VC/PitchBook | нет | непрозрачен CN |

**[idea]** Максимум ценности: либо **0 новых рядов** (честный узкий RQ), либо **2–3 дешёвых открытых** (TOP500 + AI Index extract), не 10.

---

## 6. Quantitative diagnosis

### 6.1. Что нужно, чтобы ответить на отвечаемый RQ

Только: joint-year уровни; common-window темпы; явные окна; бенчмарки 6 стран как **контекст**, не как identification; карта missingness.

### 6.2. Что уже есть и избыточно / недообосновано

| Метод | Проблема | Рекомендуемый статус (предложение) |
|-------|----------|-------------------------------------|
| M1 two-way FE | RQ не про GERD→TFP; β неотличима от 0; USA=1; G=7; lag mining; R²=0.992 от FE | **SIMPLIFY → appendix / OPTIONAL** или **DROP** из основного аргумента |
| PCA+M2 | loadings ломают смысл «capability» | **DROP** |
| Conversion ratios | механический артефакт | **DROP** |
| Pooled corr | композиция | **DROP** из выводов; within — optional |
| Naive slopes + p-values | AR(1) игнорируется; выглядят как тесты | **SIMPLIFY:** slopes/CAGR без p **или** явно «ориентир» |
| Event pre/post | n=2, HS-break внутри окна | **DROP as effect**; KEEP vertical lines «не эффект» |
| TCI composite (не начат) | без 4 tech-панелей не тестирует H1 | **не строить как «тест H1»**; optional простой rank только по **измеримым** macro-блокам |
| Elastic Net / K-means (design optional, не начаты) | нет прироста к RQ | **не начинать** |
| H3/H5 regressions (не начаты) | нет finance mix; нет clean export DGP | **не начинать** без новых данных |

### 6.3. Level 2+ уже в репо — что снимать

**[located evidence]** Реализованы Level 2: LSDV FE M1, naive trend OLS, interaction DIFF.  
Реализован Level 3: PCA + FE на PC1.  
Level 4: не реализован (правильно).

**Предложение снять из основного текста:** PCA/M2 (Level 3), conversion, pooled corr, event-as-effect, p-values naive slopes как «тесты».  
**Предложение не наращивать:** cluster-HAC «чтобы спасти M1», lag2 потому что p=0.001, DiD на CHIPS.

---

## 7. Technology-case diagnosis

**[observation]** `final_project.md` §6 дисциплинированнее `technology_cases_final.md` (там ещё BERD «business-financed», паритет 77%, H1-coherence).

| Кейс | Качество | Единый framework? |
|------|----------|-------------------|
| Semiconductors | лучший: trade+macro+qual stage map с `?/H?` | частично; без TWN/KOR/NL как данных — misspecification, это **оговорка**, не finding |
| AI | honest insufficiency + general-macro подмена запрещена в final | всё ещё читается как мини-эссе |
| HPC | insufficiency writeup; TOP500 KeyError | нет чисел |
| Quantum | insufficiency; «≈0 effect» отозвано | нет чисел |

**[observation]** Четыре домена **не сидят в одной заполненной матрице** country×tech×stage. Есть словесный TCI и четыре раздела. Это близко к «четыре эссе + общий дисклеймер».

**[idea]** Одна таблица 8 стадий × 4 tech: ячейки = измеренный proxy / `?` / qual-маркер. Без отдельных вердиктов «кто лидирует в AI».

---

## 8. Synthesis diagnosis

**[observation]** `final_project.md` §10 — сильный минимальный thesis: intensity vs volume = арифметика знаменателей; M1 слаба; tech-зависимость недоказуема; **нет winner**. Это согласовано с evidence.

Проблемы синтеза как **магистерского продукта**:

1. Документов слишком много (design, map, 6+ review layers, два «final»). Риск цитировать stale (`reports/final_synthesis.md` ещё H1 partial).
2. Working topic обещает «путь развития» и «внедрение»; вывод говорит «мы измерили другие вещи». Честно, но защита спросит: зачем 4 tech?
3. Capability и economic impact **разведены в тексте** — хорошо; M1 всё же стоит рядом с productivity и создаёт иллюзию моста.
4. Winner не назначен — **сохранить**.

---

## 9. Rival explanations / alternative framings of the RQ

Наблюдение-якорь (не finding о моделях): **интенсивности входов выше у USA, объёмы/доли поздних метрик выше у CHN.**

Кандидаты (**все `candidate`, без ранжирования**):

| ID | Класс | Кандидат |
|----|-------|----------|
| R1 | proposed mechanism | Разные модели организации: US science/finance vs CN production/scaling |
| R2 | measurement / denominators | Население ×~4 и масштаб GDP предсказывают intensity vs volume без «модели» |
| R3 | construct mismatch | Статьи/патенты-counts ≠ quality; MVA share ≠ fab; HS8542 ≠ nodes |
| R4 | confounding | Стадия развития, структура GDP, processing trade, office-bias патентов |
| R5 | selection | 8 стран без TWN; FRA вместо foundry-хаба; ISR researchers=0 |
| R6 | reverse causation | Богатые тратят больше на R&D; TFP и researchers совместно определяются |
| R7 | policy/subsidy artefact | CN patent 2021 peak; BERD/GERD vintage mix |
| R8 | scale / accounting | TFP USA=1; GDPpc–TFP r=0.91 accounting-adjacent |
| R9 | stochastic / window | Articles CAGR 1.33% vs 0.43% из-за спада USA 2021–23 |
| R10 | competing mechanism | Allied supply chain (TW/KR/NL/JP) — третий полюс, не US–CN бинарь |

**Дискриминирующие предсказания (не тесты, предложения):**

- Если R2 доминирует: абсолютные researchers/GERD $ (если собрать) сузят «US HC lead».  
- Если R1: **tech-specific** профили различаются при **одних** знаменателях — сейчас **нет данных**.  
- Если R9: результаты чувствительны к 2010–21 vs 2010–23 — **уже видно** на articles.

Альтернативные формулировки RQ (**идеи**, не выбор):

1. **Descriptive mapping:** где измеримые US–CN gaps по S→ADE, и какие звенья принципиально пусты.  
2. **Measurement thesis:** почему «лидерство» переворачивается от выбора intensity vs volume.  
3. **Semis-centered:** одна зрелая цепочка + три кейса как qualitative contrast (maturity), без притворства панелей.  
4. Не выбирать: «организация → конверсия → TFP» без identification.

---

## 10. Target State

**[idea] Рекомендуемый Target State A — «честная измеримая карта»**

Проект становится **одним** аргументом:

> В 2010–2023 (с фактическими окнами по переменным) США и Китай расходятся по **типу измерения** вдоль одной TCI-цепочки: интенсивности R&D/HC vs объёмы S/INN и доли/стоимости PRD/ADE. Это описание метрик, не доказанная «модель конверсии» и не winner. Четыре технологии — **одна матрица missingness + qualitative stress-test зрелости**; количественно заполнен только semis-trade. Экономический эффект (TFP/GDP) описывается отдельно, без приписывания AI/semis/HPC/quantum.

Следствия (удаление разрешена):

- RQ заморозить на формулировке `final_project.md` §1.2 (или ещё короче: intensity vs volume + дыры).  
- H1–H6: либо **архивировать как untested design**, либо сузить до 1–2 descriptive hypotheses без «tech-dependence».  
- Не строить TCI-индекс как тест H1.  
- M1/PCA/conversion/pooled/event-effects — не в executive argument.  
- 4 tech ≤ 1 таблица + короткий qual, не 4 главы.  
- Stale файлы: не цитировать; `remaining_risks`, `reports/final_synthesis`, `technology_cases_final` — watermark SUPERSEDED.  
- Графики: F1–F7 + FIXED F8/F9; F10 в appendix «почему не PCA»; переписать **заголовки** (F1 сейчас утверждает convergence).

**[idea] Target State B — «минимальный возврат к 4 tech»** (только если автор хочет исходный RQ)

Добор **только** открытых рядов: TOP500 Nov snapshots; 1 audited AI Index series; опционально quantum IPF. Затем Level 1 профили 4 tech × наличные стадии. **Всё ещё без** FE/DiD/PCA. TWN — qual или одна trade-таблица, не обязательный 9-й FE-кластер.

**Не Target State:** «допилить M1 HAC + H3/H5 + TCI min-max + clustering», пока RQ каузальный, а данные macro.

---

## 11. Quantitative questions that actually need methods

| ID | Вопрос | Нужен ли метод сложнее Level 1? |
|----|--------|----------------------------------|
| Q1 | Где US–CN **уровни** расходятся по измеримым блокам TCI в joint-year? | Нет: snapshot + ratios |
| Q2 | Где расходятся **темпы** на common-window? | Нет: CAGR; slopes optional без p |
| Q3 | Является ли знак gaps арифметикой знаменателя (intensity vs volume)? | Нет: явная таблица dual-scale (per GDP / per capita / counts) |
| Q4 | Какие стадии/tech **нельзя** оценить? | Нет: missingness matrix |
| Q5 | Как выглядят KOR/JPN/DEU/ISR как **контекст**, не как «контроль»? | Нет: overlay на тех же графиках |
| Q6 | Связан ли GERD с агрегатным TFP внутри стран? | Только если автор **хочет** этот побочный вопрос; иначе не нужен |
| Q7 | Различаются ли профили 4 tech? | Да **данные**, не сложный метод; сейчас нельзя |
| Q8 | Causal effect CHIPS/BIS / finance mix / conversion efficiency | **Не отвечать** имеющимися данными |

---

## 12. Methodology Options table (ключ к решению)

Тесты: **A** необходимость для конкретного вопроса; **B** прирост vs более простой аналог; **C** объяснимость на защите; **D** данные реально есть; **E** масштаб учебной магистратуры.

| Method | Why needed | What it gives | Complexity | Simpler analog | Lvl | Approval? | A–E | Status |
|--------|------------|---------------|------------|----------------|-----|-----------|-----|--------|
| Joint-year snapshot + ratios | Q1 | Сопоставимые уровни US–CN | Низкая | «последний год» с NaN | 1 | нет (уже канон) | A+ B+ C+ D+ E+ | **KEEP** |
| Common-window CAGR с (start,end,n) | Q2 | Сопоставимые темпы | Низкая | CAGR на разных окнах | 1 | нет | A+ B+ C+ D+ E+ | **KEEP** (канон окон — approval) |
| Dual-scale table (intensity **и** volume) | Q3 | Показывает R2 vs R1 | Низкая | Один столбец ratios | 1 | нет | A+ B+ C+ D+ E+ | **KEEP / усилить** |
| Missingness / TCI occupancy matrix 8×4 | Q4, 4 tech в одном каркасе | Честные `?` | Низкая | 4 эссе | 1 | нет | A+ B+ C+ D+ E+ | **KEEP (сделать явной таблицей)** |
| Time-series plots F1–F7 + FIXED F8/F9 | Q1–Q2, защита | Наглядность | Низкая | только таблицы | 1 | нет | A+ B+ C+ D+ E+ | **KEEP**; **SIMPLIFY titles** |
| Comparator overlay (KOR/JPN/ISR) | контекст, не FE | «не бинарный мир» | Низкая | только US–CN | 1 | нет | A+ B+ C+ D+ E+ | **KEEP как фон** |
| Policy timeline (даты, не эффекты) | ориентация кейсов | маркеры режима | Низкая | DiD | 1 | нет | A+ B+ C+ D+ E+ | **KEEP descriptive** |
| Naive OLS slope + p | Q2 | «скорость» | Низкая–средняя | CAGR / endpoint | 1–2 | **да, если оставлять p** | A~ B− (p врёт) C~ D+ E~ | **SIMPLIFY: slope без p или DROP p** |
| Within-country / demeaned corr | Q6 light | не Simpson | Низкая | pooled r | 1 | да, если вообще corr | A~ B+ vs pooled C+ D+ E+ | **OPTIONAL** |
| Transparent stage ranks / min-max **только по измеримым macro-блокам** | визуальный профиль US vs CN | 1 картинка radar | Низкая | таблица levels | 1 | **да** (легко принять за «TCI-тест H1») | A~ B~ C+ D+ E~ | **OPTIONAL-PENDING**; не называть тестом H1 |
| RCA / export structure HS8542 vs broad hitech | ADE специализация | «не просто доля» | Низкая–средняя | hitech share | 1 | да | A~ B~ C+ D~ (нет полного trade) E+ | **OPTIONAL**; данных мало |
| M1 LSDV two-way FE | Q6 | условная ассоциация | Средняя | scatter GERD–TFP by country | 2 | **да** | A− (не RQ) B− C~ D+ (хрупко) E− | **OPTIONAL appendix / DROP from core** |
| Cluster / HC1 SE на M1 | честность uncertainty | шире CI | Средняя | «CI включает 0» словами | 2 | если M1 живёт | A~ B+ C~ D+ E~ | **KEEP numbers if M1 kept** |
| Simple lag-0/1/2 table | показать fragility | не «лучший лаг» | Низкая | один лаг | 2 | если M1 | A~ B+ C+ D+ E+ | **KEEP as fragility, not spec search** |
| Event means n=2 | — | почти ничего | Низкая | vertical lines | 1 | нет | A− B− C+ D~ E+ | **DROP as result**; lines OK |
| Conversion ratios | H4 | артефакт | Низкая | dual-scale | 1 | нет | A− B− C− D− E− | **DROP** |
| Pooled correlation matrix | — | Simpson | Низкая | within / none | 1 | нет | A− B− C+ D+ E− | **DROP inference** |
| PCA → TechPC1 + M2 | «индекс capability» | wrong sign | Средняя | ranks Level 1 | 3 | нет | A− B− C− D− E− | **DROP** |
| TCI composite 8×4 tech | H1 preregistered | нет входных tech-рядов | Средняя | occupancy matrix | 3 | да, но **не рекомендуется** | A− сейчас D− E− | **не строить** |
| K-means / Elastic Net | design optional | декорация | Средняя | overlay comparators | 3 | нет | A− B− C− D− E− | **REJECT default** |
| H3/H5 OLS/FE | finance/export | нет mix, грязный export | 2 | qual | 2 | да | A− D− E− | **REJECT until new data** |
| DiD / event study CHIPS | causal policy | n мало, confounders | Высокая | timeline | 3 | да | A− D− E− | **REJECT** |
| Factor analysis (если «как PCA») | индекс | то же, что PCA | 3 | ranks | 3 | да | как PCA | **REJECT default** |
| IV / SC / GMM / SEM / Bayesian / VAR / ML | — | — | 4 | — | 4 | — | E− | **REJECT** |
| TOP500 + AI extract (сбор, не метод) | Q7 | заполнить 2 кейса | Сбор данных | `?` | — | **да (scope)** | A+ если State B D? E~ | **OPTIONAL-PENDING scope** |

---

## 13. Proposed Method Set (**proposal only**, не approved)

### Core (рекомендуется; почти всё Level 1)

1. Joint-year snapshot + обязательные годы на каждой цифре  
2. Common-window CAGR; для articles — **оба окна + пик 2021**  
3. Dual-scale (intensity vs volume) как центральный descriptive result  
4. TCI как **организующая матрица**, occupancy 8×4 (`measured` / `?` / `qual marker`)  
5. Графики F1–F7 + F8/F9 FIXED; нейтральные заголовки  
6. Semis: номинальные HS8542 + явный ≠fab; остальное qual  
7. Allow-list языка из `final_project.md`  
8. Карта ограничений данных как **результат**, не как извинение  

### Optional (Level 2 или спорный Level 1; ждут знания/одобрения)

- M1 в **приложении** как «мы проверили ассоциацию GERD–TFP, она хрупкая и не отвечает на RQ»  
- Naive slopes **без** p-values  
- Within-country correlations  
- Простой radar/min-max по **6–8 измеримым macro-блокам** (не 4 tech)  
- Добор TOP500 и/или AI Index (это scope данных, не эконометрика)  

### Rejected (Level 3/4 и вредные Level 1; пока автор не настоял)

- PCA, M2, F10 как evidence  
- Conversion ranking  
- Pooled corr как evidence  
- Event pre/post как эффект CHIPS/BIS  
- K-means, Elastic Net, TCI-index как тест H1  
- H3/H5 regressions на текущих переменных  
- DiD, IV, SC, GMM, SEM, Bayesian, VAR, ML  

### Awaiting user approval

- Канонический RQ: State A vs State B  
- Судьба M1: DROP / appendix / (не рекомендуется) core  
- Судьба H1–H6: archive untested vs rewrite 1–2 descriptive H  
- Строить ли простой macro-radar  
- Собирать ли TOP500 / AI Index  
- TWN: остаётся дырой или qual-вставка  

### Possible substitutes (если автор знает «похожее»)

| Если знакомо | Можно заменить |
|--------------|----------------|
| CAGR / средние темпы | OLS slope |
| «до/после» средних | event study / DiD |
| z-score / ранги / «индекс из 5 показателей вручную» | PCA / factor analysis |
| FE как «убрать среднее страны» | M1, если вообще нужен Q6 |
| Доли экспорта | RCA (если посчитают Comtrade-корзину) |
| Scatter по странам | pooled corr |

**Это предложение. Не считать Approved Method Set.**

---

## 14. Questions for the author (decision form)

Не yes/no. Можно: «не знаю X, но знаю Y».

**Q-RQ.** Какой вопрос должен остаться на обложке?  
(а) узкий: уровни/тренды измеримой цепочки + что нельзя измерить;  
(б) широкий: 4 tech и «конверсия в производство»; тогда какие **1–3** открытых ряда готовы собрать;  
(в) другое своими словами.

**Q-H.** H1–H6: оставить как «preregistered, не тестированы» / выкинуть из thesis / переписать 1–2 descriptive? Если переписать — какие формулировки вам **понятны** (не «что звучит научно»)?

**Q-M1.** Two-way FE: `TFP_it = α_i + δ_t + β GERD_{t-1} + θ log researchers` — можете объяснить профессору, **что идентифицирует β** и почему USA=1 ломает within-TFP?  
Варианты ответа: «да, оставить в приложении» / «нет, достаточно графика TFP и GERD по отдельности» / «не знаю FE, но понимаю „корреляция внутри страны после вычитания среднего“» / «хочу что-то вроде factor analysis вместо FE».

**Q-slope.** «Наклон прямой по годам» vs CAGR: что объясните увереннее? Нужны ли вам p-values, если они наивные (игнорируют автокорреляцию)?

**Q-index.** «Свести GERD, статьи, MVA к одному числу»: PCA / factor analysis / ручные ранги 1–8 / не сводить. Что узнаваемо? (PCA в проекте уже сломался на знаке articles.)

**Q-event.** CHIPS/BIS: только даты на графике, или хочется «эффект закона»? Если второе — знаете ли разницу «среднее 2 года до / 2 года после» vs DiD?

**Q-tech.** Готовы ли оставить AI/HPC/quantum как `?` в общей матрице, или обязателен хотя бы TOP500 и/или AI publications?

**Q-semis.** Сравнение без Тайваня: ок как ограничение, или нужна отдельная qual-страница foundry (без панели)?

**Q-prod.** Экономический эффект: GDP pc + оговорка «не tech-TFP» достаточно, или TFP/M1 обязательны потому что «в магистерской должна быть регрессия»?

**Q-lang.** Уверенно ли держите allow-list («ассоциировано / не измерено»), или есть соблазн писать «США превращают науку, Китай — масштабирует» как вывод?

---

## 15. Dependency graph

```
Research Question ──┬── [WAIT: Approved Method Set] ── Analytical Framework (TCI as map vs index)
                    │
                    ├── Data Requirements (какие ряды вообще нужны)
                    │         │
                    │         ▼
                    │   Data Validation (joint-year, windows, labels PERFORMED/office)
                    │         │
                    ├──► Quantitative Analysis (Core Level 1)  ── PARALLEL с Technology occupancy matrix
                    │         │
                    │         ▼
                    │   Technology cases (одна матрица; semis-trade subset)
                    │         │
                    │         ▼
                    │   Economic mechanisms = explicit NOT IDENTIFIED
                    │         │
                    └──► Synthesis ── Final conclusions (no winner)
```

| Узел | Параллельно? | Sequential? | Ждёт Method Set? |
|------|--------------|-------------|------------------|
| Выбор RQ A vs B | — | Первым | **да** |
| Чистка stale docs / DO NOT USE watermark | да | после Method Set желательно | нет для watermark |
| Core descriptives (уже посчитаны) | да | нет | нет пересчёта, да канона окон |
| M1 / radar / TOP500 | — | только если approved | **да** |
| Tech matrix | да с Q1–Q4 | после RQ freeze | да, если State B |
| Синтез / презентация | нет | в конце | **да** |
| Causal language / H-verdicts | — | непрерывный контроль | да (запреты уже есть) |

**MUST WAIT:** любой новый расчёт «индекса», любая новая регрессия, любой добор данных, любой rewrite `final_project.md`.

**Можно параллельно после approval:** watermark stale files; список figure-title fixes; черновик occupancy matrix из уже известных `?`.

---

## 16. Later agent architecture sketch (**не запускать**)

Только роли, оправданные дырами. Не писать ORCHESTRATION_PLAN.md.

| Роль | Зачем | Триггер |
|------|-------|---------|
| Method-set recorder | записать ответы §14 → Approved Method Set | после ответов автора |
| Stale-file janitor | SUPERSEDED banners; не цитировать reports/* | сразу после freeze |
| Figure-title fixer | убрать causal titles в F1/F9 originals | Core KEEP graphs |
| Window-canon calculator | articles оба окна; единый CSV | Q2 freeze |
| Optional collector | TOP500 / AI Index **только State B** | approval Q-tech |
| Tech-matrix writer | одна 8×4 таблица вместо 4 эссе | после RQ freeze |
| Thesis compressor | один читаемый отчёт из `final_project.md` | после method freeze |
| Defense/slides | `defense_risks.md` → слайды | в конце |
| **Не нужен:** econometrics expander, ML agent, DiD agent, PCA revival, literature-novelty agent | | |

---

## 17. Relevant skills found (bounded; ничего не устанавливалось)

**Search boundary:** 2026-09-20; локально `C:\Users\danii\.agents\skills\` и `C:\Users\danii\.cursor\skills-cursor\`; CLI `npx skills find` ×4 (`macroeconomics research`, `literature review`, `academic writing`, `data visualization`); источник skills.sh. **Не устанавливалось.**

Локально: `statistical-analysis`, `hypothesis-generation`, `scientific-brainstorming` есть. **Не located locally:** experimental-design, literature-review, academic-writing, data-visualization, presentation.

Клиентские hits, релевантные **позже** (0–5), порог 1K+ и репутация:

| Skill | Installs | Source | Зачем позже | Осторожность |
|-------|----------|--------|-------------|--------------|
| `statistical-analysis` (уже local, K-Dense) | local | `.agents/skills` | диагностика OLS, если M1 останется | **не** тянуть Bayesian из того же skill |
| `k-dense-ai/scientific-agent-skills@literature-review` | 1.9K | K-Dense | bounded 5–10 источников, ledger | не novelty-claims |
| `anthropics/knowledge-work-plugins@data-visualization` | 12.2K | Anthropic | подписи/F1–F9 без overclaim | не новые типы графиков |
| `bahayonghang/academic-writing-skills@latex-paper-en` | 5.4K | skills.sh | оформление, не методы | thesis на русском — проверять шаблон |
| `hypothesis-generation` (local) | local | уже использован | rival explanations, claim lint | — |

**Не рекомендовать (не fit):** `equity-research` / `macro-rates-monitor` (финансы/ставки, не tech-chain). `llmquant-macro` 479 installs — ниже 1K. `wentorai/.../economics-skills` 141 — ниже порога.

---

## 18. Open risks and unknowns

| Риск | Тип | Комментарий |
|------|-----|-------------|
| RQ drift обратно к «моделям конверсии» | process | тексты позволяют цитировать старый design |
| Stale files | process | `remaining_risks.md`, `reports/final_synthesis.md`, `technology_cases_final.md`, F9 original title |
| Articles window | measurement | меняет USA growth 1.33% vs 0.43% |
| TWN vs FRA | design vs data | semis misspecification |
| M1 как «обязательная регрессия» | incentive | ухудшает E, не лечит A |
| Добор всех missing рядов | scope creep | ломает учебный срок |
| Causal verbs | language | F1 title уже нарушает дух allow-list |
| Literature | unknown | обзора нет; не утверждать gap в литературе |
| Git history | not checked | как и в PROJECT_STATE |
| Воспроизведение M1 cluster SE из кода | unknown | cluster, видимо, в quant review вручную, не в `analysis_agent4.py` (там только HC1) |

---

## Appendix. Claim log (коротко)

| Claim | Label |
|-------|-------|
| Панель 200 строк, FRA, tech NaN, M1 numbers, PCA loadings | located evidence |
| Intensity vs volume = «разные модели» | **не** evidence; candidate R1 vs R2 |
| GERD вызывает TFP | **не** следует из M1 |
| США или Китай «выиграли» | запрещено |
| TCI/H1 «почти подтверждены» | отозвано проектом; не возвращать |
| Рекомендация State A + Core Level 1 | **idea / decision pending** |

*Конец DIAGNOSIS_AND_METHODOLOGY.md. Следующий шаг человека: ответить на §14, затем записать Approved Method Set. Этот файл — не approval.*

# Research Logic Final — исправленная логическая цепочка

Дата: 2026-09-14. Статус: этот файл **заменяет логику выводов** `reports/final_synthesis.md` §1/§4/§5/§6/§8,
`reports/tech_cases_comparison.md` §"Синтез" (абзац "Одна строка"), `reports/analysis_report.md` §1/§4,
`reports/hypothesis_table.md` — в части вердиктов и механизмов. Исходные файлы не редактируются
(аудит-трейл сохраняется, как в `data_reviewed/`); при расхождении приоритет у этого файла.
Числа не пересчитываются; используются только уже существующие доказательства:
`results/*.csv`, `regression_results_final.csv`, `data_reviewed/*`, `technology_cases_final.md`,
`quant_reviewed.md`, `project_revision.md`.

> **ARCHIVE / UPDATE note (2026-09-20, ResearchDesignAgent).**  
> Сужение RQ (§1.3) сохраняет смысл, но **каноническая Frozen RQ** (с полными окнами) и **D1–D2** — в `RQ_FREEZE.md`.  
> H1–H6 в §2 = **archived design / not tested** (не текущий hypothesis layer). Приоритет гипотез: `reports/hypothesis_table.md` (2026-09-20) > этот файл.  
> `final_project.md` остаётся главным синтезом. Тело файла не переписывалось.

Правило чтения: `+` — сильнее на данной стадии по evidence; `~` — паритет/смешанно;
`?` — нет данных для вердикта. **[expert assessment]** = качественная оценка без ряда в панели,
не evidence. Слова «сильнее/лидерство/эффект/конвертируют» без указания стадии и evidence запрещены.
Все регрессии и корреляции — ассоциации, не causality.

---

## 0. Что исправляет этот файл (карта разрывов цепи)

| Звено цепи | Разрыв до исправления | Решение здесь |
|---|---|---|
| RQ → H1–H6 | RQ требует ответа по 4 технологиям и зрелости; данные покрывают только macro + semis-trade | RQ сужен до ответимой части; неотвечаемая часть явно маркирована (§1) |
| H → test | H1-verdict «partially supported» без preregistered TCI-теста; H4 переопределена пост hoc | Вердикты разделены: preregistered test vs дескриптивное наблюдение (§2) |
| Indicators → data | BERD прочитан как «financed» (ошибка ярлыка); patents — как «origin» (ошибка ярлыка); HS-ревизии скрыты | Определения исправлены по `data_reviewed/data_quality_final.md` (§3) |
| Data → analysis | CAGR/снапшоты на несопоставимых окнах; ratio с NaN-стороной; intensity vs volume как «находка» | Только joint-year/common-window; intensity/volume — арифметика, не находка (§3–§4) |
| Analysis → cases | COM пуст, но механизмы FIN→COM сформулированы; upstream-контроль → рента без измерения | Механизмы с пустым звеном помечены «механизм не идентифицирован» (§5) |
| Cases → mechanisms | Trade→fab; volume→leadership; маркеры→эффект | Запреты + матрица с `?` (§4, §9) |
| Mechanisms → conclusion | Thesis воспроизводит исходный тезис №1 при 3/4 пустых панелях (предрешённый вывод) | Минимальный thesis, только измеримое (§6) |
| Conclusion → geopolitics | §6 final_synthesis подаёт внешние qual-знания как «выводы из данных» | Геополитика ужата до контекстных оговорок, не импликаций (§7) |

---

## 1. Research question: ответимая и неотвечаемая части

### 1.1. Исходный RQ (research_design §A)

> Как различаются модели технологического развития США и Китая в превращении
> научно-исследовательских и производственных ресурсов в технологические результаты —
> и на каких этапах цепочки эти различия наиболее устойчивы для четырёх стратегических технологий?

### 1.2. Проблема

Вторая половина RQ («на каких этапах… для четырёх технологий», «зависят ли узкие места
от зрелости») требует 4 tech-панелей. По `data_reviewed/data_quality_final.md`:
AI/HPC/quantum — 100% missing; HPC-сбор упал (KeyError); quantum не извлечён;
semis — только trade-стоимости с карантином CHN 2015–17, нулями DEU/FRA и сменами HS-ревизий
внутри окна. TCI-индекс (`tci_scores.csv`) не построен. Ответить на исходный RQ данными
проекта **невозможно**; любой ответ на полный RQ — переутверждение.

### 1.3. Исправление: суженный RQ (ответимый) + явный остаток

**Отвечаем только на это:**

> Какие различия уровней и трендов US–CN наблюдаются в измеримой macro-цепочке
> (GERD/BERD-интенсивности, researchers-интенсивность, объёмы статей/патентов-counts,
> MVA-доля, hitech share, HS8542-стоимости) в 2010–2023, и какие звенья TCI
> в принципе нельзя оценить имеющимися данными?

**Явно не отвечаем (insufficient, не «частично доказано»):**

- tech-зависимость профиля (ядро H1) — нужны 4 tech-панели, есть 1 частичная;
- зрелость → bottleneck (H2), finance → outputs (H3), production → export (H5),
  INN–COM gap (H6) — тестов нет (см. §2);
- любой каузальный «механизм конверсии» и любой overall winner.

---

## 2. Гипотезы: preregistered test vs дескриптивное наблюдение

Принцип: вердикт ставится **по preregistered тесту**. Дескриптивная согласованность —
отдельная колонка, не повышающая вердикт. Пост hoc переопределения запрещены.

| ID | Preregistered тест (research_design) | Статус теста | Дескриптивное наблюдение (не тест) | Итоговый вердикт |
|---|---|---|---|---|
| H1 | TCI-профиль 8–10 этапов × 4 tech; gap US–CN и стабильность паттерна между кейсами | **Не выполнен**: `tci_scores.csv` отсутствует; 3/4 tech-панелей пустые | Macro-асимметрия измерений: интенсивности входов выше в США, абсолютные объёмы outputs и доли PRD/ADE выше в Китае (см. §4). Это **разные измерения**, предсказуемые из знаменателей (§3.4), не рейтинг | **Not tested as preregistered. Дескриптивный паттерн — только наблюдение, не поддержка H1** (замена «partially supported (macro)») |
| H2 | Сравнение stage-gap между 4 кейсами; rank-корреляция зрелости vs этапа | **Не выполнен**: 1 частичный кейс из 4 | Структура qual-разборки semis/AI/HPC/quantum согласуется с ожиданием, но это coherence с дизайном | **Insufficient / not tested** (без изменений, но с запретом чтения coherence как evidence) |
| H3 | Cross-country regression finance mix → stage outputs | **Не выполнен**: регрессия не запускалась (лимит 2 моделей); **измерителя finance mix в панели нет** — BERD в панели это PERFORMED % GDP (OECD MSTI `P_BERPCT`), не financed, другой провайдер/винтаж, чем WB-GERD; ISR BERD>GERD 2021–23 доказывает несводимость (`data_quality_final.md` §1). Дескриптивный BERD/GERD ~77% — **смесь винтажей, не finance mix** | Pooled BERD–hitech r=+0.16 — композиционный артефакт, не evidence | **Not tested; finance mix — unmeasured. Паритет 77% как «опровержение нарратива» отзывается** (см. §3.2) |
| H4 | Output/input ratios по этапам; разрыв в patents/publications меньше, чем в capacity/export | **Не выполнен как тест конверсии**: `conversion_ratios.csv` смешивает counts÷intensities с разными знаменателями/годами — механически сконструирован, исключён (`quant_reviewed.md` §3) | Разрывы численно разнородны (GERD 0.75 vs статьи 2.17 vs патенты-counts vs MVA-доля), но это **гетерогенность измерений**, предсказуемая из знаменателей, не тест конверсии | **Not tested as preregistered. Пост hoc «partially supported (как гетерогенность)» отзывается**; наблюдение фиксируется без вердикта поддержки |
| H5 | Regression с лагами; R² science-only vs production-only | **Не выполнен**: export-регрессии нет | Pooled MVA–hitech 0.40 > articles–hitech 0.12 — between-смещён; hitech-корзина широкая + SITC-break; HS-ревизии внутри IC-окна | **Insufficient / not tested** (без изменений) |
| H6 | Gap-index US vs CN по каждому кейсу | **Не выполнен**: COM пуст (startups/licenses/revenue — нет), gap-index не построен | — | **Insufficient / not tested** (без изменений) |

**Следствие для «6 контрольных вопросов» (замена final_synthesis §4):**

1. Полностью поддержана — ни одна.
2. Частично поддержана — **ни одна** (ранее «H1-macro/H4-гетерогенность partial» — отозвано как пост hoc повышение вердикта без теста).
3. Отвергнута в сильном смысле — ни одна (мощности для rejection нет).
4. Интерпретации, отвергаемые как запрещённые (не H-вердикты): patents-counts=leadership;
   articles-volume=leadership; trade-value=fab-leadership; R&D-spending=success;
   benchmark=economic leadership; TOP500-rank=AI-capability; funding=commercialization.
5. Устойчиво только дескриптивное: противоположные знаки разрывов по интенсивностям
   vs объёмам/долям (арифметика масштаба, §3.4) + падение MVA-долей обеих стран
   (UNIDO/WB, common-window) + медленный TFP catch-up уровней при росте абсолютного
   GDP pc разрыва.
6. Слабые/отсутствующие доказательства: всё по AI/HPC/quantum; всё finance→outputs;
   всё «эффективность конверсии»; всё CHIPS/BIS-эффекты; всё fab-доли/EDA/equipment.

---

## 3. Indicators → data → analysis: что реально измерено

### 3.1. Исправленные определения (по data_quality_final.md §1 — обязательно)

| Переменная | Было (ошибочный ярлык) | Стало (использовать только так) | Следствие для логики |
|---|---|---|---|
| `berd_pct_gdp` | «Business-financed GERD», finance mix, F9 «Business-financed» | **BERD PERFORMED % GDP** (OECD MSTI `P_BERPCT`); другой провайдер/винтаж, чем WB-GERD; заголовок F9 неверен; ISR BERD>GERD 2021–23 — артефакт винтажа | **H3 неизмерима в панели.** Любое «BERD/GERD ~77% в обеих» — не finance mix, а смесь винтажей; не использовать ни за, ни против finance-нарратива |
| `patents_resident` | «by applicant origin» (WIPO origin) | **Resident filings AT national office (office basis)**, 2000–2021; USA: nonresidents > residents, CHN — наоборот | Разрыв 5.44x (2021, resident-only) отражает **home-bias офисов + субсидии CN**, не inventive output. Total-office 2.68x — тоже counts, не качество. Оба — только объёмы заявок, не INN-лидерство |
| `semi_exports_hs8542` | Единый ряд HS8542 2010–2024 | **Номинал USD, смешанные HS-ревизии** (H3 2010–11 / H4 2012–16 / H5 2017–21 / H6 2022–24), re-exports/processing trade; retained 75/200; CHN 2015–17 — hard gap; DEU/FRA — 0 retained; спайки CHN 2012–13 +63%, KOR 2016–17 +65% — flagged | **CAGR поверх окна смещён сменами ревизий и карантином.** IC-тренд читать только как «номинальные стоимости с разрывами», не как мощность/технологический тренд |
| `hitech_export_share` | Ряд с 1988 | Ряд **с 2007**; SITC Rev.4 break (Oct 2024, 28% missing) + ISR-нестабильность 2007–09 | Тренд поверх break невалиден; ранние годы не использовать |
| `researchers_per_million` | Единый ряд, GBR «ends 2019» | UNESCO-UIS; **GBR ends 2017** (8 наблюдений в окне; 2018–24 missing), USA ends 2022, ISR 0/25; FTE/headcount различаются | Тексты с «GBR ends 2019» ошибочны. CAGR/слоупы только common-window с явными (start,end,n) |
| `tfp_ctfp` | USA=1 «2000–2023» | **USA=1.000 каждый год, проверено 1994–2023** (construction); macro TFP, не tech-TFP | USA дают ноль within-вариации исхода; наклон USA не интерпретируется; M1 идентифицируется без USA |

### 3.2. H3 закрыт как unmeasured (важное исправление)

Ранее (`final_synthesis.md` matrix/§5, `hypothesis_table.md` H3, `technology_cases_final.md` §AI/синтез п.4):
«BERD/GERD ~77% в обеих странах — нарратив "частный vs направленный" данными не подтверждается».
Логическая ошибка: опровержение построено на несводимых винтажах (WB-GERD vs OECD-BERD PERFORMED).
По `data_quality_final.md` §1 это не finance mix, а смесь определений; ISR-инверсия это доказывает.
**Исправление:** тезис о паритете 77% **не использовать ни как подтверждение, ни как опровержение**.
Финансовая структура моделей — **неизмерена в панели**; оба направления («различается» /
«одинакова») — без evidence. Qual-механизмы «частный FIN→INN/COM vs направленный FIN→PRD/scaling»
переводятся в статус **недоказанных гипотез без измерителя**, а не «ослабленных механизмов».

### 3.3. Правила сопоставления окон (обязательные)

- Никаких ratio с NaN-стороной. Только **latest-joint-year**:
  researchers 2022 (USA 4937.49 vs CHN ~1849, 0.375x — intensity, не headcount);
  patents 2021 (resident 5.44x **только в паре** с total-office 2.68x);
  MVA 2021 (USA 10.53% vs CHN 26.62%, 2.53x — **доля, не масштаб**);
  GDP pc 2023 ($74352 vs $22687, 0.305x **только в паре** с абсолютным разрывом $49321→$51664).
- Никаких CAGR/слоупов на несопоставимых окнах. Common-window только:
  researchers 2010–2017 (GBR-ограничение), patents/total 2010–2021, MVA 2010–2021,
  остальное 2010–2023; TFP USA из ранжирований исключён.
  Текстовые пары «researchers 2.6% vs 6.8%», «MVA −1.1% vs −1.7%»,
  «articles 0.4% vs 8.9%» на полных окнах — **несопоставимые окна, не использовать без пометки**;
  корректные common-window см. `data_reviewed/tables_reviewed/descriptive_cagr_common_window.csv`,
  `quant_reviewed.md` §2.
- `conversion_ratios.csv`, `correlations_pooled.csv`, M2/PCA — **DO NOT USE для выводов**
  (исключения подтверждены, без изменений).

### 3.4. Intensity vs volume: арифметика, не находка (исправление circular reasoning)

Центральный «паттерн» (США — интенсивности, Китай — объёмы) — **предсказуемое следствие
знаменателей**: население ×4.2 и масштаб GDP. Большая страна при сопоставимых интенсивностях
механически даёт большие абсолюты; малая/богатая — высокие per-capita/%GDP.
Предъявлять это как эмпирическое открытие о «моделях» — circular: мера сконструирована так,
чтобы дать этот знак. **Исправление:** фиксировать как **описание выбранных метрик**,
не как свойство экономик:
«в выбранных интенсивностях выше США; в выбранных абсолютах/доляx выше Китай —
это следует из denominators, tech-содержание не установлено».
Tech-зависимость этого паттерна (ядро H1) не тестируема без tech-панелей.

### 3.5. M1: что показывает и чего не показывает (без изменений по числам, строже по чтению)

Авторитетно: `regression_results_final.csv` (M1 retained descriptive-only; M2 excluded).
M1: n=84, K=20, df=64, G=7 (ISR 0, GBR 7, USA 12); β_GERDlag1=0.0275, HC1 CI [−0.0005, 0.0554],
p=0.059; cluster (t_6) CI [−0.048, 0.103], p=0.409; θ_lres=0.0563.
Хрупкость: lag0 β=0.0125 p=0.418; lag2 β=0.0525 p=0.001 (лаг не обоснован теорией);
drop-CHN β=0.0189; drop-KOR β=0.0487; pooled OLS β=−0.207 (знак зависит от FE);
corr(gerd,lres)=0.71; AR(1) 0.32–0.90; USA-нулевая вариация исхода.

Допустимое чтение (единственное):
«В 84 страно-годах GERD_{t−1} на 1 пп выше ассоциирован с +0.027 TFP-пункта
условно по стране, году и researcher-интенсивности — **HC1-CI включает 0,
кластерный CI широк, от нуля неотличимо; лаг/окно/состав меняют знак и значимость;
обратная причинность и пропущенные переменные не устранены**».
Величина: закрытие TFP-разрыва 0.53 одной β требует +19 пп GERD — абсурд,
β — не политический мультипликатор. Лаг-1 не headlining; показывать все три лага.
Агрегатный TFP не tech-TFP: **приписывать AI/semis/HPC/quantum запрещено**.

---

## 4. Исправленная USA–CHN матрица (только измеримое; остальное — `?`)

Источники ячеек: `results/descriptive_snapshot_US_CHN.csv` (joint-year),
`data_reviewed/tables_reviewed/descriptive_snapshot_latest_joint.csv`,
`descriptive_cagr_common_window.csv`, `regression_results_final.csv`,
`results/event_CHIPS_BIS_prepost.csv` (только маркеры, n=2, без SE),
`reports/data_quality_report.md`, `data_reviewed/data_quality_final.md`.

| Stage (TCI) | USA | China | Evidence | Confidence + caveat |
|---|---|---|---|---|
| S: объём статей (general) | ~ (ниже по объёму с ~2020) | + (объём 2.17x в 2023, general) | snapshot joint-year; slopes (common-window) | MEDIUM для объёмов; **не AI/science-лидерство** (volume≠impact; English/Scopus bias; не field-specific) |
| HC: researchers/млн (general) | + (интенсивность ~2.6x в joint-2022) | ~ (уровень ниже; % рост быстрее) | snapshot joint-2022; common-window CAGR | MEDIUM-HIGH для интенсивности; **не headcount и не качество** (per-million знаменатель; FTE/headcount; GBR ends 2017, USA ends 2022, ISR 0) |
| RD: GERD % GDP | + (3.45 vs 2.58 в 2023) | ~ (0.75 от США; slopes параллельны, diff n.s.) | snapshot; trend | HIGH для интенсивностей; CN GDP revisions меняют ratio |
| FIN: структура финансирования | ? | ? | **Нет измерителя в панели** (BERD=PERFORMED, винтажная смесь; VC/AI-$ missing) | **Insufficient. Паритет 77% отозван** (§3.2) |
| INN: патенты-counts (general) | ~ (counts ниже) | + (resident 5.44x **только в паре** с total-office 2.68x, 2021 = пик субсидий CN) | snapshot joint-2021 оба ряда | MEDIUM для counts; **запрет quality-вывода** (office-basis home-bias; subsidies; triadic/PCT не собраны) |
| PRD: MVA-доля (macro) | Ниже доля (10.5% в 2021) | Выше доля (26.6% в 2021 joint; 25.0% в 2023) | snapshot joint-2021; common-window CAGR (обе доли падают) | MEDIUM-HIGH для долей; **доля, не абсолютный выпуск и не fab-мощность** (MVA macro, не semis-VA) |
| PRD: зрелые мощности / packaging / fab-доли | ? | ? | Нет SEMI-ряда | **Insufficient. MVA-доля и IC-стоимость — не измерители node-долей** |
| COM: стартапы/лицензии/revenue/frontier/adoption | ? | ? | Пусто (AI/HPC/quantum 100% missing; notable models — snapshot, не ряд) | **Insufficient** |
| ADE: HS8542-стоимости | ~ ($43.6 млрд, 2023) | + ($136.4 млрд, 3.13x **номинал**) | Comtrade joint-values | MEDIUM для стоимостей; **номинал, processing trade, re-exports HK/SG, HS-ревизии в окне, карантин CHN 2015–17; HS8542≠advanced nodes; trade≠fab** |
| ADE: hitech share (broad) | ~ (21.8%) | + (26.6%; gap 9.5→4.7 пп) | snapshot | MEDIUM для корзины; **trend over SITC-break невалиден** |
| Productivity: TFP (macro) | 1.0 (**construction**) | 0.47 (catch-up уровней +0.076 за 13 лет) | snapshot; M1 (β=0.028, CI∋0; cluster CI шире) | MEDIUM для уровней; **LOW/запрет causality; агрегатный, не tech-TFP; USA — константа** |
| Productivity: GDP pc | $74.4k | $22.7k (ratio 0.305) + **абс. разрыв вырос $49k→$52k** | snapshot | Ratio-конвергенция ≠ конвергенция уровней |
| Resilience / upstream / foundry / EDA / EUV | ? (как evidence) | ? (как evidence) | Нет рядов; NL/JP/TW/KR-структура — внешнее знание, не панель | **Insufficient как finding; допустимо только как контекст** (§7) |

Удалённые/пониженные клетки относительно старых матриц: FIN-паритет (отозван, → `?`);
«PRD mature/packaging +» по MVA/IC (→ `?` как fab-вердикт, измеримы только доля/стоимости);
«AI S/INN +» как tech-вердикт (→ general-объёмы, не AI); HPC/quantum-строки без изменений (`?`/`~0`-qual).

---

## 5. Экономические механизмы: что показано, чего нет

Язык — только ассоциативный. Для каждого канала: показание / не-показание / статус.

- **R&D → productivity.** Не идентифицирован. M1 — слабая хрупкая условная ассоциация,
  неотличимая от нуля (см. §3.5). Лаг-1 теоретически не обоснован; FE — не идентификация;
  эндогенность (богатые тратят больше), omitted variables, измерение CN — не устранены.
  Tech-приписывание запрещено. **Статус: механизма нет; есть уровни catch-up.**
- **Finance → INN/COM vs FIN → PRD/scaling.** Не тестируем: измерителя finance mix нет
  (§3.2), регрессии нет, COM пуст. Pooled r=+0.16 — артефакт. BERD-уровень выше в США
  (2.66 vs 2.00) — это **уровень интенсивности PERFORMED**, не «частная модель».
  **Статус: два недоказанных qual-предположения без измерителя, не «механизмы».**
- **S/INN-объёмы → PRD/scaling-масштаб (Китай).** Не тестируем: нет fab-ряда, нет регрессии
  PRD на RD/FIN, MVA — macro-доля, IC — номинальные стоимости с assembly-смещением.
  Совместимость дескриптивов с нарративом — не тест. **Статус: qual-предположение.**
- **PRD/scaling → торговое присутствие (H5).** Не тестируема: export-регрессии нет;
  pooled r — between-смещён; корзина широкая + SITC-break; HS-ревизии. **Статус: нет.**
- **INN → COM-конверсия и INN–COM gap (H6/H4).** COM пуст; conversion ratios исключены;
  патенты/статьи — counts/volume без качества. Ранжирование «эффективности» запрещено.
  **Статус: нет.**
- **Upstream-контроль (EDA/IP/EUV) → рента/рычаг (США+союзники).** В панели нет цен,
  марж, долей foundry/equipment, роялти. BIS/CHIPS/MiC2025/NQI/Micius — policy-маркеры,
  не evidence эффекта; event pre/post n=2 без SE, конфаундеры (цикл, COVID, downturn 2023).
  **Статус: tech-описание без экономического измерения; как механизм не заявлен.**
- **AI-диффузия через manufacturing/downstream; HPC peak→доступность;
  quantum-опционы → будущая COM.** Adoption/COM/AI-compute/IPF-рядов нет.
  **Статус: гипотезы без теста.**
- **Long-run growth («модель X даёт рост»).** Нет growth-регрессии; GDP pc — только
  уровни/тренды (ratio-конвергенция при дивергенции уровней). Sectoral TFP out of scope.
  **Статус: запрещён.**

Итог одной строкой: измеримая часть показывает, **где различаются уровни/тренды
выбранных метрик**, но не показывает, **насколько одно звено вызывает другое**;
все стрелки «→» между звеньями — недоказанные предположения, а не оценки эффектов.

---

## 6. Final thesis (минимальный, заменяет §8 final_synthesis и «одну строку» tech-cases)

**Главный вывод:** в измеримой macro-части (2010–2023, joint-year/common-window)
США выше по R&D/HC-интенсивностям (GERD, BERD PERFORMED, researchers/млн),
Китай — по абсолютным объёмам статей/патентов-counts и по долям/стоимостям
поздней части (MVA-доля, hitech share, HS8542-номинал) — **но это описание выбранных
измерений с предсказуемой знаменательной арифметикой, а не установленный факт
о «моделях»; каузальные механизмы конверсии не идентифицированы; tech-зависимость
профиля (AI/semis/HPC/quantum) недоказуема без tech-панелей; frontier-узлы
количественно не оценены в панели.**

Три опорных пункта (только измеримое):

1. **Интенсивности vs объёмы/доли — разные измерения, не рейтинг.**
   GERD 0.75, BERD-уровень 0.75, researchers-интенсивность ~0.38 (joint) vs
   статьи-объём 2.17, патенты-counts (5.44 resident / 2.68 total-office, 2021),
   MVA-доля ~2.5x (joint-2021), IC-номинал 3.13x — гетерогенность знаков следует
   из denominators; ранжирование «конверсии» запрещено.
2. **Связь ресурсов с TFP слаба и неотличима от нуля; catch-up — уровни, не механизм.**
   β_GERD=0.028 (HC1 CI∋0, p=0.06; cluster CI [−0.048, 0.103], p=0.41),
   хрупка к лагу/окну/составу; TFP CHN 0.40→0.47 — уровни macro-TFP, не tech-эффект.
3. **Единственный частичный tech-след — номинальные semis-стоимости с карантинами,
   не fab-лидерство; AI/HPC/quantum — insufficient.**
   HS8542 — номинал с HS-ревизиями, processing trade, re-exports, gap CHN 2015–17;
   hitech — broad basket + SITC-break; fab/EDA/EUV/COM/ADE-tech — нет рядов.

Чего thesis **не** утверждает (явно): кто «сильнее» в AI/HPC/quantum; что finance-модели
различаются; что конверсия эффективнее у X; что CHIPS/BIS дали эффект; что mature-масштаб
= лидерство; что объёмы = влияние; что TFP движим текущими GERD.

---

## 7. Геополитика: ужатая до контекста (замена §6 final_synthesis)

Статус: **не импликации из данных**, а внешние контекстные оговорки для читателя.
Не цитировать как findings; не выносить в executive conclusion.

1. Любое рассуждение о frontier-узлах (EUV NL, оборудование/материалы JP,
   foundry TW/KR, IP UK, OSAT-хабы) — **вне панели** (SEMI/fab-рядов нет;
   KOR/JPN-цифры в панели — GERD/trade-контекст, не мощности). US–CN пара без третьих
   сторон — неполная постановка для semis, но сама структура узлов панелью не измерена.
2. BIS Oct22/Oct23, CHIPS Act, MiC2025, Dual Circulation, NQI Act, Micius —
   **временные маркеры режима**, не evidence эффекта (event n=2, нет SE, downturn 2023,
   цикл/COVID/лаги/агрегация). Глаголы «снизили/повысили/дали эффект» запрещены;
   на графиках — только vertical lines с подписью «не эффект».
3. Decoupling-нарратив в данных смешанный **на уровне стоимостей/долей**
   (hitech CHN −3.6 пп post vs USA +1.5 пп при IC CHN +7.2% vs USA −1.9%),
   но это маркеры на фоне цикла, не оценка санкций.
4. HPC/quantum-геополитика из панели **не следует** (рядов нет; экон. эффект quantum ~0
   — qual-констатация ранней стадии, не оценка).
5. Избыточные формулировки («главный геополитический вывод», «рычаг США — upstream»,
   «рычаг Китая — mature-масштаб» как findings) — **удалены**; допустимо только:
   «внешние отраслевые источники указывают на концентрацию узлов вне US–CN;
   панелью это не измерено».

---

## 8. Hidden assumptions (явно фиксируем; ранее неявные)

1. Latest-vintage решает CN GDP revisions (GERD/GDP pc) — предполагаем, не доказываем;
   разрывы break-окон не тестированы.
2. Researchers FTE/headcount сопоставимы в пределах ряда — предполагаем с caveat;
   абсолютные головы из per-million не выводим (оценка «~1.2M→2.4M» без расчёта — удалена, §9).
3. Scopus fractional volume сопоставим US–CN внутри ряда несмотря на English bias
   и authorship inflation — используем только для объёмов, не для влияния.
4. Office-basis patent counts сопоставимы как «объёмы заявок» несмотря на home-bias
   и субсидии — используем только парой resident/total-office, не как INN.
5. HS8542-номинал сопоставим как «стоимости» несмотря на ревизии/re-exports/processing —
   тренд не читаем как технологический; CAGR поверх ревизий невалиден.
6. Лаг-1 GERD→TFP имеет экономический смысл за 1 год — **не обоснован**; показываем
   lag0/lag1/lag2 как чувствительность, структурного лага нет.
7. Country+year FE устраняют смешение — нет (только время-постоянные traits и общие шоки;
   time-varying omitted, reverse causality, измерение — остаются).
8. USA-константа безвредна для β — нет (потребляет dummy и 12 строк, сдвигает β;
   drop-USA β=0.0329 — чувствительность обязательна к упоминанию).
9. Отсутствие AI/HPC/quantum-панелей не смещает macro-выводы — предполагаем только
   при условии §1.3 (не обобщаем macro на tech).
10. Зрелость технологии классифицируема независимо от наблюдаемого bottleneck — иначе
    H2 circular (см. §9).

---

## 9. Запрещённые подмены + claims, встречающиеся один раз (disposition)

### 9.1. Девять подмен (подтверждены из technology_cases_final.md, расширены двумя)

| Подмена | Disposition |
|---|---|
| publication volume = scientific/AI leadership | Отвергнута: объём 2.17x — не влияние; impact-ряда нет |
| patent count = technological/design leadership | Отвергнута: 5.44x/2.68x counts при TFP 0.47; пик субсидий 2021; office-basis home-bias; triadic/PCT не собраны; IPF small-N |
| benchmark/frontier = economic leadership | Отвергнута: frontier-ряда нет; даже при наличии — не экономика |
| R&D spending/intensity = innovation success | Отвергнута: GERD→TFP неотличима от нуля; только ассоциация |
| manufacturing share/volume = total leadership | Отвергнута: MVA — доля, не абсолют; trade — номинальные стоимости с assembly-смещением |
| announced capacity/policy = actual production/effect | Отвергнута: CHIPS/анонсы — намерения/маркеры, не выпуск |
| supercomputer ranking = commercial AI capability | Отвергнута: TOP500 (HPL) ≠ hyperscale AI-compute ≠ cloud; ряда нет |
| AI capability = productivity gain | Отвергнута: AI-capability не измерена; TFP — агрегатный, не tech-TFP |
| government funding/program = successful commercialization | Отвергнута: NQI/MiC2025/CHIPS/BIS — маркеры; COM пуст; quantum-эффект ~0 |
| BERD level = private finance model (+ «частное финансирование США» как преимущество) | **Новая, отвергнута здесь**: BERD — PERFORMED-уровень, не модель; finance mix неизмерен (§3.2) |
| HS8542 nominal growth/CAGR = technological catch-up | **Новая, отвергнута здесь**: рост поверх HS-ревизий, карантина и цен — не технологический тренд |

### 9.2. Single-appearance claims (появляются один раз без evidence — удалены/понижены)

| Claim (где) | Решение |
|---|---|
| Абсолютные головы researchers «~1.2M→2.4M vs ~1.2M→1.6M» (final_synthesis F2) | **Удалено**: расчёта в панели нет (нужны population-ряды + FTE-допущения); joint-интенсивность — единственный допустимый ряд |
| «США выше по частному финансированию (BERD % GDP)» (final_synthesis §8 thesis) | **Переформулировано**: «США выше по BERD PERFORMED-интенсивности (уровень, не модель)» (§4, §6) |
| «США превращают… Китай — …» (tech_cases_comparison, одна строка) | **Удалено как causal**: заменено thesis §6 (описание измерений, без «превращают») |
| «KOR GERD 4.94% выше US/CN; KOR IC CAGR +6.5% vs JPN −0.9%» как fab-контекст | **Понижено**: только R&D/trade-контекст с годами/окнами, не fab-структура; без joint-таблицы не headlining |
| «Micius/NQI/MiC2025/Dual Circulation» как объяснения различий | **Только маркеры дат**, не объяснения; связь с исходами не утверждается |
| «GBR researchers ends 2019» (quant_reviewed/final_synthesis) | **Исправлено**: ends 2017 (§3.1); окна пересчитаны |
| «CAGR-пар 2.6%/6.8%, −1.1%/−1.7%, 0.4%/8.9%» без окон | **Помечены как несопоставимые окна**; валидны только common-window значения (§3.3) |
| Visual CHIPS/BIS-линии на F6/F8 как «изломы» | **Только vertical lines «не эффект»**; чтение излома как эффекта запрещено (§7) |

---

## 10. Limitations (кратко; полно — §3/§5 + data_quality_final.md)

MVD-панель мала (M1 n=84, K=20, df=64, G=7; ISR 0, GBR 7, USA 12-константа);
USA TFP=1 — константа (1994–2023); патенты — office-basis counts до 2021 (пик субсидий CN);
researchers — фрагментарны (GBR–2017, USA–2022, ISR 0; FTE/headcount);
hitech — broad basket + SITC-break (ряд с 2007); HS8542 — номинал + HS-ревизии +
processing/re-exports + карантин CHN 2015–17 + DEU/FRA 0; MVA — доля, не абсолют;
BERD — PERFORMED, винтажная смесь с WB-GERD; TiVA/VC/GVC — не собраны;
AI/HPC/quantum — missing; COM — пуст. Causal-язык запрещён
(allow-list: «ассоциировано», «условная корреляция», «дескриптивно»,
«неотличимо от нуля», «не измерено», «не тестируемо»).

Future work (без новых исследований сейчас): TCI-индекс по дизайну;
single-definition Comtrade-pull (multi-reporter, единая HS-агрегация);
Nov TOP500-pull (count+Rmax) + разделение 3 типов compute;
Stanford AI Index audited export (publications + private $; notable models — cross-section);
EPO–OECD quantum IPF CSV 2005–2024 вруч��ую; расширение панели до 15–20 стран;
sectoral TFP; отдельный finance-mix измеритель (financed, единый винтаж).

---

## Приложение A. Трассировка исправлений → issues (logic_changes.md IDs)

H1 (RQ unanswerable) → §1; H2 (H1 без TCI-теста) → §2/H1, §6;
H3 (H4 пост hoc) → §2/H4; H4 (finance unmeasured + паритет 77% отозван) → §2/H3, §3.2, §4/FIN, §5;
H5 (TFP-уровень ≠ tech-механизм; лаг) → §3.5, §5; H6 (trade→fab headlining) → §4, §5, §9.1;
H7 (предрешённый thesis №1) → §6; H8 (геополитика как findings) → §7;
H9 (office-basis ярлык) → §3.1, §4/INN; H10 (intensity/volume circular) → §3.4, §6.
M1 (головы без расчёта) → §8/п.2, §9.2; M2 (несопоставимые CAGR) → §3.3, §9.2;
M3 (GBR 2019→2017) → §3.1, §9.2; M4 (causal-глаголы) → §0-правило, §6, §9.2;
M5 (KOR/ISR single-appearance) → §9.2; M6 (HS-ревизии скрыты) → §3.1, §4/ADE, §9.1;
M7 (H2 circular зрелости) → §8/п.10, §2/H2; M8 (линии CHIPS/BIS как эффект) → §7, §9.2;
M9 (COM пуст, но FIN→COM) → §5; M10 (TFP catch-up как tech) → §3.5, §5, §6.

*Приоритет документов при расхождении: этот файл > regression_results_final.csv (числа M1) >
data_quality_final.md (определения/покрытие) > quant_reviewed.md / technology_cases_final.md
(интерпретационные запреты) > reports/*.md (старые формулировки).*

# Сравнительный анализ 4 технологических кейсов (агент 5)

Дата: 2026-09-13. Окно: 2010–2023 (патенты — до 2021). Панель: USA, CHN + KOR, JPN, DEU, GBR, ISR, FRA.
Вход: `research_design.md`, `data_map.md`, `results/*.csv`, `reports/analysis_report.md`, `reports/data_quality_report.md`.
Метод: TCI-блоки S/HC/RD/FIN/INN/COM/PRD/ADE (research design D.1). Только ассоциации, без causal claims.

> **SUPERSEDED / ARCHIVE / DO NOT CITE (2026-09-20).**  
> «H1 — partial macro» / H1–H4 «partial» в теле — **отозваны**. H1–H6 = archived / not tested.  
> **Не** использовать «одну строку для доклада» и не копировать causal verbs из тела.  
> **Актуальные authority:** `final_project.md`, `tech_framework_unified.md`, `tech_occupancy_matrix.md`, `defense_risks.md`, `RQ_FREEZE.md`.  
> `technology_cases_final.md` — **тоже SUPERSEDED** (не указывать как актуальное).

## 0. Что можно и нельзя утверждать (честный scope)

| Кейс | Количественное ядро в проекте | Статус tech-панели | Следствие |
|---|---|---|---|
| AI | Только макро-прокси: `scopus_articles`, `patents_resident`, `gerd/berd_pct_gdp`, `researchers_per_million` | `ai_publications_count`, `ai_private_investment`, `ai_notable_models` — **MISSING** (`data_quality_report.md`) | AI-специфичные выводы — только qualitative + внешние идентифицированные источники (Stanford AI Index 2025), без цифр из панели |
| Semiconductors | `semi_exports_hs8542` + `hitech_export_share` + `mva_pct_gdp` — **есть** | Fab capacity / advanced nodes — нет (SEMI платный, по data_map заменён trade + qual) | Единственный tech-кейс с количественным тестом; fab-стадии — qualitative |
| HPC | Нет | `hpc_top500_systems`, `hpc_top500_rmax` — **MISSING** (KeyError при сборе) | Только framework + различие трёх типов compute; цифр TOP500 из панели нет |
| Quantum | Нет | `quantum_ipf_count` (EPO–OECD Dec 2025) — идентифицирован, **не извлечён** | Только qualitative; экономический эффект ~0 по построению |

Общие ограничения (из агента 4, обязательны): TFP нормирован USA=1.0 каждый год (construction, не результат); pooled-корреляции — не evidence (композиционный артефакт); conversion ratios `patents/articles`, `hitech/GERD` — не рейтинг эффективности; event CHIPS/BIS — только маркеры; патенты = counts, статьи = volume≠impact.

---

## Кейс 1. Artificial Intelligence (3–5 показателей, без эссе)

Выбранные показатели: (1) scientific output — general articles как прокси + AI-публикации (missing); (2) research impact — missing; (3) private investment — missing; (4) frontier models — snapshot only; (5) adoption — missing.

Количественные якоря из панели (general, не AI-specific):
- Статьи (volume): CHN/USA 0.76 (2010) → 2.17 (2023), кроссовер ~2020; slopes +2.9k (USA) vs +48.3k/год (CHN), p<0.001. Источник: `descriptive_snapshot_US_CHN.csv`, `trend_slopes_convergence.csv`. Это **объём**, не влияние.
- Патенты-резиденты (counts): 1.21 → 5.44 (2021); CAGR 0.7% vs 15.5%. Источник: те же файлы. Quality caveat обязателен.
- FIN/RD: GERD 0.62→0.75; BERD 0.67→0.75; slopes параллельны (diff p=0.29). Источник: `descriptive_snapshot_US_CHN.csv`.
- HC: researchers/млн 0.25→~0.38–0.43; CAGR 2.6% vs 6.8%, но абсолютный прирост/год больше у США (+106 vs +82, p=0.07).

- **A. Где США сильнее:** R&D-интенсивность (% GDP) и HC-интенсивность (на млн); структура частного финансирования (BERD/GDP 2.66 vs 2.00 в 2023). Внешний qual-сигнал (не из панели, confidence ниже): private AI investment и frontier/notable models — по дизайну Stanford AI Index (Vibrancy Tool / AI Index 2025, `data_map.md` §2.1), где методология внутри индекса сопоставима, но покрытие CN слабее.
- **B. Где Китай сильнее:** абсолютные объёмы science/innovation-outputs (статьи, патенты — general); потенциальный масштаб adoption через manufacturing + downstream electronics (косвенно: MVA ~2.5x, HS8542-стоимость 3.13x — это не AI-adoption, а структурная предпосылка; прямое AI-adoption в панели не измерено).
- **C. Main bottleneck:** США — перенос innovation→PRD/scaling внутри страны (MVA-доля 10.5% vs 25.0% CHN) + зависимость от allied fabrication/compute supply chain; Китай — доступ к frontier compute и прозрачному частному финансированию (BIS Oct22/Oct23 как маркеры режима, не causal evidence) + конверсия объёма в impact (impact-ряд missing).
- **D. Main mechanism of economic advantage:** США — частный FIN → INN/COM (VC + BERD → стартапы/модели/облака); Китай — объёмы S/INN + PRD/scaling → быстрое удешевление и диффузия применений (механизм — qualitative, в панели тестируем только косвенно через M1: GERD-ассоциация с TFP слабая 0.028, CI включает 0).
- **E. Evidence:** `descriptive_snapshot_US_CHN.csv`, `descriptive_cagr.csv`, `trend_slopes_convergence.csv`, `regression_results.csv` (M1); missing-статус — `data_quality_report.md`; внешние источники-методики — `data_map.md` §2.1 (Stanford AI Index, doi 10.48550/arxiv.2504.07139).
- **F. Confidence:** MEDIUM для general science/finance gaps (HIGH-надёжность источников WDI/OECD, но прокси не AI-specific); **LOW / Insufficient** для research impact, private AI $, frontier models, adoption — цифр из панели нет, запрещены количественные вердикты.

Запрещённый вывод: «США/Китай сильнее в AI» без стадии — не делается. Допустимо только: «США — интенсивность R&D/HC и (внешний сигнал) private/frontier; Китай — объёмы outputs».

---

## Кейс 2. Semiconductors (разделить 7 стадий, не сводить к exports)

Выбранные показатели: (1) MVA % GDP (PRD macro); (2) HS8542-торговля (ADE); (3) high-tech export share (ADE broad); (4) патенты general + PCT-semis SHOULD (INN, второй — не собран); (5) fab/equipment-зависимости (qualitative).

Количественные якоря:
- MVA % GDP: 11.9/31.1 (2010) → USA 10.5 (2021) / CHN 25.0 (2023); обе доли падают (CAGR −1.1%/−1.7%). Источник: snapshot + CAGR.
- HS8542 номинал: CHN/USA 0.79 ($29.6/$37.7 млрд, 2010) → 3.13 ($136.4/$43.6 млрд, 2023); CAGR +1.1% vs +12.5%. **Карантин:** CHN 2015–17 отсутствует (multi-record); re-export/processing-trade смещение. Источник: snapshot, CAGR, `data_quality_report.md`.
- High-tech share: CHN +9.5 пп (2010) → +4.7 пп (2023); CHN падает −1.5%/год. Корзина широкая + break SITC Rev.4. Источник: те же + quality report.
- Event-маркер (не causal): pre 2020–21 vs post 2022–23: IC-экспорт USA −1.9%, CHN +7.2%; hitech USA +1.5 пп, CHN −3.6 пп; 2023 — общий спад (chip-downturn). Источник: `event_CHIPS_BIS_prepost.csv`.

Стадийная разборка (US vs CN, qual где нет ряда):

| Стадия | USA | China | Третьи страны | Evidence / Confidence |
|---|---|---|---|---|
| Chip design / IP | Сильнее (fabless-экосистема, архитектуры) — qual | Объёмы патентов, догоняющее проектирование — qual | UK (ARM-IP), TW/KR downstream-спрос | MEDIUM-LOW (нет firm-ряда; общий патент-ряд — не evidence качества) |
| EDA | Сильнее (концентрация инструментов) — qual, экспортный контроль как рычаг | Зависимость — qual bottleneck | — | LOW (ряда нет; BIS-маркер Oct22/23) |
| Equipment (в т.ч. EUV-литография) | Частично (сегменты), но ключевой рычаг — в руках союзников | Зависимость, bottleneck для advanced nodes — qual | **NL (ASML EUV), JPN** — критические узлы; TW/KR — спрос на оборудование | LOW-MEDIUM (нет SEMI-ряда; структура известна из отраслевых отчётов, в панели не тестируема) |
| Advanced fabrication (<10nm) | Слабее внутри страны (ре-шоринг через CHIPS Act — policy marker) | Слабее на frontier (bottleneck equipment), несмотря на инвестиции | **TWN, KOR — доминируют frontier foundry** (в панели: KOR IC-экспорт CAGR +6.5%, JPN −0.9% — косвенно, не мощность) | MEDIUM для факта концентрации вне US/CN (qual + trade-косвенность); LOW для точных долей мощности |
| Mature-node manufacturing | Присутствие, не доминанта | **Сильнее по масштабу** (MVA ~2.5x; IC-стоимость 3.13x — с assembly-смещением) | — | MEDIUM (MVA HIGH/MED-HIGH; trade HIGH для стоимостей, но ≠ мощности) |
| Packaging / assembly | Слабее по объёму | **Сильнее по объёму** (часть HS8542-стоимости — assembly, не frontier) | MYS и др. — OSAT-хаб (в data_map, не в панели) | MEDIUM-LOW (trade-структура + qual) |
| Downstream electronics | Сильнее в платформах/ПО/облаках — qual | **Сильнее в сборке/масштабе выпуска** (hitech share выше, хотя разрыв сузился) | — | MEDIUM (hitech MEDIUM; processing-trade caveat) |

- **A. Где США сильнее:** design/IP, EDA, отдельные сегменты equipment; платформы/облака как спрос на чипы (qual). Внутри-страновой frontier-fab — слабее, чем рычаг через союзников и контроли.
- **B. Где Китай сильнее:** масштаб mature-производства, packaging/assembly, downstream-сборка; стоимостные IC-экспорты (с оговоркой assembly≠fab-лидерство).
- **C. Main bottleneck:** Китай — equipment (EUV) + advanced fab (союзническая концентрация NL/JPN/TW/KR + BIS-контроли как маркеры); США — перенос design-лидерства во внутренний frontier-fab и packaging-масштаб (CHIPS Act — маркер, не evidence эффекта).
- **D. Main mechanism:** США (+союзники) — контроль узких upstream-звеньев (EDA/equipment/IP) → рента и рычаг; Китай — масштаб mature + сборка → доля в стоимостной торговле и снабжение downstream, но с импортной добавленной стоимостью (GVC-переменная SHOULD, в MVD не входит в топ-10 — взять из TiVA только как структурный qual).
- **E. Evidence:** snapshot/CAGR/event CSV выше + `data_quality_report.md` (trade≠fab, re-exports, разрыв 2015–17); стадии fab/EDA/EUV — `data_map.md` §2.2 + policy table (§3: `us_chips_act`, `us_bis_oct22/oct23`, `mic2025`).
- **F. Confidence:** MEDIUM для PRD-macro и торговых стоимостей; LOW для точных fab-долей и EDA/equipment-квантификации (рядов нет). Вывод «trade-лидерство = fab-лидерство» — запрещён.

---

## Кейс 3. Supercomputing / HPC (TOP500 + различие 3 типов compute)

Выбранные показатели: (1) TOP500 systems count; (2) aggregate Rmax; (3) различие supercomputer vs commercial AI compute vs general infrastructure (концептуально).

Статус: оба ряда **MISSING** в cleaned panel (`data_quality_report.md`: `hpc_top500_systems`, `hpc_top500_rmax_tflops` — 100% missing). Методика идентифицирована в `data_map.md` §2.3 (TOP500.org, Nov snapshot 2010–2025, HIGH reliability если собрать), но в этом проекте цифр нет — строить графики/рейтинги запрещено.

Поэтому только stage-логика (для будущего сбора):
- **Supercomputer performance (TOP500 Rmax/count, PRD):** state-led, dual-use, измеримо; лучший tech-ряд из четырёх при наличии. Без панели — no verdict.
- **Commercial AI compute (hyperscale training clusters):** в значительной части вне TOP500-листа (data_map риск-таблица) — TOP500 ≠ AI-compute; смешение этих двух — запрещённая ошибка.
- **General computing infrastructure (облака, дата-центры):** ближе к COM/ADE; в панели нет прокси.

- **A. Где США сильнее:** по дизайну кейса — связка frontier-системы + коммерческие облака/AI-compute (qual-гипотеза, требует TOP500 + AI Index compute narrative; в панели не тестируемо).
- **B. Где Китай сильнее:** масштаб госвложений и число систем в отдельные годы (qual-гипотеза; без Nov-снапшотов — no verdict). Единственный косвенный quant-якорь: GERD/HC-объёмы и MVA-масштаб как предпосылки, не evidence HPC.
- **C. Main bottleneck:** США — перевод peak-Rmax в широкую доступность compute (COM/ADE); Китай — доступ к frontier-чипам для compute (BIS-маркеры) + разрыв «пиковая мощность vs экосистема использования» (qual).
- **D. Main mechanism:** HPC — госфинансирование → PRD-мощность (state-led dual-use, research design §D.3); экономический эффект — косвенный (через науку/оборону/AI-обучение), не через TFP-панель (агрегатный TFP — не tech-TFP).
- **E. Evidence:** отсутствие рядов — `data_quality_report.md`; методика — `data_map.md` §2.3 (TOP500 Nov 2025 URL); policy-маркеры — `mic2025`, `us_bis_oct22` (не causal).
- **F. Confidence:** **Insufficient / LOW** для любых US–CN вердиктов по HPC. Единственный допустимый вывод: «панель не позволяет тестировать HPC-кейс; требуется Nov TOP500-pull + разделение трёх типов compute».

---

## Кейс 4. Quantum technologies (ранняя стадия; не преувеличивать экономику)

Разделить: (a) quantum computing; (b) quantum communication (Micius 2016 как S/RD-маркер); (c) quantum sensing (только если релевантно — здесь: упомянуть, не оценивать).

Выбранные показатели: (1) quantum IPF (EPO–OECD); (2) quantum publications (optional); (3) public funding / программы (NQI Act 2018 vs CN mega-emphasis — policy markers); (4) текущий экономический эффект ≈ 0 (по построению).

Статус: `quantum_ipf_count`, `quantum_publications` — **MISSING** (идентифицирован EPO–OECD «Mapping the global quantum ecosystem» Dec 2025, экстракция из чартов не выполнена — `source_registry.csv`). Qubit-milestones — только qualitative timeline (research design §E). Small-N волатильность — descriptive only.

- **A. Где США сильнее:** (qual-гипотеза) computing-экосистема: частное финансирование + связка университеты/стартапы/облака; IPF — проверить по EPO–OECD при извлечении, сейчас no verdict.
- **B. Где Китай сильнее:** (qual-гипотеза) quantum communication (спутник Micius, инфраструктурные демонстраторы) + масштаб гос-R&D как входа (GERD/HC-объёмы — косвенно, не quantum-specific).
- **C. Main bottleneck:** обе страны — наука→R&D→коммерциализация (ранняя стадия): для зрелости H2-ожидание «узкое звено = S/RD» — единственное, что согласуется с дизайном, но тестировать не на чем (H2 = insufficient по агенту 4).
- **D. Main mechanism:** пока нет механизма экономического преимущества — только задел (опционы): патенты/публикации/кадры → будущая COM. Приписывание TFP/экспорта кванту — запрещено (агрегатный TFP — не tech-TFP).
- **E. Evidence:** `source_registry.csv` (EPO–OECD URL) + `data_map.md` §2.4/§3 (`us_nqia` 2018, `cn_quantum_mega` 2016); отсутствие рядов — `data_quality_report.md`.
- **F. Confidence:** **LOW / Insufficient** для всех US–CN сравнений; допустим только qualitative mapping + план извлечения IPF 2005–2024.

---

## Единая сравнительная матрица (Technology × Stage × USA × China × Evidence × Confidence)

Легенда USA/China: `+` сильнее на стадии (по evidence), `~` паритет/смешанно, **`?` нет данных для вердикта** (недостаточно данных для `+`/`−`). Без указания стадии слова «сильнее» не употреблять.

| Technology | Stage (TCI) | USA | China | Evidence | Confidence |
|---|---|---|---|---|---|
| AI | S (output volume) | ~ (интенсивность ниже по объёму) | + (объём статей 2.17x, general) | snapshot; trend slopes | MEDIUM (прокси general, не AI-specific) |
| AI | HC / RD / FIN (inputs) | + (GERD 3.45 vs 2.58; BERD 2.66 vs 2.00; researchers/млн ~2.5x) | ~ (быстрый рост, но уровень ниже; slopes параллельны) | snapshot; CAGR; trend | HIGH-MEDIUM |
| AI | INN (patents volume) | ~ (counts ниже) | + (5.44x counts, **2021 = пик субсидий**) | snapshot; CAGR | MEDIUM (≠quality) |
| AI | COM frontier / private $ / adoption | **?** | **?** | **MISSING (100%); Stanford AI Index — идентифицирован, не извлечён** | **Insufficient** |
| Semis | INN design/IP/EDA | + | ~ | qual + policy markers | LOW-MEDIUM |
| Semis | PRD equipment / advanced fab | ~ (сегменты) + рычаг через союзников | bottleneck (зависимость) | qual; BIS/CHIPS маркеры | LOW-MEDIUM |
| Semis | PRD mature / packaging (scale) | ~ | + (MVA ~2.5x **= доля, не абсолют**) | MVA snapshot/CAGR | MEDIUM |
| Semis | ADE trade values | ~ ($43.6 млрд) | + ($136.4 млрд, 3.13x **номинал, assembly-смещ.**) | Comtrade HS8542 snapshot/CAGR | MEDIUM (≠fab; **nominal, processing trade**) |
| Semis | ADE sophistication | ~ (21.8%) | + (26.6%, но gap 9.5→4.7 пп, падение) | hitech snapshot/CAGR | MEDIUM (**SITC Rev.4 break**) |
| HPC | PRD peak (TOP500 count/Rmax) | **?** | **?** | **MISSING (KeyError)** | **Insufficient** |
| HPC | COM commercial AI compute | **?** | **?** | **нет ряда; TOP500≠cloud** | **Insufficient** |
| HPC | ADE general infra | **?** | **?** | **нет прокси** | **Insufficient** |
| Quantum | S/RD (IPF/pubs/funding) | **?** | **?** | **EPO–OECD не извлечён; NQI/Micius — маркеры** | **Insufficient/LOW** |
| Quantum | COM/PRD/ADE (экон. эффект) | ~0 | ~0 | по построению ранней стадии | LOW (допустимо как qual) |
| Cross-tech | Productivity (TFP macro) | **1.0 (construction, не результат)** | 0.47 (catch-up +0.076 за 13 лет) | snapshot; M1 (**GERD 0.028, CI∋0, p=0.06; HC 0.056, t раздут**) | MEDIUM для уровней; **LOW для causality** |

Источники колонки Evidence: `results/descriptive_snapshot_US_CHN.csv`, `descriptive_cagr.csv`, `trend_slopes_convergence.csv`, `event_CHIPS_BIS_prepost.csv`, `regression_results.csv`, `reports/data_quality_report.md`, `data/metadata/source_registry.csv`, `data_map.md` §2–3.

---

## ~~Что четыре кейса говорят о различиях моделей~~ (SUPERSEDED синтез — не цитировать)

1. ~~**Профиль, а не рейтинг (H1 — partial macro).**~~ **ОТОЗВАНО.** H1 = archived / not tested. Дескриптивный dual-scale паттерн → см. D1 в `final_project.md` / `RQ_FREEZE.md` (не «partial support»).
2. ~~**Зрелость сдвигает bottleneck (H2 — insufficient).**~~ **ОТОЗВАНО** как evidence; H2 archived. Occupancy/`?` → `tech_occupancy_matrix.md`.
3. ~~**Конверсия vs входы (H4 — partial…).**~~ **ОТОЗВАНО.** Conversion ratios DO NOT USE; H4 archived.
4. ~~**Финансовая структура — механизм… (H3).**~~ **ОТОЗВАНО.** BERD = PERFORMED, не finance mix; FIN=`?` (D2).
5. **Мир не бинарен: третьи страны — часть модели, не фон.** Semis-кейс это доказывает структурно: frontier-fab (TWN/KOR), EUV-оборудование (NL), материалы/оборудование (JPN). US–CN сравнение без них — misspecification. Косвенные следы в панели: KOR GERD 4.94% (выше US/CN), KOR IC-экспорт CAGR +6.5% vs JPN −0.9% — **косвенные прокси из панели, не fab-данные** (SEMI-ряда нет, утверждать структуру мощностей нельзя).
6. **Decoupling — маркеры, не эффект.** CHIPS Act + BIS Oct22/Oct23 лежат на изломе hitech-share (CHN −3.6 пп post vs USA +1.5 пп) при одновременном росте CHN IC-стоимости (+7.2%) и общем спаде 2023 — цикл, COVID-лаги, HS-агрегация и processing trade не позволяют causal чтения. Использование — только vertical lines (позиция агента 4, принимается).
7. **Что нужно, чтобы синтез стал тестом:** (i) Nov TOP500-pull 2010–2025 (count + Rmax, HIGH-надёжность); (ii) single-definition Comtrade HS8542-pull с устранением multi-record (CHN 2015–17); (iii) Stanford AI Index audited export (publications + private $ + notable-models snapshot как cross-section, не ряд); (iv) EPO–OECD quantum IPF-ручной CSV 2005–2024. До этого H2/H3/H5/H6 остаются insufficient/not tested, а «модельные» утверждения — **qualitative layer поверх macro-профиля, не evidence**.

**Одна строка для доклада (allow-list, 2026-09-20):** В joint-year срезах США выше по intensity-входам (GERD/BERD % GDP, researchers/mn), Китай — по volume/share поздних блоков (статьи/патенты-counts, MVA share, номинал HS8542); это **D1 dual-scale** (знаменательная арифметика), не organization model и не конверсия. AI/HPC/quantum и fab остаются `?` / qual (D2 occupancy); HS8542≠fab; TWN — qualitative hole; winner не объявляется. Актуальный текст: `final_project.md` §5–§10.

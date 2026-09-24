# Технологические кейсы — финальная проверенная версия (Technology Case Reviewer)

Дата: 2026-09-14. Окно панели: 2010–2023 (патенты — до 2021, researchers — с пропусками).
Панель: USA, CHN + KOR, JPN, DEU, GBR, ISR, FRA.
Вход: `reports/tech_cases_comparison.md`, `reports/analysis_report.md`, `reports/final_synthesis.md`,
`reports/data_quality_report.md`, `data_map.md`, `research_design.md`, `results/*.csv`.
Статус: исправленная версия после независимой проверки. Все регрессии — ассоциации, не causality.

> **SUPERSEDED / ARCHIVE note (2026-09-20, ResearchDesignAgent).**  
> Формулировка «H1 — partial macro» в синтезе кейсов — **stale / отозвана**. H1–H6 = **archived design / not tested**.  
> Актуальный RQ и D1–D2: `RQ_FREEZE.md`. Occupancy 8×4 — зона TechMatrixAgent. Методы: `APPROVED_METHOD_SET.md`.  
> Тело файла не переписывалось.

> ⛔ **DATA CANON / DO NOT CITE numbers (2026-09-20, DataCanonAgent).**  
> В теле ещё: BERD «business-financed»; BERD/GERD **~77%**; «кластер-SE невозможны».  
> Канон: BERD = **PERFORMED**; 77% отозван; cluster SE посчитаны; панель = **FRA не TWN**.  
> Читать: `DATA_CANON.md`. Тело не переписывалось.

Правило чтения: `+` — сильнее на данной стадии по evidence; `~` — паритет/смешанно/~0;
`?` — нет данных для вердикта. Метка **[expert assessment]** = тезис без ряда в панели,
ослабленный до качественной оценки. Без указания стадии слова «сильнее» не употреблять.

## 0. Честный scope: что измерено, а что нет (цепочка science → economic effect)

| Блок цепи | AI | Semiconductors | HPC / compute | Quantum |
|---|---|---|---|---|
| S (наука) | general articles есть; AI-публикации — MISSING | general articles (контекст, не semis-S) | нет | MISSING (EPO–OECD не извлечён) |
| HC | researchers/млн есть (general, не AI-кадры) | то же (general) | то же (не HPC-кадры) | то же |
| RD (GERD % GDP) | есть (general) | есть (general) | есть (general) | есть (general, не quantum-RD) |
| FIN | BERD есть (general); AI private $ — MISSING | BERD general; fab-финансы — нет | нет compute-финансирования | программы — только policy-маркеры |
| INN | патенты general; AI-патенты — нет | патенты general; PCT-semis — не собран | нет | IPF — MISSING |
| COM | frontier models — snapshot only, не ряд; стартапы/лицензии — нет | нет | нет (облака/кластеры — нет) | нет (≈0 по построению) |
| PRD/scaling | нет AI-compute ряда | MVA % GDP (macro-доля) + qual fab-разборка; SEMI-ряда нет | TOP500 — MISSING (KeyError) | нет (≈0) |
| ADE/adoption | adoption — MISSING | HS8542-стоимость + hitech share (с оговорками) | нет | нет (≈0) |
| Productivity | агрегатный TFP — не tech-TFP | то же | то же | то же |

Следствие: количественно тестируем только semis-trade + macro-контекст.
AI/HPC/quantum-вердикты US–CN — только `?` (insufficient) либо [expert assessment].
TFP нормирован USA=1.0 каждый год (construction, не результат; наклон USA ≈ 0 — шум на константе).

---

## Кейс 1. Artificial Intelligence

### 1.1. Что измеряют используемые ряды (и чего не измеряют)

- `scopus_articles` (WDI `IP.JRN.ARTC.SC`, 1996–2023, MEDIUM-HIGH): **объём** журнальных статей
  всех областей, fractional count. Не измеряет: AI-публикации, цитируемость, top-paper share.
  Сопоставимость US–CN внутри ряда — да; English/Scopus bias и authorship inflation — против CN-нейтральности.
  **Вывод: general-объём — не evidence AI-научного лидерства.** Использование — только macro-контекст.
- `patents_resident` (WIPO via WDI, до 2021, MEDIUM): **counts заявок резидентов**.
  Не измеряет: качество, triadic/PCT-семьи, AI-патенты. Пик CN-субсидий ~2021 смещает уровень вверх.
  **Counts ≠ технологическое лидерство.**
- `gerd_pct_gdp`, `berd_pct_gdp` (OECD MSTI, HIGH): **интенсивности** (% GDP), не абсолютные $.
  BERD — business-financed GERD, не VC и не AI-инвестиции. **R&D spending ≠ innovation success;
  government/private funding ≠ commercialization.**
- `researchers_per_million` (UNESCO/WDI, HIGH с оговорками): **интенсивность** кадров на млн жителей,
  не абсолютная численность и не качество. FTE/headcount и пропуски (USA 2023 n/a).
- MISSING и потому запрещены к количественным вердиктам: `ai_publications_count`,
  `ai_citations_impact`, `ai_private_investment_usd_bn`, `ai_notable_models` как ряд
  (`data_quality_report.md`: 100% missing). Внешняя методика идентифицирована, не извлечена:
  Stanford AI Index 2025 (doi 10.48550/arxiv.2504.07139) + Global AI Vibrancy Tool —
  внутри индекса сопоставимо, но покрытие CN private $ слабее (MEDIUM-LOW для CN).
  Notable models — только cross-section snapshot, не динамика.

### 1.2. Количественные якоря (только general-контекст, не AI-вердикт)

- Статьи (объём, все науки): CHN/USA 0.76 (2010) → 2.17 (2023), кроссовер ~2020;
  slopes +2.9k (USA) vs +48.3k/год (CHN), p<0.001. Evidence: `descriptive_snapshot_US_CHN.csv`,
  `trend_slopes_convergence.csv`. Confidence: MEDIUM для объёмов; **insufficient для AI-вывода**.
- Патенты-резиденты (counts): 1.21 (2010) → 5.44 (2021); CAGR 0.7% vs 15.5%. Quality caveat обязателен.
- GERD: 0.62→0.75 (2.71/1.68 → 3.45/2.58% GDP); BERD: 0.67→0.75 (1.85/1.24 → 2.66/2.00);
  slopes параллельны (diff p=0.29). **BERD/GERD ~77% в обеих странах (2023)** —
  нарратив «частный FIN США vs направленный FIN Китая» данными панели не подтверждается.
- Researchers/млн: 0.25 (2010) → ~0.34–0.43 (2021–2023, USA 2023 n/a);
  CAGR 2.6% vs 6.8%, абсолютный прирост/год +106 (USA) vs +82 (CHN), p=0.07.
  Per-million — выбор знаменателя в пользу США; по абсолютным головам картина иная (не тестируем).

### 1.3. Вердикты по цепочке (ослабленные)

- **A. Где США сильнее (измеримо):** только интенсивности входов general-R&D/HC
  (GERD/BERD % GDP, researchers/млн). Confidence: HIGH-MEDIUM. Это не AI-лидерство.
- **A-qual [expert assessment]:** private AI investment и frontier/notable models —
  внешний сигнал по дизайну Stanford AI Index в пользу США, но без извлечённого ряда
  вердикт запрещён; фиксируется как гипотеза, не evidence. Confidence: LOW / insufficient.
- **B. Где Китай сильнее (измеримо):** только абсолютные объёмы general-outputs
  (статьи, патенты-counts). Confidence: MEDIUM для объёмов; **не leadership**.
- **B-qual [expert assessment]:** масштаб быстрой диффузии применений через manufacturing/downstream —
  правдоподобный механизм, но AI-adoption в панели не измерен; MVA/HS8542 как «AI-adoption»
  запрещены (структурный контекст, не adoption). Confidence: LOW.
- **C. Bottleneck [expert assessment]:** США — перенос INN→PRD/scaling внутри страны
  (MVA-**доля** 10.5% vs 25.0% — это доля в GDP, не абсолютный выпуск; «масштаб ~2.5x» из доли
  логически невалиден) + зависимость от allied fabrication/compute; Китай — доступ к frontier compute
  и конверсия объёма в impact (impact-ряд missing; BIS Oct22/Oct23 — только маркеры режима, не evidence).
- **D. Mechanism [expert assessment, not tested]:** США — «частный FIN → INN/COM»,
  Китай — «объёмы S/INN + PRD/scaling → удешевление и диффузия». Регрессия finance→outputs
  не запускалась (лимит 2 моделей), pooled r=+0.16 — не evidence; BERD/GERD-паритет (~77%)
  противоречит сильной версии нарратива. Формулировка — только qual-гипотеза.
- **E. Evidence:** snapshot/CAGR/trend CSV + M1 (GERD-ассоциация 0.028, CI включает 0 — не AI-эффект);
  missing-статус — `data_quality_report.md`; методика внешних источников — `data_map.md` §2.1.
- **F. Confidence:** MEDIUM для general science/finance-уровней; **insufficient для любых
  AI-specific вердиктов** (impact, private $, frontier models, adoption, AI→productivity).

Запрещено: «США/Китай сильнее в AI» без стадии; «публикации/патенты = AI-лидерство»;
«benchmark/frontier = экономическое лидерство»; «AI capability = productivity gain»
(агрегатный TFP — не tech-TFP, связь не тестировалась).

---

## Кейс 2. Semiconductors (8 позиций: 7 стадий + третьи страны как сквозной узел)

### 2.1. Количественные якоря (только стоимости и macro-доли, не мощности)

- MVA % GDP (**доля, не абсолютный выпуск**): 11.9/31.1 (2010) → USA 10.5 (2021) / CHN 25.0 (2023);
  обе доли падают (CAGR −1.1%/−1.7%). Evidence: snapshot + CAGR. Confidence: MEDIUM-HIGH для долей;
  **LOW/запрет для выводов о fab-мощностях** (MVA — macro, не semis-VA).
- HS8542-номинал (USD, trade values, HIGH для стоимостей): CHN/USA 0.79 ($29.6/$37.7 млрд, 2010) →
  3.13 ($136.4/$43.6 млрд, 2023); CAGR +1.1% vs +12.5% **поверх разрыва CHN 2015–17
  (multi-record quarantine) — тренд смещён, читать с карантином**. Включает processing trade
  и re-exports (HK/SG); HS8542 ≠ advanced nodes (processors vs frontier).
  **Trade-лидерство ≠ fab-лидерство; announced capacity ≠ production.**
- High-tech export share (broad basket, MEDIUM): разрыв +9.5 пп → +4.7 пп; CHN −1.5%/год.
  **SITC Rev.4 break (Oct 2024, 28% missing) — trend over break невалиден.**
- Event-маркер (не causal, n=2 в ячейке, нет SE): pre 2020–21 vs post 2022–23:
  IC USA −1.9%, CHN +7.2%; hitech USA +1.5 пп, CHN −3.6 пп; 2023 — общий спад (chip-downturn).
  Evidence: `event_CHIPS_BIS_prepost.csv`. Использование — только vertical lines.

### 2.2. Стадийная разборка

| Стадия | USA | China | Третьи страны (bottleneck-узлы) | Evidence / Confidence |
|---|---|---|---|---|
| Chip design / IP | Сильнее (fabless-экосистема, архитектуры) [expert assessment] | Догоняющее проектирование; объёмы general-патентов — не evidence качества | UK (ARM-IP) как IP-узел; TW/KR — downstream-спрос | LOW-MEDIUM; firm-ряда нет |
| EDA | Сильнее (концентрация инструментов) [expert assessment]; экспортный контроль — рычаг, не мощность | Зависимость, bottleneck [expert assessment] | — (концентрация в США/союзниках, без квантификации в панели) | LOW; BIS — только маркеры |
| Equipment (в т.ч. EUV) | Отдельные сегменты; ключевой EUV-рычаг — **у союзников, не у США** | Зависимость, bottleneck для advanced nodes [expert assessment] | **NL (ASML EUV) — критический узел; JPN — материалы/оборудование** | LOW-MEDIUM; SEMI-ряда нет |
| Advanced fabrication (<10nm) | Слабее внутри страны; ре-шоринг (CHIPS Act) — **намерение/анонсы, не производство** | Слабее на frontier несмотря на инвестиции (bottleneck equipment) [expert assessment] | **TWN, KOR доминируют в frontier foundry** [expert assessment]; KOR IC-экспорт CAGR +6.5% vs JPN −0.9% — лишь trade-контекст, не мощность | MEDIUM для факта концентрации вне US/CN (qual); LOW для долей мощности; **анонсы ≠ выпуск** |
| Mature nodes | Присутствие, не доминанта масштаба | Сильнее по **масштабу зрелого производства** [expert assessment]; MVA-**доля** и IC-стоимость — лишь косвенный контекст с assembly-смещением | — | MEDIUM для macro-доли/trade; LOW для node-долей (ряда нет) |
| Packaging / assembly (OSAT) | Слабее по объёму внутри страны [expert assessment] | Сильнее по объёму [expert assessment]; часть HS8542-стоимости — assembly, не frontier | MYS и др. — OSAT-хабы (data_map, не панель) | MEDIUM-LOW; trade ≠ OSAT-мощность |
| Downstream demand (электроника, платформы, облака) | Сильнее в платформах/ПО/облаках как спрос на чипы [expert assessment] | Сильнее в сборке/масштабе выпуска; hitech share выше, но разрыв сузился (с SITC-break) | — | MEDIUM для hitech-стоимостей; LOW для «спроса на frontier-чипы» |
| Сквозной узел: третьи страны | Рычаг США — **через союзников** (EDA/IP + NL/JP-equipment + TW/KR-foundry), не автономно | Уязвимость CN — та же союзническая концентрация + BIS-контроли | **Без TW/KR/NL/JP сравнение US–CN — misspecification** | Qual-структура; квантификации fab-долей нет |

- **A/B (измеримо):** только macro-доля MVA и стоимостные IC/hitech-экспорты (см. §2.1 с карантинами).
  Всё про design/EDA/EUV/foundry-доли — [expert assessment], не evidence панели.
- **C. Bottleneck:** Китай — equipment (EUV) + advanced fab; США — перенос design-лидерства
  во внутренний frontier-fab и packaging-масштаб. CHIPS Act / BIS Oct22/Oct23 / MiC2025 —
  policy-маркеры, не evidence эффекта.
- **D. Mechanism [expert assessment]:** США (+союзники) — контроль узких upstream-звеньев
  (EDA/equipment/IP) → рента и рычаг; Китай — масштаб mature + сборка → доля в стоимостной торговле
  при импортной добавленной стоимости (TiVA SHOULD — только структурный qual, не тест).
- **E. Evidence:** snapshot/CAGR/event CSV + `data_quality_report.md`
  (trade≠fab, re-exports, карантин 2015–17, SITC-break); fab/EDA/EUV-стадии — `data_map.md` §2.2 + §3.
- **F. Confidence:** MEDIUM для PRD-macro и торговых стоимостей; LOW/insufficient для fab-долей
  и EDA/equipment-квантификации.

Запрещено: «manufacturing volume/IC-стоимость = total tech leadership»;
«announced fab capacity (CHIPS Act, корпоративные анонсы) = actual production»;
«патенты-counts = design-лидерство»; «R&D spending = innovation success».

---

## Кейс 3. HPC / compute (различать три типа; вердиктов нет)

Статус: `hpc_top500_systems`, `hpc_top500_rmax_tflops` — **MISSING 100%** (KeyError при сборе).
Методика идентифицирована (`data_map.md` §2.3: TOP500.org, Nov snapshot 2010–2025, HIGH если собрать),
но цифр в панели нет — графики/рейтинги запрещены.

### 3.1. Три разных сущности (смешение — запрещённая ошибка)

1. **Supercomputer performance (TOP500 count / aggregate Rmax, PRD):** state-led, dual-use, измеримо
   при наличии Nov-снапшотов. Но: Rmax = Linpack (HPL), не AI-нагрузка (HPCG/HPL-MxP);
   даже собранный TOP500 измеряет peak Linpack, не usable AI-compute и не экономический эффект.
   **Supercomputer ranking ≠ commercial AI capability; AI capability ≠ productivity gain.**
2. **Commercial AI compute (hyperscale training clusters, облака):** в значительной части **вне TOP500-листа**
   ( hyperscale-кластеры не заявляются в рейтинг). TOP500 ≠ cloud AI compute — смешение запрещено.
   В панели прокси нет.
3. **General computing infrastructure (облака, дата-центры, COM/ADE):** ближе к коммерциализации
   и внедрению; в панели не измерена.

Дополнительные угрозы сопоставимости US–CN (для будущего сбора):
неполное заявление китайских систем в TOP500 в последние годы (non-reporting bias);
различие «PRC vs China sites»; годовой срез — только Nov (не max за год без обоснования).

### 3.2. Вердикты

- **A/B:** любые «США сильнее в frontier+облаках / Китай сильнее в числе систем» —
  только **[expert assessment]-гипотезы**, в панели не тестируемы. Единственный косвенный
  quant-контекст (GERD/HC-объёмы, MVA-масштаб как предпосылки) — не evidence HPC. **No verdict.**
- **C. Bottleneck [expert assessment]:** США — перевод peak-Rmax в широкую доступность compute;
  Китай — доступ к frontier-чипам (BIS-маркеры) + разрыв «пиковая мощность vs экосистема использования».
- **D. Mechanism [expert assessment]:** HPC — госфинансирование → PRD-мощность
  (state-led dual-use, research design §D.3); экономический эффект — косвенный
  (наука/оборона/AI-обучение), не через агрегатный TFP (не tech-TFP).
- **E. Evidence:** отсутствие рядов — `data_quality_report.md`; методика — `data_map.md` §2.3;
  policy-маркеры — `mic2025`, `us_bis_oct22` (не causal).
- **F. Confidence:** **insufficient / LOW для любых US–CN вердиктов.**
  Допустимый вывод: «панель не позволяет тестировать HPC; требуется Nov TOP500-pull
  (count + Rmax) + разделение трёх типов compute + AI-compute narrative из AI Index».

---

## Кейс 4. Quantum technologies (ранняя стадия; экономика ≈ 0)

Разделять: (a) quantum computing; (b) quantum communication (Micius 2016 — S/RD-маркер);
(c) quantum sensing — упомянуть, не оценивать (ряда нет, релевантность для macro нулевая).

Статус: `quantum_ipf_count`, `quantum_publications` — **MISSING**
(EPO–OECD «Mapping the global quantum ecosystem», Dec 2025, 2005–2024 — идентифицирован
в `source_registry.csv`, экстракция из чартов не выполнена). Qubit-milestones — только qual-timeline
(research design §E): определения «кубита» несопоставимы. Small-N волатильность — только descriptive
при появлении ряда. Текущий макроэкономический эффект ≈ 0 **по построению ранней стадии**
(допустимо как qual-констатация, не оценка).

- **A/B — только [expert assessment]-гипотезы, no verdict:**
  США — computing-экосистема (частное финансирование + университеты/стартапы/облака);
  Китай — communication-демонстраторы (Micius, инфраструктура) + масштаб гос-R&D как входа
  (GERD/HC-объёмы — косвенно, не quantum-specific). IPF-проверка — только после ручного CSV 2005–2024.
  **Patent count ≠ technological leadership** (малые N, разные патентные режимы, волатильность);
  **government funding (NQI Act 2018 vs CN mega-emphasis) ≠ successful commercialization.**
- **C. Bottleneck:** обе страны — наука→R&D→коммерциализация (ранняя стадия).
  Ожидание H2 «узкое звено = S/RD» согласуется с дизайном, но тестировать не на чем (H2 insufficient).
- **D. Mechanism:** механизма экономического преимущества пока нет — только задел (опционы):
  патенты/публикации/кадры → будущая COM. Приписывание TFP/экспорта кванту запрещено.
- **E. Evidence:** `source_registry.csv` (EPO–OECD URL) + `data_map.md` §2.4/§3
  (`us_nqia` 2018, `cn_quantum_mega` 2016); отсутствие рядов — `data_quality_report.md`.
- **F. Confidence:** **LOW / insufficient для всех US–CN сравнений**; допустим только
  qualitative mapping + план извлечения IPF.

Запрещено: уверенные выводы о коммерческом и макроэкономическом эффекте;
«qubit-милстоун X = лидерство»; «финансирование программы = успех».

---

## Единая сравнительная матрица (Technology × Stage × USA × China × Evidence × Confidence)

| Technology | Stage (TCI) | USA | China | Evidence | Confidence |
|---|---|---|---|---|---|
| AI | S (output volume, general) | ~ (ниже по объёму) | + (объём статей 2.17x, general) | snapshot; trend slopes | MEDIUM (прокси general, не AI-specific) |
| AI | HC / RD / FIN (inputs, general) | + (GERD 3.45 vs 2.58; BERD 2.66 vs 2.00; researchers/млн ~2.5x интенсивность) | ~ (быстрый % рост, уровень ниже; slopes параллельны; BERD/GERD ~77% как у США) | snapshot; CAGR; trend | HIGH-MEDIUM для уровней; LOW для «модели финансирования» |
| AI | INN (patents volume, general) | ~ (counts ниже) | + (5.44x counts, 2021 = пик субсидий) | snapshot; CAGR | MEDIUM для counts; запрет quality-вывода |
| AI | COM frontier / private $ / adoption | ? | ? | MISSING 100%; Stanford AI Index — идентифицирован, не извлечён | Insufficient |
| Semis | INN design/IP/EDA | + [expert assessment] | ~ [expert assessment] | qual + policy markers | LOW-MEDIUM |
| Semis | PRD equipment / advanced fab | ~ (сегменты) + рычаг **через союзников** | bottleneck (зависимость) [expert assessment] | qual; BIS/CHIPS маркеры | LOW-MEDIUM |
| Semis | PRD mature / packaging (scale) | ~ | + [expert assessment] (MVA-**доля** и IC-стоимость — лишь контекст с assembly-смещением) | MVA snapshot/CAGR; trade values | MEDIUM для долей/стоимостей; LOW для node-долей |
| Semis | ADE trade values | ~ ($43.6 млрд) | + ($136.4 млрд, 3.13x номинал, assembly-смещ., карантин 2015–17) | Comtrade HS8542 snapshot/CAGR | MEDIUM (≠fab; nominal, processing trade) |
| Semis | ADE sophistication | ~ (21.8%) | + (26.6%, gap 9.5→4.7 пп, но SITC-break) | hitech snapshot/CAGR | MEDIUM (trend over break невалиден) |
| HPC | PRD peak (TOP500 count/Rmax) | ? | ? | MISSING (KeyError); TOP500≠AI-compute; Linpack≠AI-нагрузка | Insufficient |
| HPC | COM commercial AI compute | ? | ? | нет ряда; hyperscale вне листа | Insufficient |
| HPC | ADE general infra | ? | ? | нет прокси | Insufficient |
| Quantum | S/RD (IPF/pubs/funding) | ? | ? | EPO–OECD не извлечён; NQI/Micius — маркеры | Insufficient/LOW |
| Quantum | COM/PRD/ADE (экон. эффект) | ~0 | ~0 | по построению ранней стадии (qual) | LOW (допустимо как qual) |
| Cross-tech | Productivity (TFP macro) | 1.0 (construction, не результат) | 0.47 (catch-up +0.076 за 13 лет) | snapshot; M1 (GERD 0.028, CI∋0, p=0.06; HC t раздут) | MEDIUM для уровней; LOW для causality |

Источники колонки Evidence: `results/descriptive_snapshot_US_CHN.csv`, `descriptive_cagr.csv`,
`trend_slopes_convergence.csv`, `event_CHIPS_BIS_prepost.csv`, `regression_results.csv`,
`reports/data_quality_report.md`, `data/metadata/source_registry.csv`, `data_map.md` §2–3.

---

## Что четыре кейса говорят о различиях моделей (синтез, не 4 вывода)

1. **Профиль, а не рейтинг (H1 — partial macro / insufficient tech).**
   Устойчив только macro-паттерн: США — интенсивности входов, Китай — абсолютные объёмы
   outputs + доля PRD/ADE в измеримой части. Это разные измерения (per-capita/%GDP vs абсолют vs доли),
   гетерогенность предсказуема из знаменателей (население ×4.2, GDP-масштаб). Tech-зависимость смещения
   (ядро H1) — не тестируема: 3 из 4 tech-панелей пустые.
2. **Зрелость сдвигает bottleneck — гипотеза, не тест (H2 insufficient).**
   Структура согласуется с ожиданием (semis — PRD/scaling + upstream-зависимости;
   AI — FIN/COM-конверсия; HPC — peak vs usable; quantum — S/RD), но без tech-панелей это
   coherence с дизайном, не evidence.
3. **Конверсия vs входы (H4 — partial как гетерогенность, не рейтинг).**
   Разрывы разнородны (GERD 0.75 vs статьи 2.17 vs патенты 5.44 vs MVA-доля ~2.5x),
   что поддерживает идею «дело не только во входах». Ранжирование «эффективности» запрещено:
   знаменатели несопоставимы, качество не измерено, `conversion_ratios.csv` — не рейтинг.
4. **Финансовая структура — недоказанный механизм (H3 not tested).**
   BERD-интенсивность выше в США, но BERD/GERD ~77% в обеих странах — сильная версия
   «частный vs направленный» не подтверждается. Регрессия finance→outputs не запускалась;
   pooled r=+0.16 — не evidence. Только qual-гипотеза.
5. **Мир не бинарен: третьи страны — часть модели.** Semis структурно доказывает:
   frontier-fab (TWN/KOR), EUV (NL), материалы/оборудование (JPN). US–CN без них — misspecification.
   Панель даёт лишь косвенный контекст (KOR GERD 4.94%; KOR IC CAGR +6.5% vs JPN −0.9% —
   trade/R&D-контекст, не fab-данные).
6. **Decoupling — маркеры, не эффект.** CHIPS Act + BIS Oct22/Oct23 лежат на изломе hitech-share
   (CHN −3.6 пп post vs USA +1.5 пп) при росте CHN IC-стоимости (+7.2%) и общем спаде 2023 —
   цикл, COVID-лаги, HS-агрегация, processing trade и карантин 2015–17 запрещают causal чтение.
   Только vertical lines.
7. **Что нужно для теста:** (i) Nov TOP500-pull 2010–2025 (count + Rmax);
   (ii) single-definition Comtrade HS8542-pull с устранением multi-record;
   (iii) Stanford AI Index audited export (publications + private $; notable models — cross-section);
   (iv) EPO–OECD quantum IPF CSV 2005–2024 вручную. До этого «модельные» утверждения —
   qualitative layer поверх macro-профиля, не evidence.

**Одна строка для доклада:** США — интенсивные R&D/HC-входы (измеримо) и [expert assessment]
задел в INN/COM frontier; Китай — объёмы науки и доля зрелого PRD/scaling в торговом присутствии
(измеримо как стоимости/доли, не мощности); направление и величина смещения по AI/HPC/quantum
недоказуемы без tech-панелей, а frontier-узлы (EUV, advanced foundry, frontier AI-compute)
контролируются не бинарно, а через третьи страны и upstream-рычаги.

---

## Приложение: disposition по 9 запрещённым подменам

| Подмена | Решение в этом файле |
|---|---|
| publication volume = scientific leadership | Отвергнута: объём (2.17x) — не влияние; impact-ряда нет; AI-обобщение запрещено |
| patent count = technological leadership | Отвергнута: 5.44x counts при TFP 0.47; пик субсидий 2021; PCT/triadic не собраны; IPF small-N |
| benchmark leadership = economic leadership | Отвергнута: frontier/benchmark-ряда нет; даже при наличии — не экономика |
| R&D spending = innovation success | Отвергнута: GERD→TFP слаба и неотличима от нуля (β=0.028, CI∋0); только ассоциация |
| manufacturing volume = total leadership | Отвергнута: MVA — доля, не абсолют; trade — стоимости с assembly-смещением |
| announced capacity = actual production | Отвергнута: CHIPS Act/анонсы fab — маркеры намерения, не выпуск |
| supercomputer ranking = commercial AI capability | Отвергнута: TOP500 (HPL) ≠ hyperscale AI-compute ≠ cloud; ряда всё равно нет |
| AI capability = productivity gain | Отвергнута: AI-capability не измерена; TFP — агрегатный, не tech-TFP |
| government funding = successful commercialization | Отвергнута: NQI/MiC2025/CHIPS/BIS — маркеры; COM-блок пуст; quantum-эффект ~0 |

## Limitations (кратко; полно — `reports/final_synthesis.md` §7)

MVD-панель мала (7–8 стран, n=84 в M1, k=20, кластеров 7 — кластер-SE невозможны, HC1 игнорирует
автокорреляцию); USA TFP=1 — константа; патенты до 2021 (пик субсидий); researchers фрагментарны;
hitech — широкая корзина + SITC-break; HS8542 — номинал + processing trade + карантин 2015–17;
MVA — доля; TiVA — SHOULD/лаг; CN GDP revisions; AI/HPC/quantum — missing; COM-блок пуст.
Causal-язык запрещён («R&D повышает», «CHIPS/BIS снизили», «production вызывает export»,
«США/Китай конвертируют»).

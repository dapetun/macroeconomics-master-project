# Финальный синтез — США vs Китай: от ресурсов к производству и преимуществам

Дата: 2026-09-13. Статус: синтез агентов research-design → data-map → analysis (агент 4) → tech-cases (агент 5).
Окно: 2010–2023 (патенты — до 2021, researchers — с пропусками). Панель: USA, CHN + KOR, JPN, DEU, GBR, ISR, FRA.
Источники цифр: `results/descriptive_snapshot_US_CHN.csv`, `descriptive_cagr.csv`, `trend_slopes_convergence.csv`, `regression_results.csv`, `event_CHIPS_BIS_prepost.csv`, `key_findings.csv`; качество: `reports/data_quality_report.md`; графики: `figures/F1–F10`.

> ⛔ **SUPERSEDED / DO NOT CITE (2026-09-20, DataCanonAgent — усиление).**  
> Аудит-трейл 2026-09-13. **SynthesisAgent не должен опираться на числа/вердикты этого файла.**  
> Запрещено цитировать: H1 «Partially supported», H4 partial; BERD/GERD **~77%**; «кластер-SE невозможны»  
> (cluster SE есть в `regression_results_final.csv`); единственное articles-CAGR окно без пары;  
> GBR researchers «2019».  
> Канон данных: `DATA_CANON.md`. Актуальный синтез: `final_project.md`. RQ/D: `RQ_FREEZE.md`.  
> Тело **не** переписывалось.

> **SUPERSEDED / ARCHIVE (2026-09-20, ResearchDesignAgent).**  
> Аудит-трейл 2026-09-13. **Не цитировать** H-вердикты («H1 Partially supported», «H4 partial») — отозваны.  
> Актуальный синтез: `final_project.md`. Frozen RQ + D1–D2: `RQ_FREEZE.md`. Гипотезы: `reports/hypothesis_table.md`.  
> H1–H6 = archived design / not tested. Тело файла не переписывалось.

> **Дисклеймер, обязательный для всего документа:** AI / HPC / quantum рядов в cleaned panel нет (MISSING 100%), HPC TOP500 не собран, HS8542 по Китаю имеет разрыв 2015–2017. TFP — агрегатный PWT `ctfp`, нормированный USA=1.0 каждый год (**construction, не результат**; USA=1 each year — это не оценка производительности, а нормировка; OLS-наклон USA TFP = −3.6e⁻¹⁷, p=0.098 — шум на константе, **trend USA TFP не интерпретируется**). Все регрессии — ассоциации, не causality. **Сравнение интенсивностей (%GDP) с абсолютными объёмами (статьи/патенты) — это сопоставление разных измерений, а не рейтинг; гетерогенность разрывов предсказуема из разницы знаменателей (население, GDP).** Конвергенция ratio ≠ конвергенция уровней (абсолютный разрыв GDP pc вырос). Это уровень домашнего задания магистратуры, не статьи.

---

## 1. Executive conclusion

США и Китай демонстрируют разную конфигурацию **различий** вдоль цепочки Science → Productivity, а не общий рейтинг «кто сильнее». США устойчиво выше по **интенсивностям входов** — GERD 3.45 vs 2.58% GDP и BERD 2.66 vs 2.00% в 2023, исследователи на млн ~2.5x — при параллельных трендах без полного закрытия разрыва. Китай выше по **абсолютным объёмам** науки/инноваций — статьи CHN/USA 0.76 (2010) → 2.17 (2023) с кроссовером ~2020, патенты-резиденты 1.21 → 5.44x (2021) — и в **масштабе** manufacturing/trade — MVA-доля ~2.5x, IC-экспорт 0.79 → 3.13x в номинале. Разрывы гетерогенны по стадиям (GERD 0.75 vs статьи 2.17 vs патенты 5.44), что согласуется с идеей «дело не только во входах», но **ранжировать эффективность конверсии запрещено** — знаменатели несопоставимы (%GDP vs абсолютные количества), качество патентов/статей не измерено, conversion ratios в `conversion_ratios.csv` — не использовать как рейтинг. Связь ресурсов с агрегатным TFP слабая и хрупкая (M1: GERD +1 пп ↔ +0.028 TFP-пункта, **CI включает 0** [−0.0005, 0.0554], p=0.059 — на 5% неотличимо от нуля), медленный TFP catch-up Китая 0.395 → 0.471 — это уровни, не доказательство механизма. Технологическая зависимость профиля (ядро H1) **недоказуема**: из 4 кейсов количественно тестируем только semis-trade, AI/HPC/quantum — insufficient data. Геополитически значим только один структурный факт: frontier-узлы semis (EUV, advanced foundry, EDA) сконцентрированы вне бинарной пары US–CN, а поздний масштаб Китая — в mature-звеньях и сборке.

## 2. Main findings

### F1. Асимметрия «интенсивность vs объём» — единственный устойчивый macro-паттерн
- **Claim:** США выше по **интенсивностям входов** (%GDP, per-capita), Китай — по **абсолютным объёмам** outputs и **масштабу** PRD/ADE.
- **Evidence:** GERD CHN/USA 0.62 → 0.75; BERD 0.67 → 0.75 (`descriptive_snapshot_US_CHN.csv`, F1/F9); статьи 0.76 → 2.17, кроссовер ~2020 (F3); патенты 1.21 → 5.44x в 2021 (F4, log-scale); MVA-доля ~2.4–2.6x в пользу Китая (F5); IC-экспорт 0.79 → 3.13x (F8).
- **Interpretation:** Это **разные измерения** (интенсивности vs абсолютные объёмы vs доли), а не «рейтинг потенциала». Сравнение GERD (%GDP, bounded 0–6%) со статьями (абсолютные, масштабированы населением ×4.2) — **denominator artefact**: гетерогенность разрывов предсказуема из демографии и масштаба GDP, а не из «эффективности». **MVA % GDP — это доля, не абсолютный выпуск**; «масштаб ~2.5x» из доли логически невалиден (для абсолютного MVA нужен номинальный GDP). Описательно: интенсивности — США; объёмы+масштаб — Китай; ранжирование запрещено.
- **Confidence:** MEDIUM-HIGH для уровней (источники HIGH: OECD MSTI, WDI, Comtrade для стоимостей); **LOW для «рейтинга» или «конверсии»** (качество outputs не измерено, знаменатели несопоставимы).

### F2. Human capital: относительная конвергенция при абсолютной дивергенции
- **Claim:** Китай быстро догоняет в % терминах, но абсолютный разрыв в исследователях на млн вырос.
- **Evidence:** Researchers/млн: 3644/899 (0.25) в 2010 → ~4900/1686 (0.34) в 2021, 2107 у Китая в 2023 при USA n/a; CAGR 2.6% vs 6.8%; slopes +106 vs +82 чел/млн в год, diff p=0.07 (`trend_slopes_convergence.csv`, F2).
- **Interpretation:** Типичная ловушка «% рост = догоняет». В уровнях США добавляют больше в абсолюте каждый год. **Важно: researchers_per_million — это per-capita интенсивность, не абсолютная численность**; по абсолютным головам Китай, вероятно, уже впереди (~1.2M vs ~1.3M в 2010, ~1.6M vs ~2.4M в 2021 по оценке), но per-million знаменатель (население) **выбирает показатель, где США выигрывают** — это не «качество», а выбор denominator. Тезис «CN quantity, US quality» по количеству частично виден, по качеству — не тестируем (нет top-paper/citation ряда в panel).
- **Confidence:** MEDIUM-HIGH (UNESCO/WDI HIGH, но FTE/headcount и пропуски ISR/TWN).

### F3. Патенты и статьи — объёмы, не лидерство
- **Claim:** Интерпретация «патенты = инновационное лидерство» отвергается; «чистое лидерство США в науке» не подтверждается по объёмам.
- **Evidence:** Патенты-резиденты CHN/USA 5.44x (**2021** — пик китайских патентных субсидий; до 2022 субсидии снижены, данные после 2021 могут отличаться) при TFP 0.47 и оговорке WIPO (counts≠quality); статьи 2.17x при отсутствии impact-ряда; pooled-корреляция патенты–TFP −0.64 — композиционный артефакт, не evidence (`correlations_pooled.csv` — не использовать).
- **Interpretation:** Это прямое противоречие двум исходным тезисам из research design §«Спорные тезисы» (№7 и №5-част.). Conversion ratio «патенты/1000 статей» (USA 556 vs CHN 1887) отражает пропенсию/субсидии, не эффективность — **запрещён как рейтинг** (`conversion_ratios.csv` — не использовать).
- **Confidence:** HIGH для запрета интерпретации (методологически robust); MEDIUM для уровней counts (год = пик субсидий).

### F4. Manufacturing: персистентная доля Китая на фоне общего сдвига к услугам
- **Claim:** Доля MVA выше у Китая ~2.5x, но обе доли падают; это структура, не «деиндустриализация».
- **Evidence:** MVA % GDP: 11.9/31.1 (2010) → USA 10.5 (2021) / CHN 25.0 (2023); CAGR −1.1%/−1.7%; slopes −0.14 vs −0.51 пп/год, diff p<0.001 (F5).
- **Interpretation:** По цепочке PRD/scaling — **доля** Китая выше в зрелых производствах. **Важно: MVA % GDP — это доля в GDP, не абсолютный выпуск**; для абсолютного MVA нужен номинальный GDP (MVA_abs = MVA_pct × GDP). «Масштаб ~2.5x» из доли — логическая ошибка; в абсолютном выражении разрыв может быть другим. MVA — macro, не semis-capacity и не high-tech VA. Падение обеих долей — структурный сдвиг, быстрее с высокого уровня Китая.
- **Confidence:** MEDIUM-HIGH (UNIDO/WB MED-HIGH; лаг 1–2 года; не high-tech specific).

### F5. Экспорт: sophistication gap сужается, стоимостные IC-экспорты дивергируют — но это не fab-лидерство
- **Claim:** High-tech share: разрыв +9.5 пп → +4.7 пп (сужение); HS8542-номинал: CHN/USA 0.79 ($29.6/$37.7 млрд) → 3.13 ($136.4/$43.6 млрд).
- **Evidence:** `descriptive_snapshot_US_CHN.csv`; CAGR IC +1.1% vs +12.5%; hitech CAGR −0.3% vs −1.5%; event pre/post 2020–21 vs 2022–23 (**n=2 в каждой ячейке, нет SE**): hitech USA +1.5 пп, CHN −3.6 пп; IC USA −1.9%, CHN +7.2% при общем спаде 2023 (chip-downturn) — `event_CHIPS_BIS_prepost.csv` (F6/F8 с линиями CHIPS/BIS как маркерами).
- **Interpretation:** Противоречие тезису «decoupling уже виден однозначно»: hitech-share падает у Китая, IC-стоимость растёт — цикл, processing trade, HS-агрегация и разрыв CHN 2015–17 не позволяют causal чтения. **IC-экспорт номинален в USD** (3.13x) — включает processing trade и re-exports через HK/SG; HS8542 ≠ advanced nodes (processors vs frontier). High-tech корзина широкая + **SITC Rev.4 break** (Oct 2024, 28% missing) — trend over break невалиден. Вывод «trade-лидерство = fab-лидерство» **запрещён** (assembly-смещение, re-exports).
- **Confidence:** MEDIUM для стоимостей (Comtrade HIGH для values, но nominal); **LOW для fab-выводов** (SEMI-ряда нет).

### F6. Productivity: медленный catch-up уровней при слабой связи с текущими R&D
- **Claim:** TFP CHN 0.40 → 0.47 от США за 13 лет; GERD-ассоциация мала и неотличима от нуля на 5%.
- **Evidence:** M1 (FE + year FE, n=84, k=20, R²=0.992 **движим FE, прежде всего USA=1-константой**): β GERD_lag1 = 0.0275, SE 0.0143, **CI [−0.0005, 0.0554] включает 0**, p=0.059 (**на 5% неотличимо от нуля**); θ logRes = 0.0563, SE 0.0043, **t=13.1 раздут автокорреляцией** (HC1 игнорирует серийную корреляцию; реальная неопределённость больше) (`regression_results.csv`, `model1_tfp_gerd_hc_FE_coef.csv`); within-корреляция GERD–TFP +0.08–0.15; GDP pc ratio 0.175 → 0.305, **но абсолютный разрыв вырос $49k → $52k** (ratio-конвергенция ≠ конвергенция уровней); slopes GDP pc +$1099 vs +$933/год, diff p=0.01 (F7).
- **Interpretation:** Даже точечная β экономически мала: закрыть TFP-разрыв 0.53 одним GERD потребовало бы +19 пп — абсурд. TFP движут не текущие GERD. HC-ассоциация статистически «сильнее» (t=13.1), но **t раздут** (HC1, кластеров 7, кластер-SE невозможны); экономически мала в годовом выражении (+10% researchers ↔ +0.0054 TFP-пункта). **USA TFP=1 каждый год — константа; USA не дают within-вариации исхода, идентификация на 6 странах + CHN**.
- **Confidence:** MEDIUM для уровней catch-up; **LOW для каузальной интерпретации (запрещена)**; M2/PCA — **не использовать** (γ=−0.118 артефакт смешения масштаба, loadings art −0.36).

### F7. Технологическая гетерогенность — гипотеза, не тест
- **Claim:** Структура согласуется с ожиданием «зрелая semis → bottleneck в PRD/scaling; ранний quantum → в S/RD; AI/HPC — промежуточно», но доказательств из панели нет.
- **Evidence:** Единственный tech-тест — semis-trade (см. F5). AI/HPC/quantum панели пустые (`data_quality_report.md`: все AI/quantum 100% missing; HPC KeyError). Стадийная разборка semis (design/IP/EDA/equipment/advanced fab/mature/packaging/downstream) — только qual + policy-маркеры (`tech_cases_comparison.md`).
- **Interpretация:** Это coherence с дизайном (H2-логика), **не evidence**. Любое заявление «H2/H5/H6 доказаны» — запрещено. Честный план добора: Nov TOP500-pull, single-definition Comtrade-pull, Stanford AI Index audited export, EPO–OECD quantum IPF CSV. **В tech-матрице (§3) для AI/HPC/quantum стадий с insufficient data используется `?` (нет данных), не `+`/`−`**.
- **Confidence:** **Insufficient / LOW** для всех AI/HPC/quantum вердиктов; MEDIUM-LOW для qual-разборки semis.

## 3. USA vs China matrix

| Stage | USA | China | Evidence | Caveat |
|---|---|---|---|---|
| **Science (объём статей)** | Ниже по объёму с ~2020 (431k vs 933k в 2023) | Выше по объёму (2.17x), кроссовер ~2020, slope +48k/год vs +2.9k | snapshot; trend_slopes; F3 | Volume≠impact; Scopus coverage, English bias; не field-specific |
| **Human capital** | Выше интенсивность (~2.5x на млн), +106/год в абсолюте | Быстрый % рост (6.8%/год), уровень ~0.38 от США, +82/год | snapshot; CAGR; trend p=0.07; F2 | FTE/headcount; пропуски; quality не измерена |
| **R&D (GERD % GDP)** | Выше (3.45 vs 2.58), параллельный рост +0.072 пп/год | Ниже (0.75 от США), +0.062 пп/год, diff n.s. p=0.29 | snapshot; trend; F1 | CN GDP revisions меняют ratio; Frascati-дрейф |
| **Finance (BERD % GDP, mix)** | Выше (2.66 vs 2.00), BERD/GERD ~77% — **как у Китая** (qual-механизм «частный FIN → INN/COM» не подтверждается данными) | Ниже (2.00), BERD/GERD ~77% — **как у США** (qual-механизм «направленный FIN → PRD/scaling» не подтверждается данными) | snapshot F9; BERD–hitech pooled r=+0.16 — не evidence | **BERD/GERD ratio ~77% для обеих стран; «частный vs направленный finance» — narrative, не данные**; регрессия finance→outputs не запускалась; CN private $ opaque; VC-ряд missing |
| **Innovation (патенты)** | Ниже по counts (262k vs 1427k в 2021) | Выше по counts (5.44x) | snapshot; CAGR 0.7% vs 15.5%; F4 log | Counts≠quality; subsidies, utility models; PCT-subset не собран |
| **Manufacturing (MVA)** | Ниже доля (10.5%), −1.1%/год | Выше доля (25.0%, ~2.5x), −1.7%/год | snapshot; CAGR; trend; F5 | Macro, не high-tech VA и не fab capacity |
| **Scaling (зрелые мощности, packaging)** | Слабее масштаб mature/packaging внутри страны; ре-шоринг — policy marker | Сильнее масштаб mature/packaging | MVA + IC-стоимость косвенно; qual | Нет SEMI fab-ряда; trade≠мощности |
| **Adoption (внедрение)** | Сильнее платформы/облака/COM-экосистема (qual) | Сильнее масштаб диффузии через downstream-сборку (qual, косвенно) | hitech/MVA косвенно; нет прямого adoption-ряда | Adoption в панели не измерен; AI-adoption missing |
| **Exports** | Hitech 21.8%; IC $43.6 млрд | Hitech 26.6% (gap 9.5→4.7 пп); IC $136.4 млрд (3.13x) | snapshot; event pre/post; F6/F8 | Broad basket + SITC-break; processing trade; CHN 2015–17 missing; 2023 downturn |
| **Productivity** | TFP=1.0 (**construction, не результат**); GDP pc $74.4k | TFP 0.47 (catch-up +0.076 за 13 лет); GDP pc $22.7k (ratio 0.305), **абс. разрыв вырос $49k→$52k** | snapshot; M1 (β=0.028, **CI∋0, p=0.06**); F7 | **Агрегатный TFP, не tech-TFP; USA=1 — константа; ratio-конвергенция ≠ конвергенция уровней; causality запрещена** |
| **Technological resilience** | Рычаг через upstream (design/IP/EDA) + союзники (EUV NL, оборудование JP, foundry TW/KR); уязвимость — внутренний frontier-fab/packaging масштаб | Уязвимость — equipment (EUV) + advanced fab; устойчивость — mature-масштаб + downstream | Qual-разборка semis; policy-маркеры CHIPS/BIS/MiC2025 | Нет квантификации fab-долей; BIS/CHIPS — маркеры, не эффект; GVC-переменная TiVA — SHOULD, лаг |

## 4. Проверка гипотез

Шесть проверок (H1–H6 из research design; в ТЗ требовались H1–H5 — H6 добавлен как обязательный из дизайна):

| H | Формулировка (кратко) | Вердикт | Основание (1 строка + файл) |
|---|---|---|---|
| **H1** | Разный профиль сильных/слабых звеньев; смещение зависит от технологии | **Partially supported (macro) / Insufficient (tech-часть)** | Macro-профиль асимметричен (входы per-capita — США; объёмы+PRD/ADE — Китай), **но tech-зависимость 4 кейсов не тестируема** — нет AI/HPC/quantum панелей; **TCI-индекс не построен** (tci_scores.csv отсутствует), H1 «partially supported» — по дескриптивам, не по preregistered test (`descriptive_snapshot_US_CHN.csv`, F1–F8) |
| **H2** | Зрелость технологии определяет узкое звено | **Insufficient evidence** | Нужны 4 tech-панели; есть только semis-trade (`tech_panel.csv` AI/quantum пустые) |
| **H3** | Finance mix → stage outputs | **Not tested / Insufficient evidence** | Вне лимита 2 моделей; дескриптивно BERD–hitech r=+0.16 — не evidence; **BERD/GERD ratio ~77% для обеих стран** — «частный vs направленный» narrative, не данные (`correlations_pooled.csv`) |
| **H4** | Разрыв меньше во входах, чем в PRD/export; дело в конверсии | **Partially supported (как гетерогенность разрывов, не рейтинг эффективности)** | Разрывы разнородны (GERD 0.75 vs статьи 2.17 vs патенты 5.44 vs MVA ~2.4x — но MVA = доля, не абсолют); **эффективность не ранжируется** (знаменатели несопоставимы, качество не измерено); `conversion_ratios.csv` — **не использовать как рейтинг** |
| **H5** | Export лучше объясняется production, чем science | **Insufficient evidence** | Pooled r (MVA–hitech 0.40 > articles–hitech 0.12) between-смещён; export-регрессии нет; корзина hitech широкая + SITC Rev.4 break |
| **H6** | Innovation–commercialization gap различается по странам и tech | **Insufficient evidence** | Блок COM пуст (нет startups/licenses/revenue); gap-index не построен |

Ответы на 6 контрольных вопросов из ТЗ:
1. **Поддержаны полностью** — ни одна (нет H со статусом Supported; это честный результат при данных MVD; **TCI-индекс не построен — H1 частично по дескриптивам, не по индексу**).
2. **Частично** — H1-macro и H4-гетерогенность (см. выше; **H4 переопределена пост hoc как гетерогенность разрывов, не как тест конверсии** — исходная формулировка «разрыв меньше во входах» операционализирована как comparison ratios, что не требует regression).
3. **Не подтверждены как Rejected** — ни одна не отвергнута в сильном смысле (нет теста с мощностью для rejection); ближайшие к «не подтверждается» — интерпретации «патенты=лидерство» и «чистое лидерство США в науке по объёмам» (отвергнуты как интерпретации, не как H).
4. **Противоречия исходным тезисам:** (a) патенты 5.44x при TFP 0.47 — против «патенты=лидерство»; (b) кроссовер статей ~2020 — против «чистого лидерства США в науке»; (c) hitech-share CHN падает при росте IC-стоимости — против однозначного «decoupling уже виден».
5. **Устойчивы к разным показателям:** асимметрия интенсивность/объём (видна в GERD+BERD+researchers vs articles+patents+MVA+IC); падение MVA-долей обеих стран (два источника UNIDO/WB); медленный TFP catch-up (PWT) при росте GDP pc ratio и росте абсолютного GDP pc разрыва — **ratio-конвергенция при дивергенции уровней** ($49k→$52k).
6. **Слабые доказательства:** всё про AI/HPC/quantum; всё про finance→outputs causality (**BERD/GERD ~77% для обеих — «частный vs направленный» не подтверждается**); всё про «эффективность конверсии»; всё про эффект CHIPS/BIS; всё про fab-доли и EDA/equipment-квантификацию.

## 5. Main economic mechanism

Язык — только ассоциативный. Для каждого канала: что показывает анализ, чего не показывает.

- **Productivity.** M1: слабая положительная ассоциация GERD_{t−1} (+1 пп ↔ +0.028 TFP-пункта, **CI [−0.0005, 0.0554] включает 0, p=0.059 — на 5% неотличимо от нуля**) и более сильная статистически, но малая экономически ассоциация HC (+10% researchers ↔ +0.0054 TFP-пункта, **t=13.1 раздут HC1-автокорреляцией**). Within-корреляции согласуются (GERD–TFP ~0.08–0.15, HC ~0.29–0.49 после demeaning). Вывод: текущие R&D-интенсивности **не объясняют** TFP-разрыв 0.53; приписывать TFP кванту/AI/semis из этой панели запрещено (агрегатный TFP, не tech-TFP). **Механизм «R&D → TFP» в проекте не идентифицирован** — только уровни catch-up (0.40→0.47); **causal-язык запрещён**.
- **Capital formation.** Прямо не тестировался (нет capital stock decomposition, нет sectoral investment рядов; PWT-переменные капитала не использовались в M1/M2). Косвенно: **BERD/GERD ratio ~77% для обеих стран** — «частный vs направленный finance» **не подтверждается данными**; narrative о различии моделей финансирования остаётся qual-гипотезой. MVA-доля Китая ~2.5x — это доля в GDP, не абсолютный выпуск. Утверждать эффект нельзя.
- **Manufacturing.** Дескриптивно: масштаб MVA Китая ~2.5x при снижении обеих долей. Механизм «объёмы S/INN + направленный FIN → масштаб mature-производства и packaging» — qual, согласуется с F4–F5, но без fab-ряда и без регрессии PRD на FIN/RD это не тест. Вклад semiconductors в MVA не выделен (MVA — macro).
- **Exports.** Дескриптивно: hitech sophistication gap сужается, IC-стоимости дивергируют в пользу Китая с assembly-смещением. Механизм «PRD/scaling → торговое присутствие в зрелых звеньях при импортной добавленной стоимости» — qual (TiVA-переменная SHOULD, не в MVD-ядре). H5 (production лучше предсказывает export, чем science) не протестирована — утверждать нельзя; pooled r не evidence.
- **Long-run growth.** Не оценивается (нет growth-регрессии; GDP pc — только уровни/тренды: ratio-конвергенция 0.175→0.305 при росте абсолютного разрыва). Связка «технологический профиль → темп роста» требует sectoral TFP decomposition и causal design — явно out of scope (research design §J). Любой вывод «модель X даёт более высокий рост» — запрещён.
- **Economic resilience.** Единственный обоснованный qual-механизм через bottlenecks: США (+союзники) — устойчивость через контроль upstream-узлов (EDA/IP/equipment) и уязвимость через отсутствие внутреннего frontier-fab/packaging масштаба; Китай — устойчивость через mature-масштаб/downstream и уязвимость через EUV/advanced fab зависимость. GVC-измерение (TiVA foreign VA share) в cleaned panel не доведено до теста — только структурная интерпретация. Количественной оценки resilience нет — так и фиксируем.

Итог механизма одной строкой: измеримая часть проекта показывает *где* различаются уровни и тренды, но не *насколько* один этап вызывает другой; механизмы PRD/scaling→trade и FIN→INN/COM — правдоподобные qual-нарративы, совместимые с дескриптивами, но не оценки эффектов.

## 6. Geopolitical implications

Только то, что следует из bottlenecks и GVC-структуры, без causal claims по санкциям:

1. **Мир не бинарен — это главный геополитический вывод.** Frontier-узлы semis находятся в третьих странах: EUV-оборудование (NL), материалы/оборудование (JP), frontier foundry (TWN/KOR). US–CN сравнение без них — misspecification; любая стратегия «только US vs CN» игнорирует вето-игроков. Косвенный след в панели: KOR GERD 4.94% выше US/CN, KOR IC-экспорт CAGR +6.5% vs JPN −0.9%.
2. **Рычаг США — upstream, а не масштаб.** Контроль EDA/IP/отдельных сегментов equipment даёт ренту и рычаг экспортного контроля (BIS Oct22/Oct23 как маркеры режима), но не заменяет внутренний frontier-fab/packaging масштаб (CHIPS Act — маркер намерения, не evidence эффекта).
3. **Рычаг Китая — mature-масштаб, а не frontier.** Доминирование в mature-производстве, packaging/assembly и downstream-сборке даёт долю в стоимостной торговле (3.13x IC), но с импортной добавленной стоимостью и зависимостью от upstream — т.е. масштаб без автономии на frontier.
4. **Decoupling в данных смешанный, не однонаправленный.** Hitech-share: USA +1.5 пп vs CHN −3.6 пп post-2022 при IC-стоимости USA −1.9% vs CHN +7.2% и общем спаде 2023. Это маркеры на фоне цикла, не «эффект санкций». Формулировки «CHIPS/BIS снизили/повысили» запрещены.
5. **HPC/quantum геополитики из панели не следует.** Без TOP500 и IPF-рядов любые заявления «HPC-гонка решена» или «квантовое преимущество у X» — спекуляция. Допустимо только: обе квантовые программы — маркеры задела (NQI Act 2018 vs Micius/13th FYP), экон. эффект ~0.

Чего НЕ следует: прогнозы «кто выиграет», оценки эффективности санкций, military-импликации beyond brief qual note, детальный supply-chain граф.

## 7. Limitations

- **Data limitations.** AI/HPC/quantum ряды 100% missing; HPC-сбор упал (KeyError); патенты до 2021 (**год = пик китайских патентных субсидий**); researchers фрагментарны (USA 2023 n/a, ISR отсутствует в WDI); hitech-корзина широкая + **SITC Rev.4 break** (Oct 2024, 28% missing — trend over break невалиден); HS8542 **номинален** в USD (processing trade, re-exports HK/SG, CHN 2015–17 quarantined); MVA лаг 1–2 года, **MVA % GDP — доля, не абсолютный выпуск**; TiVA лаг 2–3 года; CN GDP revisions (NBS 2024–25) меняют GERD/GDP pc историю; PWT 11.0 перешёл на official CN GDP.
- **Identification limitations.** Панель мала (7 стран в M1, n=84, k=20, кластеров 7 — кластер-SE невозможны, **HC1 игнорирует автокорреляцию, t по θ раздут**); **USA TFP=1 каждый год — константа; USA не дают within-вариации исхода**, идентификация на 6 странах + CHN; R²=0.992 **движим FE (USA=1-константа)**, не качество модели; эндогенность (богатые тратят больше), пропущенная динамика, omitted variables; H3/H5-регрессий нет (лимит 2 моделей); event pre/post — **n=2 в каждой ячейке, нет SE**, конфаундеры (цикл, COVID, лаги fab, HS-агрегация).
- **Technology measurement limitations.** Patents = counts (CN subsidies, utility vs invention, нет triadic/PCT-качества); articles = volume (authorship inflation, English bias, не field-specific, нет citations); BERD mix — **BERD/GERD ~77% для обеих стран** («частный vs направленный» — narrative, не данные); TOP500 ≠ cloud AI compute (hyperscale вне листа); HS8542 ≠ advanced nodes (processors vs frontier); quantum small-N волатильность; qubit-milestones несопоставимы; COM-блок пуст (нет startups/licenses/revenue/VC для CN).
- **Inability to infer causality.** Все коэффициенты — условные ассоциации внутри панели с FE. **Causal-язык («R&D повышает TFP», «CHIPS/BIS снизили…», «production вызывает export», «США конвертируют... Китай конвертирует...») запрещён.** PCA-M2 — пример артефакта (смешение интенсивностей с абсолютным объёмом статей, loading art −0.36 → γ=−0.118 бессмыслен). Pooled-корреляции — композиционный артефакт (Китай инвертирует знак). **Comparison ratios (patents/articles, hitech/GERD) — не рейтинг эффективности** (знаменатели несопоставимы).
- **Limitations of USA–China comparison.** Два кейса недостаточны для panel FE по паре; comparators обязательны, но N=8 всё равно мало; **уровни vs интенсивности vs объёмы дают противоположные «рейтинги»** — любой overall winner зависит от выбора знаменателя; **ratio-конвергенция ≠ конвергенция уровней** (GDP pc ratio вырос, но абсолютный разрыв вырос $49k→$52k); PPP vs номинал, hours-worked методология CN, processing trade и HK-реэкспорт смещают US–CN gap; без TW/KR/NL/JP картина semis искажена (omitted third parties).

## 8. Final thesis

**Главный вывод:** США и Китай демонстрируют **различные конфигурации** технологического развития — **описательно**: США выше по R&D/HC-интенсивности и частному финансированию (BERD % GDP), Китай — по абсолютным объёмам науки и доле manufacturing — **но causal-механизмы «конверсии» не идентифицированы**; направление и величина различий по AI/HPC/quantum **недоказуемы** на имеющихся данных, а frontier-узлы контролируются не бинарно, а через третьи страны и upstream-рычаги.

**Supporting arguments:**
1. **Интенсивность vs объём:** GERD/BERD/researchers на млн выше в США (0.75/0.75/~0.4 от США у Китая) при параллельных трендах, а статьи (2.17x), патенты (5.44x counts), MVA-доля (~2.5x), IC-стоимость (3.13x) выше у Китая — это **разные измерения** (интенсивности vs абсолютные объёмы vs доли), гетерогенность разрывов согласуется с H4 как «дело не только во входах», **но без рейтинга эффективности** (знания не измерены, conversion ratios не рейтинг).
2. **Зрелость сдвигает bottleneck, но как недоказанная гипотеза:** единственный измеримый кейс (semis) показывает **описательно** масштаб Китая в mature/packaging при зависимости от EUV/advanced fab и рычаге США+союзников в upstream; AI/HPC/quantum — insufficient data, поэтому H2/H5/H6 остаются гипотезами, а связь R&D→TFP **слаба и неотличима от нуля на 5%** (β=0.028, CI [−0.0005, 0.0554], p=0.06).
3. **Небинарность и смешанный decoupling:** frontier foundry (TW/KR) и оборудование (NL/JP) делают US–CN пару неполной спецификацией; CHIPS/BIS — только **временные маркеры** на фоне chip-downturn 2023 (hitech CHN −3.6 пп при IC +7.2%; **n=2, нет SE, конфаундеры**), что запрещает каузальные и «победительные» выводы.

## 9. Presentation structure (13 слайдов)

| # | Title | Key message | Evidence | Visualization |
|---|---|---|---|---|
| 1 | Вопрос не «кто сильнее», а «где расходятся пути» | RQ + TCI-цепочка S→ADE + 4 кейса как stress tests | research_design §A–D | Схема TCI + 4 кейса (блок-диаграмма) |
| 2 | Что измеряем и чего нет (честный scope) | 10 MVD-переменных есть; AI/HPC/quantum — missing; TFP=USA=1 construction | data_quality_report; MVD-таблица | Таблица Ready/Not ready (зелёный/красный) |
| 3 | Входы: интенсивность — за США | GERD 0.62→0.75, BERD 0.67→0.75, параллельные slopes (p=0.29) | snapshot; trend; F1/F9 | F1 GERD trends + F9 BERD mix (2010 vs 2023) |
| 4 | Люди: % догоняет, абсолют — нет | Researchers 0.25→~0.4, CAGR 6.8% vs 2.6%, но +106 vs +82/год | snapshot; CAGR; trend p=0.07; F2 | F2 researchers + аннотация абс. разрыва |
| 5 | Наука/инновации: объёмы — за Китаем, но ≠ лидерство | Статьи 0.76→2.17 (кроссовер ~2020); патенты 1.21→5.44x (2021) — counts | snapshot; CAGR 8.9%/15.5%; F3/F4 | F3 crossover + F4 log-patents с quality-caveat |
| 6 | Производство и экспорт: масштаб vs sophistication | MVA ~2.5x, обе доли падают; hitech gap 9.5→4.7 пп; IC 0.79→3.13x (assembly-смещ.) | snapshot; CAGR; F5/F6/F8 | F5 MVA + F6 hitech + F8 IC (серая зона 2015–17) |
| 7 | Productivity: медленный catch-up, слабая связь | TFP 0.40→0.47; M1 β=0.028 (p=0.06, CI∋0); GDP pc ratio 0.175→0.305, абс. разрыв вырос | regression_results; F7 | F7 TFP levels (подпись USA=1 construction) + forest-plot M1 CI |
| 8 | Semis: единственная стадийная разборка | Design/EDA/equipment — США+союзники; mature/packaging/downstream — Китай; frontier-fab — TW/KR | tech_cases_comparison §Semis; event CSV | 7-стадийная таблица US/CN/3rd parties (цвета +/~/bottleneck) |
| 9 | AI / HPC / Quantum: чего нельзя утверждать | Все вердикты — insufficient; TOP500≠cloud; quantum экон. эффект ~0 | data_quality_report (100% missing); source_registry | Пустые панели-заглушки + план добора (4 bullet) |
| 10 | H1–H6: что поддержано, что нет | H1-macro partial, H4-гетерогенность partial; H2/H3/H5/H6 insufficient; запреты интерпретаций | hypothesis_table; key_findings | Вердикт-таблица (Partial/Insufficient) + 3 запрета |
| 11 | Механизм без causality + геополитика bottlenecks | FIN→INN/COM vs FIN→PRD/scaling (qual); рычаг — upstream, масштаб — mature; мир не бинарен | tech_cases синтез п.4–6; policy-маркеры | Две стрелки-механизма + карта узлов (NL/JP/TW/KR) |
| 12 | Limitations (почему это не статья) | Малая N, USA=1, counts≠quality, trade≠fab, нет causality | analysis_report §6–7 | 5-блоковая таблица limitations (кратко) |
| 13 | Final thesis: конфигурация, не рейтинг | 1 тезис + 3 аргумента; что дособрать для теста | §8 выше | Тезис на 1 слайд + 3 иконки-аргумента |

## 10. Report structure

1. **Introduction (1–1.5 стр.).** Что доказывается: RQ «где расходятся пути», отказ от winner-вердикта. Данные: нет. Результаты: нет, только road map + TCI-схема.
2. **Framework & Hypotheses (1.5–2 стр.).** Что доказывается: операционализация H1–H6 в TCI-блоки S/HC/RD/FIN/INN/COM/PRD/ADE. Данные: research_design §D–F. Результаты: H-таблица заготовка (вердикты — в §6).
3. **Data & Measurement (1.5–2 стр.).** Что доказывается: что измеримо (MVD 10 vars), что нет (AI/HPC/quantum missing), сопоставимость US–CN. Данные: data_map §1–4 + data_quality_report (missing %, quarantine CHN 2015–17, SITC-break, TFP-construction). Результаты: reliability-таблица + gaps_log.
4. **Descriptive: US–China gaps & trends (2–3 стр.).** Что доказывается: асимметрия интенсивность/объём, F1–F5. Данные: core_panel 2010–2023 + WDI/OECD/PWT/WIPO/Comtrade. Результаты: snapshot-таблица (ratios+gaps), CAGR, trend slopes (p-values), F1–F9 (F8 с карантином, F6/F8 с BIS/CHIPS-линиями как маркерами).
5. **Econometrics: associations, not effects (1.5–2 стр.).** Что доказывается: слабая GERD–TFP связь, артефактность PCA, запрет causality. Данные: 7 стран, 2011–2023, n=84. Результаты: M1-таблица (β=0.0275 CI, θ=0.0563 + оговорка t), within-корреляции, PCA-loadings как отрицательный результат, R²=0.992-разбор (FE-доминирование). M2 — в appendix как диагностика.
6. **Technology cases (2–3 стр.).** Что доказывается: только semis — стадийный тест; AI/HPC/quantum — qual-mapping + insufficient. Данные: HS8542 + hitech + MVA (semis); Stanford AI Index / TOP500 / EPO–OECD — идентифицированы, не извлечены. Результаты: 7-стадийная semis-таблица, Technology×Stage-матрица, event pre/post как маркеры (не эффект).
7. **Synthesis: configuration, not ranking (1–1.5 стр.).** Что доказывается: final thesis + 3 аргумента, H1–H6 вердикты, 3 противоречия тезисам, 6 ответов на контрольные вопросы. Данные: сводка §4–6. Результаты: USA vs China matrix (11 строк), hypothesis table.
8. **Mechanisms & Geopolitics (1 стр.).** Что доказывается: только bottleneck/GVC-следствия (небинарность, upstream-рычаг vs mature-масштаб, смешанный decoupling). Данные: qual-разборка + TiVA-структура (SHOULD). Результаты: нет новых цифр; явный список «чего НЕ следует».
9. **Limitations (0.75–1 стр.).** 5 блоков из §7 выше + абзац «почему это homework, не paper».
10. **Conclusion (0.5 стр.).** 1 тезис + 3 аргумента + план добора (TOP500-pull, Comtrade single-definition, AI Index export, quantum IPF CSV).
11. **Appendix.** A: variable definitions + sources.yaml; B: M2/PCA диагностика; C: «НЕ использовать» список (8 пунктов из analysis_report §6); D: reproducibility (scripts/analysis_agent4.py, notebooks/01_collect_core_data.py, results/*.csv, figures/F1–F10).

*Объём ориентира: 12–15 страниц основного текста + appendix. Новых сборов данных не требуется; добор — только как future work.*

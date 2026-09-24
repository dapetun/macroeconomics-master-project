# Project Final — США vs Китай: технологическое соперничество (единая актуальная версия)

Дата: 2026-09-16. Статус: интегральная версия после специализированных ревью.
Приоритет при расхождении: `research_logic_final.md` > `regression_results_final.csv` (числа M1) > `data_reviewed/data_quality_final.md` (определения/покрытие) > `quant_reviewed.md` / `technology_cases_final.md` > `reports/*.md` (старые формулировки).

Окно панели: 2010–2023. Панель: USA, CHN + KOR, JPN, DEU, GBR, ISR, FRA (8 стран, 200 строк 2000–2024; анализ 2010–2023 = 112 ячеек).
Исключения окон (обязательно везде): патенты — только 2000–2021 (2021 = пик субсидий CN); researchers joint-year 2022 (USA ends 2022, GBR ends 2017, ISR 0); MVA joint-year 2021 (USA ends 2021); semi — retained 75/200 с карантином CHN 2015–17, DEU/FRA 0.
Все регрессии и корреляции — ассоциации, не causality. Allow-list языка: «ассоциировано», «условная корреляция», «дескриптивно», «неотличимо от нуля», «не измерено», «не тестируемо».

Правило чтения: `+` — сильнее на данной стадии по evidence; `~` — паритет/смешанно; `?` — нет данных для вердикта. `[expert assessment]` = качественная оценка без ряда в панели, не evidence.

---

## 1. Research question

### 1.1. Исходный RQ (research_design §A)

> Как различаются модели технологического развития США и Китая в превращении научно-исследовательских и производственных ресурсов в технологические результаты — и на каких этапах цепочки эти различия наиболее устойчивы для четырёх стратегических технологий?

Вторая половина RQ («на каких этапах… для четырёх технологий», «зависят ли узкие места от зрелости») требует 4 tech-панелей и TCI-индекса (`tci_scores.csv` не построен).

### 1.2. Отвечаемая часть (единственная, на которую отвечаем)

> Какие различия уровней и трендов US–CN наблюдаются в измеримой macro-цепочке (GERD/BERD-интенсивности, researchers-интенсивность, объёмы статей/патентов-counts, MVA-доля, hitech share, HS8542-стоимости) в 2010–2023 (joint-year / common-window), и какие звенья TCI в принципе нельзя оценить имеющимися данными?

### 1.3. Явно не отвечаем (insufficient / not tested, не «частично доказано»)

- tech-зависимость профиля (ядро H1) — нужны 4 tech-панели, есть 1 частичная (semis-trade);
- зрелость → bottleneck (H2), finance → outputs (H3), production → export (H5), INN–COM gap (H6) — тестов нет;
- любой каузальный «механизм конверсии» и любой overall winner.

---

## 2. Hypotheses

Принцип: вердикт ставится **по preregistered тесту**. Дескриптивная согласованность — отдельная колонка, не повышающая вердикт. Пост hoc переопределения запрещены. Формулировки «partially supported (macro)» (H1) и «partially supported как гетерогенность» (H4) из старых `reports/*` **отозваны**.

| ID | Preregistered тест (research_design) | Статус теста | Дескриптивное наблюдение (не тест, без статуса поддержки) | Итоговый вердикт |
|---|---|---|---|---|
| H1 | TCI-профиль 8–10 этапов × 4 tech; gap US–CN и стабильность паттерна между кейсами | **Не выполнен**: `tci_scores.csv` отсутствует; AI/HPC/quantum 100% missing; semis только trade-стоимости | Macro-асимметрия измерений: интенсивности входов выше в США, абсолютные объёмы outputs и доли/стоимости PRD/ADE выше в Китае. Это **разные измерения**, предсказуемые из знаменателей (население ×4.2, масштаб GDP), не рейтинг | **Not tested as preregistered. Наблюдение — без поддержки H1** |
| H2 | Сравнение stage-gap между 4 кейсами; rank-корреляция зрелости vs этапа | **Не выполнен**: 1 частичный кейс из 4; независимого измерителя зрелости нет (риск circular) | Qual-разборка согласуется с ожиданием, но это coherence с дизайном, не evidence | **Insufficient / not tested** |
| H3 | Cross-country regression finance mix → stage outputs | **Не выполнен**: регрессия не запускалась (лимит 2 моделей); **измерителя finance mix в панели нет** — BERD = PERFORMED % GDP (OECD MSTI `P_BERPCT`), другой провайдер/винтаж, чем WB-GERD; ISR BERD>GERD 2021–23 (2023: 6.50 > 6.35) доказывает несводимость | Pooled BERD–hitech r=+0.16 — композиционный артефакт. Дескриптивный BERD/GERD ~77% — **смесь винтажей, не finance mix; отозван как за, так и против** | **Not tested; finance mix — unmeasured** |
| H4 | Output/input ratios по этапам; разрыв в patents/publications меньше, чем в capacity/export | **Не выполнен как тест конверсии**: `conversion_ratios.csv` смешивает counts÷intensities с разными знаменателями/годами — исключён (DO NOT USE) | Разрывы численно разнородны (см. §5), но это **гетерогенность измерений**, предсказуемая из знаменателей, не тест конверсии | **Not tested as preregistered. Пост hoc «partial» отозван** |
| H5 | Regression с лагами; R² science-only vs production-only | **Не выполнен**: export-регрессии нет | Pooled MVA–hitech 0.40 > articles–hitech 0.12 — between-смещён; hitech-корзина широкая + SITC-break; HS-ревизии в IC-окне | **Insufficient / not tested** |
| H6 | Gap-index US vs CN по каждому кейсу | **Не выполнен**: COM пуст (startups/licenses/revenue/adoption — нет), gap-index не построен | — | **Insufficient / not tested** |

Следствие:
1. Полностью поддержана — ни одна.
2. Частично поддержана — **ни одна** (старые «H1-macro / H4-гетерогенность partial» отозваны).
3. Отвергнута в сильном смысле — ни одна (мощности для rejection нет).
4. Отвергнуты как запрещённые интерпретации (не H-вердикты): patents-counts=leadership; articles-volume=leadership; trade-value=fab-leadership; R&D-spending=success; benchmark=economic leadership; TOP500-rank=AI-capability; funding=commercialization; BERD-level=private-model; HS8542-growth=technological catch-up.
5. Устойчиво только дескриптивное: противоположные знаки разрывов по интенсивностям vs объёмам/долям (арифметика масштаба) + падение MVA-долей обеих стран + медленный TFP catch-up уровней при росте абсолютного GDP pc разрыва.
6. Слабые/отсутствующие доказательства: всё по AI/HPC/quantum; всё finance→outputs; всё «эффективность конверсии»; всё CHIPS/BIS-эффекты; всё fab-доли/EDA/equipment.

---

## 3. Methodology

TCI-framework (research_design §D): 8 блоков S / HC / RD / FIN / INN / COM / PRD / ADE (+ Productivity отдельно, только macro-прокси). Три слоя: descriptive gap layer (US–CN ratios/gaps, joint-year), conversion layer (запрещён к рейтингу — conversion ratios исключены), cross-country pattern layer (ассоциации, не causality).

Фактически выполнено (лимит 2 моделей):
- **Descriptive:** snapshot (только latest-joint-year, никаких ratio с NaN-стороной) + CAGR/slopes только common-window с явными (start, end, n): researchers 2010–2017 (GBR-ограничение), patents/total-office + MVA 2010–2021, остальное 2010–2023; TFP USA из ранжирований исключён.
- **M1 (retained, descriptive-only):** `TFP_it = α_i + δ_t + β·GERD_{t−1} + θ·logRes_t + ε`, LSDV country+year FE, HC1 + country-cluster SEs. Авторитетно: `regression_results_final.csv`. n=84, K=20, df=64, G=7 (CHN13 DEU13 FRA13 JPN13 KOR13 USA12 GBR7 ISR0; 2011–2023, 2010 потерян лагом). FE-only R²=0.727, full R²=0.992 (прирост 0.265; высокий R² движим FE, прежде всего USA=1-константой). Чувствительности обязательны: lag0/lag1/lag2, drop-one, pooled-OLS знак, cluster-CI.
- **M2/PCA (excluded, DO NOT USE):** `TFP on TechPC1` — loadings некогерентны (GERD +0.55, BERD +0.53, logRes +0.53, logArticles −0.36 — смешение интенсивностей с абсолютным объёмом), γ=−0.118 артефактен. PCA n=91 (ISR 0). F10 scatter исключён.
- **Корреляции:** pooled-матрица (`correlations_pooled.csv`) — DO NOT USE для выводов (Simpson/композиция: pooled GERD–TFP −0.086 vs within ≈+0.03/+0.24; GDPpc–TFP +0.91 — accounting-adjacent). Если показывать — только within/two-way-demeaned с N, дескриптивно.
- **Event pre/post (CHIPS Act Aug-2022 + BIS Oct22/Oct23):** pre 2020–21 vs post 2022–23, n=2/ячейка, без SE — только vertical lines «не эффект», конфаундеры (цикл, COVID, downturn 2023, HS-агрегация, processing trade, карантин).
- **Tech-кейсы:** только semis-trade + macro-контекст количественно; AI/HPC/quantum — qual-mapping + `?` (см. §6). Старые `regression_results.csv` (HC1-only), `model2_*`, `pca_*`, `conversion_ratios.csv`, `trend_slopes_convergence.csv` (где pooled) — superseded для выводов, на диске остаются, не цитируются как evidence.

---

## 4. Data

Панель: 8 стран × 2000–2024 = 200 строк; анализ 2010–2023. Построена строго из `data/raw/` без импутации/бэкфилла (`scripts/build_reviewed_dataset.py` → `data_reviewed/core_panel_reviewed.csv`, `tech_panel_reviewed.csv` — значения байт-идентичны processed-панели; добавлены только `patents_total_office` и `semi_status`). Оригиналы `data/`, `results/`, `figures/`, `scripts/analysis_agent4.py` не менялись.

### 4.1. Готовы с оговорками (10 + 1 reviewed-добавка)

| Переменная | Raw | Kept / 200 | Missing-паттерн | Использовать только как | Severity |
|---|---|---|---|---|---|
| `gerd_pct_gdp` | WB `GB.XPD.RSDV.GD.ZS` (UNESCO-derived) | 192 | all-2024 (raw ends 2023) | R&D-интенсивность % GDP; не OECD MSTI; CN NBS GDP revisions меняют denominator | LOW |
| `researchers_per_million` | WDI `SP.POP.SCIE.RD.P6` (UNESCO-UIS) | 161 | ISR 0/25; GBR ends 2017 (2018–24 missing); USA ends 2022; all-2024 missing | Headcount/FTE различаются; per-million denominator в пользу малых популяций; **GBR ends 2017 (не 2019)** | HIGH для ISR/GBR-сравнений |
| `scopus_articles` | WDI `IP.JRN.ARTC.SC` | 192 | all-2024 | **Fractional-count S&E volume** (decimals), NSF-derived; volume, не impact; не field/AI-specific | MEDIUM |
| `patents_resident` | WDI `IP.PAT.RESD` | 176 | 2022–24 all missing (raw 2000–2021) | **Resident filings AT national office (office basis), НЕ WIPO origin**; counts, не quality; CN 2021 = пик субсидий | HIGH для level-сравнений |
| `patents_total_office` (reviewed-добавка) | resident + nonresident (perfect 176/176 join, 2000–2021) | 176 | как выше | Total office filings (office basis); counts, не quality. 2021 CHN/USA: resident-only 5.44x vs office-total **2.68x** — resident-only завышает разрыв ~2x | MEDIUM (частично чинит bias) |
| `mva_pct_gdp` | WDI `NV.IND.MANF.ZS` | 193 | CHN 2000–03 + USA 2022–24 missing в raw | **Share of GDP, не абсолютный выпуск**; macro manufacturing, не semi capacity | MEDIUM |
| `hitech_export_share` | WDI `TX.VAL.TECH.MF.ZS` | 144 | 2000–06 all missing (ряд с 2007) | Broad high-tech basket; **SITC Rev.4 break (Oct 2024, 28% missing) + ISR-нестабильность 2007–09**; CHN processing-trade bias | HIGH для early-trends |
| `gdp_pc_ppp` | WDI `NY.GDP.PCAP.PP.KD` (constant 2017 intl-$) | 200 | none (2024 — preliminary) | Single Sep-2026 vintage; только нормализация | LOW |
| `tfp_ctfp` | PWT mirror `ctfp` | 192 | all-2024 | **USA = 1.000 каждый год by construction (проверено 1994–2023)**. CHN читается только как gap к contemporaneous frontier. Macro TFP, не tech-TFP | HIGH если оценивать USA-trend |
| `berd_pct_gdp` | OECD MSTI `P_BERPCT` | 200 | none | **BERD PERFORMED % GDP, НЕ business-financed** (старый титул F9 неверен). Другой провайдер/винтаж, чем WB-GERD: **ISR BERD>GERD 2021–23** (2023: 6.50 > 6.35) доказывает несводимость; GERD−BERD не вычислять | HIGH для finance-mix |
| `semi_exports_hs8542` | Comtrade HS8542 legacy (значения неизменны) | 75 kept / 125 missing | 2000–09 out of window; CHN 2015–17 quarantined; DEU 0 (all multi-record); FRA 0 (no response); GBR 8 kept (2010–16+2018) | Номинал USD HS8542, **смешанные HS-ревизии** (H3 2010–11 / H4 2012–16 / H5 2017–21 / H6 2022–24); re-export/processing bias; спайки CHN 2012–13 +63%/+63%, KOR 2016–17 +65% retained-but-flagged; trade value, не fab capacity | HIGH; comparator-incomplete |

### 4.2. Исключены — не готовы к эконометрике (100% missing в панелях, оставлены NaN)

`hpc_top500_systems`, `hpc_top500_rmax_tflops` (нет аудированного TOP500 country-year экстракта), `ai_publications_count`, `ai_citations_impact`, `ai_private_investment_usd_bn`, `ai_notable_models` (Stanford HTML есть, audited country-year export нет; generic counts не субститут), `quantum_ipf_count`, `quantum_publications` (EPO-OECD источник идентифицирован, chart-экстракции нет), плюс `gvc_foreign_va_share` / VC (запланированы в data_map, не собраны — нет raw, нет колонки; в результатах не появляются).

Lineage-оговорка: `data/raw/comtrade_hs8542_exports_clean.csv` — USA-only (15 строк, 2010–2024, world partner). `data/processed/tech_panel.csv` (75 kept) построен из legacy по правилу `num_records==1`, не из clean-файла. Clean-файл — stale parallel artefact, не источник панели. Reviewed-панель хранит 75 legacy-значений + `semi_status` (`retained_one_record` / `quarantined_multi_record` / `missing_no_response`; карта `tables_reviewed/semi_quarantine_map.csv`). До полного single-definition multi-reporter Comtrade re-pull: DEU/FRA semi unusable, CHN 2015–17 — hard gap.

### 4.3. Effective samples (окно 2010–2023)

GERD/BERD/scopus/GDP/TFP: 14/страна (TFP USA — константа). Researchers: USA 13, CHN/KOR/JPN/DEU/FRA 14, GBR 8, ISR 0. Patents (res + total): 2010–2021, 12/страна. MVA: USA 12 (до 2021), остальные 14. Hitech: 14/страна (с 2010). Semi retained: USA/KOR/JPN/ISR 14, CHN 11, GBR 8, DEU/FRA 0. M1 n=84 (CHN/DEU/FRA/JPN/KOR 13, USA 12, GBR 7, ISR 0). PCA n=91.

---

## 5. Quantitative findings

Все числа — latest-joint-year + common-window. Никаких ratio с NaN-стороной. Никаких CAGR/слоупов на несопоставимых окнах.

### 5.1. Уровни (joint-year; snapshot)

| Блок | Joint-year | USA | CHN | Ratio/gap | Caveat |
|---|---|---|---|---|---|
| GERD % GDP | 2023 | 3.45 | 2.58 | 0.748 | Интенсивность; CN GDP revisions |
| BERD PERFORMED % GDP | 2023 | 2.66 | 2.00 | 0.754 | **Уровень PERFORMED, не модель финансирования**; FIN-структура неизмерена |
| Researchers/млн | 2022 (joint; USA 2023 n/a) | 4937.49 | ~1849 | 0.375x | **Intensity, не headcount**; denominator-артефакт (население ×4.2); FTE/headcount; GBR ends 2017, ISR 0. Абсолютные головы «~1.2M→2.4M» **удалены** (расчёта нет) |
| Статьи (fractional S&E volume) | 2023 | 430843 | 932712 | 2.165x | Volume, не citations/impact; кроссовер ~2020; не AI-specific |
| Патенты-resident (office-basis counts) | 2021 | 262244 | 1426644 | **5.44x только в паре** | Пик субсидий CN 2021; home-bias офисов (USA nonresidents > residents, CHN наоборот) |
| Патенты total-office (counts) | 2021 | 591473 | 1585663 | **2.68x в паре** | Тоже counts, не качество; triadic/PCT не собраны |
| MVA-доля | 2021 (joint; USA 2022–23 missing) | 10.53% | 26.62% | 2.53x | **Доля, не абсолютный выпуск и не fab-мощность**; MVA macro, не semis-VA |
| Hitech share (broad) | 2023 | 21.85% | 26.57% | gap 9.5→4.7 пп | SITC-break; re-exports; trend over break невалиден |
| IC HS8542 (номинал) | 2023 | $43.6 млрд | $136.4 млрд | 3.13x | **Номинал USD, processing trade, re-exports HK/SG, HS-ревизии H3–H6, карантин CHN 2015–17; HS8542≠advanced nodes; trade≠fab** |
| GDP pc PPP (2017 intl-$) | 2023 | $74352 | $22687 | 0.305x **только в паре** | **Абсолютный разрыв вырос $49321→$51664**; ratio-конвергенция ≠ конвергенция уровней |
| TFP macro (PWT ctfp) | 2023 | 1.0 (construction) | 0.471 (2010: 0.395) | catch-up +0.076 за 13 лет | **USA=1 каждый год 1994–2023 — construction**; наклон USA (≈−3.6e−17) не интерпретируется; агрегатный, не tech-TFP |

2010-якоря (для чтения трендов): GERD 2.71/1.69 (0.62); BERD 1.85/1.24 (0.67); researchers 3644/899 (0.25); статьи 407k/308k (0.76); патенты-resident 242k/293k (1.21); MVA 11.9/31.1; hitech gap +9.5 пп; GDP pc $59.8k/$10.5k (0.175); TFP 1.0/0.395; IC $37.7/$29.6 млрд (0.79).

### 5.2. Темпы (только common-window с (start,end,n))

- GERD 2010–2023: USA 1.86%/год vs CHN 3.33%/год; slopes +0.072 vs +0.062 пп/год, diff n.s. p=0.29 — **параллельный рост, конвергенции скорости нет**.
- Статьи 2010–2021 (common): USA 1.33%/год vs CHN 8.51%/год; slopes +2.9k vs +48.3k/год, p<0.001 — дивергенция объёма. Старые пары «0.4% vs 8.9%» на полных окнах — несопоставимы, не использовать.
- Патенты-resident 2010–2021: USA 0.73%/год vs CHN 15.47%/год.
- MVA-доля 2010–2021 (common): USA −1.11%/год vs CHN −1.40%/год — **обе доли падают** (структурный сдвиг, быстрее с высокого уровня CHN); slopes −0.14 vs −0.51 пп/год, diff p<0.001.
- Researchers только 2010–2017 для сравнений (GBR-ограничение). Полные-окна пары «2.6% vs 6.8%» — несопоставимы без пометки (USA 2010–2022, CHN 2010–2023).
- Hitech: USA −0.3%/год (n.s.) vs CHN −1.5%/год; slopes −0.09 (n.s.) vs −0.22 (p=0.02), diff n.s. p=0.26.
- GDP pc: +$1099 vs +$933/год, diff p=0.01 — абсолютный разрыв растёт. TFP CHN +0.0063/год (+1.4%/год), p<0.001; USA 0 по построению.
- IC-номинал CAGR (+1.1% vs +12.5%) — **смещён HS-ревизиями и карантином; технологическим трендом не читать**.

### 5.3. Регрессия M1 (единственная допустимая формулировка)

«В 84 страно-годах GERD_{t−1} на 1 пп выше ассоциирован с +0.027 TFP-пункта условно по стране, году и researcher-интенсивности — **HC1 95% CI [−0.0005, 0.0554] включает 0, p=0.059 (на 5% неотличимо от нуля); country-cluster (t_6) CI [−0.048, 0.103], p=0.409 (G=7, осторожно); лаг/окно/состав меняют знак и значимость; обратная причинность и пропущенные переменные не устранены**».

Детали: β_GERDlag1=0.02746 (HC1 SE 0.01427, t=1.92); θ_lres=0.05629 (SE 0.00429, t=13.1 HC1 / t≈7.1 cluster — **t раздут автокорреляцией AR(1) 0.32–0.90, HC1 игнорирует серийную корреляцию**); FE-only R²=0.727 → full 0.992. Хрупкость: contemporaneous β=0.0125 p=0.418; lag-2 β=0.0525 p=0.001 (лаг-1 теоретически не обоснован — показывать все три, lag-1 не headlining); pooled OLS без FE β=−0.207 (знак FE-зависим); drop-CHN β=0.0189 (p=0.157), drop-KOR β=0.0487 (p=0.017), drop-GBR β=0.0405, balanced 2011–21 β=0.0353 (±30–75% от одной страны); corr(gerd_lag1,lres)=0.71 (VIF≈2); USA-константа потребляет dummy и 12 строк (drop-USA β→0.0329); GBR только 7 строк. Величина: закрытие TFP-разрыва 0.53 одной β требует +19 пп GERD — абсурд, β — не политический мультипликатор. θ: +10% researchers ↔ +0.005 TFP-пункта, дескриптивно. M2-знак («больше tech — ниже TFP») никогда не интерпретировать (артефакт конструкции). Приписывание AI/semis/HPC/quantum запрещено (агрегатный TFP).

### 5.4. Графики (F1–F10 → текст)

- F1 GERD: OK — KOR/ISR выше всех; параллельный рост CHN. Подпись: «intensity, CHN с низкой базы».
- F2 researchers: линия честно рвётся (ISR absent, GBR ends 2017, USA ends 2022). Подпись: «ISR missing; unbalanced windows; per-million denominator; не интерполировать». Сравнений CHN-2023 vs USA-2021/2022 нет.
- F3 articles crossover 2020–21: OK как **volume**; подпись «counts, не citations/impact; не AI-specific».
- F4 patents (log, 2010–21): OK окно; подпись «resident-only; total-office gap 2.68x; пик 2021; нет post-2021».
- F5 MVA: линия USA честно останавливается (2021). Подпись «USA 2022–23 missing; доля, не абсолют; common-window 2010–2021 предпочтителен».
- F6 hitech: подпись «SITC Rev.4 break + re-export caveat; CHIPS/BIS — только vertical lines „не эффект"».
- F7 TFP: подпись «USA=1 construction — плоская линия USA дефиниционна; наклон USA не читать».
- F8 semi (FIXED-версия авторитетна): DEU/FRA опущены (нет данных), разрыв CHN 2015–17 показан разрывом, подписи HS H3/H4/H5/H6 + quarantine `semi_status`. Спайки CHN +63% 2012→13 и KOR +65% 2016→17 — retained-but-flagged, не тренды. Через gap не соединять.
- F9 BERD (FIXED-версия авторитетна): титул «BERD PERFORMED (% GDP; OECD MSTI P_BERPCT)», подпись «ISR BERD>GERD 2021–23 — артефакт винтажа, не >100%».
- F10 PCA scatter: **EXCLUDED** (M2).

---

## 6. Technology cases

Количественно тестируем только semis-trade + macro-контекст. AI/HPC/quantum-вердикты US–CN — только `?` (insufficient) либо [expert assessment].

### 6.1. AI

Измеримо только general-контекст, не AI-вердикт: объёмы статей (2.17x, general), патенты-counts (5.44 resident / 2.68 total-office, 2021), GERD/BERD-интенсивности (уровни PERFORMED), researchers-интенсивность. Всё AI-specific missing: `ai_publications_count`, `ai_citations_impact`, `ai_private_investment_usd_bn`, `ai_notable_models` как ряд (Stanford AI Index 2025 + Vibrancy Tool идентифицированы, не извлечены; CN private $ слабее; notable models — только snapshot).

- A (измеримо): США выше только по интенсивностям входов general-R&D/HC. Это не AI-лидерство. Confidence HIGH-MEDIUM.
- A-qual [expert assessment]: private AI investment и frontier/notable models — внешний сигнал по дизайну Stanford в пользу США, но без ряда вердикт запрещён; только гипотеза. LOW / insufficient.
- B (измеримо): Китай выше только по абсолютным объёмам general-outputs. MEDIUM для объёмов; **не leadership**.
- B-qual [expert assessment]: масштаб быстрой диффузии через manufacturing/downstream — правдоподобный механизм, но AI-adoption не измерен; MVA/HS8542 как «AI-adoption» запрещены. LOW.
- C. Bottleneck [expert assessment]: США — перенос INN→PRD/scaling внутри страны (MVA-**доля** 10.5% vs 25.0% joint — доля, не выпуск) + зависимость от allied fabrication/compute; Китай — доступ к frontier compute и конверсия объёма в impact (impact-ряд missing; BIS — только маркеры режима).
- D. Mechanism [expert assessment, not tested]: «частный FIN→INN/COM» vs «объёмы+PRD/scaling→удешевление/диффузия» — qual-гипотезы; регрессии finance→outputs нет; pooled r=+0.16 — не evidence; **BERD-уровень выше в США (2.66 vs 2.00) читается только как PERFORMED-интенсивность, не «частная модель»; паритет 77% отозван (§2/H3)**.
- Запрещено: «США/Китай сильнее в AI» без стадии; «публикации/патенты = AI-лидерство»; «benchmark/frontier = экономическое лидерство»; «AI capability = productivity gain».

### 6.2. Semiconductors (7 стадий + третьи страны как сквозной узел)

Количественные якоря (только стоимости и macro-доли, не мощности):
- MVA-доля: 11.9/31.1 (2010) → USA 10.5 (2021 joint) / CHN 25.0 (2023); обе доли падают. MEDIUM-HIGH для долей; **LOW/запрет для fab-мощностей** (MVA macro, не semis-VA).
- HS8542-номинал: 0.79 ($29.6/$37.7 млрд, 2010) → 3.13 ($136.4/$43.6 млрд, 2023); CAGR поверх разрыва CHN 2015–17 и HS-ревизий — **смещён, читать только как «номинальные стоимости с разрывами»**. Включает processing trade и re-exports HK/SG; HS8542≠advanced nodes. **Trade≠fab; announced capacity≠production.**
- Hitech share: разрыв +9.5 пп → +4.7 пп; **trend over SITC-break невалиден**.
- Event-маркер (n=2, без SE): IC USA −1.9%, CHN +7.2%; hitech USA +1.5 пп, CHN −3.6 пп; 2023 — общий спад. Только vertical lines.

| Стадия | USA | China | Третьи страны (bottleneck-узлы) | Evidence / Confidence |
|---|---|---|---|---|
| Chip design / IP | Сильнее [expert assessment] | Догоняющее [expert assessment]; general-патенты — не evidence | UK (ARM-IP); TW/KR — спрос | LOW-MEDIUM; firm-ряда нет |
| EDA | Сильнее [expert assessment]; контроль — рычаг, не мощность | Зависимость, bottleneck [expert assessment] | Концентрация в США/союзниках, без квантификации | LOW; BIS — маркеры |
| Equipment (в т.ч. EUV) | Отдельные сегменты; ключевой EUV-рычаг — **у союзников, не у США** | Зависимость, bottleneck для advanced [expert assessment] | **NL (ASML EUV); JPN — материалы/оборудование** | LOW-MEDIUM; SEMI-ряда нет |
| Advanced fab (<10nm) | Слабее внутри; CHIPS Act — **намерение/анонсы, не производство** | Слабее на frontier [expert assessment] | **TWN, KOR доминируют frontier foundry** [expert assessment]; KOR IC CAGR +6.5% vs JPN −0.9% — лишь trade-контекст, не мощность | Qual; LOW для долей; анонсы≠выпуск |
| Mature / packaging (scale) | ~ | [expert assessment] по масштабу; MVA-**доля** и IC-стоимость — лишь косвенный контекст с assembly-смещением | MYS и др. — OSAT-хабы (data_map, не панель) | MEDIUM для долей/стоимостей; LOW для node-долей (ряда нет) |
| Downstream demand | Сильнее в платформах/ПО/облаках [expert assessment] | Сильнее в сборке/масштабе; hitech выше, но разрыв сузился (SITC-break) | — | MEDIUM для стоимостей; LOW для «спроса на frontier» |
| Сквозной узел | Рычаг — **через союзников** (EDA/IP + NL/JP-equipment + TW/KR-foundry), не автономно | Уязвимость — та же союзническая концентрация + BIS-контроли | **Без TW/KR/NL/JP сравнение US–CN — misspecification** | Qual; квантификации fab-долей нет |

Bottleneck: Китай — equipment (EUV) + advanced fab; США — перенос design во внутренний frontier-fab/packaging-масштаб. CHIPS/BIS/MiC2025 — policy-маркеры, не evidence.

### 6.3. HPC / compute (вердиктов нет; три типа не смешивать)

`hpc_top500_systems`, `hpc_top500_rmax_tflops` — **MISSING 100%** (KeyError). Методика идентифицирована (TOP500.org, Nov snapshot 2010–2025, HIGH если собрать), цифр нет — графики/рейтинги запрещены. Три сущности: (1) supercomputer performance (TOP500 count/Rmax, PRD; Rmax=Linpack HPL, не HPCG/HPL-MxP; даже собранный TOP500 — peak Linpack, не usable AI-compute); (2) commercial AI compute (hyperscale вне листа; TOP500≠cloud); (3) general infrastructure (облака/ДЦ; не измерена). Non-reporting bias CN, «PRC vs China sites», только Nov-срез — для будущего сбора. A/B — только [expert assessment]-гипотезы, **no verdict**. Допустимый вывод: «панель не позволяет тестировать HPC; требуется Nov TOP500-pull (count+Rmax) + разделение 3 типов + AI-compute narrative». Confidence insufficient/LOW.

### 6.4. Quantum (ранняя стадия; экономика ≈ 0)

Разделять computing / communication (Micius 2016 — S/RD-маркер) / sensing (упомянуть, не оценивать). `quantum_ipf_count`, `quantum_publications` — **MISSING** (EPO–OECD Dec 2025, 2005–2024 — идентифицирован, экстракции нет). Qubit-milestones — только qual-timeline (определения несопоставимы). A/B — только [expert assessment]-гипотезы, no verdict (США — computing-экосистема; Китай — communication-демонстраторы + масштаб гос-R&D как входа, не quantum-specific; IPF — только после ручного CSV). Bottleneck обеих — наука→R&D→коммерциализация (H2-ожидание — coherence, не evidence). Механизма экономического преимущества нет — только задел (опционы). Текущий макроэффект ≈ 0 **по построению ранней стадии** (qual-констатация). Confidence LOW/insufficient. Запрещено: «qubit-милстоун = лидерство»; «финансирование = успех»; приписывание TFP/экспорта кванту.

---

## 7. Economic implications (механизмы: что показано, чего нет)

- **R&D → productivity.** Не идентифицирован. M1 — слабая хрупкая условная ассоциация, неотличимая от нуля (§5.3). FE — не идентификация; эндогенность, omitted variables, измерение CN — не устранены. Tech-приписывание запрещено. **Статус: механизма нет; есть уровни catch-up.**
- **Finance → INN/COM vs FIN → PRD/scaling.** Не тестируем: измерителя finance mix нет, регрессии нет, COM пуст. Pooled r=+0.16 — артефакт. BERD-уровень выше в США — это уровень PERFORMED-интенсивности, не «частная модель». **Статус: два недоказанных qual-предположения без измерителя.**
- **S/INN-объёмы → PRD/scaling-масштаб.** Не тестируем: нет fab-ряда, нет регрессии PRD на RD/FIN, MVA — macro-доля, IC — номинал с assembly-смещением. **Статус: qual-предположение.**
- **PRD/scaling → торговое присутствие (H5).** Не тестируема: export-регрессии нет; pooled r between-смещён; корзина + SITC-break; HS-ревизии. **Статус: нет.**
- **INN → COM-конверсия и INN–COM gap (H6/H4).** COM пуст; conversion ratios исключены; патенты/статьи — counts/volume без качества. Ранжирование «эффективности» запрещено. **Статус: нет.**
- **Upstream-контроль (EDA/IP/EUV) → рента/рычаг (США+союзники).** В панели нет цен, марж, долей foundry/equipment, роялти. BIS/CHIPS/MiC2025/NQI/Micius — маркеры, не evidence; event n=2 без SE. **Статус: tech-описание без экономического измерения.**
- **AI-диффузия; HPC peak→доступность; quantum-опционы.** Adoption/COM/AI-compute/IPF-рядов нет. **Статус: гипотезы без теста.**
- **Long-run growth.** Нет growth-регрессии; GDP pc — только уровни/тренды (ratio-конвергенция при дивергенции уровней). Sectoral TFP out of scope. **Статус: запрещён.**

Итог: измеримая часть показывает, **где различаются уровни/тренды выбранных метрик**, но не показывает, **насколько одно звено вызывает другое**; все стрелки «→» — недоказанные предположения.

---

## 8. Comparative assessment (исправленная USA–CHN матрица; только измеримое, остальное `?`)

| Stage (TCI) | USA | China | Evidence | Confidence + caveat |
|---|---|---|---|---|
| S: объём статей (general) | ~ (ниже с ~2020) | + (2.17x, 2023, general) | snapshot joint; slopes common-window | MEDIUM для объёмов; **не AI/science-лидерство** (volume≠impact; Scopus bias; не field-specific) |
| HC: researchers/млн (general) | + (интенсивность ~2.6x, joint-2022 0.375x инверсно) | ~ (уровень ниже; % рост быстрее) | snapshot joint-2022; CAGR 2010–2017 | MEDIUM-HIGH для интенсивности; **не headcount/качество** (знаменатель; FTE/headcount; GBR–2017, USA–2022, ISR 0) |
| RD: GERD % GDP | + (3.45 vs 2.58, 2023) | ~ (0.75; slopes параллельны, n.s.) | snapshot; trend | HIGH для интенсивностей; CN GDP revisions |
| FIN: структура финансирования | ? | ? | **Нет измерителя** (BERD=PERFORMED, винтажная смесь; VC/AI-$ missing) | **Insufficient. Паритет 77% отозван** |
| INN: патенты-counts (general) | ~ (counts ниже) | + (resident 5.44x **в паре** с total-office 2.68x, 2021 = пик субсидий) | snapshot joint-2021 оба ряда | MEDIUM для counts; **запрет quality** (office home-bias; subsidies; triadic/PCT нет) |
| PRD: MVA-доля (macro) | Ниже доля (10.5%, 2021 joint) | Выше доля (26.6% joint-2021; 25.0% в 2023) | snapshot joint-2021; CAGR common (обе падают) | MEDIUM-HIGH для долей; **доля, не выпуск и не fab** |
| PRD: зрелые мощности / packaging / fab-доли | ? | ? | Нет SEMI-ряда | **Insufficient. MVA/IC — не измерители node-долей** |
| COM: стартапы/лицензии/revenue/frontier/adoption | ? | ? | Пусто (AI/HPC/quantum 100% missing; notable — snapshot) | **Insufficient** |
| ADE: HS8542-стоимости | ~ ($43.6 млрд, 2023) | + ($136.4 млрд, 3.13x **номинал**) | Comtrade joint-values | MEDIUM для стоимостей; **номинал, processing, re-exports, HS-ревизии, карантин; ≠advanced nodes; ≠fab** |
| ADE: hitech share (broad) | ~ (21.8%) | + (26.6%; gap 9.5→4.7 пп) | snapshot | MEDIUM для корзины; **trend over SITC-break невалиден** |
| Productivity: TFP (macro) | 1.0 (**construction**) | 0.47 (catch-up +0.076) | snapshot; M1 (β=0.028, CI∋0; cluster шире) | MEDIUM для уровней; **запрет causality; не tech-TFP; USA — константа** |
| Productivity: GDP pc | $74.4k | $22.7k (0.305) + **абс. разрыв $49k→$52k** | snapshot | Ratio≠уровни |
| Resilience / upstream / foundry / EDA / EUV | ? (как evidence) | ? (как evidence) | Нет рядов; NL/JP/TW/KR-структура — внешнее знание, не панель | **Insufficient как finding; только контекст** |

Графики соответствуют тексту: F1–F7 с caveat-подписями выше; F8/F9 — FIXED-версии (DEU/FRA опущены, gap разрывом, PERFORMED-титул, ISR-артефакт); F10 исключён.

---

## 9. Limitations

- **Data.** AI/HPC/quantum 100% missing; HPC-сбор упал (KeyError); патенты office-basis counts до 2021 (пик субсидий CN); researchers фрагментарны (GBR–2017, USA–2022, ISR 0; FTE/headcount); hitech broad basket + SITC-break (ряд с 2007); HS8542 номинал + HS-ревизии H3–H6 + processing/re-exports + карантин CHN 2015–17 + DEU/FRA 0 + flagged-спайки; MVA — доля, не абсолют; BERD — PERFORMED, винтажная смесь с WB-GERD (ISR-инверсия); TiVA/VC/GVC — не собраны; COM пуст; GDP — 2017-винтаж, 2024 preliminary; PWT official-GDP basis для CHN TFP; CN GDP revisions.
- **Identification.** M1 n=84, K=20, df=64, G=7 (ISR 0, GBR 7, USA 12-константа); USA TFP=1 (1994–2023) — ноль within-вариации, drop-USA β=0.0329; R²=0.992 движим FE; HC1 игнорирует AR(1) 0.32–0.90 (t раздут), cluster-CI широк (G=7, осторожно); лаг-1 не обоснован (lag0 n.s., lag2 p=0.001); corr(gerd,lres)=0.71; pooled знак −0.207 FE-зависим; drop-one ±30–75%; event n=2 без SE (цикл/COVID/downturn); H3/H5-регрессий нет; endogeneity/omitted/measurement не устранены.
- **Technology measurement.** Counts≠quality (subsidies, utility vs invention, нет triadic/PCT); volume≠impact (authorship inflation, English bias, не field-specific, нет citations); trade≠fab; announced≠production; TOP500 (HPL)≠AI-compute≠cloud; HS8542≠advanced nodes; quantum small-N; qubit-милстоуны несопоставимы; COM/ADE-tech пусты.
- **Comparison.** Intensity vs volume — арифметика знаменателей (население ×4.2, GDP-масштаб), не находка о «моделях»; уровни vs интенсивности vs объёмы дают противоположные «рейтинги» — overall winner зависит от знаменателя; ratio-конвергенция ≠ конвергенция уровней; PPP vs номинал; processing/HK-реэкспорт; без TW/KR/NL/JP semis-картина — misspecification (но сама структура панелью не измерена).
- **Causality.** Запрещена. Allow-list см. преамбулу. M2/pooled/conversion/F10 — DO NOT USE. CHIPS/BIS — только vertical lines «не эффект». Геополитика §7 logic-версии — только внешние контекстные оговорки, не findings, не в executive conclusion.

Hidden assumptions (фиксируем): latest-vintage решает CN revisions — предполагаем; researchers FTE/headcount сопоставимы в пределах ряда — с caveat, головы не выводим; Scopus fractional сопоставим US–CN внутри ряда несмотря на bias — только для объёмов; office-basis counts сопоставимы как «объёмы заявок» несмотря на home-bias/субсидии — только парой, не как INN; HS8542-номинал сопоставим как «стоимости» несмотря на ревизии/re-exports — тренд не технологический; лаг-1 GERD→TFP за 1 год — не обоснован; FE устраняют только time-invariant traits и общие шоки; USA-константа не безвредна; отсутствие tech-панелей не смещает macro-выводы только при условии §1.3; зрелость без независимого измерителя — H2 circular, если выводить из bottleneck.

Future work (без исследований сейчас): TCI-индекс; single-definition Comtrade-pull; Nov TOP500-pull (count+Rmax) + 3 типа compute; Stanford AI Index audited export (publications + private $; notable — cross-section); EPO–OECD quantum IPF CSV 2005–2024 вручную; панель 15–20 стран; sectoral TFP; отдельный finance-mix измеритель (financed, единый винтаж).

---

## 10. Conclusion (минимальный thesis; заменяет §8 final_synthesis и «одну строку» tech-cases)

**Главный вывод:** в измеримой macro-части (2010–2023, joint-year/common-window) США выше по R&D/HC-интенсивностям (GERD, BERD PERFORMED, researchers/млн), Китай — по абсолютным объёмам статей/патентов-counts и по долям/стоимостям поздней части (MVA-доля, hitech share, HS8542-номинал) — **но это описание выбранных измерений с предсказуемой знаменательной арифметикой, а не установленный факт о «моделях»; каузальные механизмы конверсии не идентифицированы; tech-зависимость профиля (AI/semis/HPC/quantum) недоказуема без tech-панелей; frontier-узлы количественно не оценены в панели.**

Три опорных пункта (только измеримое):
1. **Интенсивности vs объёмы/доли — разные измерения, не рейтинг.** GERD 0.75, BERD-уровень 0.75, researchers-интенсивность ~0.38 (joint-2022) vs статьи-объём 2.17, патенты-counts (5.44 resident / 2.68 total-office, 2021), MVA-доля ~2.5x (joint-2021), IC-номинал 3.13x — гетерогенность знаков следует из denominators; ранжирование «конверсии» запрещено.
2. **Связь ресурсов с TFP слаба и неотличима от нуля; catch-up — уровни, не механизм.** β_GERD=0.028 (HC1 CI∋0, p=0.06; cluster CI [−0.048, 0.103], p=0.41), хрупка к лагу/окну/составу; TFP CHN 0.40→0.47 — уровни macro-TFP, не tech-эффект.
3. **Единственный частичный tech-след — номинальные semis-стоимости с карантинами, не fab-лидерство; AI/HPC/quantum — insufficient.** HS8542 — номинал с HS-ревизиями, processing trade, re-exports, gap CHN 2015–17; hitech — broad basket + SITC-break; fab/EDA/EUV/COM/ADE-tech — нет рядов.

Чего thesis **не** утверждает: кто «сильнее» в AI/HPC/quantum; что finance-модели различаются (и что они одинаковы — тоже не утверждает: FIN неизмерен); что конверсия эффективнее у X; что CHIPS/BIS дали эффект; что mature-масштаб = лидерство; что объёмы = влияние; что TFP движим текущими GERD; что «США превращают… Китай — …» (causal-глагол удалён).

*Геополитический контекст (не findings, не в executive conclusion): внешние отраслевые источники указывают на концентрацию frontier-узлов вне US–CN (EUV NL, оборудование/материалы JP, foundry TW/KR, IP UK); панелью это не измерено (KOR/JPN-цифры — GERD/trade-контекст, не мощности). BIS/CHIPS/MiC2025/NQI/Micius/Dual Circulation — только временные маркеры режима (event n=2, нет SE, downturn 2023). Decoupling-смесь на уровне стоимостей/долей (hitech CHN −3.6 пп post vs USA +1.5 пп при IC CHN +7.2% vs USA −1.9%) — маркеры на фоне цикла, не оценка санкций.*

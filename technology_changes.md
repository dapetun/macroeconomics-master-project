# Technology review — что проверено и что исправлено

Дата: 2026-09-14. Рецензент: Technology Case Reviewer.
База: `reports/tech_cases_comparison.md` (агент 5) → `technology_cases_final.md`.
Метод: каждый существенный тезис проверен по 5 пунктам
(источник / актуальность / что измеряет / сопоставимость US–CN / плохой ли proxy)
и по 9 запрещённым подменам; semis — по 8 позициям; HPC — 3 типа compute;
quantum — запрет уверенных экономических выводов.
Действие: исправить / ослабить / `→ [expert assessment]` / удалить.

## 0. Общая оценка исходника

Исходный `tech_cases_comparison.md` уже честный: фиксирует MISSING AI/HPC/quantum,
запрещает trade=fab, TOP500=AI-compute, causality по CHIPS/BIS, TFP-construction.
Поэтому правки — точечные: снятие остаточных сильных формулировок, явная маркировка
qual-гипотез как [expert assessment], исправление «доли → масштаба» и trade→мощность,
ужесточение HPC/quantum, явная таблица 9 подмен. Удалений целых кейсов не потребовалось.

## 1. AI — проверки и исправления

| # | Тезис исходника | Проверка (что не так) | Действие в final |
|---|---|---|---|
| A1 | Статьи 0.76→2.17, патенты 1.21→5.44 как AI-якоря | Источник ок (WDI/WIPO, актуальны), но **плохой proxy**: general-объём ≠ AI-наука; publication volume = leadership — запрещённая подмена | Ослаблен: оставлен как «general-контекст, не AI-вердикт»; добавлен §1.1 «что измеряет»; confidence для AI-вывода → insufficient |
| A2 | «США сильнее: структура частного финансирования (BERD/GDP 2.66 vs 2.00)» | BERD — business-financed GERD, не VC/AI-$; актуально, сопоставимо частично (CN opaque). Главная ошибка: **BERD/GERD ~77% в обеих странах (2023)** — «частный vs направленный» не подтверждается; R&D spending = success — подмена | Исправлен: измеримый вердикт сужен до «интенсивности входов»; finance-модель → [expert assessment, not tested]; добавлен паритет 77% |
| A3 | «США сильнее: private AI investment и frontier models (внешний qual-сигнал)» | Источник идентифицирован (Stanford AI Index 2025, Vibrancy Tool), но **ряд не извлечён** (100% missing); CN private $ undercoverage; notable models — snapshot, не динамика | Переклассифицирован: → [expert assessment]-гипотеза, вердикт запрещён; confidence LOW/insufficient |
| A4 | «Китай сильнее: масштаб adoption через MVA ~2.5x, HS8542 3.13x» | **Плохой proxy**: MVA — доля в GDP (не абсолют), HS8542 — nominal trade с assembly-смещением; adoption в панели не измерен | Ослаблен/частично удалён: MVA/HS8542 — только «структурный контекст, не adoption»; тезис adoption → [expert assessment], LOW |
| A5 | Bottleneck: «США — перенос INN→PRD; Китай — frontier compute + конверсия в impact» | Compute-ряда нет; impact-ряда нет; BIS — маркеры, не evidence | Переклассифицирован → [expert assessment]; BIS явно как маркеры режима |
| A6 | Mechanism: «частный FIN→INN/COM vs объёмы→диффузия» (+ M1 GERD 0.028 как косвенный тест) | Регрессия finance→outputs не запускалась; pooled r=+0.16 — композиционный артефакт; M1 — агрегатный TFP, не AI-эффект | Ослаблен → qual-гипотеза, not tested; M1 упомянут только как «не AI-эффект» |
| A7 | Неявный «data/adoption advantage CN» (исходный спорный тезис №4 дизайна) | Неизмеримо в панели (proprietary data, нет adoption-ряда) | Явно запрещён в final (§1.3, Приложение) |

## 2. Semiconductors — проверки и исправления (7 стадий + третьи страны)

| # | Тезис исходника | Проверка | Действие в final |
|---|---|---|---|
| S0 | MVA «~2.5x» и IC «3.13x» как масштаб/лидерство | MVA % GDP — **доля, не абсолют** («масштаб из доли» — логическая ошибка); IC — nominal + processing trade + re-exports + карантин CHN 2015–17; CAGR +12.5% поверх разрыва смещён; manufacturing volume = leadership — подмена | **Исправлено**: везде «доля, не абсолютный выпуск»; IC — «номинал, assembly-смещ., карантин»; CAGR помечен смещённым; запрет trade=fab усилен |
| S1 | Design/IP: «США сильнее» | Источника-ряда нет (firm/архитектуры вне панели); general-патенты — плохой proxy (patent count = leadership) | Ослаблен → [expert assessment], LOW-MEDIUM |
| S2 | EDA: «США сильнее; рычаг» | Ряда нет; BIS — маркеры | Оставлен как [expert assessment], LOW; явно «рычаг, не мощность» |
| S3 | Equipment/EUV: «ключевой рычаг в руках союзников» | Верно по структуре, но риск прочтения «рычаг США» | **Уточнено**: «EUV-рычаг — у союзников (NL ASML), не у США»; SEMI-ряда нет; LOW-MEDIUM |
| S4 | Advanced fab: «слабее внутри обеих; frontier — TW/KR» + «KOR CAGR +6.5% vs JPN −0.9% косвенно» | Первое — верная qual-структура; второе — **плохой proxy** (trade ≠ мощность) | Первое оставлено как [expert assessment]; второе понижено до «trade-контекст, не fab-данные»; добавлен запрет «announced capacity = production», CHIPS Act — только намерение |
| S5 | Mature: «Китай сильнее по масштабу (MVA ~2.5x; IC 3.13x)» | См. S0: оба индикатора не измеряют mature-node мощность | Ослаблен: вердикт → [expert assessment]; MVA/IC — «лишь косвенный контекст» |
| S6 | Packaging: «Китай сильнее по объёму» | HS8542-стоимость ≠ OSAT-объём | Ослаблен → [expert assessment], MEDIUM-LOW |
| S7 | Downstream: «США — платформы; Китай — сборка (hitech share)» | Hitech — broad basket + SITC-break; processing trade | Оставлен с усиленным caveat (break, корзина); спрос на frontier-чипы → LOW |
| S8 | Третьи страны: NL/JP/TW/KR/MYS упомянуты | Верно, но исходник смешивал trade-CAGR с fab-структурой | **Усилено**: сквозная строка «без TW/KR/NL/JP — misspecification»; KOR/JPN цифры — только R&D/trade-контекст; квантификации fab-долей нет (LOW) |

Покрытие 8 требуемых позиций: design/IP ✓, EDA ✓, equipment ✓, advanced fab ✓,
mature ✓, packaging ✓, downstream ✓, third-country bottlenecks ✓ (сквозной столбец + синтез п.5).

## 3. HPC — проверки и исправления (3 типа compute)

| # | Тезис исходника | Проверка | Действие в final |
|---|---|---|---|
| H1 | Различение supercomputer vs AI-compute vs general infra | Верно и сохранено; но исходник не объяснял **почему** TOP500 плох для AI (HPL vs AI-нагрузка) и не упоминал non-reporting bias CN | **Дополнено**: Rmax=Linpack (HPL), не HPCG/HPL-MxP; hyperscale вне листа; non-reporting bias; Nov-срез |
| H2 | «США сильнее: frontier+облака; Китай сильнее: госвложения/число систем (qual-гипотезы)» | Без ряда — unverifiable; supercomputer ranking = commercial AI capability — подмена | Переклассифицировано → [expert assessment]-гипотезы, **no verdict**; добавлен запрет ranking=AI-capability и AI=productivity |
| H3 | Bottleneck/mechanism (peak→доступность; чипы; state-led dual-use) | Правдоподобно, но без ряда | Оставлено как [expert assessment]; эконом-эффект — только косвенный, не через TFP |
| H4 | «Требуется Nov TOP500-pull» | Верно, но неполно | Расширен план: count+Rmax + разделение 3 типов + AI-compute narrative |

## 4. Quantum — проверки и исправления

| # | Тезис исходника | Проверка | Действие в final |
|---|---|---|---|
| Q1 | Деление computing / communication (Micius) / sensing | Верно; сохранено и усилено (sensing — упомянуть, не оценивать) | Без изменений, формулировка ужесточена |
| Q2 | «США — computing-экосистема; Китай — communication + гос-R&D» | IPF/pubs — MISSING (EPO–OECD Dec 2025 не извлечён); funding-марки (NQI 2018, Micius/13th FYP) — не ряды; patent count = leadership и funding = commercialization — подмены; small-N волатильность | Переклассифицировано → [expert assessment]-гипотезы, **no verdict**; IPF — только после ручного CSV 2005–2024 |
| Q3 | «Экон. эффект ≈ 0 по построению» | Единственная допустимая сильная формулировка для ранней стадии | Оставлена как qual-констатация (LOW), с явным запретом приписывания TFP/экспорта |
| Q4 | Bottleneck «S/RD» (H2-ожидание) | Согласуется с дизайном, но тестировать не на чем | Помечено как coherence, не evidence (H2 insufficient) |

## 5. Сквозные исправления (цепочка + матрица + синтез)

- **Цепочка**: добавлен §0 «что измерено/нет» по 9 блокам × 4 tech — исходник описывал missing
  по кейсам, но не единой таблицей разрывов цепи (COM/ADE/productivity). Разрывы теперь явны.
- **MVA-доля**: исправлена во всех местах (AI §1.3, semis §2.1–2.2, матрица, синтез) —
  было местами «масштаб ~2.5x», стало «доля, не абсолютный выпуск».
- **BERD/GERD-паритет (~77%)**: добавлен в AI-матрицу, semis-контекст и синтез п.4 —
  в исходнике был в final_synthesis, но не в tech-кейсе; сильная finance-версия теперь явно отвергнута.
- **Матрица**: сохранена с `?` для всех insufficient-клеток; mature-строка и ADE-строки получили
  явные caveat-подписи (доля/номинал/assembly/SITC-break); HPC-строка — подпись Linpack≠AI;
  quantum COM/PRD/ADE — ~0 (qual).
- **Синтез**: п.1–6 сохранены по существу; п.4 (finance) ослаблен паритетом 77%;
  п.5 (третьи страны) — trade-цифры понижены до контекста; п.6 (decoupling) — без изменений
  (уже корректно как маркеры, n=2, downturn).
- **Приложение 9 подмен**: новое — в исходнике запреты были рассыпаны по тексту;
  теперь явная disposition-таблица (требование ТЗ).
- **Ничего не удалено целиком**: все 4 кейса сохранены; удалены только сильные прочтения
  («AI-adoption измерен», «IC = fab», «CAGR поверх разрыва как чистый тренд»,
  «finance-модель подтверждена», «HPC/quantum-вердикты»).

## 6. Остаточные риски (не устранены данными, зафиксированы как limitations)

AI/HPC/quantum-ряды отсутствуют; SEMI/PCT-semis/VC/adoption/COM — нет; HS8542 требует
single-definition pull; TOP500 — Nov-pull; AI Index — audited export; quantum IPF — ручной CSV;
hitech-trend поверх SITC-break невалиден; M1 — слабый/хрупкий (GERD CI∋0, HC t раздут, USA=1).
Causal-язык запрещён. Это зафиксировано в final §Limitations, а не «исправлено» словами.

## 7. Файлы

- `technology_cases_final.md` — исправленная версия (этот ревью).
- `technology_changes.md` — этот файл.
- Исходник без изменений: `reports/tech_cases_comparison.md`.

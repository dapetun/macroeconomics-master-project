# DATA_SOURCES_CHEATSHEET — откуда данные и зачем

Шпаргалка для защиты. Язык простой: **R&D** вместо GERD в устной речи.  
Числа смотри в `dual_scale_with_absolutes.csv` / `DATA_CANON.md`. Здесь — **источники и ссылки**.

---

## Как читать таблицу

| Колонка | Смысл |
|---------|--------|
| **Зачем в проекте** | Какой узкий вопрос закрывает показатель |
| **Где лежит у нас** | Файл в репозитории |
| **Ссылка** | Страница / API, откуда тянули или куда вести преподавателя |

---

## 1. Макроцепочка (основные ряды панели)

### Доля R&D в ВВП

| | |
|--|--|
| **Что измеряет** | Какую долю ВВП страна тратит на исследования и разработки |
| **Зачем** | Сравнить «насколько интенсивно» экономика вкладывается в R&D |
| **Код / имя** | World Bank `GB.XPD.RSDV.GD.ZS` → у нас `gerd_pct_gdp` |
| **Где в проекте** | `data/raw/gerd_pct_gdp.csv` |
| **Ссылка** | https://data.worldbank.org/indicator/GB.XPD.RSDV.GD.ZS |
| **API (как качали)** | https://api.worldbank.org/v2/ |
| **Не путать с** | Абсолютными расходами на R&D (OECD, ниже) |

### Абсолютные расходы на R&D (в PPP)

| | |
|--|--|
| **Что измеряет** | Сколько денег в сумме уходит на R&D (млн USD по паритету покупательной способности) |
| **Зачем** | Показать объём вложений, а не только долю |
| **Источник** | OECD MSTI |
| **Где в проекте** | `data/raw/oecd_gerd_usd_ppp.csv` |
| **Ссылка (витрина OECD)** | https://data-explorer.oecd.org/vis?df[ag]=OECD.STI.STP&df[id]=DSD_MSTI@DF_MSTI |
| **API** | https://sdmx.oecd.org/public/rest/v1/data/DSD_MSTI@DF_MSTI |
| **Важно** | Не делить/не умножать вместе с World Bank долей R&D — разные винтажи |

### R&D, выполненный бизнесом (% ВВП)

| | |
|--|--|
| **Что измеряет** | Доля ВВП, соответствующая R&D, **выполненному** в бизнес-секторе |
| **Зачем** | Ещё один вход по R&D; **не** «кто заплатил» |
| **Код** | OECD MSTI `P_BERPCT` → у нас `berd_pct_gdp` |
| **Где** | `data/raw/oecd_berd_pct_gdp.csv` |
| **Ссылка** | https://data-explorer.oecd.org/vis?df[ag]=OECD.STI.STP&df[id]=DSD_MSTI@DF_MSTI |
| **Не говорить** | «Частная модель финансирования» / finance mix |

### Исследователи на миллион жителей

| | |
|--|--|
| **Что измеряет** | Плотность кадров R&D в населении |
| **Зачем** | Человеческий капитал как интенсивность |
| **Код** | World Bank `SP.POP.SCIE.RD.P6` |
| **Где** | `data/raw/researchers_per_million.csv` |
| **Ссылка** | https://data.worldbank.org/indicator/SP.POP.SCIE.RD.P6 |
| **UIS (первичный контур)** | https://databrowser.uis.unesco.org/resources/bulk |

### Оценка численности исследователей

| | |
|--|--|
| **Что измеряет** | Грубая оценка «сколько человек» ≈ (на миллион) × (население) |
| **Зачем** | Абсолютный слой к плотности |
| **Как считали** | `researchers_per_million × население_PWT_в_миллионах / 1000` |
| **Население** | `data/raw/pwt_pop.csv` из Penn World Table |
| **PWT сайт** | https://www.rug.nl/ggdc/productivity/pwt/ |
| **Это не** | Официальная перепись исследователей |

### Научные статьи (объём)

| | |
|--|--|
| **Что измеряет** | Число статей S&E (дробный count) |
| **Зачем** | Объём научной активности |
| **Основной свежий ряд USA/CHN (2014–2024)** | NSF *State of U.S. Science and Engineering 2026*, Figure 29 |
| **Где** | `data/raw/nsf_se_articles_indicators2026.csv` |
| **Ссылка NSF** | https://ncses.nsf.gov/pubs/nsbsep20261/discovery-r-d-activity-and-research-publications-2 |
| **Старый/дополнительный ряд WB** | `IP.JRN.ARTC.SC` → `data/raw/scopus_articles.csv` |
| **Ссылка WB** | https://data.worldbank.org/indicator/IP.JRN.ARTC.SC |
| **Не значит** | Качество науки / лидерство / внедрение |

### Патенты

| | |
|--|--|
| **Что измеряет** | Число патентных заявок в национальном ведомстве |
| **Зачем** | Объём инновационной активности (counts) |
| **Коды WB** | Резиденты: `IP.PAT.RESD`; нерезиденты: `IP.PAT.NRES` |
| **Где** | `data/raw/patents_resident.csv`, `data/raw/patents_nonresident.csv` |
| **Ссылка (резиденты)** | https://data.worldbank.org/indicator/IP.PAT.RESD |
| **Ссылка (нерезиденты)** | https://data.worldbank.org/indicator/IP.PAT.NRES |
| **WIPO (контекст)** | https://www3.wipo.int/ipstats/ |
| **Правило на защите** | Всегда пара: resident **и** total office (сумма) |

### Доля обрабатывающей промышленности в ВВП

| | |
|--|--|
| **Что измеряет** | Насколько велика обрабатывающая промышленность относительно ВВП |
| **Зачем** | Грубая картинка «промышленности» экономики |
| **Код** | World Bank `NV.IND.MANF.ZS` |
| **Где** | `data/raw/mva_pct_gdp.csv` |
| **Ссылка** | https://data.worldbank.org/indicator/NV.IND.MANF.ZS |
| **Не значит** | Абсолютный выпуск заводов / производство чипов |

### Доля высокотехнологичного экспорта

| | |
|--|--|
| **Что измеряет** | Долю hi-tech в экспорте промтоваров |
| **Зачем** | Поздний блок «выход на внешний рынок» |
| **Код** | World Bank `TX.VAL.TECH.MF.ZS` |
| **Где** | `data/raw/hitech_export_share.csv` |
| **Ссылка** | https://data.worldbank.org/indicator/TX.VAL.TECH.MF.ZS |
| **Осторожно** | Смена классификации; не равно «внедрению внутри страны» |

### Экспорт интегральных схем (чипы в торговле)

| | |
|--|--|
| **Что измеряет** | Стоимость экспорта по коду HS8542 (доллары) |
| **Зачем** | Единственный нормальный tech-ряд в панели по чипам (торговля) |
| **Где** | `data/raw/comtrade_hs8542_exports.csv` |
| **Ссылка** | https://comtradeplus.un.org/ |
| **Не значит** | Где стоят fab, на каких техпроцессах, кто контролирует производство |
| **Дыра** | Тайваня в панели нет |

### ВВП на человека

| | |
|--|--|
| **Что измеряет** | Уровень дохода на человека (PPP) |
| **Зачем** | Макрофон сравнения стран |
| **Код** | World Bank `NY.GDP.PCAP.PP.KD` |
| **Где** | `data/raw/gdp_pc_ppp.csv` |
| **Ссылка** | https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD |

### Производительность (TFP)

| | |
|--|--|
| **Что измеряет** | Совокупную факторную производительность (индекс) |
| **Зачем** | Макроитог; в приложении — зависимая переменная регрессии |
| **Источник** | Penn World Table (`ctfp`) |
| **Где** | `data/raw/pwt_ctfp.csv` |
| **Ссылка** | https://www.rug.nl/ggdc/productivity/pwt/ |
| **Важно** | У США в этой конструкции часто **1.0** — это устройство данных, не «результат исследования» |

---

## 2. Снимки по четырём технологиям (не полная панель)

### ИИ — Stanford AI Index 2025

| | |
|--|--|
| **Зачем** | Точки: доля AI-статей, цитат, частные инвестиции, заметные модели, доля AI-патентов |
| **Где у нас** | `data/raw/snapshots/ai_index_snapshot.csv` |
| **Отчёт** | https://hai.stanford.edu/ai-index/2025-ai-index-report |
| **Глава R&D (контекст)** | https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development |
| **Статус** | Снимок / exploratory, не длинный ряд нашей панели |

### Суперкомпьютеры — TOP500

| | |
|--|--|
| **Зачем** | Сколько систем страны в рейтинге (2015 и 2025) |
| **Где** | `data/raw/snapshots/top500_snapshot.csv` |
| **Списки** | https://www.top500.org/lists/top500/ |
| **Nov 2015 highlights** | https://new.top500.org/lists/top500/2015/11/highlights/ |
| **Nov 2025 list** | https://top500.org/lists/top500/list/2025/11/ |
| **Сводка по странам (2025, secondary)** | https://www.visualcapitalist.com/ranked-countries-most-supercomputers/ |
| **Не значит** | Облачные мощности для обучения ИИ |

### Квант — EPO–OECD

| | |
|--|--|
| **Зачем** | Точки по международным патентным семьям / публикациям |
| **Где** | `data/raw/snapshots/quantum_epo_oecd_snapshot.csv` |
| **Публикация OECD** | https://www.oecd.org/en/publications/mapping-the-global-quantum-ecosystem_010c37da-en.html |
| **PDF исследования** | https://link.epo.org/web/publications/studies/en-mapping-the-global-quantum-ecosystem.pdf |
| **Пресс-релиз EPO** | https://www.epo.org/en/news-events/press-centre/press-release/2025/1361562 |
| **Не значит** | Коммерческий или макроэкономический эффект |

---

## 3. Сводная карта «вопрос → данные → ссылка»

| Вопрос на защите | Показатель | Куда ткнуть пальцем |
|------------------|------------|---------------------|
| Сколько R&D относительно экономики? | Доля R&D в ВВП | https://data.worldbank.org/indicator/GB.XPD.RSDV.GD.ZS |
| Сколько R&D в деньгах? | R&D PPP | https://data-explorer.oecd.org/vis?df[ag]=OECD.STI.STP&df[id]=DSD_MSTI@DF_MSTI |
| Где гуще исследователи? | На миллион | https://data.worldbank.org/indicator/SP.POP.SCIE.RD.P6 |
| Кто больше публикует? | Статьи NSF Fig.29 | https://ncses.nsf.gov/pubs/nsbsep20261/discovery-r-d-activity-and-research-publications-2 |
| Кто больше патентует? | Патенты WB | https://data.worldbank.org/indicator/IP.PAT.RESD |
| Насколько промышленная экономика? | MVA % ВВП | https://data.worldbank.org/indicator/NV.IND.MANF.ZS |
| Какой hi-tech экспорт? | Hi-tech share | https://data.worldbank.org/indicator/TX.VAL.TECH.MF.ZS |
| Что с торговлей чипами? | Comtrade HS8542 | https://comtradeplus.un.org/ |
| Что с ИИ точечно? | AI Index | https://hai.stanford.edu/ai-index/2025-ai-index-report |
| Что с суперкомпьютерами? | TOP500 | https://www.top500.org/lists/top500/ |
| Что с квантом точечно? | EPO–OECD | https://www.oecd.org/en/publications/mapping-the-global-quantum-ecosystem_010c37da-en.html |
| Производительность / доход | PWT + WB GDP pc | https://www.rug.nl/ggdc/productivity/pwt/ · https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD |

---

## 4. Готовый ответ преподавателю

> «Основные макропоказатели — World Bank и OECD; производительность — Penn World Table; торговля чипами — UN Comtrade. По ИИ, суперкомпьютерам и кванту у нас не полная панель 2010–2023, а точечные выписки из AI Index, TOP500 и отчёта EPO–OECD. Конкретные файлы и годы — в `DATA_CANON.md` и `SNAPSHOT_SOURCE_LEDGER.md`.»

Не обязательно повторять дословно. Важно уметь назвать **источник + что он измеряет + чего не измеряет**.

---

*Файл для устной подготовки. Авторитет чисел — `DATA_CANON.md`, не этот список ссылок.*

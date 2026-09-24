# Data Map — US vs China: технологическое соперничество

> Агент: data-map | Версия: 1.0 | Дата: 2026-09-12  
> Горизонт анализа: **2010–2023/2024** (где доступно)  
> Ядро: **USA, China** | Comparators: **TWN, KOR, JPN, DEU, GBR, ISR** (+ FRA опционально)

> ⛔ **SUPERSEDED panel composition (2026-09-20, DataCanonAgent).**  
> Фактическая панель: USA, CHN, KOR, JPN, DEU, GBR, ISR, **FRA** — **без TWN**.  
> Не добавлять TWN. Labels: BERD = **PERFORMED** (`DATA_CANON.md`); словарь → `data/metadata/data_dictionary.csv` (выровнен).  
> Этот файл = planned map / intent, не фактический panel roster.

---

## 0. Проверка research design предыдущего агента

### Что оставляем без изменений
- Единая схема **TCI** (8 блоков S→ADE) — компактная и достаточная.
- 3 метода: index/gap, pooled OLS (8–10 стран), trend comparison US vs CN.
- 4 технологических кейса как **stress tests**, а не отдельные исследования.
- Явный отказ от causal claims, IV, synthetic control, sectoral TFP decomposition.

### Что сокращено (упрощение)

| Было в research design | Решение | Причина |
|------------------------|---------|---------|
| 15 core + field-specific × 4 технологии | **12 core + 4 tech-модуля** (по 2–3 показателя на tech) | Перегруз; 4×4 field publications/patents = 16 доп. рядов |
| STEM graduates | **Убрано** | Слабая сопоставимость CN; дублирует researchers |
| Field-specific publications (4 поля) | **1 агрегат** (Scopus via WB) + tech-метрики в TECH DATA | Один источник, меньше ручной работы |
| Government R&D + Finance mix (отдельно) | **Объединено**: GERD + Business-financed GERD (% GDP) | Оба из OECD MSTI, один download |
| VC (PitchBook/CB Insights) | **Downgrade → SHOULD**; proxy через Stanford AI Index | CN данные неполные; платные источники |
| SEMI fab capacity / advanced nodes | **Заменено**: trade HS854 + qualitative | SEMI World Fab Forecast — платный/ограниченный |
| Triadic patents + USPTO/EPO family | **Resident patent applications (WIPO origin)** | Проще, покрывает US+CN+comparators |
| Elastic Net / Lasso | **OPTIONAL** (не в Data Map) | Только если OLS нестабилен |
| Quantum qubit milestones (quant) | **Qualitative timeline** в POLICY/qual layer | Несопоставимые определения «qubit» |

### Итоговая логика Data Map
- **12 переменных CORE** — строят TCI и cross-country regressions.
- **TECH DATA** — 2–3 показателя на AI / semis / HPC / quantum (не входят в core count).
- **POLICY DATA** — даты событий для narrative, не для DiD.
- Все источники проверены на актуальность (сентябрь 2026).

---

## 1. CORE DATASET (12 переменных)

### 1.1 `gdp_pc_ppp`

| Поле | Значение |
|------|----------|
| **Понятное название** | ВВП на душу населения (ППС, constant intl $) |
| **Economic meaning** | Уровень экономического развития и потребительских возможностей |
| **Analytical role** | Базовый макро-контроль; denominator для per-capita метрик |
| **Stage** | Productivity / macro outcome |
| **Source** | Penn World Table 11.0 |
| **Dataset** | `rgdpe` / `pop` → rgdpe/pop или готовый `rgdpo` per capita |
| **URL** | https://www.rug.nl/ggdc/productivity/pwt/ |
| **Countries** | 185 (включая USA, CHN, TWN*, KOR, JPN, DEU, GBR, ISR, FRA) |
| **Industry** | n/a |
| **Years** | 1950–2023 |
| **Frequency** | Annual |
| **Unit** | 2021 intl $ per person |
| **Format** | CSV/Excel/Stata, long panel: country-year |
| **US–CN comparable** | Да (PPP); для CN использовать **official GDP series** (не Wu) в PWT 11.0 |
| **Missing values** | Мало для core countries |
| **Methodological problems** | PWT 11.0 перешёл на official CN GDP (2025); исторические ряды пересмотрены |
| **Primary/Secondary** | Secondary (national accounts → PWT) |
| **Priority** | **MUST** |
| **Reliability** | **HIGH** |

*Taiwan в PWT как `TWN`.

**Альтернатива:** World Bank `NY.GDP.PCAP.PP.KD` — https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD (до 2024, HIGH).

---

### 1.2 `gdp_real_growth`

| Поле | Значение |
|------|----------|
| **Понятное название** | Рост реального ВВП (%) |
| **Economic meaning** | Динамика совокупного выпуска |
| **Analytical role** | Trend layer; контекст для TFP/productivity |
| **Stage** | Productivity |
| **Source** | World Bank WDI |
| **Dataset** | Indicator `NY.GDP.MKTP.KD.ZG` |
| **URL** | https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG |
| **Countries** | 200+ |
| **Years** | 1961–2024 |
| **Frequency** | Annual |
| **Unit** | % y/y |
| **Format** | CSV via API or DataBank |
| **US–CN comparable** | Да, с оговоркой по CN revisions |
| **Missing values** | Редки |
| **Methodological problems** | CN GDP revisions (NBS 2024–2025) меняют историю |
| **Primary/Secondary** | Secondary |
| **Priority** | **SHOULD** |
| **Reliability** | **HIGH** |

---

### 1.3 `labour_productivity_gdph`

| Поле | Значение |
|------|----------|
| **Понятное название** | ВВП на час отработанного времени |
| **Economic meaning** | Labor productivity — эффективность использования труда |
| **Analytical role** | Поздний этап цепочки (productivity); H4/H5 macro proxy |
| **Stage** | Productivity |
| **Source** | OECD Productivity Statistics |
| **Dataset** | Productivity levels — indicator `GDPHRS` |
| **URL** | https://data-explorer.oecd.org/vis?df[ag]=OECD.SDD.TPS&df[id]=DSD_PDB@DF_PDB_LV |
| **Countries** | OECD + **CHN** + G20 non-OECD (проверить TWN отдельно — может отсутствовать) |
| **Years** | ~1970–2023 (rolling update) |
| **Frequency** | Annual |
| **Unit** | USD PPP per hour worked |
| **Format** | SDMX/CSV |
| **US–CN comparable** | Частично: методы hours worked различаются |
| **Missing values** | TWN, ISR — проверить; fallback: `GDP per person employed` |
| **Methodological problems** | Hours data CN менее прозрачны; не sectoral |
| **Primary/Secondary** | Secondary |
| **Priority** | **MUST** |
| **Reliability** | **MEDIUM–HIGH** |

**Fallback:** PWT `rgdpna` / `avh` (hours worked) — MEDIUM reliability.

---

### 1.4 `tfp_level`

| Поле | Значение |
|------|----------|
| **Понятное название** | TFP (multifactor productivity) at national prices |
| **Economic meaning** | Residual output growth not explained by measured inputs |
| **Analytical role** | Macro outcome; «экономический эффект» цепочки (qual-quant) |
| **Stage** | Productivity |
| **Source** | Penn World Table 11.0 |
| **Dataset** | Variable `rtfpna` |
| **URL** | https://www.rug.nl/ggdc/productivity/pwt/ |
| **Countries** | 185 |
| **Years** | 1950–2023 |
| **Frequency** | Annual |
| **Unit** | Index (2021=1) or level |
| **Format** | CSV long panel |
| **US–CN comparable** | Осторожно: aggregate TFP, не tech-specific |
| **Missing values** | Мало |
| **Methodological problems** | **Не sectoral decomposition** (explicitly out of scope); CN measurement error in capital/labor |
| **Primary/Secondary** | Secondary |
| **Priority** | **SHOULD** |
| **Reliability** | **MEDIUM** |

---

### 1.5 `gerd_pct_gdp`

| Поле | Значение |
|------|----------|
| **Понятное название** | GERD — gross domestic R&D expenditure (% GDP) |
| **Economic meaning** | Совокупные ресурсы на R&D внутри страны |
| **Analytical role** | Блок RD; input для conversion INN/RD, PRD/RD |
| **Stage** | R&D |
| **Source** | OECD MSTI |
| **Dataset** | `DSD_MSTI@DF_MSTI`, measure GERD, unit `% of GDP` |
| **URL** | https://data-explorer.oecd.org/vis?df[ag]=OECD.STI.STP&df[id]=DSD_MSTI@DF_MSTI |
| **Countries** | OECD38 + **CHN**, TWN, SGP, others; KR/JP/DE/GB/IL/US — yes |
| **Years** | 1981–2024 (Mar 2026 release) |
| **Frequency** | Annual |
| **Unit** | % of GDP |
| **Format** | SDMX/CSV |
| **US–CN comparable** | Да (Frascati-based); CN via NBS → OECD |
| **Missing values** | IL, TWN — проверить timeliness |
| **Methodological problems** | CN preliminary vs final (NBS communiqué Oct); definitional drift in basic/applied split |
| **Primary/Secondary** | Secondary (OECD); CN primary: NBS |
| **Priority** | **MUST** |
| **Reliability** | **HIGH** |

**CN primary cross-check:** NBS Communiqué 2024 — https://www.stats.gov.cn/english/PressRelease/202510/t20251010_1961462.html (2.69% GDP, 2024).

---

### 1.6 `berd_pct_gdp`

| Поле | Значение |
|------|----------|
| **Понятное название** | Business-financed GERD (% GDP) |
| **Economic meaning** | Доля частного/корпоративного финансирования R&D |
| **Analytical role** | Блок FIN + RD; H3 (finance mix → stage outputs) |
| **Stage** | Finance / R&D |
| **Source** | OECD MSTI |
| **Dataset** | `DSD_MSTI@DF_MSTI`, Business-financed GERD % GDP |
| **URL** | https://data-explorer.oecd.org/vis?df[ag]=OECD.STI.STP&df[id]=DSD_MSTI@DF_MSTI |
| **Countries** | Same as GERD |
| **Years** | 1981–2024 |
| **Frequency** | Annual |
| **Unit** | % of GDP |
| **Format** | SDMX/CSV |
| **US–CN comparable** | Частично: CN business R&D reporting улучшилась, но opaque |
| **Missing values** | Similar to GERD |
| **Methodological problems** | US detail: NSF BERD vs OECD aggregate — мелкие расхождения |
| **Primary/Secondary** | Secondary |
| **Priority** | **MUST** |
| **Reliability** | **HIGH** |

**US detail (optional):** NSF Table DISC-1 — https://ncses.nsf.gov/pubs/nsb20257/downloads

---

### 1.7 `researchers_per_million`

| Поле | Значение |
|------|----------|
| **Понятное название** | Researchers in R&D (FTE per million population) |
| **Economic meaning** | Human capital для науки и R&D |
| **Analytical role** | Блок HC; input для conversion ratios |
| **Stage** | Human capital |
| **Source** | UNESCO UIS (via World Bank WDI) |
| **Dataset** | SDG 9.5.2; WB code `SP.POP.SCIE.RD.P6` |
| **URL** | https://data.worldbank.org/indicator/SP.POP.SCIE.RD.P6 |
| **Bulk download** | https://databrowser.uis.unesco.org/resources/bulk |
| **Countries** | 146+ (Feb 2026 release) |
| **Years** | 1996–2024 |
| **Frequency** | Annual |
| **Unit** | per million inhabitants |
| **Format** | CSV |
| **US–CN comparable** | Да (Frascati definition) |
| **Missing values** | TWN — может отсутствовать; lag 1–2 года для некоторых |
| **Methodological problems** | FTE vs headcount; CN surge partly reflects reclassification |
| **Primary/Secondary** | Secondary (UIS); national surveys primary |
| **Priority** | **MUST** |
| **Reliability** | **HIGH** |

---

### 1.8 `scopus_articles`

| Поле | Значение |
|------|----------|
| **Понятное название** | Scientific and technical journal articles (fractional count) |
| **Economic meaning** | Объём научного output (science) |
| **Analytical role** | Блок S/INN; science-side of H1/H4 |
| **Stage** | Science / Innovation |
| **Source** | NSF Science & Engineering Indicators → World Bank WDI |
| **Dataset** | `IP.JRN.ARTC.SC` |
| **URL** | https://data.worldbank.org/indicator/IP.JRN.ARTC.SC |
| **Countries** | 197 |
| **Years** | 1996–2023 |
| **Frequency** | Annual |
| **Unit** | fractional article count |
| **Format** | CSV |
| **US–CN comparable** | Да, но fractional counting + English bias |
| **Missing values** | Rare for US/CN |
| **Methodological problems** | **Не field-specific**; Scopus coverage; authorship inflation in CN |
| **Primary/Secondary** | Secondary |
| **Priority** | **MUST** |
| **Reliability** | **MEDIUM–HIGH** |

---

### 1.9 `patents_resident_origin`

| Поле | Значение |
|------|----------|
| **Понятное название** | Resident patent applications (by applicant origin) |
| **Economic meaning** | Инновационный output, защита IP |
| **Analytical role** | Блок INN; H4 conversion; не equate to «quality innovation» |
| **Stage** | Innovation |
| **Source** | WIPO IP Statistics Data Center |
| **Dataset** | Patents — Total count by **applicant's origin** — Resident |
| **URL** | https://www3.wipo.int/ipstats/ |
| **Publication** | WIPI 2025 tables — https://www.wipo.int/publications/en/details.jsp?id=4822 |
| **Countries** | 150+ origins |
| **Years** | 1980–2024 (complete to 2024 in WIPI 2025) |
| **Frequency** | Annual |
| **Unit** | number of applications |
| **Format** | CSV/XLSX from IP Stats DC |
| **US–CN comparable** | Частично: CN resident count inflated vs triadic |
| **Missing values** | Low for US/CN |
| **Methodological problems** | **Patent ≠ innovation**; CN utility models excluded if using «patents» only — брать **invention patents** для CN если доступно |
| **Primary/Secondary** | Secondary |
| **Priority** | **MUST** |
| **Reliability** | **MEDIUM** |

**Optional quality proxy:** PCT applications by origin — https://www.wipo.int/pressroom/en/articles/2026/article_0003.html (SHOULD).

---

### 1.10 `mva_pct_gdp`

| Поле | Значение |
|------|----------|
| **Понятное название** | Manufacturing value added (% GDP) |
| **Economic meaning** | Роль manufacturing в экономике |
| **Analytical role** | Блок PRD; production capacity macro proxy |
| **Stage** | Production / scaling |
| **Source** | UNIDO National Accounts Database / World Bank SDG |
| **Dataset** | UNIDO: MVA; WB: `NV.IND.MANF.ZS` |
| **URL** | https://stat.unido.org/data/download (dataset: national accounts) |
| **WB mirror** | https://data.worldbank.org/indicator/NV.IND.MANF.ZS |
| **Countries** | 210+ |
| **Years** | 1990–2022 (UNIDO); WB may lag |
| **Frequency** | Annual |
| **Unit** | % of GDP |
| **Format** | CSV |
| **US–CN comparable** | Да |
| **Missing values** | Last 1–2 years — UNIDO nowcast |
| **Methodological problems** | Not high-tech specific; CN manufacturing vs services reclassification |
| **Primary/Secondary** | Secondary |
| **Priority** | **MUST** |
| **Reliability** | **MEDIUM–HIGH** |

---

### 1.11 `hitech_export_share`

| Поле | Значение |
|------|----------|
| **Понятное название** | High-technology exports (% manufactured exports) |
| **Economic meaning** | Export sophistication / tech intensity of manufacturing exports |
| **Analytical role** | Блок ADE; H5 dependent variable candidate |
| **Stage** | Adoption / export |
| **Source** | World Bank WDI (from UN Comtrade) |
| **Dataset** | `TX.VAL.TECH.MF.ZS` |
| **URL** | https://data.worldbank.org/indicator/TX.VAL.TECH.MF.ZS |
| **Countries** | 200+ |
| **Years** | 1988–2024 |
| **Frequency** | Annual |
| **Unit** | % of manufactured exports |
| **Format** | CSV |
| **US–CN comparable** | Да, но definition changed Oct 2024 (SITC Rev.4) — **не смешивать** старые/новые без проверки |
| **Missing values** | Rare |
| **Methodological problems** | **Broad high-tech basket**, not semis/AI specific; processing trade distorts CN |
| **Primary/Secondary** | Secondary |
| **Priority** | **MUST** |
| **Reliability** | **MEDIUM** |

---

### 1.12 `gvc_foreign_va_share`

| Поле | Значение |
|------|----------|
| **Понятное название** | Foreign value added share of gross exports (%) |
| **Economic meaning** | GVC backward participation — зависимость экспорта от imported inputs |
| **Analytical role** | Блок ADE/PRD; decoupling narrative (qual+quant) |
| **Stage** | Export / GVC |
| **Source** | OECD TiVA 2025 edition |
| **Dataset** | Principal indicators — `EXGR_FVASH` (total economy or manufacturing) |
| **URL** | https://data-explorer.oecd.org/vis?df[ag]=OECD.STI.PIE&df[id]=DSD_TIVA@DF_TIVA |
| **Countries** | 81 economies (incl. **CHN**, USA; **TWN** — verify) |
| **Years** | 1995–2022/2023 (check latest in 2025 edition) |
| **Frequency** | Annual |
| **Unit** | % |
| **Format** | SDMX/CSV |
| **US–CN comparable** | Да within TiVA framework |
| **Missing values** | 2-year lag; IL/TWN coverage limited |
| **Methodological problems** | ICIO revision-sensitive; not product-specific (semis) |
| **Primary/Secondary** | Secondary |
| **Priority** | **SHOULD** |
| **Reliability** | **MEDIUM–HIGH** |

---

## 2. TECHNOLOGY DATA (отдельные модули)

> Не входят в 12 core, но нужны для 4 кейсов и TCI tech-profiles.

### 2.1 AI

#### `ai_publications_count`
| Поле | Значение |
|------|----------|
| **Название** | AI research publications (country total) |
| **Stage** | Science / INN |
| **Source** | Stanford AI Index / Global AI Vibrancy Tool |
| **Dataset** | AI Metrics Over Time — publications |
| **URL** | https://hai.stanford.edu/ai-index/global-vibrancy-tool |
| **Report** | AI Index 2025 — https://doi.org/10.48550/arxiv.2504.07139 |
| **Countries** | 36 ranked + 66 with partial metrics |
| **Years** | 2010–2024 |
| **Unit** | count |
| **Comparable US–CN** | Да (consistent methodology within Index) |
| **Problems** | Field definition evolves; not peer-reviewed primary data |
| **Priority** | **MUST** (for AI case) |
| **Reliability** | **MEDIUM** |

#### `ai_private_investment`
| Поле | Значение |
|------|----------|
| **Название** | Private investment in AI (USD) |
| **Stage** | Finance / COM |
| **Source** | Stanford AI Index |
| **Dataset** | Economy pillar — private investment |
| **URL** | https://hai.stanford.edu/ai-index/global-vibrancy-tool |
| **Countries** | US, CN, UK, IL, etc. (partial) |
| **Years** | ~2013–2024 |
| **Unit** | USD billions |
| **Comparable US–CN** | **Partial** — CN private $ often underestimated |
| **Problems** | Proprietary deal data; VC definition |
| **Priority** | **SHOULD** |
| **Reliability** | **MEDIUM–LOW** for CN |

#### `ai_notable_models` (OPTIONAL)
| Поле | Значение |
|------|----------|
| **Название** | Count of notable AI models by country |
| **Stage** | COM / INN |
| **Source** | Stanford AI Index 2026 R&D chapter |
| **URL** | https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development |
| **Years** | 2023–2025 snapshot |
| **Unit** | count |
| **Priority** | **OPTIONAL** (qualitative snapshot) |
| **Reliability** | **MEDIUM** |

---

### 2.2 Semiconductors

#### `semi_exports_hs8542`
| Поле | Значение |
|------|----------|
| **Название** | Exports of electronic integrated circuits (HS8542) |
| **Stage** | ADE / PRD |
| **Source** | UN Comtrade Plus |
| **Dataset** | Trade flows — HS `8542` (or subcodes 854231, 854232) |
| **URL** | https://comtradeplus.un.org/ |
| **Countries** | All reporters; key: USA, CHN, TWN, KOR, MYS |
| **Years** | 2010–2024 |
| **Unit** | USD thousands |
| **Format** | API/CSV (free tier: limits apply) |
| **Comparable US–CN** | Да для trade values; **re-exports** distort (HK, SG) |
| **Problems** | HS854231 = processors; not equal to «advanced nodes» |
| **Priority** | **MUST** (for semis case) |
| **Reliability** | **HIGH** for trade values |

#### `semi_pct_exports` (OPTIONAL)
| Поле | Значение |
|------|----------|
| **Название** | HS8542 as % total exports |
| **Source** | UN Comtrade / OEC derived |
| **URL** | https://oec.world/en/profile/hs/processor-controller-integrated-circuits |
| **Priority** | **OPTIONAL** |
| **Reliability** | **MEDIUM** |

#### `semi_pct_patents` (WIPO PCT)
| Поле | Значение |
|------|----------|
| **Название** | Semiconductor technology PCT applications |
| **Stage** | INN |
| **Source** | WIPO PCT Yearly Review 2026 / IP Stats DC by technology field |
| **URL** | https://www.wipo.int/pressroom/en/articles/2026/article_0003.html |
| **Years** | 2010–2025 |
| **Unit** | applications |
| **Priority** | **SHOULD** |
| **Reliability** | **MEDIUM** |

**Qualitative (не quantitative row):** fab capacity, EUV dependency — industry reports (SEMI, IC Insights) — narrative only.

---

### 2.3 HPC (Supercomputers)

#### `hpc_top500_systems`
| Поле | Значение |
|------|----------|
| **Название** | Number of TOP500 systems by country |
| **Stage** | PRD / scaling |
| **Source** | TOP500.org |
| **Dataset** | List Statistics → Countries/Regions |
| **URL** | https://www.top500.org/statistics/list/ |
| **List** | Nov 2025 — https://top500.org/lists/top500/list/2025/11/ |
| **Countries** | All with listed systems |
| **Years** | Biannual 2010–2025 (aggregate annually: max or Nov snapshot) |
| **Unit** | count |
| **Format** | CSV export from list / manual scrape |
| **Comparable US–CN** | **Да** — один из лучших tech-specific рядов |
| **Problems** | Excludes cloud AI clusters; PRC vs «China» sites |
| **Priority** | **MUST** (for HPC case) |
| **Reliability** | **HIGH** |

#### `hpc_top500_rmax`
| Поле | Значение |
|------|----------|
| **Название** | Aggregate Rmax of TOP500 systems by country |
| **Stage** | PRD |
| **Source** | TOP500.org List Statistics |
| **URL** | https://www.top500.org/statistics/list/ |
| **Unit** | PFlop/s (sum Rmax) |
| **Years** | 2010–2025 |
| **Priority** | **SHOULD** |
| **Reliability** | **HIGH** |

---

### 2.4 Quantum

#### `quantum_ipf_count`
| Поле | Значение |
|------|----------|
| **Название** | Quantum international patent families (IPF) |
| **Stage** | S / INN (early-stage tech) |
| **Source** | EPO–OECD «Mapping the global quantum ecosystem» (Dec 2025) |
| **URL** | https://www.oecd.org/en/publications/mapping-the-global-quantum-ecosystem_010c37da-en.html |
| **PDF/data** | https://link.epo.org/web/publications/studies/en-mapping-the-global-quantum-ecosystem.pdf |
| **Countries** | US, CN, JP, DE, UK, CA, KR, etc. |
| **Years** | 2005–2024 (annual in report figures) |
| **Unit** | IPF count |
| **Format** | Extract from report tables/charts → manual CSV |
| **Comparable US–CN** | Да within study |
| **Problems** | **Manual extraction**; early-stage noise; small counts |
| **Priority** | **SHOULD** |
| **Reliability** | **MEDIUM** |

#### `quantum_publications` (OPTIONAL)
| Поле | Значение |
|------|----------|
| **Название** | Quantum-related scientific publications |
| **Source** | Same EPO-OECD report (2012–2022 figures) |
| **Priority** | **OPTIONAL** |
| **Reliability** | **MEDIUM** |

**Qualitative:** qubit milestones, national program funding — POLICY + narrative.

---

## 3. POLICY DATA (события для narrative / timing)

> **Не для causal DiD.** Использовать как маркеры regime shifts в qual layer и optional vertical lines on charts.

| event_id | date | country | event | relevance | source |
|----------|------|---------|-------|-----------|--------|
| `mic2025` | 2015-05 | CN | Made in China 2025 | Industrial policy / semis, HPC | State Council — http://www.gov.cn/ |
| `cn_quantum_mega` | 2016-08 | CN | Micius satellite / 13th FYP quantum emphasis | Quantum S/RD | MOST, media + OECD quantum report |
| `us_chips_act` | 2022-08-09 | US | CHIPS and Science Act signed | Semis PRD/finance | Congress.gov — Pub.L. 117-167 |
| `us_bis_oct22` | 2022-10-07 | US | BIS advanced computing & semis export controls | Semis/HPC decoupling | BIS Federal Register |
| `us_bis_oct23` | 2023-10-17 | US | BIS updated export controls (AI chips) | AI + semis ADE | BIS |
| `cn_dual_circulation` | 2020-05 | CN | Dual Circulation strategy | GVC / ADE | CPC Central Committee |
| `eu_chips_act` | 2023-09-21 | EU | EU Chips Act in force | Comparator context (DE) | EUR-Lex |
| `kr_k_chips` | 2023-03 | KR | K-Chips Act | Comparator (KOR) | MSIT Korea |
| `us_nqia` | 2018-12 | US | National Quantum Initiative Act | Quantum FIN/RD | NIST — https://www.quantum.gov/ |
| `cn_nbs_rd_revision` | 2025-10 | CN | NBS final 2024 R&D communiqué | Data interpretation | https://www.stats.gov.cn/english/PressRelease/202510/t20251010_1961462.html |

---

## 4. DATA QUALITY RISKS — что нельзя напрямую сравнивать

| Risk | Variables affected | Why | Mitigation |
|------|-------------------|-----|------------|
| **Patent quantity ≠ quality** | `patents_resident_origin`, tech patents | CN utility vs invention; filing subsidies | Use PCT subset; discuss qualitatively; ratios not levels |
| **Publication volume ≠ impact** | `scopus_articles`, `ai_publications_count` | Authorship inflation; English bias | Mention citations (AI Index) qualitatively only |
| **High-tech export definition change** | `hitech_export_share` | WB updated SITC Rev.4 Oct 2024 | Single consistent series; note break |
| **Processing trade** | `hitech_export_share`, `semi_exports_hs8542` | CN/HK re-exports | Compare USA vs CN trends; use origins where possible |
| **VC / private AI investment** | `ai_private_investment` | CN opaque; deal-level bias | US–CN gap as illustrative; not regression core |
| **Aggregate TFP** | `tfp_level` | Not tech-decomposed; input mismeasurement | Macro context only; no sector claims |
| **Labor productivity hours** | `labour_productivity_gdph` | CN hours data quality | Prefer ratios US/CN over levels; OECD metadata |
| **GDP CN revisions** | `gdp_*`, GERD intensity | NBS historical GDP revision 2024–2025 | Use latest OECD/NBS; note breaks |
| **TOP500 ≠ cloud AI compute** | `hpc_*` | Hyperscale AI training largely off-list | Pair with AI Index compute narrative |
| **TiVA lag & revisions** | `gvc_foreign_va_share` | 2–3 year lag; ICIO changes | Use as structural indicator 2010–2020 |
| **Quantum small-N** | `quantum_ipf_count` | Early stage, volatile | Descriptive only; wide confidence qualitatively |
| **Semis trade ≠ fab capacity** | `semi_exports_hs8542` | Trade reflects assembly vs leading-edge fab | Qualitative fab section; TW/KR context |

---

## 5. MINIMUM VIABLE DATASET (MVD)

> Минимум, без которого проект **можно завершить** (TCI + US–CN gap + 1 cross-country regression).

| # | variable_name | Why essential |
|---|---------------|---------------|
| 1 | `gerd_pct_gdp` | Core input RD |
| 2 | `researchers_per_million` | Core input HC |
| 3 | `scopus_articles` | Core output science |
| 4 | `patents_resident_origin` | Core output INN |
| 5 | `mva_pct_gdp` | Core PRD macro |
| 6 | `hitech_export_share` | Core ADE |
| 7 | `hpc_top500_systems` | Tech case HPC (measurable) |
| 8 | `semi_exports_hs8542` | Tech case semis |
| 9 | `ai_publications_count` | Tech case AI |
| 10 | `gdp_pc_ppp` | Macro normalization |

**MVD = 10 переменных.** Остальное улучшает H3/H5 и GVC narrative.

---

## 6. Сводная таблица

| Variable | Source | Years | Countries | Unit | Purpose | Priority | Reliability |
|----------|--------|-------|-----------|------|---------|----------|-------------|
| `gdp_pc_ppp` | PWT 11.0 | 1950–2023 | 185 | 2021 intl$/person | Macro level / normalize | MUST | HIGH |
| `gdp_real_growth` | WB WDI NY.GDP.MKTP.KD.ZG | 1961–2024 | 200+ | % | Macro dynamics | SHOULD | HIGH |
| `labour_productivity_gdph` | OECD PDB GDPHRS | ~1970–2023 | OECD+CHN | USD PPP/hour | Productivity outcome | MUST | MED-HIGH |
| `tfp_level` | PWT 11.0 rtfpna | 1950–2023 | 185 | index | TFP macro proxy | SHOULD | MEDIUM |
| `gerd_pct_gdp` | OECD MSTI | 1981–2024 | OECD+CHN+ | % GDP | R&D input | MUST | HIGH |
| `berd_pct_gdp` | OECD MSTI | 1981–2024 | OECD+CHN+ | % GDP | Finance/R&D mix | MUST | HIGH |
| `researchers_per_million` | UNESCO UIS / WB | 1996–2024 | 146+ | per mln | Human capital | MUST | HIGH |
| `scopus_articles` | NSF→WB IP.JRN.ARTC.SC | 1996–2023 | 197 | fractional count | Science output | MUST | MED-HIGH |
| `patents_resident_origin` | WIPO IP Stats DC | 1980–2024 | 150+ | applications | Innovation output | MUST | MEDIUM |
| `mva_pct_gdp` | UNIDO / WB NV.IND.MANF.ZS | 1990–2022 | 210+ | % GDP | Manufacturing capacity | MUST | MED-HIGH |
| `hitech_export_share` | WB TX.VAL.TECH.MF.ZS | 1988–2024 | 200+ | % mfg exports | Export sophistication | MUST | MEDIUM |
| `gvc_foreign_va_share` | OECD TiVA EXGR_FVASH | 1995–2022 | 81 | % | GVC participation | SHOULD | MED-HIGH |
| `ai_publications_count` | Stanford AI Index | 2010–2024 | 36–66 | count | AI science case | MUST* | MEDIUM |
| `ai_private_investment` | Stanford AI Index | ~2013–2024 | partial | USD bn | AI finance case | SHOULD | MED-LOW |
| `semi_exports_hs8542` | UN Comtrade | 2010–2024 | all | USD | Semis trade case | MUST* | HIGH |
| `hpc_top500_systems` | TOP500.org | 2010–2025 | listed | count | HPC case | MUST* | HIGH |
| `hpc_top500_rmax` | TOP500.org | 2010–2025 | listed | PFlop/s | HPC capacity | SHOULD | HIGH |
| `quantum_ipf_count` | EPO-OECD 2025 | 2005–2024 | ~20 | IPF | Quantum case | SHOULD | MEDIUM |

\*MUST для соответствующего tech case; не все входят в 12 core.

---

## 7. Рекомендуемый минимальный dataset для проекта

### Для quantitative core (скачать в Phase 1)
1. **OECD MSTI** — GERD + Business-financed GERD + Researchers (if duplicated)
2. **World Bank WDI bulk** — `SP.POP.SCIE.RD.P6`, `IP.JRN.ARTC.SC`, `TX.VAL.TECH.MF.ZS`, `NV.IND.MANF.ZS`, `NY.GDP.PCAP.PP.KD`
3. **PWT 11.0** — `rgdpe`, `pop`, `rtfpna`, `avh` (fallback productivity)
4. **WIPO IP Stats** — resident patent applications by origin (CSV)
5. **TOP500** — Nov lists 2010–2025, aggregate by country
6. **UN Comtrade** — HS8542 exports, reporters USA/CHN/TWN/KOR, 2010–2024
7. **Stanford AI Index** — AI publications + private investment (manual export from Vibrancy Tool)
8. **OECD Productivity** — GDPHRS for US, CN, DE, JP, KR, GB, IL

### Для comparators panel (H3, H5)
USA, CHN, TWN, KOR, JPN, DEU, GBR, ISR — **8 стран** (minimum N for pooled OLS).

### Порядок сбора (для следующего агента)
```
Phase 1a (½ день): WB bulk + PWT + OECD MSTI → data/raw/macro/
Phase 1b (½ день): WIPO patents + TOP500 + Comtrade → data/raw/tech/
Phase 1c (¼ дня):  Stanford AI Index + EPO-OECD quantum extract → data/raw/tech/
Phase 1d (¼ дня):  Policy events CSV → data/raw/policy_events.csv
Phase 2:           Harmonize ISO3 codes, 2010–2023 window, document gaps
```

### Файловая структура (рекомендация)
```
data/
  raw/
    oecd_msti.csv
    wb_wdi_selected.csv
    pwt11.csv
    wipo_patents_origin.csv
    top500_by_country.csv
    comtrade_hs8542.csv
    stanford_ai_index.csv
    quantum_epo_oecd.csv
    policy_events.csv
  processed/
    core_panel.csv          # 12 vars × 8 countries × years
    tech_panel.csv          # tech-specific
    tci_scores.csv          # Phase 2 output
  metadata/
    sources.yaml            # URLs, download dates, known breaks
    gaps_log.md             # missing values documentation
```

---

## 8. Mapping variables → TCI blocks

| TCI block | Core variables | Tech variables |
|-----------|---------------|----------------|
| **S** Science | `scopus_articles` | `ai_publications_count`, `quantum_ipf_count` |
| **HC** | `researchers_per_million` | — |
| **RD** | `gerd_pct_gdp` | — |
| **FIN** | `berd_pct_gdp` | `ai_private_investment` |
| **INN** | `patents_resident_origin` | `semi_pct_patents`, `quantum_ipf_count` |
| **COM** | — (qualitative) | `ai_notable_models` (optional) |
| **PRD** | `mva_pct_gdp` | `hpc_top500_systems`, `hpc_top500_rmax` |
| **ADE** | `hitech_export_share`, `gvc_foreign_va_share` | `semi_exports_hs8542` |
| **Productivity** | `labour_productivity_gdph`, `tfp_level`, `gdp_pc_ppp` | — |

---

## 9. Reliability summary by source

| Source | Reliability | Notes |
|--------|-------------|-------|
| World Bank WDI | HIGH | Standard macro; check CN revisions |
| OECD MSTI | HIGH | Best for R&D cross-country |
| Penn World Table 11.0 | HIGH | Oct 2025 release; CN series changed |
| UNESCO UIS | HIGH | R&D personnel |
| WIPO | MEDIUM | Volume not quality |
| UN Comtrade | HIGH | Trade values; interpret structure |
| UNIDO | MED-HIGH | MVA lag 1–2y |
| OECD TiVA | MED-HIGH | Lag; revisions |
| OECD Productivity | MED-HIGH | CN hours caveat |
| TOP500 | HIGH | Best HPC proxy |
| Stanford AI Index | MEDIUM | Composite; CN private $ weak |
| EPO-OECD Quantum | MEDIUM | Manual extraction |

---

*Следующий агент: начать с Phase 1a по разделу 7; не скачивать STEM, field-specific Scopus, PitchBook, SEMI paid data.*

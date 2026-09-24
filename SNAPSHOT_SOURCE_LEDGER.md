# SNAPSHOT SOURCE LEDGER

**Дата:** 2026-09-22  
**Роль:** сверка число ↔ источник ↔ год ↔ страна ↔ единица  
**Статус снимков:** exploratory; occupancy = `snapshot` ≠ `measured`

---

## Правила чтения

- Каждая цифра ниже — точечная выписка, не полный ряд 2010–2023 в панели.
- Не смешивать OECD GERD USD PPP с WB GERD % GDP.
- Статьи Scopus volume crossover: **2016→2017**, не «~2020».

---

## Macro absolutes (reuse from disk)

| Indicator | USA | CHN | Year | Unit | Source file | Claim allowed | Claim forbidden |
|-----------|-----|-----|------|------|-------------|-----------------|-----------------|
| GERD PPP | 1 009 275 | 1 028 344 | **2024** | млн USD PPP | `oecd_gerd_usd_ppp.csv` | Китай чуть выше по **объёму** GERD PPP в 2024 | «Китай тратит больше % ВВП» (это WB intensity) |
| Researchers headcount est. | ~1 686 | ~2 635 | **2022** | тыс. чел. | panel × `pwt_pop.csv` | Оценка: Китай выше по **численности** | Официальный census исследователей; STEM quality |
| PWT HC index | 3.83 | 2.75 | **2023** | индекс | `pwt_hc.csv` | США выше по индексу HC | STEM graduates / quality of education |

Таблица: `data_reviewed/tables_reviewed/dual_scale_with_absolutes.csv`.  
CAGR GERD PPP 2010–2024: USA ~6.7%/yr, CHN ~11.9%/yr.

---

## TOP500 (`data/raw/snapshots/top500_snapshot.csv`)

| Indicator | USA | CHN | When | Source | Allowed | Forbidden |
|-----------|-----|-----|------|--------|---------|-----------|
| Systems on list | 199 | 109 | Nov **2015** | TOP500 highlights | Descriptive count | = usable AI cloud compute |
| Systems on list | 171 | 40 | Nov **2025** | TOP500 via Network World / Visual Capitalist | Descriptive count; Japan 43, DEU 40 | Fab / AI training leadership |

---

## Stanford AI Index 2025 (`ai_index_snapshot.csv`)

| Indicator | USA | CHN | Year | Source figure | Allowed | Forbidden |
|-----------|-----|-----|------|---------------|---------|-----------|
| AI pubs share of world | 9.2% | 23.2% | 2023 | Fig 1.1.6 | Volume share | Science leadership / impact |
| AI citations share | 13.0% | 22.6% | 2023 | Fig 1.1.7 | Citation share | «США слабее по качеству» (Index: США в top-100 cited) |
| Private AI investment | $109.1 bn | $9.3 bn | 2024 | Economy / highlight 3 | Private $ gap | GERD finance mix / H3 |
| Notable models | 40 | 15 | 2024 | Fig 1.3.1 | Thin COM proxy | Commercial deployment |
| AI patent grants share | 14.2% | 69.7% | 2023 | Fig 1.2.3 | Counts share | Quality / triadic |

Report: https://hai.stanford.edu/ai-index/2025-ai-index-report ; PDF chapter 1.

---

## EPO–OECD quantum (`quantum_epo_oecd_snapshot.csv`)

| Indicator | USA | CHN | Span | Source | Allowed | Forbidden |
|-----------|-----|-----|------|--------|---------|-----------|
| Quantum IPF count | **3330** | **947** | 2005–2024 | Fig 3.3.1 Panel B | IPF leadership USA | National-only families (= China larger) as IPF |
| US IPF world share | 41% → 31% | — | 2015–19 → 2020–24 | Fig E4 | Share decline | Macro COM |
| Funding to firms | ~60% to US firms | — | ever recorded | Fig E6 | Funding concentration | Causal policy effect |
| Quantum pubs labels | 1806 | 2592 | 2022 | Fig 8.2.7 labels | Exploratory ranks | Exact official series without re-extract |

World IPF total ~9740 (EPO press 2025-12-17). Commercialisation / macro effect: **not measured**.

---

## Articles crossover (macro panel — fix)

| Claim | Correct | Incorrect |
|-------|---------|-----------|
| Year CHN overtakes USA on Scopus article **volume** | **2017** first year CHN>USA; last USA>CHN = **2016** | «кроссовер ~2020» |

Source: `core_panel_reviewed.csv`; F3.

---

## Figures produced this pass

| File | Role |
|------|------|
| `figures_reviewed/F11_radar_macro_blocks.png` | Min–max radar across 8 countries; not capability index |
| `figures_reviewed/F12_gerd_absolute_ppp.png` | Absolute GERD USA/CHN/KOR |
| `tables_reviewed/radar_macro_blocks_minmax.csv` | Underlying radar values |

M1 / PCA: **not recomputed**; remain appendix-only / DO NOT USE in talk track.

---

*Конец SNAPSHOT_SOURCE_LEDGER.md.*

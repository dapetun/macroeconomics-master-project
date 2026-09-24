# Occupancy matrix 8×4 (TCI × tech)

**Агент:** OccupancyAndCasesAgent  
**Дата:** 2026-09-22  
**Статус:** State A + thin snapshots — карта заполненности, не индекс-тест H1  
**Binding:** `RQ_FREEZE.md`, `APPROVED_METHOD_SET.md`, `DATA_CANON.md`, snapshots in `data/raw/snapshots/`

**Ячейки:** `measured` | `snapshot` | `qual` | `?`

**Правила**
- General-macro **не** заполняет tech-specific ячейки.
- `snapshot` ≠ `measured` (точечная выписка; exploratory).
- `HS8542` ≠ fab / ≠ nodes.
- Пустая ячейка = ограничение **этой** работы, не «неизмеримо в мире».

Машинная копия: `tech_occupancy_matrix.csv`.  
Карточки кейсов: `tech_framework_unified.md` §7.

---

## Матрица

| TCI | AI | Semiconductors | HPC | Quantum |
|-----|----|----------------|-----|---------|
| **S** science | `snapshot`: AI pubs share 2023 (AI Index Fig 1.1.6) | `?` | `?` | `snapshot`: quantum pubs labels 2022 (EPO-OECD Fig 8.2.7) |
| **HC** human capital | `?` | `?` | `?` | `?` |
| **RD** R&D | `?` (general GERD ≠ AI R&D) | `?` | `?` | `?` |
| **FIN** finance | `snapshot`: private AI $ 2024 (AI Index) — **не** GERD finance mix | `?` | `?` | `snapshot`: funding share to US firms ~60% (EPO-OECD E6) — exploratory |
| **INN** innovation | `snapshot`: AI patent grants share 2023; notable models 2024 | `?` (no WIPO field series) | `?` | `snapshot`: quantum IPF counts 2005–2024 (EPO-OECD 3.3.1B) |
| **COM** commercialization | `snapshot`: notable models 2024 (thin COM proxy) | `?` | `?` | `?` (early-stage; adoption not measured) |
| **PRD** production/scaling | `?` | `qual`: TWN foundry hole (no SEMI fab/node) | `snapshot`: TOP500 systems Nov 2015 & Nov 2025 | `?` |
| **ADE** adoption/export | `?` (org AI use mentioned in AI Index narrative only) | `measured`: `semi_exports_hs8542` + `semi_status` (≠fab) | `?` | `?` |

---

## Сводка заполненности (из 32)

| Статус | Число | Где |
|--------|-------|-----|
| `measured` | **1** | Semiconductors × ADE |
| `snapshot` | **9** | AI: S/FIN/INN/COM; HPC: PRD; Quantum: S/FIN/INN |
| `qual` | **1** | Semiconductors × PRD (TWN) |
| `?` | **21** | остальное |

**Следствие:** количественный tech-слой = semis-trade + тонкие снимки AI/HPC/quantum + карта дыр. Четыре домена — **одна** матрица, не четыре winner-вердикта.

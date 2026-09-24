# Project Revision Log

Дата: 2026-09-14. Критическое ревью после основного анализа.

---

## Источник ревью

Критическое ревью выявило 15 проблем (8 HIGH, 7 MEDIUM) в толковании результатов. Все проблемы — **интерпретационного уровня**, не数据ового; CSV/результаты пересчёта не требуются.

---

## HIGH severity (8 issues) — все исправлены

| # | Проблема | Где исправлено | Суть исправления |
|---|---|---|---|
| 1 | TFP USA=1 trend on constant | `final_synthesis.md` §0, §6, §7; `analysis_report.md` §3 | Добавлен дисклеймер: USA=1 — construction, OLS-наклон USA TFP = −3.6e⁻¹⁷, p=0.098 — шум на константе; trend USA TFP не интерпретируется; R²=0.992 движим FE |
| 2 | Intensity vs volume = denominator artefact | `final_synthesis.md` §0, F1, §8; `analysis_report.md` §1 | Добавлено: сравнение GERD (%GDP) со статьями/патентами (абсолютные) — denominator artefact; гетерогенность разрывов предсказуема из демографии и масштаба GDP; conversion ratios запрещены как рейтинг |
| 3 | MVA share ≠ scale | `final_synthesis.md` F1, F4, matrix; `tech_cases_comparison.md` matrix | Добавлено: MVA % GDP — доля, не абсолютный выпуск; «масштаб ~2.5x» из доли логически невалиден; для абсолютного MVA нужен номинальный GDP |
| 4 | Researchers per-million flipped | `final_synthesis.md` F2 | Добавлено: per-million знаменатель выбирает показатель, где США выигрывают; по абсолютным головам Китай вероятно впереди (~1.2M→2.4M vs ~1.2M→1.6M) |
| 5 | BERD model claim contradicted by data | `final_synthesis.md` matrix, §5; `hypothesis_table.md` H3; `tech_cases_comparison.md` §4 | BERD/GERD ratio ~77% для обеих стран; «частный vs направленный finance» — narrative, не данные |
| 6 | H1/H4 verdicts inflated | `hypothesis_table.md` all rows; `analysis_report.md` §4; `final_synthesis.md` §4 | H1: TCI-индекс не построен, supported по дескриптивам не по preregistered test. H4: переопределена пост hoc как гетерогенность разрывов, не рейтинг эффективности |
| 7 | M1 interpretation problems | `final_synthesis.md` F6, §5; `analysis_report.md` §3 | CI [−0.0005, 0.0554] включает 0 → на 5% неотличимо от нуля; t=13.1 раздут HC1-автокорреляцией; R²=0.992 движим FE |
| 8 | Causal verbs in thesis | `final_synthesis.md` §1, §5, §8 | Все causal-глаголы («конвертируют», «реализуют», «снизили») заменены на ассоциативные («демонстрируют различия», «ассоциировано», «маркеры») |

---

## MEDIUM severity (7 issues) — все исправлены

| # | Проблема | Где исправлено | Суть исправления |
|---|---|---|---|
| 9 | Patents year = peak (2021) | `final_synthesis.md` F3, §7; `tech_cases_comparison.md` matrix | Добавлен caveat: 2021 — пик китайских патентных субсидий; данные после 2022 могут отличаться |
| 10 | High-tech SITC Rev.4 break | `final_synthesis.md` F5, §7; `tech_cases_comparison.md` matrix | Добавлено: SITC Rev.4 break Oct 2024, 28% missing — trend over break невалиден |
| 11 | IC exports nominal | `final_synthesis.md` F5, matrix; `tech_cases_comparison.md` matrix | Добавлено: 3.13x — номинал USD, включает processing trade и re-exports через HK/SG; HS8542 ≠ advanced nodes |
| 12 | CHIPS/BIS pre/post | `final_synthesis.md` F5; `analysis_report.md` §3 | Добавлено: n=2 в каждой ячейке, нет SE, статистические выводы невозможны; конфаундеры (цикл, COVID) |
| 13 | Tech matrix shows +/- for insufficient data | `tech_cases_comparison.md` matrix | AI COM/HPC/Quantum строки переписаны: все `?` (net данных), не `+`/`−` |
| 14 | GDP pc absolute gap growing | `final_synthesis.md` F6, matrix | Добавлено: ratio-конвергенция ≠ конвергенция уровней; абсолютный разрыв вырос $49k→$52k |
| 15 | KOR claims from panel | `tech_cases_comparison.md` §4, matrix | KOR GERD/IC CAGR помечены как косвенные прокси, не fab-данные |

---

## Файлы, подвергшиеся правке

| Файл | Кол-во правок | Тип правок |
|---|---|---|
| `reports/final_synthesis.md` | 12 | Дисклеймер, F1–F7, matrix, §4–§8 |
| `reports/analysis_report.md` | 3 | M1 table, event section, H-table |
| `reports/hypothesis_table.md` | 1 (полная перезапись) | Все 6 строк H1–H6 |
| `reports/tech_cases_comparison.md` | 3 | Scope table, matrix, §4 synthesis |
| `reports/data_quality_report.md` | 1 | Cross-country comparability |

---

## Файлы, НЕ подвергшиеся правке (данные корректны)

- `results/*.csv` — все CSV корректны, проблемы были в интерпретации
- `data/core_panel.csv`, `data/tech_panel.csv` — данные без изменений
- `scripts/analysis_agent4.py` — скрипт без изменений
- `figures/F1–F10` — графики без изменений

---

## Итог

Все 15 проблем исправлены текстовыми правками в 5 отчётных файлах. Данные (CSV, panel, скрипты, графики) не затронуты — ошибки были исключительно в интерпретации и формулировках.

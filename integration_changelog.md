# Integration Changelog

Дата: 2026-09-16. Интегратор: Integration Agent.
Источники: текущая версия (`research_design.md`, `data_map.md`, `reports/*`, `results/*`, `figures/*`) + `project_revision.md` + `data_reviewed/data_quality_final.md` + `data_reviewed/data_changes.md` + `quant_reviewed.md` + `quant_changes.md` + `technology_cases_final.md` + `technology_changes.md` + `research_logic_final.md` + `logic_changes.md`.
Приоритет при конфликте: `research_logic_final.md` > `regression_results_final.csv` > `data_quality_final.md` > `quant_reviewed.md` / `technology_cases_final.md` > `reports/*.md`. Новых фактов не добавлялось; числа — только из существующих CSV/reviewed-таблиц.

---

## 1. Диспозиция по каждому изменению (принять / отклонить / конфликт / обновление других частей)

### A. Data-слой (data_quality_final + data_changes)

| # | Изменение | Принять? | Конфликт? | Требует обновления других частей? |
|---|---|---|---|---|
| D1 | BERD «financed» → **PERFORMED** (P_BERPCT); F9-титул неверен; ISR BERD>GERD 2021–23 (6.50>6.35) | **Да** | Да: старые `data_map.md` §1.6, `reports/*` называют financed/mix | Да: §2/H3, §4/FIN, §5–§8 final — FIN→`?`, паритет отозван |
| D2 | Patents «origin» → **office-basis resident** (+ добавлен `patents_total_office`: 2021 5.44x resident / 2.68x total) | **Да** | Да: `data_map.md` §1.9, старые тексты «origin» | Да: все INN-строки — только парой + пик субсидий + запрет quality |
| D3 | Articles generic → **fractional S&E volume** | **Да** | Нет | Да: S-строки — «volume, не impact; не AI-specific» |
| D4 | GDP — **constant-2017 single vintage, 2024 preliminary**; TFP **USA=1/год construction (1994–2023)** | **Да** | Нет (подтверждает project_revision #1) | Да: TFP-строки, M1-чтение (USA-константа), F7-подпись |
| D5 | Hitech — **ряд с 2007 + SITC-break**; MVA — **доля, не масштаб**; semi — **номинал + HS H3–H6 + quarantine + `semi_status`** | **Да** | Нет (подтверждает project_revision #3/#10/#11) | Да: PRD/ADE-строки, F5/F6/F8-подписи, запрет trade=fab |
| D6 | D1-snapshot: запрет ratio с NaN → **latest-joint-year** (`descriptive_snapshot_latest_joint.csv`) | **Да** | Да: старые snapshot-таблицы смешивали NaN (researchers-2023, patents-2023, MVA USA-2023) | Да: §5.1 final — researchers 2022, patents 2021, MVA 2021 |
| D7 | D2-CAGR: несопоставимые окна → **common-window** (`descriptive_cagr_common_window.csv`) | **Да** | Да: `descriptive_cagr.csv`, тексты F2/F4 | Да: §5.2 final — только common значения с (start,end,n) |
| D8 | M1 n=84 (ISR0 GBR7 USA12) / PCA n=91; M2 «DO NOT USE» endorsed; F8/F9 FIXED-фигуры; semi-quarantine map; event n=2 descriptive-only | **Да** | Нет | Да: §3/§5.3/§9 final — n/K/df/G-штамп везде, F10 excluded, F8/F9 FIXED авторитетны |
| D9 | AI/HPC/quantum/GVC/VC — excluded (100% missing; clean Comtrade USA-only — stale artefact, не источник панели) | **Да** | Нет | Да: §6 final — все `?`, план добора в limitations |

### B. Quant-слой (quant_reviewed + quant_changes; все 15 пунктов сверены с project_revision)

| # | Изменение | Принять? | Конфликт? | Обновление? |
|---|---|---|---|---|
| Q1–Q3 | Joint-year + common-window + dual-reporting (5.44+2.68; intensity-артефакт; MVA-доля; BERD-уровень; IC-номинал; conversion excluded; GDPpc пара ratio+абсолют) | **Да** | Нет с data-слоем; усиливает project_revision #2–#4/#14 | Да: §5.1–§5.2, §8-матрица |
| Q4 | Pooled-корреляции DO NOT USE; только within/two-way дескриптивно | **Да** | Нет | Да: §3 final |
| Q5 | F1–F7 endorsed с подписями; F5 «USA ends 2021»; F8/F9 FIXED endorsed; F10 excluded | **Да** | Нет | Да: §5.4 final |
| Q6–Q10 | M1 descriptive-only (`regression_results_final.csv` авторитетен); USA zero-variance anchor (drop-USA 0.0329); 3 лага как sensitivity; corr 0.71; штамп n/K/df/G; cluster-CI первичен ([−0.048,0.103] p=0.409, G=7 осторожно) | **Да** | Частично: старые тексты давали только HC1 p=0.059 — дополнены cluster (более осторожно) | Да: §5.3 final — оба CI, все хрупкости |
| Q11–Q15 | No imputation; outliers retained-but-flagged + drop-one; +19 пп абсурд-тест; M2-знак не читать; causal purge + allow-list; H1–H4 «mixed/weak» | **Да, кроме вердикта H1–H4**: «mixed/weak/inconclusive» **ужесточён до «not tested + наблюдение»** по logic-приоритету (§2) | **Да, конфликт Q15 vs logic H2–H3**: разрешён в пользу logic (preregistration + осторожность) | Да: §2, §6-thesis, §10 |

### C. Technology-слой (technology_cases_final + technology_changes)

| # | Изменение | Принять? | Конфликт? | Обновление? |
|---|---|---|---|---|
| T0 | §0 scope-цепочка (что измерено/нет по 9 блокам × 4 tech) | **Да** | Нет | Да: §6-преамбула final |
| T-AI | A1–A7: general-контекст вместо AI-вердикта; finance-модель → [expert assessment]; frontier/private → гипотеза; adoption → [expert assessment]; volume/benchmark/AI→TFP/funding подмены отвергнуты | **Да, с одной поправкой**: finance-паритет 77% как «опровержение» **отозван** (см. L-H4 ниже) | **Да, конфликт с logic H4**: tech-синтез п.4 использовал паритет как антитезис — отозван | Да: §6.1, §7, §8/FIN |
| T-S | S0–S8: «доля, не абсолют»; IC-номинал+карантин+CAGR-смещён; design/EDA/EUV/fab → [expert assessment]; «EUV-рычаг у союзников»; KOR/JPN-цифры → trade/R&D-контекст; 8 позиций покрыты; trade=fab и announced=production запрещены | **Да** | Нет (HS-ревизии добавлены из logic M6 как усиление) | Да: §6.2, §8/PRD/ADE |
| T-HPC | 3 типа compute + Linpack≠AI + non-reporting bias + no verdict | **Да** | Нет | Да: §6.3 |
| T-Q | computing/communication/sensing + no verdict + экон. ≈0 qual + IPF только после CSV | **Да** | Нет | Да: §6.4 |
| T-сквозные | Матрица с `?`; синтез п.1–6; Приложение 9 подмен (новое) | **Да, кроме**: «одна строка» с «превращают» **удалена** (causal), синтез п.4 ослаблен паритетом-отзывом | **Да, конфликт causal-глагола vs purge**: разрешён в пользу purge | Да: §8, §10-thesis |

### D. Logic-слой (research_logic_final + logic_changes; наивысший приоритет интерпретации)

| # | Изменение | Принять? | Конфликт и разрешение |
|---|---|---|---|
| L-H1 (RQ unanswerable) | RQ сужен (§1.2–§1.3 final); неотвечаемое маркировано | **Да** | Нет с data/quant (подтверждает missing); переопределяет старые conclusions |
| L-H2 (H1 без TCI) | «Partially supported (macro)» → **Not tested + наблюдение** | **Да** | **Конфликт со всеми reports + quant Q15 + tech-синтезом п.1**: разрешён в пользу logic (preregistration; более осторожно) |
| L-H3 (H4 пост hoc) | «Partial как гетерогенность» → **Not tested + наблюдение** | **Да** | Тот же конфликт; то же разрешение |
| L-H4 (FIN unmeasured + паритет 77% отозван) | FIN → `?`; паритет не использовать ни за, ни против; BERD-уровень = PERFORMED-интенсивность | **Да** | **Конфликт с quant (§3 BERD-раздел), tech (AI-D/п.4), всеми reports (matrix/§5/H3)**: разрешён в пользу logic+data (ярлык PERFORMED + ISR-инверсия = более надёжный источник/данные). Единственное ужесточение сверх prior-ревью — осознанное |
| L-H5 (TFP≠tech + лаг) | M1 только ассоциация с cluster-CI + 3 лага; tech-приписывание запрещено | **Да** | Нет (усиливает quant); числа из quant без изменений |
| L-H6 (trade→fab) | Только стоимости/доли с caveat-стеком; fab → `?`; IC-CAGR смещён; 10-й/11-й запреты | **Да** | Нет (усиливает data+tech) |
| L-H7 (предрешённый thesis) | Минимальный thesis (§10 final) без «моделей»/winner/tech-обобщений | **Да** | **Конфликт со старым §8 final_synthesis и «одной строкой» tech-cases**: разрешён в пользу logic (осторожность) |
| L-H8 (геополитика) | §6 ужата до контекстных оговорок, не findings | **Да** | Конфликт со старым §6 (5 пунктов как выводы): разрешён в пользу logic |
| L-H9–H10 (office-basis; intensity circular) | Пара 5.44+2.68 обязательна; intensity/volume — арифметика, не находка | **Да** | Нет (усиливает data/project_revision) |
| L-M1–M10 | Головы удалены; только common-window; GBR ends 2017; causal-глаголы («превращают», «частное финансирование» как модель) удалены; KOR/ISR понижены; HS-ревизии раскрыты; H2-circular зафиксирован; CHIPS/BIS только lines «не эффект»; COM-стрелки недействительны; TFP catch-up — только macro-уровни | **Да** | Конфликты: головы vs F2 (удалены — нет расчёта); «ends 2019» vs факт 2017 (факт побеждает); старые CAGR-пары без окон (помечены несопоставимыми) |

Отклонено: ничего из специализированных ревью не отклонено целиком; отклонены только отдельные старые формулировки (H1/H4 partial, FIN-паритет как evidence, головы-оценка, «превращают», KOR-fab headlining, полные-окна CAGR-пары, «GBR ends 2019»), все — по правилу «более надёжный источник / качественные данные / осторожность».

---

## 2. Consistency-проверка (после интеграции)

- [x] Цифры: GERD 3.45/2.58 (0.748); BERD PERFORMED 2.66/2.00 (0.754, не модель); researchers joint-2022 4937.49/~1849 (0.375x); статьи 430843/932712 (2.165x); патенты 2021 resident 262244/1426644 (5.44x) + total-office 591473/1585663 (2.68x); MVA joint-2021 10.53/26.62 (2.53x доля); hitech 21.85/26.57 (gap 9.5→4.7 пп); GDPpc $74352/$22687 (0.305x) + абс. $49321→$51664; TFP 1.0/0.471 (2010: 0.395); IC $43.6/$136.4 млрд (3.13x номинал); M1 β=0.02746 HC1 [−0.0005,0.0554] p=0.059 / cluster [−0.048,0.103] p=0.409, θ=0.05629, n=84 K=20 df=64 G=7 — одинаково в §§5–8, 10.
- [x] Определения: BERD PERFORMED; patents office-basis; articles fractional S&E volume; GDP 2017-vintage; TFP USA=1 construction 1994–2023; MVA доля; hitech basket+SITC-break; semi номинал+HS H3–H6+quarantine — одинаково в §§4–9.
- [x] Годы: анализ 2010–2023; patents 2010–2021; researchers joint 2022 (GBR–2017, USA–2022, ISR 0); MVA joint 2021; semi CHN-gap 2015–17; researchers-CAGR 2010–2017; patents/MVA-CAGR 2010–2021 — одинаково везде.
- [x] Названия: `gerd_pct_gdp`, `researchers_per_million`, `scopus_articles`, `patents_resident` / `patents_total_office`, `mva_pct_gdp`, `hitech_export_share`, `gdp_pc_ppp`, `tfp_ctfp`, `berd_pct_gdp`, `semi_exports_hs8542` + `semi_status` — одинаково.
- [x] Выводы: ни одна H не поддержана (даже частично); FIN unmeasured; конверсия не ранжируется; M1 неотличима от нуля; AI/HPC/quantum insufficient; fab `?`; CHIPS/BIS маркеры — одинаково в §§2, 5–8, 10.
- [x] Гипотезы: preregistered-test vs наблюдение разделены везде (§2 — канон; §§6–8, 10 ссылаются, не переопределяют).
- [x] Графики↔текст: F1–F7 caveat-подписи; F8/F9 FIXED авторитетны; F10 excluded; USA-2021/2022-концы не сравниваются с CHN-2023; gap не соединяется; CHIPS/BIS «не эффект» — §5.4 ↔ §§5–8.

---

## 3. Созданные файлы

- `project_final.md` — единая актуальная версия (§§1–10: RQ; hypotheses; methodology; data; quantitative findings; technology cases; economic implications; comparative assessment; limitations; conclusion). Новых фактов нет.
- `integration_changelog.md` — этот файл.

## 4. Остаточные риски (не устранены; зафиксированы в `project_final.md` §9)

Малая N (n=84, G=7); USA=1-константа; tech-панели missing; 2021-пик субсидий; SITC/HS-breaks; номинал+processing; доля≠масштаб; FIN неизмерен; denominator-артефакты; ratio≠уровни. Structural, out of scope; требуют TCI-индекса, single-definition Comtrade-pull, TOP500-pull, AI Index export, quantum IPF CSV, панели 15–20 стран, sectoral TFP (см. §9 Future work).

# Remaining Risks (нельзя исправить в текущем проекте)

Дата: 2026-09-14. Риски, которые **structural** и не устраняются текстовыми правками.

> ⛔ **SUPERSEDED / DO NOT CITE (2026-09-20, DataCanonAgent — усиление).**  
> Файл — **частично stale** относительно `final_project.md`, `RQ_FREEZE.md`, `DATA_CANON.md`.  
> **Не цитировать** из тела:  
> (1) «H1 partially supported» / любой H-PARTIAL — H1–H6 = **archived / not tested**;  
> (2) BERD/GERD **~77%** как evidence за/против finance — **отозван**; BERD = **PERFORMED**, не finance mix;  
> (3) «кластер-SE **невозможны**» — **ложь**: country-cluster SE **посчитаны** (`regression_results_final.csv`; β GERD cluster p≈0.409); формулировка «G=7 → SE хрупки» допустима, «невозможны» — нет.  
> Актуальные: `DATA_CANON.md`, `final_project.md`, `APPROVED_METHOD_SET.md`, `reports/hypothesis_table.md`.  
> Тело файла **не** переписывалось (баннер only).

> **SUPERSEDED / ARCHIVE note (2026-09-20, ResearchDesignAgent).**  
> §3 ещё содержит устаревшую формулировку «H1 partially supported» — **отозвана**. H1–H6 = **archived design / not tested** (без SUPPORTED/PARTIAL/REJECTED).  
> Актуальный RQ и D1–D2: `RQ_FREEZE.md`. Методы: `APPROVED_METHOD_SET.md`. Гипотезы: `reports/hypothesis_table.md`.  
> Паритет BERD/GERD ~77% как антитезис finance-mix — также stale относительно `final_project.md`. Тело файла не переписывалось.

---

## 1. Структурные ограничения данных (нельзя исправить без нового сбора)

| Риск | Описание | Влияние на выводы |
|---|---|---|
| AI/HPC/quantum 100% missing | Stanford AI Index, TOP500, EPO–OECD не извлечены | H2/H5/H6 — insufficient; tech-зависимость H1 не тестируема |
| TFP USA=1 by construction | PWT нормирует USA=1 каждый год | USA не дают within-вариации; идентификация на 6 странах + CHN; R²=0.992 движим FE |
| Патенты 2021 = пик субсидий CN | До 2022 субсидии снижены | Counts 5.44x могут быть завышены; trend после 2021 неизвестен |
| SITC Rev.4 break Oct 2024 | 28% hitech-ряда отсутствует | Trend hitech exports over break невалиден |
| HS8542 nominal + processing trade | 3.13x включает re-exports HK/SG | Trade ≠ fab capacity; стоимость ≠ frontier production |
| MVA % GDP = share, не absolute | Для абсолютного MVA нужен номинальный GDP | «Масштаб ~2.5x» из доли логически невалиден |
| BERD/GERD ~77% обе страны | Частный vs направленный finance не различается по ratio | Narratives о financial structure не подтверждаются данными |

---

## 2. Методологические ограничения (нельзя исправить в рамках панели)

| Риск | Описание | Влияние |
|---|---|---|
| N=8 стран, n=84 наблюдения | Малая панель для FE-модели | Низкая мощность; HC1 t раздут автокорреляцией; кластер-SE невозможны (7 кластеров) |
| Endogeneity | Богатые тратят больше на R&D | β GERD = 0.028 — ассоциация, не causal effect |
| Omitted variables | Нет capital stock, institutional quality, trade openness в M1 | Коэффициенты смещены |
| Aggregate TFP | PWT ctfp — не tech-TFP | Нельзя приписывать AI/semis/quantum |
| Conversion ratios = denominator artefact | Знаменатели несопоставимы (%GDP vs absolute counts) | Ранжирование «эффективности конверсии» запрещено |
| Ratio convergence ≠ level convergence | GDP pc ratio вырос, но абсолютный разрыв вырос $49k→$52k | «Догоняне» по ratio не означает сокращения разрыва в долларах |

---

## 3. Ограничения интерпретации (приняты как есть)

| Риск | Описание | Статус |
|---|---|---|
| Causal language запрещён | Все выводы — ассоциативные | Исправлено в текстах; оговорка в §0 |
| H1 «partially supported» без TCI-индекса | TCI не построен; вердикт по дескриптивам | Признано; preregistered test не выполнен |
| H4 переопределена пост hoc | Исходная H4 = test conversion, operationalized as gap heterogeneity | Признано; ранжирование эффективности запрещено |
| Event pre/post n=2, нет SE | CHIPS/BIS — только маркеры | Признано; causal effects не оцениваются |
| KOR claims = косвенные прокси | Нет fab-данных по KOR | Признано; структура мощностей не квантифицирована |
| Пулы корреляций = композиционный артефакт | Китай инвертирует знак | Указано «не использовать» в analysis_report §6 |

---

## 4. Что требуется для будущего улучшения (out of scope)

1. **TCI-индекс**: сбор 12–15 переменных для S→ADE и построение индекса по дизайну (H1 test)
2. **AI панель**: Stanford AI Index audited export (publications, private $, notable models)
3. **HPC панель**: Nov TOP500 pull 2010–2025 (count + Rmax) + разделение 3 типов compute
4. **Quantum панель**: EPO–OECD IPF CSV 2005–2024
5. **Comtrade single-definition**: устранение multi-record CHN 2015–17, единообразная агрегация
6. **SEMI fab data**: доля мощностей по узлам (advance/mature) для прямого теста H2
7. **Расширение панели**: 15–20 стран для кластер-SE и robustness
8. **Sectoral TFP**: раздельная productivity для semis/AI/HPC вместо агрегатного PWT
9. **TiVA GVC-переменная**: foreign VA share для теста export→production mechanism
10. **Causal design**: IV/DID/SDID для теста CHIPS/BIS effects (при расширении данных)

---

## Итог

15 проблем крит-ревью исправлены на уровне интерпретации. Structural ограничения (малая N, USA=1, missing tech-панели, denominator artefacts) —out of scope для текущего проекта и зафиксированы в limitations.

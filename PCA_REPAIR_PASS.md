# PCA repair — PASS (вариант a: intensity-only)

**Дата:** 2026-09-20  
**Агент:** QuantitativeAgent  
**Протокол:** `APPROVED_METHOD_SET.md` § PCA repair  
**Вердикт:** **PASS** — выбран вариант **(a) intensity-only**

---

## Почему старый PCA сломан

| Факт | Значение |
|------|----------|
| Смешение шкал | GERD%/BERD%/log(researchers) **+** log(articles) counts |
| PC1 loading articles | **≈ −0.36** (`results/pca_loadings.csv`) |
| M2 γ (TFP~PC1_lag1) | **≈ −0.118** — wrong sign как «capability» |
| Статус старого | **DO NOT USE**; `figures/F10_pca_tfp_scatter.png` **не** evidence |

---

## Repair cycle (один проход a→b→c)

| Variant | Gate | n | years | countries | var_exp PC1 | PC1 loadings (все >0) |
|---------|------|---|-------|-----------|-------------|------------------------|
| **(a) intensity** | **PASS ★ selected** | 91 | 2010–2023 | 7 (ISR out) | **90.7%** | GERD 0.598; BERD 0.585; researchers/mn 0.548 |
| (b) logged volumes | PASS (не выбран) | 96 | 2010–2021 | 8 | 92.0% | log art/pat all >0 |
| (c) within-z intensity | PASS (не выбран) | 91 | 2010–2023 | 7 | 91.2% | wz_* all >0 |

**Выбор (a):** предпочтительный intensity-consistent набор из протокола; не смешивает %GDP с counts. Варианты b/c прошли gate, но не нужны после успеха (a).

**Success gate:** все loadings одного знака для «higher R&D/HC intensity» — **да**.

---

## Интерпретация PC1 (a)

- **PC1** ≈ общий фактор **intensity входов** (GERD % GDP, BERD PERFORMED % GDP, researchers per million).
- Это **дескриптивный индекс одной шкалы**, не «capability→TFP» и не тест H1.
- **M2 `TFP ~ PC1`:** **не запускался** в этом проходе (OPTIONAL secondary only). Старый M2 остаётся EXCLUDED. Если когда-либо добавить M2 — только appendix + caveat **USA TFP=1** + **запрет** tech→TFP causality.
- Appendix-фигура (не старый F10): `data_reviewed/figures_reviewed/F10_appendix_pc1_intensity_ONLY.png` — ряды PC1 по странам, без scatter vs TFP.

---

## Файлы артефактов

| Файл | Роль |
|------|------|
| `results/pca_repair_a_intensity_loadings.csv` | Loadings варианта (a) |
| `results/pca_repair_a_intensity_variance.csv` | Доля дисперсии |
| `results/pca_repair_a_intensity_scores.csv` | Scores PC1 |
| `results/pca_repair_selected_loadings.csv` | Указатель на выбранный repair |
| `results/pca_repair_selected_variance.csv` | То же для variance |
| `results/pca_repair_gate_summary.csv` | Сводка a/b/c |
| `results/pca_repair_verdict.txt` | PASS / a_intensity |
| `results/pca_loadings.csv` | **старый broken** — не цитировать |

**Не смешивать** с volume-PCA (b) в одном «capability» индексе без явной документации шкалы.

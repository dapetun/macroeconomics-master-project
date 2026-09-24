# DO NOT USE — количественные методы / артефакты (QuantitativeAgent)

**Дата:** 2026-09-20  
**Статус:** выведены из аргумента тезиса (State A). Файлы могут остаться на диске как архив.

---

## Запрещено в аргументе

| Артефакт / практика | Почему | Что вместо |
|---------------------|--------|------------|
| `results/conversion_ratios.csv` | Counts÷intensities, разные знаменатели; не «эффективность конверсии» | Dual-scale table |
| Pooled Pearson / `correlations_pooled.csv` как **inference** | Композиция стран/лет | Within-country / descriptive only |
| Event pre/post CHIPS/BIS как **эффект** (`event_CHIPS_BIS_prepost.csv`) | Нет identification | Vertical date lines = **markers only** |
| Старый PCA + M2 + `figures/F10_pca_tfp_scatter.png` | Articles loading −0.36; γ_M2 ≈ −0.118 | Repair (a) PC1 descriptive **или** drop |
| M1 как ответ на RQ / «эффект GERD» | Cluster CI включает 0; USA TFP=1 | Appendix associational (`M1_INTERPRETATION.md`) |
| DiD, IV, GMM, ML, k-means, Elastic Net, FA (default) | Not approved | — |
| Lag shopping / HAC «для значимости» M1 | Fragility ≠ выбор спецификации | Fragility table as-is |
| TWN panel expansion / State B data pulls | Scope freeze | Qual hole (TechMatrix) |

---

## Разрешено с оговорками

- Joint-year snapshot + common-window CAGR (articles — **оба** окна + пик USA 2021)
- Dual-scale intensity vs volume (`dual_scale_intensity_volume.csv`)
- M1 numbers из `regression_results_final.csv` + caveats
- PCA repair **(a)** как descriptive intensity index (appendix); M2 не форсировать
- Policy dates на графиках как маркеры, без causal claim

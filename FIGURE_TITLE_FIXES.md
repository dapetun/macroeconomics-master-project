# FIGURE TITLE FIXES — нейтральные заголовки

**Дата:** 2026-09-20  
**Агент:** QuantitativeAgent  
**Правило:** без causal / convergence / winner language; год/окно на фигуре или в title.

---

## Old → New

| Figure | Old title (из `scripts/analysis_agent4.py`) | New title | Status |
|--------|-----------------------------------------------|-----------|--------|
| **F1** | R&D intensity: **China converges** toward US level, Korea/Israel lead | GERD intensity (% GDP), 2010–2023: levels and trends by country | **REGENERATED** `figures/F1_gerd_trends.png` |
| **F2** | Human capital: US level ~2x China (**2021**); ISR missing… | Researchers per million, 2010–2023 (joint US–CN level year **2022**; GBR ends **2017**; ISR missing) | **REGENERATED** |
| **F3** | Science output: **China overtook** USA ~2020 (volume, not impact) | Scopus article counts (volume), 2010–2023 + CHN/USA ratio; USA peak 2021 marked | **REGENERATED** |
| **F4** | Patents: **China >> USA** in counts since ~2011 — quantity, NOT quality | Patent counts (office-basis resident), 2010–2021 — quantity, not quality | **REGENERATED** |
| **F5** | Production structure: China ~25% vs USA ~11% — persistent gap | Manufacturing value added (% GDP), 2010–2021 joint window (USA/CHN levels ~2021) | **REGENERATED** |
| **F6** | Export sophistication: China share fell after 2021… (+ red CHIPS text as effect tone) | High-tech export share (% manuf. exports), 2010–2023 — broad basket, not semis-only; CHIPS/BIS **markers only** | **REGENERATED** |
| **F7** | Aggregate TFP: China ~0.40→0.47 of US; macro proxy, not tech-TFP | Aggregate TFP levels, 2010–2023 (USA=1 by construction; macro proxy, not tech-TFP) | **REGENERATED** |
| **F8** | Semiconductor trade: China exports > USA… | Use **FIXED**: `data_reviewed/figures_reviewed/F8_*_FIXED.png` | KEEP FIXED; original superseded |
| **F9** | **Finance mix**: business R&D… / ylabel business-**financed** | Use **FIXED** BERD **PERFORMED**: `figures_reviewed/F9_*_FIXED.png` | KEEP FIXED; original DO NOT CITE wording |
| **F10** | Capability vs TFP (pooled r=…) | **DO NOT USE** old scatter. Appendix replacement: `data_reviewed/figures_reviewed/F10_appendix_pc1_intensity_ONLY.png` (PC1 intensity time series; **не** TFP cause) | Old F10 stays excluded |

---

## Примечание

Перегенерация через `scripts/quant_level1_pca_refresh.py` из `core_panel_reviewed.csv`.  
F8/F9 originals в `figures/` не перезаписывались этим скриптом — цитировать FIXED.

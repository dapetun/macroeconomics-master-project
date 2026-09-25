# DEEP_LITERATURE_NOTES.md

**Дата проверки:** 2026-09-25  
**Граница поиска:** знания агента + известные первоисточники/документация API; это не систематический обзор литературы.  
**Правило:** если DOI/URL не подтверждён — статус «не найдено в границах этой проверки».

---

## Методы эконометрики и роста

### 1. Solow (1957) — остаток производительности
- **Источник:** Solow, R. M. (1957). Technical Change and the Aggregate Production Function. *Review of Economics and Statistics*, 39(3), 312–320.  
- **DOI:** https://doi.org/10.2307/1926047  
- **Что берём:** рост выпуска минус вклад факторов = остаток (TFP) в разложении Солоу.  
- **Статус:** проверено по известным первоисточникам.

### 2. Griliches (1979, 1990) — производство знаний / патенты
- **Источник:** Griliches, Z. (1979). Issues in Assessing the Contribution of Research and Development to Productivity Growth. *Bell Journal of Economics*; Griliches, Z. (1990). Patent Statistics as Economic Indicators. *Journal of Economic Literature*.  
- **DOI (1990):** https://doi.org/10.1257/jel  
- **Что берём:** патенты как индикатор инновационной активности; идея «функции производства знаний» R&D → инновации.  
- **Статус:** проверено по известным первоисточникам (точные страницы JEL — сверять по библиотеке).

### 3. Coe & Helpman (1995) — R&D и TFP
- **Источник:** Coe, D. T., & Helpman, E. (1995). International R&D Spillovers. *European Economic Review*, 39(5), 859–887.  
- **DOI:** https://doi.org/10.1016/0014-2921(94)00100-Q  
- **Что берём:** панельная связь внутреннего (и зарубежного) R&D с TFP на уровне стран.  
- **Статус:** проверено по известным первоисточникам.

### 4. Griffith, Redding & Van Reenen (2004) — две стороны R&D
- **Источник:** Griffith, R., Redding, S., & Van Reenen, J. (2004). Mapping the Two Faces of R&D. *Review of Economics and Statistics*, 86(4), 883–895.  
- **DOI:** https://doi.org/10.1162/0034653043125194  
- **Что берём:** отдача от R&D зависит от расстояния до технологического фронтира (innovation vs imitation).  
- **Статус:** проверено по известным первоисточникам.

### 5. Aghion & Howitt — фронтир и догоняющий рост
- **Источник:** Aghion, P., & Howitt, P. (1992/1998/2009). Schumpeterian growth models (книга *The Economics of Growth*, MIT Press, 2009).  
- **Что берём:** качественное различие стратегии у фронтира и стратегии догоняющего освоения.  
- **Статус:** проверено по известным первоисточникам (учебная/книжная линия).

### 6. Young (1995); Zhu (2012) — источники роста Азии/Китая
- **Young, A. (1995).** The Tyranny of Numbers. *QJE*. DOI: https://doi.org/10.2307/2946695  
- **Zhu, X. (2012).** Understanding China’s Growth. *Journal of Economic Perspectives*, 26(4), 103–124. DOI: https://doi.org/10.1257/jep.26.4.103  
- **Что берём:** осторожность в трактовке «чуда» роста; разложение на накопление факторов vs TFP.  
- **Статус:** проверено по известным первоисточникам.

### 7. Balassa (1965) — RCA
- **Источник:** Balassa, B. (1965). Trade Liberalisation and “Revealed” Comparative Advantage. *The Manchester School*, 33(2), 99–123.  
- **DOI:** https://doi.org/10.1111/j.1467-9957.1965.tb00050.x  
- **Что берём:** индекс выявленного сравнительного преимущества для специализации в экспорте.  
- **Статус:** проверено по известным первоисточникам.

### 8. Cameron, Gelbach & Miller (2008) — мало кластеров
- **Источник:** Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-Based Improvements for Inference with Clustered Errors. *Review of Economics and Statistics*, 90(3), 414–427.  
- **DOI:** https://doi.org/10.1162/rest.90.3.414  
- **Что берём:** при малом числе кластеров обычные cluster SE ненадёжны; расширение панели до ~39 стран улучшает ситуацию относительно G=7.  
- **Статус:** проверено по известным первоисточникам.

### 9. Feenstra, Inklaar & Timmer (2015) / PWT — rtfpna vs ctfp
- **Источник:** Feenstra, R. C., Inklaar, R., & Timmer, M. P. (2015). The Next Generation of the Penn World Table. *American Economic Review*, 105(10), 3150–3182. DOI: https://doi.org/10.1257/aer.20130954  
- **Документация PWT:** https://www.rug.nl/ggdc/productivity/pwt/  
- **Что берём:** `rtfpna` — TFP в национальных ценах (динамика внутри страны); `ctfp` — уровень относительно США (кросс-секция / gap).  
- **Статус:** проверено по известным первоисточникам.

---

## Данные и институциональные источники

### 10. UN Comtrade — код 490 и репортёры
- **Документация:** https://comtradeplus.un.org/ ; API reference files.  
- **Что берём:** партнёр **490 = Other Asia, nes** используется как proxy для Тайваня в зеркальной статистике; коды репортёров брать из справочника (FRA часто 251, CHE 757, NOR 579).  
- **Статус:** проверено пробными запросами API 2026-09-25 (импорт CHN HS8542 2023 ≈ $350.1 млрд).

### 11. TOP500 — добровольная подача
- **Сайт:** https://www.top500.org/lists/top500/  
- **Что берём:** списки добровольные; падение числа китайских систем после ~2019–2021 часто связывают с меньшей подачей новых систем, а не только с потерей мощности — проверяем через First Appearance.  
- **Статус:** методология списков — проверено; конкретные новостные утверждения о «запрете подачи» — **не найдено единого официального первоисточника в границах этой проверки** (трактовать осторожно).

### 12. Epoch AI — notable models
- **Данные:** https://epoch.ai/data/notable_ai_models.csv  
- **Документация:** https://epoch.ai/  
- **Что берём:** поля Country, Model accessibility, Frontier model, Training compute; критерии «notable» заданы Epoch и могут давать отбор.  
- **Статус:** файл скачан 2026-09-25; детали критериев — сверять на сайте Epoch.

### 13. Экспортный контроль BIS и литография NL
- **BIS Oct 7, 2022** и **Oct 17, 2023** — правила экспорта advanced computing / semiconductors (Federal Register / BIS press).  
- **Нидерланды:** ограничения на экспорт литографического оборудования ASML (~2023), в координации с союзниками.  
- **Что берём:** только даты вертикальных линий на графиках, **не** оценка causal эффекта.  
- **Статус:** даты — по известным официальным анонсам; точные URL FR сверять при сдаче.

---

## Ограничения обзора

Не претендует на полноту литературы по AI geopolitics, SEMI industry reports (SEMI — платно) или military HPC. Пропуски помечены явно выше.

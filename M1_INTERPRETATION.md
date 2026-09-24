# M1 TWFE — интерпретация (вторичный / appendix)

**Дата:** 2026-09-20  
**Агент:** QuantitativeAgent  
**Авторитет чисел:** `regression_results_final.csv` (не пересчитывалось)  
**Размещение:** **appendix / secondary associational check** — **не** ответ на Frozen RQ

---

## Спецификация (KEEP)

\[
\mathrm{TFP}_{it} = \alpha_i + \delta_t + \beta\,\mathrm{GERD}_{i,t-1} + \theta\,\log(\mathrm{researchers\_per\_million})_{it} + \varepsilon_{it}
\]

LSDV: country FE + year FE. ISR выпал (нет researchers). Окно после lag: **n=84**, **G=7**.

| Term | β | SE_HC1 | p_HC1 | CI_HC1 | SE_cluster | p_cluster | CI_cluster |
|------|---|--------|-------|--------|------------|-----------|------------|
| `gerd_lag1` | **0.02746** | 0.01427 | **0.059** | [−0.00051, 0.05543] | 0.03100 | **0.409** | [−0.04833, 0.10325] |
| `lres` | 0.05629 | 0.00429 | ≈0 | [0.04787, 0.06470] | 0.00792 | ≈0 | [0.03690, 0.07567] |

---

## Что это значит

1. **Within-country условная ассоциация** GERD (lag1) и TFP при контроле researchers и общих шоков лет — не каузальный эффект GERD→TFP и не «конверсия науки».
2. Под **cluster SE** (G=7) доверительный интервал β_GERD **включает 0** (p≈0.409) → **это не finding эффекта**. HC1 p≈0.059 не «спасает» вывод.
3. **USA TFP = 1 by construction** каждый год (PWT ctfp) → нулевая within-вариация у USA; якорь панели, не результат.
4. Fragility (lag0/lag2, drop-one) уже в `regression_results_final.csv` — **только** как таблица хрупкости; **запрещено** lag shopping / HAC ради значимости.
5. **Не отвечает** на Frozen RQ / D1 (intensity vs volume). RQ закрывается Level 1 dual-scale + окнами данных.

---

## Разрешённый язык

- «условная ассоциация», «неотличимо от нуля под cluster SE», «дескриптивно / appendix»
- **Запрещено:** «эффект GERD на TFP», «доказательство конверсии», ответ на RQ через M1

---

## Что не делалось в этом проходе

- Нет пересчёта M1, нет новых SE, нет DiD/IV/HAC, нет lag shopping.

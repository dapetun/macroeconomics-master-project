# Тайвань (TWN): qualitative foundry hole

**Агент:** TechMatrixAgent  
**Дата:** 2026-09-20  
**Статус:** qualitative note only — **не** расширение панели, **не** импутация, **не** числовой ряд  
**Binding:** `DATA_CANON.md` §6 (панель = FRA, не TWN); `RQ_FREEZE.md` D2; `APPROVED_METHOD_SET.md` (TWN panel Not approved)  
**Связанные артефакты:** `tech_occupancy_matrix.md` (ячейка Semiconductors × PRD = `qual`); `tech_framework_unified.md`

---

## Зачем Тайвань важен для foundry

В цепочке полупроводников блок **PRD (production / scaling)** для advanced logic во многом опирается на **foundry**-модель: fabless-дизайн (часто США и союзники) → контрактное производство на advanced nodes → packaging / OSAT. Отраслевая литература и policy-дискуссия (CHIPS, export controls) регулярно указывают на **концентрацию frontier foundry** вне пары USA–CHN — прежде всего на Тайване (и частично на Корее) как на узле, без которого сравнение «США vs Китай по fab» структурно неполно.

В рамке TCI это значит: даже идеально измеренный bilateral US–CN trade **не** закрывает вопрос «кто производит advanced nodes». Foundry — отдельный контур **мощностей и узлов**, не тождественный экспорту HS8542.

---

## Почему отсутствие TWN в панели — дыра (FRA не замена)

Канон панели (`DATA_CANON` §6): 8-я страна = **FRA**, не TWN. Решение State A: **не добавлять** Тайвань, **не импутировать** foundry-доли.

| Что есть | Чего нет |
|----------|----------|
| FRA как comparator по general-macro (GERD, HC, trade incompleteness для HS8542) | Ряд TWN по fab capacity / node share / foundry revenue |
| `semi_exports_hs8542` для USA, CHN, KOR, JPN, GBR, ISR (фрагментарно) | Сопоставимый foundry-контур TWN в `tech_panel` |
| Qual-маркер в occupancy (PRD × semis) | Числовой gap US–CN–TWN по advanced fab |

**FRA ≠ substitute for TWN foundry.** Франция релевантна как европейский comparator по R&D/macro и как страна с **пустым** usable HS8542 в панели; она **не** закрывает missingness по advanced foundry. Подставлять FRA (или KOR/JPN trade) вместо TWN-foundry — нарушение D2: дыра читалась бы как «закрытая» или как нулевой разрыв.

В occupancy: Semiconductors × **PRD** = `qual` (TWN foundry hole); × **ADE** = `measured` trade с оговоркой **≠fab**.

---

## Что можно и нельзя утверждать

**Можно (qual / structural caveat):**
- Без учёта TWN (и смежных allied fab-узлов) bilateral US–CN semis-картина по **производству advanced nodes** — misspecification на уровне дизайна сравнения.
- Отсутствие TWN в панели = **результат missingness** (D2), часть ответа на RQ («какие звенья нельзя оценить»).
- HS8542-стоимости описывают **торговый контур**, не foundry leadership.

**Нельзя:**
- Фабриковать доли foundry, nm-shares, utilization, «TSMC % global» как «оценки проекта».
- Читать `semi_exports_hs8542` США/Китая как fab- или node-лидерство.
- Расширять панель на TWN «для красоты» в этом проходе.
- Ставить grade `+` / winner по advanced fab на expert-only спекуляции.
- Заменять TWN-дыру general-macro FRA или MVA % GDP.

---

## Объём и роль в тезисе

~1 страница qualitative context для SynthesisAgent: указать дыру, связать с ячейкой PRD×semis, запретить fab-claims из trade. Экономический эффект foundry / rent upstream **не измерен** панелью — только structural caveat вне causal conclusion.

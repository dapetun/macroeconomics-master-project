# ResearchDesignAgent — changelog

**Дата:** 2026-09-20  
**Brief:** ORCHESTRATION_PLAN.md §9.1  
**Target State:** A  
**Не делалось:** rewrite тела `final_project.md`; изменение `APPROVED_METHOD_SET.md`; сбор данных; регрессии; запуск других агентов.

---

## Change log table

| Change | Reason | Evidence | Files affected | Downstream impact |
|--------|--------|----------|----------------|-------------------|
| Создан `RQ_FREEZE.md` с Frozen RQ, D1, D2, архивом H1–H6 | Зафиксировать единственную обложку и hypothesis layer для State A | Binding texts = `APPROVED_METHOD_SET.md` / `final_project.md` §1.2; оркестрация §9.1 | `RQ_FREEZE.md` (**created**) | Все downstream агенты читают RQ/гипотезы отсюда |
| Hypothesis table → D1–D2 current; H1–H6 archived / not tested; ban SUPPORTED/PARTIAL/REJECTED | Заменить иллюзию «ещё дотестируем H» на measurable D1–D2 | Approved Set §D1–D2; `final_project.md` §2 отозвал partial | `reports/hypothesis_table.md` | Quant/Tech/Synthesis цитируют D1–D2, не H-verdicts |
| SUPERSEDED banner на `research_design.md` | §A–C всё ещё «Final RQ» / H1–H6 как живые | Grep: полный causal RQ в §A | `research_design.md` | Design history; не обложка |
| SUPERSEDED note на `remaining_risks.md` | §3 всё ещё «H1 partially supported» | Grep + `PROJECT_STATE.md` UNRESOLVED drift | `remaining_risks.md` | Не цитировать H-partial |
| SUPERSEDED banner на `reports/final_synthesis.md` | Живые H1 Partially supported / H4 partial | Grep §4/§6/§9 | `reports/final_synthesis.md` | Audit-trail only |
| ARCHIVE note на `technology_cases_final.md` | «H1 — partial macro» в синтезе | Grep ~L250 | `technology_cases_final.md` | TechMatrix читает occupancy, не H1-partial |
| PROPOSAL ONLY watermark на `DIAGNOSIS_AND_METHODOLOGY.md` | Working causal RQ §1; approval не здесь | Файл сам: «не утверждение»; Approved Set существует | `DIAGNOSIS_AND_METHODOLOGY.md` | Методы только из Approved Set |
| SUPERSEDED banner на `reports/tech_cases_comparison.md` | «H1 — partial macro» | Grep синтез | `reports/tech_cases_comparison.md` | Worst-offender watermark |
| ARCHIVE note на `research_logic_final.md` | Суженный RQ OK, но H-слой без D1–D2; приоритет гипотез устарел | §1.3 vs Frozen RQ windows; §2 H-table | `research_logic_final.md` | Логика OK как history; канон = RQ_FREEZE + hypothesis_table |
| SUPERSEDED framing на `.codex/AGENTS.md` | «превращаться в преимущества» = causal interest | Grep opening | `.codex/AGENTS.md` | Agent prompts не откатывают Frozen RQ |

---

## Grep scan: где ещё «живой» старый RQ / H-verdicts

### Watermarked (worst offenders / design-facing)

| File | Why watermarked |
|------|-----------------|
| `research_design.md` | §A = full causal RQ as «Final» |
| `remaining_risks.md` | H1 partially supported |
| `reports/final_synthesis.md` | H1 Partially supported |
| `technology_cases_final.md` | H1 partial macro |
| `DIAGNOSIS_AND_METHODOLOGY.md` | working organization→conversion RQ |
| `reports/tech_cases_comparison.md` | H1 partial macro |
| `research_logic_final.md` | H-layer без D1–D2; RQ без полных окон |
| `.codex/AGENTS.md` | causal interest framing |

### Listed only (changelog; не watermark — history / already revoked / Synthesis owns)

| File | Note |
|------|------|
| `final_project.md` §1.1 | Исходный RQ помечен как исходный; §1.2 = Frozen — **не трогать тело** (Synthesis) |
| `project_final.md` | Уже superseded `final_project.md` |
| `PROJECT_STATE.md` | Документирует исходный vs отвечаемый RQ; audit map |
| `ORCHESTRATION_PLAN.md` / `APPROVED_METHOD_SET.md` | Оркестрация / approval — корректно ссылаются на archive |
| `logic_changes.md`, `integration_changelog.md` | История отзыва partial |
| `reports/analysis_report.md` | Старый analysis trail (не в minimum targets; Synthesis/Quant зона) |

---

## Answers to §9.1 QUESTIONS

1. **Где ещё «живой» старый RQ?** Главные: `research_design.md` §A, `DIAGNOSIS_AND_METHODOLOGY.md` §1 working RQ, `.codex/AGENTS.md` interest, плюс H-partial в `remaining_risks.md` / `reports/final_synthesis.md` / tech cases. Полный список — таблицы выше.
2. **Нужен ли отдельный `RQ_FREEZE.md`?** **Да** — создан: единая точка Frozen RQ + D1–D2 + archive note + pointer to Approved Set (оркестрация оставляла вопрос открытым; brief пользователя требовал файл).

---

## Key conclusions (confidence)

| Conclusion | Label |
|------------|-------|
| Frozen RQ дословно совпадает с `final_project.md` §1.2 и Approved Set | **CONFIRMED** |
| D1–D2 measurable, non-causal; согласованы с intensity-vs-volume и missingness | **CONFIRMED** |
| H1–H6 явно archived / not tested; SUPPORTED/PARTIAL/REJECTED запрещены в hypothesis layer | **CONFIRMED** |
| Баннеры достаточны без rewrite тел stale-файлов | **LIKELY** |
| Все места с «живым» causal RQ пойманы grep'ом | **LIKELY** (brief scan; не полный corpus PDF/notebooks) |
| Synthesis должен позже выровнять `final_project.md` §2 на D1–D2 без полного rewrite сейчас | **NEEDS_REVIEW** (владелец: SynthesisAgent) |
| Числа dual-scale / occupancy подтверждают D1–D2 | **UNCERTAIN** в этом проходе (не запускались Quant/Tech; не собирались данные) |

---

## Acceptance checklist

- [x] Frozen RQ verbatim в `RQ_FREEZE.md` и `reports/hypothesis_table.md`
- [x] D1–D2 measurable, non-causal
- [x] H1–H6 explicitly archived / not tested
- [x] Changelog complete
- [x] `APPROVED_METHOD_SET.md` / тело `final_project.md` не изменены
- [x] Другие агенты не запускались

---

## HANDOFF

**→ DataCanonAgent** читает: `RQ_FREEZE.md`, `APPROVED_METHOD_SET.md`, `reports/hypothesis_table.md` (D1 окна), `data_reviewed/data_quality_final.md`.  
**→ QuantitativeAgent** читает: Frozen RQ + D1 (dual-scale / CAGR), Approved Core/Optional; **не** тестирует H1–H6.  
**→ TechMatrixAgent** читает: D2 + occupancy 8×4 требования Approved Set; `technology_cases_final.md` (с баннером).

*Конец ResearchDesignAgent_changelog.md.*

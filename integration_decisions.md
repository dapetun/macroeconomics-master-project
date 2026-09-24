# Integration decisions — SynthesisAgent

**Дата:** 2026-09-20  
**Brief:** ORCHESTRATION_PLAN.md §9.5  
**Тезис:** `final_project.md` (обновлён in place; отдельный `FINAL_THESIS.md` не создавался)

---

## Decision table

| Issue | Options | Decision | Reason | Evidence | Impact |
|-------|---------|----------|--------|----------|--------|
| Форма тезиса | (a) rewrite `final_project.md` in place; (b) новый `FINAL_THESIS.md` + pointer | **(a)** update `final_project.md` | Один путь обложки; бриф предпочитает in-place если cleaner; избегает dual-source drift | Upstream: Synthesis owns body; ResearchDesign не трогал тело | Adversarial читает один файл |
| Hypothesis layer | (a) оставить H1–H6 как «Not tested» таблицу в §2; (b) D1–D2 current + H archived | **(b)** D1–D2 current; H1–H6 archived | RQ_FREEZE / Approved Set; запрет SUPPORTED/PARTIAL | `RQ_FREEZE.md`; `reports/hypothesis_table.md`; Quant dual-scale; Tech occupancy | §2 совпадает с Frozen design |
| Центральный quant-результат | (a) snapshot §5.1 as before; (b) dual-scale table first | **(b)** §5.0 dual-scale = D1 center | Approved Core; Quant handoff | `dual_scale_intensity_volume.csv`; all intensity USA_higher / volume CHN_higher | D1 explicit in thesis |
| Articles CAGR | (a) одно окно; (b) оба + peak | **(b)** dual-window + USA peak 2021 | DATA_CANON; ни одно окно не sole canon | `articles_cagr_dual_window.csv`; peak 471378 @2021 | §5.0 / conclusion cite both |
| Tech section format | (a) четыре эссе AI/semis/HPC/quantum; (b) одна 8×4 occupancy | **(b)** occupancy + semis stress + TWN note | TechMatrix handoff; end four-essay; D2 | `tech_occupancy_matrix.md` (1/1/30); `tech_framework_unified.md` | §6 = holes map, no domain winners |
| TWN | (a) ignore; (b) expand panel; (c) qual hole + note | **(c)** qual + `TWN_FOUNDRY_QUAL_NOTE.md` | Approved: no TWN expansion; FRA≠substitute | DATA_CANON §6; occupancy PRD×semis=`qual` | Structural caveat in §6.3/§10 |
| M1 placement | (a) main productivity bridge; (b) appendix/secondary only; (c) drop entirely | **(b)** short §5.3 + Приложение A; not RQ answer | Approved Optional; cluster p≈0.409 | `M1_INTERPRETATION.md`; `regression_results_final.csv` | Defense can cite assoc.; no effect claim |
| PCA | (a) cite old F10/M2; (b) drop all PCA; (c) repair (a) appendix only, M2 unused | **(c)** PASS (a) optional appendix; M2 not run; old DO NOT USE | Quant gate PASS; Approved optional | `PCA_REPAIR_PASS.md`; F10_appendix intensity ONLY | §5.4 / App B; no tech→TFP |
| Mechanisms section | (a) list candidate mechanisms as findings; (b) NOT IDENTIFIED table | **(b)** §7 = NOT IDENTIFIED | Binding: no org→conversion; allow-list | Approved allow-list; DO_NOT_USE_QUANT | Purges «USA converts / China scales» |
| Winner language | (a) soft ranking by stage grades; (b) explicit no winner | **(b)** no overall / no domain winner | Frozen RQ; occupancy mostly `?` | 30/`?` cells; dual-scale denominator arithmetic | §8/§10 |
| Stale citations | (a) keep citing final_synthesis/remaining_risks; (b) DO NOT CITE | **(b)** bannered files not authority | DataCanon / ResearchDesign | SUPERSEDED banners; DATA_CANON §9 | Priority stack in preamble |
| Methods creep | (a) add DiD/IV/new series; (b) hold Approved Set | **(b)** no new methods / no State B | Brief WHAT NOT TO DO | `APPROVED_METHOD_SET.md` | Acceptance: methods match |
| Defense risks | (a) leave 2026-09-16 list; (b) refresh for D1/D2/M1/PCA/TWN | **(b)** refresh `defense_risks.md` | Expected professor Qs per brief | Updated Qs aligned to §5–§6 | Prep for Adversarial / defense |
| Patents citation | (a) resident-only 5.44×; (b) always pair + total-office 2.68× | **(b)** pair mandatory | DATA_CANON §5 | dual_scale both rows; snapshot 2021 | All key tables paired |
| BERD / GBR labels | (a) legacy financed / GBR 2019; (b) PERFORMED / GBR 2017 | **(b)** canon labels | DATA_CANON §§3–4 | quality_final; Quant F2 title | No finance-mix / 2019 drift |

---

## Open for AdversarialReviewer (known remaining risks)

1. Prose elsewhere in repo (notebooks, old reports) may still quote «converges/overtook» figure titles or H1-partial — thesis body purged; corpus-wide not rewritten.  
2. Expert-assessment language in old tech cases still on disk under SUPERSEDED banners — risk of accidental citation.  
3. M1 still numerically present — risk of overclaim if read without §5.3 caveats.  
4. PCA appendix figure could be misread as capability→TFP if caption ignored.  
5. Dual-scale «USA_higher / CHN_higher» could be misread as winner by stage if allow-list skipped.

---

## Append — Adversarial HIGH fixes (2026-09-20, parent / surgical fix)

| Issue | Options | Decision | Reason | Evidence | Impact |
|-------|---------|----------|--------|----------|--------|
| Stale PROJECT_STATE hierarchy | (a) leave 2026-09-16 stack; (b) refresh to RQ_FREEZE / Method Set / DATA_CANON / final_project 2026-09-20 | **(b)** refresh hierarchy + executive; adversarial = ready-with-fixes | ADV-H01 | `ADVERSARIAL_REVIEW.md`; `RQ_FREEZE.md` | Navigators cite canon, not stale authority |
| tech_cases one-liner + banner | (a) delete file; (b) DO NOT CITE + allow-list one-liner; fix pointer away from technology_cases_final | **(b)** neutralize L149; banner → final_project + occupancy + framework | ADV-H02/H03 | `reports/tech_cases_comparison.md` | No «превращают» / no broken authority path |
| D1 «supported» language | (a) leave; (b) «consistent with / matches_D1_sign» | **(b)** changelog + CSV header + hypothesis_table note | ADV-M01 (required in fix brief) | Quant changelog; dual_scale CSVs | No SUPPORTED drift for D1 |
| Oral M1 θ_lres / PCA / TWN | (a) separate DEFENSE_ORAL_NOTES.md; (b) section in defense_risks | **(b)** oral table in `defense_risks.md` + DO NOT OPEN list | ADV-H04/H05 | M1 cluster CI∋0; PCA PASS (a) | Author rehearsal checklist |
| Defense readiness label | (a) mark defense-ready; (b) HIGH closed; residual MEDIUM/LOW | **(b)** HIGH closed; residual MEDIUM/LOW for author | Brief WHAT NOT TO DO | `FIXES_APPLIED.md` | Honest status for Даниил |

*Конец integration_decisions.md.*

# FIXES_APPLIED — Adversarial HIGH (2026-09-20)

**Источник:** `REQUIRED_FIXES.md` / `ADVERSARIAL_REVIEW.md`  
**Агент:** surgical parent fix (не reopen State B; не DiD/IV/ML; не H1–H6 tests)  
**Статус:** **HIGH closed**; residual **MEDIUM/LOW** остаются автору (устные/слайды). Не «clean defense-ready».

---

## HIGH closed

| ID | Fix | Before → After | Files |
|----|-----|----------------|-------|
| **ADV-H01** | Refresh document hierarchy + executive | Hierarchy pointed to `final_project` 2026-09-16 + H1–H6 as current → **RQ_FREEZE / APPROVED_METHOD_SET / DATA_CANON / final_project (2026-09-20)**; **D1–D2** current; H1–H6 archived; PCA PASS (a); occupancy 1/1/30; adversarial **READY WITH FIXES**; SUPERSEDED list expanded | `PROJECT_STATE.md` |
| **ADV-H02** | Kill convert/scale one-liner | «США **превращают**… Китай — … масштаб…» → allow-list dual-scale / D1–D2 / no winner one-liner; H1/H4 partial bullets struck as **ОТОЗВАНО** | `reports/tech_cases_comparison.md` |
| **ADV-H03** | Fix banner authority pointer | Banner listed `technology_cases_final.md` as «актуальное» → **DO NOT CITE**; point to `final_project.md` + `tech_framework_unified.md` + `tech_occupancy_matrix.md` + `defense_risks.md` | `reports/tech_cases_comparison.md` |
| **ADV-H04** | Oral script M1 θ_lres | Caveats already in `final_project` §5.3/App A; **added** oral rehearsal table (θ_lres ≠ cadres→TFP; cluster CI∋0; PCA appendix-only; intensity≠model; HS8542≠fab; TWN hole) | `defense_risks.md` |
| **ADV-H05** | DO NOT CITE / DO NOT OPEN list | Thesis preamble already expanded; **added** defense «не открывать» list incl. tech_cases / analysis_report / technology_cases_final / pre-refresh PROJECT_STATE | `defense_risks.md` (+ prior `final_project.md`) |

**Also applied (brief item 3 / soft creep ADV-M01, lightweight):**

| Item | Before → After | Files |
|------|----------------|-------|
| D1 language | «D1 supported…» → «Level-1 signs **consistent with** D1»; CSV `supports_D1_level` → `matches_D1_sign`; hypothesis_table note post-Quant | `QuantitativeAgent_changelog.md`; `dual_scale_intensity_volume.csv`; `dual_scale_D1_summary.csv`; `scripts/quant_level1_pca_refresh.py`; `reports/hypothesis_table.md` |
| Latest-adversarial pointer | `final_changelog.md` (2016-09-16) looked like latest | Banner → superseded by `ADVERSARIAL_REVIEW.md` | `final_changelog.md` |
| Integration log | — | Append rows for adversarial fix decisions | `integration_decisions.md` |

---

## Residual MEDIUM / LOW (author — not closed here)

| ID | Severity | Residual | Owner action |
|----|----------|----------|--------------|
| **ADV-M02** | MEDIUM | SUPERSEDED bodies still contain H1-partial / 77% / cluster myths under banners | Slides only from `final_project` / `defense_risks` / dual-scale / occupancy |
| **ADV-M03** | MEDIUM | §0 steps 5–6 list M1/PCA in argument map | Oral: RQ = steps 1–4+7; M1/PCA only if asked |
| **ADV-M05** | MEDIUM | Old `figures/F10_pca_tfp_scatter.png` still on disk | Do not put on slides; if PCA → appendix intensity ONLY |
| **ADV-M07** | MEDIUM | App G / TWN concentration wording | Oral: structural caveat, shares не измерены (covered in defense_risks O5) |
| **ADV-L02** | LOW | Dense 2010-anchor paragraph in §5.1 | Cite from dual-scale/snapshot tables |
| (slides) | MEDIUM | Presentation not built | Author defense prep |

---

## Explicitly not done (per brief)

- No new data / methods / DiD / IV / ML  
- No State B reopen; no H1–H6 regrade  
- No full rewrite of SUPERSEDED corpora  
- No claim of full defense-ready while MEDIUM remain  

---

## Count

- **HIGH closed:** 5 / 5 (ADV-H01…H05)  
- **Residual MEDIUM/LOW:** listed above  

*Конец FIXES_APPLIED.md.*

# REQUIRED FIXES — после AdversarialReviewer

**Дата:** 2026-09-20  
**Источник:** `ADVERSARIAL_REVIEW.md`  
**Порядок:** сверху вниз; HIGH сначала. Не открывать State B; не добавлять DiD/IV/ML; не ставить SUPPORTED на H1–H6.

---

## Уже сделано в этом проходе (verify only)

| # | Fix | File | Status |
|---|-----|------|--------|
| 0a | Расширен DO NOT CITE + отказ от стека `PROJECT_STATE` | `final_project.md` преамбула | DONE |
| 0b | Caveat θ_lres (не causal / не RQ) | `final_project.md` §5.3 + App A | DONE |
| 0c | Anti–stage-winner note над §8 | `final_project.md` §8 | DONE |
| 0d | «Intensity-фактор» → intensity-индекс (не FA) | `final_project.md` App B | DONE |

---

## HIGH — сделать до защиты

### 1. Обновить `PROJECT_STATE.md` (ADV-H01)

- [x] Иерархия документов: `RQ_FREEZE` / `APPROVED_METHOD_SET` / `DATA_CANON` > `final_project.md` (**2026-09-20**) > dual-scale / occupancy > M1 numbers  
- [x] Executive: текущие гипотезы = **D1–D2**; H1–H6 = archived / not tested  
- [x] Методы: Core Level 1 + occupancy; M1/PCA optional; Not approved list  
- [x] Этап: Synthesis DONE; AdversarialReviewer DONE (этот проход); pointer → `ADVERSARIAL_REVIEW.md`  
- [x] Убрать implication, что adversarial 2026-09-16 — последний  

**Owner:** Parent — **DONE** (`FIXES_APPLIED.md`)  

### 2. Обезвредить `reports/tech_cases_comparison.md` (ADV-H02, ADV-H03)

- [x] Баннер: **DO NOT CITE**; актуальные = `final_project.md`, `tech_occupancy_matrix.md`, `defense_risks.md`  
- [x] **Убрать** pointer на `technology_cases_final.md` как «актуальное»  
- [x] Строку L149 «США превращают…» — удалить или заменить allow-list одной строкой без causal verbs / finance-модели  
- [x] Опционально: strikethrough блоков H1/H4 «partial» (L141–144)  

**Owner:** Author / parent — **DONE**  

### 3. Oral script: M1 θ_lres (ADV-H04)

- [x] В слайдах/речи: «значимый θ_researchers ≠ эффект кадров на TFP; FE-ассоциация; RQ закрывают dual-scale + holes»  
- [x] Не отвечать на RQ через M1  

**Owner:** Author — **DONE** (oral table in `defense_risks.md`; rehearse)  

### 4. Подтвердить DO NOT CITE в презе/заметках (ADV-H05)

- [x] В списке «не открывать на защите»: `remaining_risks`, `final_synthesis`, `tech_cases_comparison`, `analysis_report`, `technology_cases_final`, старый `PROJECT_STATE` до refresh  

**Owner:** Author — **DONE** (`defense_risks.md`)  

---

## MEDIUM — желательно до защиты

### 5. Убрать язык «D1 supported» (ADV-M01)

- [x] `QuantitativeAgent_changelog.md` L40: «supported» → «Level-1 signs **consistent with** D1»  
- [x] CSV: переименовать `supports_D1_level` → `matches_D1_sign` (или документировать alias в DATA_CANON)  

**Owner:** Author / Quant micro — **DONE** (lightweight with HIGH pass)  

### 6. Не цитировать SUPERSEDED-тела (ADV-M02)

- [ ] Слайды только из `final_project` / `defense_risks` / dual-scale / occupancy  
- [ ] Не копировать 77% / «cluster SE невозможны» / H1-partial  

**Owner:** Author  

### 7. Позиционирование M1/PCA (ADV-M03)

- [ ] В докладе: шаги 1–4 + conclusion сначала; M1/PCA только если спросят  

**Owner:** Author  

### 8. F10 на слайдах (ADV-M05)

- [ ] Не вставлять `figures/F10_pca_tfp_scatter.png`  
- [ ] Если нужен PCA: только `F10_appendix_pc1_intensity_ONLY.png` + «не vs TFP»  

**Owner:** Author  

### 9. Синхронизировать `hypothesis_table.md` (ADV-M06)

- [x] Одна фраза: после Quant/Synthesis Level-1 signs consistent with D1; **SUPPORTED не ставится**  

**Owner:** Author — **DONE** (lightweight)  

### 10. App G / TWN oral (ADV-M07)

- [x] Формула: «structural misspecification caveat; shares не измерены»  

**Owner:** Author — **DONE** in `defense_risks.md` O5 (rehearse)  

---

## LOW — по возможности

### 11. Pointer на актуальный adversarial (ADV-L03)

- [x] В `final_changelog.md` (2026-09-16) или `PROJECT_STATE`: «superseded as latest adversarial by `ADVERSARIAL_REVIEW.md`»  

**Owner:** Parent — **DONE**  

### 12. §5.1 2010-якоря (ADV-L02)

- [ ] При цитировании — из dual-scale/snapshot, не из плотного абзаца  

**Owner:** Author  

---

## Явно НЕ делать

- Не предлагать DiD / IV / ML / Elastic Net / k-means «чтобы усилить»  
- Не reopen State B / TOP500 / AI Index / TWN panel  
- Не объявлять winner  
- Не ставить H1–H6 SUPPORTED / PARTIAL / REJECTED  
- Не возвращать conversion ratios / pooled corr как inference  
- Не форсировать M2  

---

## Acceptance для parent

- [x] Все HIGH (1–4) закрыты или осознанно приняты  
- [x] Тезис остаётся State A descriptive  
- [x] Handoff: defense prep / presentation, не новый agent zoo  

См. `FIXES_APPLIED.md`. Residual MEDIUM: M02 (stale body discipline), M03 (oral arc), M05 (F10 slide).

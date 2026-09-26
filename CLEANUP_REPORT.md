# CLEANUP_REPORT — sanitary cleanup на `deep-research`

**Дата:** 2026-09-26  
**Режим:** audit → delete (слой 20pp уже подтверждён на `report-20pp`) → keep-core intact.

## Что удалено

- **~200 tracked файлов** слоя 20pp / State A, дублирующих ветку `report-20pp`: старые ноутбуки `01–05*`, `scripts/*.py` вне `deep/`, `data_reviewed/**` (кроме bridge), `figures/`, `results/*` вне `deep/`, `reports/`, `final_project.md`, `RQ_FREEZE.md`, `DEFENSE_GUIDE.md`, agent changelogs и пр.
- **Untracked AI/temp:** `_impl_tmp/`, `_review_tmp/`, `_audit_research_notes.md`, `CLEANUP_AUDIT.md`.

## Что оставлено (keep-core)

| Категория | Пути |
|-----------|------|
| Deep код | `notebooks/deep/`, `scripts/deep/` |
| Deep данные | `data/deep/`, `data/raw/deep/` |
| Deep результаты | `results/deep/` |
| Планы / RQ / аудиты | `DEEP_*`, `IMPLEMENTATION_*`, `AGENT_HANDOFF.md`, `METHODOLOGY_*`, `APPROVED_METHOD_SET.md`, `POST_IMPLEMENTATION_AUDIT*`, `reviews/` |
| Агенты | `.cursor/agents/` |
| Зависимости | `requirements-deep.txt`, `.gitignore` |

## Bridge (исключение)

Для воспроизведения старого M1 в D00/D01 оставлены:

- `data/deep/legacy/core_panel_reviewed.csv`
- `data/deep/legacy/regression_results_final.csv`

Полный 20pp-корпус — только на `report-20pp`.

## Правки документов / кода

- `AGENT_HANDOFF.md` §3: корпус 20pp → ветка `report-20pp`.
- `APPROVED_METHOD_SET.md`: баннер + авторитет чисел на `report-20pp`.
- `README.md`: точка входа для deep-research.
- `.gitignore`: `_impl_tmp/`, `_review_tmp/`, `_audit_research_notes.md`.
- `D00` / `D01`: путь к panel → `data/deep/legacy/…` (+ sync `.ipynb`).

## Валидация

```
python notebooks/deep/D00_data_audit.py   # ok
python notebooks/deep/D01_baseline.py     # ok
python notebooks/deep/D11_synthesis.py    # ok
```

## Риск

Локальные ссылки в исторических `DEEP_RESEARCH_PLAN.md` / `METHODOLOGY_OPTIONS.md` на `RQ_FREEZE.md` / старые ноутбуки остаются как история; актуальная навигация — `README.md` + `AGENT_HANDOFF.md`.

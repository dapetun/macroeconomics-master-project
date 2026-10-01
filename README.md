# Macroeconomics master project

Аналитический трек: панель OECD+Китай, гипотезы H1–H7.
Analysis track: OECD+China panel, hypotheses H1–H7.

## Структура / Layout

| Путь | Содержание |
|------|------------|
| `src/macrodeep/` | Общая библиотека (пути, стиль, I/O, эконометрика, графики) |
| `notebooks/deep/` | Скрипты анализа `D00`–`D11` |
| `scripts/deep/` | Загрузка сырых данных и сборка панели |
| `data/` | Сырые и собранные данные |
| `results/deep/` | Таблицы и рисунки |
| `reports/` | Отчёты и презентация |
| `tests/` | Минимальные smoke-тесты |

## Документы для сдачи / Deliverables

| Файл | Содержание |
|------|------------|
| `reports/Отчёт по проекту макра.docx` | Основной отчёт |
| `reports/REPORT_PLAIN.docx` | Упрощённая версия отчёта |
| `reports/PRESENTATION.pptx` | Презентация |

## Установка / Install

Нужны оба шага (editable-пакет + pinned runtime deps для download/Excel):

```bash
pip install -r requirements-deep.txt
pip install -e .
```

`pyproject.toml` задаёт минимальные зависимости пакета `macrodeep` (numpy/pandas/matplotlib/statsmodels).
`requirements-deep.txt` — полный runtime для пайплайна и download-скриптов (`requests`, `openpyxl`, `scipy`, …).
Файл `uv.lock` — локальный артефакт uv; в git не коммитится (см. `.gitignore`).

## Запуск / Run

```bash
python notebooks/run_all.py          # весь пайплайн в одном процессе
python notebooks/deep/D00_data_audit.py
# … D01 … D11 по отдельности
python -m pytest tests -q
```

## Архив методологических MD / Docs archive

Перед сдачей намеренно убраны промежуточные агентские и плановые markdown
(`AGENT_HANDOFF.md`, `DEEP_*`, `IMPLEMENTATION_*`, `METHODOLOGY_*`, `reviews/` и т.п.).
Они **не потеряны**: остаются в git history ветки `deep-research` / коммитов до cleanup на `final-alignment`
(см. также родитель коммита `5f14cd5` для части data/docs cleanup).

Канон для сдачи: код + `data/` + `results/` + `reports/`. Исследовательский контекст RQ/аудитов —
из history при необходимости, не из working tree.

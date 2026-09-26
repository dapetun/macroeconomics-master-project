# IMPLEMENTATION_PLAN.md — поэтапная реализация исправлений по методологическому аудиту

**Ветка:** `deep-research` (база: коммит `df073d1`).
**Основание:** `METHODOLOGY_AUDIT.md` → `REVIEW_OF_METHODOLOGY_AUDIT.md` → решения Даниила от 2026-09-26.
**Сопутствующие документы:** `AGENT_HANDOFF.md` (контекст и правила для агентов), `IMPLEMENTATION_CHECKLIST.md` (галочки по шагам).
**Принцип:** новых методов нет. Исправляем данные, добавляем три согласованные спецификации, честно переписываем вердикты и текст. Каждый этап: реализация → проверка → понимание результата → коммит → следующий этап.

---

# Часть 0. Что решено до начала реализации

## 0.1. Согласовано (менять нельзя)

1. Главный вопрос о «двух путях развития» остаётся **рамкой**. Выводы делаются только по пяти измеримым подвопросам A–E (текст — в Stage 8).
2. **США в Comtrade докачиваем.** Причина отсутствия найдена: в загрузчике используются устаревшие коды стран (841 вместо 842 для США, 58 вместо 56 для Бельгии).
3. **H1:** норма показывается в двух равноправных вариантах — «доход + население» и «только доход». Вариант «норма без Китая» и вариант с квадратом дохода — проверки.
4. **H2:** основная спецификация — **раздельная**: интенсивность R&D и ВВП по отдельности. Прежняя модель с объёмом R&D остаётся как проверка. Решение принято **после** расчётов, это фиксируется в `DEEP_DEVIATIONS.md`.
5. **H3** остаётся в основном тексте как честный отрицательный результат, вердикт — «не согласуется».
6. **H7** подаётся как хрупкий результат с оговоркой, без сильных выводов. LPM остаётся.
7. **Тест Хаусмана** исправляется: одинаковые эффекты года в FE и RE, классические стандартные ошибки.
8. **Солоу:** основное сравнение — вклады в процентных пунктах; доли TFP — дополнение.
9. Предсказания H1–H7 в `DEEP_RQ_AND_HYPOTHESES.md` **не переписываются** (вопреки совету аудитора). Новые наблюдения подаются отдельно, с пометкой «обнаружено после расчётов».
10. Слово «preregistered» убирается. Формулировка: «гипотезы сформулированы в плане до расчётов».
11. Бюджет: 1–2 выходных. Ветка — `deep-research`. Коммит `df073d1` переносить не нужно: он уже в `deep-research`.

## 0.2. Отклонено (не возвращать без решения Даниила)

- DiD, event study, synthetic control, IV, динамическая панель (GMM): нет контрольной группы, после событий 2022 года только 1 год данных, нет правдоподобного инструмента.
- Random Forest, Gradient Boosting, LASSO и любое ML: ни один вопрос проекта не является задачей прогноза, нужны интерпретируемые коэффициенты.
- Кластеризация стран, новый PCA, составной индекс: главная находка — страны сильны в **разных** звеньях, одно число это скроет. Старый PCA в ноутбуках `notebooks/03_pca.ipynb` не трогаем.
- Регрессии рядов TOP500 и Epoch на макропоказатели: мало точек, эффект слишком свежий.
- Расширение панели развивающимися странами; вариант D (сравнение с Кореей и Японией).
- Дополнительные проверки устойчивости сверх уже посчитанных в D03 и D04.
- «Обязательное» обновление статуса `METHODOLOGY_OPTIONS.md` и `APPROVED_METHOD_SET.md`.

## 0.3. Что может измениться по ходу (правила заданы заранее)

- **Вердикт H5** зависит от того, окажутся ли США в тройке экспортёров оборудования HS8486 в 2023 году. Правило — в Stage 7.
- **Значения RCA** изменятся, потому что в выборку войдут США и Бельгия. Это ожидаемо.
- **Сумма «зеркала» Тайваня** вырастет, потому что добавится импорт США из Тайваня. Это ожидаемо.
- **Числа по старым странам Comtrade** могут немного измениться из-за пересмотра данных в Comtrade. Правило — в Stage 6 (DP-6b).
- **Вердикт H6** станет «согласуется частично»: в 2010, 2013 и 2014 годах доля Китая по мощности не ниже доли по числу систем.

## 0.4. Точки решения человека (DECISION REQUIRED)

- **DP-0.** Исходные результаты не воспроизводятся (Stage 0).
- **DP-6a.** Докачка Comtrade не удалась (Stage 6).
- **DP-6b.** Пересмотр данных Comtrade изменил старые страны больше чем на 1 % во многих строках (Stage 6).
- **DP-4.** Независимый ревьюер эконометрики нашёл расхождение со спецификацией (Stage 4).
- **DP-any.** Любое проверяемое число отличается от ожидаемого больше чем на 10 % или имеет другой знак.
- **DP-8b.** Выполнять ли необязательный этап 8b.

Формат для каждой точки — в `AGENT_HANDOFF.md`, раздел «Как запрашивать решение».

---

# Часть 1. Master Plan

## 1.1. Порядок выполнения

```text
S0 Подготовка и проверка воспроизводимости      [Critical, небольшой]
 │
 ├─ S1 H1: варианты нормы                         [Core, небольшой]
 ├─ S2 H2: раздельная спецификация                [Core, небольшой]
 ├─ S3 Хаусман + Солоу в п.п. + имена в H7        [Core, небольшой]
 │
 ├─ S4 Независимая проверка эконометрики (только чтение)   [Critical gate]
 │      выполняется ПАРАЛЛЕЛЬНО с S5 → S6
 ├─ S5 TOP500: столбцы и единицы мощности (H6)    [Critical, небольшой]
 ├─ S6 Comtrade: США и Бельгия, подписи партнёров (H5)   [Critical, средний, нужна сеть]
 │
 S7 Сводные таблицы D10/D11 с вердиктами, рассчитанными кодом   [Core, средний]
 │
 S8 Тексты: подвопросы, результаты, макросвязь, ограничения     [Core, средний]
 │
 (S8b Необязательная доработка — только по решению DP-8b)       [Optional]
 │
 S9 Интеграция и проверка согласованности       [Critical, средний]
 │
 S10 Финальный независимый методологический аудит (только чтение)   [Critical]
```

Строгая последовательность для исполнителя: **S0 → S1 → S2 → S3 → (S4 параллельно с S5 → S6) → S7 → S8 → [S8b] → S9 → S10**.

Почему эконометрика идёт раньше данных: S1–S3 и S5–S6 не зависят друг от друга по данным (Comtrade и TOP500 не входят в панель). При таком порядке независимый ревьюер S4 проверяет эконометрику, пока исполнитель чинит данные.

## 1.2. Граф зависимостей

```text
S0 ──► S1 ──► S2 ──► S3 ──┬──► S4 (review, read-only) ──┐
                          └──► S5 ──► S6 ───────────────┼──► S7 ──► S8 ──► [S8b] ──► S9 ──► S10
```

- **S1, S2, S3** логически независимы (разные файлы), но выполняются **последовательно** в одном рабочем дереве, чтобы не смешивать коммиты.
- **S4** можно запускать параллельно с **S5 и S6**: ревьюер только читает D01–D05 и D08, а S5/S6 меняют другие файлы (D06, D07, `download_comtrade.py`, `data/raw/deep/comtrade/`).
- **S7** стартует только после принятия S4 **и** S6.

## 1.3. Git-чекпоинты

- После принятия каждого этапа оркестратор ставит локальный тег `impl-sN-ok` (S0: `impl-s0-ok`).
- Откат незакоммиченных правок: `git restore --staged --worktree <пути этапа>`.
- Откат закоммиченного неудачного этапа: `git reset --hard <последний тег impl-*-ok в порядке выполнения>`. Это безопасно: коммиты не отправлены на сервер, а неотслеживаемые файлы (`METHODOLOGY_AUDIT.md`, `_review_tmp/` и другие) `reset` не удаляет.
- **Исключение:** если проблему нашёл S4 уже после коммитов S5/S6, не откатывать, а исправлять **отдельным коммитом вперёд**.
- Запрещено: `git push`, `git clean`, `git rebase`, `git add -A`, `git add .`, любые действия с `main` и `retro`.

## 1.4. Модели агентов (подробно — в `AGENT_HANDOFF.md`, раздел Agent Architecture)

- **Оркестратор:** Claude Opus 5.5, High (`claude-opus-5-5-high`).
- **Исполнитель этапов S0–S3, S5–S9, S8b:** Claude Sonnet 5, High Thinking (`claude-sonnet-5-thinking-high`). Новый субагент на каждый этап.
- **Независимые ревьюеры S4 и S10:** Claude Opus 5.5, High (`claude-opus-5-5-high`), режим только чтения.
- Claude Sonnet 5 Medium в Cursor недоступен, поэтому не используется. Composer 2.5 не нужен: механической работы здесь мало, и она встроена в этапы.

---

# Часть 2. Общие правила для всех этапов

## 2.1. Как запускать код

- Ноутбук = скрипт `notebooks/deep/DXX_*.py` (jupytext percent). Запуск из корня репозитория: `python notebooks/deep/DXX_имя.py`.
- Парные `.ipynb` хранятся **без выводов**. После правки `.py` синхронизировать пару: `jupytext --to ipynb notebooks/deep/DXX_имя.py`. Флаг `--execute` не использовать: в ядре Jupyter нет `__file__`.
- Скрипты пишут только в `results/deep/tables/` и `results/deep/figures/`. Сторонних эффектов нет (проверено).
- Панель `data/deep/panel_oecd_chn.csv` (936 × 57, 39 стран × 2000–2023, без дубликатов страна-год) **не пересобирается**. `scripts/deep/build_panel.py` не запускать.

## 2.2. Временные файлы

Все проверочные скрипты — в неотслеживаемой папке `_impl_tmp/`. Её не коммитить. В Stage 0 создаётся помощник `_impl_tmp/compare_with_head.py`: он сравнивает таблицу с версией из git и печатает добавленные, удалённые и изменённые строки.

## 2.3. Пять уровней проверки (для каждого этапа)

1. **Техническая:** скрипт завершился без ошибок, файлы созданы, в выводе нет предупреждений `FAIL` или `Traceback`.
2. **Данные:** размер, число наблюдений, страны, годы, пропуски, дубликаты, единицы.
3. **Статистическая:** коэффициенты, p-value, N, число кластеров G совпадают с ожидаемыми в пределах допуска.
4. **Экономическая:** знак и порядок величины осмысленны. Если число выглядит странно, сначала проверить данные, единицы, преобразования и спецификацию и только потом код.
5. **Воспроизводимость:** повторный запуск того же скрипта даёт идентичные CSV (`git diff --stat` пуст после второго запуска). Таблицы, которые этап не должен был менять, не изменились.

## 2.4. Допуски

- Коэффициенты и доли — ±10 % от ожидаемого (или ±0,01 для величин меньше 0,1).
- p-value — та же сторона от порогов 0,05 и 0,10, что и в ожидании.
- N и G — точное совпадение.
- При выходе за допуск — **DP-any**: остановиться и сообщить.

## 2.5. Документация по ходу

Каждый этап, который меняет данные, переменные, спецификацию или вердикт, добавляет строку в конец таблицы `DEEP_DEVIATIONS.md`. Формат из 5 столбцов: `| 2026-09-26 | REV-Sx | Что изменено | Почему | Влияние на выводы |`. Файл в UTF-8. В PowerShell он может отображаться «кракозябрами» — это проблема консоли, а не файла; править через редактор или Python с `encoding="utf-8"`.

`DEEP_RESULTS.md` до Stage 8 помечен баннером «идёт пересмотр» (ставится в Stage 0), поэтому временное расхождение чисел в нём допустимо.

## 2.6. Шаблон отчёта исполнителя оркестратору (после каждого этапа)

```text
Stage: Sx
Status: PASSED / FAILED / BLOCKED (DP-..)
Changed files: <git show --stat HEAD>
Validation: <вывод проверок, ключевые числа: ожидалось → получено>
Economic check: <1–3 предложения>
Unchanged-check: <какие таблицы сравнены, результат>
Docs updated: <строка DEEP_DEVIATIONS / нет>
Out-of-scope issues found: <список или "нет">
Commit: <hash, message>
```

---

# Часть 3. Detailed Stage Plans

---

## Stage 0 — Подготовка и проверка воспроизводимости

**Приоритет:** Critical. **Объём:** небольшой, 2–4 файла, новых данных нет. **Риск:** исходные результаты могут не воспроизводиться.

**Goal.** Убедиться, что окружение работает и текущие результаты воспроизводятся без изменений. Зафиксировать исходную точку и пометить `DEEP_RESULTS.md` как пересматриваемый.

**Исследовательская задача.** Без воспроизводимой исходной точки нельзя отличить эффект исправлений от случайных расхождений.

**Depends on:** —. **Blocks:** все этапы.

**Предпосылки.** Установлены пакеты из `requirements-deep.txt`.

**Файлы для изучения:** `AGENT_HANDOFF.md`, этот план, `requirements-deep.txt`, `notebooks/deep/_common.py`.

**Можно изменять:** `DEEP_RESULTS.md` (только баннер), `_impl_tmp/*`. Коммитятся: `IMPLEMENTATION_PLAN.md`, `IMPLEMENTATION_CHECKLIST.md`, `AGENT_HANDOFF.md`, `METHODOLOGY_AUDIT.md`, `REVIEW_OF_METHODOLOGY_AUDIT.md`.

**Нельзя изменять:** всё остальное. `_audit_research_notes.md` и `_review_tmp/` не коммитить.

**Данные / переменные / метод:** не меняются.

### Implementation

1. `git switch deep-research`; `git status --short`. Ожидаемые неотслеживаемые файлы: `METHODOLOGY_AUDIT.md`, `REVIEW_OF_METHODOLOGY_AUDIT.md`, `_audit_research_notes.md`, `_review_tmp/`, три файла плана. Отслеживаемых изменений быть не должно.
2. `git tag impl-s0-base` на текущем HEAD.
3. Проверка окружения: `python -c "import pandas, numpy, statsmodels, linearmodels, scipy, jupytext, requests, matplotlib; print('ok')"`.
4. Создать `_impl_tmp/compare_with_head.py`:

```python
import io, subprocess, sys
import pandas as pd

path = sys.argv[1]
ref = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
old_txt = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
old = pd.read_csv(io.StringIO(old_txt))
new = pd.read_csv(path)
print(f"{path}: old {old.shape} new {new.shape}")
print("columns added:", sorted(set(new.columns) - set(old.columns)), "removed:", sorted(set(old.columns) - set(new.columns)))
common = [c for c in old.columns if c in new.columns]
m = old[common].merge(new[common], how="outer", indicator=True)
print(m["_merge"].value_counts().to_string())
diff = m[m["_merge"] != "both"]
if len(diff):
    print(diff.head(40).to_string())
```

5. Запустить все ноутбуки по порядку: D00, D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11 (`python notebooks/deep/<файл>.py`).
6. `git status --porcelain results/deep`.
7. В начало `DEEP_RESULTS.md`, сразу после заголовка, вставить:
   `> **Статус (2026-09-26):** идёт пересмотр по REVIEW_OF_METHODOLOGY_AUDIT.md. Числа и вердикты ниже будут обновлены в Stage 8 IMPLEMENTATION_PLAN.md. До этого ориентироваться на results/deep/tables/D11_hypothesis_verdicts.csv.`

### Validation

- **Техническая:** все 12 скриптов завершились без ошибок.
- **Воспроизводимость:** после шага 6 **нет изменённых CSV** в `results/deep/tables/`. Если изменились только PNG — записать в чеклист «PNG недетерминированы», выполнить `git restore results/deep/figures`, в дальнейшем коммитить только PNG изменённых этапом скриптов.
- **Данные:** `python -c "import pandas as pd; p=pd.read_csv('data/deep/panel_oecd_chn.csv'); print(p.shape, p.duplicated(['country_iso3','year']).sum())"` → `(936, 57) 0`.

### Acceptance criteria

Окружение работает; исходные CSV воспроизводятся байт в байт; баннер добавлен; помощник сравнения создан.

### Failure conditions

- Скрипт падает → остановиться, показать трассировку. Код не править.
- Изменились CSV → **DP-0**: исходная точка не воспроизводится. Показать `git diff --stat` и 5 первых различий из `compare_with_head.py`. Дальше не идти.

### Interpretation / Limitations

Этап не влияет на выводы. Ограничение: PNG могут отличаться побайтно при одинаковом содержании.

### Rollback

`git restore DEEP_RESULTS.md results/deep`.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking. Задача: шаги 1–7 и проверка. Depends on: —. Can run in parallel with: —. Blocks: S1.

### Commit

`git add IMPLEMENTATION_PLAN.md IMPLEMENTATION_CHECKLIST.md AGENT_HANDOFF.md METHODOLOGY_AUDIT.md REVIEW_OF_METHODOLOGY_AUDIT.md DEEP_RESULTS.md .cursor/agents/stage-implementer.md .cursor/agents/econometrics-reviewer.md .cursor/agents/final-methodology-auditor.md`
`git commit -m "docs: add implementation plan, audit review; mark DEEP_RESULTS as under revision"`
Оркестратор после принятия: `git tag impl-s0-ok`.

**Next Stage:** S1.

---

## Stage 1 — H1: два варианта нормы и проверки

**Приоритет:** Core. **Объём:** небольшой, 1 скрипт + 1 документ. **Риск:** низкий.

**Goal.** Показать отклонения США и Китая от нормы в двух равноправных вариантах: «доход + население» и «только доход», плюс две проверки. Явно зафиксировать, что для Китая норма по населению — прогноз за пределами выборки.

**Исследовательская задача.** Подвопрос A: по каким показателям США и Китай отклоняются от типичного уровня для стран с сопоставимым доходом (и размером)?

**Depends on:** S0. **Blocks:** S4, S7.

**Файлы для изучения:** `notebooks/deep/D02_benchmarking.py`, раздел H1 в `DEEP_RQ_AND_HYPOTHESES.md`, `REVIEW_OF_METHODOLOGY_AUDIT.md` (замечание 14).

**Можно изменять:** `notebooks/deep/D02_benchmarking.py`, `notebooks/deep/D02_benchmarking.ipynb` (через jupytext), `DEEP_DEVIATIONS.md` (одна строка).

**Нельзя изменять:** логику существующих таблиц `D02_residuals_all`, `D02_residuals_norm_without_chn`, `D02_profile_2019_2023`, `D02_quadratic_check` (они должны остаться идентичными).

**Данные:** панель; показатели `rd_gdp`, `researchers_pm`, `articles_pm`, `pat_res_pm`, `mva_share`, `hitech_share`; регрессоры `ln_gdppc`, `ln_pop`, `year`.

**Переменные.** Новая локальная переменная `ln_gdppc2 = ln_gdppc²` (внутри функции, в панель не пишется).

### Метод и спецификация

Pooled OLS с эффектами года, **без** эффектов страны: сравниваем страну с другими странами того же года, а не с самой собой.

```text
ln(k_it) = a + b1·ln_gdppc_it + b2·ln_pop_it + λ_t + e_it          (вариант with_pop)
ln(k_it) = a + b1·ln_gdppc_it + λ_t + e_it                        (вариант without_pop)
ln(k_it) = a + b1·ln_gdppc_it + b2·ln_pop_it + λ_t + e_it, оценено без CHN   (проверка with_pop_norm_without_chn)
ln(k_it) = a + b1·ln_gdppc_it + b3·ln_gdppc_it² + b2·ln_pop_it + λ_t + e_it  (проверка with_pop_quadratic)
```

- `k_it` — показатель k страны i в году t (6 показателей, каждый в отдельной регрессии).
- `ln_gdppc` — логарифм ВВП на душу по ППС; `ln_pop` — логарифм населения.
- `λ_t` — эффекты года (общие для всех стран сдвиги).
- `e_it` — остаток. **Отклонение от нормы** = `exp(e_it) − 1`, в процентах; среднее за 2019–2023 годы для USA и CHN.
- Единица наблюдения: страна-год; период 2000–2023; 39 стран. Стандартные ошибки не используются: это описательное сравнение без статистического вывода.

### Implementation

1. Заменить функцию `residuals_for` на версию с параметром `rhs`:

```python
def residuals_for(k: str, df: pd.DataFrame, exclude_chn: bool = False,
                  rhs: str = "ln_gdppc + ln_pop + C(year)") -> pd.DataFrame:
    d = df.dropna(subset=[k, "ln_gdppc", "ln_pop"]).copy()
    d["ln_gdppc2"] = d["ln_gdppc"] ** 2
    d["lnk"] = np.log(d[k].where(d[k] > 0))
    d = d.dropna(subset=["lnk"])
    train = d[d["country_iso3"] != "CHN"] if exclude_chn else d
    res = smf.ols(f"lnk ~ {rhs}", data=train).fit()
    d["resid"] = d["lnk"] - res.predict(d)
    d["pct_above"] = np.exp(d["resid"]) - 1
    d["indicator"] = k
    return d[["country_iso3", "year", "indicator", "resid", "pct_above"]]
```

2. Перед комментарием `# quadratic robustness summary` вставить блок вариантов (переменные `inds`, `ypos`, `w` уже определены выше в файле):

```python
VARIANTS = {
    "with_pop": ("ln_gdppc + ln_pop + C(year)", False),
    "without_pop": ("ln_gdppc + C(year)", False),
    "with_pop_norm_without_chn": ("ln_gdppc + ln_pop + C(year)", True),
    "with_pop_quadratic": ("ln_gdppc + ln_gdppc2 + ln_pop + C(year)", False),
}
vrows = []
for vname, (rhs, excl) in VARIANTS.items():
    for k in inds:
        r = residuals_for(k, panel, exclude_chn=excl, rhs=rhs)
        r = r[r.country_iso3.isin(["USA", "CHN"]) & r.year.between(2019, 2023)]
        for c, v in r.groupby("country_iso3")["pct_above"].mean().items():
            vrows.append({"variant": vname, "indicator": k, "country_iso3": c, "pct_above": v})
variants = pd.DataFrame(vrows)
save_table(variants, "D02_profile_variants_2019_2023")

fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
for ax, vname, title in [(axes[0], "with_pop", "Норма: доход + население"),
                         (axes[1], "without_pop", "Норма: только доход")]:
    sub = variants[variants.variant == vname]
    u = sub[sub.country_iso3 == "USA"].set_index("indicator").reindex(inds)["pct_above"] * 100
    c = sub[sub.country_iso3 == "CHN"].set_index("indicator").reindex(inds)["pct_above"] * 100
    ax.barh(ypos - w / 2, u, w, label="USA", color=COLOR_USA)
    ax.barh(ypos + w / 2, c, w, label="CHN", color=COLOR_CHN)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_yticks(ypos)
    ax.set_yticklabels(inds)
    style_axes(ax, title=title, xlabel="% выше/ниже нормы, среднее 2019–2023")
axes[0].legend()
save_fig(fig, "D02_profile_with_vs_without_pop")

last = panel[panel.year == 2019]
others = last[~last.country_iso3.isin(["USA", "CHN"])]
support = pd.DataFrame([{
    "ln_pop_CHN": float(last.loc[last.country_iso3 == "CHN", "ln_pop"].iloc[0]),
    "ln_pop_USA": float(last.loc[last.country_iso3 == "USA", "ln_pop"].iloc[0]),
    "ln_pop_max_others": float(others["ln_pop"].max()),
    "ln_gdppc_CHN": float(last.loc[last.country_iso3 == "CHN", "ln_gdppc"].iloc[0]),
    "ln_gdppc_min_others": float(last.loc[last.country_iso3 != "CHN", "ln_gdppc"].min()),
}])
save_table(support, "D02_support_check")
```

3. Запустить `python notebooks/deep/D02_benchmarking.py`; `jupytext --to ipynb notebooks/deep/D02_benchmarking.py`.
4. Добавить строку в `DEEP_DEVIATIONS.md`: `| 2026-09-26 | REV-S1 | H1: добавлены варианты нормы (без населения, норма без Китая, квадрат дохода) и проверка области данных | Вывод о США менял знак в зависимости от учёта населения; Китай вне выборки по населению | Вывод о США формулируется условно; вывод о Китае устойчив по знаку |`.

### Expected output

`D02_profile_variants_2019_2023.csv` (48 строк = 4 варианта × 6 показателей × 2 страны), `D02_support_check.csv`, `D02_profile_with_vs_without_pop.png`.

### Validation

- **Техническая:** скрипт без ошибок; три новых файла созданы.
- **Данные:** 48 строк, 4 уникальных `variant`, 6 `indicator`, 2 страны, пропусков в `pct_above` нет.
- **Статистическая** (в процентах, `pct_above × 100`):
  - `rd_gdp`: CHN with_pop +91, without_pop +186, norm_without_chn +177, quadratic ≈ +89; USA with_pop −6, without_pop +41, norm_without_chn +3, quadratic ≈ −4;
  - `pat_res_pm`: CHN with_pop +812, without_pop +3628; USA with_pop +13, without_pop +373.
- **Проверка области данных:** `ln_pop_CHN` ≈ 21,07; `ln_pop_USA` ≈ 19,62; `ln_pop_max_others` ≈ 18,66; `ln_gdppc_CHN` ≈ 9,84; `ln_gdppc_min_others` ≈ 9,76.
- **Неизменность:** `python _impl_tmp/compare_with_head.py results/deep/tables/D02_profile_2019_2023.csv` → все строки `both`. То же для `D02_residuals_all.csv`, `D02_residuals_norm_without_chn.csv`, `D02_quadratic_check.csv`.
- **Экономическая:** у Китая все шесть показателей выше нормы в обоих вариантах (знак «+»). У США знак `rd_gdp` меняется между вариантами — так и должно быть: население положительно связано с долей R&D, поэтому для большой страны «ожидаемая» доля выше.
- **Воспроизводимость:** второй запуск D02 не меняет CSV.

### Acceptance criteria

Все проверки пройдены; старые таблицы идентичны; строка в `DEEP_DEVIATIONS.md` добавлена.

### Failure conditions

- Старые таблицы D02 изменились → ошибка в новой функции; исправлять только в рамках S1.
- Знак CHN в одном из основных вариантов отрицательный или числа вне допуска → **DP-any**.

### Interpretation

Это **описательное сравнение**, а не «правильный уровень» и не причинный эффект. Формулировка: «на X % выше типичного уровня для страны с таким доходом (и размером) в тот же год». Вывод о Китае («выше нормы почти по всем показателям») устойчив по знаку, но величина меняется в 2–4 раза. Вывод о США **зависит** от того, учитывается ли размер страны.

### Limitations

Норма построена почти только по богатым странам; для Китая это прогноз за пределами выборки по населению (ln_pop 21,1 при максимуме 18,7 у остальных, кроме США). Показатели — объёмы и доли, а не качество.

### Rollback

`git restore notebooks/deep/D02_benchmarking.* results/deep DEEP_DEVIATIONS.md`.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking. Depends on: S0. Parallel with: —. Blocks: S2.

### Commit

`git add notebooks/deep/D02_benchmarking.py notebooks/deep/D02_benchmarking.ipynb results/deep/tables/D02_profile_variants_2019_2023.csv results/deep/tables/D02_support_check.csv results/deep/figures/D02_profile_with_vs_without_pop.png DEEP_DEVIATIONS.md`
`git commit -m "feat(H1): add norm variants with/without population and support check"`
Тег оркестратора: `impl-s1-ok`. **Next Stage:** S2.

---

## Stage 2 — H2: раздельная спецификация (интенсивность R&D + ВВП)

**Приоритет:** Core. **Объём:** небольшой, 1 скрипт + 2 файла описания. **Риск:** низкий.

**Goal.** Сделать основной модель, в которой интенсивность R&D и ВВП оцениваются отдельно. Прежнюю модель с объёмом R&D оставить как проверку. Исправить описание `rd_ppp` в словаре данных.

**Исследовательская задача.** Подвопрос B: как в среднем по 39 странам R&D связан с патентами? Главный вопрос на защите: «не отражает ли связь просто размер экономики?»

**Depends on:** S1. **Blocks:** S4, S7.

**Файлы для изучения:** `notebooks/deep/D03_knowledge_production.py`, `notebooks/deep/_common.py` (функция `twfe`), `scripts/deep/build_panel.py` (строки 100–110, 174), `data/deep/data_dictionary_deep.csv`, замечания 3, 5 и 20 в `REVIEW_OF_METHODOLOGY_AUDIT.md`.

**Можно изменять:** `notebooks/deep/D03_knowledge_production.py` и `.ipynb`; в `data/deep/data_dictionary_deep.csv` — только строку `rd_ppp`; в `scripts/deep/build_panel.py` — только кортеж `("rd_ppp", ...)` на строке 174 (текст описания); `DEEP_DEVIATIONS.md`.

**Нельзя изменять:** существующие спецификации D03 (они должны дать идентичные строки); `_common.py`; панель; `build_panel.py` не запускать.

**Данные:** панель, 39 стран, 2000–2021 (патенты заканчиваются в 2021 году).

**Переменные** (создаются внутри D03, в панель не пишутся):
- `ln_rd_gdp_lag1 = ln(rd_gdp_{i,t−1})` — логарифм доли R&D в ВВП с лагом 1;
- `ln_gdp_lag1 = ln(gdp_ppp_{i,t−1})` — логарифм ВВП по ППС с лагом 1 (`gdp_ppp = gdppc_ppp × pop`).

### Метод и спецификация

Двусторонние фиксированные эффекты (TWFE) через OLS с дамми страны и года, ошибки кластеризованы по стране (39 кластеров), функция `twfe` из `_common.py`.

```text
Основная:  ln_pat_res_it = α_i + λ_t + β1·ln(rd_gdp)_{i,t−1} + β2·ln(gdp_ppp)_{i,t−1} + ε_it
Проверка:  ln_pat_res_it = α_i + λ_t + β·ln_rd_ppp_{i,t−1} + ε_it     (прежняя main_lag1)
```

- `ln_pat_res` — логарифм патентных заявок резидентов (зависимая).
- `β1` — на сколько процентов больше патентов связано с интенсивностью R&D, выше на 1 %, при том же ВВП.
- `β2` — связь с размером экономики.
- `α_i` — эффекты страны (постоянные особенности: патентная система, язык, структура экономики).
- `λ_t` — эффекты года (общие шоки и тренды).
- `ε_it` — ошибка.
- Лаг 1: результаты R&D проявляются не сразу; лаги 0/1/2 уже проверены и дают одинаковые коэффициенты.
- **Ключевой момент для интерпретации:** `ln_rd_ppp = ln(rd_gdp) − ln(100) + ln(gdp_ppp)`. Прежняя модель — это частный случай основной с ограничением `β1 = β2`. Раздельная модель снимает это ограничение.
- Взаимодействие «R&D × Китай» остаётся в таблице, но его p-value **не используется**: оно оценено по одной стране (21 наблюдение).

### Implementation

1. Сразу после строки `panel["ln_rd_x_chn"] = ...` вставить:

```python
panel = panel.sort_values(["country_iso3", "year"])
panel["ln_rd_gdp_lag1"] = np.log(panel.groupby("country_iso3")["rd_gdp"].shift(1))
panel["ln_gdp_lag1"] = np.log(panel.groupby("country_iso3")["gdp_ppp"].shift(1))
```

2. Сразу после `specs = []` вставить (основная спецификация идёт первой):

```python
# main: R&D volume is intensity x GDP by construction, so the two parts are estimated separately
d_split = panel.dropna(subset=["ln_pat_res", "ln_rd_gdp_lag1", "ln_gdp_lag1", "ln_rd_ppp_lag1"])
t = twfe(d_split, "ln_pat_res", ["ln_rd_gdp_lag1", "ln_gdp_lag1"])
t["spec"] = "main_split_intensity_gdp"
specs.append(t)
t = twfe(d_split, "ln_pat_res", ["ln_rd_ppp_lag1"])
t["spec"] = "volume_same_sample"
specs.append(t)
```

3. Запустить D03; синхронизировать `.ipynb`.
4. В `data/deep/data_dictionary_deep.csv` заменить строку `rd_ppp` на:
   `rd_ppp,"Оценка объёма R&D = доля R&D в ВВП × ВВП по ППС (не данные OECD)","расчёт: World Bank rd_gdp × gdppc_ppp × pop","USD PPP (постоянные цены)",level,"Прямые данные OECD о GERD есть только по 9 странам; см. DEEP_DEVIATIONS"`.
   В `build_panel.py`, строка 174, заменить первые четыре элемента кортежа на те же тексты (`rd_note` оставить).
5. Строка в `DEEP_DEVIATIONS.md`: `| 2026-09-26 | REV-S2 | H2: основной стала раздельная модель (ln доли R&D и ln ВВП); прежняя модель с объёмом R&D — проверка; исправлено описание rd_ppp | Объём R&D сконструирован как доля × ВВП, поэтому прежний коэффициент смешивал R&D и размер экономики. Выбор сделан ПОСЛЕ расчётов | Связь с интенсивностью R&D слабая (p≈0,09); значительная часть прежней связи — рост экономики |`.

### Expected output

В `D03_all_specs.csv` — две новые спецификации (`main_split_intensity_gdp` — 2 строки, `volume_same_sample` — 1 строка); остальные строки без изменений.

### Validation

- **Техническая:** скрипт без ошибок.
- **Данные:** у обеих новых спецификаций N = 734, G = 39; у Китая в выборке 21 наблюдение (`d_split[d_split.country_iso3=="CHN"].shape[0]` — проверить отдельным однострочником).
- **Статистическая:** `ln_rd_gdp_lag1` β ≈ 0,561, p ≈ 0,094; `ln_gdp_lag1` β ≈ 1,752, p ≈ 0,002; `volume_same_sample` β ≈ 0,995, p ≈ 0,002.
- **Неизменность:** `compare_with_head.py results/deep/tables/D03_all_specs.csv` — ровно 3 строки `right_only` (новые), 0 строк `left_only`. `D03_vif.csv` без изменений.
- **Экономическая:** β2 > β1 и значим. Это осмысленно: крупные и растущие экономики патентуют больше. β1 > 0 со слабой значимостью: интенсивность R&D внутри страны меняется медленно (около 29 % вариации приходится на изменения внутри стран).
- **Воспроизводимость:** второй запуск не меняет CSV.

### Acceptance criteria

Новые спецификации совпадают с ожиданием; старые идентичны; словарь исправлен; строка в журнале есть.

### Failure conditions

N ≠ 734 или коэффициенты вне допуска → **DP-any**. Спецификацию (например, «добавить контроль») не менять.

### Interpretation

Условная связь (conditional association), **не причинный эффект**. Формулировка: «патенты растут вместе с объёмом R&D; значительная часть этой связи — общий рост экономики; связь с интенсивностью R&D положительная, но статистически слабая (p≈0,09)». Про Китай — только описательно: «наклон у Китая по его собственному ряду круче (≈1,5 против ≈0,7 у остальных); надёжно оценить эту разницу по одной стране нельзя».

### Limitations

Обратная связь (патенты → R&D) не исключена; лаг её не решает, потому что R&D инерционен. Патенты — заявки по месту подачи, а не по происхождению; ряд заканчивается в 2021 году.

### Rollback

`git restore notebooks/deep/D03_knowledge_production.* results/deep data/deep/data_dictionary_deep.csv scripts/deep/build_panel.py DEEP_DEVIATIONS.md`.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking. Depends on: S1. Blocks: S3.

### Commit

`git commit -m "feat(H2): add split specification (R&D intensity + GDP) as main; fix rd_ppp description"` (добавлять файлы поимённо). Тег: `impl-s2-ok`. **Next Stage:** S3.

---

## Stage 3 — Небольшие эконометрические исправления: Хаусман, Солоу в п. п., имена в H7

**Приоритет:** Core. **Объём:** небольшой, 3 скрипта. **Риск:** низкий. Три независимые подзадачи в разных файлах выполняются одним исполнителем последовательно, одним коммитом на подзадачу.

**Depends on:** S2. **Blocks:** S4, S7.

**Нельзя изменять:** все остальные таблицы D01, D05, D08, кроме перечисленных ниже.

### 3A. Тест Хаусмана (D01)

**Goal.** Заменить некорректный тест (FE с эффектами года против RE без них, кластеризованные ошибки) классическим тестом на одинаковых моделях.

**Исследовательская задача.** Фон к H3: показать, что выбор FE обсуждался. Выбор FE обосновывается содержательно, а не тестом.

**Спецификация.** Выборка D01: строки панели с непустыми `dln_tfp` и `rd_gdp_lag1`.

```text
FE: dln_tfp_it = α_i + β·rd_gdp_{i,t−1} + Σ_s δ_s·1[year=s] + ε_it   (α_i — фиксированные)
RE: то же, α_i — случайные
H = (β_FE − β_RE)² / (Var(β_FE) − Var(β_RE)),  H ~ χ²(1)
```

Ошибки классические (не робастные), иначе классическая формула теста неверна. `dln_tfp` — рост TFP в % (100 × Δln rtfpna), `rd_gdp_lag1` — доля R&D в ВВП с лагом.

**Implementation.** В `notebooks/deep/D01_baseline.py` заменить весь блок от `# Hausman FE vs RE on dln_tfp ~ rd_gdp_lag1` до `save_table(haus, "D01_hausman")` включительно на:

```python
# Classical Hausman: FE and RE with the same year dummies, non-robust covariance, 1 df
from scipy import stats

pdf = panel.set_index(["country_iso3", "year"])
exog = pdf[["rd_gdp_lag1"]].copy()
exog["const"] = 1.0
yr = pd.get_dummies(pdf.index.get_level_values("year"), prefix="y", drop_first=True, dtype=float)
yr.index = pdf.index
exog = pd.concat([exog, yr], axis=1)
y = pdf["dln_tfp"]
fe = PanelOLS(y, exog, entity_effects=True).fit()
re = RandomEffects(y, exog).fit()
b_fe, b_re = float(fe.params["rd_gdp_lag1"]), float(re.params["rd_gdp_lag1"])
v_fe, v_re = float(fe.cov.loc["rd_gdp_lag1", "rd_gdp_lag1"]), float(re.cov.loc["rd_gdp_lag1", "rd_gdp_lag1"])
diff_v = v_fe - v_re
hausman_stat = (b_fe - b_re) ** 2 / diff_v if diff_v > 0 else np.nan
haus = pd.DataFrame([{
    "beta_fe": b_fe, "beta_re": b_re, "var_fe": v_fe, "var_re": v_re,
    "hausman_stat": hausman_stat,
    "p_value": float(1 - stats.chi2.cdf(hausman_stat, 1)) if np.isfinite(hausman_stat) else np.nan,
    "note": "classical Hausman, year dummies in both FE and RE, non-robust cov; FE chosen on substantive grounds, not by this test",
}])
save_table(haus, "D01_hausman")
```

**Validation.** `D01_hausman.csv`: `beta_fe` ≈ −0,050, `beta_re` ≈ −0,022, `p_value` > 0,1 (ожидается ≈ 0,88). `D01_ladder.csv` и `D01_m1_replication.csv` идентичны (`compare_with_head.py`). Экономически: оба коэффициента около нуля и незначимы, тест не отвергает RE. Это не довод за RE: FE выбирается потому, что постоянные особенности стран правдоподобно связаны с R&D.

**Interpretation.** «Тест Хаусмана не отвергает модель со случайными эффектами (p≈0,88); фиксированные эффекты выбраны по содержательной причине».

**Journal:** `| 2026-09-26 | REV-S3 | Тест Хаусмана пересчитан на одинаковых моделях (эффекты года в FE и RE, классические ошибки) | Прежний тест сравнивал разные модели | Вывод не меняется: тест не используется для выбора модели |`.

**Commit:** `fix(D01): like-for-like classical Hausman test`.

### 3B. Солоу в процентных пунктах (D05)

**Goal.** Добавить в таблицу вклады в п. п. в год. Доли TFP при росте около нуля неустойчивы.

**Исследовательская задача.** Подвопрос C: за счёт чего рос ВВП США и Китая.

**Спецификация (не меняется):**

```text
g_Y = α·g_K + (1 − α)·(g_L + g_h) + g_A,   α = 1 − (labsh_t + labsh_{t−1})/2
```

`g_Y, g_K, g_L, g_h` — лог-разности `rgdpna`, `rnna`, `emp`, `hc` (PWT); `g_A` — остаток (TFP). Среднее по периодам 2001–07, 2008–12, 2013–19, 2020–23. Это учётное тождество, а не модель причинности.

**Implementation.** В `notebooks/deep/D05_growth_accounting.py` сразу после `dec = pd.DataFrame(rows)` вставить:

```python
for c in ["g_Y", "contrib_K", "contrib_Lh", "g_A"]:
    dec[f"{c}_pp"] = dec[c] * 100
dec["capital_share_of_growth"] = dec["contrib_K"] / dec["g_Y"]
```

**Validation.** `D05_decomposition.csv`: CHN `g_A_pp` = 4,79 (2001–07), 2,93, 2,05, 1,36 (2020–23); CHN `contrib_K_pp` от 3,23 до 5,43; USA `contrib_K_pp` от 0,53 до 1,05; USA `g_A_pp` от 0,17 до 0,95. Старые столбцы идентичны (`compare_with_head.py` на общих столбцах — все строки `both`). `D05_tfp_share.csv` и `D05_tfp_check.csv` без изменений. Экономически: у Китая рост в основном за счёт капитала, вклад TFP снижается; у США вклады меньше и стабильнее.

**Journal:** `| 2026-09-26 | REV-S3 | Солоу: добавлены вклады в п.п. | Доли TFP неустойчивы при росте около нуля | Основное сравнение H4 — в п.п.; вердикт H4 не меняется |`.

**Commit:** `feat(H4): add growth contributions in percentage points`.

### 3C. Имена организаций в проверке H7 (D08)

**Goal.** Сохранить в таблице, какие три китайские организации исключаются в проверке устойчивости.

**Спецификация (не меняется).** LPM: `open_m = β·is_chn_m + year FE + domain FE + org_type FE + u_m`, модели Epoch 2015–2025, только USA_only и CHN_only, ошибки кластеризованы по организации.

**Implementation.** В `notebooks/deep/D08_ai_open_closed.py` перед `save_table(out, "D08_lpm")` вставить:

```python
out["note"] = ""
out.loc[out.spec == "drop_top3_cn_open", "note"] = "dropped: " + ", ".join(top_cn)
```

**Validation.** В `note` есть Alibaba, DeepSeek, Baidu (точные названия — как в данных Epoch). `LPM_main` β ≈ 0,25, p ≈ 0,009; `drop_top3_cn_open` β ≈ 0,11, p ≈ 0,22. Числовые столбцы `D08_lpm.csv` и `D08_descriptives.csv` без изменений.

**Commit:** `chore(H7): record names of dropped Chinese organizations`.

### Общее для Stage 3

- **Acceptance:** все три подзадачи прошли проверки; `.ipynb` синхронизированы; две строки в журнале.
- **Failure:** любое число вне допуска → **DP-any**. Если `PanelOLS` выдаёт ошибку коллинеарности — остановиться и показать ошибку, спецификацию не менять.
- **Rollback:** по подзадаче — `git restore` соответствующего скрипта и таблиц.
- **Subagents:** 1 Stage Implementer — Claude Sonnet 5, High Thinking. Depends on: S2. Blocks: S4, S5.
- **Тег:** `impl-s3-ok`. **Next:** запустить S4 (ревьюер) и параллельно начать S5.

---

## Stage 4 — Независимая проверка эконометрики (только чтение)

**Приоритет:** Critical gate. **Объём:** средний, только чтение. **Выполняется параллельно с S5 → S6.**

**Goal.** Независимо убедиться, что S1–S3 реализуют ровно утверждённые спецификации, выборки не изменились, интерпретация в журнале не содержит причинных утверждений.

**Depends on:** S3 (тег `impl-s3-ok`). **Can run in parallel with:** S5, S6. **Blocks:** S7.

**Входы:** этот план (Stage 1–3), `AGENT_HANDOFF.md`, код на теге `impl-s3-ok` (`git show impl-s3-ok:<путь>`), таблицы D01–D05 и D08, новые строки `DEEP_DEVIATIONS.md`.

**Что проверить:**

1. Код D02, D03, D01, D05, D08 соответствует формулам из Stage 1–3: зависимые переменные, регрессоры, лаги, эффекты страны и года, кластеризация, выборки.
2. **Независимо переоценить в памяти** (свой код, без записи в `results/`): H2 split — через `linearmodels.PanelOLS(entity_effects=True, time_effects=True)` с кластеризацией по стране; H1 with_pop и without_pop для `rd_gdp`; Хаусман. Коэффициенты должны совпасть до 1e-6, стандартные ошибки — в пределах 10 % (у `linearmodels` и `statsmodels` разные поправки на малую выборку).
3. N и G совпадают с планом; у Китая в H2 21 наблюдение.
4. Строки журнала S1–S3 не утверждают причинность и честно помечают, что выбор H2 сделан после расчётов.
5. Нет ли пропущенной ошибки (например, сдвиг лага без сортировки, утечка будущих значений).

**Constraints.** Не менять файлы проекта и не запускать ноутбуки проекта (они пишут в `results/`). Можно писать только в `_impl_tmp/review_s4/` и в отчёт.

**Output.** Файл `reviews/S4_ECONOMETRICS_REVIEW.md`, его коммитит оркестратор. Содержание: по каждому пункту — «соответствует / не соответствует», доказательство (числа, строки кода), серьёзность, рекомендация. Итог: PASS / PASS WITH NOTES / FAIL.

**Validation ревьюера.** Каждое утверждение подкреплено числом или строкой кода.

**Stop conditions / DP-4.** При FAIL оркестратор не переходит к S7 и выносит вопрос Даниилу в формате DECISION REQUIRED. Исправление после решения — отдельным коммитом вперёд (S5/S6 не откатывать).

**Subagents.**
1. **Econometrics Reviewer** — Claude Opus 5.5, High. Почему Opus: нужно самостоятельно оценить корректность эконометрического дизайна; Sonnet здесь не подходит.

**Commit (оркестратор):** `docs: add independent econometrics review for stages 1-3`. Тег: `impl-s4-ok` (ставится, когда ревью PASS или замечания закрыты).

---

## Stage 5 — TOP500: объединение столбцов и единиц мощности (H6)

**Приоритет:** Critical (график и таблица сейчас неверны). **Объём:** небольшой, 1 скрипт. **Риск:** низкий.

**Goal.** Мощность Rmax в TOP500 записана в разных столбцах и единицах: до 2015 года в GFlop/s (столбцы `RMax`, `Rmax`), с 2019 года в TFlop/s (`Rmax [TFlop/s]`). Объединить в один ряд в TFlop/s, пересчитать доли и таблицу эксафлопсных систем.

**Исследовательская задача.** Подвопрос D: позиции США и Китая в вычислительных мощностях.

**Depends on:** S3 (порядок работы в дереве). **Can run in parallel with:** S4. **Blocks:** S6 (порядок), S7.

**Файлы:** `notebooks/deep/D07_top500.py`, `data/raw/deep/top500/top500_all.csv` (только чтение; списки 2010, 2011, 2013, 2014, 2015, 2019, 2022, 2024, 2025).

**Можно изменять:** `notebooks/deep/D07_top500.py` и `.ipynb`, `DEEP_DEVIATIONS.md`.

**Переменные:** `rmax` — мощность системы в TFlop/s (единый ряд).

**Метод:** описательные доли: `share_systems = n_systems / n_tot`, `share_rmax = rmax_sum / rmax_tot` по году и стране. Эксафлопсная система — `rmax ≥ 1 000 000` TFlop/s (1 EFlop/s).

### Implementation

1. Удалить строку `rmax_col = [c for c in df.columns if "Rmax" in c][0]`.
2. Заменить блок от `df["rmax"] = pd.to_numeric(df[rmax_col], errors="coerce")` до `df["rmax"] = df["rmax"] / 1000.0` (включая проверку `med_2020`) на:

```python
gf = pd.to_numeric(df["RMax"], errors="coerce").fillna(pd.to_numeric(df["Rmax"], errors="coerce"))
tf = pd.to_numeric(df["Rmax [TFlop/s]"], errors="coerce")
# lists 2010-2015 report Rmax in GFlop/s, lists 2019+ in TFlop/s
df["rmax"] = tf.fillna(gf / 1000.0)
```

3. После строки `exa = df[df.rmax >= 1_000_000][...]` добавить `exa = exa.rename(columns={"rmax": "rmax_tflops"})`.
4. В подписи линии заменить `label=f"{c} Rmax"` на `label=f"{c} мощность (Rmax)"`.
5. Запустить D07; синхронизировать `.ipynb`.
6. Строка журнала: `| 2026-09-26 | REV-S5 | TOP500: объединены столбцы Rmax, GFlop/s переведены в TFlop/s | Код брал первый столбец с «Rmax» (пустой в 2010 и с 2019); единицы различались | Доли по мощности пересчитаны; таблица эксафлопсных систем исправлена; H6 → «согласуется частично» |`.

### Validation

- **Данные:** `rmax` не пустой в ≥ 99 % строк каждого года; `rmax_sum > 0` во всех 9 годах; сумма `share_systems` по году = 1.
- **Статистическая** (CHN `share_rmax`): 2010 — 0,130; 2011 — 0,142; 2013 — 0,194; 2014 — 0,169; 2015 — 0,212; 2019 — 0,323; 2022 — 0,106; 2024 — 0,027; 2025 — 0,014. USA `share_rmax` 2024 — 0,553.
- **Эксафлопсные системы:** ровно 8 строк — Frontier (2022); El Capitan, Frontier, Aurora (2024); El Capitan, Frontier, Aurora, JUPITER Booster (2025). Строк раньше 2022 года нет.
- **Неизменность:** `D07_new_entries.csv`, `D07_architecture_top50.csv`, `D07_segments.csv` идентичны (не зависят от Rmax). Столбцы `n_systems` и `share_systems` в `D07_shares.csv` идентичны.
- **Экономическая:** у США доля по мощности выше доли по числу систем (верхушка сосредоточена в США). У Китая после 2019 года доля по мощности ниже доли по числу систем (много систем средней мощности, новые крупные машины в список не подаются). В 2010–2014 годах у Китая были Tianhe-1A и Tianhe-2, поэтому доля по мощности была выше.

### Acceptance / Failure

Все проверки пройдены → принять. Любая доля вне допуска или эксафлопсные системы до 2022 года → остановиться (**DP-any**).

### Interpretation / Limitations

Описательно. TOP500 — добровольная подача; нет списков 2012, 2016–2018, 2020–2021, 2023, поэтому пик доли Китая мог прийтись на 2016–2018 годы. TOP500 не охватывает облачные и коммерческие вычисления для ИИ.

### Rollback

`git restore notebooks/deep/D07_top500.* results/deep DEEP_DEVIATIONS.md`.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking. Parallel with: S4 (ревьюер). Blocks: S6.

### Commit

`fix(H6): harmonise TOP500 Rmax columns and units; rebuild exascale table`. Тег: `impl-s5-ok`. **Next:** S6.

---

## Stage 6 — Comtrade: США и Бельгия, подписи партнёров, реимпорт (H5)

**Приоритет:** Critical. **Объём:** средний, 2 скрипта + сырые данные, **нужна сеть**. **Риск:** средний (лимиты API, пересмотр данных).

**Goal.** Исправить коды стран в загрузчике, перекачать Comtrade, чтобы в данных появились США и Бельгия. Исправить график источников импорта Китая (убрать строку «Мир», подписать код 156 как реимпорт) и назвать RCA «относительно выборки».

**Исследовательская задача.** Подвопрос D: позиции США и Китая в торговле микросхемами и оборудованием.

**Depends on:** S5 (порядок в дереве). **Can run in parallel with:** S4. **Blocks:** S7.

**Файлы:** `scripts/deep/download_comtrade.py`, `notebooks/deep/D06_semiconductors.py`, `data/raw/deep/comtrade/*`.

**Можно изменять:** эти файлы, соответствующий `.ipynb`, `data/raw/deep/comtrade/*` (перезапись загрузчиком), `DEEP_DEVIATIONS.md`.

**Данные:** UN Comtrade public preview API; HS8542 (микросхемы, экспорт и импорт), HS8486 (оборудование), TOTAL (общий экспорт); 2010–2023; партнёры Китая; «зеркало» Тайваня (импорт других стран из партнёра 490).

**Переменные:** `sample_ic_share` (вместо `world_ic_share`) — доля микросхем в общем экспорте **выборки**; `rca = ic_share / sample_ic_share`; новые `total_m`, `reimport_156`, `reimport_share`.

**Метод:** описательная статистика торговли. RCA = доля HS8542 в экспорте страны / доля HS8542 в экспорте выборки (OECD + Китай), а не мира.

### Implementation

**6.1. Загрузчик.** В `load_reporters()` первой строкой тела цикла `for x in rows:` вставить:

```python
        if x.get("entryExpiredDate"):
            continue
```

Перед `return mapping` вставить:

```python
    assert mapping.get("USA") == 842 and mapping.get("BEL") == 56, (mapping.get("USA"), mapping.get("BEL"))
```

**6.2. Перекачка.** `python scripts/deep/download_comtrade.py --force` (3–10 минут). Если в выводе много `FAIL` или ошибка лимита — подождать 1 час и повторить **один раз**. Если снова не получилось — `git restore data/raw/deep/comtrade/` и **DP-6a**.

**6.3. Сравнение со старыми данными.** Создать `_impl_tmp/check_comtrade.py`:

```python
import io, subprocess
import pandas as pd

path = "data/raw/deep/comtrade/comtrade_world_flows.csv"
old = pd.read_csv(io.StringIO(subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True, check=True).stdout.decode("utf-8")))
new = pd.read_csv(path)
print("new reporters:", sorted(set(new.reporter_code) - set(old.reporter_code)))
print("reporters total:", new.reporter_code.nunique())
k = ["reporter_code", "year", "flow", "cmd"]
m = old.groupby(k).value_usd.sum().to_frame("old").join(new.groupby(k).value_usd.sum().to_frame("new"), how="inner")
m["rel"] = (m.new / m.old - 1).abs()
print("rows compared", len(m), "rows >1%:", int((m.rel > 0.01).sum()), "max rel", float(m.rel.max()))
chn = new[(new.country_iso3 == "CHN") & (new.year == 2023) & (new.cmd.astype(str) == "8542")]
print(chn[["flow", "value_usd"]])
print("dups:", int(new.duplicated(k + ["partner_code"]).sum()))
```

**6.4. D06.**
1. Заменить `world_ic_share` на `sample_ic_share` (3 места). Комментарий над блоком: `# RCA relative to the sample (OECD + China), not to world trade`.
2. После строки `src = chn_p[(chn_p.cmd.astype(str) == "8542") & (chn_p.year == 2023)].copy()` вставить:

```python
total_m_2023 = float(src.loc[src.partner_code == 0, "value_usd"].sum())
reimport_2023 = float(src.loc[src.partner_code == 156, "value_usd"].sum())
save_table(pd.DataFrame([{"year": 2023, "total_m": total_m_2023, "reimport_156": reimport_2023,
                          "reimport_share": reimport_2023 / total_m_2023}]), "D06_china_reimport_2023")
src = src[src.partner_code != 0]
```

3. Заменить словарь `PARTNERS`:

```python
PARTNERS = {
    490: "Тайвань", 410: "Корея", 392: "Япония", 842: "США", 458: "Малайзия",
    704: "Вьетнам", 344: "Гонконг", 702: "Сингапур", 156: "Китай (реимпорт)",
    608: "Филиппины", 764: "Таиланд", 372: "Ирландия", 276: "Германия",
    360: "Индонезия", 528: "Нидерланды", 699: "Индия", 484: "Мексика", 376: "Израиль",
}
```

4. Заголовок графика источников: `"Импорт Китаем HS8542 по партнёрам, 2023, без строки «Мир» ($ млрд)"`.
5. Запустить D06; синхронизировать `.ipynb`.

**6.5. Журнал:** `| 2026-09-26 | REV-S6 | Comtrade: исправлены коды США (842) и Бельгии (56), данные перекачаны; убрана строка «Мир» на графике; код 156 подписан как реимпорт; RCA назван «относительно выборки» | Загрузчик брал устаревшие коды 841 и 58 | В H5 есть США; RCA пересчитан на 39 странах; расхождения у старых стран: <N строк >1%> |`.

### Validation

- **Данные:** новые коды `[56, 842]`; всего 39 отчитывающихся стран; дубликатов 0; CHN 2023 HS8542: импорт ≈ 350,1 млрд, экспорт ≈ 136,3 млрд (±2 %).
- **Пересмотр данных:** число строк с расхождением больше 1 % у старых стран. Если таких строк больше 5 % от сравнённых → **DP-6b**.
- **D06:** в `D06_china_ic_sources_2023.csv` нет `partner_code` 0 и нет «голых» чисел в `partner`. Если число есть — найти название в `https://comtradeapi.un.org/files/v1/app/reference/partnerAreas.json`, добавить в `PARTNERS`, перезапустить. `reimport_share` ≈ 0,13 (0,12–0,14). В `D06_equipment_trade.csv` и `D06_ic_trade_panel.csv` есть `USA` и `BEL`. У Китая `ic_net < 0` во всех 14 годах.
- **Экономическая:** экспорт США по HS8486 в 2023 году — не меньше 1 млрд $ и в пятёрке выборки (Applied Materials, Lam, KLA). Если меньше 1 млрд $ — подозрение на ошибку данных, остановиться (**DP-any**). RCA Китая остаётся больше 1; у Кореи — самый высокий в выборке.
- **Воспроизводимость:** повторный запуск D06 (без перекачки) не меняет CSV.

### Acceptance

США и Бельгия в данных; график и таблица партнёров исправлены; реимпорт посчитан; журнал обновлён; записаны для S7: место США по HS8486 в 2023 году, сумма, RCA Китая за 2010 и 2023 годы.

### Failure conditions and DECISION REQUIRED

- **DP-6a (докачка не удалась).**
  - Варианты: (1) повторить позже; (2) скачать CSV вручную на сайте comtradeplus.un.org и положить в тот же формат; (3) запасной вариант — оставить старые данные и убрать утверждения о США в H5 и лестнице утверждений.
  - Последствия: (1) задержка; (2) ручной шаг, который плохо воспроизводится; (3) сравнение США и Китая в полупроводниках станет односторонним.
  - Рекомендация: (3) после двух неудачных попыток. Правила для этого случая уже заложены в Stage 7.
- **DP-6b (пересмотр данных у старых стран).**
  - Варианты: (1) принять новую версию данных для всех стран; (2) оставить старые данные для 37 стран и дописать только США и Бельгию.
  - Последствия: (1) числа по старым странам немного изменятся, но все данные будут одной версии; (2) смешение версий данных.
  - Рекомендация: (1).

### Interpretation / Limitations

Торговля ≠ производство; реимпорт (код 156) указывает на переработку и сборку. RCA — относительно выборки: в ней нет Тайваня, Сингапура, Малайзии, Филиппин, Вьетнама, Гонконга.

### Rollback

`git restore scripts/deep/download_comtrade.py data/raw/deep/comtrade notebooks/deep/D06_semiconductors.* results/deep DEEP_DEVIATIONS.md`.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking. Задача включает сетевую загрузку и проверку данных (роль Data Audit встроена: объём небольшой, отдельный агент не нужен). Parallel with: S4. Blocks: S7.

### Commit

`fix(H5): use current Comtrade reporter codes (USA 842, BEL 56), re-download; fix partner labels, add reimport share`. Тег: `impl-s6-ok`. **Next:** S7 (только после `impl-s4-ok`).

---

## Stage 7 — Сводные таблицы D10/D11: вердикты, рассчитанные кодом

**Приоритет:** Core. **Объём:** средний, 2 скрипта. **Риск:** средний (много строк с числами).

**Goal.** Вердикты и числа в `D11_hypothesis_verdicts.csv` и `D11_claim_ladder.csv` вычисляются **кодом** из пересчитанных таблиц по правилам, заданным заранее. Так исключаются ручные опечатки и подгонка.

**Исследовательская задача.** Все подвопросы: единый источник вердиктов для текста.

**Depends on:** S4 (PASS) и S6. **Blocks:** S8.

**Можно изменять:** `notebooks/deep/D10_robustness_summary.py`, `notebooks/deep/D11_synthesis.py`, их `.ipynb`.

**Нельзя изменять:** поля `prediction` в D11 (скопировать существующие строки дословно); столбцы `H`, `type`.

### Implementation 7.1 — D10

В начало файла добавить `import numpy as np`. После блока `# H2` вставить:

```python
for term in ["ln_rd_gdp_lag1", "ln_gdp_lag1"]:
    r = sp[(sp.spec == "main_split_intensity_gdp") & (sp.term == term)]
    if len(r):
        detail.append({"claim": "H2", "metric": f"split_{term}", "value": float(r.beta.iloc[0]), "p": float(r.p.iloc[0])})
```

После блока `# H3` вставить:

```python
b3_all = rb[rb.term.isin(["rd_gap", "rdstock_gap"])]
detail.append({"claim": "H3", "metric": "n_specs_beta3_negative", "value": int((b3_all.beta < 0).sum()), "p": np.nan})
detail.append({"claim": "H3", "metric": "n_specs_total", "value": int(len(b3_all)), "p": np.nan})
b5 = rb[(rb.spec == "five_year") & (rb.term == "rd_gap")]
if len(b5):
    detail.append({"claim": "H3", "metric": "beta3_five_year", "value": float(b5.beta.iloc[0]), "p": float(b5.p.iloc[0])})
```

### Implementation 7.2 — D11

Переписать построение `claims` и `ladder` так, чтобы числа и вердикты брались из таблиц. Использовать ровно эти правила (они заданы до получения новых чисел):

```python
import numpy as np

def tbl(name):
    return pd.read_csv(T / f"{name}.csv")

def coef(df, spec, term):
    r = df[(df.spec == spec) & (df.term == term)]
    if r.empty:
        raise KeyError(f"{spec}/{term}")
    return float(r.beta.iloc[0]), float(r.p.iloc[0])

# H1
v = tbl("D02_profile_variants_2019_2023")
def dev(c, ind, var):
    return 100 * float(v[(v.country_iso3 == c) & (v.indicator == ind) & (v.variant == var)].pct_above.iloc[0])
chn_main = v[(v.country_iso3 == "CHN") & v.variant.isin(["with_pop", "without_pop"])]
chn_all_above = bool((chn_main.pct_above > 0).all())
usa_flip = np.sign(dev("USA", "rd_gdp", "with_pop")) != np.sign(dev("USA", "rd_gdp", "without_pop"))
h1_verdict = "смешанно; вывод о США зависит от спецификации нормы" if usa_flip else "смешанно"
h1_result = (f"CHN выше нормы по {'всем шести' if chn_all_above else 'не всем'} показателям в обоих вариантах нормы "
             f"(rd_gdp: {dev('CHN','rd_gdp','with_pop'):+.0f}% с населением, {dev('CHN','rd_gdp','without_pop'):+.0f}% без населения). "
             f"USA rd_gdp: {dev('USA','rd_gdp','with_pop'):+.0f}% с населением, {dev('USA','rd_gdp','without_pop'):+.0f}% без населения. "
             "Норма для CHN по населению — экстраполяция (D02_support_check).")

# H2
sp = tbl("D03_all_specs")
b_vol, p_vol = coef(sp, "main_lag1", "ln_rd_ppp_lag1")
b_int, p_int = coef(sp, "main_split_intensity_gdp", "ln_rd_gdp_lag1")
b_gdp, p_gdp = coef(sp, "main_split_intensity_gdp", "ln_gdp_lag1")
b_nochn, _ = coef(sp, "no_chn", "ln_rd_ppp_lag1")
int_clause = "значимая" if p_int < 0.05 else ("слабая (p<0,10)" if p_int < 0.10 else "не выявлена")
h2_verdict = ("согласуется для объёма R&D" if (b_vol > 0 and p_vol < 0.05) else "неопределённо") + f"; связь с интенсивностью R&D {int_clause}"
h2_result = (f"Раздельная модель (основная): интенсивность R&D β={b_int:.2f}, p={p_int:.3f}; ВВП β={b_gdp:.2f}, p={p_gdp:.3f}. "
             f"Объём R&D (доля×ВВП, прежняя основная): β={b_vol:.2f}, p={p_vol:.3f}; без CHN β={b_nochn:.2f}. "
             "Значительная часть связи — общий рост экономики. Взаимодействие с CHN оценено по одной стране; p-value не используется.")

# H3
rb = tbl("D04_robustness")
b3 = rb[rb.term.isin(["rd_gap", "rdstock_gap"])]
b_m, p_m = coef(rb, "main", "rd_gap")
b_5, p_5 = coef(rb, "five_year", "rd_gap")
if b_m > 0 and p_m < 0.05:
    h3_verdict = "согласуется"
elif bool((b3.beta < 0).all()):
    h3_verdict = "не согласуется"
else:
    h3_verdict = "неопределённо"
h3_result = (f"β3 < 0 в {int((b3.beta < 0).sum())} из {len(b3)} спецификаций (основная {b_m:.2f}, p={p_m:.3f}); "
             f"в пятилетних средних {b_5:.2f}, p={p_5:.3f}. Коэффициент при gap_c не трактуется как догоняющий рост.")

# H4
dec = tbl("D05_decomposition")
chn4 = dec[dec.country_iso3 == "CHN"].set_index("period")
usa4 = dec[dec.country_iso3 == "USA"].set_index("period")
lower = chn4.tfp_share < usa4.tfp_share
h4_verdict = "согласуется" if lower.all() else ("не согласуется" if not lower.any() else "частично не согласуется")
h4_result = (f"Вклады, п.п. в год: TFP CHN {chn4.loc['2001-2007','g_A_pp']:.1f} (2001–07) → {chn4.loc['2020-2023','g_A_pp']:.1f} (2020–23); "
             f"капитал CHN {chn4.contrib_K_pp.min():.1f}–{chn4.contrib_K_pp.max():.1f}; "
             f"USA: капитал {usa4.contrib_K_pp.min():.1f}–{usa4.contrib_K_pp.max():.1f}, TFP {usa4.g_A_pp.min():.1f}–{usa4.g_A_pp.max():.1f}. "
             "Доли TFP неустойчивы при росте около нуля; основное сравнение — в п.п.")

# H5
ic = tbl("D06_ic_trade_panel"); eqt = tbl("D06_equipment_trade")
reimp = tbl("D06_china_reimport_2023"); src = tbl("D06_china_ic_sources_2023")
chn_ic = ic[ic.country_iso3 == "CHN"]
net_all = bool((chn_ic.ic_net < 0).all())
e23 = eqt[eqt.year == 2023].sort_values("value_usd", ascending=False).reset_index(drop=True)
has_usa = "USA" in set(eqt.country_iso3)
usa_rank = int(e23.index[e23.country_iso3 == "USA"][0]) + 1 if has_usa else None
usa_eq_bn = float(e23.loc[usa_rank - 1, "value_usd"]) / 1e9 if has_usa else None
if not has_usa:
    h5_verdict = "согласуется частично; часть про США не проверена (нет данных Comtrade по США)"
elif net_all and set(e23.country_iso3.head(3)) == {"USA", "NLD", "JPN"}:
    h5_verdict = "согласуется (торговля)"
elif net_all:
    h5_verdict = "согласуется частично (торговля)"
else:
    h5_verdict = "не согласуется"
tw_kr = float(src[src.partner_code.isin([490, 410])].value_usd.sum()) / float(reimp.total_m.iloc[0])
h5_result = (f"CHN — чистый импортёр микросхем в {int((chn_ic.ic_net < 0).sum())} из {len(chn_ic)} лет; "
             f"реимпорт (код 156) — {100 * float(reimp.reimport_share.iloc[0]):.0f}% импорта 2023; Тайвань+Корея — {100 * tw_kr:.0f}%. "
             + (f"США — {usa_rank}-е место по экспорту HS8486 в 2023 ({usa_eq_bn:.1f} млрд $). " if has_usa else "")
             + "RCA рассчитан относительно выборки OECD+Китай, не мира.")

# H6
sh = tbl("D07_shares")
c6 = sh[sh.iso == "CHN"].sort_values("list_year").reset_index(drop=True)
viol = [int(y) for y in c6[c6.share_rmax >= c6.share_systems].list_year]
peak_i = int(c6.share_systems.idxmax())
rise_fall = c6.share_systems.iloc[0] < c6.share_systems.iloc[peak_i] > c6.share_systems.iloc[-1]
h6_verdict = ("согласуется" if not viol else "согласуется частично") if rise_fall else "не согласуется"
h6_result = (f"Доля CHN по числу систем: {c6.share_systems.iloc[0]:.2f} ({int(c6.list_year.iloc[0])}) → "
             f"{c6.share_systems.iloc[peak_i]:.2f} ({int(c6.list_year.iloc[peak_i])}) → {c6.share_systems.iloc[-1]:.2f} ({int(c6.list_year.iloc[-1])}). "
             f"Доля по мощности не ниже доли по числу систем в годы: {viol if viol else 'нет'}. "
             "Нет списков 2012, 2016–2018, 2020–2021, 2023; подача систем добровольная.")

# H7
lpm = tbl("D08_lpm")
b7, p7 = coef(lpm, "LPM_main", "is_chn")
b7d, p7d = coef(lpm, "drop_top3_cn_open", "is_chn")
names = str(lpm.loc[lpm.spec == "drop_top3_cn_open", "note"].iloc[0]).replace("dropped: ", "")
h7_verdict = ("согласуется" if (b7 > 0 and p7 < 0.05) else "неопределённо") + (", но результат хрупкий" if p7d >= 0.05 else "")
h7_result = (f"LPM: {100 * b7:+.0f} п.п. (p={p7:.3f}); без трёх организаций ({names}) {100 * b7d:+.0f} п.п. (p={p7d:.3f}). "
             "Сильных выводов не делаем.")
```

Затем собрать `claims` из прежних полей `H`, `prediction`, `type` (дословно) и новых `result`, `verdict`. Evidence:
- H1: `D02_profile_variants_2019_2023.csv; D02_support_check.csv`;
- H2: `D03_all_specs.csv`;
- H3: `D04_robustness.csv; D10_key_numbers.csv`;
- H4: `D05_decomposition.csv`;
- H5: `D06_ic_trade_panel.csv; D06_equipment_trade.csv; D06_china_reimport_2023.csv`;
- H6: `D07_shares.csv; D07_exascale_table.csv`;
- H7: `D08_lpm.csv`.

В `ladder` заменить три ячейки USA (остальное дословно):

```python
exa = tbl("D07_exascale_table").drop_duplicates("Name")
usa_rmax24 = 100 * float(sh[(sh.iso == "USA") & (sh.list_year == 2024)].share_rmax.iloc[0])
lvl3_usa = (f"экспорт оборудования HS8486: {usa_eq_bn:.1f} млрд $ (2023), {usa_rank}-е место в выборке"
            if has_usa else "не измерено: нет данных Comtrade по США")
lvl4_usa = f"TOP500: доля мощности {usa_rmax24:.0f}% (2024); эксафлопсных систем в данных: {len(exa)}, из них в США: {int((exa.iso == 'USA').sum())}"
lvl7_usa = "торговля микросхемами и оборудованием (Comtrade 2010–2023)" if has_usa else "не измерено"
```

Запустить D10, затем D11; синхронизировать оба `.ipynb`.

### Validation

- **Техническая:** оба скрипта без ошибок; `KeyError` из `coef` означает, что спецификации нет, — остановиться.
- **Содержательная (ожидаемые вердикты):**
  - H1 — «смешанно; вывод о США зависит от спецификации нормы»;
  - H2 — «согласуется для объёма R&D; связь с интенсивностью R&D слабая (p<0,10)»;
  - H3 — «не согласуется», «β3 < 0 в 7 из 7»;
  - H4 — «частично не согласуется»;
  - H5 — зависит от данных S6 (записать фактический вердикт);
  - H6 — «согласуется частично», годы нарушений [2010, 2013, 2014];
  - H7 — «согласуется, но результат хрупкий».
- **Числа в строках** совпадают с таблицами S1–S6 (сверить 3–4 числа вручную).
- **Неизменность:** поля `prediction` идентичны прежним (`compare_with_head.py` по столбцам `H`, `prediction` → все `both`).
- **Экономическая:** в `result` нет слов «доказано», «вызвал», «эффект R&D на»; вердикты не противоречат числам.

### Acceptance / Failure

Вердикты совпадают с ожидаемыми (H5 — по правилу) → принять. Если вердикт, рассчитанный кодом, отличается от ожидаемого (кроме H5) → **DP-any**: правило не менять, показать числа.

### Interpretation / Limitations

Вердикты — описательные или ассоциативные. «Согласуется» не значит «доказано».

### Rollback

`git restore notebooks/deep/D10_robustness_summary.* notebooks/deep/D11_synthesis.* results/deep`.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking. Depends on: S4 PASS, S6. Blocks: S8.

### Commit

`feat(synthesis): compute D10/D11 verdicts and claim ladder from result tables`. Тег: `impl-s7-ok`. **Next:** S8.

---

## Stage 8 — Тексты: подвопросы, результаты, макросвязь, ограничения

**Приоритет:** Core. **Объём:** средний–большой, 2 документа. **Риск:** расхождение текста и таблиц; причинные формулировки.

**Goal.** Привести `DEEP_RQ_AND_HYPOTHESES.md` и `DEEP_RESULTS.md` в соответствие с решениями и новыми результатами. **Единственный источник чисел** — `D11_hypothesis_verdicts.csv`, `D11_claim_ladder.csv` и таблицы, на которые они ссылаются.

**Depends on:** S7. **Blocks:** S8b, S9.

**Можно изменять:** `DEEP_RQ_AND_HYPOTHESES.md` (только статус и новый раздел подвопросов), `DEEP_RESULTS.md` (полная переработка по шаблону), `DEEP_DEVIATIONS.md`.

**Нельзя изменять:** таблицы H1–H7 в `DEEP_RQ_AND_HYPOTHESES.md`; раздел «Ожидания Даниила»; любые CSV и код.

### Implementation 8.1 — `DEEP_RQ_AND_HYPOTHESES.md`

1. Строку `**Статус:** preregistered / design-locked до запуска S6–S12` заменить на:
   `**Статус:** гипотезы сформулированы в плане до расчётов; их направления совпадают с более ранним документом вариантов (коммит 6aa0f64). Проверить по истории Git, что расчёты не запускались до фиксации гипотез, нельзя: план, гипотезы и результаты попали в один коммит (f3e7383). Поэтому слова «предварительная регистрация» не используем.`
2. Сразу после абзаца главного вопроса (перед `## H1`) вставить:

```markdown
### Как отвечаем на главный вопрос: пять измеримых подвопросов

Главный вопрос — рамка работы. Выводы делаются только по подвопросам:

- **A (H1).** По каким показателям науки, R&D и производства США и Китай отклоняются от типичного уровня для стран с сопоставимым доходом (и размером)?
- **B (H2, H3).** Как в среднем по 39 странам R&D связан с патентами и с ростом производительности (TFP)?
- **C (H4).** За счёт чего рос ВВП США и Китая в 2001–2023 годах: капитал, труд и образование или производительность?
- **D (H5, H6).** Какие позиции у США и Китая в торговле микросхемами и оборудованием и в суперкомпьютерах (TOP500)?
- **E (H7, квант).** Чем различаются подходы США и Китая к моделям ИИ (число, вычисления, открытость) и что о кванте можно сказать только качественно?

Звенья «финансирование», «коммерциализация» и «внедрение» количественно не измеряются.
```

### Implementation 8.2 — `DEEP_RESULTS.md` (структура строго такая)

1. Заголовок и шапка (ветка, дата 2026-09-26, панель, язык выводов). Баннер «идёт пересмотр» **удалить**.
2. `## Ответ на главный вопрос по подвопросам` — по 2–4 предложения на A, B, C, D, E; числа — из D11. Обязательные формулировки:
   - A: «вывод о США зависит от того, учитывается ли размер страны»;
   - B: «H3 — честный отрицательный результат: теория предсказывала более сильную связь R&D с ростом у отстающих стран, в данных знак обратный»; «связь в H2 во многом отражает размер экономики»;
   - C: вклады в п. п.;
   - D: реимпорт, место США по оборудованию (или «не проверено»), доли TOP500 с оговоркой о добровольной подаче;
   - E: открытость «держится на трёх крупнейших лабораториях; результат хрупкий».
   Закончить фразой «Победитель не объявляется».
3. `## Вердикты по гипотезам` — таблица `| H | Подвопрос | Вердикт | Ключевое число | Источник |`. Вердикт и число — дословно из `D11_hypothesis_verdicts.csv`.
4. `## Связь с макроэкономикой: что утверждаем и что нет` — взять блок-цитату из раздела 5.2 файла `REVIEW_OF_METHODOLOGY_AUDIT.md` (начинается словами «Мы не утверждаем…»), числа обновить по `D05_decomposition.csv`. Под ней — таблица звеньев из того же раздела 5.2.
5. `## Обнаружено после расчётов (не входило в гипотезы)` — 4 пункта: снижение вклада TFP Китая в п. п.; зависимость вывода H1 о США от учёта населения; связь H2 во многом отражает размер экономики; доля реимпорта в импорте микросхем Китая.
6. `## Выбор модели` — одна фраза про тест Хаусмана (p из `D01_hausman.csv`) и содержательное обоснование FE.
7. `## Главные таблицы и графики` — прежний список плюс `D02_profile_with_vs_without_pop.png`, `D06_china_reimport_2023.csv`, `D07_exascale_table.csv`.
8. `## Ограничения (обязательно)` — прежние 6 пунктов плюс:
   - RCA относительно выборки OECD + Китай, не мира;
   - TOP500: добровольная подача, пик доли Китая мог прийтись на 2016–2018 годы;
   - взаимодействие «R&D × Китай» в H2 оценено по одной стране;
   - норма H1 для Китая — прогноз за пределами выборки по населению;
   - выбор основной спецификации H2 сделан после расчётов (см. `DEEP_DEVIATIONS.md`).
9. Ссылка на `DEEP_DEVIATIONS.md`.

### Implementation 8.3 — журнал

`| 2026-09-26 | REV-S8 | Тексты: подвопросы A–E, статус гипотез без «preregistered», новые вердикты, раздел о макросвязи, находки после расчётов, ограничения | Решения по REVIEW_OF_METHODOLOGY_AUDIT.md | Выводы сформулированы скромнее и соответствуют данным |`.

### Validation

- Каждое число в `DEEP_RESULTS.md` находится в указанном источнике (проверить **все** числа в разделах 2–6).
- Поиск по `DEEP_RESULTS.md` и `DEEP_RQ_AND_HYPOTHESES.md`: нет `preregistered`, `доказано`, `подтверждено`, `вызвал`, `эффект R&D на`, `not significant across`; число `0.995` / `0,995` встречается только как «прежняя основная».
- Таблицы H1–H7 и раздел «Ожидания Даниила» в `DEEP_RQ_AND_HYPOTHESES.md` идентичны версии на теге `impl-s0-ok` (`git diff impl-s0-ok -- DEEP_RQ_AND_HYPOTHESES.md` показывает только статус и новый раздел).
- Для каждого подвопроса A–E есть хотя бы один результат и хотя бы одно ограничение.

### Acceptance / Failure

Все проверки пройдены → принять. Если текст требует числа, которого нет в таблицах, **не считать его вручную**: остановиться и сообщить.

### Rollback

`git restore DEEP_RESULTS.md DEEP_RQ_AND_HYPOTHESES.md DEEP_DEVIATIONS.md`.

### Subagents

1. **Stage Implementer (тексты)** — Claude Sonnet 5, High Thinking. High, а не Medium: текст содержит интерпретацию, и нужна аккуратность с причинными формулировками. После этапа оркестратор (Opus) сам сверяет каждый вердикт с D11.

### Commit

`docs: rewrite results by sub-questions A-E, update verdicts, macro-link wording and limitations`. Тег: `impl-s8-ok`. **Next:** DP-8b → S8b или S9.

---

## Stage 8b — Необязательная доработка (только по решению DP-8b)

**Приоритет:** Optional. **Объём:** небольшой.

**DECISION REQUIRED (DP-8b):** выполнять ли пункты ниже. Рекомендация: пункт 1 — да (дёшево и полезно на защите), пункты 2–3 — только при наличии времени.

1. Абзац в `DEEP_RESULTS.md` о том, почему у Китая RCA > 1 при чистом импорте: переработка, сборка, реимпорт (число — из `D06_china_reimport_2023.csv`).
2. Доля вариации внутри стран (within-R²) в таблицах H2 и H3. Метод: `1 − SSR(полная модель) / SSR(модель только с эффектами страны и года)`; ожидается ≈ 0,28 для H2 volume и ≈ 0,036 для H3. Добавить столбец `within_r2` в D03 и D04 без изменения остальных столбцов.
3. В тексте H7 на первом месте — доли открытых моделей по годам из `D08_descriptives.csv`, регрессия — вторым.

Каждый пункт — отдельный коммит; после этапа обязательно повторить S9. **Subagent:** Stage Implementer — Claude Sonnet 5, High Thinking. Тег: `impl-s8b-ok`.

---

## Stage 9 — Интеграция и проверка согласованности

**Приоритет:** Critical. **Объём:** средний. **Depends on:** S8 (и S8b, если выполнялся). **Blocks:** S10.

**Goal.** Проверить, что проект согласован целиком: данные, код, модели, результаты, текст, вопрос исследования, ограничения.

### Implementation и Validation

1. **Код, с нуля:** запустить D00–D11 по порядку. Все без ошибок.
2. **Детерминизм:** после запуска `git status --porcelain results/deep/tables` пуст (результаты совпадают с закоммиченными).
3. **Данные:** панель 936 × 57 без дубликатов; Comtrade — 39 отчитывающихся стран; TOP500 — 9 списков; Epoch без изменений (`git diff impl-s0-base --stat -- data/raw/deep/epoch data/raw/deep/top500 data/deep/panel_oecd_chn.csv` пуст).
4. **Модели:** D02, D03, D04, D01 читают одну панель; `D04_*.csv` идентичны исходным (`git diff impl-s0-base --stat -- results/deep/tables/D04_*` пуст). Если выполнялся пункт 8b(2), допустим только новый столбец `within_r2`: проверить `compare_with_head.py <файл> impl-s0-base` по общим столбцам.
5. **Результаты:** каждый файл, упомянутый в `DEEP_RESULTS.md`, существует; вердикты в `DEEP_RESULTS.md` дословно совпадают с `D11_hypothesis_verdicts.csv`.
6. **Текст:** выводы не сильнее вердиктов; нет причинных слов; H3 в основном тексте.
7. **Вопрос исследования:** каждый подвопрос A–E покрыт результатом и ограничением; главный вопрос назван рамкой.
8. **Ограничения:** в `DEEP_RESULTS.md` есть все 11 пунктов ограничений (6 прежних + 5 новых).
9. **Журнал:** в `DEEP_DEVIATIONS.md` есть строки REV-S1, S2, S3 (две), S5, S6, S8.
10. **Git:** `git log impl-s0-base..HEAD --oneline` — по одному логическому коммиту на подзадачу; нет коммитов с `_review_tmp/`, `_impl_tmp/`, `_audit_research_notes.md`.

Отчёт — файл `reviews/S9_INTEGRATION_REPORT.md` с галочками по 10 пунктам и найденными расхождениями.

### Acceptance / Failure

Все 10 пунктов выполнены. При расхождении — определить этап-источник, вернуться к нему (правило из `AGENT_HANDOFF.md`, раздел «Проблема в чужом этапе»), затем повторить S9 целиком.

### Subagents

1. **Stage Implementer** — Claude Sonnet 5, High Thinking: пункты 1–5, 8–10.
2. **Оркестратор** (Claude Opus 5.5, High) сам проверяет пункты 6–7: это оценка соответствия текста и вопроса, её нельзя делегировать исполнителю.

### Commit

`docs: add integration consistency report`. Тег: `impl-s9-ok`. **Next:** S10.

---

## Stage 10 — Финальный независимый методологический аудит

**Приоритет:** Critical. **Режим:** только чтение. **Depends on:** S9. **Blocks:** — (дальше решает Даниил).

**Goal.** Агент, который **не участвовал** в реализации, проверяет результат без доверия к нему.

**Handoff аудитору:**
- **Role:** независимый методолог-эконометрист.
- **Context:** учебный магистерский проект; цель — защищаемая, а не максимально сложная аналитика.
- **Input:** репозиторий на теге `impl-s9-ok`; `REVIEW_OF_METHODOLOGY_AUDIT.md`; `IMPLEMENTATION_PLAN.md`, Часть 0 (решения); `reviews/S4_ECONOMETRICS_REVIEW.md`; `reviews/S9_INTEGRATION_REPORT.md`.
- **Task:**
  1. Код соответствует спецификациям плана.
  2. Данные корректны: Comtrade с США, единицы TOP500, панель.
  3. Модели: переоценить H2 split, H1 variants, H3 main независимо.
  4. Интерпретация не сильнее данных, нет причинных утверждений.
  5. Воспроизводимость: запуск в отдельном клоне или worktree, результаты совпадают.
  6. Анализ отвечает на подвопросы A–E.
  7. Решения Части 0 соблюдены; отклонённые методы не появились.
- **Constraints:** не менять файлы проекта; писать только `POST_IMPLEMENTATION_AUDIT.md`.
- **Output:** `POST_IMPLEMENTATION_AUDIT.md` — замечания с категориями «критично / существенно / мелочь», доказательствами и рекомендацией. Итог: ACCEPT / ACCEPT WITH FIXES / REJECT.
- **Stop conditions:** если нужно решение по методологии — описать варианты, не решать.

**Subagent:** Final Methodology Auditor — Claude Opus 5.5, High. Новый агент, без доступа к переписке исполнителей.

**Commit (оркестратор):** `docs: add post-implementation methodological audit`. Дальше Даниил решает, какие замечания исправлять.

---

# Часть 4. Проверка плана перед передачей

- **Понятно без догадок?** Да: у каждого этапа есть файлы, код, формулы, ожидаемые числа.
- **Результат проверяем?** Да: числовые ожидания с допусками и проверки неизменности.
- **Можно безопасно остановиться?** Да: точки DP-* и правило остановки.
- **Можно откатить?** Да: теги `impl-sN-ok`, `git restore` и `git reset --hard` на последний принятый тег.
- **Скрытые предположения?** Сведены к явным: коды Comtrade, единицы TOP500, выборка D03 (N = 734) и D01 проверены до написания плана.
- **Лишняя сложность?** Нет: новых методов нет. Два агента-ревьюера и один исполнитель на этап.
- **Соответствует данным?** Да: все ожидаемые числа получены диагностикой на текущих данных (`_review_tmp/*_output.txt`).
- **Каждая модель защищаема?** Да: TWFE с кластеризацией для H2 и H3, описательная норма H1, учётное тождество Солоу, LPM — всё с явной оговоркой об условной связи.
- **Соответствует вопросу?** Да: подвопросы A–E покрывают все гипотезы, главный вопрос — рамка.
- **Реалистично?** Да: этапы S0–S9 — порядка 1–1,5 выходных; S6 может занять дольше из-за API.

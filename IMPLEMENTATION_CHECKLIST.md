# IMPLEMENTATION_CHECKLIST.md

Компактная последовательность для исполнителя. Подробности каждого пункта — в `IMPLEMENTATION_PLAN.md` (раздел с тем же номером Stage). Правила и роли — в `AGENT_HANDOFF.md`.

**Порядок:** S0 → S1 → S2 → S3 → (S4 ∥ S5 → S6) → S7 → S8 → [S8b] → S9 → S10.
**Ветка:** `deep-research`. Коммиты только поимённым `git add <файлы>`. Без `git push`.

Отмечать `[x]` по мере выполнения и коммитить обновлённый чеклист вместе с коммитом этапа.

## Стандартный блок контроля субагента (повторяется в каждом этапе)

```text
[ ] Correct model selected
[ ] Task clearly specified
[ ] Inputs identified
[ ] Scope limited (список разрешённых файлов передан)
[ ] Dependencies checked (предыдущий тег impl-*-ok существует)
[ ] Implementation completed
[ ] Validation completed (5 уровней)
[ ] No out-of-scope changes (git status / git show --stat)
[ ] Main agent reviewed output
[ ] Commit created, tag set by orchestrator
```

## Стандартный checkpoint после этапа

```text
[ ] Код запускается
[ ] Данные корректны
[ ] Результаты получены и совпадают с ожиданиями в допуске
[ ] Предыдущие результаты не сломаны (compare_with_head.py)
[ ] Новые результаты экономически интерпретируемы
[ ] Документация обновлена (строка DEEP_DEVIATIONS.md, если нужна)
[ ] Acceptance criteria выполнены
```

---

## Stage 0 — Подготовка и воспроизводимость [Critical]
Субагент: Claude Sonnet 5, High Thinking (`claude-sonnet-5-thinking-high`)
```text
[x] Блок контроля субагента
[x] git switch deep-research; git status --short (только ожидаемые неотслеживаемые файлы)
[x] git tag impl-s0-base
[x] Проверка импорта пакетов
[x] Создан _impl_tmp/compare_with_head.py
[x] Запущены D00–D11 по порядку без ошибок
[x] git status --porcelain results/deep: CSV не изменились (иначе DP-0, стоп)
[x] PNG: если изменились — запись «PNG недетерминированы» + git restore results/deep/figures (не потребовалось: results/deep не изменился вообще)
[x] Баннер «идёт пересмотр» в начале DEEP_RESULTS.md
[x] Checkpoint
[x] В коммит входят .cursor/agents/{stage-implementer,econometrics-reviewer,final-methodology-auditor}.md
[x] Commit: docs: add implementation plan, audit review; mark DEEP_RESULTS as under revision
[ ] Тег impl-s0-ok (оркестратор)
```

## Stage 1 — H1: варианты нормы [Core]
Субагент: Claude Sonnet 5, High Thinking
```text
[x] Блок контроля субагента
[x] residuals_for с параметром rhs и ln_gdppc2
[x] Блок VARIANTS → D02_profile_variants_2019_2023.csv (48 строк)
[x] График D02_profile_with_vs_without_pop.png
[x] D02_support_check.csv
[x] python D02; jupytext --to ipynb D02
[x] Проверка: rd_gdp USA with_pop ≈ −6 %, without_pop ≈ +41 %; CHN +91 % / +186 %
[x] Проверка: ln_pop CHN ≈ 21,07, max остальных ≈ 18,66
[x] Старые таблицы D02 идентичны (compare_with_head.py ×4)
[x] Строка REV-S1 в DEEP_DEVIATIONS.md
[x] Checkpoint
[x] Commit: feat(H1): add norm variants with/without population and support check
[ ] Тег impl-s1-ok
```

## Stage 2 — H2: раздельная спецификация [Core]
Субагент: Claude Sonnet 5, High Thinking
```text
[x] Блок контроля субагента
[x] Сортировка панели + ln_rd_gdp_lag1, ln_gdp_lag1 в D03
[x] Спецификации main_split_intensity_gdp и volume_same_sample (первыми в specs)
[x] python D03; jupytext
[x] Проверка: β интенсивности ≈ 0,561 (p≈0,094), β ВВП ≈ 1,752 (p≈0,002), N = 734, G = 39, CHN = 21
[x] D03_all_specs: +3 строки, старые идентичны; D03_vif идентичен
[x] Строка rd_ppp в data_dictionary_deep.csv и кортеж в build_panel.py (build_panel НЕ запускать)
[x] Строка REV-S2 (с пометкой «выбор после расчётов»)
[x] Checkpoint
[x] Commit: feat(H2): add split specification (R&D intensity + GDP) as main; fix rd_ppp description
[ ] Тег impl-s2-ok
```

## Stage 3 — Хаусман, Солоу в п. п., имена в H7 [Core]
Субагент: Claude Sonnet 5, High Thinking
```text
[x] Блок контроля субагента
3A [x] Новый блок Хаусмана в D01 → p_value > 0,1 (≈0,88); D01_ladder и D01_m1_replication идентичны
   [x] Строка REV-S3 (Хаусман); Commit: fix(D01): like-for-like classical Hausman test
3B [x] Столбцы *_pp и capital_share_of_growth в D05 → CHN g_A_pp 4,79 → 1,36
   [x] Старые столбцы и D05_tfp_share идентичны; строка REV-S3 (Солоу)
   [x] Commit: feat(H4): add growth contributions in percentage points
3C [x] note с именами в D08_lpm → Alibaba, DeepSeek, Baidu; числа D08 идентичны
   [x] Commit: chore(H7): record names of dropped Chinese organizations
[x] jupytext для D01, D05, D08
[x] Checkpoint
[ ] Тег impl-s3-ok
```

## Stage 4 — Независимая проверка эконометрики [Critical gate, только чтение]
Субагент: Claude Opus 5.5, High (`claude-opus-5-5-high`). Запускается параллельно с S5 → S6.
```text
[ ] Блок контроля субагента (read-only, пишет только отчёт и _impl_tmp/review_s4/)
[ ] Код D01, D02, D03, D05, D08 сверен со спецификациями Stage 1–3
[ ] Независимая переоценка H2 split, H1 rd_gdp, Хаусмана (коэффициенты до 1e-6, SE ±10 %)
[ ] N, G, выборка Китая проверены
[ ] Строки журнала без причинных утверждений; пометка «H2 выбран после расчётов» есть
[ ] reviews/S4_ECONOMETRICS_REVIEW.md: PASS / PASS WITH NOTES / FAIL
[ ] При FAIL → DP-4 (стоп перед S7), исправление коммитом вперёд
[ ] Commit (оркестратор): docs: add independent econometrics review for stages 1-3
[ ] Тег impl-s4-ok
```

## Stage 5 — TOP500 [Critical]
Субагент: Claude Sonnet 5, High Thinking
```text
[ ] Блок контроля субагента
[ ] Объединение RMax/Rmax (GFlop/s ÷ 1000) и Rmax [TFlop/s]; удалены rmax_col и проверка med_2020
[ ] exa → rmax_tflops; подпись графика
[ ] python D07; jupytext
[ ] Проверка: rmax_sum > 0 во всех 9 годах; CHN share_rmax 0,130 / 0,323 (2019) / 0,014 (2025)
[ ] Эксафлопсные: 8 строк, все ≥ 2022 (Frontier, El Capitan, Aurora, JUPITER Booster)
[ ] new_entries, architecture_top50, segments идентичны
[ ] Строка REV-S5
[ ] Checkpoint
[ ] Commit: fix(H6): harmonise TOP500 Rmax columns and units; rebuild exascale table
[ ] Тег impl-s5-ok
```

## Stage 6 — Comtrade: США и Бельгия [Critical, нужна сеть]
Субагент: Claude Sonnet 5, High Thinking
```text
[ ] Блок контроля субагента
[ ] load_reporters: пропуск записей с entryExpiredDate + assert USA=842, BEL=56
[ ] python scripts/deep/download_comtrade.py --force (при неудаче: 1 повтор через час → DP-6a)
[ ] _impl_tmp/check_comtrade.py: новые коды [56, 842]; 39 стран; CHN 2023 M≈350,1 / X≈136,3 млрд
[ ] Расхождения старых стран >1 %: <5 % строк (иначе DP-6b)
[ ] D06: sample_ic_share; D06_china_reimport_2023; убран partner 0; PARTNERS; заголовок
[ ] python D06; jupytext
[ ] Проверка: нет «голых» кодов; reimport_share ≈ 0,13; USA и BEL в таблицах; CHN ic_net < 0 все 14 лет
[ ] Экономика: экспорт HS8486 США 2023 ≥ 1 млрд $ и в топ-5
[ ] Записать для S7: место США, сумма, RCA CHN 2010 и 2023
[ ] Строка REV-S6
[ ] Checkpoint
[ ] Commit: fix(H5): use current Comtrade reporter codes (USA 842, BEL 56), re-download; fix partner labels, add reimport share
[ ] Тег impl-s6-ok
```

## Stage 7 — Вердикты D10/D11 из таблиц [Core]
Субагент: Claude Sonnet 5, High Thinking. Старт только при наличии impl-s4-ok И impl-s6-ok.
```text
[ ] Блок контроля субагента
[ ] D10: import numpy; split_* для H2; n_specs_beta3_negative, n_specs_total, beta3_five_year для H3
[ ] D11: функции tbl/coef; правила H1–H7 ровно по плану; prediction/type дословно
[ ] D11 ladder: уровни 3, 4, 7 для USA из таблиц
[ ] python D10; python D11; jupytext ×2
[ ] Ожидаемые вердикты: H1 смешанно…США; H2 согласуется для объёма…слабая; H3 не согласуется (7 из 7);
    H4 частично не согласуется; H5 по правилу; H6 согласуется частично [2010, 2013, 2014]; H7 согласуется, но хрупкий
[ ] prediction идентичны прежним
[ ] Нет причинных слов в result
[ ] Checkpoint
[ ] Commit: feat(synthesis): compute D10/D11 verdicts and claim ladder from result tables
[ ] Тег impl-s7-ok
```

## Stage 8 — Тексты [Core]
Субагент: Claude Sonnet 5, High Thinking; сверка вердиктов — оркестратор
```text
[ ] Блок контроля субагента
[ ] DEEP_RQ_AND_HYPOTHESES.md: новый статус; раздел «пять измеримых подвопросов»
[ ] Таблицы H1–H7 и «Ожидания Даниила» не изменены (git diff impl-s0-ok)
[ ] DEEP_RESULTS.md по структуре 1–9; баннер удалён
[ ] Все числа сверены с D11 и таблицами-источниками
[ ] Поиск запрещённых слов: preregistered, доказано, подтверждено, вызвал, not significant across
[ ] A–E: у каждого есть результат и ограничение
[ ] 11 пунктов ограничений
[ ] Строка REV-S8
[ ] Checkpoint
[ ] Commit: docs: rewrite results by sub-questions A-E, update verdicts, macro-link wording and limitations
[ ] Тег impl-s8-ok
[ ] DP-8b: спросить Даниила про S8b
```

## Stage 8b — Необязательная доработка [Optional, только после решения DP-8b]
Субагент: Claude Sonnet 5, High Thinking
```text
[ ] Блок контроля субагента
[ ] (1) Абзац про RCA > 1 при чистом импорте — отдельный коммит
[ ] (2) within_r2 в D03/D04 — отдельный коммит (≈0,28 и ≈0,036)
[ ] (3) H7: сначала доли по годам — отдельный коммит
[ ] Тег impl-s8b-ok; затем обязательно S9
```

## Stage 9 — Интеграция [Critical]
Субагент: Claude Sonnet 5, High Thinking (пункты 1–5, 8–10); оркестратор — пункты 6–7
```text
[ ] Блок контроля субагента
[ ] 1 Запуск D00–D11 с нуля без ошибок
[ ] 2 git status --porcelain results/deep/tables пуст
[ ] 3 Панель, TOP500, Epoch не изменились относительно impl-s0-base; Comtrade 39 стран
[ ] 4 D04_* идентичны impl-s0-base (если был 8b(2) — отличается только столбец within_r2)
[ ] 5 Все файлы из DEEP_RESULTS.md существуют; вердикты = D11
[ ] 6 Текст не сильнее вердиктов, нет причинных слов, H3 в основном тексте (оркестратор)
[ ] 7 A–E покрыты; главный вопрос — рамка (оркестратор)
[ ] 8 11 ограничений на месте
[ ] 9 Строки журнала REV-S1, S2, S3×2, S5, S6, S8
[ ] 10 История коммитов чистая; временные файлы не закоммичены
[ ] reviews/S9_INTEGRATION_REPORT.md
[ ] Commit: docs: add integration consistency report
[ ] Тег impl-s9-ok
```

## Stage 10 — Финальный независимый аудит [Critical, только чтение]
Субагент: Claude Opus 5.5, High — новый агент, не участвовавший в реализации
```text
[ ] Блок контроля субагента
[ ] Передан handoff из IMPLEMENTATION_PLAN.md, Stage 10
[ ] Проверены: код, данные, модели, интерпретация, воспроизводимость (отдельный worktree), A–E, решения Части 0
[ ] POST_IMPLEMENTATION_AUDIT.md: ACCEPT / ACCEPT WITH FIXES / REJECT
[ ] Commit (оркестратор): docs: add post-implementation methodological audit
[ ] Передать Даниилу для решения по замечаниям
```

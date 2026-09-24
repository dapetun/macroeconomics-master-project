# Final Changelog — adversarial review project_final.md → final_project.md

Дата: 2026-09-16. Роль: скептический преподаватель макроэкономики. Проверены: RQ, гипотезы, данные, методология, количественные результаты, tech-кейсы, механизмы, conclusion. Формат каждого замечания: severity / claim / problem / why it matters / correction. Исправлены все HIGH и необходимые MEDIUM (отмечены [FIXED]); LOW — зафиксированы, исправлены где дёшево.

> **Superseded as latest adversarial** by `ADVERSARIAL_REVIEW.md` + `REQUIRED_FIXES.md` (2026-09-20). Этот файл = audit trail прохода 2026-09-16, не текущий verdict.

---

## 1. Research question

**[MEDIUM][FIXED] RQ-1. Рамка «2010–2023» без расшифровки фактических окон.**
- claim: «Окно панели: 2010–2023» + «отвечаем … в 2010–2023 (joint-year/common-window)».
- problem: патенты фактически 2010–2021, researchers joint 2022 / common 2010–2017, MVA joint 2021. Читатель ждёт единый 2010–2023 для всех метрик.
- why it matters: несопоставимые данные под единой шапкой; риск обвинения в сокрытии усечений и cherry-picking окна.
- correction: §1.2 переформулирован с явными фактическими окнами; каждая цифра в §5/§8/§10 идёт с годом/(start,end,n). Добавлено обоснование выбора 2010 (пост-кризис + старт hitech-ряда) и оговорка об отсутствии чувствительности к другим рамкам.

**[LOW] RQ-2. Вторая часть RQ («какие звенья нельзя оценить») — мета-вопрос.**
- claim: суженный RQ включает «какие звенья нельзя оценить».
- problem: это вопрос о данных, а не о мире; может читаться как попытка выдать missing за finding.
- why it matters: низкое — честная оговорка, но требует дисциплины «missing ≠ zero».
- correction: сохранено, но усилено правилом `?` и переформулировкой quantum «≈0» → «не измерен» (см. TECH-4).

## 2. Hypotheses

**[MEDIUM][FIXED] H-1. Pooled r=+0.16 без источника.**
- claim: «Pooled BERD–hitech r=+0.16 — композиционный артефакт».
- problem: число из старой pooled-матрицы (DO NOT USE), в quant_reviewed не рекомпутировано; приводится как факт.
- why it matters: unsupported claim; преподаватель спросит «откуда 0.16, N=?».
- correction: помечено «r≈+0.16 из старой pooled-матрицы, DO NOT USE, только пример запрета»; запрещено цитировать как evidence.

**[LOW] H-2. H2-coherence всё ещё упомянута.**
- claim: «Qual-разборка согласуется с ожиданием».
- problem: даже слово «согласуется» может читаться как мягкая поддержка.
- why it matters: низкое — рядом стоит «не evidence».
- correction: оставлено с «coherence с дизайном, не evidence»; вердикт insufficient без изменений.

## 3. Data quality

**[HIGH][FIXED] D-1. Ratio HS8542 3.13x смешивает HS-ревизии.**
- claim: «$43.6 vs $136.4 млрд, 3.13x» с caveat только про CAGR.
- problem: endpoints 2010 (H3) vs 2023 (H6) — разные покрытия HS; ratio не like-for-like, но подаётся как level-gap.
- why it matters: несопоставимые данные; технологический catch-up из номинального ratio с ревизиями — запрещённая подмена №11.
- correction: во все упоминания добавлено «H6 vs H3, не like-for-like; только номинальные стоимости»; CAGR вынесен в «приведён чтобы запретить чтение».

**[MEDIUM][FIXED] D-2. Bare incomparable CAGR («2.6% vs 6.8%», «0.4% vs 8.9%») цитируются даже для запрета.**
- claim: старые пары приводятся в кавычках «несопоставимы, не использовать».
- problem: само нарушение правила «только common-window с (start,end,n)»: голые числа без окон приглашают к цитированию.
- why it matters: cherry-picking-риск; студент унесёт числа без caveat.
- correction: голые пары удалены («не приводятся»); оставлены только common-window с (start,end,n).

## 4. Methodology

**[HIGH][FIXED] M-1. Slope p-values как тесты (p=0.29 / p<0.001 / p=0.02 / p=0.01).**
- claim: §5.2 даёт diff p-values для slopes без источника и SE-метода.
- problem: slopes — OLS по тренду с AR(1) 0.32–0.90; SE наивные, cluster/HAC нет; источник (trend_slopes_convergence, pooled/unbalanced?) не указан.
- why it matters: causal-adjacent overconfidence; та же ошибка, что M1-HC1, но без дисклеймера; преподаватель разберёт первым.
- correction: добавлен общий дисклеймер «slopes — OLS-дескрипция, SE/p наивные, AR(1) игнорируется, только ориентир»; все p помечены naive; cluster/HAC — в future work.

**[MEDIUM][FIXED] M-2. «USA потребляет dummy и 12 строк».**
- claim: USA-константа «потребляет dummy и 12 строк».
- problem: строки USA участвуют в оценке year-FE и θ; «потребляет» вводит в заблуждение, будто строки выброшены.
- why it matters: методологическая неточность; занижает/искажает понимание FE-идентификации.
- correction: «0 within-вариации TFP, вклад — только year-FE/θ; drop-USA обязательна».

**[LOW][FIXED] M-3. K=20 без расшифровки; within-r двусмысленность.**
- claim: «K=20», «within ≈+0.03/+0.24».
- problem: K непроверяем; два within-r без указания выборок выглядят противоречием.
- why it matters: воспроизводимость.
- correction: K=20 (=2+6 country-FE при G=7+12 year-FE); within +0.03 full-panel vs +0.24 M1-subsample lagged — разные выборки.

## 5. Quantitative results

**[HIGH][FIXED] Q-1. Thesis смешивает joint-годы в одном предложении без годов.**
- claim: §10 п.1: «GERD 0.75, BERD 0.75, researchers ~0.38 vs статьи 2.17, патенты 5.44/2.68, MVA ~2.5x, IC 3.13x».
- problem: годы 2023/2022/2021 смешаны без меток — несопоставимые снапшоты как «профиль».
- why it matters: cherry-picking-обвинение; запрет NaN-ratio обойдён смешением лет.
- correction: каждый пункт §10/§8 теперь с годом (GERD 2023, researchers joint-2022, патенты/MVA joint-2021, IC 2023 H6/H3).

**[LOW][FIXED] Q-2. GDPpc slopes vs endpoints; TFP «+1.4%/год».**
- claim: «+$1099 vs +$933, разрыв вырос $49k→$52k»; «TFP +0.0063/год (+1.4%/год)».
- problem: slope (OLS-наклон) vs endpoint-diff — разные метрики; сумма наклонов не равна diff endpoints из-за округления/OLS; «+1.4%» не помечен как CAGR vs slope.
- why it matters: арифметический допрос на защите.
- correction: помечено «OLS-slopes — другая метрика, не противоречие endpoints»; TFP slope — дескрипция с наивным SE.

## 6. Technology cases

**[HIGH][FIXED] TECH-1. `+`/`~` для [expert assessment] (нарушение собственного правила).**
- claim: таблица §6.2: «Chip design USA сильнее [expert assessment]», «EDA сильнее», «Equipment…» с grade `+`.
- problem: преамбула: `+` — только по evidence; qual-строки evidence не имеют. Capability выдана за graded advantage.
- why it matters: technology capability ≠ economic advantage; центральный пункт скепсиса; собственное противоречие.
- correction: все qual-строки переведены на `?/H? [expert assessment, гипотеза]`; `+`/`~` только для измеренных MVA/IC/hitech; легенда переписана.

**[HIGH][FIXED] TECH-2. MVA/IC как evidence bottleneck.**
- claim: §6.1C: bottleneck США с parenthetical «(MVA-доля 10.5% vs 25.0%)»; §6.2 использует доли/стоимости в fab-строках.
- problem: MVA — macro-доля, IC — номинал с assembly-смещением; trade≠fab, share≠scale — собственные запреты нарушены parenthetical-подпоркой.
- why it matters: macro→tech leap; преподаватель: «как доля GDP доказывает packaging-bottleneck?».
- correction: parenthetical удалён; везде «MVA/IC — не evidence bottleneck, см. только §5.1»; fab-строки — `?`.

**[MEDIUM][FIXED] TECH-3. KOR IC CAGR как fab-контекст в foundry-строке.**
- claim: «TWN, KOR доминируют…; KOR IC CAGR +6.5% vs JPN −0.9% — лишь trade-контекст».
- problem: trade-CAGR в строке про foundry-доли приглашает читать trade как мощность — запрещённая подмена.
- why it matters: capability≠advantage; trade≠fab.
- correction: CAGR удалён из строки; оставлено «панелью не измерено; trade-контекст только в §5».

**[MEDIUM][FIXED] TECH-4. Quantum «макроэффект ≈0 по построению».**
- claim: «экономика ≈0 по построению ранней стадии (qual-констатация)».
- problem: absence of evidence → evidence of zero; нефальсифицируемо, ряда нет.
- why it matters: unsupported claim; спросят «где стандартная ошибка нуля?».
- correction: «эффект не измерен; в панели неотличим от отсутствия; “≈0” — допущение, не оценка».

**[LOW][FIXED] TECH-5. «HIGH если собрать» для TOP500-методики.**
- claim: «методика HIGH если собрать».
- problem: спекулятивный confidence для несобранных данных.
- correction: «методика известна, данных нет».

## 7. Economic mechanisms

**[LOW][FIXED] E-1. Заголовок «Upstream-контроль → рента/рычаг» утверждает механизм.**
- claim: bullet-титул содержит «→ рента/рычаг», тело говорит «не заявлен».
- problem: титул сильнее тела; стрелка без оценки.
- why it matters: causal-язык в заголовке уносится в цитаты.
- correction: переименовано в «Гипотеза upstream-контроля…»; статус «не заявлен» сохранён.

**[LOW] E-2. «Есть уровни catch-up» в R&D-буллите.**
- claim: «механизма нет; есть уровни catch-up».
- problem: может читаться как «catch-up есть благодаря R&D».
- why it matters: низкое.
- correction: уточнено «дескриптивный catch-up уровней TFP — не эффект R&D».

## 8. Conclusion + geopolitics

**[HIGH][FIXED] C-1. Геополитика внутри §10 Conclusion + uncited external claim.**
- claim: курсивный абзац в §10: «внешние отраслевые источники указывают на концентрацию…» + decoupling-числа (hitech −3.6 пп, IC +7.2%).
- problem: собственное правило (§9): «геополитика не в executive conclusion»; источник концентрации не цитирован; event n=2 числа в conclusion приглашают к sanction-прочтению даже с «не оценка».
- why it matters: geopolitical overreach; главное место, где вывод сильнее evidence.
- correction: абзац удалён из §10 в Приложение G (вне conclusion); «источники указывают» заменено на «панелью не измерено, не findings»; event-числа только в §6.2.

---

## Что исправлено в final_project.md (карта)

- §1.2, §5.1/§5.2/§8/§10: годы/окна в каждой цифре; обоснование 2010; голые CAGR удалены.
- §2/H3: pooled r помечен DO NOT USE.
- §3: slopes-дисклеймер; K=20 расшифрован; USA-вклад переформулирован; within-r разведён.
- §4.1/§5.1/§6.2/§10: HS-ratio с H3/H6-caveat.
- §6.1–6.4: `?/H?` вместо `+` для qual; MVA/IC-подпорки удалены; KOR-CAGR удалён; quantum переформулирован; TOP500-confidence снят.
- §7: upstream-титул → гипотеза; catch-up уточнён.
- §10→Приложение G: геополитика вынесена, uncited claim удалён.
- Не менялись: числа M1 (`regression_results_final.csv`), значения панели, вердикты H (not tested), запреты подмен.

## Остаточные риски (признаны, не устранимы без новых данных)

1. Slopes/p наивные (нужен HAC/cluster) — см. future work.
2. HS single-definition re-pull, TOP500-pull, AI Index export, quantum IPF CSV — отсутствуют.
3. Панель 7–8 стран, G=7 — cluster-SE ненадёжны по построению.
4. Зрелость без независимого измерителя (H2 circular-риск) — только при условии невывода bottleneck из зрелости.

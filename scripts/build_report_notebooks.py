"""Build report notebooks 01–05 for branch report-20pp."""
from __future__ import annotations

from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
NB_DIR = ROOT / "notebooks"


def md(source: str) -> nbf.NotebookNode:
    return nbf.v4.new_markdown_cell(source.strip() + "\n")


def code(source: str) -> nbf.NotebookNode:
    return nbf.v4.new_code_cell(source.strip() + "\n")


def write_nb(name: str, cells: list[nbf.NotebookNode]) -> Path:
    nb = nbf.v4.new_notebook()
    nb["cells"] = cells
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    path = NB_DIR / name
    nbf.write(nb, path)
    print("wrote", path.relative_to(ROOT))
    return path


# Shared bootstrap used in every notebook
BOOT = r'''
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path("..").resolve()
PANEL_PATH = ROOT / "data_reviewed" / "core_panel_reviewed.csv"
TABLES = ROOT / "data_reviewed" / "tables_reviewed"
RAW = ROOT / "data" / "raw"
OUT_FIG = ROOT / "notebooks" / "figures"
OUT_TAB = ROOT / "notebooks" / "tables"
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_TAB.mkdir(parents=True, exist_ok=True)

panel = pd.read_csv(PANEL_PATH)
panel = panel[(panel["year"] >= 2010) & (panel["year"] <= 2024)].copy()
US_CN = panel[panel["country_iso3"].isin(["USA", "CHN"])].copy()

def cagr(start: float, end: float, n_years: int) -> float:
    """Compound annual growth rate; n_years = end_year - start_year."""
    if start is None or end is None or np.isnan(start) or np.isnan(end) or start <= 0 or n_years <= 0:
        return np.nan
    return (end / start) ** (1 / n_years) - 1

print("panel rows", len(panel), "US+CN rows", len(US_CN))
print("countries", sorted(panel["country_iso3"].unique()))
'''


def build_01() -> None:
    cells = [
        md(
            """
# 01. Данные и две шкалы измерения (методы 1–3)

**Ветка:** `report-20pp`  
**Роль:** теория (блоки A–D) + уровни в общий год, среднегодовой темп, два окна для статей.

**Расшифровки:**
- **GERD** — валовые внутренние расходы на НИОКР (*Gross Domestic Expenditure on R&D*).
- **BERD** — расходы на НИОКР, выполненные бизнесом (*Business Enterprise R&D*, PERFORMED).
- **CAGR** — среднегодовой темп прироста (*compound annual growth rate*).
- **ППС** — паритет покупательной способности.
"""
        ),
        md(
            """
## Теория (кратко, для отчёта)

### A. Зачем сравнивать две шкалы
Национальная статистика науки публикует и **интенсивность** (например, GERD в процентах ВВП), и **объём** (абсолютные расходы, число статей). Это разные знаменатели, а не две «модели развития».

- OECD. *Frascati Manual 2015*.
- OECD/Eurostat. *Oslo Manual 2018*.

### B. Цепочка «наука → внедрение»
Линейная схема удобна как оглавление отчёта. В литературе она давно описана как упрощение: есть обратные связи и обучение на производстве (Kline & Rosenberg, 1986).

### C. Национальные инновационные системы
Страны различаются организацией науки, фирм и государства. Здесь сравниваются **измеримые индикаторы**, а не «какая система лучше» (Freeman, 1987; Lundvall, 1992; Nelson, 1993).

### D. Догоняющее развитие и масштаб
Поздний догоняющий может быстро наращивать **объём** при меньшей **интенсивности** (Abramovitz, 1986; Gerschenkron, 1962; Lee, 2013). Это рамка для чтения: Китай выше по статьям и абсолютному GERD в млн долл. по ППС; США выше по GERD% ВВП и исследователям на миллион жителей.
"""
        ),
        code(BOOT),
        md(
            """
## Метод 1. Уровни в общий год

Для каждого показателя берём последний год, в котором есть значения **и** у США, **и** у Китая (joint year). Рядом с цифрой всегда пишем год.
"""
        ),
        code(
            r'''
dual = pd.read_csv(TABLES / "dual_scale_with_absolutes.csv")
display_cols = [
    "var", "scale_family", "joint_year", "USA", "CHN",
    "CHN_USA_ratio", "gap_sign_level", "cagr_t0", "cagr_t1", "CAGR_USA", "CAGR_CHN", "note",
]
show = dual[display_cols].copy()
show.to_csv(OUT_TAB / "01_dual_scale_with_absolutes.csv", index=False)
show
'''
        ),
        md(
            r"""
## Метод 2. Среднегодовой темп на общем окне (CAGR)

Формула: \(\mathrm{CAGR} = (y_{t_1}/y_{t_0})^{1/(t_1-t_0)} - 1\). Окно \((t_0, t_1)\) пишется явно для каждого ряда.
"""
        ),
        code(
            r'''
cagr_tbl = pd.read_csv(TABLES / "descriptive_cagr_common_window.csv")
cagr_tbl.to_csv(OUT_TAB / "01_cagr_common_window.csv", index=False)
cagr_tbl.head(20)
'''
        ),
        md(
            """
## Метод 3. Два окна для статей и год пересечения

- CAGR статей считается **дважды**: 2010–2021 (пик США) и 2010–2024 (полный актуальный горизонт).
- Пересечение объёма статей: последний год, когда США ≥ Китая — **2016**; первый год, когда Китай > США — **2017**. Формулировка «около 2020» **неверна**.
- Ряд 2014–2024 для США/Китая: **NSF Indicators 2026**, Figure 29 (Scopus, дробный подсчёт). К 2024 Китай ≈2.45× США по объёму.
"""
        ),
        code(
            r'''
arts = US_CN[["country_iso3", "year", "scopus_articles"]].dropna().sort_values(["year", "country_iso3"])
wide = arts.pivot(index="year", columns="country_iso3", values="scopus_articles").dropna()
wide["CHN_gt_USA"] = wide["CHN"] > wide["USA"]
crossover_years = wide.loc[wide["CHN_gt_USA"]].index.min()
last_usa_lead = wide.loc[~wide["CHN_gt_USA"]].index.max()
print("last year USA >= CHN:", int(last_usa_lead))
print("first year CHN > USA:", int(crossover_years))
if 2024 in wide.index:
    print("2024 USA/CHN:", float(wide.loc[2024, "USA"]), float(wide.loc[2024, "CHN"]),
          "ratio", float(wide.loc[2024, "CHN"] / wide.loc[2024, "USA"]))

dual_art = pd.read_csv(TABLES / "articles_cagr_dual_window.csv")
dual_art.to_csv(OUT_TAB / "01_articles_cagr_dual_window.csv", index=False)

fig, ax = plt.subplots(figsize=(8, 4.5))
for iso, color in [("USA", "#1f77b4"), ("CHN", "#d62728")]:
    s = arts[arts["country_iso3"] == iso]
    ax.plot(s["year"], s["scopus_articles"], marker="o", label=iso, color=color)
ax.axvline(2016.5, color="gray", linestyle="--", linewidth=1, label="пересечение 2016→2017")
ax.set_title("S&E статьи (NSF/Scopus): США и Китай, 2010–2024")
ax.set_xlabel("Год")
ax.set_ylabel("Число статей (дробный подсчёт)")
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUT_FIG / "01_articles_crossover.png", dpi=150)
plt.show()
dual_art
'''
        ),
        md(
            """
## Краткий вывод для отчёта (метод 1–3)

По таблице dual-scale при выбранных шкалах: США выше по **интенсивности** (GERD%, BERD%, исследователи на млн), Китай выше по **объёму/доле** (статьи, патенты, MVA%, hitech%, абсолютный GERD PPP, оценка численности исследователей). Это арифметика шкал, а не вердикт «победитель». Пересечение статей — 2016–2017; к 2024 разрыв по объёму статей вырос примерно до 2.45× (NSF 2026).
"""
        ),
    ]
    write_nb("01_data_and_scales.ipynb", cells)


def build_02() -> None:
    cells = [
        md(
            """
# 02. Два тренда и проверка разницы наклонов (методы 4 и 5)

**Метод 4** — две отдельные прямые: для США и для Китая отдельно оценивается  
`y = a + b × год`.

**Метод 5** — одна регрессия на двух странах:  
`y = a + b × год + c × (страна=Китай) + d × (год × (страна=Китай))`.

- `b` — наклон США;
- `b + d` — наклон Китая;
- **`d`** — насколько наклон Китая отличается от наклона США.

Если доверительный интервал для `d` не содержит ноль, разница наклонов в **этой** спецификации статистически отличима от нуля. Это описание двух прямых, а не доказательство, что «политика Китая ускорила науку».

В отчёте считаем два ряда: число статей Scopus и GERD в процентах ВВП.
"""
        ),
        code(BOOT + "\nimport statsmodels.formula.api as smf"),
        code(
            r'''
def fit_separate_slopes(df: pd.DataFrame, ycol: str, year0: int = 2010, year1: int = 2024):
    """Method 4: OLS y ~ year separately for USA and CHN."""
    rows = []
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for iso, color in [("USA", "#1f77b4"), ("CHN", "#d62728")]:
        sub = df[(df["country_iso3"] == iso) & (df["year"] >= year0) & (df["year"] <= year1)][
            ["year", ycol]
        ].dropna()
        sub = sub.rename(columns={ycol: "y"})
        m = smf.ols("y ~ year", data=sub).fit(cov_type="HC1")
        rows.append({
            "series": ycol,
            "country": iso,
            "n": int(m.nobs),
            "intercept": m.params["Intercept"],
            "slope_b": m.params["year"],
            "slope_se": m.bse["year"],
            "slope_p": m.pvalues["year"],
            "r2": m.rsquared,
            "window": f"{year0}-{year1}",
        })
        ax.scatter(sub["year"], sub["y"], color=color, alpha=0.7, label=f"{iso} данные")
        xgrid = np.linspace(sub["year"].min(), sub["year"].max(), 50)
        ax.plot(xgrid, m.params["Intercept"] + m.params["year"] * xgrid, color=color, label=f"{iso} прямая")
    ax.set_title(f"Метод 4: отдельные прямые — {ycol}")
    ax.set_xlabel("Год")
    ax.set_ylabel(ycol)
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_FIG / f"02_method4_{ycol}.png", dpi=150)
    plt.show()
    return pd.DataFrame(rows)


def fit_interaction(df: pd.DataFrame, ycol: str, year0: int = 2010, year1: int = 2024):
    """Method 5: y ~ year + China + year:China."""
    sub = df[(df["country_iso3"].isin(["USA", "CHN"])) & (df["year"] >= year0) & (df["year"] <= year1)][
        ["country_iso3", "year", ycol]
    ].dropna().copy()
    sub = sub.rename(columns={ycol: "y"})
    sub["China"] = (sub["country_iso3"] == "CHN").astype(int)
    m = smf.ols("y ~ year + China + year:China", data=sub).fit(cov_type="HC1")
    d = m.params["year:China"]
    ci_low, ci_high = m.conf_int().loc["year:China"]
    out = pd.DataFrame([{
        "series": ycol,
        "n": int(m.nobs),
        "b_USA_slope": m.params["year"],
        "c_China_level": m.params["China"],
        "d_slope_diff": d,
        "d_se": m.bse["year:China"],
        "d_p": m.pvalues["year:China"],
        "d_ci_low": ci_low,
        "d_ci_high": ci_high,
        "d_excludes_zero": not (ci_low <= 0 <= ci_high),
        "r2": m.rsquared,
        "window": f"{year0}-{year1}",
    }])
    print(m.summary().tables[1])
    return out, m
'''
        ),
        md("## Статьи Scopus"),
        code(
            r'''
sep_art = fit_separate_slopes(US_CN, "scopus_articles", year0=2010, year1=2024)
int_art, _ = fit_interaction(US_CN, "scopus_articles", year0=2010, year1=2024)
sep_art
'''
        ),
        code("int_art"),
        md("## GERD в процентах ВВП"),
        code(
            r'''
sep_gerd = fit_separate_slopes(US_CN, "gerd_pct_gdp", year0=2010, year1=2023)
int_gerd, _ = fit_interaction(US_CN, "gerd_pct_gdp", year0=2010, year1=2023)
sep_gerd
'''
        ),
        code("int_gerd"),
        code(
            r'''
summary = pd.concat([sep_art, sep_gerd], ignore_index=True)
interaction = pd.concat([int_art, int_gerd], ignore_index=True)
summary.to_csv(OUT_TAB / "02_method4_separate_slopes.csv", index=False)
interaction.to_csv(OUT_TAB / "02_method5_interaction.csv", index=False)
interaction
'''
        ),
        md(
            """
## Краткий вывод для отчёта (методы 4–5)

На графике видны две прямые (метод 4). Таблица с `d` (метод 5) показывает, отличима ли разница наклонов. Интерпретация: описание темпов изменения рядов за 2010–2023, без каузального языка.
"""
        ),
    ]
    write_nb("02_trends_two_slopes.ipynb", cells)


def build_03() -> None:
    cells = [
        md(
            """
# 03. Метод главных компонент на шкале интенсивности (метод 9)

**Единственная ML-часть отчёта.**

Берём три ряда **интенсивности** на уровне страна–год:
1. GERD в процентах ВВП;
2. BERD (PERFORMED) в процентах ВВП;
3. исследователи на миллион жителей.

Стандартизируем столбцы, оцениваем метод главных компонент. Первая главная компонента сжимает сонаправленные ряды; смотрим долю объяснённой дисперсии и нагрузки. Это **не** «индекс технологической мощи» и не рейтинг способностей.
"""
        ),
        code(
            BOOT
            + """
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
"""
        ),
        code(
            r'''
cols = ["gerd_pct_gdp", "berd_pct_gdp", "researchers_per_million"]
pca_df = panel[["country_iso3", "year"] + cols].dropna().copy()
print("complete country-year rows:", len(pca_df))
print(pca_df.groupby("country_iso3").size().sort_values(ascending=False))

X = pca_df[cols].to_numpy()
scaler = StandardScaler()
Z = scaler.fit_transform(X)
pca = PCA(n_components=3, random_state=0)
scores = pca.fit_transform(Z)

var = pd.DataFrame({
    "PC": [1, 2, 3],
    "variance_explained": pca.explained_variance_ratio_,
    "variance_explained_pct": 100 * pca.explained_variance_ratio_,
})
loadings = pd.DataFrame(pca.components_.T, index=cols, columns=["PC1", "PC2", "PC3"])
pca_df = pca_df.assign(PC1=scores[:, 0], PC2=scores[:, 1])

var.to_csv(OUT_TAB / "03_pca_variance.csv", index=False)
loadings.to_csv(OUT_TAB / "03_pca_loadings.csv")
pca_df.to_csv(OUT_TAB / "03_pca_scores.csv", index=False)

print("Variance explained:")
print(var.to_string(index=False))
print("Loadings:")
print(loadings.to_string())
var
'''
        ),
        code(
            r'''
# Latest year per country for a simple country scatter on PC1
latest = pca_df.sort_values("year").groupby("country_iso3", as_index=False).tail(1)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(latest["country_iso3"], latest["PC1"], color="#4c72b0")
for _, r in latest.iterrows():
    if r["country_iso3"] in ("USA", "CHN"):
        ax.bar([r["country_iso3"]], [r["PC1"]], color="#d62728" if r["country_iso3"] == "CHN" else "#1f77b4")
ax.axhline(0, color="gray", linewidth=0.8)
ax.set_title("Первая главная компонента интенсивности (последний доступный год по стране)")
ax.set_ylabel("PC1 (стандартизованная шкала)")
ax.set_xlabel("Страна")
ax.grid(True, axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(OUT_FIG / "03_pca_pc1_by_country.png", dpi=150)
plt.show()
latest[["country_iso3", "year", "PC1", "gerd_pct_gdp", "berd_pct_gdp", "researchers_per_million"]]
'''
        ),
        md(
            """
## Краткий вывод для отчёта (метод 9)

Первая компонента объясняет большую долю дисперсии трёх intensity-рядов (ожидаемо порядка ~90%, как в `results/pca_repair_a_intensity_variance.csv`). Нагрузки показывают, что GERD%, BERD% и исследователи на млн движутся в одну сторону. США и Китай различаются по положению на PC1 — это сжатие выбранных шкал интенсивности, не вердикт о «мощи».
"""
        ),
    ]
    write_nb("03_pca.ipynb", cells)


def build_04() -> None:
    cells = [
        md(
            """
# 04. Корреляции внутри страны (метод 12) и приложение M1 (метод 14)

## Метод 12
Для **одной** страны по годам считаем корреляцию Пирсона между двумя рядами. Это ассоциация совместного движения во времени, **не** причинно-следственная связь.

Пары для отчёта:
- GERD% ВВП и число статей;
- исследователи на млн и число статей;
- GERD% ВВП и TFP (`tfp_ctfp`).

## Метод 14 (только приложение)
Панельная регрессия с фиксированными эффектами страны и года (спецификация M1):  
`TFP_{it} = α_i + δ_t + β·GERD_{i,t−1} + θ·log(researchers_per_million)_{it} + ε_{it}`.

Почему не в сюжет: (а) у США в Penn World Table `ctfp = 1` каждый год **по построению**; (б) при кластерных стандартных ошибках доверительный интервал для β_GERD включает ноль. Честная фраза: «в этой спецификации устойчивой связи нет».
"""
        ),
        code(BOOT),
        code(
            r'''
pairs = [
    ("gerd_pct_gdp", "scopus_articles"),
    ("researchers_per_million", "scopus_articles"),
    ("gerd_pct_gdp", "tfp_ctfp"),
]
rows = []
for iso in ["USA", "CHN"]:
    sub = panel[panel["country_iso3"] == iso]
    for x, y in pairs:
        xy = sub[["year", x, y]].dropna()
        n = len(xy)
        corr = xy[x].corr(xy[y]) if n >= 5 else np.nan
        rows.append({
            "country": iso,
            "x": x,
            "y": y,
            "pearson_r": corr,
            "n_years": n,
            "year_min": int(xy["year"].min()) if n else np.nan,
            "year_max": int(xy["year"].max()) if n else np.nan,
        })
corr_tbl = pd.DataFrame(rows)
corr_tbl.to_csv(OUT_TAB / "04_within_country_correlations.csv", index=False)
corr_tbl
'''
        ),
        code(
            r'''
fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=False)
for ax, iso in zip(axes, ["USA", "CHN"]):
    sub = panel[panel["country_iso3"] == iso][["year", "gerd_pct_gdp", "scopus_articles"]].dropna()
    ax.scatter(sub["gerd_pct_gdp"], sub["scopus_articles"], c=sub["year"], cmap="viridis")
    ax.set_title(f"{iso}: GERD% vs статьи")
    ax.set_xlabel("GERD, % ВВП")
    ax.set_ylabel("Статьи Scopus")
    ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUT_FIG / "04_within_corr_gerd_articles.png", dpi=150)
plt.show()
'''
        ),
        md(
            """
## Приложение: M1 (не пересчитываем, читаем канон)

Числа из `regression_results_final.csv` / `M1_INTERPRETATION.md`. Не подбираем лаги ради значимости.
"""
        ),
        code(
            r'''
m1_path = ROOT / "regression_results_final.csv"
m1 = pd.read_csv(m1_path)
# Keep a compact appendix view if columns exist; otherwise show head.
m1.to_csv(OUT_TAB / "04_m1_appendix_source.csv", index=False)
print("M1 source rows:", len(m1))
m1.head(20)
'''
        ),
        md(
            """
### Обязательная оговорка по TFP
В Penn World Table показатель `ctfp` для США равен 1 **каждый год по построению** (Feenstra, Inklaar, Timmer, 2015). Поэтому within-оценка для США по TFP не информативна как «рост производительности США».

### Разрешённый язык
«условная ассоциация», «неотличимо от нуля под cluster SE», «дескриптивно / приложение».  
**Запрещено:** «эффект GERD на TFP», «доказательство конверсии».
"""
        ),
    ]
    write_nb("04_associations.ipynb", cells)


def build_05() -> None:
    cells = [
        md(
            """
# 05. Точечные снимки технологий (метод 18)

Снимки — числа на **конкретную дату / период** из внешнего отчёта. Это не полный ряд 2010–2023 и не тест гипотез H1–H6.

Источники:
- Stanford HAI. *AI Index Report 2025*.
- TOP500 List (ноябрь 2015 и ноябрь 2025).
- EPO–OECD. *Mapping the global quantum ecosystem* (2025).

Подробная сверка: `SNAPSHOT_SOURCE_LEDGER.md`.
"""
        ),
        code(BOOT),
        code(
            r'''
ai = pd.read_csv(RAW / "snapshots" / "ai_index_snapshot.csv")
top = pd.read_csv(RAW / "snapshots" / "top500_snapshot.csv")
quantum = pd.read_csv(RAW / "snapshots" / "quantum_epo_oecd_snapshot.csv")
ai.to_csv(OUT_TAB / "05_ai_index_snapshot.csv", index=False)
top.to_csv(OUT_TAB / "05_top500_snapshot.csv", index=False)
quantum.to_csv(OUT_TAB / "05_quantum_snapshot.csv", index=False)
'''
        ),
        md("## Искусственный интеллект (Stanford AI Index)"),
        code(
            r'''
ai_us_cn = ai[ai["country_iso3"].isin(["USA", "CHN"])].copy()
ai_us_cn
'''
        ),
        code(
            r'''
# Simple grouped bars for selected AI indicators
focus = [
    "ai_publications_share_of_world",
    "ai_citations_share_of_world",
    "ai_private_investment_usd_bn",
    "ai_notable_models_count",
    "ai_patents_share_of_world_grants",
]
plot_df = ai_us_cn[ai_us_cn["indicator"].isin(focus)].copy()
fig, axes = plt.subplots(1, len(focus), figsize=(14, 3.5), sharey=False)
for ax, ind in zip(axes, focus):
    sub = plot_df[plot_df["indicator"] == ind]
    order = ["USA", "CHN"]
    vals = [sub.loc[sub["country_iso3"] == c, "value"].values[0] for c in order]
    ax.bar(order, vals, color=["#1f77b4", "#d62728"])
    ax.set_title(ind.replace("_", "\n"), fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
fig.suptitle("Снимки AI Index: США vs Китай (годы см. таблицу)", y=1.05)
fig.tight_layout()
fig.savefig(OUT_FIG / "05_ai_index_bars.png", dpi=150, bbox_inches="tight")
plt.show()
'''
        ),
        md("## Суперкомпьютеры (TOP500)"),
        code(
            r'''
top_us_cn = top[top["country_iso3"].isin(["USA", "CHN"])].copy()
pivot = top_us_cn.pivot_table(index="list_month", columns="country_iso3", values="value")
print(top_us_cn.to_string(index=False))
fig, ax = plt.subplots(figsize=(6, 4))
pivot[["USA", "CHN"]].plot(kind="bar", ax=ax, color=["#1f77b4", "#d62728"])
ax.set_title("Число систем в TOP500")
ax.set_ylabel("Системы")
ax.set_xlabel("Список")
ax.grid(True, axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(OUT_FIG / "05_top500_counts.png", dpi=150)
plt.show()
top_us_cn
'''
        ),
        md("## Квантовые технологии (EPO–OECD, международные патентные семьи)"),
        code(
            r'''
q = quantum.copy()
q_us_cn = q[q["country_iso3"].isin(["USA", "CHN", "JPN", "WORLD"])]
q_us_cn
'''
        ),
        md(
            """
## Оговорки по полупроводникам и Тайваню (½ страницы максимум)

- Код **HS8542** в торговой статистике — экспорт электронных интегральных схем по таможенной классификации. Это **не** измерение мощности фабрик (fab capacity) и не «лидерство в полупроводниках».
- **Тайвань** в панели страны **нет**. Роль foundry на Тайване — качественная оговорка (`qual`), не расчёт. Франция в панели **не** заменяет Тайвань как foundry.

Матрица заполненности 8 блоков × 4 технологии — справочно, не кульминация: см. `tech_occupancy_matrix.md`.
"""
        ),
        code(
            r'''
occ = pd.read_csv(ROOT / "tech_occupancy_matrix.csv")
occ.to_csv(OUT_TAB / "05_occupancy_matrix.csv", index=False)
occ
'''
        ),
        md(
            """
## Краткий вывод для отчёта (метод 18)

Снимки показывают **разные знаки** по разным индикаторам (например, Китай выше по доле AI-публикаций и патентов; США выше по частным инвестициям в ИИ и по числу notable models; США выше по международным патентным семьям в кванте; число систем TOP500 у США выше в обоих выбранных моментах). Это точечные факты из источников, а не ряд и не объявление победителя.
"""
        ),
    ]
    write_nb("05_tech_snapshots.ipynb", cells)


if __name__ == "__main__":
    NB_DIR.mkdir(parents=True, exist_ok=True)
    build_01()
    build_02()
    build_03()
    build_04()
    build_05()
    print("done")

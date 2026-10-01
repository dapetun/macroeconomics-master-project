"""Вспомогательные функции графиков. / Plotting helpers."""
from __future__ import annotations

from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .labels import FOCUS_SERIES
from .style import COLOR_CHN, COLOR_USA, GRAY


def plot_observed(ax: plt.Axes, years, values, **style) -> None:
    """Линия рвётся при пропуске года. / Break the line when a year is missing."""
    years = np.asarray(list(years), dtype=float)
    values = np.asarray(list(values), dtype=float)
    order = np.argsort(years)
    years, values = years[order], values[order]
    start = 0
    first = True
    for i in range(1, len(years) + 1):
        gap = i < len(years) and (years[i] - years[i - 1]) > 1
        if i == len(years) or gap:
            kw = dict(style)
            if not first:
                kw["label"] = None
            ax.plot(years[start:i], values[start:i], **kw)
            first = False
            start = i


def year_ticks(ax: plt.Axes, years: Iterable, *, rotation: float = 25) -> None:
    """Целые годы на оси X. / Integer year ticks on the x-axis."""
    years = sorted({int(y) for y in years})
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], rotation=rotation, ha="right")


def barh_usa_chn(
    ax: plt.Axes,
    usa: Sequence[float] | pd.Series,
    chn: Sequence[float] | pd.Series,
    labels: Sequence[str],
    *,
    width: float = 0.36,
) -> None:
    """Две горизонтальные полосы США/Китай. / Twin USA/China horizontal bars."""
    ypos = np.arange(len(labels))
    ax.barh(ypos - width / 2, usa, width, label="США", color=COLOR_USA)
    ax.barh(ypos + width / 2, chn, width, label="Китай", color=COLOR_CHN)
    ax.axvline(0, color=GRAY, lw=0.8)
    ax.set_yticks(ypos)
    ax.set_yticklabels(list(labels))


def plot_focus_lines(
    ax: plt.Axes,
    df: pd.DataFrame,
    *,
    x: str,
    y: str,
    group_col: str = "country_iso3",
    series=FOCUS_SERIES,
    scale: float = 1.0,
    **style,
) -> None:
    """Линии по FOCUS_SERIES (США/Китай). / Lines for FOCUS_SERIES (USA/China)."""
    for code, color, lab in series:
        s = df[df[group_col] == code].sort_values(x)
        ax.plot(s[x], s[y] * scale, color=color, label=lab, marker="o", **style)

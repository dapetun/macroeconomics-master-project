"""Общая библиотека анализа OECD+Китай. / Shared OECD+China analysis library.

Эконометрика подгружается лениво: графики не тянут statsmodels.
Econometrics is lazy-loaded so plotting scripts skip statsmodels.
"""
from __future__ import annotations

from typing import Any

from .io import load_panel, save_fig, save_table
from .labels import (
    ARCH_LABEL,
    ARCH_ORDER,
    FOCUS_CGROUP,
    FOCUS_SERIES,
    INDICATOR_LABELS,
    VAR_LABELS_SHORT,
)
from .paths import COUNTRIES, FIGURES, PANEL_PATH, RAW_DEEP, REPORTS, ROOT, TABLES, YEARS
from .plot import barh_usa_chn, plot_focus_lines, plot_observed, year_ticks
from .quantum import load_quantum_snapshot
from .top500 import pick_accel_column
from .style import (
    BLUE,
    BLUE_BRIGHT,
    CMAP_NAVY,
    COLOR_CHN,
    COLOR_OTHER,
    COLOR_USA,
    FIGSIZE,
    FIGSIZE_SQUARE,
    FIGSIZE_TALL,
    GRAY,
    GRAY_MED,
    GRAY_PALE,
    INK,
    NAVY,
    ORANGE,
    ORANGE_MID,
    SERIES,
    apply_hse_style,
    country_color,
    style_axes,
)

__all__ = [
    "ARCH_LABEL",
    "ARCH_ORDER",
    "BLUE",
    "BLUE_BRIGHT",
    "CMAP_NAVY",
    "COLOR_CHN",
    "COLOR_OTHER",
    "COLOR_USA",
    "COUNTRIES",
    "FIGSIZE",
    "FIGSIZE_SQUARE",
    "FIGSIZE_TALL",
    "FIGURES",
    "FOCUS_CGROUP",
    "FOCUS_SERIES",
    "GRAY",
    "GRAY_MED",
    "GRAY_PALE",
    "INDICATOR_LABELS",
    "INK",
    "NAVY",
    "ORANGE",
    "ORANGE_MID",
    "PANEL_PATH",
    "RAW_DEEP",
    "REPORTS",
    "ROOT",
    "SERIES",
    "TABLES",
    "VAR_LABELS_SHORT",
    "YEARS",
    "apply_hse_style",
    "barh_usa_chn",
    "coef_table",
    "country_color",
    "load_panel",
    "load_quantum_snapshot",
    "ols_cluster",
    "pick_accel_column",
    "plot_focus_lines",
    "plot_observed",
    "save_fig",
    "save_table",
    "style_axes",
    "twfe",
    "twfe_betas",
    "within_demean",
    "year_ticks",
]

_LAZY_ECON = frozenset({"twfe", "twfe_betas", "ols_cluster", "coef_table", "within_demean"})


def __getattr__(name: str) -> Any:
    if name in _LAZY_ECON:
        from . import econometrics as _econ

        return getattr(_econ, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

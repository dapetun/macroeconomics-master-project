"""Стиль графиков (брендбук НИУ ВШЭ). / Chart style (HSE brand book)."""
from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Основная: navy/blue/серые; рядом — оранжевая семья. / Core navy/blue/grays; orange accent family.
NAVY = "#0F2D69"
BLUE = "#374B9B"
BLUE_BRIGHT = "#0050CF"
GRAY = "#6B7A99"
GRAY_MED = "#939598"
GRAY_PALE = "#E6E7E8"
ORANGE = "#EB691E"
ORANGE_MID = "#EB8C3C"
INK = "#1C1C1C"

COLOR_USA = NAVY
COLOR_CHN = ORANGE
COLOR_OTHER = GRAY_MED
SERIES = [NAVY, BLUE, BLUE_BRIGHT, ORANGE, ORANGE_MID, GRAY, GRAY_MED]
CMAP_NAVY = LinearSegmentedColormap.from_list("hse_navy", [GRAY_PALE, BLUE, NAVY])

# Ширина ≈ полоса отчёта (~16.5 см). / Width ≈ report text column (~16.5 cm).
FIGSIZE = (6.4, 3.9)
FIGSIZE_TALL = (6.4, 6.2)
FIGSIZE_SQUARE = (6.4, 6.4)


def apply_hse_style() -> None:
    """Кегль рядом с 14 пт текста отчёта. / Type size near 14 pt report text."""
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "font.size": 12,
            "axes.titlesize": 13,
            "axes.labelsize": 12,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
            "legend.fontsize": 11,
            "axes.edgecolor": NAVY,
            "axes.labelcolor": NAVY,
            "axes.titlecolor": NAVY,
            "xtick.color": NAVY,
            "ytick.color": NAVY,
            "text.color": INK,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.linewidth": 0.8,
            "lines.linewidth": 2.2,
            "lines.markersize": 6,
            "legend.frameon": False,
            "axes.grid": False,
            "savefig.dpi": 200,
            "figure.dpi": 120,
            "savefig.bbox": "tight",
        }
    )


def style_axes(ax: plt.Axes, title: str = "", ylabel: str = "", xlabel: str = "") -> None:
    """Подпись к рисунку — в отчёте; title обычно пустой. / Caption lives in the report; title usually empty."""
    if title:
        ax.set_title(title, pad=8)
    else:
        ax.set_title("")
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(NAVY)
    ax.spines["bottom"].set_color(NAVY)
    ax.grid(True, color=GRAY_PALE, linewidth=0.8)
    ax.set_axisbelow(True)


def country_color(iso3: str, *, other: str | None = None) -> str:
    """Цвет страны для столбцов. / Country color for bars."""
    if iso3 == "USA":
        return COLOR_USA
    if iso3 == "CHN":
        return COLOR_CHN
    return other if other is not None else COLOR_OTHER

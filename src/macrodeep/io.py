"""Ввод-вывод панели, таблиц и рисунков. / Panel, table, and figure I/O."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .paths import FIGURES, PANEL_PATH, TABLES


def load_panel(path: Path | None = None) -> pd.DataFrame:
    """Загрузить панель OECD+Китай. / Load the OECD+China panel."""
    df = pd.read_csv(path or PANEL_PATH)
    df["year"] = df["year"].astype(int)
    return df


def save_table(df: pd.DataFrame, name: str) -> Path:
    """Сохранить CSV в results/deep/tables. / Write CSV under results/deep/tables."""
    TABLES.mkdir(parents=True, exist_ok=True)
    out = TABLES / f"{name}.csv"
    df.to_csv(out, index=False)
    return out


def save_fig(
    fig: plt.Figure,
    name: str,
    dpi: int = 200,
    tight_rect: tuple[float, float, float, float] | None = None,
) -> Path:
    """Сохранить PNG; layout один раз. / Save PNG; apply layout once."""
    FIGURES.mkdir(parents=True, exist_ok=True)
    out = FIGURES / f"{name}.png"
    if tight_rect is None:
        fig.tight_layout()
    else:
        fig.tight_layout(rect=tight_rect)
    fig.savefig(out, dpi=dpi, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return out

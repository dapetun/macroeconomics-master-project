"""Хелперы столбцов TOP500. / TOP500 column helpers."""
from __future__ import annotations

from collections.abc import Sequence


def pick_accel_column(columns: Sequence[str]) -> str | None:
    """Предпочесть имя ускорителя, не «… Cores». / Prefer accelerator name over Cores count."""
    cols = list(columns)
    if "Accelerator/Co-Processor" in cols:
        return "Accelerator/Co-Processor"
    named = [c for c in cols if "Accelerator" in c and "Co-Processor" in c and "Cores" not in c]
    return named[0] if named else None

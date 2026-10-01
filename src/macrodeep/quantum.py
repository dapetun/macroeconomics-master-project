"""Quantum EPO–OECD snapshot I/O. / Загрузка quantum snapshot."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .paths import ROOT, TABLES

SNAP_DEFAULT = ROOT / "data" / "raw" / "snapshots" / "quantum_epo_oecd_snapshot.csv"
OUT_NAME = "D09_quantum_snapshot_reuse"


def _existing_reuse_nonempty(reuse_path: Path) -> bool:
    """True if reuse CSV exists and has at least one data row."""
    if not reuse_path.exists():
        return False
    try:
        existing = pd.read_csv(reuse_path)
    except (pd.errors.EmptyDataError, ValueError):
        return False
    return len(existing) > 0


def load_quantum_snapshot(
    path: Path | None = None,
    *,
    reuse_path: Path | None = None,
) -> pd.DataFrame:
    """Загрузить EPO–OECD snapshot; пустой/отсутствующий → ошибка.
    Load EPO–OECD snapshot; missing/empty raises (no silent overwrite).
    """
    snap = path if path is not None else SNAP_DEFAULT
    reuse = reuse_path if reuse_path is not None else (TABLES / f"{OUT_NAME}.csv")

    if not snap.exists():
        raise FileNotFoundError(
            f"Quantum snapshot missing: {snap}. "
            "Restore from git (5f14cd5^:data/raw/snapshots/quantum_epo_oecd_snapshot.csv) "
            "or from results/deep/tables/D09_quantum_snapshot_reuse.csv."
        )
    try:
        df = pd.read_csv(snap)
    except pd.errors.EmptyDataError as exc:
        if _existing_reuse_nonempty(reuse):
            raise ValueError(
                f"Quantum snapshot at {snap} is empty; refuse overwrite of non-empty {reuse}."
            ) from exc
        raise ValueError(f"Quantum snapshot at {snap} is empty.") from exc

    if len(df) == 0:
        if _existing_reuse_nonempty(reuse):
            raise ValueError(
                f"Quantum snapshot at {snap} is empty; refuse overwrite of non-empty {reuse}."
            )
        raise ValueError(f"Quantum snapshot at {snap} is empty.")
    return df

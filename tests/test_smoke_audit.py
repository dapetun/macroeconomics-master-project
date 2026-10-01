"""Минимальные smoke-тесты по замечаниям аудита. / Minimal smoke tests from the audit."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from macrodeep import load_quantum_snapshot, pick_accel_column, twfe, twfe_betas  # noqa: E402


def test_twfe_and_twfe_betas_close_on_tiny_panel():
    rng = np.random.default_rng(0)
    rows = []
    for c, c0 in enumerate(["A", "B", "C", "D"]):
        for y in range(2000, 2010):
            rows.append(
                {
                    "country_iso3": c0,
                    "year": y,
                    "dln_tfp": 0.01 * c + 0.002 * (y - 2000) + 0.1 * rng.normal(),
                    "rd_c": 0.5 * c + 0.05 * rng.normal(),
                    "gap_c": 0.2 * (3 - c) + 0.02 * rng.normal(),
                }
            )
    df = pd.DataFrame(rows)
    df["rd_gap"] = df["rd_c"] * df["gap_c"]
    xs = ["rd_c", "gap_c", "rd_gap"]
    full = twfe(df, "dln_tfp", xs)
    fast = twfe_betas(df, "dln_tfp", xs)
    for x in xs:
        b = float(full.loc[full.term == x, "beta"].iloc[0])
        assert abs(b - fast[x]) < 1e-8


def test_pick_accel_column_prefers_name_not_cores():
    cols = [
        "Rank",
        "Accelerator/Co-Processor Cores",
        "Accelerator/Co-Processor",
        "Processor",
    ]
    assert pick_accel_column(cols) == "Accelerator/Co-Processor"
    cols2 = ["Rank", "Accelerator/Co-Processor Cores", "Foo"]
    assert pick_accel_column(cols2) is None


def test_d09_fails_when_snapshot_missing(tmp_path):
    missing = tmp_path / "missing_snapshot.csv"
    with pytest.raises(FileNotFoundError):
        load_quantum_snapshot(missing)


def test_d09_refuses_empty_overwrite(tmp_path):
    empty = tmp_path / "empty.csv"
    empty.write_text("country_iso3,indicator,value\n", encoding="utf-8")
    reuse = tmp_path / "D09_quantum_snapshot_reuse.csv"
    reuse.write_text(
        "country_iso3,indicator,value\nUSA,quantum_ipf_count,3330\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="refuse overwrite"):
        load_quantum_snapshot(empty, reuse_path=reuse)

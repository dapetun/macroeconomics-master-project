"""Один процесс на весь пайплайн D00–D11. / Single-process runner for D00–D11.

Снимает повторный cold-import statsmodels/matplotlib.
Avoids repeated cold imports of statsmodels/matplotlib.
"""
from __future__ import annotations

import runpy
import time
from pathlib import Path

SCRIPTS = [
    "D00_data_audit.py",
    "D01_baseline.py",
    "D02_benchmarking.py",
    "D03_knowledge_production.py",
    "D04_rd_tfp_frontier.py",
    "D05_growth_accounting.py",
    "D06_semiconductors.py",
    "D07_top500.py",
    "D08_ai_open_closed.py",
    "D09_quantum_card.py",
    "D10_robustness_summary.py",
    "D11_synthesis.py",
]


def main() -> None:
    # Явный стиль графиков один раз на процесс / Apply chart style once per process
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from macrodeep import apply_hse_style

    apply_hse_style()

    root = Path(__file__).resolve().parent / "deep"
    t_all = time.perf_counter()
    for name in SCRIPTS:
        path = root / name
        t0 = time.perf_counter()
        runpy.run_path(str(path), run_name="__main__")
        print(f"[run_all] {time.perf_counter() - t0:5.2f}s  {name}")
    print(f"[run_all] TOTAL {time.perf_counter() - t_all:.2f}s")


if __name__ == "__main__":
    main()

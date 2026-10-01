# %% [markdown]
# D09 — Квант: качественная карточка / Quantum: qualitative card

# %%
from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from macrodeep import load_quantum_snapshot, save_table  # noqa: E402
from macrodeep.quantum import OUT_NAME  # noqa: E402


def main() -> None:
    df = load_quantum_snapshot()
    save_table(df, OUT_NAME)

    card = pd.DataFrame([
        {"level": "science/pubs", "status": "snapshot", "note": "EPO-OECD labels; not panel"},
        {"level": "patents IPF", "status": "snapshot", "note": "USA IPF > CHN; national-only may reverse"},
        {"level": "funding", "status": "snapshot", "note": "~60% funding to US firms (report)"},
        {"level": "commercialization", "status": "missing", "note": "not measured"},
        {"level": "macro effect", "status": "missing", "note": "no econometrics by design: immature tech"},
    ])
    save_table(card, "D09_quantum_card")
    print(df[["country_iso3", "indicator", "value"]].head(9).to_string(index=False))
    print(card)
    print("D09 done")


if __name__ == "__main__":
    main()

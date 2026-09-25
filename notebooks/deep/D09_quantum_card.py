# %% [markdown]
# D09 — Квант: качественная карточка

# %%
from pathlib import Path
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "notebooks" / "deep"))
from _common import save_table

snap = ROOT / "data" / "raw" / "snapshots" / "quantum_epo_oecd_snapshot.csv"
df = pd.read_csv(snap) if snap.exists() else pd.DataFrame()
save_table(df, "D09_quantum_snapshot_reuse")

card = pd.DataFrame([
    {"level": "science/pubs", "status": "snapshot", "note": "EPO-OECD labels; not panel"},
    {"level": "patents IPF", "status": "snapshot", "note": "USA IPF > CHN; national-only may reverse"},
    {"level": "funding", "status": "snapshot", "note": "~60% funding to US firms (report)"},
    {"level": "commercialization", "status": "missing", "note": "not measured"},
    {"level": "macro effect", "status": "missing", "note": "no econometrics by design: immature tech"},
])
save_table(card, "D09_quantum_card")
print(card)
print("D09 done")

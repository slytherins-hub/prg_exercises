"""Stáhne záznamy z MIT-BIH Arrhythmia Database (PhysioNet) a uloží je jako .txt."""
import numpy as np
from pathlib import Path
import wfdb

OUT = Path(__file__).parent.parent / "docs" / "cviceni_09"

# Záznamy s normálním sinusovým rytmem (klidová TF ~60–80 BPM)
records_klid = [("100", "mitbih_100.txt"), ("101", "mitbih_101.txt")]
# Záznamy se zvýšenou TF (relativně vyšší průměrná TF)
records_zatez = [("119", "mitbih_119.txt"), ("117", "mitbih_117.txt")]

SAMPTO = 5400  # 15 s při 360 Hz

for rec_id, fname in records_klid:
    rec = wfdb.rdrecord(rec_id, pn_dir="mitdb", sampto=SAMPTO)
    t   = np.arange(rec.sig_len) / rec.fs
    ekg = rec.p_signal[:, 0].astype(float)
    path = OUT / "ekg_klid" / fname
    np.savetxt(path, np.column_stack([t, ekg]), fmt="%.5f",
               header="cas[s]  ekg[mV]", comments="")
    print(f"Uloženo: {path}  ({len(t)} vzorků, fs={rec.fs} Hz)")

for rec_id, fname in records_zatez:
    rec = wfdb.rdrecord(rec_id, pn_dir="mitdb", sampto=SAMPTO)
    t   = np.arange(rec.sig_len) / rec.fs
    ekg = rec.p_signal[:, 0].astype(float)
    path = OUT / "ekg_zatez" / fname
    np.savetxt(path, np.column_stack([t, ekg]), fmt="%.5f",
               header="cas[s]  ekg[mV]", comments="")
    print(f"Uloženo: {path}  ({len(t)} vzorků, fs={rec.fs} Hz)")

print("Hotovo.")

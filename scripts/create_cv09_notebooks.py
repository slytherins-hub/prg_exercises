"""Generátor notebooků pro cvičení 9 (NumPy a Matplotlib)."""
import nbformat
from pathlib import Path

OUT = Path(__file__).parent.parent / "docs" / "cviceni_09"


def md(text: str) -> nbformat.NotebookNode:
    return nbformat.v4.new_markdown_cell(text)


def code(text: str) -> nbformat.NotebookNode:
    return nbformat.v4.new_code_cell(text)


# ─────────────────────────────────────────────────────────────────
#  NOTEBOOK 1 – NumPy
# ─────────────────────────────────────────────────────────────────

numpy_cells = [
    md("""\
# CÍL 2: NumPy

> Tento notebook je součástí cvičení 9 předmětu BPC-PRG.  
> Projdi ho postupně – každou buňku spusť klávesou **Shift+Enter**.  
> 📥 **[Stáhnout notebook (cviceni_09_numpy.ipynb)](cviceni_09_numpy.ipynb)**
"""),

    md("## Co je NumPy?\n\n"
       "[**NumPy**](https://numpy.org/) *(Numerical Python)* je open-source matematická knihovna "
       "jazyka Python, na které stojí celý vědecký Python ekosystém. "
       "Vznikla v roce 2005 a dnes ji využívají datové vědy, fyzika, bioinformatika i strojové učení.\n\n"
       "Jejím jádrem je datová struktura **`ndarray`** (N-dimensional array) – "
       "kompaktní pole čísel uložené přímo v paměti jako v jazyku C. "
       "Na rozdíl od Python listu ukládá všechny prvky stejného datového typu bez extra réžie "
       "a operace nad ním jsou implementovány v kompilovaném C/Fortran kódu.\n\n"
       "> **💡 Tip:** NumPy v Pythonu z velké části nahrazuje MATLAB – syntaxe je velmi podobná, "
       "ale Python je volně dostupný a aktivně vyvíjený.\n\n"
       "### Kde NumPy potkáš v biomedicíně?\n\n"
       "| Oblast | Popis |\n"
       "|--------|-------|\n"
       "| Zpracování signálů (EKG, EEG, SpO₂) | Časové řady jako 1D pole, FFT, filtrování |\n"
       "| Medicínské snímky (MRI, CT, histologie) | 2D/3D matice pixelů, geometrické transformace |\n"
       "| Klinická data a biostatistika | Rychlé výpočty průměrů, std, korelací na tisících záznamů |\n"
       "| Strojové učení a AI | Všechny datové sady jsou interně numpy pole |\n\n"
       "### Místo v Python ekosystému\n\n"
       "NumPy je základ, na kterém staví ostatní vědecké knihovny:\n\n"
       "```\n"
       "NumPy ──► Matplotlib   (grafy, vizualizace)\n"
       "      ──► Pandas       (tabulková data, DataFrame)\n"
       "      ──► SciPy        (vědecké algoritmy – FFT, filtry, statistická analýza)\n"
       "      ──► scikit-learn (strojové učení)\n"
       "      ──► TensorFlow / PyTorch  (hluboké neuronové sítě)\n"
       "```\n\n"
       "Standardní import – zkratka `np` je všeobecnou konvencí:\n\n"
       "```python\n"
       "import numpy as np\n"
       "```"),

    # ── 2.1 Proč numpy ─────────────────────────────────────────────
    md("## 2.1 Proč numpy a ne Python seznam?\n\n"
       "**numpy pole (`ndarray`)** je základní datová struktura knihovny NumPy. "
       "Na rozdíl od Python listu:\n\n"
       "- uchovává data v **kompaktním bloku paměti stejného datového typu** (např. všechna `float64`),\n"
       "- operace jsou implementované v C/Fortran – Python smyčka není potřeba,\n"
       "- mohou být **vícerozměrná** (2D matice, 3D tenzory…),\n"
       "- podporují přímou **matematickou syntaxi**: `a * 2`, `a + b`, `np.sin(a)` – bez `for` cyklu.\n\n"
       "Výsledek: **10–100× rychlejší** pro numerické operace a výrazně čitelnější kód.\n\n"
       "Srovnání syntaxe – násobení každého prvku dvěma:\n\n"
       "```python\n"
       "# Python list – musíš projít každý prvek\n"
       "result = [x * 2 for x in my_list]\n\n"
       "# NumPy – přímá matematická operace na celém poli\n"
       "result = my_array * 2\n"
       "```"),

    code("""\
import numpy as np
import time

n = 10_000_000
py_list  = list(range(n))
np_array = np.arange(n)

# Varianta 1 – klasická for smyčka
result_loop = [0] * n
start = time.time()
for i in range(n):
    result_loop[i] = py_list[i] * 2
t_loop = time.time() - start

# Varianta 2 – list comprehension
start = time.time()
result_lc = [x * 2 for x in py_list]
t_lc = time.time() - start

# Varianta 3 – NumPy vektorizace
start = time.time()
result_np = np_array * 2
t_np = time.time() - start

print(f"for smyčka:         {t_loop:.3f} s")
print(f"list comprehension: {t_lc:.3f} s")
print(f"NumPy:              {t_np:.3f} s")
print(f"\\nNumPy vs. for smyčka:        {t_loop / t_np:.0f}×")
print(f"NumPy vs. list comprehension: {t_lc / t_np:.0f}×")
"""),

    # ── 2.2 Vytvoření pole ─────────────────────────────────────────
    md("## 2.2 Vytvoření pole"),

    code("""\
import numpy as np

# Ze seznamu
a = np.array([1, 2, 3, 4, 5])
a
"""),

    code("""\
# Číselná řada – arange(start, stop, krok)
np.arange(0, 10, 2)
"""),

    code("""\
# Rovnoměrně rozložené hodnoty – ideální pro časové osy
np.linspace(0, 1, 6)   # 6 hodnot od 0 do 1 včetně
"""),

    code("""\
np.zeros(4)
"""),

    code("""\
np.ones((2, 3))
"""),

    code("""\
# Gaussův šum – realistické biomedicínské hodnoty
noise = np.random.normal(loc=0, scale=0.1, size=8)
np.round(noise, 3)
"""),

    # ── 2.3 Tvar, dtype, reshape ───────────────────────────────────
    md("## 2.3 Tvar, datové typy a reshape"),

    md("### Tvar a indexování – 1D pole"),

    code("""\
signal = np.array([0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1])
signal
"""),

    code("""\
signal.shape, signal.ndim, len(signal)
"""),

    code("""\
signal[0], signal[-1]   # první a poslední prvek
"""),

    code("""\
signal[2:5]   # prvky 2–4
"""),

    code("""\
signal[::2]   # každý druhý prvek
"""),

    md("### 2D pole (matice)"),

    code("""\
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix
"""),

    code("""\
matrix.shape
"""),

    code("""\
matrix[1, 2]   # řádek 1, sloupec 2 → 6
"""),

    code("""\
matrix[0, :]   # první řádek
"""),

    code("""\
matrix[:, 1]   # druhý sloupec
"""),

    md("### Datové typy (dtype)"),

    code("""\
a_int = np.array([1, 2, 3])
a_int.dtype
"""),

    code("""\
a_float = np.array([1.0, 2.0, 3.0])
a_float.dtype
"""),

    code("""\
# Explicitní nastavení – float32 ušetří paměť oproti float64
a32 = np.zeros(4, dtype=np.float32)
print(f"dtype: {a32.dtype}   paměť na prvek: {a32.itemsize} B")
"""),

    code("""\
# Konverze dtype pomocí astype
a_int.astype(float)
"""),

    md("### Změna tvaru (reshape)"),

    code("""\
flat = np.arange(12)
flat
"""),

    code("""\
flat.reshape(3, 4)   # 3 řádky × 4 sloupce
"""),

    code("""\
flat.reshape(2, 2, 3).shape   # 3D tenzor – shape stačí
"""),

    code("""\
# -1 = NumPy dopočítá rozměr automaticky
flat.reshape(1, -1).shape, flat.reshape(-1, 1).shape
"""),

    # ── 2.4 Pokročilé indexování ───────────────────────────────────
    md("## 2.4 Pokročilé indexování\n\n"
       "Kromě klasického slicingu nabízí NumPy dva mocné způsoby výběru prvků:\n\n"
       "- **Fancy indexing** – výběr pomocí pole celých čísel (libovolné pozice),\n"
       "- **Boolean (binární) indexing** – výběr pomocí masky True/False (filtrování dle podmínky)."),

    md("### Fancy indexing"),

    code("""\
data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
data[[0, 2, 5]]   # prvky na pozicích 0, 2, 5
"""),

    code("""\
data[[5, 0, 5, 2]]   # libovolné pořadí, opakování je OK
"""),

    code("""\
# Výběr konkrétních pacientů z matice měření
mereni = np.array([[120, 80, 72],   # pacient 0: systola, diastola, TF
                   [135, 88, 90],   # pacient 1
                   [118, 76, 65],   # pacient 2
                   [145, 95, 88]])  # pacient 3

mereni[[0, 2]]   # pacienti 0 a 2
"""),

    md("### Boolean (binární) indexing"),

    code("""\
# Maska – pole True/False stejné délky jako data
mask = np.array([True, False, True, False, True, False, True, False])
data[mask]
"""),

    code("""\
# Masku nejčastěji vytvoříme podmínkou přímo
data > 40
"""),

    code("""\
data[data > 40]
"""),

    code("""\
# Kombinace podmínek: & = AND,  | = OR
data[(data > 20) & (data < 70)]
"""),

    code("""\
# Detekce R-peaků: indexy vzorků nad prahem 1.0
ekg = np.array([0.1, 0.3, 1.4, 1.6, 0.5, 0.2, 1.5, 0.3])
np.where(ekg > 1.0)[0]
"""),

    # ── 2.5 Matematické operace ────────────────────────────────────
    md("## 2.5 Matematické operace\n\n"
       "NumPy operace jsou **vektorizované** – pracují na celém poli naráz, bez explicitního cyklu."),

    code("""\
a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([0.5, 0.5, 0.5, 0.5])

a + b
"""),

    code("""\
a ** 2
"""),

    code("""\
np.round(np.sqrt(a), 3)
"""),

    code("""\
print(f"sum: {a.sum()}   mean: {a.mean()}   std: {a.std():.3f}")
print(f"min: {a.min()}   max: {a.max()}")
"""),

    code("""\
# Podmínkové indexování a agregace v jednom výrazu
a[a > 2].mean()
"""),

    # ── 2.6 Ukládání a načítání ────────────────────────────────────
    md("## 2.6 Ukládání a načítání polí\n\n"
       "NumPy má vlastní binární formáty, které zachovají dtype a tvar přesně:\n\n"
       "| Formát | Funkce | Obsah |\n"
       "|--------|--------|-------|\n"
       "| `.npy` | `np.save` / `np.load` | jedno pole |\n"
       "| `.npz` | `np.savez` / `np.load` | více pojmenovaných polí v jednom souboru |\n\n"
       "```python\n"
       "# .npy – jedno pole\n"
       "np.save('data.npy', pole)       # uložit\n"
       "pole = np.load('data.npy')      # načíst → přímo ndarray\n\n"
       "# .npz – více polí najednou\n"
       "np.savez('data.npz', x=cas, y=signal, meta=pole3)  # uložit\n"
       "d = np.load('data.npz')                             # načíst → dict-like objekt\n"
       "cas, signal = d['x'], d['y']                        # přístup přes klíče\n"
       "```\n\n"
       "> **💡 Tip:** `.npz` se hodí, když potřebuješ předat více polí dohromady – "
       "například v dalším cíli uložíme takto všechna data pro Matplotlib (EKG, MRI, glykémie…) "
       "do jednoho souboru `mpl_data.npz`."),

    # ── Úkol ──────────────────────────────────────────────────────
    md("""\
---

## 📝 ÚKOL: Analýza dat klinické studie

Stáhni si datový soubor se záznamy 20 pacientů:  
📥 **[pacienti.npy](pacienti.npy)**

Soubor obsahuje 2D pole tvaru `(20, 3)` – každý řádek je jeden pacient, sloupce jsou:
| Sloupec | Ukazatel | Jednotka |
|---------|----------|----------|
| 0 | Systolický krevní tlak | mmHg |
| 1 | Diastolický krevní tlak | mmHg |
| 2 | Tepová frekvence | BPM |

Formát `.npy` je binární formát NumPy – rychlý a přesný (zachovává dtype, tvar). Načteš ho jednoduše:
```python
data = np.load("pacienti.npy")
```

**1.** Načti soubor `pacienti.npy` a vypiš tvar pole a prvních 5 řádků.

**2.** Vypiš průměr a směrodatnou odchylku každého ukazatele.

**3.** Pomocí boolean indexingu najdi pacienty s hypertenzí – systolický tlak ≥ 140 mmHg. Vypiš jejich počet a průměrný systolický tlak.

**4.** Přidej 4. sloupec: **pulzní tlak** = systolický − diastolický. Použij `np.column_stack()` nebo `np.hstack()`.

**5.** Zjisti, který pacient má nejvyšší tepovou frekvenci – vypiš jeho index a celý záznam. Použij `np.argmax()`.
"""),

    code("""\
# --- ZDE PIŠE STUDENT ---

import numpy as np

# 1. Načtení dat
data = np.load("pacienti.npy")


# 2. Průměr a std každého ukazatele


# 3. Pacienti s hypertenzí (systolický ≥ 140)


# 4. Pulzní tlak jako nový sloupec


# 5. Pacient s nejvyšší tepovou frekvencí

"""),
]

numpy_nb = nbformat.v4.new_notebook(cells=numpy_cells)
numpy_nb.metadata["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
numpy_nb.metadata["language_info"] = {"name": "python", "version": "3.13.0"}

# ── Vygenerování dat pro úkol ────────────────────────────────────
import numpy as _np

_rng = _np.random.default_rng(42)
_systola  = _rng.normal(125, 15, 20)
_diastola = _rng.normal(80, 10, 20)
_tf       = _rng.integers(55, 96, 20).astype(float)
_pacienti = _np.column_stack([_systola, _diastola, _tf])
_pacienti = _np.round(_pacienti, 1)
path_data = OUT / "pacienti.npy"
_np.save(path_data, _pacienti)
print(f"Vytvořeno: {path_data}")

path_numpy = OUT / "cviceni_09_numpy.ipynb"
with open(path_numpy, "w", encoding="utf-8") as f:
    nbformat.write(numpy_nb, f)
print(f"Vytvořeno: {path_numpy}")


# ─────────────────────────────────────────────────────────────────
#  Data pro Matplotlib notebook
# ─────────────────────────────────────────────────────────────────

_rng_m = _np.random.default_rng(99)

# Signál EKG + respirace
_t    = _np.linspace(0, 2, 1000)
_ekg  = (
    _np.exp(-((_t - 0.5)**2) / 0.001) * 1.5
    + _np.exp(-((_t - 1.2)**2) / 0.001) * 1.5
    + _rng_m.normal(0, 0.04, len(_t))
)
_resp = _np.sin(2 * _np.pi * 0.3 * _t) + _rng_m.normal(0, 0.05, len(_t))

# MRI-like obraz 64×64
_xx = _np.linspace(-3, 3, 64)
_XX, _YY = _np.meshgrid(_xx, _xx)
_mri  = _np.exp(-(_XX**2 + _YY**2) / 2)
_mri += 0.3 * _np.exp(-((_XX - 1)**2 + (_YY + 1)**2) / 0.3)
_mri += 0.2 * _np.exp(-((_XX + 1.5)**2 + (_YY - 0.5)**2) / 0.5)
_mri += _rng_m.normal(0, 0.03, _mri.shape)

# Tepová frekvence – 4 skupiny
_klid   = _rng_m.normal(70,  8,  30)
_chuze  = _rng_m.normal(95,  10, 30)
_beh    = _rng_m.normal(140, 12, 30)
_sprint = _rng_m.normal(175, 8,  30)

# Glykémie – zdraví vs. diabetici
_zdravi    = _rng_m.normal(5.2, 0.5, 200)
_diabetici = _rng_m.normal(9.1, 1.8, 200)

# Zátěžový test – 30 pacientů × 60 minut
# Fáze: Klid 0-9, Zahřívání 10-19, Aerobní 20-39, Sprint 40-49, Regenerace 50-59
_mean_phase = _np.array([70]*10 + [100]*10 + [140]*20 + [170]*10 + [85]*10, dtype=float)
_baseline   = _rng_m.normal(0, 8, (30, 1))   # každý pacient má jiný baseline
_tf_test    = _mean_phase + _baseline + _rng_m.normal(0, 5, (30, 60))
_tf_test    = _np.clip(_np.round(_tf_test, 1), 45, 220)


# ── Skupiny snímků pro segmentační úkol (Cíl 5) ─────────────────
# skupina_a: "Zdravá tkáň"      – malý, kompaktní jasný region   ~20 % plochy
# skupina_b: "Nádorová tkáň"    – velký, rozlitý jasný region    ~45 % plochy
_rng_seg = _np.random.default_rng(77)
_xx_s = _np.linspace(-3, 3, 64)
_XXs, _YYs = _np.meshgrid(_xx_s, _xx_s)

_skupina_a = _np.zeros((5, 64, 64))
_centra_a = [(-0.4, 0.3), (0.5, -0.5), (-0.2, -0.3), (0.3, 0.4), (-0.5, 0.0)]
for _i, (_cx, _cy) in enumerate(_centra_a):
    _img = _np.exp(-((_XXs - _cx)**2 + (_YYs - _cy)**2) / 0.18)
    _img += _rng_seg.normal(0, 0.04, (64, 64))
    _skupina_a[_i] = _np.clip(_img, 0, 1)

_skupina_b = _np.zeros((5, 64, 64))
_centra_b = [(0.0, 0.0), (-0.3, 0.3), (0.4, -0.2), (-0.1, -0.4), (0.2, 0.3)]
for _i, (_cx, _cy) in enumerate(_centra_b):
    _img = _np.exp(-((_XXs - _cx)**2 + (_YYs - _cy)**2) / 1.4)
    _img += _rng_seg.normal(0, 0.04, (64, 64))
    _skupina_b[_i] = _np.clip(_img, 0, 1)

path_mpl_data = OUT / "mpl_data.npz"
_np.savez(path_mpl_data,
    t=_t, ekg=_ekg, resp=_resp, mri=_mri,
    klid=_klid, chuze=_chuze, beh=_beh, sprint=_sprint,
    zdravi=_zdravi, diabetici=_diabetici,
    tf_test=_tf_test)
print(f"Vytvořeno: {path_mpl_data}")

# ── Uložení snímků jako PNG souborů ─────────────────────────────
import matplotlib as _mpl
_mpl.use("Agg")
import matplotlib.pyplot as _plt_save

_dir_a = OUT / "skupina_a"
_dir_b = OUT / "skupina_b"
_dir_a.mkdir(exist_ok=True)
_dir_b.mkdir(exist_ok=True)

for _i in range(5):
    _plt_save.imsave(_dir_a / f"snimek_{_i:02d}.png", _skupina_a[_i], cmap="gray", vmin=0, vmax=1)
    _plt_save.imsave(_dir_b / f"snimek_{_i:02d}.png", _skupina_b[_i], cmap="gray", vmin=0, vmax=1)
print(f"Vytvořeny PNG snímky: {_dir_a}, {_dir_b}")

# ── EKG signály pro Cíl 6 (dvě skupiny, .txt soubory) ───────────
# fs = 500 Hz, 10 s záznamu → 5000 vzorků
# Klidová TF: ~62–68 BPM, Zátěžová TF: ~95–108 BPM
_fs = 500
_dur = 10.0
_t_ekg = _np.linspace(0, _dur, int(_fs * _dur), endpoint=False)

def _gen_ekg(tf_bpm, rng, noise=0.06):
    """Generuje syntetický EKG signál pro danou TF (BPM)."""
    period = 60.0 / tf_bpm          # perioda v sekundách
    sig = _np.zeros(len(_t_ekg))
    peak_t = _np.arange(period / 2, _dur, period)
    for pt in peak_t:
        sig += 1.5 * _np.exp(-((_t_ekg - pt) ** 2) / (2 * 0.003**2))
    sig += rng.normal(0, noise, len(_t_ekg))
    return sig

_rng_ekg = _np.random.default_rng(55)
_tf_klid   = [62, 65, 68, 63, 67]    # klidová TF (BPM)
_tf_zatez  = [98, 103, 107, 95, 101] # zátěžová TF (BPM)

_dir_ekg_k = OUT / "ekg_klid"
_dir_ekg_z = OUT / "ekg_zatez"
_dir_ekg_k.mkdir(exist_ok=True)
_dir_ekg_z.mkdir(exist_ok=True)

for _i, _tf in enumerate(_tf_klid):
    _sig = _gen_ekg(_tf, _rng_ekg)
    _np.savetxt(_dir_ekg_k / f"pacient_{_i:02d}.txt",
                _np.column_stack([_t_ekg, _sig]), fmt="%.5f",
                header="cas[s]  ekg[mV]", comments="")
for _i, _tf in enumerate(_tf_zatez):
    _sig = _gen_ekg(_tf, _rng_ekg)
    _np.savetxt(_dir_ekg_z / f"pacient_{_i:02d}.txt",
                _np.column_stack([_t_ekg, _sig]), fmt="%.5f",
                header="cas[s]  ekg[mV]", comments="")
print(f"Vytvořeny EKG soubory: {_dir_ekg_k}, {_dir_ekg_z}")

# ── Reálná EKG data z MIT-BIH Arrhythmia Database (PhysioNet) ───
# Záznamy 100 a 101 – normální sinusový rytmus, 15 s záznamu
_dir_ekg_real = OUT / "ekg_real"
_dir_ekg_real.mkdir(exist_ok=True)

_MITBIH_RECORDS = [("100", "mitbih_100.txt"), ("101", "mitbih_101.txt")]
_MITBIH_SAMPTO  = 5400   # 15 s při 360 Hz

try:
    import wfdb as _wfdb
    for _rec_id, _fname in _MITBIH_RECORDS:
        _rec = _wfdb.rdrecord(_rec_id, pn_dir="mitdb", sampto=_MITBIH_SAMPTO)
        _t_r = _np.arange(_rec.sig_len) / _rec.fs
        _ekg_r = _rec.p_signal[:, 0].astype(float)
        _np.savetxt(_dir_ekg_real / _fname,
                    _np.column_stack([_t_r, _ekg_r]), fmt="%.5f",
                    header="cas[s]  ekg[mV]", comments="")
    print(f"Vytvořeny reálné EKG soubory: {_dir_ekg_real}")
except Exception as _e:
    print(f"WARN: nelze stáhnout MIT-BIH data ({_e}) – demo buňka nemusí fungovat")


# ─────────────────────────────────────────────────────────────────
#  NOTEBOOK 2 – Matplotlib
# ─────────────────────────────────────────────────────────────────

mpl_cells = [
    md("""\
# CÍL 3: Matplotlib

> Tento notebook je součástí cvičení 9 předmětu BPC-PRG.  
> Projdi ho postupně – každou buňku spusť klávesou **Shift+Enter**.  
> 📥 **[Stáhnout notebook](cviceni_09_matplotlib.ipynb)** &nbsp;|&nbsp; 📥 **[Stáhnout data (mpl_data.npz)](mpl_data.npz)**
"""),

    code("""\
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# Všechna data jsou předpřipravena – stáhni mpl_data.npz a načti:
d = np.load("mpl_data.npz")

t, ekg, resp        = d["t"], d["ekg"], d["resp"]
mri                 = d["mri"]
zatez               = [d["klid"], d["chuze"], d["beh"], d["sprint"]]
zdravi, diabetici   = d["zdravi"], d["diabetici"]

# Zátěžový test: tf_test.shape == (30, 60)
# 30 pacientů měřených každou minutu po dobu 60 minut
# Fáze:  Klid 0–9 min | Zahřívání 10–19 | Aerobní 20–39 | Sprint 40–49 | Regenerace 50–59
tf_test = d["tf_test"]
"""),

    md("## Co je Matplotlib?\n\n"
       "[**Matplotlib**](https://matplotlib.org/) je nejrozšířenější Python knihovna pro tvorbu grafů a vizualizací. "
       "Vznikla v roce 2003 jako náhrada za grafiku MATLABu – odtud jméno.\n\n"
       "Její hlavní modul, který budeš téměř vždy importovat, se jmenuje **`pyplot`**. "
       "Poskytuje rozhraní inspirované MATLABem a umožňuje tvorbu grafů několika řádky kódu.\n\n"
       "V biomedicíně ji využiješ na:\n\n"
       "- vykreslení **časových řad** (EKG, dech, krevní tlak, teplota),\n"
       "- zobrazení **medicínských snímků** (MRI, CT, histologické řezy) jako 2D matice,\n"
       "- **statistické grafy** – boxploty pro srovnání skupin pacientů, histogramy pro rozložení hodnot,\n"
       "- **vědecké publikace** – výstup ve formátu PDF/SVG s přesnou kontrolou nad každým detailem.\n\n"
       "Matplotlib je úzce provázaný s NumPy – jako data přijímají funkce přímo numpy pole.\n\n"
       "### Co vše lze vykreslit?\n\n"
       "| Typ grafu | Funkce | Kdy ho použít |\n"
       "|-----------|--------|---------------|\n"
       "| Spojnicový | `ax.plot()` | Časové řady – EKG, dech, průběh léčby |\n"
       "| Sloupcový | `ax.bar()` | Srovnání kategorií – průměry skupin, výsledky měření |\n"
       "| Bodový (scatter) | `ax.scatter()` | Korelace dvou proměnných – výška vs. váha |\n"
       "| Histogram | `ax.hist()` | Rozložení hodnot – glykémie, BMI, TF |\n"
       "| Boxplot | `ax.boxplot()` | Mediány a rozptyl napříč skupinami pacientů |\n"
       "| Obrázek / heatmapa | `ax.imshow()` | MRI, CT snímky, korelační matice |\n"
       "| Výsečový | `ax.pie()` | Podíly – zastoupení diagnóz v populaci |\n\n"
       "> **💡 Poznámka:** Pro interaktivní a webové grafy existují moderní alternativy "
       "jako **Plotly** nebo **Bokeh**. Matplotlib je ale základ, na kterém jsou postavené "
       "i vyšší knihovny jako **Seaborn** nebo **Pandas** `.plot()`."),

    md("## 3.1 Základní struktura matplotlib\n\n"
       "Matplotlib má dvě vrstvy rozhraní:\n\n"
       "- **`plt.plot()`** – rychlé globální funkce, dobré pro jeden jednoduchý graf,\n"
       "- **`fig, ax = plt.subplots()`** – přímá práce s objekty Figure a Axes, "
       "doporučovaný přístup jakmile máš víc grafů nebo potřebuješ přesnou kontrolu.\n\n"
       "Budeme používat druhý přístup – je přehlednější a lépe se škáluje na složitější vizualizace."),

    code("""\
fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(t[:100], ekg[:100])
ax.set_title("Ukázkový graf (fig, ax pattern)")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("EKG (mV)")
ax.grid(True, alpha=0.4)
plt.show()
"""),

    md("## 3.2 Vykreslení signálu\n\n"
       "Spojnicový graf je základní vizualizace pro časové řady – EKG, dech, krevní tlak, teplotu."),

    code("""\
fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(t, ekg, linewidth=0.8)
ax.set_title("EKG (2 s, 500 Hz)")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("Amplituda (mV)")
ax.grid(True, alpha=0.4)
plt.show()
"""),

    md("### Více grafů pod sebou – `sharex=True`\n\n"
       "`plt.subplots(2, 1, sharex=True)` vytvoří dva grafy sdílející osu X – "
       "ideální pro srovnání více kanálů (EKG + dech, EKG + tlak apod.)."),

    code("""\
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5), sharex=True)
ax1.plot(t, ekg, linewidth=0.8)
ax1.set_ylabel("EKG (mV)")
ax2.plot(t, resp, color="seagreen")
ax2.set_ylabel("Respirace")
ax2.set_xlabel("Čas (s)")
fig.suptitle("Pacientský záznam – EKG a dech")
plt.tight_layout()
plt.show()
"""),

    md("## 3.3 Zobrazení matice / obrazu\n\n"
       "`imshow()` zobrazí 2D numpy pole jako obrázek nebo heatmapu – "
       "každá hodnota odpovídá barvě pixelu. Hodí se pro medicínské snímky (MRI, CT), "
       "korelační matice nebo síťové váhy v neuronových sítích."),

    code("""\
fig, ax = plt.subplots()
im = ax.imshow(mri, cmap="gray")
fig.colorbar(im)
ax.axis("off")
ax.set_title("Simulovaný MRI průřez")
plt.show()
"""),

    md("> **💡 Tip:** Pro medicínské obrazy se nejčastěji používá `cmap=\"gray\"`. "
       "`viridis` je dobrou volbou pro vědecké heatmapy – je perceptuálně uniformní "
       "(stejné rozdíly v datech odpovídají stejně vnímaným rozdílům v barvě) "
       "a čitelná i při výtisku nebo pro barvoslepé."),

    md("## 3.4 Boxplot – statistické srovnání skupin\n\n"
       "Boxplot je ideální pro srovnání rozložení hodnot napříč skupinami – "
       "různé pacienty, různé podmínky měření, různé diagnózy. "
       "Ukazuje medián, kvartily, vousy a odlehlé hodnoty."),

    code("""\
fig, ax = plt.subplots()
ax.boxplot(zatez, tick_labels=["Klid", "Chůze", "Běh", "Sprint"])
ax.set_title("Tepová frekvence při různé zátěži")
ax.set_ylabel("TF (BPM)")
ax.grid(True, axis="y", alpha=0.4)
plt.show()
"""),

    md("## 3.5 Histogram – rozložení hodnot\n\n"
       "Histogram ukazuje, jak jsou hodnoty rozloženy. "
       "Hodí se pro první pohled na data – je rozložení symetrické? "
       "Má odlehlé hodnoty? Odpovídá normálnímu rozložení?"),

    code("""\
fig, ax = plt.subplots()
ax.hist(zdravi,    bins=25, alpha=0.6, label="Zdravá populace")
ax.hist(diabetici, bins=25, alpha=0.6, label="Diabetici")
ax.axvline(7.0, color="black", linestyle="--", label="mez 7.0 mmol/l")
ax.set_xlabel("Glykémie (mmol/l)")
ax.set_ylabel("Počet pacientů")
ax.legend()
plt.show()
"""),

    md("""\
---

## 📝 ÚKOL: Zátěžový test – analýza a vizualizace

Data `tf_test` jsou již načtena v nastavovací buňce.  
Jde o matici **30 pacientů × 60 minut** tepové frekvence (BPM) z protokolu:

| Fáze | Minuty |
|------|--------|
| Klid | 0–9 |
| Zahřívání | 10–19 |
| Aerobní | 20–39 |
| Sprint | 40–49 |
| Regenerace | 50–59 |

**1. Průměrný signál v čase**  
Vypočítej průměrnou TF napříč pacienty pro každou minutu (`mean(axis=0)`) a vykresli jako spojnicový graf.  
Osa X = minuty (0–59), osa Y = TF (BPM). Přidej nadpis a popsané osy.

**2. Boxplot per fáze**  
Pro každou fázi vezmi hodnoty všech pacientů a všech minut (`tf_test[:, 0:10].ravel()` atd.) a vykresli boxplot pěti skupin.  
Popisky: `["Klid", "Zahřívání", "Aerobní", "Sprint", "Regenerace"]`.

**3. Histogram – klid vs. sprint**  
Do jednoho histogramu vykresli hodnoty fáze Klid a fáze Sprint (oba `ravel()`).  
Přidej legendu a popsané osy.

**4.** Ke každému grafu přidej markdownovou buňku s jednou větou – co graf ukazuje.
"""),

    code("""\
# --- ZDE PIŠE STUDENT ---

# tf_test.shape == (30, 60)
# Fáze: Klid 0–9, Zahřívání 10–19, Aerobní 20–39, Sprint 40–49, Regenerace 50–59

# 1. Průměrná TF v čase (signál)


# 2. Boxplot – 5 fází
faze_data   = [tf_test[:, 0:10].ravel(), tf_test[:, 10:20].ravel(),
               tf_test[:, 20:40].ravel(), tf_test[:, 40:50].ravel(),
               tf_test[:, 50:60].ravel()]
faze_labels = ["Klid", "Zahřívání", "Aerobní", "Sprint", "Regenerace"]


# 3. Histogram – klid vs. sprint

"""),
]

mpl_nb = nbformat.v4.new_notebook(cells=mpl_cells)
mpl_nb.metadata["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
mpl_nb.metadata["language_info"] = {"name": "python", "version": "3.13.0"}

path_mpl = OUT / "cviceni_09_matplotlib.ipynb"
with open(path_mpl, "w", encoding="utf-8") as f:
    nbformat.write(mpl_nb, f)
print(f"Vytvořeno: {path_mpl}")


# ─────────────────────────────────────────────────────────────────
#  NOTEBOOK 3 – Úkol: Segmentace medicínských snímků (Cíl 5)
# ─────────────────────────────────────────────────────────────────

seg_cells = [
    md("""\
# CÍL 5: ÚKOL – Segmentace medicínských snímků

> Tento notebook je součástí cvičení 9 předmětu BPC-PRG.  
> 📥 **[Stáhnout notebook (cviceni_09_segmentace.ipynb)](cviceni_09_segmentace.ipynb)**
"""),

    code("""\
# Ukázkové načtení a zobrazení dvou snímků pomocí pevně zadané cesty
# Spuštěním této buňky ověříš, že jsou soubory dostupné a funkce plt.imread() funguje
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

snimek_a = plt.imread("skupina_a/snimek_00.png")[:, :, 0]
snimek_b = plt.imread("skupina_b/snimek_00.png")[:, :, 0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(snimek_a, cmap="gray", vmin=0, vmax=1)
ax1.set_title("skupina_a/snimek_00.png")
ax1.axis("off")
ax2.imshow(snimek_b, cmap="gray", vmin=0, vmax=1)
ax2.set_title("skupina_b/snimek_00.png")
ax2.axis("off")
plt.suptitle("Ukázka: načtení snímků pomocí plt.imread()")
plt.tight_layout()
plt.show()
print(f"Tvar pole: {snimek_a.shape}, hodnoty: min={snimek_a.min():.3f}, max={snimek_a.max():.3f}")
"""),

    md("""\
## Zadání

Máš k dispozici dvě skupiny simulovaných medicínských snímků ve složkách
`skupina_a/` a `skupina_b/` (5 snímků `.png` v každé složce):

- **`skupina_a/`** – „Zdravá tkáň": malý, kompaktní jasný region (~20 % plochy)
- **`skupina_b/`** – „Nádorová tkáň": velký, rozlitý jasný region (~45 % plochy)

Snímky načteš pomocí `plt.imread()`. Ten vrátí RGBA pole tvaru `(64, 64, 4)` –
pro práci s intenzitou stačí vzít první kanál: `snimek = plt.imread(...)[:, :, 0]`

Proveď postupně tyto kroky:

1. **Načti data** – načti všechny snímky ze složek a zobraz první snímek z každé skupiny.
2. **Prahování** – naprahuj jeden snímek, vytvoř binární masku a zobraz ji vedle originálu.
3. **Kvantitativní analýza** – spočítej poměrnou plochu pokrytou strukturou a průměrnou intenzitu uvnitř masky.
4. **Srovnání skupin** – zpracuj všechny snímky obou skupin a porovnej poměrné plochy boxplotem.
"""),

    code("""\
%matplotlib inline
import glob
import numpy as np
import matplotlib.pyplot as plt

# Krok 1 – načtení snímků
files_a = sorted(glob.glob("skupina_a/*.png"))
files_b = sorted(glob.glob("skupina_b/*.png"))

# plt.imread vrátí RGBA pole (64, 64, 4) – bereme jen první kanál (intenzita)
skupina_a = [plt.imread(f)[:, :, 0] for f in files_a]
skupina_b = [plt.imread(f)[:, :, 0] for f in files_b]

print(f"Načteno snímků skupiny A: {len(skupina_a)}, tvar: {skupina_a[0].shape}")
print(f"Načteno snímků skupiny B: {len(skupina_b)}, tvar: {skupina_b[0].shape}")

# Zobrazení prvního snímku z každé skupiny
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(skupina_a[0], cmap="gray", vmin=0, vmax=1)
ax1.set_title("Zdravá tkáň – snímek 0")
ax1.axis("off")
ax2.imshow(skupina_b[0], cmap="gray", vmin=0, vmax=1)
ax2.set_title("Nádorová tkáň – snímek 0")
ax2.axis("off")
plt.suptitle("Vstupní data")
plt.tight_layout()
plt.show()
"""),

    md("""\
### Krok 2 – Prahování a vizualizace masky

Naprahuj snímek – vytvoř **binární masku**: NumPy pole `bool`, kde `True` = pixel patří do struktury.

```python
maska = snimek > PRAH
```

Zobraz vedle sebe původní snímek a binární masku.
"""),

    code("""\
# Krok 2 – prahování
PRAH = 0.5
snimek = skupina_a[0]

maska = snimek > PRAH

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(snimek, cmap="gray", vmin=0, vmax=1)
ax1.set_title("Původní snímek")
ax1.axis("off")
ax2.imshow(maska, cmap="gray")
ax2.set_title(f"Binární maska (práh = {PRAH})")
ax2.axis("off")
plt.tight_layout()
plt.show()
"""),

    md("""\
### Krok 3 – Kvantitativní analýza

Pro snímek a masku z Kroku 2 spočítej:

- **poměrnou plochu struktury** – kolik % pixelů je `True` v masce  
  `podil = maska.sum() / maska.size * 100`
- **průměrnou intenzitu** – průměr hodnot pixelů *uvnitř* masky  
  `mean_int = snimek[maska].mean()`
"""),

    code("""\
# Krok 3 – kvantitativní analýza
podil    = maska.sum() / maska.size * 100
mean_int = snimek[maska].mean()

print(f"Plocha struktury: {podil:.1f} %")
print(f"Průměrná intenzita: {mean_int:.3f}")
"""),

    md("""\
### Krok 4 – Srovnání skupin: boxplot

Zpracuj **všechny snímky** obou skupin: pro každý snímek spočítej poměrnou plochu
při `PRAH = 0.5`. Výsledky ulož do dvou seznamů a vykresli boxplot.
"""),

    code("""\
# Krok 4 – srovnání skupin
PRAH = 0.5

podily_a = []
for snimek in skupina_a:
    maska = snimek > PRAH
    podil = maska.sum() / maska.size * 100
    podily_a.append(podil)

podily_b = []
for snimek in skupina_b:
    maska = snimek > PRAH
    podil = maska.sum() / maska.size * 100
    podily_b.append(podil)

fig, ax = plt.subplots()
ax.boxplot([podily_a, podily_b], tick_labels=["Zdravá tkáň", "Nádorová tkáň"])
ax.set_ylabel("Plocha struktury (%)")
ax.set_title("Srovnání skupin – segmentovaná plocha")
ax.grid(True, axis="y", alpha=0.4)
plt.show()

print("Skupina A (zdravá tkáň):", [f"{p:.1f} %" for p in podily_a])
print("Skupina B (nádorová tkáň):", [f"{p:.1f} %" for p in podily_b])
"""),

    md("""\
### Interpretace

*Sem napiš, jak se skupiny liší a co by mohl výsledek znamenat klinicky.*
"""),
]

seg_nb = nbformat.v4.new_notebook(cells=seg_cells)
seg_nb.metadata["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
seg_nb.metadata["language_info"] = {"name": "python", "version": "3.13.0"}

path_seg = OUT / "cviceni_09_segmentace.ipynb"
with open(path_seg, "w", encoding="utf-8") as f:
    nbformat.write(seg_nb, f)
print(f"Vytvořeno: {path_seg}")


# ─────────────────────────────────────────────────────────────────
#  NOTEBOOK 4 – Úkol: Analýza tepové frekvence z EKG (Cíl 6)
# ─────────────────────────────────────────────────────────────────

ekg_cells = [
    md("""\
# CÍL 6: ÚKOL – Analýza tepové frekvence z EKG

> Tento notebook je součástí cvičení 9 předmětu BPC-PRG.  
> 📥 **[Stáhnout notebook (cviceni_09_ekg.ipynb)](cviceni_09_ekg.ipynb)**
"""),

    code("""\
# Ukázkové načtení a zobrazení dvou reálných EKG záznamů pomocí pevně zadané cesty
# Data z MIT-BIH Arrhythmia Database (PhysioNet), fs = 360 Hz
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

data_0 = np.loadtxt("ekg_real/mitbih_100.txt", skiprows=1)
data_1 = np.loadtxt("ekg_real/mitbih_101.txt", skiprows=1)
t0, ekg0 = data_0[:, 0], data_0[:, 1]
t1, ekg1 = data_1[:, 0], data_1[:, 1]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5), sharex=True)
ax1.plot(t0, ekg0, linewidth=0.7, color="steelblue")
ax1.set_ylabel("EKG (mV)")
ax1.set_title("MIT-BIH záznam 100")
ax1.grid(True, alpha=0.3)
ax2.plot(t1, ekg1, linewidth=0.7, color="darkorange")
ax2.set_xlabel("Čas (s)")
ax2.set_ylabel("EKG (mV)")
ax2.set_title("MIT-BIH záznam 101")
ax2.grid(True, alpha=0.3)
plt.suptitle("Ukázka: reálné EKG záznamy (MIT-BIH Arrhythmia Database, PhysioNet)")
plt.tight_layout()
plt.show()
print(f"Délka záznamu: {t0[-1]:.1f} s, vzorkovací frekvence: {1/(t0[1]-t0[0]):.0f} Hz")
"""),

    md("""\
## Zadání

Máš k dispozici dvě skupiny EKG záznamů (5 pacientů v každé skupině):

- **`ekg_klid/`** – záznamy v klidu (~60–70 BPM)
- **`ekg_zatez/`** – záznamy při zátěži (~95–110 BPM)

Každý soubor `.txt` je tabulka se dvěma sloupci:  
`cas[s]` (čas v sekundách) a `ekg[mV]` (amplituda signálu). První řádek je záhlaví,  
proto použij `np.loadtxt(soubor, skiprows=1)`.

Proveď postupně tyto kroky:

1. **Načti a vykresli** jeden EKG signál – ukaž, jak vypadá.
2. **Naprahuj signál** – najdi vzorky nad prahem (R-vrcholy = srdeční údery).
3. **Detekuj vrcholy** – z každé skupiny nad prahem vyber jeden bod (náběžná hrana).
4. **Spočítej tepovou frekvenci** (BPM) z časů nalezených vrcholů.
5. **Zpracuj všechny záznamy** obou skupin a porovnej TF boxplotem.
"""),

    code("""\
%matplotlib inline
import glob
import numpy as np
import matplotlib.pyplot as plt

# Krok 1 – načtení souborů
files_klid  = sorted(glob.glob("ekg_klid/*.txt"))
files_zatez = sorted(glob.glob("ekg_zatez/*.txt"))

# np.loadtxt vrátí matici (N, 2) – sloupec 0 = čas, sloupec 1 = signál
data0 = np.loadtxt(files_klid[0], skiprows=1)
t   = data0[:, 0]   # čas v sekundách
ekg = data0[:, 1]   # amplituda v mV

print(f"Načteno {len(files_klid)} klidových a {len(files_zatez)} zátěžových záznamů")
print(f"Délka záznamu: {t[-1]:.1f} s, vzorkovací frekvence: {1/(t[1]-t[0]):.0f} Hz")

# Vizualizace prvního záznamu
fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(t, ekg, linewidth=0.8, color="steelblue")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("EKG (mV)")
ax.set_title("EKG signál – pacient 0 (klidová skupina)")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
"""),

    md("""\
### Krok 2 – Prahování: které vzorky jsou „vrchol"?

Každý srdeční úder způsobí v EKG charakteristický ostrý výkyv – **R-vlna**.  
Jednoduchý způsob, jak ji najít: stanovíme **práh** (threshold) a označíme všechny
vzorky, kde je signál nad tímto prahem.

```python
PRAH = 0.5
nad_prahem = ekg > PRAH   # → pole True/False
```

Výsledkem je logická maska – `True` tam, kde je amplituda dostatečně vysoká.  
Na grafu to odpovídá oblasti okolo každé R-vlny.
"""),

    code("""\
# Krok 2 – prahování
PRAH = 0.5
nad_prahem = ekg > PRAH

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(t, ekg, linewidth=0.8, color="steelblue", label="EKG")
ax.axhline(PRAH, color="tomato", linestyle="--", linewidth=1, label=f"Práh = {PRAH}")
ax.fill_between(t, PRAH, ekg, where=nad_prahem, alpha=0.3, color="tomato", label="Nad prahem")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("EKG (mV)")
ax.set_title("Prahování EKG signálu")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
"""),

    md("""\
### Krok 3 – Detekce R-vrcholů: náběžná hrana

Po prahování máme v `nad_prahem` skupiny `True` hodnot – jednu skupinu na každý srdeční úder.
Chceme z každé skupiny vybrat **právě jeden bod**.

Trik s `np.roll()`:  
`np.roll(pole, -1)` posune pole o jedno místo doleva (každý prvek se „podívá" na svého souseda vpravo).  
Vzoreky, kde je `True` a soused vpravo je `False`, jsou **poslední True v sérii** = sestupná hrana = vrchol R-vlny.

```
ind:          0     1     2     3     4     5     6
nad_prahem: False False  True  True  True False False
roll(-1):   False  True  True  True False False False
----------------------------------------
nad & ~roll: False False False False  True False False  ← jedna značka na vrchol
```
"""),

    code("""\
# Krok 3 – detekce vrcholů (sestupná hrana = konec každé skupiny nad prahem)
vrcholy = nad_prahem & ~np.roll(nad_prahem, -1)
vrcholy[-1] = False   # poslední vzorek vždy False (okrajový efekt roll)

vrcholy_idx = np.where(vrcholy)[0]
print(f"Nalezeno vrcholů: {len(vrcholy_idx)}")

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(t, ekg, linewidth=0.8, color="steelblue", label="EKG")
ax.axhline(PRAH, color="gray", linestyle="--", linewidth=0.8, label=f"Práh = {PRAH}")
ax.scatter(t[vrcholy_idx], ekg[vrcholy_idx], color="tomato", zorder=5, s=60, label="R-vrchol")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("EKG (mV)")
ax.set_title(f"Detekce R-vrcholů – nalezeno {len(vrcholy_idx)} úderů")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
"""),

    md("""\
### Krok 4 – Výpočet tepové frekvence

Časy R-vrcholů `t[vrcholy_idx]` nám říkají, kdy přesně každý srdeční úder nastal.  
Interval mezi sousedními vrcholy = délka jednoho srdečního cyklu (R-R interval).  
Z R-R intervalu v sekundách snadno spočítáme TF v BPM:

```python
rr_intervaly = np.diff(t[vrcholy_idx])   # délka každého cyklu [s]
tf_bpm       = 60 / rr_intervaly.mean() # → průměrná TF [BPM]
```
"""),

    code("""\
# Krok 4 – tepová frekvence
cas_vrcholu  = t[vrcholy_idx]
rr_intervaly = np.diff(cas_vrcholu)   # R-R intervaly v sekundách
tf_bpm       = 60 / rr_intervaly.mean()

print(f"Průměrný R-R interval: {rr_intervaly.mean():.3f} s")
print(f"Tepová frekvence: {tf_bpm:.1f} BPM")
"""),

    md("""\
### Krok 5 – Srovnání skupin: boxplot

Zpracuj **všechny záznamy** obou skupin stejným postupem (prahování → detekce vrcholů → TF).  
Výsledky ulož do dvou seznamů a porovnej boxplotem.
"""),

    code("""\
# Krok 5 – srovnání skupin
PRAH = 0.5

def spocitej_tf(soubor):
    # Načte EKG soubor a vrátí průměrnou TF v BPM.
    data = np.loadtxt(soubor, skiprows=1)
    t_s  = data[:, 0]
    ekg_s = data[:, 1]
    nad = ekg_s > PRAH
    vrc = nad & ~np.roll(nad, -1)
    vrc[-1] = False
    idx = np.where(vrc)[0]
    if len(idx) < 2:
        return float("nan")
    return 60 / np.diff(t_s[idx]).mean()

tf_klid  = [spocitej_tf(f) for f in files_klid]
tf_zatez = [spocitej_tf(f) for f in files_zatez]

print("Klidová TF (BPM): ", [f"{x:.1f}" for x in tf_klid])
print("Zátěžová TF (BPM):", [f"{x:.1f}" for x in tf_zatez])

fig, ax = plt.subplots()
ax.boxplot([tf_klid, tf_zatez], tick_labels=["Klidová", "Zátěžová"])
ax.set_ylabel("Tepová frekvence (BPM)")
ax.set_title("Srovnání skupin – tepová frekvence")
ax.grid(True, axis="y", alpha=0.4)
plt.show()
"""),

    md("""\
### Interpretace

*Sem napiš, jak se skupiny liší a co výsledek ukazuje.*
"""),
]

ekg_nb = nbformat.v4.new_notebook(cells=ekg_cells)
ekg_nb.metadata["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
ekg_nb.metadata["language_info"] = {"name": "python", "version": "3.13.0"}

path_ekg = OUT / "cviceni_09_ekg.ipynb"
with open(path_ekg, "w", encoding="utf-8") as f:
    nbformat.write(ekg_nb, f)
print(f"Vytvořeno: {path_ekg}")



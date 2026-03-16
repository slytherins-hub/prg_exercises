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

path_mpl_data = OUT / "mpl_data.npz"
_np.savez(path_mpl_data,
    t=_t, ekg=_ekg, resp=_resp, mri=_mri,
    klid=_klid, chuze=_chuze, beh=_beh, sprint=_sprint,
    zdravi=_zdravi, diabetici=_diabetici,
    tf_test=_tf_test)
print(f"Vytvořeno: {path_mpl_data}")


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

    md("### Detekce událostí – `ax.scatter()`\n\n"
       "Při analýze signálů nás často zajímá, kdy nastane konkrétní událost – "
       "R-vlna v EKG, vrchol respirace, nástup záchvatu. "
       "Události lze detekovat naprahováním a vizualizovat jako body přes spojnicový graf "
       "pomocí `ax.scatter()`."),

    code("""\
# Prahování: vzorky nad prahem → True
prahovana = ekg > 0.5
# Zachovej jen poslední True v každé sérii (= vrchol vlny)
r_peaks = prahovana & ~np.roll(prahovana, -1)
r_peaks[-1] = False

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(t, ekg, linewidth=0.8, label="EKG")
ax.scatter(t[r_peaks], ekg[r_peaks], color="red", zorder=5, label="R-vrchol")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("EKG (mV)")
ax.set_title(f"EKG – detekce R-vrcholů  (nalezeno: {r_peaks.sum()})")
ax.legend()
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

    md("""\
## 3.3b Segmentace obrazu – prahování

V medicínské analýze obrazu nás zajímá, *kde* v obraze se nachází určitá struktura –
cévy, tumor, tuková tkáň. Základní přístup je **prahování** (*thresholding*):
vytvoříme **binární masku** – numpy pole `bool`, kde `True` označuje pixely patřící
hledané struktuře.

```python
maska = obraz > PRÁH      # pixely nad prahem → True
```

Masku pak zobrazíme vedle původního obrazu pomocí `plt.subplots(1, 2)`.
"""),

    code("""\
PRAH = 0.5
maska = mri > PRAH

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))
ax1.imshow(mri, cmap="gray")
ax1.set_title("Původní obraz")
ax1.axis("off")
ax2.imshow(maska, cmap="gray")
ax2.set_title(f"Segmentační maska  (práh = {PRAH})")
ax2.axis("off")
plt.suptitle("Segmentace jasných oblastí – prahování")
plt.tight_layout()
plt.show()

podil = maska.sum() / maska.size * 100
print(f"Plocha jasných oblastí: {podil:.1f} %  |  Průměrná intenzita: {mri[maska].mean():.3f}")
"""),

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
## 3.6 Segmentace signálu – `axvspan`

V biomedicíně je signál często rozdělen do fází: klidová, zátěžová, regenerační.  
`ax.axvspan(x_start, x_end, alpha=..., color=..., label=...)` zakreslí barevný pás
do pozadí grafu – tím vizuálně „segmentuje" průběh signálu bez přepisování dat.
"""),

    code("""\
fazes = [(0,  10, "steelblue",       "Klid"),
         (10, 20, "goldenrod",       "Zahřívání"),
         (20, 40, "tomato",          "Aerobní"),
         (40, 50, "firebrick",       "Sprint"),
         (50, 60, "mediumseagreen",  "Regenerace")]

fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(tf_test.mean(axis=0), color="navy", linewidth=1.5)
for x0, x1, col, label in fazes:
    ax.axvspan(x0, x1, alpha=0.18, color=col, label=label)
ax.set_xlabel("Minuta")
ax.set_ylabel("TF (BPM)")
ax.set_title("Průměrná TF – segmentace fází zátěžového testu")
ax.legend(loc="upper right", fontsize=8)
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

**2. Segmentace fází**  
Do grafu z úkolu 1 přidej barevné pozadí pro každou fázi pomocí `ax.axvspan()`.  
Každá fáze musí mít vlastní barvu a popisek v legendě (viz ukázka výše).

**3. Boxplot per fáze**  
Pro každou fázi vezmi hodnoty všech pacientů a všech minut (`tf_test[:, 0:10].ravel()` atd.) a vykresli boxplot pěti skupin.  
Popisky: `["Klid", "Zahřívání", "Aerobní", "Sprint", "Regenerace"]`.

**4. Histogram – klid vs. sprint**  
Do jednoho histogramu vykresli hodnoty fáze Klid a fáze Sprint (oba `ravel()`).  
Přidej legendu a popsané osy.

**5. Segmentace snímku**  
`mri` máš již načtený z `mpl_data.npz`.  
Vytvoř binární masku prahováním: `maska = mri > PRÁH` (zkus práh 0.5).  
Zobraz vedle sebe původní obraz a masku pomocí `plt.subplots(1, 2)` + `imshow()`.  
Vypiš, kolik procent plochy tvoří pixely nad prahem a jaká je jejich průměrná intenzita.

**6.** Ke každému grafu přidej markdownovou buňku s jednou větou – co graf ukazuje.
"""),

    code("""\
# --- ZDE PIŠE STUDENT ---

# tf_test.shape == (30, 60)
# Fáze: Klid 0–9, Zahřívání 10–19, Aerobní 20–39, Sprint 40–49, Regenerace 50–59

# 1. Průměrná TF v čase (signál)


# 2. Segmentace fází (axvspan) – přidej do grafu výše


# 3. Boxplot – 5 fází
faze_data   = [tf_test[:, 0:10].ravel(), tf_test[:, 10:20].ravel(),
               tf_test[:, 20:40].ravel(), tf_test[:, 40:50].ravel(),
               tf_test[:, 50:60].ravel()]
faze_labels = ["Klid", "Zahřívání", "Aerobní", "Sprint", "Regenerace"]


# 4. Histogram – klid vs. sprint


# 5. Segmentace snímku
# mri je 2D numpy pole (64×64) – pixely nad prahem → True
PRAH = 0.5


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

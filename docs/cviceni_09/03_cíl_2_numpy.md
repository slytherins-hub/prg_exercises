# CÍL 2: NUMPY

> Táto stránka byla nahrazena interaktivním Jupyter Notebookem.
> Viz navigace → **Cíl 2 – NumPy**.


### 2.1 Proč numpy a ne Python seznam?

Python list zvládne uložit čísla a procházet je cyklem. Pro vědecké výpočty to ale nestačí – je pomalý a neúsporný.

Srovnání:

```python
import numpy as np
import time

n = 10_000_000
py_list = list(range(n))
np_array = np.arange(n)

# Python list
start = time.time()
result = [x * 2 for x in py_list]
print(f"Python list: {time.time() - start:.3f} s")

# NumPy
start = time.time()
result = np_array * 2
print(f"NumPy:       {time.time() - start:.3f} s")
```

NumPy bývá **10–100× rychlejší** na numerických operacích. Důvod: numpy pole (`ndarray`) uchovává data v **kompaktním bloku paměti stejného datového typu** a operace jsou implementované v C – bez Pythonové smyčky.

Navíc: místo `for` cyklu píšeš přímé matematické operace – kód je kratší a čitelnější.

---

### 2.2 Vytvoření pole

```python
import numpy as np

# Ze seznamu
a = np.array([1, 2, 3, 4, 5])
print(a)          # [1 2 3 4 5]
print(a.dtype)    # int64
print(a.shape)    # (5,)

# Číselná řada
b = np.arange(0, 10, 2)       # od 0 do 10 (vyjma), krok 2
print(b)  # [0 2 4 6 8]

# Rovnoměrně rozložené hodnoty – ideální pro osy
t = np.linspace(0, 1, 5)      # 5 hodnot od 0 do 1 včetně
print(t)  # [0.   0.25 0.5  0.75 1.  ]

# Nuly, jedničky, prázdné pole
print(np.zeros(4))             # [0. 0. 0. 0.]
print(np.ones((2, 3)))         # 2×3 matice jedniček
print(np.full((3, 3), 7))      # 3×3 matice sedmiček

# Náhodná data (biomedicínský kontext – šum)
noise = np.random.normal(0, 0.1, size=100)   # Gaussův šum, průměr 0, std 0.1
```

---

### 2.3 Tvar a indexování

```python
signal = np.array([0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1])

# Základní vlastnosti
print(signal.shape)    # (8,) – jednorozměrné pole délky 8
print(signal.ndim)     # 1
print(len(signal))     # 8

# Indexování – stejně jako u listů
print(signal[0])       # 0.5  – první prvek
print(signal[-1])      # 1.1  – poslední prvek

# Slicing – [od:do:krok]
print(signal[2:5])     # [1.8 0.9 2.1]  – prvky 2, 3, 4
print(signal[::2])     # každý druhý prvek

# 2D pole (matice)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.shape)         # (3, 3)
print(matrix[1, 2])         # 6  – řádek 1, sloupec 2
print(matrix[0, :])         # [1 2 3]  – celý první řádek
print(matrix[:, 1])         # [2 5 8]  – celý druhý sloupec
```

---

### 2.4 Matematické operace

Numpy operace jsou **vektorizované** – pracují na celém poli naráz, bez explicitního cyklu:

```python
a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([0.5, 0.5, 0.5, 0.5])

print(a + b)        # [1.5 2.5 3.5 4.5]
print(a * 2)        # [2.  4.  6.  8. ]
print(a ** 2)       # [ 1.  4.  9. 16.]
print(np.sqrt(a))   # [1.    1.414 1.732 2.   ]

# Agregace
print(a.sum())      # 10.0
print(a.mean())     # 2.5
print(a.std())      # směrodatná odchylka
print(a.min(), a.max())

# Podmínkové indexování – vrátí prvky splňující podmínku
print(a[a > 2])     # [3. 4.]
print(a[a > 2].mean())   # průměr jen z hodnot nad 2
```

---

### 2.5 Praktický příklad: simulace EKG pulzu

```python
import numpy as np

# Časová osa: 1 sekunda, 500 vzorků
t = np.linspace(0, 1, 500)

# Jednoduchý model QRS komplexu – součet sinusoid + šum
qrs = (
    1.5 * np.exp(-((t - 0.5) ** 2) / 0.001)    # R-vlna (ostrý peak)
    - 0.3 * np.exp(-((t - 0.47) ** 2) / 0.002)  # Q-vlna
    + 0.4 * np.exp(-((t - 0.55) ** 2) / 0.005)  # S-vlna
    + 0.1 * np.sin(2 * np.pi * 1.2 * t)         # P-vlna (velmi zjednodušeně)
    + np.random.normal(0, 0.05, size=len(t))     # šum senzoru
)

print(f"Délka signálu: {len(qrs)} vzorků")
print(f"Vzorkovací frekvence: 500 Hz")
print(f"Délka záznamu: {len(qrs)/500:.1f} s")
print(f"Průměrná hodnota: {qrs.mean():.3f}")
print(f"Maximum (R-peak): {qrs.max():.3f}")
```

---

**📝 ÚKOL: Práce s numpy polem**

Vytvoř nový Jupyter Notebook (`cviceni_09_numpy.ipynb`) a v něm:

1. Vytvoř 1D numpy pole reprezentující tepovou frekvenci pacienta za 10 minut – 10 hodnot v rozsahu 60–100 BPM. Použij `np.random.randint()`.
2. Vypiš průměr, minimum, maximum a směrodatnou odchylku.
3. Vyfiltruj hodnoty nad 80 BPM a vypiš, kolik jich je a jaký je jejich průměr.
4. Vytvoř 2D pole (matici) `5 × 3`, kde každý řádek je jedno měření a sloupce jsou: systolický tlak, diastolický tlak, tepová frekvence. Hodnoty vymysli nebo vygeneruj náhodně v realistickém rozsahu.
5. Vypiš průměrné hodnoty pro každý sloupec (`matrix.mean(axis=0)`).

---


# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 2: DĚDIČNOST

### 2.1 Proč dědičnost existuje

Třída `BiomedicalSignal` z cíle 1 funguje pro všechny signály. V praxi ale různé typy signálů potřebují různé věci navíc:

- **EKG** má specifický svod (lead I, II, III…) a vzorkovací frekvenci. Z délky záznamu a frekvence se dá spočítat trvání v sekundách.
- **Dechový signál** má přirozený rozsah a lze z něj odhadnout dechovou frekvenci.
- **Signál krevního tlaku** obvykle nese systolickou a diastolickou složku.

Mohl bys každou verzi udělat jako samostatnou třídu – zkopírovat `BiomedicalSignal` a přizpůsobit. Problém: pak máš tři kopie `mean_value()`, tři kopie `plot()`. Opravíš chybu v jedné a zbylé dvě zůstanou špatné. A přidání nové metody musíš udělat třikrát.

**Dědičnost** tohle řeší: napíšeš jednou společnou část do **rodičovské třídy** a každá **odvozená třída** si ji zdědí. Přidá jen to, co je pro ni specifické.

---

### 2.2 Jak to vypadá v kódu

Přejmenujeme základní verzi třídy na `Signal` – bude obsahovat jen to, co platí pro všechny typy:

```python
import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, name, values):
        self.name = name
        self.values = np.array(values, dtype=float)

    def mean_value(self):
        return np.mean(self.values)

    def min_value(self):
        return np.min(self.values)

    def max_value(self):
        return np.max(self.values)

    def plot(self):
        plt.figure(figsize=(10, 3))
        plt.plot(self.values, color="steelblue")
        plt.title(self.name)
        plt.xlabel("Vzorky")
        plt.ylabel("Amplituda")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
```

Teď vytvoříme odvozenou třídu `ECGSignal`, která zdědí vše ze `Signal` a přidá EKG-specifické věci:

```python
class ECGSignal(Signal):                         # (Signal) = dědí od Signal
    def __init__(self, name, values, sampling_rate, lead="II"):
        super().__init__(name, values)            # zavolá __init__ třídy Signal
        self.sampling_rate = sampling_rate
        self.lead = lead

    def duration_seconds(self):
        return len(self.values) / self.sampling_rate

    def __str__(self):
        return (
            f"[{self.name}] svod={self.lead}, "
            f"vzorkování={self.sampling_rate} Hz, "
            f"délka={self.duration_seconds():.3f} s, "
            f"průměr={self.mean_value():.2f}"
        )
```

Dvě klíčové věci:

- `ECGSignal(Signal)` – závorka říká, **od které třídy se dědí**.
- `super().__init__(name, values)` – **zavolá `__init__` rodičovské třídy**, aby se nastavily společné atributy `name` a `values`. Teprve pak přidáme vlastní `sampling_rate` a `lead`.

`super()` je odkaz na rodičovskou třídu. Díky tomu nekopíruješ kód – zavoláš ho z jednoho místa.

---

### 2.3 Jak to použít

```python
ekg = ECGSignal(
    "EKG pacienta 42",
    [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8],
    sampling_rate=500,
    lead="I",
)

# Metody zděděné ze Signal – ECGSignal je nikde nedefinuje, ale fungují:
print(ekg.mean_value())    # funguje díky dědičnosti
print(ekg.max_value())     # funguje díky dědičnosti
ekg.plot()                 # funguje díky dědičnosti

# Vlastní metody ECGSignal:
print(f"Délka záznamu: {ekg.duration_seconds():.3f} s")
print(f"Svod: {ekg.lead}")

# __str__ je redefinovaná, takže print vypíše podrobnou verzi:
print(ekg)
```

Výstup:

```
[EKG pacienta 42] svod=I, vzorkování=500 Hz, délka=0.020 s, průměr=1.19
```

Metody `mean_value()`, `max_value()`, `plot()` nikde v `ECGSignal` nejsou – jsou zděděné ze `Signal` a fungují automaticky pro všechny objekty odvozené třídy.

---

### 2.4 Kde dědičnost potkáš v knihovnách

Dědičnost sám od nuly psát nebudeš každý den – ale v knihovnách ji najdeš všude, a teď ji uvidíš:

- `Exception` → `ValueError`, `TypeError`, `IndexError` – všechny jsou odvozené třídy výjimek. Proto funguje `except Exception` jako záchrana pro všechny.
- `sklearn.base.BaseEstimator` → `LinearRegression`, `RandomForestClassifier` – všechny modely v scikit-learn dědí od společného základu, proto mají metody `fit()` a `predict()`.
- `matplotlib.axes.Axes` – základ pro všechny typy os; specializované typy grafů dědí od něj.

Kdykoli čteš dokumentaci a vidíš zápis `class LinearRegression(BaseEstimator, RegressorMixin)`, víš co to znamená: třída dědí od dvou rodičů a přebírá jejich chování.

> **💡 Poznámka:** V tomhle cíli nemusíš psát žádný kód. Jde jen o to pochopit princip, vidět, jak dědičnost vypadá, a rozpoznat ji v dokumentaci knihoven. V dalším cíli ji použiješ prakticky.

---

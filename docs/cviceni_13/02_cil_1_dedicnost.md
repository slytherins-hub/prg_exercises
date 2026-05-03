# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 1: DĚDIČNOST

Ve cvičení 11 sis napsal první vlastní třídu (`StudentsGrades`) a víš tedy, co je **třída**, **objekt**,
**atribut**, **metoda**, `__init__` a `self`. V tomhle cíli přidáš jeden nový, velmi užitečný koncept —
**dědičnost** — a v dalším cíli ho rovnou použiješ na úloze s DNA sekvencemi.

---

### 1.1 Proč dědičnost existuje

Představ si, že chceš pracovat s různými typy biomedicínských signálů — **EKG**, **dechový signál**,
**krevní tlak**. Všechny jsou to signály, takže mají mnoho společného:

- mají nějaký **název** a pole **hodnot**,
- umí spočítat průměr, minimum, maximum,
- dají se vykreslit do grafu.

Ale každý typ má i něco **navíc**:

- EKG má **svod** (lead I, II, III…) a **vzorkovací frekvenci** → z nich se dá spočítat délka záznamu v sekundách.
- Dechový signál má **dechovou frekvenci**.
- Krevní tlak má **systolickou** a **diastolickou** složku.

Bez dědičnosti bys měl dvě špatné možnosti:

1. **Všechno nacpat do jedné třídy** — ta je pak přeplácaná atributy, které se pro jeden typ nepoužívají.
2. **Udělat tři samostatné třídy** — pak máš `mean_value()` a `plot()` napsané **třikrát**. Opravíš chybu v jedné
   a zbylé dvě ji mají dál.

**Dědičnost** tohle řeší: společnou část napíšeš jednou do **rodičovské třídy**, a každá **odvozená třída**
si ji automaticky zdědí. Dopíše jen to, co je pro ni specifické.

---

### 1.2 Rodičovská třída `Signal`

Začneme obecnou třídou, která platí pro libovolný signál:

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

Na této třídě není nic nového — jen kombinuje to, co už umíš: `__init__`, `self`, metody, NumPy a matplotlib.

---

### 1.3 Odvozená třída `ECGSignal`

Teď vytvoříme specializovanou třídu `ECGSignal`, která zdědí vše ze `Signal` a přidá EKG-specifické věci:

```python
class ECGSignal(Signal):                              # ← závorka = dědíme od Signal
    def __init__(self, name, values, sampling_rate, lead="II"):
        super().__init__(name, values)                # ← zavolá __init__ rodiče
        self.sampling_rate = sampling_rate
        self.lead = lead

    def duration_seconds(self):
        return len(self.values) / self.sampling_rate

    def __str__(self):
        return (
            f"[{self.name}] svod={self.lead}, "
            f"vzorkování={self.sampling_rate} Hz, "
            f"délka={self.duration_seconds():.2f} s, "
            f"průměr={self.mean_value():.2f}"
        )
```

Dvě věci, které jsou nové a podstatné:

- **`class ECGSignal(Signal):`** — závorka za názvem říká, **od jaké třídy se dědí**. `ECGSignal` je **potomek**
  třídy `Signal` (říká se taky „rodič" a „dítě", nebo „nadtřída" a „podtřída").
- **`super().__init__(name, values)`** — **zavolá `__init__` rodiče**, aby se nastavily společné atributy
  (`name`, `values`). Teprve pak přidáme vlastní `sampling_rate` a `lead`. Bez `super()` by ses o nastavení
  `self.name` a `self.values` musel postarat ručně — zkopírovat ten kód. S `super()` nekopíruješ nic.

---

### 1.4 Jak to použít

```python
ekg = ECGSignal(
    "EKG pacienta 42",
    [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8],
    sampling_rate=500,
    lead="I",
)

# Metody zděděné ze Signal – ECGSignal je nikde nedefinuje, přesto fungují:
print(ekg.mean_value())    # 1.19
print(ekg.max_value())     # 2.1
ekg.plot()                 # vykreslí graf

# Vlastní metody ECGSignal:
print(f"Délka záznamu: {ekg.duration_seconds():.3f} s")
print(f"Svod: {ekg.lead}")

# __str__ je definovaná v ECGSignal, takže print používá tuhle verzi:
print(ekg)
# [EKG pacienta 42] svod=I, vzorkování=500 Hz, délka=0.02 s, průměr=1.19
```

Všimni si: `mean_value()`, `max_value()`, `plot()` **nikde v `ECGSignal` nejsou napsané** — pocházejí ze `Signal`
a fungují automaticky. Kdybys k `Signal` přidal další metodu, dostane ji `ECGSignal` zdarma.

---

### 1.5 Dědičnost v knihovnách kolem tebe

Vlastní hierarchii tříd si skoro nikdy nebudeš psát od nuly. Ale **dědičnost potkáš všude** v knihovnách,
které používáš — a teď ji v jejich dokumentaci poznáš:

- **Výjimky**: `ValueError`, `TypeError`, `IndexError` jsou všechny odvozené od `Exception`.
  Proto `except Exception:` odchytne všechny — potomci se chytí spolu s rodičem.
- **scikit-learn**: `LinearRegression`, `RandomForestClassifier` dědí od společného základu, a proto mají
  stejné metody `fit()` a `predict()`.
- **NumPy a matplotlib** jsou plné hierarchií tříd, které sis teď mohl všimnout.

---

#### 📝 ÚKOL: Dodělej třídy `Signal` a `ECGSignal`

1. Opiš si obě třídy z ukázek výše do souboru `signal.py` a ověř, že ukázka v sekci 1.4 funguje.

2. Přidej do `Signal` metodu `count_above(threshold)`, která vrátí **počet hodnot nad zadanou mezí**.
   Vyzkoušej ji na objektu `ekg` — kolik vzorků EKG přesahuje 1.0?

   > **Nápověda:** V NumPy stačí `np.sum(self.values > threshold)`.

3. Vytvoř druhou odvozenou třídu `RespirationSignal`, která dědí od `Signal` a přidá atribut `breathing_rate`
   (dechová frekvence v dechách za minutu). Žádné nové metody nejsou potřeba — jen `__init__` s `super()`
   a uložení atributu.

4. Vytvoř si jeden objekt `RespirationSignal` a ověř, že na něm funguje zděděná `plot()` i nové `breathing_rate`.

---

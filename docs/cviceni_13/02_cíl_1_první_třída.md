# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 1: PRVNÍ VLASTNÍ TŘÍDA

### 1.1 Jak třída vypadá

Začneme rovnou příkladem. Tady je třída pro biomedicínský signál – přečti si ji celou, pak si ji projdeme část po části:

```python
import numpy as np
import matplotlib.pyplot as plt


class BiomedicalSignal:
    def __init__(self, name, values, sampling_rate=1000):
        self.name = name
        self.values = np.array(values, dtype=float)
        self.sampling_rate = sampling_rate

    def mean_value(self):
        return np.mean(self.values)

    def max_value(self):
        return np.max(self.values)

    def plot(self):
        time = np.arange(len(self.values)) / self.sampling_rate
        plt.figure(figsize=(10, 3))
        plt.plot(time, self.values, color="steelblue")
        plt.title(self.name)
        plt.xlabel("Čas (s)")
        plt.ylabel("Amplituda")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
```

Tři věci, které si hned všimneš:

- Třída začíná klíčovým slovem `class` a názvem s velkým písmenem.
- Metody jsou odsazené uvnitř třídy – jsou její součástí.
- Každá metoda má jako první parametr `self` – za chvíli vysvětlíme proč.

---

### 1.2 Co je `__init__`

`__init__` je **speciální metoda** – Python ji zavolá automaticky pokaždé, když vytváříš nový objekt. Slouží k inicializaci objektu: nastaví jeho atributy na základě hodnot, které předáš při vytvoření.

Podívej se, co se stane při tomto řádku:

```python
ekg = BiomedicalSignal("EKG pacient 42", [0.5, 1.2, 1.8, 0.9, 2.1], 500)
```

Python udělá toto:

1. Vytvoří nový prázdný objekt třídy `BiomedicalSignal`.
2. Zavolá `__init__` a předá mu `name="EKG pacient 42"`, `values=[0.5, 1.2, 1.8, 0.9, 2.1]`, `sampling_rate=500`.
3. `__init__` nastaví atributy objektu pomocí `self.name = ...`, `self.values = ...`, `self.sampling_rate = ...`.
4. Výsledný objekt uloží do proměnné `ekg`.

`__init__` říká Pythonu, jak objekt „postavit" z dodaných dat. Dvojité podtržítka (`__`) jsou Pythonova konvence pro speciální metody, které má zavolat sám – ty je jen definuješ.

Parametr `sampling_rate=1000` v `__init__` má výchozí hodnotu. To znamená, že pokud ho nepředáš, automaticky se použije `1000`:

```python
ekg_auto = BiomedicalSignal("EKG", [0.5, 1.2, 1.8])  # sampling_rate bude 1000
ekg_500  = BiomedicalSignal("EKG", [0.5, 1.2, 1.8], 500)  # sampling_rate bude 500
```

---

### 1.3 Co je `self`

`self` je **odkaz na konkrétní objekt**, se kterým právě pracuješ. Díky `self` metoda ví, ke kterému objektu patří a ke kterým datům má přistupovat.

Zkus vytvořit dva různé objekty:

```python
ekg  = BiomedicalSignal("EKG",       [0.5, 1.2, 1.8, 0.9, 2.1], 500)
resp = BiomedicalSignal("Respirace", [0.3, 0.4, 0.5, 0.4, 0.6],  25)

print(ekg.mean_value())   # self = ekg  → počítá průměr z dat ekg
print(resp.mean_value())  # self = resp → počítá průměr z dat resp
```

Oba objekty sdílí **stejnou definici metody** `mean_value()`, ale díky `self` každý pracuje se svými vlastními daty.

`self` se píše jako první parametr každé metody, ale při volání ho **nikdy nepředáváš** – Python ho doplní sám. Zápis `ekg.mean_value()` je zkratka za `BiomedicalSignal.mean_value(ekg)`.

Zjednodušeně: `self.name` = „název tohoto konkrétního objektu". `self.values` = „hodnoty tohoto konkrétního objektu".

---

### 1.4 Jak to celé funguje dohromady

Tady je kompletní ukázka – vytvoření objektů a základní práce s nimi:

```python
ekg  = BiomedicalSignal("EKG",       [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1], 500)
resp = BiomedicalSignal("Respirace", [0.3, 0.4, 0.5, 0.4, 0.6, 0.5, 0.3, 0.4],  25)

# Atributy se čtou bez závorek
print(ekg.name)            # EKG
print(ekg.sampling_rate)   # 500
print(len(ekg.values))     # 8

# Metody se volají se závorkami
print(ekg.mean_value())    # průměr EKG
print(resp.max_value())    # maximum dechového signálu

# Vizualizace
ekg.plot()
```

> **💡 Tip:** Atributy čteš bez závorek (`ekg.name`), metody voláš se závorkami (`ekg.mean_value()`). Závorky = voláš funkci/metodu, bez závorek = čteš hodnotu.

---

### 1.5 Metoda `plot()` zblízka

Metoda `plot()` je praktická ukázka toho, proč se OOP hodí. Jako uživatel třídy nepotřebuješ vědět, jak přesně se vizualizace dělá – prostě zavoláš `ekg.plot()` a dostaneš graf. Složitost je schovaná uvnitř.

Interně metoda:

1. Sestaví osu času: `np.arange(len(self.values)) / self.sampling_rate` – každý vzorek přepočítá na sekundy.
2. Otevře nové okno matplotlib.
3. Vykreslí signál s popisky os a nadpisem.

Kdybys věc implementoval jako volnou funkci, vypadalo by to takhle:

```python
def plot_signal(name, values, sampling_rate):
    time = np.arange(len(values)) / sampling_rate
    ...

plot_signal(ekg_name, ekg_values, ekg_sampling_rate)  # ugh, tři argumenty
```

Method call `ekg.plot()` je přehlednější, protože objekt si potřebné věci pamatuje sám.

---

**📝 ÚKOL: Doplň a vyzkoušej třídu**

Začni s třídou `BiomedicalSignal` z ukázky výše. Postupně ji rozšiř:

1. Vytvoř alespoň 3 objekty s různými názvy a daty (klidně vymyšlená – EKG, dech, tepová frekvence, saturace…). Vypiš jejich průměry.

2. Přidej metodu `min_value()`, která vrátí minimální hodnotu signálu. Otestuj na svých objektech.

3. Přidej metodu `__str__()`, která vrátí čitelný popis objektu, například:

    ```
    [EKG] vzorkování=500 Hz, n=8, průměr=1.16
    ```

    Vyzkoušej ji voláním `print(ekg)` – Python `__str__` zavolá automaticky.

4. Přidej metodu `count_above(threshold)`, která vrátí počet hodnot nad zadanou mezí. Otestuj ji.

5. Rozšiř metodu `plot()` tak, aby vykreslila vodorovnou čáru na úrovni průměru (nápověda: `plt.axhline()`). Porovnej vizuálně, jak průměrná linie sedí na datech.

---

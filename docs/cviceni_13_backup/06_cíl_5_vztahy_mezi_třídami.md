# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 5: DĚDIČNOST

### 5.1 Kdy nestačí jedna třída

Zatím máš jednu třídu `BiomedicalSignal`, která funguje pro všechny typy signálů. Pro začátek je to v pohodě – ale v praxi se brzy ukáže, že různé typy signálů potřebují různé věci:

- **EKG** má svod (lead I, II, III…) a vzorkovací frekvenci – z délky záznamu a frekvence se dá spočítat trvání v sekundách,
- **dechový záznam** má jiný přirozený rozsah a dá se z něj odhadnout dechová frekvence,
- **krevní tlak** se měří jinak a typicky má systolickou i diastolickou složku.

Mohl by ses rozhodnout zkopírovat třídu `BiomedicalSignal` a kopii upravit. Ale to je problém – máš pak duplicitní kód: tři kopie `mean_value()`, `min_value()`, `normalize()`. Opravíš chybu v jedné a zbylé dvě zůstanou špatné.

**Dědičnost** tohle řeší elegantně: napíšeš jednou společnou část a každá odvozená třída ji zdědí. Přidá jen to, co je pro ni specifické.

### 5.2 Společná základní třída

Nejdřív vytvoříme třídu `Signal`, která obsahuje to, co je společné všem typům signálů:

```python
import numpy as np


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

    def __str__(self):
        return (
            f"[{self.name}] "
            f"n={len(self.values)}, "
            f"průměr={self.mean_value():.2f}, "
            f"rozsah=[{self.min_value():.2f}, {self.max_value():.2f}]"
        )
```

Tahle třída se nazývá **rodičovská třída** nebo **nadtřída** (*parent class* / *base class*). Je výchozí bod, od kterého ostatní třídy zdědí metody i atributy.

### 5.3 Odvozená třída – EKG signál

Teď vytvoříme `ECGSignal`, která dědí od `Signal` a přidává to, co je specifické pro EKG:

```python
class ECGSignal(Signal):
    def __init__(self, name, values, sampling_rate, lead="II"):
        super().__init__(name, values)  # zavolá __init__ rodičovské třídy
        self.sampling_rate = sampling_rate
        self.lead = lead

    def duration_seconds(self):
        return len(self.values) / self.sampling_rate

    def __str__(self):
        base = super().__str__()  # použije __str__ z Signal
        return f"{base}, svod={self.lead}, délka={self.duration_seconds():.2f} s"
```

Co se tu děje:

- `ECGSignal(Signal)` říká Pythonu: *tato třída dědí od `Signal`*,
- `super().__init__(name, values)` zavolá inicializaci rodičovské třídy – nastaví `self.name` a `self.values`,
- teprve pak přidáme vlastní atributy `sampling_rate` a `lead`,
- v `__str__` si půjčíme výstup ze `Signal` přes `super().__str__()` a rozšíříme ho o nové informace.

`super()` je odkaz na rodičovskou třídu. Díky tomu nekopíruješ kód – zavoláš ho z jednoho místa.

### 5.4 Druhá odvozená třída

Stejný přístup funguje pro dechový záznam:

```python
class RespirationSignal(Signal):
    def __init__(self, name, values, sampling_rate):
        super().__init__(name, values)
        self.sampling_rate = sampling_rate

    def duration_seconds(self):
        return len(self.values) / self.sampling_rate

    def __str__(self):
        base = super().__str__()
        return f"{base}, délka={self.duration_seconds():.2f} s"
```

Metody `mean_value()`, `min_value()`, `max_value()` – ty `RespirationSignal` vůbec nedefinuje. Zdědí je ze `Signal` automaticky.

### 5.5 Jak to vypadá v praxi

```python
ekg = ECGSignal(
    "EKG pacienta #42",
    [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8],
    sampling_rate=500,
    lead="I",
)
resp = RespirationSignal(
    "Dech pacienta #42",
    [0.3, 0.4, 0.5, 0.4, 0.6, 0.5, 0.3, 0.4],
    sampling_rate=25,
)

print(ekg)
print(resp)
print()

# Klíčová výhoda: oba sdílí metody ze Signal
for signal in [ekg, resp]:
    print(f"{signal.name}: průměr = {signal.mean_value():.2f}")
```

Výstup:

```
[EKG pacienta #42] n=10, průměr=1.19, rozsah=[0.50, 2.10], svod=I, délka=0.02 s
[Dech pacienta #42] n=8, průměr=0.43, rozsah=[0.30, 0.60], délka=0.32 s

EKG pacienta #42: průměr = 1.19
Dech pacienta #42: průměr = 0.43
```

Funkce `mean_value()` napsaná jednou v `Signal` funguje pro oba typy objektů – to je hlavní výhoda dědičnosti.

### 5.6 Kontrola typu: `isinstance()`

Python umožňuje zjistit, jestli je objekt instancí určité třídy:

```python
print(isinstance(ekg, ECGSignal))   # True
print(isinstance(ekg, Signal))      # True – ECGSignal dědí od Signal
print(isinstance(resp, ECGSignal))  # False
print(isinstance(resp, Signal))     # True
```

`ECGSignal` je zároveň instancí `ECGSignal` i `Signal`. To umožňuje psát funkce, které přijmou libovolný typ signálu – stačí, aby dědil od `Signal`.

> **💡 Tip:** `isinstance()` je bezpečnější než `type(obj) == ECGSignal`. Ten druhý způsob vrátí `False` pro odvozené třídy – `isinstance()` správně rozpozná celou hierarchii.

### 5.7 Kdy dědičnost použít a kdy ne

Dědičnost se hodí, když:

- více tříd sdílí velkou část chování,
- odvozená třída je *specializací* rodičovské (EKG *je* typ signálu),
- chceš zabránit duplicitnímu kódu.

Nemá smysl ji používat, když třídy spolu nesouvisejí nebo jedna prostě drží druhou jako atribut. V takovém případě je lepší **kompozice** – objekt jednoduše obsahuje v atributu jiný objekt. Třeba třída `PatientRecord` může mít atribut `signals`, což je seznam objektů `Signal`. Žádná dědičnost, jen přirozené skládání dat.

**📝 ÚKOL: Hierarchie signálů**

1. Vytvoř základní třídu `Signal` s atributy `name` a `values` a metodami `mean_value()`, `min_value()`, `max_value()`, `__str__()`.
2. Odvoď z ní třídu `ECGSignal` s atributy `sampling_rate` a `lead`. Přidej metodu `duration_seconds()` a přepiš `__str__()`.
3. Odvoď z `Signal` ještě jednu vlastní třídu – např. `BloodPressureSignal`, `TemperatureSignal` nebo jinou. Přidej k ní aspoň jeden vlastní atribut a jednu vlastní metodu.
4. Vytvoř alespoň 2 objekty každého odvozeného typu.
5. Ulož je všechny do jednoho seznamu a projdi ho cyklem – pro každý signál vypiš průměr (metoda zděděná ze `Signal` funguje pro všechny).
6. Ověř pomocí `isinstance()`, že objekt `ECGSignal` je instancí i třídy `Signal`.

> **💡 Tip:** V každé odvozené třídě volej `super().__init__(name, values)` jako první věc v `__init__`. Bez toho objekty nebudou mít atributy `name` a `values` zděděné ze `Signal`.

---
# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 2: TŘÍDY, ATRIBUTY A METODY

### 2.1 Základní pojmy

Než se pustíš do kódu, je dobré ujasnit si čtyři základní pojmy:

- **třída** je šablona nebo návrh, podle kterého vytváříš objekty,
- **objekt** je konkrétní instance třídy,
- **atribut** je hodnota uložená v objektu,
- **metoda** je funkce, která patří objektu a pracuje s jeho daty.

Na jednoduchém příkladu:

- třída může být `BiomedicalSignal`,
- objekt může být konkrétní signál `ekg_signal`,
- atribut může být `name` nebo `values`,
- metoda může být třeba `mean_value()`.

### 2.2 Jak vypadá první smysluplná třída

První smysluplnou třídu si ukážeme na biomedicínském signálu. Cíl ale není naučit se „třídu pro EKG“, ale pochopit obecný princip: objekt má atributy a metody.

Jednodušší, ale už prakticky použitelná verze třídy může vypadat třeba takto:

```python
import numpy as np


class BiomedicalSignal:
    def __init__(self, name, values):
        self.name = name
        self.values = np.array(values, dtype=float)

    def mean_value(self):
        return np.mean(self.values)

    def count_above(self, threshold):
        return np.sum(self.values > threshold)
```

Tahle třída už obsahuje:

- název signálu,
- hodnoty signálu jako `numpy` pole,
- metodu bez vstupního parametru navíc,
- metodu, která naopak vstupní parametr potřebuje.

### 2.3 Co je `__init__`

Metoda `__init__` je speciální metoda, která se zavolá automaticky ve chvíli, kdy vytváříš nový objekt.

Například když napíšeš:

```python
ekg_signal = BiomedicalSignal("EKG", [0.12, 0.15, 0.11, 0.52])
```

Python ve skutečnosti použije metodu `__init__` a dosadí do ní hodnoty:

- `name = "EKG"`
- `values = [0.12, 0.15, 0.11, 0.52]`

Uvnitř `__init__` se tyto hodnoty uloží do objektu přes `self`.

To znamená:

- `self.name` je název konkrétního objektu,
- `self.values` jsou data konkrétního objektu.

> **💡 Poznámka:** `self` není klíčové slovo jako `if` nebo `for`, ale je to zavedený způsob, jak v Pythonu odkazujeme na právě vytvářený nebo používaný objekt.

### 2.4 Jak to celé funguje dohromady

Třída je šablona. Objekt je konkrétní instance této šablony.

Například:

```python
ekg_signal = BiomedicalSignal("EKG", [0.12, 0.15, 0.11, 0.52])

print(ekg_signal.name)
print(ekg_signal.mean_value())
print(ekg_signal.count_above(0.2))
```

V tomhle příkladu se děje následující:

1. vytvoří se objekt `ekg_signal`,
2. do atributů objektu se uloží název a data,
3. při volání `mean_value()` objekt použije svoje vlastní uložená data,
4. při volání `count_above(0.2)` objekt opět pracuje se svým `self.values`, ale navíc použije i zadaný vstupní parametr `0.2`.

To je hlavní myšlenka OOP: objekt si nese svoje data a zároveň umí nabídnout operace, které k těm datům patří.

### 2.5 Dvě ukázkové metody

V ukázce jsou schválně jen dvě jednoduché metody:

- `mean_value()`
- `count_above(threshold)`

První metoda nemá žádný další vstup kromě `self`:

```python
def mean_value(self):
    return np.mean(self.values)
```

Vrátí tedy průměr přímo z dat, která už objekt obsahuje.

Druhá metoda má kromě `self` ještě jeden vstupní parametr:

```python
def count_above(self, threshold):
    return np.sum(self.values > threshold)
```

Tahle metoda spočítá, kolik hodnot v signálu je větších než zadaný práh.

### 2.6 Praktický kontext

Tady jsou příklady, kde by se podobná třída hodila:

- krátký úsek EKG,
- fotopletysmografický signál,
- jednoduchý dechový signál,
- časovou řadu saturace kyslíku.

**📝 ÚKOL: Rozšíření třídy pro signál**

1. Rozšiř třídu `BiomedicalSignal` o atribut `sampling_rate`.
2. Přidej ještě jeden vlastní atribut podle sebe, například `unit`, `patient_id` nebo `signal_type`.
3. Přidej metodu `normalize(min_value=0, max_value=1)`, která vrátí signál přepočítaný do zadaného intervalu.
4. Přidej ještě jednu jednoduchou metodu podle sebe, například `min_value()`, `value_range()` nebo `length()`.
5. Vytvoř alespoň 2 různé objekty signálu a nové metody na nich vyzkoušej.

> **💡 Tip:** Tohle je přesně typ situace, kde OOP pomáhá. Operace, které přirozeně patří k datům, často dávají větší smysl jako metody objektu než jako náhodně rozházené funkce bez kontextu.

---
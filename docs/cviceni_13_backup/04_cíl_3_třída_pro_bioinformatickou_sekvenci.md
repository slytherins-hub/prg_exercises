# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 3: ROZŠIŘUJEME TŘÍDU

### 3.1 Třída roste spolu s potřebami

V cíli 2 jsi napsal třídu `BiomedicalSignal` s dvěma základními metodami. To byl dobrý začátek, ale zatím toho třída moc neumí. V reálném projektu se potřeby postupně mění – přidáš zpracování dat, výpis do konzole, normalizaci, detekci anomálií. A to je přesně práce s třídou: **rozšiřuješ ji postupně**, přesně jak rostou požadavky.

To je jedna z velkých výhod OOP oproti volným funkcím. Přidáš metodu do jednoho místa a okamžitě ji mají všechny objekty dané třídy k dispozici – bez toho, abys přepisoval volání po celém kódu.

V tomhle cíli přidáme do `BiomedicalSignal`:

- metody pro základní statistiku (minimum, maximum),
- metodu pro normalizaci dat do libovolného rozsahu,
- speciální metodu `__str__`, která říká Pythonu, jak objekt vypsat.

### 3.2 Přidáváme metody krok za krokem

Tady je rozšířená verze třídy z cíle 2:

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

    def min_value(self):
        return np.min(self.values)

    def max_value(self):
        return np.max(self.values)

    def normalize(self, min_out=0.0, max_out=1.0):
        min_val = np.min(self.values)
        max_val = np.max(self.values)
        if max_val == min_val:
            return np.full_like(self.values, min_out)
        scale = (max_out - min_out) / (max_val - min_val)
        return min_out + scale * (self.values - min_val)
```

Každá metoda je krátká a dělá jednu věc. To není jen estetika – kratší metody jsou snadněji testovatelné a ostatní vývojáři (nebo ty o měsíc později) je snáze pochopí.

Metoda `normalize()` má výchozí hodnoty parametrů – pokud ji zavoláš bez argumentů, normalizuje do rozsahu 0–1. Ale `signal.normalize(-1, 1)` vrátí rozsah −1 až 1. Je to pohodlná konvence, která šetří psaní v nejčastějším případě a zároveň zachovává flexibilitu.

### 3.3 Speciální metoda `__str__`

Python má speciální metody se dvěma podtržítky na začátku a konci – říká se jim **dunder metody** (z anglického *double underscore*). Volá je Python sám v určitých situacích, ty je jen definuješ.

Nejpraktičtější ze všech je `__str__`. Python ji zavolá vždy, když chceš objekt převést na text – třeba přes `print()` nebo `str()`.

Bez `__str__` dostaneš nevypovídající výstup:

```
<__main__.BiomedicalSignal object at 0x0000024F3A1B2C50>
```

S `__str__` si sám rozhodneš, co se zobrazí:

```python
    def __str__(self):
        return (
            f"[{self.name}] "
            f"n={len(self.values)}, "
            f"průměr={self.mean_value():.2f}, "
            f"rozsah=[{self.min_value():.2f}, {self.max_value():.2f}]"
        )
```

Teď `print(signal)` vrátí okamžitě srozumitelný výstup:

```
[EKG] n=10, průměr=1.19, rozsah=[0.50, 2.10]
```

Hodí se to při ladění, generování reportů nebo kdykoli chceš rychle vidět, co objekt obsahuje – bez toho, abys ručně přistupoval k atributům.

### 3.4 Jak to vypadá v praxi

```python
ekg = BiomedicalSignal("EKG", [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7, 1.1, 1.3, 0.8])
resp = BiomedicalSignal("Respirace", [0.3, 0.4, 0.5, 0.4, 0.6, 0.5, 0.3, 0.4])

print(ekg)
print(resp)
print()
print(f"Normalizovaný EKG (0–1):   {ekg.normalize()}")
print(f"Normalizovaný EKG (−1–1):  {ekg.normalize(-1, 1)}")
```

Výstup:

```
[EKG] n=10, průměr=1.19, rozsah=[0.50, 2.10]
[Respirace] n=8, průměr=0.43, rozsah=[0.30, 0.60]

Normalizovaný EKG (0–1):   [0.    0.389 0.722 0.222 1.    0.556 0.111 0.333 0.444 0.167]
Normalizovaný EKG (−1–1):  [-1.   -0.222  0.444 -0.556  1.    0.111 -0.778 -0.333 -0.111 -0.667]
```

> **💡 Tip:** Metoda `normalize()` nemění `self.values`. Vrací nové `numpy` pole – původní data zůstávají nedotčená. Je to dobrý zvyk: metody by neměly tiše přepisovat data, pokud to není jejich explicitní úkol. Neočekávané vedlejší efekty jsou zákeřný zdroj chyb.

**📝 ÚKOL: Rozšíření vlastní třídy**

Vezmi třídu, kterou jsi vytvořil v cíli 2, a rozšíř ji:

1. Přidej metody `min_value()` a `max_value()`.
2. Přidej metodu `normalize(min_out=0.0, max_out=1.0)`.
3. Přidej metodu `__str__`, která vrátí čitelný výstup: název, počet vzorků, průměr, rozsah.
4. Vyzkoušej `print()` na alespoň 2 objektech a ověř, že výstup je smysluplný.
5. Vyzkoušej `normalize()` s různými rozsahy výstupu.

---
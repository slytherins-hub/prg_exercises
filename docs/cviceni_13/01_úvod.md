# CVIČENÍ 13: OOP

Algoritmizace a programování

## ÚVOD

### Co se v tomto cvičení naučíš?

1. Co je OOP a proč Python objektový jazyk vůbec je.
2. K čemu se OOP hodí – a kdy ho nepotřebuješ.
3. Jak navrhnout vlastní třídu s atributy a metodami.
4. Co jsou `__init__` a `self` a jak to celé funguje.
5. Co je dědičnost a proč se vyplatí o ní vědět.
6. Jak navrhnout a otestovat třídu pro biologické sekvence.

---

### Python je objektově orientovaný jazyk

Tohle se říká v každém kurzu Pythonu, ale málokdy se vysvětlí, co to **ve skutečnosti znamená pro tebe**.

V Pythonu je **úplně všechno objekt**. Číslo `42` je objekt třídy `int`. Řetězec `"ACGT"` je objekt třídy `str`. Seznam `[1, 2, 3]` je objekt třídy `list`. Dokonce i funkce je objekt.

Kdykoli voláš metodu, už s OOP pracuješ:

```python
"ACGT".upper()        # metoda upper() na objektu třídy str
[1, 2, 3].append(4)   # metoda append() na objektu třídy list
```

Knihovny, které v tomto oboru používáš, jsou celé postavené na třídách:

```python
import numpy as np

arr = np.array([1, 2, 3])   # arr je objekt třídy ndarray
print(arr.mean())            # mean() je metoda objektu
print(arr.shape)             # shape je atribut objektu

import matplotlib.pyplot as plt

fig, ax = plt.subplots()     # fig a ax jsou objekty
ax.plot([1, 2, 3])           # plot() je metoda objektu Axes
ax.set_title("Signál")       # set_title() je metoda objektu Axes
```

OOP je kolem tebe pořád – i kdybys nikdy vlastní třídu nenapsal. Proto se mu vyplatí rozumět.

---

### K čemu je OOP dobré?

Představ si, že zpracováváš biomedicínský signál – třeba krátký úsek EKG. Přístup **bez OOP** vypadá nějak takto:

```python
# Přístup bez OOP – data a operace jsou oddělené
signal_name = "EKG_pacient_42"
signal_values = [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7]
signal_sampling_rate = 500

def signal_mean(values):
    return sum(values) / len(values)

def signal_plot(name, values, sampling_rate):
    ...

print(signal_mean(signal_values))
signal_plot(signal_name, signal_values, signal_sampling_rate)
```

Vše funguje. Ale co když máš 10 pacientů? Najednou máš 30 proměnných (`signal_name_1`, `signal_values_1`, `signal_name_2`, ...) a do každé funkce musíš ručně předávat správnou kombinaci. Velká šance na záměnu.

S **OOP** patří data a operace nad nimi k sobě – do jednoho objektu:

```python
# Přístup s OOP – vše na jednom místě
ekg = BiomedicalSignal("EKG_pacient_42", [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7], 500)

print(ekg.mean_value())   # průměr tohoto signálu
ekg.plot()                # graf tohoto signálu
```

A pro 10 pacientů:

```python
pacienti = [
    BiomedicalSignal("EKG_01", [...], 500),
    BiomedicalSignal("EKG_02", [...], 500),
    # ...
]

for pacient in pacienti:
    print(pacient.mean_value())  # každý objekt umí sám spočítat svůj průměr
```

Čistý kód, minimum šancí na záměnu dat.

---

### Základní pojmy

Čtyři pojmy, které potřebuješ znát:

| Pojem | Vysvětlení | Příklad |
|-------|-----------|---------|
| **třída** | Šablona (plán) pro vytváření objektů | `BiomedicalSignal` |
| **objekt** | Konkrétní instance třídy | `ekg = BiomedicalSignal(...)` |
| **atribut** | Hodnota uložená v objektu | `ekg.name`, `ekg.values` |
| **metoda** | Funkce patřící objektu, pracuje s jeho daty | `ekg.mean_value()`, `ekg.plot()` |

> **💡 Poznámka:** Třída je jako formulář pacienta. Atributy jsou políčka ve formuláři (jméno, hodnoty měření, frekvence). Objekt je jeden konkrétně vyplněný formulář. Metody jsou akce, které s vyplněným formulářem můžeš provést – vypočítat průměr, vykreslit graf.

---

### Musím psát OOP kód?

Krátká odpověď: **ne vždy**.

Pro jednoduché skripty – spočítat BMI, zpracovat jeden soubor, projít seznam hodnot – funkce a proměnné úplně stačí. Složité OOP struktury tam, kde to není potřeba, kód zbytečně komplikují.

**Ale rozumět OOP potřebuješ**, a to ze dvou důvodů:

1. **Používáš cizí třídy každý den.** `numpy`, `pandas`, `matplotlib`, `scikit-learn` – celé to jsou knihovny plné tříd a objektů. Abys věděl, proč `ndarray.reshape()` funguje jinak než volná funkce, nebo proč `ax.set_title()` a `plt.title()` dělají různé věci, musíš chápat, co je objekt a co je metoda.

2. **Jakmile projekt přeroste pár desítek řádků**, OOP výrazně pomůže udržet přehled – zvláště pokud pracuješ s komplexnějšími strukturami dat.

---

# CVIČENÍ 10B: ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 1: SELECTION SORT

### 1.1 Trocha teorie k řazení

**Řazení (sorting)** je úloha, ve které chceš uspořádat hodnoty do správného pořadí — typicky od nejmenšího k největšímu. Je to jedna z nejčastějších operací, kterou v praxi potkáš:

- výsledky ve sportovním závodě od nejrychlejšího k nejpomalejšímu,
- studenti seřazení podle bodů v testu,
- soubory v průzkumníku seřazené podle data změny,
- data připravená pro **binární vyhledávání** (viz minulé cvičení).

Řadicích algoritmů existuje celá řada. Liší se rychlostí, paměťovými nároky a tím, jak se chovají při stejných hodnotách. Rozdělují se podle několika kritérií; pro začátek ti stačí jedno:

- **Stabilní algoritmus** zachovává relativní pořadí prvků se stejnou hodnotou (stejným klíčem řazení).
- **Nestabilní algoritmus** tuto vlastnost nezaručuje.

Když řadíš čistá čísla, je ti stabilita jedno — dvě stejné sedmičky se od sebe neliší. Důležitá je ve chvíli, kdy se stejným klíčem pracují různé objekty, které od sebe umíš odlišit (třeba záznamy studentů se stejným počtem bodů).

V dnešním cvičení si ukážeme dva jednoduché klasické algoritmy: **Selection Sort** (nestabilní) a **Bubble Sort** (stabilní). Oba mají stejnou asymptotickou složitost, ale každý k řazení přistupuje jinak.

---

### 1.2 Princip Selection Sortu

Selection Sort patří mezi jednoduché **nestabilní** řadicí algoritmy. Jeho výhodou je nízká paměťová náročnost — pracuje přímo v původním seznamu, bez pomocných kopií.

Základní princip algoritmu pro vzestupné seřazení:

1. Najdi nejmenší prvek v seznamu.
2. Prohoď ho s prvním prvkem.
3. Pak najdi druhý nejmenší prvek a prohoď ho s druhým prvkem.
4. Opakuj, dokud nejsou všechny prvky na správném místě.

![Selection Sort](../assets/cviceni_11/10_selection_sort_visualization.png)

Všimni si, že v každém průchodu algoritmus prohodí dva prvky — nalezené minimum a prvek na aktuální pozici. Takové prohození může přeskočit pořadí dvou stejných hodnot, a proto je algoritmus **nestabilní**.

> **💡 Nápověda:** Prohození dvou prvků seznamu jde v Pythonu zapsat velmi elegantně bez pomocné proměnné:
>
> ```python
> my_list[1], my_list[3] = my_list[3], my_list[1]
> ```

---

### 1.3 Testovací data: generátor náhodných čísel

Než se pustíš do implementace, připrav si způsob, jak vyrobit testovací seznam. Ručně psát pokaždé jiné hodnoty je otrava — Python má přímo modul `random`, kterým si vygeneruješ libovolně dlouhý seznam čísel v zadaném rozsahu.

```python
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
```

Použití:

```python
values = random_numbers(10)              # 10 čísel v rozsahu 0–100
print(values)   # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)   # 5 čísel v rozsahu 0–20
```

> **💡 Tip:** Pokud chceš, aby se ti při každém spuštění vygenerovala **stejná** posloupnost (třeba kvůli opakovatelnému testu), přidej na začátek `random.seed(42)` nebo jiné pevné číslo.

Funkci `random_numbers()` použiješ jak pro testování Selection Sortu, tak pro Bubble Sort v další části.

---

### 1.4 Úkol: implementace `selection_sort()`

**📝 ÚKOL: Selection Sort**

1. Vytvoř modul `sorting.py` a zkopíruj do něj funkci `random_numbers()` z předchozí sekce.
2. Do stejného souboru doplň funkci `selection_sort()`.
3. Funkce má jeden vstupní parametr: libovolně dlouhý seznam čísel.
4. Funkce vrátí **nový** vzestupně seřazený seznam. Původní seznam nechává beze změny.
5. Volání funkce ověř v `main()` — třeba na krátkém seznamu `[5, 1, 4, 2, 8]` a na náhodně vygenerovaném seznamu 20 čísel.

> **💡 Tip:** Abys nechal původní seznam beze změny, na začátku funkce si vytvoř jeho kopii — například `numbers = numbers[:]` nebo `numbers = list(numbers)`.

---

### 1.5 Stručně ke složitosti

| Nejlepší scénář | Nejhorší scénář |
| --- | --- |
| $O(n^2)$ | $O(n^2)$ |

Selection Sort je **vždy** $O(n^2)$ — nedokáže využít toho, že je seznam už skoro seřazený. I tak musí pro každou pozici projít zbytek seznamu a najít minimum. V další části si ukážeme Bubble Sort, který se v některých případech chová lépe.

---

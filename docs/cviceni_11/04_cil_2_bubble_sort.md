# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 2: BUBBLE SORT

### 2.1 Bubble Sort - princip

Bubble Sort patří mezi nejjednodušší **stabilní** řadicí algoritmy. Pracuje na principu „probublávání": opakovaně 
porovnává dvojice sousedních prvků a prohazuje je, pokud jsou ve špatném pořadí. Největší hodnoty se tak postupně
„probublají" na konec seznamu.

Základní princip algoritmu pro vzestupné seřazení:

1. Začni na první pozici.
2. Porovnej dva po sobě jdoucí prvky.
3. Pokud je první větší než druhý, prohoď jejich pořadí.
4. Posuň se o jednu pozici dál.
5. Po jednom průchodu se největší hodnota dostane na konec.
6. Opakuj, dokud není seřazená celá sekvence.

![Bubble Sort](../assets/cviceni_11/11_bubble_sort_visualization.png)

> **Tip:** U Bubble Sortu se vyplatí vzít si papír a projít si pár kroků ručně — hned pak vidíš, proč se největší 
> hodnota každou iterací „probublává" na konec seznamu.

---

#### ÚKOL: Bubble Sort - implementace

1. Do modulu `sorting.py` (který už obsahuje `selection_sort()` a `random_numbers()`) doplň funkci `bubble_sort()`.
2. Funkce má jeden vstupní parametr: libovolně dlouhý seznam čísel.
3. Funkce vrátí **nový** vzestupně seřazený seznam. Původní seznam nechává beze změny.
4. Volání funkce ověř v `main()` — třeba na krátkém seznamu `[5, 1, 4, 2, 8]` a na náhodně vygenerovaném seznamu 20-ti čísel (`random_numbers(20)`).

> **Nápověda:** Algoritmus nemusí znovu kontrolovat prvky, které už jsou na správném místě — konec seznamu zůstává
> po každém průchodu seřazený. Tomu by mělo odpovídat nastavení řídicích cyklů.

> **Tip:** Abys nechal původní seznam beze změny, na začátku funkce si vytvoř jeho kopii — například
> `numbers = numbers[:]`, `numbers = list(numbers)` nebo `numbers = numbers.copy()`.

---

### 2.2 Bubble Sort - analýza složitosti

Bubble Sort používá dva do sebe vnořené průchody přes seznam — pro seznam o délce $n$ to v nejhorším případě znamená
zhruba $n \cdot n$ porovnání. Časová složitost proto roste s kvadrátem velikosti vstupu.

|                 | Kdy nastane? | Asymptotická složitost |
|-----------------|--------------|------------------------|
| Nejlepší scénář |              |                        |
| Nejhorší scénář |              |                        |

V praxi se Bubble Sort používá jen zřídka. Jakmile roste objem dat, jeho výkon rychle klesá. Pro skutečnou práci
se používají rychlejší algoritmy — v další části uvidíš, jak to Python řeší interně.

> **Poznámka:** Bubble Sort je schopný dosáhnout složitosti $O(n)$ pro nejlepší scénář, pokud je vstupní seznam 
> už seřazený a algoritmus umí po průchodu bez jediného prohození řazení ukončit.

---

### 2.3 Bubble Sort - vizualizace

Vizualizaci si můžeš udělat velmi jednoduše pomocí sloupcového grafu v `matplotlib`. Nemusíš kvůli tomu přepisovat celý 
algoritmus — stačí do hotového Bubble Sortu vložit pár řádků, které po každém kroku překreslí aktuální stav seznamu.

#### ÚKOL: Vizualizace Bubble Sortu

1. Na začátek souboru přidej:
    ```python
    import matplotlib.pyplot as plt
    ```
2. Před začátek řazení:
    ```python
    plt.ion()
    plt.show()
    ```
3. Blok níže vlož **dovnitř vnitřního cyklu**, tedy tam, kde právě porovnáváš prvky:
    ```python
    index_highlight1 = j
    index_highlight2 = j + 1
    colors = ["steelblue"] * len(values)
    colors[index_highlight1] = "tomato"
    colors[index_highlight2] = "tomato"
    plt.clf()
    plt.bar(range(len(values)), values, color=colors)
    plt.title("Bubble Sort")
    plt.pause(0.1)
    ```
4. Po skončení řazení přidej:
    ```python
    plt.ioff()
    plt.show()
    ```
5. Spusť svůj kód a sleduj, jak se seznam postupně řadí.
   > **Tip:** Na začátku si zkus krátký seznam, třeba 8 až 10 hodnot (použij například `random_numbers(10)`). 
   > U delších seznamů už bývá animace pomalejší a méně přehledná.

**Co jednotlivé řádky dělají:**

1. `plt.ion()` zapne interaktivní režim, který umožňuje průběžné aktualizace grafu.
2. `plt.show()` zobrazí prázdný graf, který budeš později aktualizovat.
3. `index_highlight1 = j` a `index_highlight2 = j + 1` nastaví indexy právě porovnávaných prvků. 
   > Proměnná `j` je index vnitřního cyklu, který prochází seznam a porovnává sousední prvky.
4. `colors = ["steelblue"] * len(values)` vytvoří seznam barev pro všechny sloupce.
   > Proměnná `values` je seznam, který řadíš.
5. `colors[index_highlight1] = "tomato"` obarví první zvýrazněný sloupec červeně.
6. `colors[index_highlight2] = "tomato"` obarví druhý zvýrazněný sloupec červeně.
7. `plt.clf()` smaže předchozí obrázek, aby se vykreslil nový stav.
8. `plt.bar(...)` vykreslí aktuální hodnoty jako sloupce.
9. `plt.title(...)` nastaví název grafu.
10. `plt.pause(0.1)` na chvíli zastaví program, aby byla změna v grafu vidět.
11. `plt.ioff()` vypne interaktivní režim, aby se graf už dál neaktualizoval.
12. `plt.show()` zobrazí finální graf se seřazenými hodnotami.

---

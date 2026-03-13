# CVIČENÍ 11: ŘADICÍ ALGORITMY

Algoritmizace a programování

## CÍL 1: SELECTION SORT

Selection Sort patří mezi jednoduché **nestabilní** řadicí algoritmy. Jeho výhodou je hlavně nízká paměťová náročnost, protože pracuje přímo v původním seznamu.

### 1.3 Princip algoritmu

Základní princip algoritmu pro vzestupné seřazení:

1. Najdi nejmenší prvek v seznamu.
2. Prohoď ho s prvním prvkem.
3. Pak najdi druhý nejmenší prvek a prohoď ho s druhým prvkem.
4. Opakuj, dokud nejsou všechny prvky na správném místě.

![Selection Sort](../assets/cviceni_11/10_selection_sort_visualization.png)

**📝 ÚKOL: Načtení dat z CSV**

1. Do modulu `sorting.py` implementuj funkci `read_data()`.
2. Funkce bude mít jeden vstupní parametr: název CSV souboru.
3. Pomocí modulu `csv` načti CSV soubor ve formě slovníku.
4. Klíče slovníku budou názvy sloupců a hodnoty budou čísla uložená v příslušném sloupci.
5. Funkce vrátí slovník všech čísel uložených pod jednotlivými klíči.
6. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
7. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

**📝 ÚKOL: Selection Sort**

1. Do modulu `sorting.py` implementuj funkci `selection_sort()`.
2. Funkce bude mít jeden vstupní parametr: libovolně dlouhý seznam celých čísel.
3. Funkce vrátí vzestupně seřazený seznam.
4. Jako vstup použij některou z číselných řad načtených v předešlém úkolu.
5. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
6. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

> **💡 Nápověda:** Prohození dvou prvků seznamu jde v Pythonu zapsat velmi jednoduše:
>
> ```python
> my_list[1], my_list[3] = my_list[3], my_list[1]
> ```

**📝 ÚKOL: Rozšíření funkce**

1. Rozšiř rozhraní funkce `selection_sort()` o nepovinný parametr `direction`.
2. Parametr rozhodne, jestli bude posloupnost seřazena vzestupně nebo sestupně.
3. Uprav algoritmus tak, aby uměl vracet obě varianty.
4. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

### 1.4 Analýza algoritmu Selection Sort

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce.

Zjisti také v dokumentaci, jaká je asymptotická složitost metod `insert()` a `pop()`. Jak by se změnila asymptotická složitost algoritmu, kdybys prohazování prvků realizoval pomocí těchto metod?

| Případ | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| vzestupné seřazení posloupnosti |  |  |
| sestupné seřazení posloupnosti |  |  |

### 1.5 Jednoduchá vizualizace Selection Sortu

Vizualizaci můžeš udělat velmi jednoduše pomocí sloupcového grafu. Nemusíš kvůli tomu přepisovat celý algoritmus. Stačí do už hotového Selection Sortu vložit pár řádků, které po každém kroku překreslí aktuální stav seznamu.

Použití je jednoduché:

1. `import matplotlib.pyplot as plt` dej na začátek souboru.
2. `plt.ion()` a `plt.figure(...)` dej před začátek řazení.
3. Blok níže vlož dovnitř vnitřního cyklu, tedy tam, kde právě porovnáváš prvky.
4. Po skončení řazení přidej `plt.ioff()` a `plt.show()`.

Tady je jen samotný kód pro vizualizaci:

```python
colors = ["steelblue"] * len(values)
colors[index_highlight1] = "tomato"
colors[index_highlight2] = "tomato"
plt.clf()
plt.bar(range(len(values)), values, color=colors)
plt.title("Selection Sort")
plt.pause(0.1)
```

Třeba pro:

```python
values = [25, 12, 8, 30, 19]
index_highlight1 = 0
index_highlight2 = 2
```

vznikne graf, kde budou červeně zvýrazněné sloupce s hodnotami `25` a `8`.

Co dělají jednotlivé řádky:

1. `colors = ["steelblue"] * len(values)` vytvoří seznam barev pro všechny sloupce.
2. `colors[index_highlight1] = "tomato"` obarví první zvýrazněný sloupec červeně.
3. `colors[index_highlight2] = "tomato"` obarví druhý zvýrazněný sloupec červeně.
4. `plt.clf()` smaže předchozí obrázek, aby se vykreslil nový stav.
5. `plt.bar(range(len(values)), values, color=colors)` vykreslí aktuální hodnoty jako sloupce.
6. `plt.title("Selection Sort")` nastaví název grafu.
7. `plt.pause(0.1)` na chvíli zastaví program, aby byla změna v grafu vidět.

Tenhle blok vlož dovnitř cyklu na místo, kde chceš ukázat aktuální krok algoritmu. U Selection Sortu typicky nastavíš:

```python
index_highlight1 = i
index_highlight2 = min_index
```

Po skončení algoritmu ještě přidej:

```python
plt.ioff()
plt.show()
```

> **💡 Tip:** Na začátku si zkus krátký seznam, třeba 8 až 10 hodnot. U delších seznamů už bývá animace pomalejší a méně přehledná.

**📝 ÚKOL: Vizualizace Selection Sortu**

1. Doplň do své implementace Selection Sortu jednoduché překreslování barplotu.
2. Zvýrazni právě procházený prvek a aktuálně nalezené minimum.
3. Vyzkoušej vizualizaci na krátkém seznamu čísel.
4. Krátce si všimni, jak se minimum v každém průchodu posouvá na správnou pozici.

---
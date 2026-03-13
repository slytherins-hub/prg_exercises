# CVIČENÍ 11: ŘADICÍ ALGORITMY

Algoritmizace a programování

## CÍL 1: INSERTION SORT

Insertion Sort je další ze **stabilních** řadicích algoritmů a v praxi bývá efektivnější než Selection Sort a Bubble Sort. Připomíná třídění karet v ruce.

### 1.8 Princip algoritmu

Princip algoritmu pro vzestupné seřazení:

1. První prvek považuj za seřazený.
2. Vezmi první prvek z neseřazené části.
3. Porovnávej ho s prvky nalevo.
4. Větší prvky posouvej o jednu pozici doprava.
5. Na uvolněné místo vlož aktuální prvek.
6. Pokračuj dalším prvkem z neseřazené části.

![Insertion Sort](../assets/cviceni_11/10_insertion_sort_visualization.png)

**📝 ÚKOL: Insertion Sort**

1. Do modulu `sorting.py` implementuj funkci `insertion_sort()`.
2. Funkce bude mít jeden vstupní parametr: libovolně dlouhý seznam celých čísel.
3. Funkce vrátí vzestupně seřazený seznam.
4. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
5. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

### 1.9 Analýza algoritmu Insertion Sort

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce. Výsledky porovnej s ostatními algoritmy řazení.

| Algoritmus | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| Insertion Sort |  |  |

**📝 ÚKOL: Vizualizace Insertion Sortu**

1. Doplň do své implementace Insertion Sortu jednoduché překreslování sloupcového grafu.
2. Zvýrazni prvek, který právě vkládáš do seřazené části seznamu.
3. Vyzkoušej vizualizaci na krátkém seznamu čísel.
4. Sleduj, jak se seřazená část seznamu rozšiřuje zleva doprava.

---
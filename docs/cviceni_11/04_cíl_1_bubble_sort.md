# CVIČENÍ 11: ŘADICÍ ALGORITMY

Algoritmizace a programování

## CÍL 1: BUBBLE SORT

Bubble Sort patří mezi nejjednodušší **stabilní** algoritmy řazení. Pracuje na principu „probublávání“ čísel správným směrem.

### 1.6 Princip algoritmu

Základní princip algoritmu pro vzestupné seřazení:

1. Začni na první pozici.
2. Porovnej dva po sobě jdoucí prvky.
3. Pokud je první větší než druhý, prohoď jejich pořadí.
4. Posuň se o jednu pozici dál.
5. Po jednom průchodu se největší hodnota dostane na konec.
6. Opakuj, dokud není seřazená celá sekvence.

![Bubble Sort](../assets/cviceni_11/10_bubble_sort_visualization.png)

**📝 ÚKOL: Bubble Sort**

1. Do modulu `sorting.py` implementuj funkci `bubble_sort()`.
2. Funkce bude mít jeden vstupní parametr: libovolně dlouhý seznam celých čísel.
3. Funkce vrátí vzestupně seřazený seznam.
4. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
5. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

> **💡 Nápověda:** Všimni si, že algoritmus znovu nekontroluje prvky, které už dostal na správné místo. Tomu by mělo odpovídat nastavení řídicích cyklů.

### 1.7 Analýza algoritmu Bubble Sort

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce. Výsledky porovnej s ostatními algoritmy řazení.

| Algoritmus | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| Bubble Sort |  |  |

**📝 ÚKOL: Vizualizace Bubble Sortu**

1. Doplň do své implementace Bubble Sortu jednoduché překreslování sloupcového grafu.
2. Zvýrazni dvojici prvků, které právě porovnáváš.
3. Vyzkoušej vizualizaci na krátkém seznamu čísel.
4. Sleduj, jak největší hodnoty postupně „vybublají“ na konec seznamu.

---
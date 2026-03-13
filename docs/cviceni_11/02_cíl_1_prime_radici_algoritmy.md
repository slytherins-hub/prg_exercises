# CVIČENÍ 11: ŘADICÍ ALGORITMY

Algoritmizace a programování

## CÍL 1: PŘÍMÉ ŘADICÍ ALGORITMY

### 1.1 Stabilní a nestabilní algoritmy řazení

Řadicí algoritmy dělíme na **stabilní** a **nestabilní**. Toto dělení vychází z toho, jak algoritmus zachází s prvky, které mají stejný klíč řazení.

Stabilní algoritmus zachovává relativní pořadí shodných prvků tak, jak byly v původní posloupnosti. Nestabilní algoritmus tento výsledek nezaručuje.

![Stabilní a nestabilní řazení](../assets/cviceni_11/10_stable_vs_unstable_sorting.png)

Stabilitu nepotřebuješ vždy. Pokud řadíš jen samotná čísla bez dalšího významu, pravděpodobně ti bude jedno, v jakém pořadí za sebou dvě stejné hodnoty skončí.

Důležitá je ale ve chvíli, kdy se stejným klíčem řazení pracují různé objekty, které od sebe umíš odlišit. Typický příklad je seznam jmen nebo záznamů, kde můžeš řadit podle více různých kritérií.

> **💡 Poznámka:** Stabilní algoritmy mívají často vyšší výpočetní nebo paměťovou náročnost. Pokud stabilitu nepotřebuješ, může být výhodnější použít i nestabilní algoritmus.

#### 1.2 GitHub repozitář pro dnešní cvičení

Soubory pro dnešní cvičení jsou k dispozici na GitHubu.

**Adresa repozitáře:** doplní vyučující.

**📝 ÚKOL: Git a příprava repozitáře**

1. Na vlastním GitHub účtu vytvoř kopii zdrojového repozitáře (`fork`).
2. Naklonuj si repozitář ze svého GitHub účtu do složky s dnešním cvičením.
3. V lokálním repozitáři nastav pomocí terminálu novou vzdálenou adresu (`remote`) na původní adresu repozitáře (`upstream`).
4. V lokálním repozitáři vytvoř novou větev s názvem `sorting_algorithms` a přepni se do ní.

> **💡 Tip:** Pokud si nejsi jistý postupem, vrať se ke cvičení o Gitu a GitHubu a použij stejný workflow jako minule.

---

### 1.3 Selection Sort

Selection Sort patří mezi jednoduché **nestabilní** řadicí algoritmy. Jeho výhodou je hlavně nízká paměťová náročnost, protože pracuje přímo v původním seznamu.

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

#### 1.4 Analýza algoritmu Selection Sort

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce.

Zjisti také v dokumentaci, jaká je asymptotická složitost metod `insert()` a `pop()`. Jak by se změnila asymptotická složitost algoritmu, kdybys prohazování prvků realizoval pomocí těchto metod?

| Případ | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| vzestupné seřazení posloupnosti |  |  |
| sestupné seřazení posloupnosti |  |  |

---

### 1.5 Bubble Sort

Bubble Sort patří mezi nejjednodušší **stabilní** algoritmy řazení. Pracuje na principu „probublávání“ čísel správným směrem.

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

#### 1.6 Analýza algoritmu Bubble Sort

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce. Výsledky porovnej s ostatními algoritmy řazení.

| Algoritmus | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| Bubble Sort |  |  |

---

### 1.7 Insertion Sort

Insertion Sort je další ze **stabilních** řadicích algoritmů a v praxi bývá efektivnější než Selection Sort a Bubble Sort. Připomíná třídění karet v ruce.

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

#### 1.8 Analýza algoritmu Insertion Sort

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce. Výsledky porovnej s ostatními algoritmy řazení.

| Algoritmus | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| Insertion Sort |  |  |

---
# CVIČENÍ 10: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## CÍL 2: SEKVENČNÍ A BINÁRNÍ VYHLEDÁVÁNÍ

V této sekci se seznámíš se základními algoritmy pro vyhledávání. Vyhledávání je jedna z nejčastějších úloh, 
které programátor řeší. Současně se s ním setkáváš takřka denně i jako uživatel. Znáš Google?:)

![Ukázka vyhledávání](../assets/cviceni_10/09_google_search_example.png)

Vyhledávání ale nemusí znamenat jen to, že se snažíš najít prvek v nějaké databázi. Algoritmy vyhledávání řeší celou 
řadu užitečných úloh, třeba kombinatorické nebo optimalizační problémy:

- Plánovač tras či aktivit
- Nalezení nejkratší cesty
- Optimalizace průmyslových procesů
- Prolamování hesel
- Vyjádření podobnosti mezi objekty

U algoritmů vyhledávání, a vlastně obecně, platí, že neexistuje jeden univerzální algoritmus vhodný pro řešení všech
problémů. Před implementací algoritmu nebo výběrem už hotové metody je potřeba dobře zvážit situaci, kterou řešíš.

Mezi ty základní patří např.:

- Vyhledávání v neseřazené struktuře
- Vyhledávání v seřazené struktuře
- Vyhledáváme pouze jednou
- Vyhledáváme opakovaně ve stejné struktuře
- Vyhledáváme v rozsáhlé struktuře/nekonečném datovém streamu
- Vyhledáváme první výskyt
- Vyhledáváme poslední výskyt (četnost prvku)

#### 2.1 Než začneme…

Vyzkoušíš si práci s Gitem a GitHubem. Nejprve si soubory k dnešnímu cvičení přesuneš na svůj GitHub účet
a potom je naklonuješ do pracovního adresáře s dnešním cvičením.

**Adresa repozitáře**: [https://github.com/slytherins-hub/lecture_searching](https://github.com/slytherins-hub/lecture_searching)

#### ÚKOL: Git a příprava repozitáře

1. Na vlastním GitHub účtu vytvoř kopii zdrojového repozitáře (`fork`).
2. Otevři v prohlížeči adresu zdrojového repozitáře.
3. Vpravo nahoře najdi tlačítko `Fork` a klikni na něj.
4. Naklonuj si repozitář ze svého GitHub účtu na Plochu.

> **Poznámka:** Podrobný postup viz cvičení 9, cíl 3.

---

#### 2.2 Sekvenční vyhledávání v neseřazeném seznamu

Mějme naše data uložena v iterovatelné datové struktuře (např. seznamu, kde pořadí každé hodnoty je dáno jejím indexem). 
Základní způsob nalezení konkrétní hodnoty pak spočívá jednoduše v tom, že postupně (v sekvenci) projdeme každý prvek 
seznamu, dokud nenalezneme naši hodnotu.

![Sekvenční vyhledávání](../assets/cviceni_10/09_sequential_search_diagram.png)

Pokud vyhledáváš v **neseřazeném** seznamu, znamená to, že prvky v něm nejsou uspořádané tak, aby ti jejich pořadí 
pomohlo při hledání. Po každém porovnání tedy obvykle nemáš informaci, která by ti dovolila přeskočit část seznamu, 
a proto musíš v nejhorším případě projít všechny prvky.

V dnešním cvičení budeš pracovat s různými typy sekvencí, které jsou uložené v souboru `.json`. Prvním krokem bude 
prozkoumat obsah souboru a data načíst.

#### ÚKOL: Načtení dat ze souboru

1. V modulu `searching.py` doplň funkci `read_data()`.
2. Funkce bude mít dva vstupní parametry:
	- název souboru k načtení,
	- klíč specifický pro naše data.
3. Ověř, že zadaný klíč pochází z množiny povolených řešení v souboru `sequential.json`.
4. Pokud klíč není platný, vrať hodnotu `None`.
5. Pomocí modulu `json` načti `.json` soubor ve formě slovníku.
6. Vrať hodnoty uložené pod klíčem definovaným druhým vstupním parametrem (`field`).
7. Funkci `read_data()` zavolej z hlavní funkce `main()` se vstupním argumentem `sequential.json` a `unordered_numbers`.
8. Výstup funkce ulož do proměnné `sequential_data` a její obsah vytiskni v terminálu.
9. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

V dalším kroku si vytvoříme funkci pro sekvenční vyhledávání. Tento algoritmus nazýváme jako *naivní* – algoritmus 
totiž není příliš sofistikovaný ani výpočetně efektivní. Na některých typech neseřazených sekvencí však může jít
o jediné možné řešení.

#### ÚKOL: Sekvenční vyhledávání

Implementuj algoritmus sekvenčního vyhledávání, který v neseřazeném seznamu najde pozice a četnost výskytu zadaného čísla.

1. V modulu `searching.py` vytvoř funkci `linear_search()`.
2. Funkce bude mít dva vstupní parametry:
	- prohledávanou sekvenci,
	- hledané číslo.
3. Funkce vrátí slovník se dvěma klíči:
	- `positions` pro seznam pozic (indexů),
	- `count` pro počet výskytů hledaného čísla.
4. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
5. V hlavní funkci definuj také vyhledávané číslo.
6. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

---

#### 2.3 Analýza algoritmu sekvenčního vyhledávání pro neseřazený seznam

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce níže. 
Nezapomeň, že při analýze zanedbáváme konstanty. Základní výpočetní jednotkou u sekvenčního vyhledávání bude počet 
porovnání, které algoritmus musí provést k dosažení výsledku.

|                 | Kdy nastane? | Asymptotická složitost |
|-----------------|--------------|------------------------|
| Nejlepší scénář |              |                        |
| Nejhorší scénář |              |                        |

---

#### 2.4 Binární vyhledávání na seřazeném seznamu

Binární vyhledávání využívá výhodu, kterou dává seřazení hodnot v datové struktuře. Jde o algoritmus typu 
*Rozděl a panuj* (Divide and Conquer). Základní myšlenkou je postupné rozdělení problému na menší části. 
Z řešení dílčích částí pak sestavíš celkový výsledek. Základní princip algoritmu pro vrácení pozice hledané hodnoty 
vypadá následovně:

1. Zkontroluj prostřední prvek. Pokud obsahuje hledanou hodnotu, ukonči hledání a vrať pozici prostředního prvku.
2. Pokud je prostřední prvek menší než hledané číslo, zmenši oblast prohledávání na pravou půlku seznamu.
3. Pokud je prostřední prvek větší než hledané číslo, zmenši oblast prohledávání na levou polovinu seznamu.
4. Opakuj předchozí kroky dokud existuje oblast, která ještě nebyla prohledána.

Vizuální ukázka pro hledání hodnoty 45 může vypadat např. takto:

![Binární vyhledávání](../assets/cviceni_10/09_binary_search_visualization.png)

> **Poznámka:**
> Implementačně lze v Pythonu velikost prohledávané oblasti měnit několika způsoby. Varianta se slicingem je jednoduchá
> na pochopení, ale méně efektivní, protože vytváří nové části seznamu. Výhodnější je držet si index levého a pravého 
> okraje prohledávané oblasti a měnit jen ty. V tom případě zůstává změna rozsahu oblasti na konstantní složitosti $O(1)$.

#### ÚKOL: Binární vyhledávání

Implementuj algoritmus binárního vyhledávání, který zjistí, jestli se ve vzestupně seřazené posloupnosti nachází 
zadané číslo, a vrátí jeho pozici.

1. V modulu `searching.py` vytvoř funkci `binary_search()`.
2. Funkce bude mít dva vstupní parametry:
	- prohledávaný seznam čísel,
	- hledané číslo.
3. Funkce vrátí index, na kterém se hledané číslo v sekvenci nachází.
4. Pokud číslo nalezené není, funkce vrátí hodnotu `None`.
5. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
6. V hlavní funkci definuj vyhledávané číslo.
7. Seřazený seznam čísel získej ze souboru `sequential.json` pod klíčem `ordered_numbers`.
8. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

---

#### 2.5 Analýza algoritmu binárního vyhledávání

Proveď analýzu implementovaného algoritmu a odhadni jeho asymptotickou složitost pro případy uvedené v tabulce. 
Výsledky porovnej se sekvenčním vyhledáváním.

Jak se bude chovat algoritmus v nejhorším případě? Nejhorší scénář nastane ve chvíli, kdy velikost prohledávané oblasti
obsahuje už jen jeden prvek, bez ohledu na to, jestli hledané číslo opravdu obsahuje, nebo ne. Základní výpočetní 
jednotkou bude opět počet porovnání. Uvědom si, že po prvním porovnání zůstane k prohledání polovina všech hodnot ($n/2$),
po druhém porovnání čtvrtina ($n/4$) a po třetím porovnání osmina ($n/8$). Jaký je celkový počet porovnání v závislosti
na počtu prvků v nejhorším scénáři?

**Případ 1:** Prvek se nachází v seznamu

|                 | Kdy nastane? | Asymptotická složitost |
|-----------------|--------------|------------------------|
| Nejlepší scénář |              |                        |
| Nejhorší scénář |              |                        |

**Případ 2:** Prvek se nenachází v seznamu

|                 | Kdy nastane? | Asymptotická složitost |
|-----------------|--------------|------------------------|
| Nejlepší scénář |              |                        |
| Nejhorší scénář |              |                        |

> **Poznámka:** Vždy zvaž, jestli seřazení dat stojí za výpočetní práci navíc, kterou program musí vykonat. 
> Při malé nebo naopak velmi velké velikosti vstupních dat může být sekvenční vyhledávání metodou první volby. 
> Pokud ale víš, že budeš v datech vyhledávat opakovaně, často se vyplatí provést seřazení hned na začátku.

---

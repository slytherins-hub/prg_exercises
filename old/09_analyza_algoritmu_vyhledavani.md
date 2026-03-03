# CVIČENÍ 9: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## ÚVOD

Čas, potřebný pro zpracování dat pomocí konkrétního algoritmu, zpravidla narůstá v závislosti na množství dat, které je nutné zpracovat (vliv má samozřejmě také konkrétní počítač, spuštěné procesy a další parametry). Aby bylo možné určit alespoň přibližný odhad výpočetního času, využívá se odhadu růstu funkce, která popisuje složitost v závislosti na velikosti vstupních dat. V algoritmizaci a programování se jedná o důležité téma, neboť nám umožňuje odpovědět na základní otázky:

Jak dlouho program poběží pro zadaná vstupní data?

Kolik paměťového prostoru program využije?

Je zadaný problém řešitelný v požadovaném čase?

Schopnost analyzovat složitost algoritmu umožňuje programátorům porovnat mezi sebou více algoritmů a rozhodnout, který z nich pro daný problém použít, aby navržené řešení bylo maximálně výpočetně efektivní (asi nikdo z nás by nechtěl několik vteřin či dokonce minut čekat na odezvu programů, které denně používáme). Odhad složitosti algoritmu lze provést jak pro výpočetní čas, tak pro paměťové nebo jiné prostředky.

V této lekci si vyzkoušíme základy analýzy asymptotické složitosti na algoritmech vyhledávání. Jedná se o algoritmy, které jsou základem naprosté většiny programů a využíváme je prakticky na denní bázi (např. vyhledávání přes Google).

V praxi se jen málokdy setkáte s potřebou implementovat tyto algoritmy svépomocí, protože jsou součástí základní sady příkazů u většiny jazyků. Jedná se nicméně o principiálně jednoduché postupy, na kterých lze vliv asymptotické náročnosti na běh programu velmi dobře pochopit. Alespoň základní orientace mezi těmito algoritmy také umožňuje zvolit konkrétní implementaci v závislosti na našich datech a řešeném problému. V kombinaci s např. vhodnou datovou strukturou, tak můžeme **zrychlit náš program o několik řádů**!

## CÍL 1

### ANALÝZA ASYMPTOTICKÉ SLOŽITOSTI

Odhad řádu růstu funkce *g*(*n*) zkoumaného algoritmu lze provést řadou různých způsobů. Mezi základní řadíme například:

***f*****(*****n*****) = *****O*****(*****g*****(*****n*****)) – Big O Notation
**Asymptotická horní mez – algoritmus pro jakákoliv vstupní data asymptoticky nepřesáhne stanovenou funkci.

***f*****(*****n*****) = 𝛀****(*****g*****(*****n*****)) – Big Omega Notation
**Asymptotická dolní mez – algoritmus pro jakákoliv vstupní data asymptoticky nedosáhne lepší složitosti než je stanovená funkce.

***f*****(*****n*****) = Θ****(*****g*****(*****n*****)) – Big Theta Notation
**Asymptotická těsná mez – kde platí zároveň ***O*** i 𝜴.

Nás bude zajímat zejména odhad složitosti v nejhorším možném scénáři. V tomto případě postupujeme zpravidla tak, že: a) zanedbáme členy funkce g(n) rostoucí stejně rychle nebo pomaleji než člen s nejrychlejším růstem; b) zanedbáme konstanty funkce g(n).

|  | V praxi je kromě asymptotické složitosti nutné zohlednit také další parametry. Někdy tak může být výhodnější použít algoritmus s horší asymptotickou složitostí:  Složitá implementace Algoritmy s lepší asymptotickou složitostí jsou často více komplikované a mohou zvýšit čas potřebný na implementaci.  Malá velikost vstupních dat Pro malou velikost vstupních dat může vzrůst vliv konstant a výrazů nižšího řádu, které jsou u asymptotické složitosti zanedbány. Algoritmus s vyšší asymptotickou složitostí tedy může výpočetně překonat asymptoticky jednodušší algoritmus.  Rozdíly mezi průměrným a nejhorším scénářem V určitých případech může být výhodnější zvolit algoritmus, který má vyšší asymptotickou složitost pro nejhorší scénář, ale relativně nízkou složitost průměrnou (např. když víme, že nejhorší scénář nenastává příliš často). Naopak v kritických situacích (např. kontrolní systémy letadel) můžeme preferovat algoritmus s nižší průměrnou složitostí, pokud je jeho asymptotická složitost v nejhorším případě lepší než u jiného řešení. |
| --- | --- |

## CÍL 2

### ALGORITMY VYHLEDÁVÁNÍ

V této sekci se seznámíme se základními algoritmy pro vyhledávání. Vyhledávání je jedna z nejčastějších úloh, které programátor musí řešit. Současně se s ním setkáváme takřka denně jako uživatelé. Znáte Google?:)

![09_image4.png](images/09_google_search_example.png)


Vyhledávání ale nemusí znamenat jen to, že se snažíme nalézt prvek v nějaké databázi. Algoritmy vyhledávání řeší celou řadu užitečných úloh, např. kombinatorické nebo optimalizační úlohy:


Plánovač tras či aktivit

Nalezení nejkratší cesty

Optimalizace průmyslových procesů

Prolamování hesel

Vyjádření podobnosti mezi objekty

U algoritmů vyhledávání (a obecně) platí, že **neexistuje** jeden univerzální algoritmus vhodný pro řešení všech problémů. Před implementací algoritmu nebo výběru již implementované metody bychom měli dobře zvážit situaci, kterou budeme řešit. Mezi ty základní patří např.:

Vyhledávání v neseřazené struktuře

Vyhledávání v seřazené struktuře

Vyhledáváme pouze jednou

Vyhledáváme opakovaně ve stejné struktuře

Vyhledáváme v rozsáhlé struktuře/nekonečném datovém streamu

Vyhledáváme první výskyt

Vyhledáváme poslední výskyt (četnost prvku)

#### 2.1	Než začneme…

Vyzkoušíme si práci s Gitem/GitHubem. Nejprve si soubory k dnešnímu cvičení přesuneme na individuální GitHub účet a poté naklonujeme do pracovního adresáře s dnešním cvičení.

**Adresa repozitáře**: 

| Úkol – Git (Podrobný postup viz cv. 11 – cíl 3) |
| --- |
| Na vlastním GitHub účtu vytvořte kopii (fork) zdrojového repozitáře. Otevřete v prohlížeči adresu zdrojového repozitáře. Vpravo nahoře najdete tlačítko Fork a klikněte na něj.  Naklonujte si repozitář ze svého GitHub účtu do složky s dnešním cvičením. |

#### 2.2	Sekvenční vyhledávání v neseřazeném seznamu

Mějme naše data uložena v iterovatelné datové struktuře (např. seznamu, kde pořadí každé hodnoty je dáno jejím indexem). Základní způsob nalezení konkrétní hodnoty pak spočívá jednoduše v tom, že postupně (v sekvenci) projdeme každý prvek seznamu, dokud nenalezneme naši hodnotu. 

![09_image2.png](images/09_sequential_search_diagram.png)


Pokud vyhledáváme v **neseřazeném** seznamu znamená to, že jednotlivé prvky byly do seznamu umístěny náhodně. Při každém porovnání s hledanou hodnotou může a nemusí dojít k nalezení prvku. Jinými slovy, v každé iteraci je (většinou) stejná pravděpodobnost, že nalezneme hledaný prvek.

V dnešním cvičení budeme pracovat s různými typy sekvencí, které jsou uloženy v souboru *.json. Naším prvním úkolem bude prozkoumat obsah tohoto souboru a data poté načíst.

| Úkol |
| --- |
| V modulu searching.py doplňte funkci read_data(). Funkce má dva vstupní parametry. Prvním vstupním parametrem je název souboru k načtení. Druhým vstupním parametrem je klíč specifický pro naše data.  Funkce ověří, že zadaný klíč pochází z množiny povolených řešení (viz soubor "sequential.json"). Pokud ne, funkce vrátí hodnotu None.  Funkce pomocí modulu json načte *.json soubor ve formě slovníku. Funkce vrátí hodnoty uložené pod klíčem definovaným druhým vstupním parametrem (field).  Funkci read_data() zavolejte z hlavní funkce se vstupním argumentem "sequential.json" a "unordered_numbers".  Výstup funkce uložte do proměnné sequential_data a její obsah vytiskněte v terminálu.  Vytvořte novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push). |

V dalším kroku si vytvoříme funkci pro sekvenční vyhledávání. Tento algoritmus nazýváme jako *naivní* – algoritmus totiž není příliš sofistikovaný ani výpočetně efektivní. Na některých typech neseřazených sekvencí však může jít o jediné možné řešení.

| Samostatný úkol |
| --- |
| Implementujte algoritmus sekvenčního vyhledávání, který v neseřazeném seznamu nalezne pozice a četnost výskytu zadaného čísla.  V modulu searching.py vytvořte funkci linear_search(). Funkce bude mít dva vstupní parametry – prohledávanou sekvenci a hledané číslo.  Funkce vrátí slovník se dvěma klíči. Pod prvním klíčem positions bude uložen seznam pozic (indexů). Pod druhým klíčem count bude uložen počet výskytů hledaného čísla.  Volání funkce a korektnost její implementace ověřte voláním z hlavní funkce main().  V hlavní funkci definujte také vyhledávané číslo.  Vytvořte novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push). |

#### 2.3	Analýza algoritmu sekvenčního vyhledávání pro neseřazený seznam

Proveďte analýzu implementovaného algoritmu a odhadněte jeho asymptotickou složitost pro případy uvedené v tabulce níže. Nezapomeňte, že při analýze zanedbáváme konstanty. Základní výpočetní jednotkou u sekvenčního vyhledávání bude množství porovnání, které algoritmus musí provést k dosažení výsledku.

| Nejlepší scénář | Nejhorší scénář |
| --- | --- |
|  |  |

#### 2.4	Vyhledávání vzorů v neseřazené sekvenci

V předchozím příkladu jsme vyhledávali vždy jen jeden specifický element. V celé řadě případů je však nutné vyhledávat posloupnost elementů, tzv. vzor. V následujícím příkladu si rozšíříme příklad z předchozího úkolu na vyhledávání vzorů v sekvenci DNA.

Mějme naše data opět uložena v iterovatelné datové struktuře – textovém řetězci. Naivní algoritmus nalezení pozice vzoru opět spočívá jednoduše v tom, že postupně (v sekvenci) projdeme prvky řetězce, dokud nenalezneme přesnou shodu na všech pozicích mezi vzorem a podřetězcem prohledávané sekvence.

![09_image5.png](images/09_pattern_matching_diagram.png)


Základní princip algoritmu pro nalezení pozic vzoru v sekvenci může vypadat např. takto:

Nastav ukazatel v analyzované sekvenci na podřetězec v rozsahu nultý až *m*-tý prvek, kde *m* je délka vzoru.

Porovnej shodu prvků mezi vzorem a podřetězcem.

Pokud jsou všechny prvky shodné, ulož pozici prostředního prvku podřetězce.

Posuň ukazatel o jednu pozici doprava.

Opakuj předchozí kroky dokud existuje oblast, která ještě nebyla prohledána.

| Samostatný úkol |
| --- |
| Implementujte algoritmus sekvenčního vyhledávání vzorů, který v řetězci DNA nalezne pozice výskytu zadaného vzoru. Délka vzoru může být různá.  V modulu searching.py vytvořte funkci pattern_search(). Funkce bude mít dva vstupní parametry – prohledávanou sekvenci a hledaný vzor. Pro usnadnění můžete využít kód z minulého úkolu. Prohledávanou sekvenci získáte ze souboru sequential.json pod klíčem "dna_sequence".  Funkce vrátí množinu, ve které budou uloženy pozice (indexy) výskytu vzoru v sekvenci.  Volání funkce a korektnost její implementace ověřte voláním z hlavní funkce main(). V hlavní funkci definujte také vyhledávaný vzor, např. "ATA"  Vytvořte novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push). |

#### 2.5	Upravené vyhledávání vzorů v neseřazené sekvenci

V naivním algoritmu v úkolu 2.3 jsme v každé iteraci provedli vždy *m* operací (porovnání), kde *m* je délka vzoru. Toto můžeme ještě trochu vylepšit. Porovnání jednotlivých prvků v jedné iteraci má totiž smysl provádět jen do té doby, dokud jsou prvky shodné. Ve chvíli, kdy nalezneme první neshodu, nemá smysl v porovnání dalších prvků pokračovat a můžeme se přesunout rovnou na další iteraci.

| Samostatný úkol |
| --- |
| Upravte algoritmus ve funkci pattern_search() tak, aby při nalezení první neshody algoritmus automaticky pokračoval další iterací (posun indexu o pozici doprava a porovnání nového podřetězce).  Vytvořte novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push). |

### **2.****6****	****Analýza algoritmu vyhledávání vzorů**

Proveďte analýzu naivního – “vylepšeného” – algoritmu vyhledávání vzorů a odhadněte jeho asymptotickou složitost pro případy uvedené v tabulce níže. Pro zápis uvažujte: ***n***** – délka analyzované sekvence**;** *****m***** – délka vzoru**.

| Algoritmus | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| Naivní – vylepšený |  |  |

#### 2.7	Binární vyhledávání na seřazeném seznamu

Binární vyhledávání využívá výhodu, kterou nám poskytuje seřazení hodnot v datové struktuře. Jedná se o algoritmus typu *Rozděl a panuj* (Divide and Conquer) s jejichž obecnou podstatou se seznámíme později. Základní myšlenkou algoritmu je postupné rozdělení problému na menší  části. Z řešení dílčích částí poté sestavíme celkový výsledek. Základní princip algoritmu pro vrácení pozice hledané hodnoty vypadá následovně:

Zkontroluj prostřední prvek. Pokud obsahuje hledanou hodnotu, ukonči hledání a vrať pozici prostředního prvku.

Pokud je prostřední prvek menší než hledané číslo, zmenši oblast prohledávání na pravou půlku seznamu.

Pokud je prostřední prvek větší než hledané číslo, zmenši oblast prohledávání na levou polovinu seznamu.

Opakuj předchozí kroky dokud existuje oblast, která ještě nebyla prohledána. 

Vizuální ukázka pro hledání hodnoty 45 může vypadat např. takto:

![09_image1.png](images/09_binary_search_visualization.png)


|  | Implementačně lze v Pythonu velikost prohledávané oblasti změnit několika způsoby. Destruktivní varianta s využitím slicingu odstraní v každé iteraci nepotřebnou polovinu sekvence. Indexy levého a pravého okraje oblasti pak zůstávají konstantní. Asymptotická složitost pro tyto operace nad seznamem je však O(n) či O(k) v případě odstranění nebo vyjmutí podsekvence (k = počet vyjmutých prvků).     Algoritmus lze optimalizovat vhodným nastavením pozic levého a pravého okraje prohledávané oblasti. V takovém případě snížíme asymptotickou složitost změny rozsahu oblasti na konstantní O(1). |
| --- | --- |

| Samostatný úkol |
| --- |
| Implementujte algoritmus binárního vyhledávání, který zjistí, zda-li se ve vzestupně seřazené posloupnosti nachází libovolné požadované číslo a vrátí jeho pozici.  V modulu searching.py vytvořte funkci binary_search(). Funkce bude mít dva vstupní parametry – prohledávaný seznam čísel a hledané číslo. Seřazený seznam čísel získáte ze souboru sequential.json pod klíčem "ordered_numbers".  Funkce vrátí index, na kterém se hledané číslo v sekvenci nachází. Pokud není číslo nalezeno, funkce vrátí hodnotu None.  Volání funkce a korektnost její implementace ověřte voláním z hlavní funkce main(). V hlavní funkci definujte také vyhledávané číslo.  Vytvořte novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push). |

#### 2.8	Analýza algoritmu binárního vyhledávání

Proveďte analýzu implementovaného algoritmu a odhadněte jeho asymptotickou složitost pro případy uvedené v tabulce. Výsledky porovnejte s algoritmem pro sekvenční vyhledávání. 

Jak se bude chovat algoritmus v nejhorším případě? Nejhorší scénář nastane ve chvíli, kdy velikost prohledávané oblasti bude obsahovat pouze jeden prvek, bez ohledu na to, jestli prvek obsahuje hledané číslo či nikoliv. Základní výpočetní jednotkou bude opět počet porovnání. Uvědomte si, že po prvním porovnání zůstane k prohledání polovina všech hodnot (*n*/2), po druhém porovnání čtvrtina (*n*/4) a po třetím porovnání osmina (*n*/8). Jaký je celkový počet porovnání v závislosti na počtu prvků v případě nejhoršího scénáře?

| Případ | Nejlepší scénář | Nejhorší scénář |
| --- | --- | --- |
| prvek se nachází v seznamu |  |  |
| prvek se nenachází v seznamu |  |  |

|  | Vždy bychom měli zvážit, zda seřazení dat stojí za výpočetní práci navíc, kterou musí program vykonat. Při malé nebo naopak velmi velké velikosti vstupních dat může být sekvenční vyhledávání metodou první volby. Pokud naopak víme, že v datech budeme vyhledávat opakovaně, vyplatí se provést na začátku jejich seřazení. Toho velmi efektivně využívají některé pokročilé datové struktury, které provádí zařazení prvku ihned po jeho vložení. |
| --- | --- |

CÍL 3

DOBROVOLNÝ ÚKOL – MĚŘENÍ ČASU

V Pythonu můžeme kromě asymptotické složitosti provést odhad doby běhu programu pomocí balíčku time. Prozkoumejte, jaké příkazy balíčku jsou vhodné pro měření času (code execution time measurement).

Vytvořte si generátor vlastních sekvencí o různé délce (seřazené sekvence, neseřazená čísla, atd.) nebo do modulu searching.py importujte již předpřipravé generátory z modulu generators.py, který je dostupný na e-learningu. Pokuste se změřit dobu běhu jednotlivých funkcí pro různě dlouhá data. Lze z výsledků odhadnout asymptotickou složitost implementovaných algoritmů?

|  | Měření doby běhu bloku kódu je ovlivněno dalšími procesy systému. Aby bylo měření alespoň trochu reprezentativní, měli bychom provést pro jednu délku sekvence několik pokusů a jejich výsledky poté zprůměrovat. |
| --- | --- |


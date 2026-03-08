# CVIČENÍ 3: SEZNAMY A VĚTVENÍ PROGRAMU

Algoritmizace a programování

## CÍL 1

### SEZNAMY, VNOŘENÉ SEZNAMY

**Seznam** (ang. *list*) je datová struktura, která může obsahovat různé datové typy: celočíselné hodnoty, reálná čísla, textové řetězce nebo logické proměnné. Seznam se zapisuje jako posloupnost prvků oddělených čárkami do hranatých závorek. Pořadí prvků je jasně definované – [první prvek, druhý, …, předcházející prvek, aktuální prvek, následující prvek, ... poslední prvek]. S vybranými prvky pak díky indexování můžeme pracovat i jednotlivě. 

#### 1.1	Vytváříme seznam

Seznam můžeme inicializovat pomocí příkazu list() nebo pomocí prázdných hranatých závorek.

| empty_list = list() empty_list = [] |
| --- |

Seznam vytvoříme také přiřazením posloupnosti prvků v [hranatých závorkách] do konkrétní proměnné.

| Vyzkoušej a analyzuj výstup |
| --- |
| numbers = [2, 5, 87, 65, 44, 56, 12, 1] print(numbers)  names = ["Alice", "Thomas"] print(names)  results = [True, True, False, True] print(results) |

Seznam může obsahovat také prvky různých datových typů.

| Vyzkoušej a analyzuj výstup |
| --- |
| one_way = ["Praque", "Paris", 1031, "km", 9.5, "hod"] print(one_way) |

#### 1.2	Operace se seznamy

V minulé hodině jsme si vyzkoušeli některé operátory a funkce u textových řetězců. Vyzkoušejme je i u datové struktury seznam.

| Vyzkoušej a analyzuj výstup |
| --- |
| print(names + results) print(results * 3) print(5 in numbers) print("Alice" in names) print("Alex" not in names) print(len(names)) |

Seznam o *n* prvcích lze indexovat stejně jako u textových řetězců: první prvek má index 0 a poslední prvek má index *n* - 1. K indexaci lze také použít záporných indexů, kdy poslední prvek má index -1, předposlední prvek má index -2 atd.

| Úkol |
| --- |
| Vytvoř proměnnou week_days a do ní přiřaď seznam textových řetězců s názvy dnů v týdnu.  Zjisti, zda je délka textového řetězce 3. a 5. prvku seznamu stejná. Využij relační operaci == a indexaci pomocí hranatých závorek. |

Pokud provedeme přiřazení existující proměnné se seznamem do nové proměnné new_list = old_list, tak se vytvoří pouze reference na seznam původní. A proto, práce s původním seznamem ovlivní i seznamy z něj vytvořené.

Hodnoty seznamu lze po jejich vytvoření dodatečně změnit; říkáme, že jsou měnitelné (angl. *mutable*). Hodnoty prvků seznamu se sice změní, ale přepíší se na stejném místě v paměti, jejich ID zůstává stejné).

| Vyzkoušej a analyzuj výstup |
| --- |
| days = week_days print(days) week_days[4] = "My day" print(days) |

| Samostatný úkol |
| --- |
| Vytvoř seznam my_numbers, který bude obsahovat čísla od 1 do 13.  Pomocí indexování vypiš postupně následující prvky ze seznamu my_numbers: [6, 7, 8, 9, 10] [11, 10, 9, 8, 7] [1, 3, 5, 7, 9, 11, 13] [2, 4, 6, 8, 10, 12] [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] [13, 11, 9, 7, 5, 3, 1] |

#### 1.3	Vnořený seznam

Vnořený seznam (ang. *nested list*) je seznam, který je prvkem jiného seznamu. Vnořený seznam lze vytvořit vložením seznamu do již existujícího.

| nested_list = ["a", "b", ["cc", "dd", ["eee", "fff"]], "g", "h"] |
| --- |

Indexování prvku vnořeného seznamu se provádí zadáním vícenásobného indexu. Indexy se píší za sebou v hranatých závorkách např.:

variable_name[index_for_item_in_list][index_for_item_in_nested_list]

| print(nested_list[2][0]) |
| --- |

| Vyzkoušej a analyzuj výstup |
| --- |
| print(nested_list[2]) print(nested_list[2][2]) print(nested_list[2][2][0]) |

| Úkol |
| --- |
| V seznamu nested_list nahraď pomocí indexace textový řetězec "dd" hodnotou 0 a textový řetězec "fff" hodnotou 1.  Do terminálu vytiskni obsah upravené proměnné nested_list a zkontroluj správnost provedených úprav. |

#### 1.4	Seznam – metody

S datovou strukturou seznam lze pracovat také pomocí metod. Metody voláme pomocí tečkové notace - za objekt napíšeme tečku, název metody a kulaté závorky s případnými argumenty. Většina metod u seznamů nic nevrací, provádí se změny v existujících seznamech. V tomto je zásadní rozdíl oproti textovým řetězcům, se kterými jsme pracovali minule, které jsou neměnitelné (angl. *immutable*). Připomeňme si:

| name = "Legolas" print(name) name.upper() print(name) |
| --- |

Obsah proměnné name se nezměnil. Pokud budeme chtít pracovat se změněným novým řetězcem je potřeba si ho uložit. Obvykle budeme chtít změněný řetězec uložit do původní proměnné a “zahodit” původní hodnotu:

| name = name.upper() print(name) |
| --- |

Teď zpět k seznamům, které je možné měnit. První metodou je append(), která umožňuje **vložení** **jednoho prvku** na konec existujícího seznamu. Vstupní argumentem metody je objekt, který chceme vložit na konec seznamu. Ten napíšeme do kulatých závorek. 

| Vyzkoušej a analyzuj výstup |
| --- |
| the_lord_of_the_rings = ["Legolas", "Gimli", "Boromir", "Aragorn"] print(the_lord_of_the_rings)  the_lord_of_the_rings.append("Gandalf") print(the_lord_of_the_rings) |

Metoda extend() umožňuje **vložení** **více prvků** na konec seznamu. Vstupem je iterovatelný objekt, ze kterého jsou postupně přidávány prvky na konec existujícího seznamu.

| Vyzkoušej a analyzuj výstup |
| --- |
| next_names = ["Gimli", "Glum"] the_lord_of_the_rings.extend(next_names) print(the_lord_of_the_rings) |

Jaký je rozdíl mezi metodami append() a extend()? Co se stane, když provedeme vložení více prvků do seznamu pomocí metody append()?

| Vyzkoušej a analyzuj výstup |
| --- |
| the_lord_of_the_rings.append(["Legolas", "Saruman"]) print(the_lord_of_the_rings) |

Metoda remove() slouží k **odstranění** **prvního** **výskytu** zadaného prvku. Vstupním argumentem je prvek, který chceme ze seznamu odstranit.

| Vyzkoušej a analyzuj výstup |
| --- |
| the_lord_of_the_rings.remove("Gimli") print(the_lord_of_the_rings) |

Metoda pop() slouží také k **odstranění prvku** ze seznamu. **Odstraněný prvek** ale metoda **vrací** a je tedy možné prvek přiřadit do proměnné a dál s ním pracovat. Vstupním argumentem metody je **index** **prvku**, který chceme odebrat. V případě, že **index nezadáme**, provede se odstranění **posledního** prvku seznamu.

| Vyzkoušej a analyzuj výstup |
| --- |
| last_one = the_lord_of_the_rings.pop() print(the_lord_of_the_rings) print(last_one)  first_one = the_lord_of_the_rings.pop(0) print(the_lord_of_the_rings) print(first_one) |

Metoda insert() slouží k **vložení prvku na zadaný index**. Metoda má dva vstupní argumenty: první je index a druhý je objekt, který chceme do seznamu vložit.

| Vyzkoušej a analyzuj výstup |
| --- |
| the_lord_of_the_rings.insert(0, "Frodo") print(the_lord_of_the_rings) |

| Samostatný úkol |
| --- |
| Vytvoř skript car_list_methods.py .  Tento skript zpracuje zadaný textový řetězec, který bude obsahovat údaje o konkrétním autě: značku automobilu, model automobilu, rok výroby, číslo karoserie (8 místné), číslo motoru (10 místné), barvu karoserie a technickou kontrolu (True/False).  Do proměnné my_car přiřaď textový řetězec, např.:  my_car = "bugatti, divo, 2018, 34562876, 9845284635, blue, True"   Převeď textový řetězec my_car na seznam my_car_list a změň datový typ prvků tak, aby odpovídal jeho obsahu.  Pomocí vhodných metod proveď následující operace se seznamem my_car_list: Na konec seznamu vlož prvek, který bude obsahovat informaci o počtu majitelů. Odstraň prvky obsahující číslo karoserie a číslo motoru a tato čísla přiřaď do proměnných body_number a engine_number. Na konec seznamu přidej dva prvky: křestní jméno (např. "Jan") a příjmení (např. "Novak") aktuálního majitele. Jako poslední prvek vložte seznam např. [2014, 2018], který obsahuje roky předchozí technické kontroly. |

Obsah proměnné my_car_list bude vypadat například takto:

| ['bugatti', 'divo', 2018, 'blue', True, 2, 'Jan', 'Novak', [2014, 2018]] |
| --- |

## CÍL 2

### VĚTVENÍ PROGRAMU

Podmínka (angl. *condition*) obecně umožňuje větvit program do více větví a tím umožňuje pokračovat programu v běhu různými variantami. Program pokračuje vždy jen jednou větví (variantou) a to podle okolností – tedy podle vyhodnocení aktuálních podmínek. Do podmínek dáváme logické výrazy nebo složené logické výrazy (použití logických operací and, or, >, ==, ...). Vyhodnocení jedné podmínky – True / False – umožní větvení na dvě větve. Každá další vnořená podmínka umožňuje další košatější větvení. Kolik podmínek pro větvení budeme muset definovat záleží na složitosti řešeného programu a počtu možných variant řešení. Jakmile program projde jednou z větví, bude pokračovat program dalším příkazem za větvením.

#### 2.1	Jednoduché větvení (if)

Jednoduché větvení programu provádíme pomocí příkazu if, který používá vyhodnocení podmínky (CONDITION).  V nejjednodušší variantě definujeme pouze jednu variantu běhu programu, která se provede po splnění podmínky CONDITION. Splněním podmínky rozumíme výsledek True. Pokud podmínka není splněna, výsledek je False, nejsou provedeny žádné příkazy a program pokračuje dále za příkazem větvení. Uvedeme několik slovních příkladů:

Když mám počet kreditů získaných během studia menší než 180, musím absolvovat další předměty.

Když mám úspory větší než je cena automobilu, koupím si ho.

Když je pátek a zároveň 13. den v měsíci, vsadím si sportku.

Když je venku tma, zapnu osvětlení.

Když mám chuť na pizzu, objednám si ji.

Příkaz větvení je ve vývojových diagramech značen kosočtvercem, ze kterého vychází dvě směrové šipky. Každá směrová šipka prochází svou větví a ukončení větvení je v bodě setkání obou směrových šipek. Syntaxe příkazu if a vývojový diagram je následující:

| if (CONDITION):     CODE_BLOCK_TRUE |  | Jestliže je podmínka CONDITION vyhodnocená jako pravdivá, provedou se příkazy v bloku CODE_BLOCK_TRUE. Počet příkazů v CODE_BLOCK_TRUE může být různý, minimálně však jeden. Příkazy stejné úrovně musí být zarovnány přesně pod sebou a musí být odsazeny pomocí čtyř mezer. Pokud je podmínka vyhodnocena jako nepravdivá, program pokračuje prvním příkazem, který není odsazen, případně další větví. |
| --- | --- | --- |

|  | Tabulátor si nastavte v PyCharm na 4 mezery. Settings -> Editor -> Code Style -> Python -> Tab size = 4 |
| --- | --- |

| Úkol |
| --- |
| Do proměnné my_money přiřaď hodnotu svých úspor a do car_price cenu automobilu. Pokud jsou zadané úspory větší než je cena vysněného automobilu, přiřaď do nové proměnné own_car hodnotu True, do proměnné my_car textový řetězec např. "black-blue bugatti divo" a na závěr vypiš, jaké auto jste pořídili. Při zadávání hodnot, vyzkoušej obě varianty: mám na auto/nemám na auto. Příkaz print() zahrň do sekvence příkazu if odsazením nebo jej dej až za příkaz if. Ovlivní to funkčnost skriptu? |

Malý dovětek k seznamům, prázdný seznam se vyhodnocuje v podmínce jako False a pro kontrolu prázdného seznamu lze využít tento zápis:

| Vyzkoušej a analyzuj výstup |
| --- |
| my_list = list() print(my_list)  if my_list:     print("Vím, že NENÍ prázdný.")  if not my_list:     print("Vím, že JE prázdný.") |

#### 2.2	Složené větvení (if-else)

Pokud potřebujeme definovat i operace pro případ, že podmínka není splněna, pak budeme používat syntaxi příkazu if-else. Uveďme slovní příklady, ze kterých bude použití patrné:

Budu kupovat automobil. Když mám úspory větší než je cena automobilu v plné výbavě, koupím si auto s plnou výbavou. Pokud ne, koupím si auto v základní výbavě.

Stojím na křižovatce, která není označena dopravními značkami. Když přijíždí auto zprava, dám mu přednost (stojím). Pokud není žádné auto zprava, mám přednost já a mohu jet.

Výpočet prémií. Pokud je měsíční příjem menší než 100 tis. Kč, budou se prémie počítat jako procenta z měsíčního zisku. Pokud je příjem vyšší než 100 tis. Kč, budou prémie vyplaceny jako neměnná částka nezávislá na výši příjmu.

Syntax příkazu if-else** **a vývojový diagram je následující: 

| if (CONDITION):    CODE_BLOCK_TRUE else:    CODE_BLOCK_FALSE |  | Běh programu po splnění podmínky je definován blokem příkazů CODE_BLOCK_TRUE, a v opačném případě je definován blokem příkazů CODE_BLOCK_FALSE. Bloky příkazů musí být odsazeny od levého okraje stejně, jak se uvedeno v syntaxi příkazu. |
| --- | --- | --- |

| Úkol |
| --- |
| Vytvoř program, který bude mít za úkol vložit nový prvek na začátek nebo na konec již seřazeného seznamu a to pouze v případě, že výsledná posloupnost bude stále narůstající.  V případě, že je nový prvek menší než první prvek seznamu, přidej ho na začátek. Prvek, který by byl větší než poslední prvek seznamu, vlož na konec. Jiné prvky nezařazuj (nevyhoví podmínce menší než první, větší než poslední prvek). Do proměnné sequence přiřaď seřazený seznam celých čísel (např. [17, 18, 19, 20]) Do proměnné number přiřaď další prvek (číslo), který budeš chtít zařadit (např. 5). Proveď zařazení prvku na správnou pozici. Vypiš do terminálu výsledný seznam.  Program vytvoř přesně podle vývojového diagramu včetně využití operace slučování seznamů. Jakými metodami by bylo možné slučování seznamů nahradit? |

#### 2.3	Vnořené větvení (if-elif-else)

Další variantou větvení je vnořené větvení, kdy je nutno definovat více podmínek pro stanovení dalšího pokračování programu. Je stanoveno, že pokud platí první podmínka CONDITION_1, provede se blok příkazů CODE_BLOCK_TRUE a pokračuje se dále příkazem za větvením. Pokud ovšem není splněna první podmínka, je stanovena další podmínka CONDITION_2 na základě které se určuje řešení dalších variant: řešení pro splnění druhé podmínky je dáno blokem příkazů CODE_BLOCK_FALSE_TRUE a řešení pro nesplnění podmínky je dáno blokem příkazů CODE_BLOCK_FALSE_FALSE. Syntaxe příkazu if-elif-else** **a vývojový diagram jsou uvedeny zde:

| if (CONDITION_1):     CODE_BLOCK_TRUE elif (CONDITION_2):     CODE_BLOCK_FALSE_TRUE else:     CODE_BLOCK_FALSE_FALSE |  |
| --- | --- |

Slovní příklad, kdy použijeme if-elif-else:

Řadíme podle abecedy jmenný seznam studentů. Pokud je pouze jedno příjmení začínající konkrétním písmenem, pak ho zařadíme a pokračujeme dále. Pokud je však více příjmení začínajících stejným písmenem, budeme posuzovat podle pořadí i druhé písmeno (př. Dobrovský, Dušek, Dvořák).

| Úkol |
| --- |
| Vytvoř program, který určí maximum ze zadaných čísel. Do proměnných number_1 a number_2 přiřaď číselné hodnoty. Pomocí podmínek a porovnávání urči maximum z těchto čísel a jeho hodnotu ulož do proměnné maximum_number. Pokud jsou čísla shodná, přiřaď do proměnné maximum_number číslo number_1 a vypiš hlášku: "same numbers.". Zjištěné maximum vypiš do terminálu. Pro inspiraci využij vývojový diagram. |

![image3.png](images/03_flowchart_find_maximum.png)


## SAMOSTATNÉ ÚKOLY

| Samostatný úkol |
| --- |
| Vytvoř skript odd_or_even.py, který bude určovat, zda je číslo zadané z klávesnice liché (ang. odd) nebo sudé (ang. even). Výsledek přiřaďte do proměnné is_even a bude nabývat hodnot True/False. Podle obsahu proměnné is_even pak do terminálu vypiš buď "The number (zadané číslo) is even." nebo "The number (zadané číslo) is odd." Nakresli si vývojový diagram na papír. |

| Samostatný úkol |
| --- |
| Vytvoř skript max_of_3_numbers.py, který určí maximum ze tří čísel pomocí operace porovnávání. Do proměnné numbers přiřaď seznam tří různých čísel. Výsledek (maximum z čísel) ulož do proměnné maximum_number. Výsledek vypiš do terminálu celou větou včetně doplnění hodnoty zjištěného maxima. Nakresli si vývojový diagram na papír. |


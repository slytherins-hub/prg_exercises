# CVIČENÍ 4: ŘÍZENÍ TOKU PROGRAMU POMOCÍ CYKLŮ (FOR)

Algoritmizace a programování

## CÍL 1

### CYKLY S PEVNÝM POČTEM OPAKOVÁNÍ

#### 1.1	Obecná syntaxe

Cykly s pevným počtem opakování se uplatní zejména tam, kde známe velikost vstupních dat, která potřebujeme procházet a upravovat. Cyklus s pevným počtem opakování je uvozen *hlavičkou* s vyhrazeným příkazem for, za nímž následuje deklarace řídící proměnné (VAR), iteratibilní proměnné (ITERATIBLE_VAR) a na konci je dvojtečka. *Tělo cyklu* tedy blok příkazů, které se budou opakovat (CODE_BLOCK_A), jsou pod hlavičkou odsazené obdobně jako u podmínek s if. 

Cykly s pevným počtem opakování jsou ve vývojových diagramech značeny šestiúhelníkem, ze kterého vychází jedna šipka, která prochází tělem cyklu (CODE_BLOCK_A), a vrací se zpět. Z šestiúhelníku vychází také druhá šipka, která značí běh programu po skončení cyklu. Základní syntaxe a vývojový diagram vypadá následovně:

| for VAR in ITERATIBLE_VAR:     CODE_BLOCK_A |  |
| --- | --- |

Iterabilní proměnná je jakákoliv proměnná, do které můžeme uložit více než jednu položku a skrz tyto položky můžeme procházet – iterovat hodnotu ukazatele:

| my_string = "Zde mam znaky, ktere mohu prochazet" my_list = [1, 10, 18, "Slovo", 13] |
| --- |

K obsahu řídící proměnné lze přistupovat uvnitř cyklu a její název lze volit libovolně. Příkaz for přiřadí řídící proměnné vždy aktuální hodnotu z iterabilní proměnné a následně provede vše, co je odsazené v těle cyklu.

| Vyzkoušej a analyzuj výstup |
| --- |
| game_of_houses = ["Lannister", "Stark", "Tyrell", "Martel", "Tarly", "Bolton"] for house_name in game_of_houses:     print(f"I support the {house_name} family.") |

#### 1.2	Řízení cyklu

V některých případech může být nutné běh cyklu měnit např. předčasně ukončit. V takovém případě můžeme využít kombinaci podmínky umístěné uvnitř těla cyklu s vyhrazeným slovem break. Příkaz break ukončuje celý cyklus tzn. v případě splnění podmínky se cyklus ukončí a další příkazy (CODE_BLOCK_B) se již neprovedou.

| for VAR in ITERATIBLE_VAR:     if VAR == True:         break     CODE_BLOCK_B |  |
| --- | --- |

Druhou možností, u cyklů s pevným počtem opakování, je příkaz continue, který také obvykle používáme ve spojení s podmínkou. Příkaz continue přeskočí všechny následující příkazy v cyklu (CODE_BLOCK_B). Program bude pokračovat od začátku cyklu, avšak novou iterací (změní se obsah proměnné VAR).

| for VAR in ITERATIBLE_VAR:     if VAR == True:         continue     CODE_BLOCK_B |  |
| --- | --- |

| Úkol |
| --- |
| Uprav kód z příkladu 1.1 pomocí syntaxe if–break tak, aby program vypsal pouze první tři rodová jména. Výsledek by měl vypadat takto:         I support the Lannister family.         I support the Stark family.         I support the Tyrell family.  Uprav kód pomocí syntaxe if–continue tak, aby program vypsal všechna rodová jména kromě Starků, a Boltonů. Výsledek by měl vypadat takto:         I support the Lannister family.         I support the Tyrell family.         I support the Martel family.         I support the Tarly family.  V tomto příkladu pravděpodobně bude potřeba sestavit podmínku kombinací více logických výrazů. Zjistěte, co pro zachování dobré čitelnosti kódu doporučuje příručka kodéra PEP 8. Styl formátování případně upravte. |

#### 1.3	Funkce range()

Často budeme potřebovat některou část kódu *n*-krát zopakovat a k tomu lze použít funkci range(n), která vrací sekvenci čísel. Nicméně pokud vypíšeme funkci range() např. s argumentem 5, přímo sekvenci čísel nedostaneme, místo toho funkce vrátí speciální hodnotu typu range.

| >>> print(range(5)) range(0, 5) |
| --- |

Funkce range(n) vrací objekt reprezentující neměnnou sekvenci čísel od *0* do *n-1* a čísel bude přesně *n*. Sekvenci čísel lze procházet pomocí for cyklu nebo ji lze převést na seznam.

| Vyzkoušej a analyzuj výstup |
| --- |
| for idx in range(5):     print(idx)  print(list(range(5))) |

V Pythonu se range(n) obvykle využívá v případě, kdy je nutné něco *n*-krát opakovat a řídící proměnná idx - počítadlo - nás nezajímá, v programu se nevyužije. 

Proměnná idx je zkratka z termínu *index* (číslo prvku). V programování se využívá např. pro číslování průchodu cyklem, ale pro lepší srozumitelnost kódu je vhodné řídící proměnou vždy adekvátně pojmenovat vzhledem k iterabilní proměnné. Jak lze v tomto případě přejmenovat proměnou idx?

Funkce range můžeme mít až tři vstupní parametry - range(start, stop, step) - podobně jako u slicingu, který známe z řetězců nebo seznamů. Parametry start a step jsou nepovinné a ovlivňují rozsah a počet hodnot.

| Samostatný úkol |
| --- |
| Pomocí cyklu for a funkce range() vypočítej hodnoty druhých mocnin: čísel 0 až 5, čísel 6 až 10, všech lichých čísel od 1 do 11. |

#### 1.4	**Interpretace a implementace vývojového diagramu**

V seznamu data_stream máme k dispozici záznam naměřených hodnot. Jednotlivé prvky mohou nabývat buď číselných hodnot nebo textových řetězců "null" (systém hodnotu nezaznamenal) a "error" (systém zaznamenal nějaký druh chyby):

| data_stream = [0, 3, 10, "null", -5, 23, "null", -8, "error", 13, 0, 0] |
| --- |

Na následující stranu jsme vložili vývojový diagram algoritmu, který s daty specifickým způsobem pracuje. Proveďte analýzu vývojového diagramu a pokuste se algoritmus implementovat v prostředí Python. 

| Samostatný úkol |
| --- |
| Proveď analýzu vývojového diagramu. Pokus se algoritmus implementovat v prostředí Python. Pokus se odpovědět na následující otázky: Které bloky odpovídají větvení programu a které cyklům? Bude v nějakém případě vynuceno přerušení hlavního cyklu pomocí příkazu break? Co je cílem algoritmu? Kolikrát proběhne hlavní cyklus pro výše uvedená vzorová data? |

![image2.png](images/04_flowchart_algorithm_analysis.png)


## CÍL 2

### ITERÁTORY N-TIC

#### 2.1	Datová struktura *n*-tice (tuple)

*N*-tice (tuple) je datová struktura podobná seznamům, která může obsahovat *n* prvků. *N*-tice se dvěma prvky je dvojice, se třemi prvky trojice atd. 

*N*-tice se vytváří zapisem do kulatých závorek a jednotlivé prvky jsou oddělené čárkou. Jednotlivé prvky je možné indexovat stejně jako u seznamů pomocí hranatých závorek. Na rozdíl od seznamů ovšem nelze *n*-tice dodatečně měnit, jsou tedy *immutable* (neměnné). Prvkům *n*-tice nelze přiřadit novou hodnotu a nemají metody, které u seznamů mění jejich obsah jako append() nebo pop().

| Vyzkoušej a analyzuj výstup |
| --- |
| day_tuple = (0, "Monday")  day = day_tuple[1] print(day_tuple) print(day)  day_tuple[1] = "Tuesday" day_tuple.append("1.3.2022") |

Obsah *n*-tice lze „rozbalit“ a hodnoty přiřadit najednou do několika proměnných. Na levou stranu znaku rovná se napíšeme názvy proměnných oddělených čárkou a vpravo *n*-tici.

| Vyzkoušej a analyzuj výstup |
| --- |
| index, day = (0, "Monday") print(index) print(day) |

#### 2.2	Funkce enumerate()

Funkce enumerate() se využívá pro očíslování existující sekvence a vrací sekvenci dvojic (*index*, *původní hodnota*). Mějme seznam dní v týdnu, které chceme očíslovat pomocí funkce enumerate(). Funkce enumerate vytváří objekt typu enumerate, což je iterátor. Jeho hodnoty nejsou pomocí funkce print() “viditelné”, ale lze ho převést na seznam.

| Vyzkoušej a analyzuj výstup |
| --- |
| days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] print(enumerate(days))  print(list(enumerate(days))) |

Obvykle se iterátory využívají právě v cyklech, protože lze přes ně iterovat, jde je postupně procházet v cyklu. V případě, že enumerate() použijeme ve for cyklu, bude tato funkce do řídící proměnné postupně přiřazovat jednotlivé dvojice hodnot.

| Vyzkoušej a analyzuj výstup |
| --- |
| days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] for day_tuple in enumerate(days):     print(day_tuple) |

Cyklus for umí *n*-tice také rozbalit a toho můžeme využít i u funkce enumerate(), která právě *n*-tici (dvojici hodnot) vrací.

| Vyzkoušej a analyzuj výstup |
| --- |
| days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] for day_index, day in enumerate(days):     print(f"{day_index}. day of the week is {day}.") |

| Úkol |
| --- |
| Vytvoř skript character_analysis.py, který analyzuje jednotlivé znaky v zadaném řetězci a označí je buď za samohlásky nebo souhlásky. Např.: 2. znak slova uhlir je souhlaska Definuj dvě nové konstanty: CONSONANTS = "qwrtzpsdfghjklxcvbnmščřžďťř"       VOWELS = "aeiouyáéěíóúůý" Vytvoř si novou proměnou my_word a do ní přiřaď libovolný textový řetězec. Pomocí for cyklu a funkce enumerate() projdi celé zadané slovo znak po znaku a pomocí podmínek, rozhodni, zda analyzovaný znak patří do skupiny souhlásek (CONSONANTS) nebo samohlásek (VOWELS) a výstup vhodně vypiš. 1. znak slova rub je souhlaska 2. znak slova rub je samohlaska 3. znak slova rub je souhlaska |

#### 2.3	Funkce zip()

Funkce zip() umožňuje procházení více sekvencí najednou a to vytvářením sekvence *n*-tic. Máme například seznam měst a seznam států, ve kterých města leží. Pokud tyto dva seznamy použijeme jako vstupní argumenty do funkce zip() a výstup vytiskneme, vidíme, že tato funkce vytvořila iterátor podobně jako funkce enumerate().

| Vyzkoušej a analyzuj výstup |
| --- |
| cities = ["Tokyo", "Stockholm", "London", "Paris", "Prague"] countries = ["Japan", "Sweden", "United Kingdom", "France", "Czechia"] print(zip(cities, countries))  print(list(zip(cities, countries))) |

Tento objekt lze také převést na seznam a vidíme, že funkce zip() vytváří sekvenci dvojic z prvků obou seznamů. 

První vytvořená dvojice odpovídá prvním prvkům obou seznamů ("Tokyo", "Japan"), druhá dvojice odpovídá druhým prvkům obou seznamům ("Stockholm", "Sweden") atd.

V cyklech se funkce zip() nejvíce uplatní v případě, že potřebujeme současně v jednom cyklu procházet více proměnných, jejichž hodnoty spolu souvisejí.

| Vyzkoušej a analyzuj výstup |
| --- |
| cities = ["Tokyo", "Stockholm", "London", "Paris", "Prague"] countries = ["Japan", "Sweden", "United Kingdom", "France", "Czechia"] for city, country in zip(cities, countries):     print(f"{city} is in {country}.") |

Funkce zip() lze použít i pro více sekvencí a v následujícím případě tak vznikne iterátor čtveřic.

| Vyzkoušej a analyzuj výstup |
| --- |
| cities = ["Tokyo", "Stockholm", "London", "Paris", "Prague"] countries = ["Japan", "Sweden", "United Kingdom", "France", "Czechia"] population = [13960000, 976000, 8962000, 2176000, 1324000] numbers = range(5) for city, country, residents, number in zip(cities, countries, population, numbers):     print(f"{number}. {city} is in {country} and has {residents} residents.") |

Co se stane v případě, když funkce zip dostane sekvence, které nejsou stejně dlouhé? Například přidáme do seznamu měst Vatikán, který je městským státem a nelze k němu přiřadit konkrétní zemi.

| Vyzkoušej a analyzuj výstup |
| --- |
| cities = ["Tokyo", "Stockholm", "London", "Paris", "Prague", "Vatican"] countries = ["Japan", "Sweden", "United Kingdom", "France", "Czechia"] for city, country in zip(cities, countries):     print(f"{city} is in {country}.") |

## CÍL 3

### VNOŘENÉ CYKLY

#### 3.1	Obecná syntaxe

Vnořený cyklus je situace, kdy jeden cyklus je umístěn v těle cyklu jiného. To znamená, že během jednotlivých iterací vnějšího cyklu dochází k opakovanému provádění vnitřního cyklu. Při zápisu vnořených cyklů je nutné dbát správné odsazení jednotlivých příkazů stejně jako u vnořených podmínek.

| for OUT_VAR in OUT_ITERATIBLE_VAR:     for IN_VAR in IN_ITERATIBLE_VAR:         CODE_BLOCK_C |  |
| --- | --- |

Vyzkoušejme si jednoduchý vnořený cyklu na krátkém příkladu, kdy budeme pouze počítat jednotlivé průchody vnějším a vnitřním cyklem. Které příkazy v níže uvedeném kódu spadají pod vnější cyklus a které pod vnitřní? Jak to poznáme? Předtím než kód spustíme, zkuste také odhadnout, kolikrát se provede vnější cyklus a kolikrát vnitřní.

| Vyzkoušej a analyzuj výstup |
| --- |
| for out_idx in range(3):     print(f"Spouštím {out_idx}. běh vnějšího cyklu.")     for in_idx in range(2):         print(f"\tSpouštím {in_idx}. běh vnitřního cyklu.") |

Počet vnořených cyklů může být libovolný. Měla by však být zachována dobrá čitelnost a výpočetní efektivita kódu (výpočetní náročnost roste s vnořením exponenciálně).

#### 3.2	Příklad

Nyní rozšíříme náš program na analýzu znaků textového řetězce. Mějme proměnnou cities, která obsahuje seznam textových řetězců.

| cities = ["Brno", "Nezamyslice", "Ostrava"] |
| --- |

Každý textový řetězec je složen z libovolného počtu znaků. Naším cílem je provést analýzu všech znaků v každém řetězci. Jelikož už víme, že datová struktura seznam i datový typ textový řetězec jsou iterabilní, lze provést tuto analýzu pomocí vnořených cyklů.

Program bude probíhat následovně:

Vnější cyklus vybere první položku ze seznamu cities a umístí ji do řídící proměnné word.

V první iteraci vnějšího cyklu se spustí vnořený cyklus.

Vnořený cyklus postupně přiřazuje jednotlivé znaky z proměnné word do proměnné char.

V každé iteraci vnořeného cyklu se provádí potřebné operace s proměnou char.

Vnořený cyklus skončí a program se vrací na začátek vnějšího cyklu.

Vnější cyklus pokračuje druhou iterací (druhou položkou seznamu).

Princip vnoření cyklu je ukázán na následujícím vývojovém diagramu.

![image6.png](images/04_flowchart_nested_for.png)


| Úkol |
| --- |
| Vytvoř skript words_analysis.py, který všechny textové řetězce zadané v seznamu analyzuje po jednotlivé znacích a označí je buď za samohlásky nebo souhlásky, stejně jako v minulém úkolu. Definuj opět dvě konstanty: CONSONANTS = "qwrtzpsdfghjklxcvbnmščřžďťř" VOWELS = "aeiouyáéěíóúůý" Vytvoř si novou proměnou cities a do ní přiřaď libovolný seznam textových řetězců odpovídajících tvým oblíbeným městům. Pomocí vnořeného cyklu analyzuj všechna slova v seznamu. Vnější cyklus bude procházet jednotlivé textové řetězce v seznamu. Vnitřní cyklus bude analyzovat každý znak zvlášť a bude tedy podobný tomu z minulého úkolu. |

### SAMOSTATNÝ ÚKOL

#### Střelba na terč

Vytvořte nový skript shooting.py. Do skriptu implementujte program, jehož cílem je simulace střelby na terč. Počet terčů, na které bude program střílet, bude určen uživatelským vstupem. Program se bude řídit následujícími pravidly:

Na terče se střílí vždy postupně od prvního do posledního. Do každého terče se vystřílí plný zásobník, ve kterém je 8 nábojů.

O zásahu terče rozhoduje náhoda. Program vygeneruje náhodné číslo od 0 do 100 (jak na to viz níže). Střelec zasáhne terč, pokud vygenerované číslo bude větší než 45.

Po vystřílení zásobníku se střelec přesune na další terč a celý zásobník se automaticky doplní.

Po vystřílení jednoho zásobníku program vypíše procentuální úspěšnost zásahu na aktuálním terči.

Po ukončení střelby program vypíše procentuální úspěšnost pro celou simulaci.

Náhodné generování čísla lze provést pomocí modulu random. Na první řádek skriptu umístěte kód pro import modulu a funkce pro generování náhodných čísel:

| from random import randrange |
| --- |

Funkce randrange() má stejné vstupní parametry jako funkce range(), se kterou jsme už seznámili. Výstupem je v tomto případě jedno náhodně zvolené číslo z požadovaného rozsahu. Náhodné číslo z intervalu <0; 100> pak můžeme generovat například takto:

| randrange(0, 101) |
| --- |

Tato úloha je zadána bez detailního návodu na postup. Než začnete vytvářet program, zamyslete se, jak by měl vypadat algoritmus a datové struktury pro reprezentaci terčů/zásahů. Vytvořte si vývojový diagram a konzultujte jej s lektorem. 


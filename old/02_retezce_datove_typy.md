# CVIČENÍ 2: TEXTOVÉ ŘETĚZCE A DATOVÉ TYPY

Algoritmizace a programování

## CÍL 1

### TEXTOVÉ ŘETĚZCE

Řetězec je bytové (byte = jednotka informace = 8 bitů) pole reprezentující posloupnost znaků (characters) abecedy. Abeceda je v IT oblasti vždy definována standardem – v případě Pythonu se jedná o standard Unicode. Textový řetězec vytvoříme buď pomocí apostrofů nebo uvozovek:

| my_string = "Hello, world!" my_string = 'Hello, world!' |
| --- |

#### 1.1	Vytváříme řetězce

| Úkol |
| --- |
| Pomocí funkce print() vytiskni řetězec s dvojitými uvozovkami:   "Let’s learn more about Python!"  Vytiskni stejný řetězec, tentokrát s jednoduchými uvozovkami.  Nyní vytiskni řetězec:   "When I grow up, I’ll be a master of the 'snake' language."  Co se stane, pokud vnitřní i vnější uvozovky budou stejného typu? |

Textové řetězce samozřejmě můžeme ukládat do proměnných tak, jak jsme si ukázali v první lekci. Vytisknout poté můžeme přímo obsah proměnné. Připomeňme si:

| error_message = "This program does not do anything yet, please contact the provider." print(error_message) |
| --- |

Jak se bude lišit výstup, pokud zadáme příkaz následujícím způsobem?

| Vyzkoušej a analyzuj výstup |
| --- |
| print("error_message") |

#### 1.2	Znaky v řetězci

Již jsme si řekli, že řetězce sestávají z posloupnosti znaků. Znak může být písmeno, číslice, ale také řada dalších symbolů: např. "?", "#" nebo mezera " ". Každý řetězec má pak určitý počet znaků, který můžeme zjistit pomocí následující syntaxe:

| >>> len("How are you?") 12 |
| --- |

| Vyzkoušej a analyzuj výstup |
| --- |
| >>> len("I am fine!") >>> len("10") >>> len("3 + 1") >>> len(" ") >>> len("") |

#### 1.3	Zpětné lomítko (escape character)

Zpětné lomítko je speciální znak, který začíná speciální sekvenci uvnitř textového řetězce. Tato speciální sekvence třeba pokročilé formátování textového řetězce (odsazení, zalomení řádku). Kromě vytváření řetězců se s nimi běžně setkáte např. při načítání textových dat ze souborů.

| >>> print("I am fine!\nTomorrow will be even better!") I am fine! Tomorrow will be even better! |
| --- |

Speciální sekvence \n vložila to textového řetězce nový řádek. Co dělá sekvence \t?

| Vyzkoušej a analyzuj výstup |
| --- |
| >>> print("I am fine!\tTomorrow will be\neven better!") |

Zpětné lomítko má také jeden důsledek ve chvíli, kdy jej **nechceme** použít jako *escape character*, např. při zadání cesty k souborům a adresářům. V takovém případě musíme lomítko zdvojit:

| working_dir = "C:\\Python\\MyProject" print(working_dir) |
| --- |

| Úkol |
| --- |
| Zjisti počet znaků uložených v proměnné working_dir.  Jak se výstup liší oproti zapsanému řetězci? |

Pro zadávání cest k souborům lze využít speciálního prefixu r. Tento prefix se vždy uvádí před apostrofy či uvozovky a indikuje tak zvláštní zacházení s textovým řetězcem. V tomto případě to znamená, že budeme zadávat surový textový řetězec a každý znak bude představovat sám sebe.

| Vyzkoušej a analyzuj výstup |
| --- |
| working_dir = r"C:\Python\MyProject" print(working_dir) |

#### 1.4	Skládání řetězců

Pokud máme k dispozici dva a více řetězců, můžeme je vzájemně skládat a vytvořit z nich jeden dlouhý řetězec. To se hodí třeba v případě, kdy jednu část řetězce potřebujeme použít vícekrát v kombinaci s jiným řetězcem, jehož obsah se mění (např. jméno uživatele):

| print("This lecture was prepared by:" + " " + "Michal") |
| --- |

Pro skládání řetězců můžeme využít přímo názvy proměnných, ve kterých jsou řetězce uloženy:

| Vyzkoušej a analyzuj výstup |
| --- |
| message = "This lecture was prepared by:" lector_name = "Michal" print(message + " " + lector_name) |

Textové řetězce s proměnným obsahem můžeme získat z různých zdrojů. Tím může být databáze, soubor na pevném disku nebo třeba komunikační kanál mezi webovými servery. My si ukážeme jednoduché načtení textového řetězce pomocí konzole a klávesnice:

| input("Enter your name: ") |
| --- |

| Samostatný úkol |
| --- |
| Vytvoř skript welcome.py.  Ve skriptu vybídni uživatele k zadání svého jména pomocí funkce input() a zadané jméno přiřaď do proměnné user_name.  Vypiš textový řetězec (se jménem v proměnné user_name):   "Well done, user_name. You are such an amazing programmer!"  Zajisti, aby před zobrazením zprávy byly všechny textové řetězce uloženy v proměnných. |

#### 1.5	Opakování řetězců

Už jsme si ukázali, že operátor + může mít i další funkci než sčítání dvou čísel. Obdobně je to i s operátorem *, který lze použít pro opakování textového řetězce.

| >>> print("Let’s sing:", "la" * 5) Zazpivame si: lalalalala |
| --- |

Kromě toho, že funkce print() umožňuje vytisknout různé hodnoty, je možné i ovládat i formu jejich výpisu. Na příkladech níže si vyzkoušíme, jak se jednotlivé výpisy liší a co způsobuje jejich odlišnost.

| Vyzkoušej a analyzuj výstup |
| --- |
| print("Let’s sing:", "la" * 5, sep="") print("Let’s sing:", "la" * 5, "la" * 5, "la" * 5, sep="\n") print("la" * 5, end="") print("la" * 5, "la" * 5, sep="", end="!") |

#### 1.6	Výběr znaku (indexace)

V některých případech potřebujeme naopak z dlouhého řetězce získat jeho část (např. z rodného čísla rok narození). Pro jednoduchost začneme výběrem jednoho znaku. Znaky lze z řetězce vybrat pomocí operace **vybírání** (angl. *subscripting*). Ta se v Pythonu zapisuje podobně jako volání funkce s tím rozdílem, že použijeme **hranaté závorky**. Např. pro znak na 2. pozici:

| Vyzkoušej a analyzuj výstup |
| --- |
| second_character = "Slytherin"[2] print(second_character) |

Pokud jste vše provedli správně, získali jste znak na 3. pozici. Proč tomu tak je? Python jako většina programovacích jazyků určuje pořadí prvků od hodnoty 0. Pořadí znaků v našem textovém řetězci je tedy následující:

| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| znak | S | l | y | t | h | e | r | i | n |

| Úkol |
| --- |
| Uprav zdrojový kód tak, aby program zobrazil 5. znak řetězce "Slytherin".  Vytiskni do terminálu textový řetězec "Sly" pomocí indexace původního slova a spojení textových řetězců. |

Výběr znaku (či obecně prvku) můžeme samozřejmě provést také pomocí **názvu** proměnné, pokud v ní máme textový řetězec uložen. Co se navíc stane, pokud pro výběr použijeme záporné číslo? Pojďme si obě varianty vyzkoušet na příkladu:

| Vyzkoušej a analyzuj výstup |
| --- |
| my_house = "Slytherin" second_character = my_house[1]  nth_character = my_house[-1]  print(second_character) print(nth_character) |

Poslední výpis zobrazí poslední znak zadaného textového řetězce. Záporná čísla lze tedy použít pro indexování od konce. Indexaci znaků můžeme tedy v Pythonu provádět dvojím způsobem:

| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| záporný index | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
| znak | S | l | y | t | h | e | r | i | n |

|  | Výběr (subscripting) pomocí pořadí prvku (indexu) můžeme provést pouze u takových proměnných, které jsou sekvenční (obsahují posloupnost více prvků) a iterovatelné. O iterovatelných proměnných si povíme něco později. Zde si vystačíme s konstatováním, že jde o sekvenci prvků, které mají jednoznačně určené pořadí (přiřazený index), podobně jako v tabulce výše. |
| --- | --- |

#### 1.7	Řezání řetězců (slicing)

Na příkladu skládání řetězce "Sly" jsme si ukázali, že vyjmutí více znaků z řetězce (tzv. podřetězec angl. *substring*) pomocí indexace není příliš praktické. V Pythonu proto můžeme delší části řetězce (a obecně sekvenčních proměnných) vybírat pomocí tzv. **řezání** angl. *slicing*. Slicing vytváříme podobně jako indexaci pomocí **hranatých závorek**, současně však pomocí operátu dvojtečka vymezíme interval (“od” a “do”), ve kterém budeme řezání provádět: 

| quidditch_match = "Slytherin beats Gryffindor"  quidditch_team = quidditch_match[0:9] message = quidditch_team + " " + "wins!" print(message) |
| --- |

Pokud potřebuje vyseknout část řetězce od prvního nebo do posledního prvku, můžeme využít (a budeme ji preferovat) také zkrácenou variantu bez uvedení indexu krajních prvků:

| quidditch_team = quidditch_match[:9] |
| --- |

Všimněte si, že poslední prvek (10. znak; index č. 9) již není ve výběru obsažen. To může být ze začátku trochu matoucí, nicméně nám to umožňuje hezky čitelnou syntaxi např. v případě, kdy potřebujeme řetězec rozdělit na dvě části:

| idx = 9 print(quidditch_match[:idx] + quidditch_match[idx:]) |
| --- |

Zde jsme pro řezání řetězce použili hodnotu v proměnné idx. Rovnou si tedy ukážeme, co v takovém případě může být častým zdrojem chyb:

| idx = 5.5 print(quidditch_match[:idx] + quidditch_match[idx:]) |
| --- |
| Traceback (most recent call last): … TypeError: slice indices must be integers or None or have an __index__ method |

Podle chybové hlášky vidíme, že hodnoty, které používáme pro indexaci a řezání řetězců musí být celá čísla (angl. *integer*).

Slicing nám kromě vyříznutí intervalu umožňuje zvolit krok mezi jednotlivými prvky (tedy “od”, “do” a “po”). Můžeme tak vybrat například každý druhý znak nebo obrátit pořadí znaků:

| print(quidditch_match[:9:2]) |
| --- |

| Vyzkoušej a analyzuj výstup |
| --- |
| print(quidditch_match[2:10:3]) print(quidditch_match[9::-1]) print(quidditch_match[-5:]) print(quidditch_match[:]) |

#### 1.8	Operace s textovými řetězci

Operace s textovými řetězci můžeme provádět pomocí vyhrazených operátorů, funkcí a metod. Některé základní operátory už znáte z minulé lekce, např. pro vyhodnocení shody dvou řetězců:

| Vyzkoušej a analyzuj výstup |
| --- |
| school = "Hogwarts" print(school == "Hogwarts") print(school == "HogWarts") print(school != "") |

Všimněte si, že při porovnání řetězců záleží na velikosti písmen. Pokud bychom chtěli porovnat řetězce bez ohledu na velikost znaků, museli bychom oba řetězce převést buď na malá nebo velká písmena (to si ukážeme za chvíli). 

Teď si vyzkoušíme ještě jeden šikovný trik. Pomocí operátoru in zjistíme, jestli v sobě řetězec obsahuje jiný podřetězec:

| Vyzkoušej a analyzuj výstup |
| --- |
| item = "vanilla ice cream" my_favourite = "lemon" my_hatred = "smurf"  print(my_favourite in item) print("vanilla" in item) print(my_hatred not in item) |

K tomu, jak tyto výrazy použít k řízení našich programů, se dostaneme v dalších lekcích (takže si je opravdu dobře zapamatujte). Nyní se podíváme na některé metody, které mohou naše řetězce transformovat. Metoda je na rozdíl od funkce svázána přímo s objektem (hodnotou). Metody pro řetězce tedy (zpravidla) nebudou fungovat u jiných objektů, např. celých čísel. Metody voláme pomocí tečkové notace – za objekt napíšeme tečku, název metody a kulaté závorky s případnými argumenty (podobně jako u funkcí):

| Vyzkoušej a analyzuj výstup |
| --- |
| teachers_name = "Severus" print(teachers_name.upper()) print(teachers_name.lower()) print(teachers_name) |

|  | Všimněte si, že metoda nemění obsah původní proměnné, ale vrací nový textový řetězec. Vytvořený řetězec se totiž nedá změnit, je možné jen vytvořit nový – odvozený. Takovým objektům se v Pythonu říká nezměnitelné (angl. immutables). |
| --- | --- |

Abychom mohli s výstupy z metod u neměnných objektů dále pracovat, obdobně jako u funkcí, přiřadíme jejich výsledek do proměnné.

| Vyzkoušej a analyzuj výstup |
| --- |
| teachers_name = "Severus" new_teachers_name = teachers_name.upper() print(teachers_name) print(new_teachers_name) |

V závěru si ještě ukážeme, jak rozdělit řetězce na základě specifického dělícího znaku pomocí metody split(). Dělící znaky se zapisují jako vstupní argumenty do kulatých závorek. Tato operace se hodí v případech, kdy potřebujeme z řetězce “vytáhnout” jednotlivé podřetězce, které jsou odděleny jednotným oddělovačem (např. chceme rozdělit větu na jednotlivá slova). Výstupem jsou rozdělené podřetězce uložené do datové struktury nazývané **seznam** (angl. *list*). S tímto faktem si dnes vystačíme, se seznamy totiž budeme pracovat v dalších lekcích.

| Vyzkoušej a analyzuj výstup |
| --- |
| teachers_string = "Snape, Dumbledore, Lupin"  teachers_list = teachers_string.split(",") print(teachers_list)  another_teachers_list = teachers_string.split(", ") print(another_teachers_list) |

|  | Funkcí a metod pro práci s řetězci je celá řada. Podívej se do taháku (Cheat sheet) na základní přehled těch nejvíce užitečných a zjisti, co s textovým řetězci dělají. |
| --- | --- |

#### 1.9	Formátovaný řetězec (f-string)

*F-string* je další speciální typ řetězce s prefixem, který umožňuje vložit výrazy a hodnoty proměnných, aniž bychom museli převádět jejich datový typ (o datových typech si řekneme o něco později, nyní si vystačíme s jednoduchým příkladem). To se hodí např. ve chvíli, kdy potřebujeme uložit stav našeho programu (hodnotu proměnné) do textového souboru nebo jej zobrazit uživateli. F-string vytvoříme připojením znaku *f* před textový řetězec. Konkrétní výrazy pak můžeme umístit vložením výrazu do **složených závorek**:

| points = 235 message = f"Your house has {points} points." print(message) |
| --- |

| Vyzkoušej a analyzuj výstup |
| --- |
| print(f"Your house has points points.") print(f"Your house has points + 15 points.") print(f"Your house has {points + 15} points.") |

## CÍL 2

### DATOVÉ TYPY

Datové typy jsou zjednodušeně řečeno zavedené **standardy**, které nám umožňují srozumitelně interpretovat (převést) data uložená v binární sekvenci. Programátorům dále umožňuje vhodná volba datového typu do určité míry (především v oblasti data science) optimalizovat paměťové prostředky, které program využívá. Datový typ stanovuje jednak délku slova, ale také způsob interpretace binárního zápisu. O datových typech by se dalo hloubat dlouho, proto** **si ukážeme primárně některé praktické příklady, které se mohou hodit.

#### 2.1	Ověření datového typu

Na začátku si ukážeme užitečnou funkci isinstance(), pomocí které můžeme zjistit, jaký datový typ konkrétní proměnná obsahuje. Pomocí této funkce můžeme zajistit, aby program dostal jen taková data, se kterými umí pracovat (a např. nepočítal odmocninu z textového řetězce). Výstupem funkce je hodnota True nebo False.

| Vyzkoušej a analyzuj výstup |
| --- |
| input_number = "325.8"  is_string = isinstance(input_number, str) print(is_string)  is_float = isinstance(input_number, float) print(is_float) |

#### 2.2	Převod číselných datových typů

Převod mezi číselnými typy využijeme hlavně ve chvíli, kdy potřebujeme ušetřit paměťové prostředky a nevadí nám snížení přesnosti. Např. pokud nám někdo pošle obrazová data (typicky *int8*) ve formě 32 bitových čísel s plovoucí čárkou (*float*) a zbytečně tak zahltí paměťový prostor:

| gray_pixel = 128.00 # datovy typ float gray_pixel = int(gray_pixel) print(gray_pixel) |
| --- |

a opačným směrem:

| gray_pixel = float(gray_pixel) |
| --- |

### **2.3	Číselná reprezentace znaků**

Zejména při analýze textu a práci s textovými řetězci se pak hodí převod znaků na posloupnost celých čísel (tomuto procesu se říká vektorizace):

| my_string = "ž" numerical = ord(my_string) print(numerical) |
| --- |

a opět opačným směrem:

| my_string = chr(numerical) |
| --- |

Divíte se, proč Python převedl znak "ž" zrovna na hodnotu 382? Python kóduje znaky pomocí kódování UTF-8. Vyhledejte tabulku znaků pro kódování UTF-8 a zkontrolujte v ní pořadí znaku. Pořadí je někdy uvedeno v hexadecimální soustavě, převod můžete provést pomocí funkce hex(). 

V prostředí PyCharm lze změnit kódovací abecedu, pomocí které budou zobrazovány znaky v editoru. Tuto možnost naleznete v pravém dolním rohu. Zkuste změnit kódování z UTF-8 na US-ASCII. Co se po změně stalo se znakem "ž" ve vašem skriptu a proč?

### **2.4	Převod čísel na řetězce a naopak**

Občas se hodí naše data převést do jiného datového typu, než ve kterém jsme je obdrželi. Taková situace může nastat např. při načítání číselných hodnot z textového souboru. Číslo totiž v takovém případě nereprezentuje skutečnou hodnotu, ale pouze symbol či znak, pomocí kterého tuto hodnotu vyjadřujeme:

| Vyzkoušej a analyzuj výstup |
| --- |
| my_number = "1022" converted_number = int(my_number) print(converted_number) |

a opačně:

| my_number = str(converted_number) |
| --- |

| Úkol |
| --- |
| Pomocí funkce int() zkus převést řetězec: "-85", "30.2" a "12A".  Zkus převést stejné řetězce pomocí funkce float(). Jaký je rozdíl ve výstupu? |

Co se však stalo, když uživatel místo čísla zadal jiný znak abecedy? Program velmi pravděpodobně vrátil chybovou zprávu. Pokud chceme takovou situaci ošetřit bez přerušení běhu programu, můžeme použít syntaxi pro zpracování výjimek: 

| try:     int("Yes!") except ValueError:     print("String cannot be converted to integer") |
| --- |

Pomocí bloku try programu říkáme, aby se o převod jen pokusil, avšak bez ukončení chybou, pokud se převod nepovedl. V případě selhání program vrátí odpověď formulovanou v bloku except, ale pokračuje dál bez přerušení. Výjimku (angl. *exception*), kterou chcete zachytit, je zpravidla nutné definovat v hlavičce bloku except. Touto problematikou se v tomto kurzu zabývat nebudeme, detaily však můžete nalézt v dokumentaci.

Nakonec se podíváme na speciální hodnoty u číselného typu s plovoucí čárkou – nekonečno, mínus nekonečno a tzv. nehodnotu (angl. *Not a Number* - *NaN*). S těmito hodnotami se setkáte zejména u numerických výpočtů, a to třeba ve chvíli, kdy výstupním výrazem je číslo mimo rozsah daného datového typu (tzv. přetečení paměti):

| Vyzkoušej a analyzuj výstup |
| --- |
| infinity = float("Inf") minus_infinity = float("-Inf") not_number = float("NaN") |

## SAMOSTATNÉ ÚKOLY

| Samostatný úkol |
| --- |
| Vytvoř skript replace_char.py.  Ve skriptu vyzvi uživatele, aby v terminálu zadal slovo (textový řetězec), jedno číslo a jeden znak.  Současně ulož slovo do proměnné my_word, číslo do proměnné char_pos a znak do proměnné new_char.  Doplň skript tak, aby program zaměnil znak v řetězci my_word na pozici char_pos za znak uložený v proměnné new_char.  Doplň skript o tisk upraveného textového řetězce do terminálu. |

| Samostatný úkol |
| --- |
| Vytvoř skript capitalize_name.py.  Ve skriptu vyzvi uživatele, aby v terminálu zadal své jméno a následně své příjmení.  Oba textové řetězce se ulož do proměnných name a surname.  Doplň skript tak, aby program u obou textových řetězců převedl první znak na velké písmeno a zbytek textu na malá písmena.  Na závěr spoj dohromady upravené textové řetězce tak, aby první bylo jméno pak následovala mezera a na závěr bylo příjmení.  Doplň skript o tisk spojeného upraveného textového řetězce do terminálu. |


# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## CÍL 2: PRVNÍ PROGRAM A ZÁKLADY SYNTAXE

Nyní se podíváme na samotný kód. Otevřete soubor `main.py`, který vidíte v levém panelu (Project View).

### 2.1 Hello World

Tradičně začínáme programem, který vypíše pozdrav. V Pythonu k tomu slouží funkce `print()`.

Když otevřete soubor `main.py`, uvidíte, že nám `uv` vygeneroval profesionální strukturu s funkcí `main()`. Pro začátek si to ale zjednodušíme. **Smažte celý obsah souboru** a napište pouze tento jeden řádek:

```python
print("Hello world!")
```

Program jednoduše spustíte stisknutím zelené šipky **Run** vpravo nahoře (nebo klávesovou zkratkou `Shift + F10`).

> **Poznámka:** Program lze spustit i v terminálu příkazem `python main.py`.

🎉 **Gratulujeme!** Právě jste spustili svůj první Python program. Může to vypadat jednoduše, ale každý programátor začínal právě tímto – výpisem "Hello World!". Od tohoto bodu vede cesta k jakékoliv aplikaci, kterou si dokážete představit.

Zkuste upravit text v uvozovkách na `"Hello Python!"` a spusťte program znovu.

> ** Tip: Jak organizovat kód při procvičování?**
>
> Během cvičení budete psát mnoho programů. Máte dvě možnosti:
>
> **1. Více souborů (doporučeno):**
> - V levém panelu (Project View) klikněte pravým tlačítkem na složku projektu
> - Zvolte **New → Python File** a pojmenujte soubor (např. `promenne.py`, `kalkulacka.py`)
> - PyCharm soubor vytvoří a otevře
> - Spustíte stejně jako `main.py` (zelená šipka nebo `Shift + F10`)
> - **Výhoda:** Máte přehled, můžete se vracet k starším příkladům
>
> **2. Jeden soubor s komentováním:**
> - Když chcete zkusit nový kód, zakomentujte starý (`Ctrl + /`)
> - Napište nový kód pod něj
> - **Výhoda:** Vše na jednom místě, rychlé experimentování
> - **Nevýhoda:** Časem se v tom ztratíte
>
> **Který způsob zvolit?** Pro úkoly vytvářejte nové soubory. Pro rychlé zkoušení syntaxe používejte komentování.

**O komentování:**
Komentáře slouží k vysvětlení kódu a Python je ignoruje. Začínají znakem `#`.

⌨️ **Klávesová zkratka:** **`Ctrl + /`** (označte řádky a stiskněte zkratku pro zakomentování/odkomentování).

```python
# Toto je komentář
print("Ahoj") # Komentář může být i za příkazem
```

---

#### ÚKOL: Vytvoř svůj první soubor

Vyzkoušej si vytvoření nového souboru:

1. Klikni pravým tlačítkem na složku projektu v levém panelu
2. Vyber **New → Python File**
3. Pojmenuj soubor `pozdrav.py`
4. Do nového souboru napiš:
 ```python
 # Můj první vlastní soubor
 print("Ahoj ze souboru pozdrav.py!")
 ```
5. Spusť program (zelená šipka)

**Tip:** Všimni si, že PyCharm automaticky spustí nově vytvořený soubor.

---

### 💻 Důležité znaky pro programování

Při programování budete potřebovat speciální znaky. Zde je přehled, jak je napsat na **české** a **anglické** klávesnici:

| Znak | Název | Česká klávesnice | Anglická klávesnice |
|------|-----------------|-----------------------------------------------------------------------|------------------------------------------------------|
| `#` | Hash (mřížka) | pravý <kbd>Alt</kbd> + <kbd>X</kbd> | <kbd>Shift</kbd> + <kbd>3</kbd> |
| `()` | Kulaté závorky | <kbd>Shift</kbd> + <kbd>)</kbd>/<kbd>)</kbd> (vedle <kbd>Enter</kbd>) | <kbd>Shift</kbd> + <kbd>9</kbd>/<kbd>0</kbd> |
| `[]` | Hranaté závorky | pravý <kbd>Alt</kbd> + <kbd>F</kbd>/<kbd>G</kbd> | <kbd>[</kbd>/<kbd>]</kbd> |
| `{}` | Složené závorky | pravý <kbd>Alt</kbd> + <kbd>B</kbd>/<kbd>N</kbd> | <kbd>Shift</kbd> + <kbd>[</kbd>/<kbd>]</kbd> |
| `<>` | Lomené závorky | pravý <kbd>Alt</kbd> + <kbd>,</kbd>/<kbd>.</kbd> | <kbd>Shift</kbd> + <kbd>,</kbd>/<kbd>.</kbd> |
| `/` | Lomítko | <kbd>/</kbd> | <kbd>/</kbd> |
| `\` | Zpětné lomítko | pravý <kbd>Alt</kbd> + <kbd>Q</kbd> | <kbd>\\</kbd> |
| `_` | Podtržítko | <kbd>Shift</kbd> + <kbd>-</kbd> | <kbd>Shift</kbd> + <kbd>-</kbd> (vedle <kbd>0</kbd>) |
| `:` | Dvojtečka | <kbd>Shift</kbd> + <kbd>.</kbd> | <kbd>Shift</kbd> + <kbd>;</kbd> |
| `;` | Středník | <kbd>;</kbd> (nad <kbd>Tab</kbd>) | <kbd>;</kbd> |
| `"` | Uvozovky | <kbd>Shift</kbd> + <kbd>ů</kbd> | <kbd>Shift</kbd> + <kbd>'</kbd> |
| `'` | Apostrof | <kbd>Shift</kbd> + <kbd>¨</kbd> | <kbd>'</kbd> |

> ** Proč programátoři často používají anglickou klávesnici?**
> Speciální znaky potřebné pro programování (`{}`, `[]`, `/`, `\`) jsou na anglické klávesnici **mnohem dostupnější** – většinou stačí jeden <kbd>Shift</kbd> místo pravého <kbd>Alt</kbd> kombinací. To výrazně zrychluje psaní kódu. Pokud hodně programujete, zvažte přepnutí layoutu na US International (ale každému vyhovuje něco jiného).

> **⚠️ Pozor na klávesu <kbd>Insert</kbd>!**
> Pokud omylem stisknete <kbd>Insert</kbd>, přepne se režim na přepisování - poznáte to podle **širšího kurzoru** (místo tenké čárky). Nový text pak přepisuje existující znaky místo vkládání. Vypnete stisknutím <kbd>Insert</kbd> znovu.

---

### 2.2 Proměnné (Variables)

Proměnná slouží k uložení hodnoty (čísla, textu). V Pythonu nemusíme určovat typ proměnné předem, pozná se automaticky.

Příklad (doplňte do svého souboru místo předchozího kódu):
```python
name = "Petr"
age = 20
greeting = "Ahoj"

print(greeting)
print(name)
print(f"Věk: {age}") # f-string: elegantnejsi zpusob vypisu promennych
```

> **Poznámka o f-stringových literálech (f-string):**
> Před uvozovky napíšeme `f` a do složených závorek `{}` můžeme vložit proměnnou nebo výraz. Python automaticky převede hodnotu na text a vloží ji do řetězce.

**Pravidla pro pojmenování proměnných podle PEP 8:**

> **📘 Co je PEP 8?**
> **PEP 8** (Python Enhancement Proposal 8) je **oficiální průvodce stylem** pro psaní kódu v Pythonu. Definuje konvence, jak má vypadat "hezký" a čitelný Python kód – od mezer kolem operátorů přes pojmenování proměnných až po délku řádků.
>
> **Proč PEP 8 dodržovat?**
> - **Čitelnost:** Váš kód vypadá jako ostatní Python kód → ostatní ho snáze pochopí
> - **Profesionalita:** Dodržování PEP 8 je standard v celém Python ekosystému
> - **Spolupráce:** V týmových projektech všichni píší stejným stylem
> - **AI nástroje:** GitHub Copilot a podobné nástroje očekávají PEP 8 styl
>
> 📖 Plný text najdete na: [python.org/dev/peps/pep-0008](https://peps.python.org/pep-0008/)
>
> **Pro začátečníky:** Zatím se soustředíme na základní pravidla níže. S pokročilými konvencemi se seznámíte postupně.

1. **Snake case pro proměnné a funkce**: Názvy píšeme **malými písmeny**, slova oddělujeme **podtržítkem** (`_`).
 ```python
 # SPRÁVNĚ (snake_case)
 user_name = "Marie"
 total_score = 150
 patient_temperature = 37.5
 is_valid = True

 # ❌ ŠPATNĚ (camelCase - používá se v Javě/JavaScriptu)
 userName = "Marie"
 totalScore = 150

 # ❌ ŠPATNĚ (PascalCase - v Pythonu jen pro třídy)
 UserName = "Marie"
 TotalScore = 150
 ```

2. **Konstanty velkými písmeny**: Hodnoty, které se **nemění**, píšeme **VELKÝMI_PÍSMENY**.
 ```python
 # Konstanty - obvykle se definují na začátku souboru
 MAX_SPEED = 120
 PI = 3.14159
 DEFAULT_TEMPERATURE = 36.6
 ```

3. **Výstižnost před stručností**: Název by měl **popisovat obsah** – raději delší a jasný než krátký a nejasný.
 ```python
 # SPRÁVNĚ - jasné
 patient_age = 65
 heart_rate_bpm = 72

 # ❌ ŠPATNĚ - co znamená "p", "a", "hr"?
 p = 65
 a = 65
 hr = 72
 ```

4. **Angličtina**: Mezinárodní standard – usnadní spolupráci a použití ve větších projektech.
 ```python
 # DOPORUČENO
 temperature = 37.5
 patient_name = "Jan Novák"

 # ⚠️ Funguje, ale není standard (pro školní projekty OK)
 teplota = 37.5
 jmeno_pacienta = "Jan Novák"
 ```
 > V tomto kurzu můžete v učebních příkladech používat i české názvy pro lepší pochopení. V reálných projektech ale preferujte angličtinu.

5. **Bez diakritiky**: Python sice zvládá háčky a čárky, ale lepší je se jim vyhnout.
 ```python
 # SPRÁVNĚ
 cislo = 42
 vysledek = 100

 # ❌ ŠPATNĚ (technicky funguje, ale není doporučeno)
 číslo = 42
 výsledek = 100
 ```

6. **Nezačínat číslem**: Proměnná nesmí začínat číslicí.
 ```python
 # SPRÁVNĚ
 place_1 = "zlato"
 patient_001 = "Jan Novák"

 # ❌ CHYBA - nelze zkompilovat
 1_place = "zlato"
 001_patient = "Jan Novák"
 ```

7. **Nepřepisujte vestavěné funkce**: Nepoužívejte názvy, které v Pythonu už něco znamenají (`print`, `len`, `list`, `str`, `sum`, `max`, `min`...).
 ```python
 # ❌ ŠPATNĚ - přepíše vestavěnou funkci
 print = "Nějaký text"
 print("Ahoj") # CHYBA! print už není funkce, ale text!

 # SPRÁVNĚ
 message = "Nějaký text"
 output_text = "Nějaký text"
 print(message) # Funguje korektně
 ```

> ** Poznámka o podtržítcích:**
> - **Podtržítko na začátku** (`_internal`, `__private`): Označuje "interní" proměnné. Používá se až v pokročilejším programování při tvorbě modulů a tříd.
> - **Podtržítko na konci** (`class_`, `type_`): Používá se, když chceme použít název, který je rezervované klíčové slovo Pythonu (např. `class`, `type`, `list` jsou rezervované, takže použijeme `class_`, `type_`, `list_`).

---

#### ÚKOL: První proměnná

Vytvořte proměnnou `course` s hodnotou `"Algoritmizace"` a vypište větu:
```
Vítejte v kurzu Algoritmizace
```

**Tip:** Použijte proměnnou uvnitř funkce `print()` (například pomocí f-stringu).

---

### 2.3 Matematické operátory

Python funguje skvěle jako kalkulačka. K dispozici máme základní operátory:

| Operace | Znak | Příklad | Výsledek |
|--------------------------------|------|----------|----------|
| Sčítání | `+` | `5 + 3` | `8` |
| Odčítání | `-` | `10 - 2` | `8` |
| Násobení | `*` | `4 * 2` | `8` |
| Dělení (vrací desetinné číslo) | `/` | `10 / 2` | `5.0` |
| Celočíselné dělení | `//` | `7 // 3` | `2` |
| Zbytek po dělení (modulo) | `%` | `7 % 3` | `1` |
| Umocnění | `**` | `2 ** 3` | `8` |

```python
# Vyzkoušejte si různé operátory
print(2 + 3) # 5
print(10 - 20) # -10
print(2 * 5) # 10
print(10 / 3) # 3.333...
print(10 // 3) # 3 (celočíselné dělení)
print(10 % 3) # 1 (zbytek)
print(2 ** 6) # 64 (dvě na šestou)
```

**Praktický příklad:**
```python
# Výpočet BMI (Body Mass Index)
weight = 75 # kg
height = 1.80 # m

bmi = weight / (height ** 2)
print(f"Vaše BMI: {bmi}") # Vypíše na 1 des. místo
```

**Příklad: Zbytek po dělení (modulo)**

Modulo `%` nám vrátí zbytek po celočíselném dělení. Hodí se např. k určení, zda je číslo sudé.

```python
number = 14
divisor = 3

remainder = number % divisor
print(f"Číslo {number} děleno {divisor} má zbytek {remainder}")
```

---

#### ÚKOL: Výpočet daně z příjmu

Představte si, že máte měsíční příjem 25 000 Kč a chcete spočítat, kolik zaplatíte na dani za celý rok. Daňová sazba je 15 %.

Vytvořte program, který:

1. Definuje konstanty `MONTHS = 12` a `TAX_RATE_PCT = 15`
2. Vytvoří proměnnou `monthly_income = 25000`
3. Vypočítá roční příjem (měsíční příjem × počet měsíců)
4. Převede procenta na desetinné číslo (15 % → 0.15)
5. Vypočítá celkovou daň (roční příjem × daňová sazba)
6. Vypíše oba výsledky pomocí f-stringu

---

### 2.4 Logické operátory

Kromě počítání často potřebujeme hodnoty porovnávat. Výsledkem je vždy `True` (pravda) nebo `False` (nepravda).

| Operace | Znak | Příklad | Výsledek |
|------------------|------|-----------|----------|
| Rovnost | `==` | `5 == 5` | `True` |
| Nerovnost | `!=` | `5 != 3` | `True` |
| Větší než | `>` | `5 > 5` | `False` |
| Menší než | `<` | `2 < 5` | `True` |
| Větší nebo rovno | `>=` | `5 >= 5` | `True` |
| Menší nebo rovno | `<=` | `4 <= -5` | `False` |

```python
# Vyzkoušejte porovnání
print(5 > 2) # True
print(10 == 10) # True
print(5 != 5) # False
print(3 < 2) # False
print(7 <= 10) # True
```

**Praktický příklad:**
```python
temperature = 38.5

has_fever = temperature >= 38.0
print(f"Horečka: {has_fever}") # Vypíše True nebo False
```

### 2.5 Seznamy a indexace

**Seznam** (list) je sbírka hodnot uzavřená v hranatech závorkách `[]`. Můžeme v něm mít čísla, texty, nebo cokoliv jiného.

```python
# Seznam teplot pacientů
temperatures = [36.6, 37.2, 38.1, 36.9, 37.5]

# Přístup k jednotlivým prvkům pomocí indexu (začíná od 0!)
print(temperatures[0]) # 36.6 (první prvek)
print(temperatures[1]) # 37.2 (druhý prvek)
print(temperatures[4]) # 37.5 (pátý prvek)
```

> ⚠️ **Důležité:** Indexování začíná od **0**, ne od 1! První prvek je `seznam[0]`, druhý je `seznam[1]` atd.

#### Funkce len() - zjištění délky

Funkce `len()` nám řekne, **kolik prvků** je v seznamu (nebo kolik znaků v textu).

```python
# Délka seznamu
temperatures = [36.6, 37.2, 38.1, 36.9, 37.5]
count = len(temperatures)
print(f"Máme {count} měření teploty") # Máme 5 měření teploty

# Délka textu (počet znaků včetně mezer)
name = "Jan Novák"
length = len(name)
print(f"Jméno má {length} znaků") # Jméno má 9 znaků
```

**Praktický příklad:**
```python
patients = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]

first_patient = patients[0]
second_patient = patients[1]

print(f"První pacient: {first_patient}")
print(f"Druhý pacient: {second_patient}")
```

### 2.6 Jednoduché podmínky a odsazování

Podmínky nám umožňují větvit program – vykonat určitou část kódu jen tehdy, když platí nějaký předpoklad.

#### Odsazování (Indentation)

V Pythonu je odsazování **klíčové** pro strukturu programu. Určuje, které příkazy patří do bloku (např. do podmínky nebo cyklu).
* Používáme **4 mezery** (nebo 1 tabulátor, ale nemíchejte to!).
* ⌨️ **Klávesové zkratky:**

 * **`Tab`** – odsadí řádek (přidá 4 mezery)
 * **`Shift + Tab`** – odsune řádek zpět (odebere 4 mezery)
 * **Tip:** Můžete označit více řádků a odsadit/odsunout je najednou!

#### Podmínky if/else

Používáme klíčová slova `if` (když) a `else` (jinak). Důležité je **odsazení** kódu pod podmínkou!

```python
number = 10

if number > 5:
 print("Číslo je větší než 5") # Odsazený řádek = patří do podmínky
else:
 print("Číslo je menší nebo rovno 5")
```

**Praktický příklad:**
```python
temperature = 38.5

# Detekce horečky (>= 38 °C)
if temperature >= 38.0:
 print("Pacient má horečku!")
else:
 print("Teplota v normě")
```

---

#### ÚKOL: Kontrola srdeční frekvence

Napište program, který kontroluje srdeční frekvenci pacienta.

Vytvořte:

- Proměnnou `heart_rate` s hodnotou 105 (tepů za minutu)
- Konstantu `TACHYCARDIA_LIMIT = 100` (hranice pro zrychlený tep)

Program má pomocí podmínky zkontrolovat, zda je `heart_rate` větší než limit, a vypsat:

- Pokud ANO: `"Zrychlený tep: 105 tepů/min (limit: 100)"`
- Pokud NE: `"Srdeční frekvence v normě"`

**Tip:** Použijte f-stringy pro výpis hodnot proměnných.

---

### 2.7 Cyklus for

Cyklus `for` nám umožňuje opakovat určitou činnost pro prvky v nějaké skupině. Nejprve si ukážeme opakování pomocí čísel.

#### For s range()
Funkce `range(n)` vygeneruje čísla od 0 do *n*-1.

```python
# Vypíše "Ahoj" 5x pod sebou a pak se rozloučí
for i in range(5):
 print(f"Ahoj {i}")
 print("...další řádek v cyklu (taky odsazený)")

print("Toto se vypíše až po skončení cyklu (už není odsazené).")
```

Řídící proměnná `i` v každém kroku cyklu nabývá nové hodnoty (`0`, `1`, `2`, `3`, `4`).

#### For se seznamem

Již víme, že seznam je sbírka hodnot (viz sekce 2.5). Nyní si ukážeme, jak projít **všechny** prvky v seznamu pomocí cyklu `for`.

```python
# Seznam oblíbených ovoce
fruits = ["jablko", "hruška", "banán", "pomeranč"]

# Projdeme všechny položky a vypíšeme je
for fruit in fruits:
 print(f"Mám rád {fruit}")
```

Výstup bude:
```
Mám rád jablko
Mám rád hruška
Mám rád banán
Mám rád pomeranč
```

V každém kroku cyklu proměnná `fruit` dostane hodnotu jednoho prvku ze seznamu.

---

#### ÚKOL 1: Kontrola lůžek na oddělení

Na oddělení je 10 lůžek očíslovaných od 0 do 9. Napište program, který pomocí cyklu `for` vypíše všechna čísla lůžek ve formátu:

```
Lůžko č. 0
Lůžko č. 1
Lůžko č. 2
...
```

**Tip:** Použijte `range(10)` a f-string pro výpis.

---

#### ÚKOL 2: Výpis teplot pacientů

Vytvořte seznam `temperatures` s alespoň 5 hodnotami teplot (např. `[36.6, 37.2, 38.1, 36.9, 37.5]`).

Pomocí cyklu `for` projděte všechny teploty a vypište je ve formátu:
```
Teplota: 36.6 °C
```

**Tip:** Použijte `for temp in temperatures:` pro průchod seznamem.

---

### 2.8 Co když udělám chybu? (Chyby a jejich řešení)

Chyby jsou **přirozenou součástí** programování. Nikdo nepíše dokonalý kód napoprvé! Důležité je umět chyby **číst, pochopit a opravit**.

#### Typy chyb

**1. Syntaktická chyba (SyntaxError)**
Porušení pravidel jazyka Python – např. chybějící dvojtečka, špatné odsazení.

```python
# ❌ CHYBA: Chybí dvojtečka za if
if temperature > 38
 print("Horečka")
```

**Chybová hláška:**
```
 File "main.py", line 1
 if temperature > 38
 ^
SyntaxError: expected ':'
```

**Jak opravit:** Přidejte dvojtečku: `if temperature > 38:`

---

**2. Chyba názvu (NameError)**
Použití neexistující proměnné nebo funkce.

```python
# ❌ CHYBA: Proměnná 'age' neexistuje
print(f"Věk: {age}")
```

**Chybová hláška:**
```
NameError: name 'age' is not defined
```

**Jak opravit:** Definujte proměnnou před použitím: `age = 20`

---

**3. Chyba typu (TypeError)**
Nekompatibilní operace mezi datovými typy.

```python
# ❌ CHYBA: Nelze sčítat text a číslo
result = "Věk: " + 25
```

**Chybová hláška:**
```
TypeError: can only concatenate str (not "int") to str
```

**Jak opravit:** Použijte f-string: `result = f"Věk: {25}"`

---

**4. Chyba odsazení (IndentationError)**
Špatné odsazení kódu.

```python
# ❌ CHYBA: Špatné odsazení
if True:
print("Ahoj")
```

**Chybová hláška:**
```
File "<input>", line 2
 print("Ahoj")
 ^
IndentationError: expected an indented block after 'if' statement on line 1
```

**Jak opravit:** Odsaďte řádek `print("Ahoj")` 4 mezerami (nebo Tab).

---

#### Jak číst chybové hlášky (Traceback)

Když Python narazí na chybu, vypíše **Traceback** (zpětné trasování):

```
Traceback (most recent call last):
 File "main.py", line 5, in <module>
 print(f"Výsledek: {result}")
NameError: name 'result' is not defined
```

**Důležité informace:**

1. **Soubor a řádek:** `File "main.py", line 5` → Chyba je na řádku 5
2. **Kód:** `print(f"Výsledek: {result}")` → Toto způsobilo chybu
3. **Typ chyby:** `NameError: name 'result' is not defined` → Proměnná `result` neexistuje

---

#### Tipy pro ladění (debugging)

- **Čtěte chybu pozorně** – Python říká, co je špatně
- **Začněte od spodu** – Poslední řádek Tracebacku obsahuje hlavní info
- **Kontrolujte číslo řádku** – Chyba může být i na jiném řádku, Python jen oznámí, kde skončil
- **Testujte po malých krocích** – Nečekejte se spuštěním, až napíšete 50 řádků
- **Použijte `print()`** – Vypisujte hodnoty proměnných pro kontrolu

**Příklad ladění:**
```python
temperature = 38.5
# Kontrolní výpis (debugging)
print(f"DEBUG: Teplota = {temperature}")

if temperature > 38.0:
 print("Horečka detekována")
```

---

#### ÚKOL: Detektiv chyb

Následující 4 kódy obsahují chyby. Vaším úkolem je:

1. **Zkopírovat každý kód do PyCharmu**
2. **Spustit ho** a přečíst si chybovou hlášku
3. **Opravit chybu** podle toho, co Python vypíše
4. **Spustit znovu** a ověřit, že kód funguje

**Kód 1:**
```python
heart_rate = 72
if heart_rate > 100
 print("Tachykardie!")
```

**Kód 2:**
```python
patient_name = "Jan Novák"
print(f"Pacient: {pacient_name}")
```

**Kód 3:**
```python
temperature = 37.5
if temperature > 38.0:
print("Horečka!")
```

**Kód 4:**
```python
temperatures = [36.6, 37.2, 38.1]
first_temp = temperatures[0]
last_temp = temperatures[3]
print(last_temp)
```

**Tip:** Každá chyba odpovídá jednomu z typů chyb popsaných výše. Přečtěte si chybovou hlášku pozorně – Python vám napoví, co je špatně!

> **Zlaté pravidlo:** Pište kód po malých částech (3-5 řádků) a průběžně testujte. Nenechávejte testování až na konec!

---


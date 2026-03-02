# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## CÍL 2: ZÁKLADY PRÁCE S ŘETĚZCI

### 2.1 Načítání vstupu od uživatele - funkce input()

Než začneme pracovat s řetězci, musíme vědět, jak **získat data od uživatele**. K tomu slouží funkce `input()`.

**Základní syntaxe:**
```python
jmeno = input("Zadej své jméno: ")
print(f"Ahoj, {jmeno}!")
```

**Jak to funguje:**

1. Program se **zastaví** a čeká na vstup uživatele
2. Uživatel napíše text a stiskne **Enter**
3. Text se **uloží do proměnné** (vždy jako `str`!)
4. Program pokračuje dál

**Praktický příklad - sběr dat pacienta:**
```python
print("=== Registrace pacienta ===")
name = input("Jméno: ")
age = input("Věk: ") # ⚠️ Vrací STRING, ne číslo!
allergies = input("Alergie (oddělené čárkou): ")

print(f"\nPacient: {name}")
print(f"Věk: {age} let")
print(f"Alergie: {allergies}")
```

**Výstup:**
```
=== Registrace pacienta ===
Jméno: Jan Novák
Věk: 35
Alergie: penicilín, latex

Pacient: Jan Novák
Věk: 35 let
Alergie: penicilín, latex
```

> **⚠️ KRITICKÉ:** `input()` **VŽDY vrací string**, i když uživatel zadá číslo!
> ```python
> age = input("Věk: ") # Uživatel napíše: 25
> print(type(age)) # <class 'str'>
> # age + 5 # ❌ CHYBA! Nelze sčítat string a int
>
> # Správně - převeď na int:
> age = int(input("Věk: "))
> print(age + 5) # Funguje: 30
> ```

**Prázdný vstup:**
```python
response = input("Chceš pokračovat? (ano/ne): ")
if response == "": # Uživatel jen stiskl Enter
 print("Nezadal jsi nic!")
```

---

#### ÚKOL: Převod měrných jednotek

Vytvoř program, který:

1. Načte od uživatele teplotu ve Fahrenheitech (jako text)
2. Převede ji na číslo (`float`)
3. Vypočítá teplotu ve stupních Celsia podle vzorce: `celsius = (fahrenheit - 32) * 5/9`
4. Vypíše výsledek ve formátu: `"X °F je Y °C"`

**Tip:** Nezapomeň převést vstup z `input()` na `float`!

> **Poznámka:** Pokud uživatel zadá neplatný vstup (např. text místo čísla), program spadne s chybou. Ošetření chyb (`try-except`) se naučíme později!
---

### 2.2 Vytváření řetězců

Řetězce vytvoříme pomocí uvozovek (`"`) nebo apostrofů (`'`). Oba způsoby jsou rovnocenné:

```python
message = "Hello, world!"
another_message = 'Hello, world!'

print(message)
print(another_message)
```

**Kdy použít jaké uvozovky?**
- Pokud text obsahuje apostrof, použij vnější uvozovky: `"Let's go!"`
- Pokud text obsahuje uvozovky, použij vnější apostrofy: `'He said "Hello"'`

**💻 Zkus:**
```python
# Vytvořte řetězec obsahující text: "Let's learn more about Python!"
text = "Let's learn more about Python!"
print(text)

# Co se stane, když použijeme apostrofy?
# text = 'Let's go' # ❌ CHYBA - Python si myslí, že řetězec končí před Let
```

### 2.3 Délka řetězce

Funkce `len()` (length = délka) vrátí počet znaků v řetězci:

```python
text = "How are you?"
length = len(text)
print(f"Text má {length} znaků") # 12
```

**Pozor:** Mezery se počítají! Prázdný řetězec `""` má délku 0.

**💻 Zkus:**
```python
print(len("Python")) # 6
print(len("10")) # 2 (text, ne číslo!)
print(len("3 + 1")) # 5 (včetně mezer)
print(len(" ")) # 1 (mezera je znak)
print(len("")) # 0 (prázdný řetězec)

# Praktický příklad - validace rodného čísla
birth_num = "9501152345"
if len(birth_num) == 10:
 print("Délka rodného čísla je správná")
else:
 print(f"Chyba: očekáváno 10 číslic, máme {len(birth_num)}")
```

---

#### ÚKOL: Kontrola délky hesla

Vytvoř program, který:

1. Načte heslo od uživatele pomocí `input()`
2. Zjistí jeho délku pomocí `len()`
3. Vypíše: `"Tvoje heslo má X znaků"`
4. Pokud je heslo kratší než 8 znaků, vypíše: `"Heslo je příliš krátké!"`

---

### 2.4 Skládání řetězců

Řetězce spojíme operátorem `+`:

```python
greeting = "Dobrý den"
name = "Karle"
message = greeting + ", " + name + "!"
print(message) # Dobrý den, Karle!
```

**Opakování řetězce** (`*`):

```python
print("Ha" * 5) # HaHaHaHaHa
print("-" * 20) # Čára z pomlček
```

**💻 Zkus:**
```python
# Načti jméno uživatele
user_name = input("Zadej své jméno: ")

# Vytvoř uvítací zprávu
message = "Vítej, " + user_name + "! Jsi skvělý programátor!"
print(message)

# Nebo pomocí f-stringu (moderní způsob):
print(f"Vítej, {user_name}! Jsi skvělý programátor!")
```

---

#### ÚKOL: Hlavička zprávy

Vytvoř program, který:

1. Načte název nemocnice a oddělení
2. Vytvoří hlavičku složenou z opakujících se znaků `=` a textu:
 ```
 ==============================
 [Název nemocnice] - [Oddělení]
 ==============================
 ```

**Tip:** Použij `"=" * 30` pro vytvoření čáry a `+` pro spojení textů.

---

### 2.5 F-stringy - moderní formátování textu

**F-stringy** (formatted string literals) jsou **nejlepší způsob**, jak v Pythonu skládat text s proměnnými. Jsou rychlé, čitelné a mocné.

#### Základní syntaxe

```python
name = "Jan"
age = 25

# Starý způsob:
message = "Ahoj, jmenuji se " + name + " a je mi " + str(age) + " let."

# F-string:
message = f"Ahoj, jmenuji se {name} a je mi {age} let."
print(message) # "Ahoj, jmenuji se Jan a je mi 25 let."
```

**Proč f-stringy?**
- **Čitelnost:** Vidíš, co bude ve výstupu
- **Rychlost:** Rychlejší než `.format()` nebo `+`
- **Flexibilita:** Můžeš vkládat výrazy, ne jen proměnné

#### Výrazy uvnitř f-stringů

Do `{}` můžeš dát **jakýkoliv Python výraz**:

```python
a = 10
b = 5

print(f"Součet: {a + b}") # "Součet: 15"
print(f"Rozdíl: {a - b}") # "Rozdíl: 5"
print(f"Je a větší? {a > b}") # "Je a větší? True"
print(f"Délka jména: {len('Python')}") # "Délka jména: 6"
```

**Medicínský příklad:**
```python
bmi_weight = 75 # kg
bmi_height = 1.80 # m

# Výpočet přímo v f-stringu:
print(f"BMI: {bmi_weight / (bmi_height ** 2):.1f}")
# "BMI: 23.1"
```

#### Formátování čísel

Při práci s čísly často potřebujeme kontrolovat, kolik desetinných míst se zobrazí:

```python
pi = 3.141592653589793

print(f"Pi: {pi}") # "Pi: 3.141592653589793"
print(f"Pi: {pi:.2f}") # "Pi: 3.14" (2 desetinná místa)
print(f"Pi: {pi:.4f}") # "Pi: 3.1416" (4 desetinná místa)
```

**Formát `{variable:.Xf}` znamená:**

- `variable` = proměnná, kterou chceš zobrazit
- `:.Xf` = zobraz s X desetinnými místy
 - `.2f` = 2 desetinná místa
 - `.1f` = 1 desetinné místo
 - `.0f` = žádné desetinné místo (zaokrouhlí)

**💻 Zkus - praktický úkol:**
```python
# Vytvoř program pro výpočet BMI s pěkným výstupem
name = input("Jméno: ")
weight = float(input("Váha (kg): "))
height = float(input("Výška (m): "))

bmi = weight / (height ** 2)

print(f"Pacient: {name.title()}")
print(f"Váha: {weight:.1f} kg")
print(f"Výška: {height:.2f} m")
print(f"BMI: {bmi:.2f}")

# Vyhodnocení
if bmi < 18.5:
 category = "podváha"
elif bmi < 25:
 category = "normální váha"
elif bmi < 30:
 category = "nadváha"
else:
 category = "obezita"

print(f"Kategorie: {category}")
```

---

#### ÚKOL: Výpočet krevního tlaku (MAP)

Střední arteriální tlak (MAP) se počítá: `MAP = (systolic + 2 * diastolic) / 3`

Vytvoř program, který:

1. Načte systolický a diastolický tlak od uživatele
2. Vypočítá MAP
3. Vypíše výsledek s 1 desetinným místem: `"MAP: X.X mmHg"`

**Tip:** Použij `{map:.1f}` pro formátování s 1 desetinným místem.

> **Shrnutí f-stringů:**
> - `{variable}` - prostě hodnota
> - `{variable:.2f}` - 2 desetinná místa
> - `{a + b}` - můžeš vkládat výrazy
> - F-stringy jsou **nejčitelnější a nejrychlejší** způsob formátování!

---


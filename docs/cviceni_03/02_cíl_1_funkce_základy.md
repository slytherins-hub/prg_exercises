# CVIČENÍ 3: FUNKCE A SEZMANY

Algoritmizace a programování

## CÍL 1: FUNKCE – ZÁKLADY

### 1.1 Co je to funkce?

**Funkce** je **pojmenovaný blok kódu**, který můžeme volat opakovaně. Je to jako **recept v kuchařce** – jednou napíšeme, vícekrát použijeme.

**Proč používat funkce?**

1. **Znovupoužitelnost** – Kód píšeme jen jednou
2. **Čitelnost** – Pojmenovaná funkce vysvětluje, co dělá
3. **Testovatelnost** – Funkce lze testovat samostatně
4. **Organizace** – Velký program rozdělíme na menší celky

> **Už jsi funkce používal!** Například `print()`, `len()`, `input()`, `range()` – to všechno jsou funkce, které Python poskytuje. Nyní se naučíš vytvářet vlastní!

**Medicínský příklad – výpočet BMI:**

```python
# BEZ funkce - opakování kódu
weight_1 = 75
height_1 = 1.80
bmi_1 = weight_1 / (height_1 ** 2)
print(f"BMI pacienta 1: {bmi_1:.1f}")

weight_2 = 68
height_2 = 1.65
bmi_2 = weight_2 / (height_2 ** 2)
print(f"BMI pacienta 2: {bmi_2:.1f}")

# S FUNKCÍ - elegantní řešení
def calculate_bmi(weight, height):
 """Vypočítá BMI (Body Mass Index)."""
 return weight / (height ** 2)

bmi_1 = calculate_bmi(75, 1.80)
bmi_2 = calculate_bmi(68, 1.65)
print(f"BMI pacienta 1: {bmi_1:.1f}")
print(f"BMI pacienta 2: {bmi_2:.1f}")
```

> **Klíčový princip:** **DRY – Don't Repeat Yourself**. Pokud píšete stejný kód vícekrát, potřebujete funkci!

**Proč je duplikace kódu problém?**

1. **Chyby se násobí** – Máš bug? Musíš ho opravit na 10 místech místo na jednom
2. **Změny jsou náročné** – Chceš změnit výpočet BMI? Hledáš všechny výskyty v kódu
3. **Kód je nečitelný** – 500 řádků místo 50
4. **Těžko se testuje** – Nemůžeš otestovat "funkci", která neexistuje

> **Pravidlo:** Když kopíruješ kód potřetí, zabal ho do funkce!

### 1.2 Anatomie funkce

```python
def function_name(param1, param2):
 """
 Stručný popis toho, co funkce dělá.

 Delší vysvětlení funkce (volitelné). Zde můžeme popsat,
 jak funkce pracuje, případná omezení nebo důležité poznámky.

 Args:
 param1 (typ): Popis prvního parametru.
 param2 (typ): Popis druhého parametru.

 Returns:
 typ: Popis návratové hodnoty.
 """
 # Tělo funkce
 result = param1 + param2
 return result
```

**Části funkce:**

1. `def` – Klíčové slovo pro definici funkce
2. `function_name` – Název funkce (doporučení: malá písmena, podtržítka)
3. `(param1, param2)` – Parametry (vstupy funkce)
4. `:` – Dvojtečka začínající blok funkce
5. `"""Docstring"""` – Dokumentace funkce psaná hned pod hlavičkou.
 * První řádek: stručné shrnutí funkce.
 * Prázdný řádek.
 * Detailnější popis (volitelné).
 * Sekce `Args:` – popis parametrů.
 * Sekce `Returns:` – popis návratové hodnoty.
6. Tělo funkce – Kód, který se vykoná
7. `return` – Návratová hodnota (výstup funkce)

---

### 1.3 První funkce

```python
def greet():
 """Vypíše text 'Ahoj'."""
 print("Ahoj!")

# Volání funkce
greet() # Vypíše: Ahoj!
```

### 1.4 Funkce s parametry

```python
def greet_patient(name):
 """Pozdraví pacienta jménem.

 Args:
 name (str): Jméno pacienta.

 Returns:
 None: Funkce nic nevrací.
 """
 print(f"Dobrý den, pane/paní {name}!")

# Volání
greet_patient("Novák") # Dobrý den, pane/paní Novák!
greet_patient("Svobodová") # Dobrý den, pane/paní Svobodová!
```

### 1.5 Funkce s návratovou hodnotou (`return`)

```python
def calculate_bmi(weight, height):
 """Vypočítá hodnotu BMI (Body Mass Index) z hmotnosti a výšky.

 Args:
 weight (float): Hmotnost v kilogramech.
 height (float): Výška v metrech.

 Returns:
 float: Vypočítaná hodnota BMI.
 """
 bmi = weight / (height ** 2)
 return bmi

# Použití
patient_bmi = calculate_bmi(75, 1.80)
print(f"BMI: {patient_bmi:.1f}") # BMI: 23.1
```

**Klíčový rozdíl:**

* Funkce **bez `return`** nic nevrací (technicky vrací `None`)
* Funkce **s `return`** vrací hodnotu, kterou můžeme uložit nebo použít

```python
# BEZ return - jen vypíše
def print_bmi(weight, height):
 bmi = weight / (height ** 2)
 print(f"BMI: {bmi:.1f}")

print_bmi(75, 1.80) # Vypíše: BMI: 23.1
result = print_bmi(75, 1.80)
print(result) # None (funkce nic nevrací)

# S return - vrací hodnotu
def calculate_bmi(weight, height):
 bmi = weight / (height ** 2)
 return bmi

result = calculate_bmi(75, 1.80)
print(f"BMI: {result:.1f}") # BMI: 23.1
```

---

### 1.6 Funkce s více parametry

```python
def evaluate_pressure(systolic, diastolic):
 """Vyhodnotí krevní tlak na základě systolické a diastolické hodnoty.

 Args:
 systolic (int | float): Systolický krevní tlak v mmHg.
 diastolic (int | float): Diastolický krevní tlak v mmHg.

 Returns:
 str: Textové vyhodnocení krevního tlaku
 ("Normální", "Vyšší normální", "Mírná hypertenze",
 nebo "Vysoká hypertenze").
 """
 if systolic < 120 and diastolic < 80:
 return "Normální"
 elif systolic < 130 and diastolic < 85:
 return "Vyšší normální"
 elif systolic < 140 and diastolic < 90:
 return "Mírná hypertenze"
 else:
 return "Vysoká hypertenze"

# Použití
result = evaluate_pressure(125, 82)
print(f"Tlak 125/82: {result}") # Vyšší normální

result2 = evaluate_pressure(145, 95)
print(f"Tlak 145/95: {result2}") # Vysoká hypertenze
```

---

### 1.7 📚 Doporučený postup pro začátečníky

**Nejdřív vytvoř fungující skript, pak ho zabal do funkce!**

#### Nejprve: Napiš skript s konkrétními hodnotami

```python
# Krok za krokem testuj v interaktivním režimu nebo po částech
weight = 75
height = 1.80

print(f"Váha: {weight} kg") # Zkontroluj, že máš správnou hodnotu
print(f"Výška: {height} m") # Zkontroluj výšku

bmi = weight / (height ** 2)
print(f"BMI: {bmi}") # Vypočítej a zkontroluj BMI

rounded_bmi = round(bmi, 1)
print(f"BMI zaokrouhlené: {rounded_bmi}") # Finální výsledek
```

> **Tip:** Spouštěj kód po každém řádku nebo po malých blocích – hned vidíš, co funguje a co ne!

#### Potom: Když skript funguje, zabal ho do funkce

```python
def calculate_bmi(weight, height):
 """Vypočítá BMI a vrátí jej zaokrouhlené na jedno desetinné místo.

 Args:
 weight (float): Hmotnost v kilogramech.
 height (float): Výška v metrech.

 Returns:
 float: Hodnota BMI zaokrouhlená na jedno desetinné místo.
 """
 # Zkopíruj fungující kód ze skriptu
 bmi = weight / (height ** 2)
 rounded_bmi = round(bmi, 1)
 return rounded_bmi

# Testuj funkci se stejnými hodnotami jako měl skript
result = calculate_bmi(75, 1.80)
print(f"BMI: {result}") # Mělo by dát stejný výsledek jako skript
```

> ⚠️ **Nedělej to naopak!** Začátečníci často píšou funkci hned a pak neví, proč nefunguje. **Nejdřív rozchodíš skript, pak vytvoříš funkci.**

---

#### ÚKOL: První vlastní funkce

Vytvoř program `medical_functions.py` skládající se ze tří části:

**Část 1: Pozdrav pacienta**
* Napiš funkci `greet_patient()`:

 * Funkce přijímá jeden parametr typu `str` představující jméno pacienta.
 * Funkce zobrazí personalizovaný pozdrav pacienta na základě zadaného jména.
 * Funkce nic nevrací (`None`), pouze vypíše pozdrav ve tvaru:
 ```python
 greet_patient("Jan Novák")
 # Dobrý den, pane/paní Jan Novák!
 ```

**Část 2: Validace teploty**
* Napiš funkci `has_fever()`:

 * Funkce přijímá jeden parametr typu `float` představující teplotu těla v °C.
 * Funkce vyhodnotí, zda má pacient horečku na základě zadané tělesné teploty.
 * Funkce vrátí hodnotu typu bool:

 * Vrátí `True`, pokud je teplota vyšší nebo rovna 38.0°C.
 * Vrátí `False`, pokud je teplota nižší než 38.0°C.

**Část 3: Převod teploty**
* Napiš funkci `celsius_to_fahrenheit()`:

 * Funkce přijímá jeden parametr typu `float` představující teplotu ve °C.
 * Funkce převede °C na °F (F = C × 9/5 + 32).
 * Funkce vrací hodnotu typu `float`.
 ```python
 temp_f = celsius_to_fahrenheit(36.5)
 print(f"36.5°C = {temp_f:.1f}°F")
 # 36.5°C = 97.7°F
 ```

---


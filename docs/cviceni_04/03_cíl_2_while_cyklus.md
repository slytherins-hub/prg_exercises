# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE A SLOVNÍKY

Algoritmizace a programování

## CÍL 2: WHILE CYKLUS

### 2.1 Proč potřebujeme while cyklus?

**For cyklus** funguje skvěle, když **známe počet opakování** dopředu:
```python
# Vím, že mám 5 pacientů
patients = ["Jan", "Marie", "Petr", "Anna", "Eva"]
for patient in patients:
    print(patient)

# Vím, že chci opakovat 10×
for i in range(10):
    print(i)
```

Ale co v těchto situacích?

**1. Validace vstupu, dokud není správný**
```python
# Čekáme na správný vstup od uživatele
# Kolikrát se zeptáme? Nevíme - záleží na uživateli!
age = -1 # Neplatná hodnota pro start

while age < 0 or age > 120:
    age_str = input("Zadej věk (0-120): ")
    try:
        age = int(age_str)
    except ValueError:
        print("Zadej prosím celé číslo.")
        continue

print(f"Věk {age} přijat")
```

**2. Průběžné sledování pacienta do návratu do normy**
```python
# Měříme tepovou frekvenci, dokud není v normě
heart_rate = measure_sensor()

while heart_rate > 100 or heart_rate < 60:
    print(f"Abnormální tep: {heart_rate} bpm")
    alert_nurse()
    time.sleep(10)
    heart_rate = measure_sensor()

print("Tep v normě")
```

> **Klíčový rozdíl:**
> 
> - **For** = "Udělej to N-krát" (známý počet)
> - **While** = "Dělej to, DOKUD platí podmínka" (neznámý počet)

---

### 2.2 Co je while a kdy ho použít?

**While cyklus** opakuje blok kódu, **dokud platí podmínka**.

**Srovnání for vs while:**

| Vlastnost           | `for`                         | `while`                          |
|---------------------|-------------------------------|----------------------------------|
| **Počet opakování** | Známe dopředu                 | Neznáme (záleží na podmínce)     |
| **Použití**         | Procházení sekvencí           | Opakování do splnění podmínky    |
| **Příklad**         | "Projdi 10 pacientů"          | "Ptej se, dokud nezadá správně"  |
| **Riziko**          | Bezpečné (skončí automaticky) | Nekonečný cyklus (musíme hlídat) |
| **Syntaxe**         | `for i in range(10):`         | `while i < 10:`                  |

---

### 2.3 Syntax while cyklu

```python
while PODMINKA:
    # Tělo cyklu
    # Kód, který se opakuje
    # Podmínka se kontroluje před každou iterací
```

**Jak while funguje:**

1. **Zkontroluje podmínku** – Je `True` nebo `False`?
2. **Pokud `True`** → Vykoná tělo cyklu
3. **Vrátí se na začátek** → Znovu zkontroluje podmínku
4. **Pokud `False`** → Ukončí cyklus, pokračuje dál

**Jednoduchý příklad – odpočítávání:**

```python
counter = 5

while counter > 0:
    print(f"Odpočet: {counter}")
    counter -= 1 # Důležité! Snížíme counter

print("Start!")
```

**Výstup:**
```
Odpočet: 5
Odpočet: 4
Odpočet: 3
Odpočet: 2
Odpočet: 1
Start!
```

**Krok po kroku:**

- **1. iterace:** `counter = 5`, podmínka `5 > 0` je `True` → vypíše 5, sníží na 4
- **2. iterace:** `counter = 4`, podmínka `4 > 0` je `True` → vypíše 4, sníží na 3
- ...
- **6. iterace:** `counter = 0`, podmínka `0 > 0` je `False` → **KONEC**

> **⚠️ KRITICKÉ:** Pokud zapomeneš změnit `counter` (např. `counter -= 1`), podmínka bude **vždy True** → **nekonečný cyklus**!

---

#### ÚKOL: Simulace uklidnění tepu

Simuluj uklidnění tepu pacienta po zátěži:

1. Začni hodnotou `heart_rate = 120`
2. V každém průchodu cyklem sniž tep o 5
3. Každý mezivýsledek vypiš jako `Tep: X bpm`
4. Jakmile se dostaneš na 60 nebo méně, cyklus ukonči a vypiš potvrzení normalizace

Očekávaný výstup:
```
Tep: 120 bpm
Tep: 115 bpm
Tep: 110 bpm
...
Tep: 60 bpm
Tep normalizován.
```

---

### 2.4 Nekonečné cykly

**Nekonečný cyklus** = cyklus, který **nikdy neskončí**, protože podmínka je **pořád splněná**.

**❌ Příklad špatně – nekonečný cyklus:**
```python
counter = 0

while counter < 5:
    print(counter)
    # CHYBA: Zapomněli jsme zvýšit counter!
    # Podmínka bude pořád True (0 < 5)

# Program se NIKDY nedostane sem!
```

**Jak poznáš nekonečný cyklus?**

- Program "zamrzne" a nic se neděje
- Terminál vypíše nekonečně mnoho řádků
- CPU využití skočí na 100%

**Jak ho zastavit?**

- V PyCharmu: **Červené tlačítko Stop** nebo **Ctrl + C**
- V terminálu: **Ctrl + C**

> **⚠️ Prevence nekonečných cyklů:**
>
> 1. **Vždy měň podmínku** uvnitř cyklu (`counter += 1`, `user_input = ...`)
> 2. **Kontroluj logiku** – může podmínka být někdy `False`?

---

### 2.5 Řízení toku cyklu

#### Break – okamžité ukončení cyklu

**`break`** **ukončí celý cyklus** – program pokračuje za cyklem.

```python
counter = 0

while counter < 10:
    print(counter)

    if counter == 5:
        print("Našli jsme 5, končíme!")
        break # Ukončí cyklus

    counter += 1

print("Konec") # Sem skočí po break
```

**Výstup:**
```
0
1
2
3
4
5
Našli jsme 5, končíme!
Konec
```

**Medicínský příklad – monitoring s alarmem:**

```python
heart_rate = 70

while True: # Nekonečný cyklus - bezpečný díky break!
    print(f"Tep: {heart_rate} bpm")

    if heart_rate > 120:
        print("TACHYKARDIE! Volám lékaře!")
        break # Kritický stav - ukončíme monitoring

    if heart_rate < 40:
        print("BRADYKARDIE! Volám lékaře!")
        break

    # Simulace změny
    heart_rate_str = input("Nový tep: ")
    try:
        heart_rate = int(heart_rate_str)
    except ValueError:
        print("Neplatný vstup, zadej celé číslo.")
        continue

print("Lékař převzal pacienta")
```

#### Continue – přeskočení zbytku iterace

**`continue`** **přeskočí zbytek aktuální iterace** a vrátí se na začátek cyklu (zkontroluje podmínku).

```python
counter = 0

while counter < 5:
    counter += 1 # Důležité dát PŘED continue!

    if counter == 3:
        print("Přeskakuji 3")
        continue # Přeskočí zbytek, vrátí se na while

    print(f"Číslo: {counter}")

print("Konec")
```

**Výstup:**
```
Číslo: 1
Číslo: 2
Přeskakuji 3
Číslo: 4
Číslo: 5
Konec
```

**Medicínský příklad – filtrování chybných měření:**

```python
measurements = 0
valid_count = 0

while measurements < 10:
    temp_str = input(f"Měření {measurements + 1}/10 - Teplota: ")
    measurements += 1 # Počítáme všechna měření

    # Kontrola validity
    try:
        temp = float(temp_str)
    except ValueError:
        print("Neplatné číslo, ignoruji")
        continue # Přeskočíme zbytek, další měření

    if temp < 35 or temp > 42:
        print("Mimo rozsah, ignoruji")
        continue # Další měření

    # Sem se dostaneme jen s platnými daty
    valid_count += 1
    print(f"Platné měření: {temp}°C")

print(f"\nCelkem platných měření: {valid_count}/10")
```

> **`Break` a `continue` fungují i ve for cyklu!**
> Vše, co jsi se naučil o `break` a `continue`, funguje stejně i v `for` cyklu:
>
> ```python
> # Hledání v seznamu – break při nálezu
> patients = ["Jan", "Marie", "Petr", "Anna"]
>
> for patient in patients:
>     if patient == "Petr":
>         print(f"Found {patient}")
>         break # Ukončí cyklus
>     print(f"Checking {patient}...")
> ```
---

#### ÚKOL: Filtrování čísel

Natrénuj `continue` a `break` nad připravenými daty:

```python
numbers = [4, 9, 5, 6, 8, 7, 2, 3]
```

1. Procházej seznam pomocí `while` cyklu (přes index).
2. Pokud je číslo dělitelné 3, přeskoč ho (`continue`).
3. Pokud narazíš na 7, okamžitě ukonči cyklus (`break`).
4. Ostatní čísla vypiš.
5. Na konci vypiš, zda cyklus skončil kvůli sedmičce, nebo došel na konec seznamu.
6. Zkus stejnou úlohu vyřešit ještě jednou tak, že `while` nahradíš `for` cyklem.

**Tip:** Číslo je dělitelné 3, pokud `number % 3 == 0`

---

### 2.6 Validace vstupu pomocí while

Jeden z **nejčastějších použití** `while` je **validace uživatelského vstupu** – opakujeme, dokud uživatel nezadá správná data.

**Problém – bez validace:**
```python
age_str = input("Zadej věk: ")
age = int(age_str) # Co když zadá "abc"? Program spadne.
print(f"Věk: {age}")
```

**Řešení – s validací:**

#### Vzor 1: While True + break

```python
while True:
    age_str = input("Zadej věk (0-120): ")

    # Kontrola 1: Je to celé číslo?
    try:
        age = int(age_str)
    except ValueError:
        print("Zadej prosím celé číslo!")
        continue # Zkus znovu

    # Kontrola 2: Je v rozsahu?
    if age < 0 or age > 120:
        print("Věk musí být mezi 0 a 120!")
        continue # Zkus znovu

    # Všechno OK - ukončíme cyklus
    print(f"Věk {age} přijat")
    break

# Teď můžeme bezpečně používat age
print(f"Za 10 let ti bude {age + 10}")
```

#### Vzor 2: Podmínka s flagovou proměnnou

```python
valid_input = False

while not valid_input:
    age_str = input("Zadej věk (0-120): ")

    try:
        age = int(age_str)
        if 0 <= age <= 120:
            valid_input = True # Změní podmínku na False
            print(f"Věk {age} přijat")
        else:
            print("Věk musí být mezi 0 a 120!")
    except ValueError:
        print("Zadej prosím celé číslo!")

# Teď máme age
print(f"Za 10 let ti bude {age + 10}")
```

> **Který vzor použít?**
> 
> - **While True + break** – jednodušší, přehlednější (doporučeno)
> - **Flagová proměnná** – explicitnější podmínka

---

#### ÚKOL: Validace rodného čísla

Proveď validaci rodného čísla, které ti zadá uživatel:

1. V cyklu `while` načítej rodné číslo od uživatele pomocí funkce `input()` tak dlouho, dokud nezadá validní hodnotu.
2. Umožni uživateli ukončit zadávání slovem `konec`.
3. U každého pokusu ověř:
	- přesně 10 znaků (`len(...) == 10`),
	- pouze číslice (`.isdigit()`),
    - zkontroluj dělitelonost 11-ti.
4. Pokud je vstup nevalidní, vypiš důvod a nech uživatele zkusit další pokus.
5. Jakmile je vstup validní, vypiš: `Rodné číslo bylo přijato.`
6. Pokud uživatel zadá `konec`, vypiš: `Zadávání bylo ukončeno.`
7. Nakonec vypiš celkový počet pokusů.

---


# CVIČENÍ 3: FUNKCE A SEZMANY

Algoritmizace a programování

## CÍL 2: SEZNAMY

### 2.1 Co je to seznam?

**Seznam** (anglicky *list*) je **uspořádaná kolekce prvků**. Může obsahovat různé datové typy: čísla, texty, logické hodnoty, dokonce i další seznamy.

**Klíčové vlastnosti:**

* **Uspořádaný:** Prvky mají definované pořadí (index)
* **Měnitelný** (mutable): Lze přidávat, odebírat a měnit prvky – **na rozdíl od řetězců!**
* **Indexovatelný:** Přístup k prvkům přes index (od 0)
* **Heterogenní:** Může obsahovat různé datové typy

```python
# Prázdný seznam
empty_list = []
also_empty = list()

# Seznam čísel
temperatures = [36.5, 37.0, 38.2, 36.8]

# Seznam textových řetězců
patients = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]

# Seznam různých typů (heterogenní)
patient_data = ["Jan Novák", 45, True, 175.5] # jméno, věk, pojištěn, výška
```

> **Rozdíl mezi seznamy a řetězci:** Řetězce jsou **immutable** (neměnitelné) – nemůžeš změnit jednotlivý znak. Seznamy jsou **mutable** – můžeš měnit prvky, přidávat nové, odebírat staré.

### 2.2 Vytváření seznamů

#### Přímé přiřazení

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
```

#### Prázdný seznam a postupné plnění

```python
measurements = []
measurements.append(36.5)
measurements.append(37.0)
measurements.append(38.2)
print(measurements) # [36.5, 37.0, 38.2]
```

> **In-place modifikace:** `.append()` mění seznam **přímo** (in-place), protože seznamy jsou **mutable**. To je rozdíl oproti řetězcům:
> ```python
> # Seznam - MUTABLE (měnitelný)
> temps = [36.5]
> temps.append(37.0) # Mění přímo seznam temps
> print(temps) # [36.5, 37.0]
>
> # Řetězec - IMMUTABLE (neměnitelný)
> text = "Ahoj"
> text.upper() # VYTVOŘÍ nový řetězec, ale NEZMĚNÍ původní
> print(text) # "Ahoj" (pořád malé!)
>
> # Pro řetězce musíš přiřadit novou hodnotu:
> text = text.upper() # Teď text obsahuje "AHOJ"
>
> # Další metoda na stringu funguje stejně:
> word = "kocka"
> word.replace("k", "p") # vrátí nový string, původní se nezmění
> print(word) # "kocka"
> ```

> ⚠️ **Pozor na „kopii“ seznamu (častý zdroj skrytých chyb):**
> ```python
> a = [1, 2, 3]
> b = a # NENÍ copied, jen druhý název pro stejný seznam
> b.append(4)
> print(a) # [1, 2, 3, 4]
> print(b) # [1, 2, 3, 4]
> ```
> Proč? V Pythonu proměnná drží **odkaz na objekt**. Při `b = a` nevzniká nový seznam.
>
> Pokud chceš skutečně nový (samostatný) seznam:
> ```python
> a = [1, 2, 3]
> b = a.copy() # nebo a[:]
> b.append(4)
> print(a) # [1, 2, 3]
> print(b) # [1, 2, 3, 4]
> ```
> Není nutné to teď umět používat všude, ale je dobré vědět, že tohle chování může dělat těžko odhalitelné chyby.

#### Převod z jiných datových typů

```python
# Z textového řetězce
dna = list("ACGTTAGC")
print(dna) # ['A', 'C', 'G', 'T', 'T', 'A', 'G', 'C']

# Ze stringu pomocí split()
data = "Jan,25,Praha"
parts = data.split(",")
print(parts) # ['Jan', '25', 'Praha']
```

---

### 2.3 Indexování a slicing

Stejně jako u textových řetězců, můžeme přistupovat k jednotlivým prvkům nebo jejich částem:

```python
patients = ["Jan", "Marie", "Petr", "Anna", "Tomáš"]

# Indexování (číslování od 0)
print(patients[0]) # Jan (první prvek)
print(patients[2]) # Petr (třetí prvek)
print(patients[-1]) # Tomáš (poslední prvek)
print(patients[-2]) # Anna (předposlední)

# Slicing (výběr části)
print(patients[1:4]) # ['Marie', 'Petr', 'Anna'] (indexy 1, 2, 3)
print(patients[:3]) # ['Jan', 'Marie', 'Petr'] (od začátku do indexu 3)
print(patients[2:]) # ['Petr', 'Anna', 'Tomáš'] (od indexu 2 do konce)
print(patients[::2]) # ['Jan', 'Petr', 'Tomáš'] (každý druhý)
print(patients[::-1]) # ['Tomáš', 'Anna', 'Petr', 'Marie', 'Jan'] (pozpátku)
```

**Vizualizace indexování:**
```
Index: 0 1 2 3 4
 ┌─────┬────────┬───────┬───────┬────────┐
Pacienti:│ Jan │ Marie │ Petr │ Anna │ Tomáš │
 └─────┴────────┴───────┴───────┴────────┘
Zpětný: -5 -4 -3 -2 -1
```

#### Změna prvku v seznamu vs řetězec (důležité)

```python
patients = ["Jan", "Marie", "Petr"]
patients[1] = "Pavel" # OK: list je mutable
print(patients) # ['Jan', 'Pavel', 'Petr']

word = "Marie"
# word[1] = "a" # TypeError: 'str' object does not support item assignment
word = word.replace("a", "A") # Správně: vytvoříš nový string
print(word) # MArie
```

> ⚠️ **Zapamatuj si:** U seznamu můžeš změnit prvek přes index. U řetězce tohle nejde.

---

### 2.4 Operace se seznamy

#### Spojování seznamů (`+`)

```python
group_a = ["Jan", "Marie"]
group_b = ["Petr", "Anna"]
all_patients = group_a + group_b
print(all_patients) # ['Jan', 'Marie', 'Petr', 'Anna']
```

#### Opakování (`*`)

```python
baseline = [0]
week_data = baseline * 7
print(week_data) # [0, 0, 0, 0, 0, 0, 0]
```

#### Kontrola obsahu (`in`, `not in`)

```python
patients = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]

if "Jan Novák" in patients:
 print("Pacient je v databázi")

if "Anna Černá" not in patients:
 print("Pacient NENÍ v databázi")
```

#### Porovnávání seznamů

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(list1 == list2) # True (stejné prvky ve stejném pořadí)
print(list1 == list3) # False (jiné pořadí)
```

#### Práce s více seznamy současně

**`enumerate()` – Průchod seznamem s indexem:**

```python
patients = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]

# Místo počítání indexu ručně:
for i in range(len(patients)):
 print(f"{i+1}. {patients[i]}")

# Použij enumerate() - elegantnější:
for i, patient in enumerate(patients, start=1): # 1 = začíná od 1
 print(f"{i}. {patient}")

# Výstup:
# 1. Jan Novák
# 2. Marie Svobodová
# 3. Petr Dvořák
```

**`zip()` – Spojování dvou seznamů:**

```python
names = ["Jan", "Marie", "Petr"]
temperatures = [36.5, 37.2, 38.1]

# Projdi obě seznamy paralelně:
for name, temperature in zip(names, temperatures):
 print(f"{name}: {temperature}°C")

# Výstup:
# Jan: 36.5°C
# Marie: 37.2°C
# Petr: 38.1°C
```

> **Tip:** `zip()` funguje i pro 3 a více seznamů - např. `zip(names, temperatures, pressures)`

---

#### ÚKOL: Práce se seznamy

Vytvoř program `blood_pressure.py`, který analyzuje týdenní měření krevního tlaku.

```python
# Seznam měření systolického tlaku za týden
blood_pressure = [120, 125, 118, 130, 135, 128, 122]
```

**Tvé úkoly:**

1. Najdi nejvyšší a nejnižší hodnotu měření (použij `max()` a `min()`)
2. Spočítej, kolik měření bylo nad 130 mmHg (použij `for` cyklus)
3. Vypiš všechny výsledky přehledně (použij f-stringy)
4. Vytvoř seznam dnů `days = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]` a pomocí `zip(days, blood_pressure)` vypiš měření ve formátu `Po: 120 mmHg`

---

### 2.5 Rozdíl mezi funkcemi a metodami

```python
# FUNKCE - volá se samostatně
numbers = [3, 1, 4, 1, 5]
length = len(numbers) # len() je funkce
maximum = max(numbers) # max() je funkce

# METODA - volá se přes tečkovou notaci
numbers.append(9) # append() je metoda objektu numbers
numbers.sort() # sort() je metoda objektu numbers
```

### 2.6 Základní metody pro přidávání prvků

#### `append()` – Přidá jeden prvek na konec

```python
patients = ["Jan", "Marie"]
patients.append("Petr")
print(patients) # ['Jan', 'Marie', 'Petr']
```

#### `extend()` – Přidá více prvků (rozbalí iterovatelný objekt)

```python
patients = ["Jan", "Marie"]
new_patients = ["Petr", "Anna"]
patients.extend(new_patients)
print(patients) # ['Jan', 'Marie', 'Petr', 'Anna']
```

**Pozor na rozdíl mezi append() a extend():**

```python
patients = ["Jan", "Marie"]

# append() - přidá CELÝ seznam jako JEDEN item
patients.append(["Petr", "Anna"])
print(patients) # ['Jan', 'Marie', ['Petr', 'Anna']] ← vnořený seznam!

# extend() - rozbalí seznam a přidá jednotlivé prvky
patients2 = ["Jan", "Marie"]
patients2.extend(["Petr", "Anna"])
print(patients2) # ['Jan', 'Marie', 'Petr', 'Anna']
```

#### `insert()` – Vloží prvek na konkrétní pozici

```python
patients = ["Jan", "Marie", "Petr"]
patients.insert(1, "Anna") # Vlož na index 1
print(patients) # ['Jan', 'Anna', 'Marie', 'Petr']
```

**💻 Příklad: Fronta pacientů v čekárně**

```python
# Prázdná fronta
waiting_room = []

# Příchod pacientů
waiting_room.append("Jan Novák")
waiting_room.append("Marie Svobodová")
waiting_room.append("Petr Dvořák")
print("Fronta:", waiting_room)

# Urgentní případ - přednost
waiting_room.insert(0, "Anna Nová - URGENTNÍ")
print("Po urgenci:", waiting_room)
```

---

### 2.7 Metody pro odebírání prvků

#### `remove()` – Odebere první výskyt zadaného prvku

```python
patients = ["Jan", "Marie", "Petr", "Marie"]
patients.remove("Marie") # Odebere první "Marie"
print(patients) # ['Jan', 'Petr', 'Marie']
```

⚠️ **Pozor:** Pokud prvek neexistuje, nastane chyba `ValueError`!

```python
patients = ["Jan", "Marie"]
# patients.remove("Anna") # ValueError: list.remove(x): x not in list

# Bezpečnější varianta s kontrolou
if "Anna" in patients:
 patients.remove("Anna")
else:
 print("Pacient není v seznamu")
```

#### `pop()` – Odebere a vrátí prvek na indexu (výchozí: poslední)

```python
patients = ["Jan", "Marie", "Petr", "Anna"]

# Bez argumentu - odebere poslední
last = patients.pop()
print(last) # Anna
print(patients) # ['Jan', 'Marie', 'Petr']

# S indexem - odebere item na indexu
first = patients.pop(0)
print(first) # Jan
print(patients) # ['Marie', 'Petr']
```

**💻 Příklad: Správa fronty pacientů**

```python
queue = ["Jan Novák", "Marie Svobodová", "Petr Dvořák", "Anna Černá"]
print("Původní fronta:", queue)

# Zavolání prvního pacienta
current_patient = queue.pop(0)
print(f"\nVoláme pacienta: {current_patient}")
print("Zbývá ve frontě:", queue)

# Pacient Marie Svobodová odchází (zrušila návštěvu)
queue.remove("Marie Svobodová")
print("Po zrušení:", queue)

# Příchod nového pacienta
queue.append("Tomáš Novotný")
print("Po příchodu nového:", queue)
```

---

### 2.8 Další užitečné metody

#### `index()` – Najde index prvního výskytu prvku

```python
patients = ["Jan", "Marie", "Petr", "Anna"]
position = patients.index("Petr")
print(position) # 2
```

#### `count()` – Spočítá výskyty prvku

```python
measurements = [36.5, 37.0, 36.5, 38.0, 36.5]
count_normal = measurements.count(36.5)
print(count_normal) # 3
```

#### `sort()` – Seřadí seznam (in-place, mění původní)

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers) # [1, 2, 5, 8, 9]

# Sestupně
numbers.sort(reverse=True)
print(numbers) # [9, 8, 5, 2, 1]
```

⚠️ **Pozor:** `sort()` nemá návratovou hodnotu (vrací `None`), mění seznam na místě!

```python
numbers = [5, 2, 8]
result = numbers.sort()
print(result) # None ← metoda nevrací hodnotu
print(numbers) # [2, 5, 8] ← seznam je změněný
```

**Alternativa – funkce `sorted()`** (vrací nový seznam):

```python
numbers = [5, 2, 8]
sorted_numbers = sorted(numbers)
print(numbers) # [5, 2, 8] ← původní nezměněn
print(sorted_numbers) # [2, 5, 8] ← nový seřazený
```

> **Kdy použít co?** `list.sort()` - když chceš seřadit původní seznam (úspora paměti). `sorted(list)` - když potřebuješ zachovat i původní seznam.

#### ÚKOL: Práce s metodami seznamů

Vytvoř program `patient_list.py`, který simuluje správu seznamu pacientů v ordinaci.

**Tvé úkoly:**

1. Vytvoř prázdný seznam `patients`.
2. Přidej postupně 5 pacientů pomocí `append()`: Jan Novák, Marie Svobodová, Petr Dvořák, Anna Černá, Tomáš Novotný.
3. Vypiš aktuální stav seznamu.
4. Odeber prvního pacienta (byl ošetřen) pomocí `pop(0)` a vypiš ho.
5. Pacient "Petr Dvořák" zrušil návštěvu - odeber ho pomocí `remove()`.
6. Přidej na začátek urgentního pacienta "Karel Urgentní" pomocí `insert(0, ...)`.
7. Seřaď zbývající pacienty abecedně pomocí `sort()`.
8. Vypiš konečný stav seznamu.

**Očekávaný výstup:**
```
Původní seznam: ['Jan Novák', 'Marie Svobodová', 'Petr Dvořák', 'Anna Černá', 'Tomáš Novotný']
Ošetřen: Jan Novák
Po ošetření: ['Marie Svobodová', 'Petr Dvořák', 'Anna Černá', 'Tomáš Novotný']
Po zrušení: ['Marie Svobodová', 'Anna Černá', 'Tomáš Novotný']
Po urgenci: ['Karel Urgentní', 'Marie Svobodová', 'Anna Černá', 'Tomáš Novotný']
Seřazeno: ['Anna Černá', 'Karel Urgentní', 'Marie Svobodová', 'Tomáš Novotný']
```

---

### 2.9 Co jsou vnořené seznamy?

**Vnořený seznam** je seznam, jehož prvky jsou také seznamy. Používá se např. pro reprezentaci **dvourozměrných dat** (tabulky, matice).

```python
# Tabulka pacientů: [jméno, věk, temperature]
patients_data = [
 ["Jan Novák", 45, 36.5],
 ["Marie Svobodová", 32, 37.2],
 ["Petr Dvořák", 28, 38.1]
]
```

**Proč používat vnořené seznamy?**
* Reprezentace **tabulek** (řádky a sloupce)
* **Matice** v matematice a obrazovém zpracování
* **Vícerozměrná data** (např. týdenní měření více pacientů)

---

### 2.10 Indexování vnořených seznamů

Používáme **vícenásobné indexování**: `list[row][column]`

```python
# Tabulka pacientů
patients = [
 ["Jan Novák", 45, 36.5], # Index 0
 ["Marie Svobodová", 32, 37.2], # Index 1
 ["Petr Dvořák", 28, 38.1] # Index 2
]

# Přístup k celému řádku
print(patients[0]) # ['Jan Novák', 45, 36.5]

# Přístup ke konkrétnímu prvku
print(patients[0][0]) # Jan Novák (první pacient, jméno)
print(patients[0][1]) # 45 (první pacient, věk)
print(patients[0][2]) # 36.5 (první pacient, temperature)

print(patients[1][0]) # Marie Svobodová (druhý pacient, jméno)
print(patients[2][2]) # 38.1 (třetí pacient, temperature)
```

**Vizualizace indexování:**

```
 [0] [1] [2]
 ┌────────────────┬──────┬───────┐
[0] │ "Jan Novák" │ 45 │ 36.5 │
 ├────────────────┼──────┼───────┤
[1] │ "Marie Svobod."│ 32 │ 37.2 │
 ├────────────────┼──────┼───────┤
[2] │ "Petr Dvořák" │ 28 │ 38.1 │
 └────────────────┴──────┴───────┘

Přístup: patients[řádek][sloupec]
Příklad: patients[1][2] = 37.2
```

---

### 2.11 Iterace přes vnořené seznamy

#### Cyklus přes řádky

```python
patients = [
 ["Jan Novák", 45, 36.5],
 ["Marie Svobodová", 32, 37.2],
 ["Petr Dvořák", 28, 38.1]
]

# Zpracování každého pacienta
for patient in patients:
 name = patient[0]
 age = patient[1]
 temperature = patient[2]
 print(f"{name} ({age} let): {temperature}°C")
```

**Výstup:**
```
Jan Novák (45 let): 36.5°C
Marie Svobodová (32 let): 37.2°C
Petr Dvořák (28 let): 38.1°C
```

#### Vnořený cyklus (řádky × sloupce)

```python
# Matice 3×3
matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# Projdi všechny prvky
for row in matrix:
 for item in row:
 print(item, end=" ")
 print() # Nový řádek po každém řádku matrix
```

**Výstup:**
```
1 2 3
4 5 6
7 8 9
```

> **Jak vnořený cyklus funguje (krokování):**
>
> 1. Vnější cyklus vezme první řádek `[1, 2, 3]`
>    - Vnitřní cyklus projde: `item=1` → vypíše "1 ", `item=2` → vypíše "2 ", `item=3` → vypíše "3 "
>    - Po vnitřním cyklu: `print()` → nový řádek
> 2. Vnější cyklus vezme druhý řádek `[4, 5, 6]`
>    - Vnitřní cyklus projde: `item=4` → vypíše "4 ", `item=5` → vypíše "5 ", `item=6` → vypíše "6 "
>    - Po vnitřním cyklu: `print()` → nový řádek
> 3. Vnější cyklus vezme třetí řádek `[7, 8, 9]`
>    - Vnitřní cyklus projde: `item=7` → vypíše "7 ", `item=8` → vypíše "8 ", `item=9` → vypíše "9 "
>    - Po vnitřním cyklu: `print()` → nový řádek
>
> **Tip:** Zkus si tento kód prokrokovat v debuggeru PyCharm – uvidíš, jak se proměnné mění krok po kroku!

---

### 2.12 Vytváření vnořených seznamů

#### Přímé vytvoření

```python
measurements = [
 ["Pondělí", 36.5, 120, 80],
 ["Úterý", 36.7, 125, 82],
 ["Středa", 37.2, 128, 85]
]
```

#### Postupné plnění

```python
# Prázdná tabulka
weekly_data = []

# Přidávání řádků
weekly_data.append(["Pondělí", 36.5])
weekly_data.append(["Úterý", 36.7])
weekly_data.append(["Středa", 37.2])

print(weekly_data)
# [['Pondělí', 36.5], ['Úterý', 36.7], ['Středa', 37.2]]
```

#### Pomocí cyklu

```python
# Vytvoř matici 3×3 plnou nul
matrix = []
for i in range(3):
 row = []
 for j in range(3):
 row.append(0)
 matrix.append(row)

print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Nebo jednodušeji s násobením
matrix = []
for i in range(3):
 matrix.append([0] * 3)
```

> ⚠️ **Krátká poznámka k vnořeným seznamům:**
> `list.copy()` dělá jen **mělkou kopii** (zkopíruje vnější seznam, ne vnitřní seznamy).
> U vnořených struktur pak můžeš nechtěně měnit data i v „kopii“.
> Když potřebuješ opravdu nezávislou kopii celé vnořené struktury, existuje `copy.deepcopy(...)` (z modulu `copy`).
>
> ```python
> import copy
>
> original = [[1, 2], [3, 4]]
> copied = copy.deepcopy(original)
> copied[0][0] = 99
>
> print(original) # [[1, 2], [3, 4]]
> print(copied) # [[99, 2], [3, 4]]
> ```

---

#### ÚKOL: Analýza teplot pacientů

Vytvoř program `temperature_analysis.py`, který zpracuje teplotní záznamy pacientů.

**Vstupní data:**

```python
# Data: [jméno, teplota_den1, teplota_den2, teplota_den3]
temperature_log = [
 ["Jan Novák", 36.5, 36.7, 36.6],
 ["Marie Svobodová", 37.2, 38.1, 38.5],
 ["Petr Dvořák", 36.8, 36.9, 37.0]
]
```

**Tvé úkoly:**

1. Projdi všechny pacienty pomocí `for` cyklu.
2. U každého pacienta spočítej průměrnou teplotu (`sum(...) / len(...)`).
3. U každého pacienta najdi maximální naměřenou teplotu (`max(...)`).
4. Vypiš výstup ve formátu:

 * `Jméno pacienta: ...`
 * `Průměr: ...°C`
 * `Maximum: ...°C`
5. Pokud je maximální teplota vyšší nebo rovna 38.0°C, vypiš navíc varování:

 * `POZOR: Byla zaznamenána horečka!`

---


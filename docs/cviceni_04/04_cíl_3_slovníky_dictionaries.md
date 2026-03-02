# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE, MNOŽINY A SLOVNÍKY

Algoritmizace a programování

## CÍL 4: SLOVNÍKY (DICTIONARIES)

### 4.1 Proč potřebujeme slovníky?

**Seznam** funguje skvěle pro **sekvenci podobných prvků**:
```python
temperatures = [36.5, 37.2, 36.8, 37.0] # Teploty pacientů
print(temperatures[0]) # První měření
```

Ale co když chceme **párovat** informace? Například **ID pacienta → jeho jméno**?

**❌ Problém se seznamy:**
```python
# Musíme hlídat, aby indexy odpovídaly!
patient_ids = ["P001", "P002", "P003"]
patient_names = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]

# Jak najít jméno pro ID "P002"?
# 1. Najdi index ID v prvním seznamu
index = patient_ids.index("P002") # index = 1
# 2. Použij stejný index v druhém seznamu
name = patient_names[index] # "Marie Svobodová"

print(f"Pacient P002: {name}")
```

**Problémy tohoto přístupu:**

- **Složité** – dva kroky místo jednoho
- **Chybové** – když přidáš/smažeš prvek a zapomeneš v druhém seznamu
- **Nečitelné** – není jasné, že seznamy spolu souvisejí
- **Pomalé** – `.index()` musí projít celý seznam (O(n))


**Řešení: Slovník**
```python
# Jeden slovník - přímé párování klíč→hodnota
patients = {
    "P001": "Jan Novák",
    "P002": "Marie Svobodová",
    "P003": "Petr Dvořák"
}

# Přímý přístup pomocí klíče - JEDNODUCHÉ!
name = patients["P002"] # "Marie Svobodová"
print(f"Pacient P002: {name}")
```

**Výhody slovníku:**

- **Jednoduché** – jeden krok místo dvou
- **Bezpečné** – klíč a hodnota jsou propojené
- **Čitelné** – jasné, co je klíč a co hodnota
- **Rychlé** – přístup je v průměru O(1) místo O(n)

**Medicínské příklady využití slovníků:**

| Situace                  | Bez slovníku (složité)               | Se slovníkem (jednoduché)        |
|--------------------------|--------------------------------------|----------------------------------|
| **ICD-10 kódy**          | Dva seznamy: kódy + názvy            | `{"E11": "Diabetes mellitus"}`   |
| **Laboratorní výsledky** | Seznam `[("hemoglobin", 14.5), ...]` | `{"hemoglobin": 14.5, ...}`      |
| **Databáze pacientů**    | ID a jména v oddělených seznamech    | `{"P001": "Jan Novák", ...}`     |
| **DNA kodony**           | Hledání v seznamu dvojic             | `{"AUG": "Methionin", ...}`      |
| **Nastavení přístroje**  | Pozice v seznamu = význam            | `{"mode": "CT", "voltage": 120}` |

> **📘 Co je slovník (dictionary)?**
> **Slovník** je datová struktura, která **páruje klíče s hodnotami**. Místo indexování čísly (0, 1, 2...) indexujeme **smysluplnými klíči** (jméno, kód, ID...).

---

#### Kdy použít co?

| Situace                       | Seznam                      | Slovník                                                                               |
|-------------------------------|-----------------------------|---------------------------------------------------------------------------------------|
| **Sekvence prvků**            | `[1, 2, 3, 4]`              | ❌ Zbytečné                                                                            |
| **Pořadí záleží**             | `["pondělí", "úterý", ...]` | ⚠️ Slovník (Python 3.7+) zachovává pořadí vložení, ale nepřistupuje se k němu indexem |
| **Párování klíč→hodnota**     | ❌ Dva seznamy komplikované  | `{"a": 1, "b": 2}`                                                                    |
| **Vyhledávání podle indexu**  | `list[5]` rychlé            | ❌ Nemá indexy                                                                         |
| **Vyhledávání podle hodnoty** | ❌ `value in list` O(n)      | `dict[key]` v průměru O(1)                                                            |
| **Unikátní klíče**            | ❌ Může mít duplicity        | Klíče automaticky unikátní                                                            |
| **Čitelnost kódu**            | ❌ Co znamená `data[2]`?     | `data["age"]` je jasné                                                                |

> ** Klíčový princip:**
> Pokud potřebuješ **najít hodnotu podle něčeho jiného než pozice** (číslo, jméno, kód...), použij **slovník**!

> **⚠️ Pozor – klíče musí být unikátní:**
> Ve slovníku **nemůžeš mít stejný klíč dvakrát**. Pokud přidáš stejný klíč, druhá hodnota **přepíše** první.

---

### 4.2 Vytváření slovníků

Slovník vytvoříme pomocí **složených závorek `{}`** a párů **klíč: hodnota** oddělených čárkou.

```python
# Prázdný slovník
patient = {}

# Přidávání hodnot do prázdného slovníku
patient["name"] = "Jan Novák"
patient["age"] = 45
patient["diagnosis"] = "Diabetes"

print(patient)
# {'name': 'Jan Novák', 'age': 45, 'diagnosis': 'Diabetes'}

# Nebo rovnou s hodnotami
lab_results = {
    "hemoglobin": 14.5,
    "leukocytes": 8.2,
    "thrombocytes": 250
}
```

> **Poznámka:**
> - **Klíč** – nejčastěji řetězec (`str`), ale může být i číslo (`int`)
> - **Hodnota** – může být **cokoliv** (`str`, `int`, `float`, `list`...)

### 4.3 Přístup k hodnotám

K hodnotám přistupujeme pomocí **klíče v hranatých závorkách** `slovnik[klic]`.

**Základní přístup:**

```python
patient = {
    "name": "Jan Novák",
    "age": 45,
    "diagnosis": "Diabetes"
}

# Přístup k hodnotě pomocí klíče
name = patient["name"] # "Jan Novák"
age = patient["age"] # 45

print(f"Pacient {name}, věk {age} let")
# Výstup: Pacient Jan Novák, věk 45 let
```

**Změna hodnoty:**

```python
# Změna existující hodnoty
patient["age"] = 46 # Narozeniny!
print(patient["age"]) # 46

# Přidání nové hodnoty
patient["blood_group"] = "AB+"
print(patient)
# {'name': 'Jan Novák', 'age': 46, 'diagnosis': 'Diabetes', 'blood_group': 'AB+'}
```

#### ⚠️ Co když klíč neexistuje?

Pokud se pokusíš přistoupit ke klíči, který ve slovníku **není**, dostaneš **chybu `KeyError`**:

```python
patient = {"name": "Jan Novák", "age": 45}

print(patient["allergies"]) # KeyError: 'allergies'
```

**Řešení 1: Zkontroluj, zda klíč existuje (`in`)**

```python
if "allergies" in patient:
    print(f"Alergie: {patient['allergies']}")
else:
    print("Alergie nezadány")
```

**Řešení 2: Použij podmínku s výchozí hodnotou**

```python
if "allergies" in patient:
    allergies = patient["allergies"]
else:
    allergies = "Žádné"
print(f"Alergie: {allergies}")

if "blood_group" in patient:
    blood_group = patient["blood_group"]
else:
    blood_group = "Neznámá"
print(f"Krevní skupina: {blood_group}")
```

> ** Kdy použít co?**
> - **`slovnik[klic]`** – Když **víš jistě**, že klíč existuje (jinak chyba)
> - **`in slovnik`** – Když chceš **zkontrolovat existenci** před přístupem

**Medicínský příklad – bezpečný přístup k datům:**

```python
lab_results = {
    "hemoglobin": 14.5,
    "leukocytes": 8.2,
    "thrombocytes": 250
}

# Nebezpečné - chyba, pokud klíč neexistuje
# crp = lab_results["CRP"] # KeyError!

# Bezpečné s kontrolou klíče
if "CRP" in lab_results:
    crp = lab_results["CRP"]
else:
    crp = "Nevyšetřeno"
print(f"CRP: {crp}") # "CRP: Nevyšetřeno"

# Kontrola všech běžných hodnot
values_to_check = ["hemoglobin", "leukocytes", "CRP", "glucose"]

for value_name in values_to_check:
    if value_name in lab_results:
        result = lab_results[value_name]
    else:
        result = "Nevyšetřeno"
    print(f"{value_name}: {result}")
```

**Výstup:**
```
hemoglobin: 14.5
leukocytes: 8.2
CRP: Nevyšetřeno
glucose: Nevyšetřeno
```

#### ÚKOL (rychlé procvičení):

Vytvoř slovník `book` s klíči:

- `"title"` a hodnotou `"1984"`,
- `"author"` a hodnotou `"George Orwell"`,
- `"year"` a hodnotou `1949`.

Pak:

1. Vypiš název knihy.
2. Změň rok na `1950`.
3. Přidej nový klíč `"available"` s hodnotou `True`.

---

### 4.4 Iterace přes slovníky

Slovníky můžeme procházet pomocí **for cyklu** několika způsoby.

> **⚠️ Poznámka o pořadí:**
> I když Python 3.7+ zachovává pořadí vkládání, **slovníky nejsou určené pro pořadí**. Používej je pro **vyhledávání podle klíče**, ne pro pořadí prvků!

#### Iterace přes klíče

```python
patient = {"name": "Jan", "age": 45, "diagnosis": "Diabetes"}

# Varianta 1: Přes klíče (výchozí chování)
for key in patient:
    print(key)

# Varianta 2: Explicitně pomocí .keys()
for key in patient.keys():
    print(key)
```

**Výstup:**
```
name
age
diagnosis
```

#### Iterace přes hodnoty

```python
for value in patient.values():
    print(value)
```

**Výstup:**
```
Jan
45
Diabetes
```

#### Iterace přes páry klíč-hodnota

```python
for key, value in patient.items():
    print(f"{key}: {value}")
```

**Výstup:**
```
name: Jan
age: 45
diagnosis: Diabetes
```

> ** Doporučení:** Téměř vždy použij `.items()` – získáš klíč i hodnotu najednou!

**Medicínský příklad – zpracování laboratorních výsledků:**

```python
lab_results = {
    "hemoglobin": 14.5,
    "leukocytes": 8.2,
    "thrombocytes": 250,
    "CRP": 12.5
}

# Referenční rozsahy
reference = {
    "hemoglobin": (13.0, 17.0),
    "leukocytes": (4.0, 10.0),
    "thrombocytes": (150, 400),
    "CRP": (0, 5)
}

print("=== LABORATORNÍ VÝSLEDKY ===")
for parameter, value in lab_results.items():
    min_norm, max_norm = reference[parameter]

    if min_norm <= value <= max_norm:
        status = "V normě"
    else:
        status = "Mimo normu!"

    print(f"{parameter}: {value} ({min_norm}-{max_norm}) {status}")
```

**Výstup:**
```
=== LABORATORNÍ VÝSLEDKY ===
hemoglobin: 14.5 (13.0-17.0) V normě
leukocytes: 8.2 (4.0-10.0) V normě
thrombocytes: 250 (150-400) V normě
CRP: 12.5 (0-5) Mimo normu!
```

#### ÚKOL:

Máš slovník:
```python
prodeje = {"leden": 120, "unor": 95, "brezen": 140}
```

1. Pomocí `.items()` vypiš všechny měsíce ve formátu: `leden: 120 ks`.
2. Spočítej celkový součet prodejů.
3. Vypiš měsíc s nejvyšším prodejem.

---

### 4.5 Metody slovníků

Užitečné metody pro práci se slovníky:

#### `.keys()`, `.values()`, `.items()` – Získání klíčů, hodnot a párů

```python
patient = {"name": "Jan", "age": 45, "diagnosis": "Diabetes"}

# Převod na seznam
keys_list = list(patient.keys()) # ['name', 'age', 'diagnosis']
values_list = list(patient.values()) # ['Jan', 45, 'Diabetes']
pairs_list = list(patient.items()) # [('name', 'Jan'), ('age', 45), ...]
```

> **Poznámka:** Použití v cyklech viz sekce 3.5 – Iterace přes slovníky.

#### `.pop(key)` – Odstranění a vrácení hodnoty

```python
patient = {"name": "Jan", "age": 45, "diagnosis": "Diabetes"}

# Odstraní klíč a vrátí jeho hodnotu
diagnosis = patient.pop("diagnosis")
print(diagnosis) # "Diabetes"
print(patient) # {'name': 'Jan', 'age': 45}

# S defaultní hodnotou (pokud klíč neexistuje)
allergies = patient.pop("allergies", "Žádné")
print(allergies) # "Žádné"
```

#### `del` – Odstranění klíče

```python
patient = {"name": "Jan", "age": 45, "diagnosis": "Diabetes"}

del patient["diagnosis"] # Odstraní klíč
print(patient) # {'name': 'Jan', 'age': 45}
```

> ** `.pop()` vs `del`:**
> - **`.pop()`** – odstraní a **vrátí hodnotu**, má defaultní hodnotu
> - **`del`** – jen odstraní, **nevrací nic**

#### `.update()` – Sloučení slovníků

```python
patient = {"name": "Jan", "age": 45}
additional_data = {"diagnosis": "Diabetes", "blood_group": "AB+"}

patient.update(additional_data)
print(patient)
# {'name': 'Jan', 'age': 45, 'diagnosis': 'Diabetes', 'blood_group': 'AB+'}

# Pokud klíč už existuje, přepíše se
patient.update({"age": 46})
print(patient["age"]) # 46
```

---


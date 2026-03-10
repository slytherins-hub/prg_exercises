# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## CÍL 2: LIST COMPREHENSION

**Proč je list comprehension důležitý?**

- Je stručný, ale pořád čitelný.
- Snižuje množství opakovaného kódu (`for` + `append`).
- U jednoduchých transformací a filtrací bývá často i rychlejší.

> **Tip:** Nejde o co nejkratší zápis. Jde o přehledný kód, který se dobře upravuje.

---

### 2.1 Základní tvar

Klasický cyklus:

```python
heart_rates = [58, 64, 72, 102]
rates_plus_one = []

for rate in heart_rates:
    rates_plus_one.append(rate + 1)

print(rates_plus_one)
```

!!! output "Výstup programu"
    ```text
    [59, 65, 73, 103]
    ```

List comprehension:

```python
heart_rates = [58, 64, 72, 102]
rates_plus_one = [rate + 1 for rate in heart_rates]
print(rates_plus_one)
```

!!! output "Výstup programu"
    ```text
    [59, 65, 73, 103]
    ```

Obecná šablona:

```python
[VYRAZ for PRVEK in SEZNAM]
```

---

### 2.2 Filtrování podmínkou

Klasický cyklus:

```python
heart_rates = [58, 64, 72, 102, 98, 110, 76, 59]
warning_rates = []

for rate in heart_rates:
    if rate < 60 or rate > 100:
        warning_rates.append(rate)

print(warning_rates)
```

!!! output "Výstup programu"
    ```text
    [58, 102, 110, 59]
    ```

List comprehension s podmínkou:

```python
warning_rates = [rate for rate in heart_rates if rate < 60 or rate > 100]
print(warning_rates)
```

!!! output "Výstup programu"
    ```text
    [58, 102, 110, 59]
    ```

Šablona:

```python
[VYRAZ for PRVEK in SEZNAM if PODMINKA]
```

---

### 2.3 Volání funkce v list comprehension

List comprehension může v části `VYRAZ` volat funkci.

Šablona:

```python
[funkce(prvek) for prvek in seznam]
```

Příklad:

```python
temperatures_c = [36.5, 37.0, 38.2]

def celsius_to_fahrenheit(value):
    return round(value * 9 / 5 + 32, 1)

temperatures_f = [celsius_to_fahrenheit(value) for value in temperatures_c]
print(temperatures_f)
```

!!! output "Výstup programu"
    ```text
    [97.7, 98.6, 100.8]
    ```

---

### 2.4 Příklady

Ukázka 1: formátování řádků reportu

```python
patient_ids = ["P001", "P002", "P003"]
bmi_values = [22.7, 25.6, 31.1]

def format_bmi_line(patient_id, bmi):
    return f"{patient_id}: BMI {bmi:.1f}"

report_lines = [format_bmi_line(patient_id, bmi) for patient_id, bmi in zip(patient_ids, bmi_values)]
print(report_lines)
```

!!! output "Výstup programu"
    ```text
    ['P001: BMI 22.7', 'P002: BMI 25.6', 'P003: BMI 31.1']
    ```

Ukázka 2: převod hodnot z textu na čísla

```python
raw_values = ["58", "64", "72", "102"]
heart_rates = [int(value) for value in raw_values]
print(heart_rates)
```

!!! output "Výstup programu"
    ```text
    [58, 64, 72, 102]
    ```

---

### 2.5 Kdy použít list comprehension

Použij, když:

- vytváříš nový seznam,
- podmínka/transformace je přímočará,
- výsledek je čitelný na první pohled.

Nepoužívej, když:

- výraz uvnitř závorek je příliš dlouhý,
- potřebuješ složité větvení,
- potřebuješ mezikroky a ladění po částech.

---

#### ÚKOL: Kontrola objednávek

Máš data:

```python
records = [
    ("ORD-001", 2, 499),
    ("ORD-002", 8, 149),
    ("ORD-003", 1, 1299),
    ("ORD-004", 5, 89),
    ("ORD-005", 10, 59),
]
```

1. Pomocí list comprehension vytvoř seznam „větších objednávek", které splňují jednu z těchto podmínek:

    - cena za kus je větší nebo rovna 1000 Kč, nebo
    - počet kusů je větší nebo roven 5.

2. Pomocí list comprehension vytvoř seznam řádků reportu pro větší objednávky ve formátu:

    `"ORD-001: celkem 998 Kč"`

> **Tip:** Rozděl řešení do více krátkých comprehension místo jedné dlouhé.

---

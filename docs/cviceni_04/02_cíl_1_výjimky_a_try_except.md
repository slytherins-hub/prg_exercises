# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE, MNOŽINY A SLOVNÍKY

Algoritmizace a programování

## CÍL 1: VÝJIMKY A TRY/EXCEPT

`try/except` použij, když kód může skončit chybou (např. převod vstupu na číslo).

Když Python narazí v bloku `try` na chybu, která by jinak program ukončila, **skočí do odpovídající větve `except`**.
Díky tomu program nespadne na tracebacku a můžeš uživateli vypsat srozumitelnou zprávu nebo nechat běh pokračovat dál.

Bez `try/except`: chyba → program se zastaví.
S `try/except`: chyba → přesun do `except` → program pokračuje.

> **📘 Co je výjimka (exception)?**
> 
> Výjimka je chyba za běhu programu.
> 
> Příklad: `int("abc")` vyhodí `ValueError`.

**Nejčastější typy výjimek:**

* `ValueError` – hodnota má špatný formát (`int("abc")`)
* `TypeError` – nekompatibilní datové typy (`"5" + 3`)
* `KeyError` – neexistující klíč ve slovníku (`data["chybny_klic"]`)

### 1.1 Základní syntaxe

```python
try:
    # Kód, který může spadnout na chybě
    ...
except ValueError:
    # Co udělat, když nastane konkrétní chyba
    ...
```

### 1.2 Více `except` větví

Do jednoho `try` můžeš dát více `except` bloků pro různé chyby:

```python
try:
    value = int(input("Zadej číslo: "))
    result = 100 / value
except ValueError:
    print("Nezadal jsi celé číslo.")
except ZeroDivisionError:
    print("Nelze dělit nulou.")
```

Python bere `except` shora dolů a použije **první odpovídající** větev.

### 1.3 Jak zachytit chybovou hlášku

Pokud chceš vidět konkrétní text chyby, použij `as e`:

```python
try:
    age = int(input("Zadej věk: "))
except ValueError as e:
    print(f"Neplatný vstup: {e}")
```

To je užitečné hlavně při debugování.

### 1.4 Jak to funguje krok za krokem

Medicínský příklad – výpočet dávky léku na základě váhy pacienta:

```python
weight_text = input("Zadej váhu pacienta (kg): ")
dose_per_kg = 5  # mg/kg

try:
    weight = float(weight_text)
    dose = weight * dose_per_kg
    print(f"Dávka léku: {dose} mg")
except ValueError:
    print("Chyba: Zadej prosím platné číslo.")
```

1. Kód uvnitř `try` se spustí (načtení váhy a výpočet dávky).
2. Pokud je váha neplatná (např. "abc"), vyhodí se `ValueError`.
3. Program skočí do `except ValueError` a vypíše chybovou zprávu.
4. Program pokračuje dál (nezastaví se).

**⚠️ Čeho se vyvarovat!**

* Nepoužívej holé `except:` bez typu chyby! (schová i chyby, které nechceš ignorovat)
* Nedávej do `try` zbytečně moc kódu! (hůř zjistíš, kde přesně chyba vznikla)
* Nedělej `except ...: pass` bez zprávy! (chyba se ztratí a debug je těžký)

**❌ Prakticky špatně:**

```python
weight_text = input("Zadej váhu pacienta (kg): ")
dose_per_kg = 5

try:
    weight = float(weight_text)
    dose = weight * dose_per_kg
    print(f"Dávka: {dose} mg")
except:
    pass
```

**Proč je to špatně?**

* Nevíš, jaká chyba nastala.
* Program chybu potichu ignoruje.
* Těžko se hledá problém.

**✅ Prakticky správně:**

```python
weight_text = input("Zadej váhu pacienta (kg): ")
dose_per_kg = 5

try:
    weight = float(weight_text)
    dose = weight * dose_per_kg
    print(f"Dávka: {dose} mg")
except ValueError:
    print("Chyba: Zadej prosím platné číslo.")
```

**Jak s tím pracovat správně:**

* Chytej jen konkrétní chyby (např. `except ValueError:`), ne všechno.
* Uvnitř `except` dej uživateli jasnou zprávu, co opravit.
* Nepoužívej `try/except` na maskování logických chyb v programu.

#### ÚKOL: Ošetření chyb při násobení

Doplň ošetření chyb pro tento kód:
```python
number_text = "12x"
number = int(number_text)
print(number * 2)
```

1. Použij `try/except ValueError`.
2. Při chybě vypiš: `Neplatné číslo`.
3. Pokud je vstup validní, vypiš dvojnásobek čísla.

---


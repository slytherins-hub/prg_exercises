# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## CÍL 3: POKROČILÉ PODMÍNKY

### 3.1 Spojování podmínek (Logické operátory)

V předchozím cíli jsme se naučili porovnávat hodnoty (`>`, `<`, `==`, ...). Nyní si ukážeme, jak spojíme více podmínek dohromady.

| Operátor | Význam | Příklad | Výsledek |
|----------|----------------------------|---------------------|----------|
| `and` | A zároveň (platí obojí) | `5 > 0 and 1 < 10` | `True` |
| `or` | Nebo (platí alespoň jedno) | `1 == 1 or 10 == 2` | `True` |
| `not` | Negace (opak) | `not (10 > 5)` | `False` |

```python
# Vyzkoušejte logické operátory
print(True and False) # False (musí platit OBĚ)
print(True or False) # True (stačí JEDNO)
print(not True) # False (opak)
```

**Rozšíření předchozího příkladu s horečkou:**

V sekci 2.6 jsme kontrolovali pouze horečku. Nyní si ukážeme, jak zkontrolovat, zda je teplota v normálním rozmezí (36-37 °C) pomocí `and`.

```python
temperature = 36.8

# Kontrola normální teploty (36-37 °C) - musí platit OBĚ podmínky
if temperature >= 36.0 and temperature <= 37.0:
 print("Normální teplota")
else:
 print("Teplota mimo normu")
```

---

#### ÚKOL: Varovný systém vitálních funkcí

Napište program, který zkontroluje, zda je potřeba zavolat lékaře.

Vytvořte proměnné:

- `temperature = 39.2` (teplota v °C)
- `heart_rate = 105` (srdeční frekvence)

Lékaře zavolejte, pokud **ALESPOŇ JEDNA** z následujících podmínek platí:

- Teplota je >= 39.0 °C (vysoká horečka)
- Srdeční frekvence je > 110 tepů/min

Program má vypsat:

- `"VAROVÁNÍ: Zavolejte lékaře!"` pokud platí alespoň jedna podmínka
- `"Vitální funkce v pořádku"` pokud jsou obě hodnoty v normě

**Tip:** Použijte operátor `or` pro spojení podmínek.

---


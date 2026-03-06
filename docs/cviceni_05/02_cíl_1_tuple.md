# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## CÍL 1: TUPLE (N-TICE)


`tuple` ber jako **seznam v kulaté závorce**, který **nejde měnit**.

```python
record = ("P001", 58, 96)
print(record)
print(record[0])
```

!!! output "Výstup programu"
    ```text
    ('P001', 58, 96)
    P001
    ```

Když tuple zkusíš změnit, dostaneš chybu:

```python
record[1] = 60  # TypeError
```

> **Tip:** Tuple používej, když máš pevnou sadu hodnot, která se během programu nemá měnit.


### 1.1 Proč tuple?

- **Bezpečnější data:** Když se hodnota nemá měnit (např. pevný záznam pacienta), tuple ji chrání před náhodnou úpravou.
- **Jasný záměr:** Když vidíš tuple, víš, že jde o „hotová data“, ne o seznam, který budeš dál měnit.
- **Mírně úspornější/rychlejší:** Tuple bývá v Pythonu obvykle o něco úspornější na paměť a někdy i rychlejší než list, ale hlavní důvod použití je neměnitelnost.

> **Poznámka:** Neber tuple jako „zázračné zrychlení“. Největší přínos je bezpečnost a čitelnost kódu.

---

### 1.2 Rozbalování tuple (unpacking)

Stejným způsobem můžeš rozbalit i seznam se stejným počtem prvků.

```python
patient_id, heart_rate, spo2 = ("P001", 58, 96)
print(patient_id)
print(heart_rate)
print(spo2)
```

!!! output "Výstup programu"
    ```text
    P001
    58
    96
    ```

---

### 1.3 `zip(...)` a `enumerate(...)`

`zip(...)` spojí prvky a vrací dvojice jako tuple:

```python
ids = ["P001", "P002", "P003"]
bmi = [22.7, 25.6, 31.1]

pairs = list(zip(ids, bmi))
print(pairs)
print(pairs[0])
```

!!! output "Výstup programu"
    ```text
    [('P001', 22.7), ('P002', 25.6), ('P003', 31.1)]
    ('P001', 22.7)
    ```

`enumerate(...)` vrací také tuple: `(index, hodnota)`. 

> **Poznámka:** Cyklus for umí *n*-tice také rozbalit. Toho lze využít u funkcí `enumerate()` a `zip()`, které právě *n*-tici (dvojici hodnot) vrací.

```python
rates = [58, 64, 72]

for idx, value in enumerate(rates):
    print(idx, value)
```

!!! output "Výstup programu"
    ```text
    0 58
    1 64
    2 72
    ```


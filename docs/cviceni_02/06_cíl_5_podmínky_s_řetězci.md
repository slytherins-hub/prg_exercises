# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## CÍL 5: PODMÍNKY S ŘETĚZCI

### 5.1 Vnořené podmínky (if-elif-else)

Když máme více než 2 možnosti, použijeme `elif` (zkratka "else if"):

```python
password = input("Zadej heslo: ")

if len(password) < 6:
 result = "Příliš krátké (minimálně 6 znaků)"
elif len(password) < 10:
 result = "Střední síla"
elif len(password) < 15:
 result = "Silné heslo"
else:
 result = "Velmi silné heslo"

print(f"Hodnocení: {result}")
```

**Jak if-elif-else funguje:**

1. Python testuje podmínky **shora dolů**
2. Když najde **první pravdivou**, provede její blok a **skončí**
3. Pokud **žádná není pravdivá**, provede `else`

**Vývojový diagram:**

```mermaid
flowchart TD
 Start([START]) --> Input[Načti heslo]
 Input --> Check1{len < 6?}
 Check1 -->|ANO| Result1[Příliš krátké]
 Check1 -->|NE| Check2{len < 10?}
 Check2 -->|ANO| Result2[Střední síla]
 Check2 -->|NE| Check3{len < 15?}
 Check3 -->|ANO| Result3[Silné heslo]
 Check3 -->|NE| Result4[Velmi silné]
 Result1 --> Output[Vypiš výsledek]
 Result2 --> Output
 Result3 --> Output
 Result4 --> Output
 Output --> End([KONEC])

 style Start fill:#a5d6a7,stroke:#2e7d32,stroke-width:2px,color:#000
 style Input fill:#ce93d8,stroke:#6a1b9a,stroke-width:2px,color:#000
 style Check1 fill:#ffcc80,stroke:#e65100,stroke-width:2px,color:#000
 style Check2 fill:#ffcc80,stroke:#e65100,stroke-width:2px,color:#000
 style Check3 fill:#ffcc80,stroke:#e65100,stroke-width:2px,color:#000
 style Result1 fill:#90caf9,stroke:#1565c0,stroke-width:2px,color:#000
 style Result2 fill:#90caf9,stroke:#1565c0,stroke-width:2px,color:#000
 style Result3 fill:#90caf9,stroke:#1565c0,stroke-width:2px,color:#000
 style Result4 fill:#90caf9,stroke:#1565c0,stroke-width:2px,color:#000
 style Output fill:#ce93d8,stroke:#6a1b9a,stroke-width:2px,color:#000
 style End fill:#a5d6a7,stroke:#2e7d32,stroke-width:2px,color:#000
```

**Medicínský příklad - klasifikace BMI:**
```python
bmi = float(input("Zadej BMI: "))

if bmi < 18.5:
 category = "podváha"
 warning = "Doporučujeme zvýšit příjem kalorií"
elif bmi < 25:
 category = "normální váha"
 warning = "Vše v pořádku"
elif bmi < 30:
 category = "nadváha"
 warning = "Doporučujeme zvýšit pohybovou aktivitu"
else:
 category = "obezita"
 warning = "Konzultujte s lékařem"

print(f"Kategorie: {category}")
print(f"Doporučení: {warning}")
```

> **Pozor na pořadí!** Podmínky se testují shora dolů. Pokud dáš `elif bmi < 30` před `elif bmi < 25`, výsledek bude špatně!

---


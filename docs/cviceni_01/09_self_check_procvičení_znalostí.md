# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

### Část A: Teoretické otázky (vyberte správnou odpověď)

**1. Co udělá příkaz `uv init`?**

- a) Spustí Python program
- b) Vytvoří nový projekt se základní strukturou
- c) Nainstaluje Python
- d) Otevře PyCharm

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Vytvoří nový projekt se základní strukturou (včetně pyproject.toml a main.py)
</details>

**2. Jak napíšete znak `#` na české klávesnici?**

- a) `Shift + 3`
- b) `pravý Alt + X`
- c) `Ctrl + 3`
- d) `Alt + X`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `pravý Alt + X` (na anglické klávesnici je to `Shift + 3`)
</details>

**3. Jak se správně pojmenovává proměnná v Pythonu?**

- a) `MonthlyIncome`
- b) `monthly-income`
- c) `monthly_income`
- d) `MONTHLY_INCOME`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `monthly_income` (snake_case - pro běžné proměnné)
</details>

**4. Co se stane, když omylem stisknete klávesu Insert?**

- a) Smaže celý kód
- b) Přepne na přepisovací režim (širší kurzor)
- c) Uloží soubor
- d) Nic

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Přepne na přepisovací režim - poznáte podle širšího kurzoru místo tenké čárky
</details>

**5. Co vypíše tento kód?**
```python
temperatures = [36.6, 37.2, 38.1]
print(temperatures[0])
```

- a) `36.6`
- b) `37.2`
- c) `[36.6, 37.2, 38.1]`
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `36.6` (první prvek seznamu, indexujeme od 0)
</details>

**4. Co vrátí `5 % 2`?**

- a) 2.5
- b) 2
- c) 1
- d) 0

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) 1 (zbytek po dělení 5 ÷ 2)
</details>

**5. Co vrátí `len([10, 20, 30, 40])`?**

- a) 10
- b) 40
- c) 3
- d) 4

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) 4 (počet prvků v seznamu)
</details>

**6. Jaký je rozdíl mezi `and` a `or`?**

- a) `and` vyžaduje obě podmínky, `or` alespoň jednu
- b) `and` je rychlejší než `or`
- c) Žádný rozdíl
- d) `or` vyžaduje obě podmínky

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `and` vyžaduje, aby platily OBĚ podmínky, `or` stačí, když platí alespoň jedna
</details>

**7. Co vypíše `print(f"Teplota: {38.5} °C")`?**

- a) `f"Teplota: {38.5} °C"`
- b) `Teplota: {38.5} °C`
- c) `Teplota: 38.5 °C`
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `Teplota: 38.5 °C` (f-string automaticky dosadí hodnotu ze závorek)
</details>

**8. Jak pojmenujeme konstantu (hodnotu, která se nemění)?**

- a) `maxSpeed`
- b) `max_speed`
- c) `MAX_SPEED`
- d) `Max_Speed`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `MAX_SPEED` (konstanty píšeme velkými písmeny)
</details>

**9. Co vrátí `2 ** 3`?**

- a) 5
- b) 6
- c) 8
- d) 9

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) 8 (mocnění: 2³ = 2 × 2 × 2 = 8)
</details>

**10. Co vrátí `10 // 3`?**

- a) 3.333...
- b) 3
- c) 4
- d) 1

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) 3 (celočíselné dělení - vrací jen celou část)
</details>

**11. Který operátor kontroluje rovnost?**

- a) `=`
- b) `==`
- c) `===`
- d) `equals`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `==` (jeden `=` je přiřazení, dva `==` je porovnání)
</details>

**12. Co vrátí `range(5)`?**

- a) `[0, 1, 2, 3, 4]`
- b) `[1, 2, 3, 4, 5]`
- c) Čísla od 0 do 4 (ne seznam, ale speciální objekt)
- d) `5`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Čísla od 0 do 4 (range vrací speciální objekt, ne seznam)
</details>

### Část B: Najděte chybu v kódu

**13. Co je špatně?**
```python
for i in range(5)
 print(i)
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

Chybí dvojtečka za `range(5)` → správně: `for i in range(5):`
</details>

**14. Co je špatně?**
```python
if temperature > 38:
print("Horečka")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

Špatné odsazení! Správně:
```python
if temperature > 38:
 print("Horečka") # 4 mezery/tab
```
</details>

**15. Co je špatně?**
```python
temps = [36.6, 37.2, 38.1]
print(temps[3])
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

Index 3 neexistuje! Seznam má indexy 0, 1, 2. → `IndexError: list index out of range`
</details>

**16. Co je špatně?**
```python
result = "Věk: " + 25
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

Nelze sčítat text a číslo! → `TypeError`. Správně: `result = f"Věk: {25}"` nebo `"Věk: " + str(25)`
</details>

**17. Co je špatně?**
```python
temperatures = [36.6, 37.2, 38.1]
for temp in temperature:
 print(temp)
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

Překlep v názvu! Je `temperatures` (množné číslo), ale v cyklu `temperature` (jednotné). → `NameError`
</details>

### Část C: Praktické úkoly

**18. Co vypíše tento program?**
```python
count = 0
for num in [1, 2, 3, 4, 5]:
 if num % 2 == 0:
 count += 1
print(count)
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`2` (počet sudých čísel: 2, 4)
</details>

**19. Co vypíše tento kód?**
```python
for temp in [36.5, 38.5, 37.0]:
 if temp >= 38.0:
 print("Horečka")
 else:
 print("Normální")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

```
Normální
Horečka
Normální
```
</details>

**20. Co vypíše tento program?**
```python
x = 10
if x > 5 and x < 15:
 print("Ano")
else:
 print("Ne")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`Ano` (10 je větší než 5 A zároveň menší než 15, obě podmínky platí)
</details>

**21. Co vypíše tento program?**
```python
for i in range(3):
 print(f"Řádek {i}")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

```
Řádek 0
Řádek 1
Řádek 2
```
(range(3) generuje 0, 1, 2)
</details>

**22. Co vypíše tento kód?**
```python
temp = 37.5
if temp >= 39.0:
 print("A")
else:
 if temp >= 38.0:
 print("B")
 else:
 print("C")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`C` (37.5 není >= 39.0 ani >= 38.0, takže se provede vnořené `else`)
</details>

**23. Doplňte chybějící kód:**

```python
# Vypočítejte BMI (váha / výška²)
weight = 75 # kg
height = 1.80 # m

bmi = ___ # DOPLŇTE

if ___: # DOPLŇTE podmínku pro BMI >= 25
 print("Nadváha")
else:
 print("Normální")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

```python
bmi = weight / (height ** 2)

if bmi >= 25:
 print("Nadváha")
else:
 print("Normální")
```
</details>

**24. Napište kód, který spočítá, kolik je v seznamu hodnot větších než 5**

```python
numbers = [3, 7, 2, 9, 5, 8]
# VÁŠ KÓD ZDE
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

```python
numbers = [3, 7, 2, 9, 5, 8]
count = 0
for num in numbers:
 if num > 5:
 count += 1
print(count) # Vypíše: 3 (čísla 7, 9, 8)
```
</details>

**25. Co udělá `x += 5`?**

- a) Nastaví x na 5
- b) Přičte 5 k x
- c) Vynásobí x pěti
- d) Porovná x s 5

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Přičte 5 k x (je to zkratka pro `x = x + 5`)
</details>

**26. Jak vypíšete všechny prvky seznamu pomocí cyklu?**
```python
fruits = ["jablko", "hruška", "banán"]
# Vyber správný kód:
```

- a) `for i in range(fruits):`
- b) `for fruit in fruits:`
- c) `for fruits in fruit:`
- d) `for i = 0 to 3:`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `for fruit in fruits:` - správná syntaxe pro průchod seznamem
</details>

**27. Co vrátí `True or False`?**

- a) `True`
- b) `False`
- c) Chybu
- d) Záleží na kontextu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `True` (operátor `or` vrací `True`, pokud platí alespoň jedna podmínka)
</details>

**28. Co vrátí `not True`?**

- a) `True`
- b) `False`
- c) `None`
- d) 0

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `False` (operátor `not` vrací opak - negaci)
</details>

**29. Který kód správně kontroluje, zda je číslo mezi 10 a 20 (včetně)?**

- a) `if x > 10 and x < 20:`
- b) `if x >= 10 and x <= 20:`
- c) `if x = 10 or x = 20:`
- d) `if 10 < x < 20:`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `if x >= 10 and x <= 20:` (včetně znamená >= a <=)
</details>

**30. Co se stane, když použijeme proměnnou, která neexistuje?**
```python
print(age) # age není definována
```

- a) `SyntaxError`
- b) `NameError`
- c) `TypeError`
- d) Vypíše `None`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `NameError: name 'age' is not defined`
</details>

### Část D: Klávesové zkratky a speciální znaky

**31. Kterou klávesovou zkratkou zakomentujete/odkomentujete kód v PyCharmu?**

- a) `Ctrl + C`
- b) `Ctrl + K`
- c) `Ctrl + /`
- d) `Alt + /`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `Ctrl + /` (označte řádky a stiskněte pro zakomentování/odkomentování)
</details>

**32. Kterou klávesou odsadíte kód v PyCharmu?**

- a) `Enter`
- b) `Space` (4x)
- c) `Tab`
- d) `Ctrl + I`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `Tab` (vytvoří 4 mezery, použijte `Shift + Tab` pro odsazení zpět)
</details>

**33. Na anglické klávesnici je znak `{` dostupnější než na české. Proč?**

- a) Na české klávesnici znak `{` není
- b) Na anglické stačí `Shift + [`, na české `pravý Alt + B`
- c) Není rozdíl
- d) Na anglické klávesnici je to `Ctrl + [`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Na anglické stačí `Shift + [`, na české `pravý Alt + B` (proto programátoři preferují anglickou klávesnici)

---
</details>

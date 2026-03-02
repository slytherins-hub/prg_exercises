# CVIČENÍ 3: FUNKCE A SEZMANY

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

### Část A: Funkce - základy

**1. Co vrátí tato funkce?**
```python
def calculate(x, y):
 result = x + y

print(calculate(5, 3))
```

- a) 8
- b) None
- c) 5
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) None - funkce nic nevrací (chybí `return`), takže vrací implicitně `None`
</details>

**2. Jaký je rozdíl mezi funkcí a metodou?**

- a) Žádný rozdíl
- b) Funkce se volá samostatně `len(list)`, metoda přes tečku `list.append()`
- c) Funkce jsou rychlejší
- d) Metody jsou zastaralé

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Funkce se volá samostatně (např. `len(numbers)`), metoda se volá na objektu přes tečku (např. `numbers.append(5)`)
</details>

**3. Co znamená princip DRY?**

- a) "Don't Run Yet" - nespouštěj zatím
- b) "Don't Repeat Yourself" - neopakuj se
- c) "Do Require Yield" - vyžaduj yield
- d) "Debug Right Yesterday" - debuguj hned

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) "Don't Repeat Yourself" - pokud píšeš stejný kód vícekrát, zabal ho do funkce
</details>

**4. Co vypíše tento kód?**
```python
def greet(name):
 return f"Ahoj, {name}!"
 print("Konec")

result = greet("Jan")
print(result)
```

- a) Ahoj, Jan! a Konec
- b) Jen Ahoj, Jan!
- c) Jen Konec
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Jen "Ahoj, Jan!" - `return` ukončí funkci, `print("Konec")` se nikdy neprovede
</details>

**5. Jaký je správný Google-style docstring?**

- a) `# Tato funkce počítá BMI`
- b) `"""Počítá BMI."""`
- c)
```python
"""Počítá BMI.

Args:
 weight: Hmotnost v kg
 height: Výška v metrech

Returns:
 BMI jako float
"""
```

- d) `// Počítá BMI`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Trojité uvozovky s popisem, Args a Returns sekcemi
</details>

### Část B: Seznamy - základy a operace

**6. Co je pravda o seznamech?**

- a) Jsou immutable (neměnitelné)
- b) Jsou mutable (měnitelné)
- c) Mohou obsahovat jen čísla
- d) Indexují se od 1

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Jsou mutable - můžeš měnit prvky, přidávat, odebírat (na rozdíl od stringů)
</details>

**7. Co vypíše `[1, 2, 3] + [4, 5]`?**

- a) `[1, 2, 3, 4, 5]`
- b) `[5, 7, 3]`
- c) `15`
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `[1, 2, 3, 4, 5]` - operátor `+` spojuje seznamy (concatenation)
</details>

**8. Co vrátí `[10, 20, 30][1]`?**

- a) 10
- b) 20
- c) 30
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) 20 - index 1 je druhý prvek (indexuje se od 0)
</details>

**9. Co udělá tento kód?**
```python
numbers = [1, 2, 3]
numbers[1] = 99
```

- a) Chybu - seznamy jsou immutable
- b) Vytvoří nový seznam
- c) Změní druhý prvek na 99: `[1, 99, 3]`
- d) Přidá 99 na konec

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Změní druhý prvek na 99 - seznamy jsou mutable, prvky lze měnit
</details>

**10. Co vypíše tento kód?**
```python
names = ["Jan", "Marie", "Petr"]
for i, name in enumerate(names, 1):
 print(f"{i}. {name}")
```

- a) 0. Jan, 1. Marie, 2. Petr
- b) 1. Jan, 2. Marie, 3. Petr
- c) Jan, Marie, Petr
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) 1. Jan, 2. Marie, 3. Petr - `enumerate(list, 1)` začíná číslovat od 1
</details>

### Část C: Metody seznamů

**11. Jaký je rozdíl mezi `append()` a `extend()`?**

- a) Žádný rozdíl
- b) `append()` přidá celý seznam jako jeden prvek, `extend()` přidá jednotlivé prvky
- c) `append()` je rychlejší
- d) `extend()` je zastaralé

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `numbers.append([4, 5])` → `[1, 2, 3, [4, 5]]` (vnořený), `numbers.extend([4, 5])` → `[1, 2, 3, 4, 5]` (rozbalené)
</details>

**12. Co vrátí metoda `sort()`?**

- a) Seřazený seznam
- b) None
- c) True/False
- d) Index

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) None - `sort()` mění seznam na místě (in-place) a nic nevrací
</details>

**13. Co udělá `numbers.pop()`?**

- a) Odebere a vrátí první prvek
- b) Odebere a vrátí poslední prvek
- c) Odebere všechny prvky
- d) Vypíše seznam

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Odebere a vrátí poslední prvek - `pop(0)` by odebralo první
</details>

**14. Kdy použít `sorted()` místo `sort()`?**

- a) Nikdy - `sort()` je vždy lepší
- b) Když chceš zachovat původní seznam nezměněný
- c) Když chceš seřadit vzestupně
- d) Když je seznam krátký

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `sorted(list)` vrací nový seřazený seznam a původní nechává nezměněný. `list.sort()` mění původní seznam.
</details>

**15. Co se stane při `numbers.remove(5)`, když 5 není v seznamu?**

- a) Nic
- b) ValueError
- c) Vrátí None
- d) Odebere první prvek

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) ValueError: list.remove(x): x not in list - proto je lepší nejdřív zkontrolovat `if 5 in numbers:`
</details>

### Část D: Vnořené seznamy

**16. Co vrátí `[[1, 2], [3, 4]][1][0]`?**

- a) 1
- b) 2
- c) 3
- d) 4

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) 3 - `[1][0]` znamená: vezmi druhý řádek `[3, 4]`, z něj první prvek `3`
</details>

**17. Jak vytvoříš matici 2×3 plnou nul?**

- a) `[[0] * 2] * 3`
- b) `[[0, 0, 0], [0, 0, 0]]`
- c) `[0] * 6`
- d) `matrix(2, 3)`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `[[0, 0, 0], [0, 0, 0]]` - varianta a) vytvoří 3 reference na STEJNÝ seznam (nebezpečné!)
</details>

**18. Co vypíše tento vnořený cyklus?**
```python
for i in range(2):
 for j in range(3):
 print(i, j, end=" ")
```

- a) 0 0 0 1 1 1 2 2 2
- b) 0 1 2 0 1 2
- c) 0 0 0 1 0 2 1 0 1 1 1 2
- d) 2 3

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) 0 0 0 1 0 2 1 0 1 1 1 2 - vnější cyklus 2×, vnitřní cyklus pro každou iteraci vnějšího 3×
</details>

### Část E: Kombinace konceptů

**19. Co je špatně v tomto kódu?**
```python
def sum_list(numbers):
 for number in numbers:
 total = total + number
 return total
```

- a) Nic, je to správně
- b) `total` není inicializováno před použitím
- c) Špatná syntaxe cyklu
- d) `return` je mimo funkci

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `total` musí být nejdřív inicializováno: `total = 0` před cyklem, jinak bude UnboundLocalError
</details>

**20. Co vrátí tato funkce?**
```python
def find_maximum(numbers_list):
 max_value = numbers_list[0]
 for item in numbers_list:
 if item > max_value:
 max_value = item
 return max_value

result = find_maximum([3, 7, 2, 9, 1])
```

- a) 3
- b) 7
- c) 9
- d) [3, 7, 2, 9, 1]

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) 9 - funkce najde a vrátí maximální hodnotu ze seznamu

---
</details>

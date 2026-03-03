# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

### Část A: Datové typy a konverze

**1. Jaký je datový typ výsledku: `"5" + "3"`?**

- a) `int` s hodnotou 8
- b) `str` s hodnotou "53"
- c) `float` s hodnotou 8.0
- d) Chyba

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `str` s hodnotou "53" (concatenation řetězců)
</details>

**2. Co vrátí `int("3.14")`?**

- a) 3
- b) 3.14
- c) "3"
- d) ValueError (chyba)

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) ValueError - int() neumí převést desetinné číslo jako string! Musí být: `int(float("3.14"))`
</details>

**3. Co je pravda o stringech v Pythonu?**

- a) Jsou mutable (lze měnit)
- b) Jsou immutable (nelze měnit)
- c) Obsahují pouze ASCII znaky
- d) Mají pevnou délku

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Jsou immutable - po vytvoření nelze změnit, lze jen vytvořit nový string
</details>

**4. Co vrátí `type("123")`?**

- a) `<class 'int'>`
- b) `<class 'str'>`
- c) `<class 'float'>`
- d) 123

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `<class 'str'>` - uvozovky znamená text, ne číslo!
</details>

**5. Jak převést text "37.5" na desetinné číslo?**

- a) `int("37.5")`
- b) `float("37.5")`
- c) `str(37.5)`
- d) `number("37.5")`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `float("37.5")` - int() by vyhodilo chybu, protože "37.5" není celé číslo
</details>

### Část B: Indexování a slicing

**6. Co vypíše `"Python"[1]`?**

- a) "P"
- b) "y"
- c) "t"
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) "y" (indexování od 0: P=0, y=1, t=2, ...)
</details>

**7. Co vrátí `"Hello"[-1]`?**

- a) "H"
- b) "o"
- c) "l"
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) "o" (záporný index = od konce: -1=poslední, -2=předposlední, ...)
</details>

**8. Co vypíše `"Python"[1:4]`?**

- a) "yth"
- b) "ytho"
- c) "Pyt"
- d) "tho"

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) "yth" (slice od indexu 1 DO indexu 4, ale BEZ něj: pozice 1, 2, 3)
</details>

**9. Jak získat string pozpátku?**

- a) `text.reverse()`
- b) `text[::-1]`
- c) `reverse(text)`
- d) `text[-1:]`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `text[::-1]` (slice s krokem -1)
</details>

**10. Co vrátí `"Programming"[::2]`?**

- a) "Pormig"
- b) "Porming"
- c) "Pormn"
- d) "Pormi"

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) "Pormig" (každý druhý znak: P-o-r-m-i-g)
</details>

### Část C: Metody stringů

**11. Co vrátí `" Python ".strip()`?**

- a) `"Python"`
- b) `" Python "`
- c) `"Python "`
- d) `" Python"`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `"Python"` (odstraní mezery z obou stran)
</details>

**12. Co vypíše tento kód?**
```python
text = "python"
print(text.upper())
print(text)
```

- a) PYTHON\nPYTHON
- b) PYTHON\npython
- c) python\npython
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) PYTHON\npython (`.upper()` vrací NOVÝ string, původní se NEMĚNÍ - immutability!)
</details>

**13. Co vrátí `"a,b,c".split(",")`?**

- a) `"abc"`
- b) `["a", "b", "c"]`
- c) `["a,b,c"]`
- d) `("a", "b", "c")`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `["a", "b", "c"]` (seznam stringů)
</details>

**14. Co vrátí `"Hello World".find("o")`?**

- a) 1
- b) 4
- c) 7
- d) 2

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) 4 (první výskyt "o" je na indexu 4: H-e-l-l-o)
</details>

**15. Co udělá `" ".join(["a", "b", "c"])`?**

- a) `"a b c"`
- b) `"abc"`
- c) `["a b c"]`
- d) `"a,b,c"`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `"a b c"` (spojí prvky seznamu s mezerou mezi nimi)
</details>

**16. Co vrátí `"banana".count("a")`?**

- a) 1
- b) 2
- c) 3
- d) 4

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) 3 (b-**a**-n-**a**-n-**a**)
</details>

### Část D: F-stringy a formátování

**17. Co vypíše `f"Hodnota: {3.14159:.2f}"`?**

- a) "Hodnota: 3.14159"
- b) "Hodnota: 3.14"
- c) "Hodnota: 3.1"
- d) "Hodnota: 3"

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) "Hodnota: 3.14" (`.2f` = 2 desetinná místa)
</details>

**18. Co vypíše `f"{5 + 3}"`?**

- a) "5 + 3"
- b) "8"
- c) "53"
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) "8" (f-string vyhodnotí výraz uvnitř `{}`)
</details>

### Část E: Praktické úkoly

**19. Co vypíše tento kód?**
```python
count = 0
for char in "Hello":
 if char in "aeiou":
 count += 1
print(count)
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`2` (samohlásky: e, o)
</details>

**20. Doplň kód pro kontrolu, zda věta obsahuje slovo "python" (case-insensitive):**
```python
sentence = "I love Python!"
if ___: # DOPLŇTE
 print("Obsahuje python")
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

```python
if "python" in sentence.lower():
 print("Obsahuje python")
```
</details>

**21. Napiš kód, který převede `"36.5"` (string) na číslo a přidá 1:**

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

```python
temp_str = "36.5"
temp_num = float(temp_str) # Převod
result = temp_num + 1 # 37.5
```
NEBO jednořádkově: `result = float("36.5") + 1`
</details>

**22. Co vypíše `len("Hello World")`?**

- a) 10
- b) 11
- c) 12
- d) 2

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) 11 (mezera se počítá!)
</details>

### Část F: Debugování

**23. Co udělá breakpoint v PyCharmu?**

- a) Smaže řádek kódu
- b) Zastaví program na daném řádku během debug módu
- c) Označí chybu
- d) Spustí program rychleji

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Zastaví program na daném řádku během debug módu
</details>

**24. Co dělá klávesa F8 v debuggeru?**

- a) Spustí program normálně
- b) Step Over - provede aktuální řádek a posune se dál
- c) Ukončí debugování
- d) Nastaví breakpoint

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Step Over - provede aktuální řádek a posune se na další
</details>

**25. Co dělá klávesa F9 v debuggeru?**

- a) Step Over
- b) Resume - pokračuje do dalšího breakpointu
- c) Zastaví debugování
- d) Vrátí se o řádek zpět

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Resume - pokračuje do dalšího breakpointu (nebo do konce programu)
</details>

### Část G: Najdi chybu

**26. Co je špatně?**
```python
name = "Alice"
name[0] = "a" # Změna na malé "a"
print(name)
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

Stringy jsou IMMUTABLE! Nelze měnit jednotlivé znaky.
Řešení: `name = "a" + name[1:]` nebo `name = name.replace("A", "a")`
</details>

**27. Co je špatně?**
```python
age = input("Věk: ") # Uživatel zadá "25"
age_next_year = age + 1
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`input()` vrací STRING! Musí být: `age = int(input("Věk: "))`
Jinak chyba: TypeError (nelze sčítat string a int)
</details>

**28. Co je špatně?**
```python
text = "python"
text.upper()
print(text)
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`.upper()` vrací NOVÝ string, ale nepřiřazujeme ho! Vypíše "python".
Řešení: `text = text.upper()`
</details>

### Část H: CSV zpracování a seznamy

**29. Co vypíše tento kód?**
```python
data = "Jan,25,Praha"
parts = data.split(",")
print(parts[1])
```

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

`"25"` (druhý prvek pole, ale jako STRING!)
</details>

**30. Co vrátí `enumerate(["a", "b", "c"], start=1)` při první iteraci?**

- a) (0, "a")
- b) (1, "a")
- c) (1, "b")
- d) "a"

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) (1, "a") - `start=1` znamená, že indexování začíná od 1, ne od 0
</details>

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou pro ty, kteří chtějí procvičit nabyté znalosti nad rámec povinných úkolů.

### BONUS 1: Validátor rodného čísla

Napište program pro kontrolu českého rodného čísla a extrakci informací z něj.

**Zadání:**

1. Načtěte rodné číslo od uživatele pomocí `input()`
2. Zkontrolujte základní validitu:

 - Délka musí být přesně 10 znaků
 - Všechny znaky musí být číslice (použijte metodu `.isdigit()`)
3. Pokud je validní, extrahujte informace:

 - Rok narození: První 2 znaky (např. "95")
 - Měsíc: Znaky 2-4 (např. "01" pro muže, "51" pro ženy - u žen +50)
 - Den: Znaky 4-6 (např. "15")
4. Určete pohlaví:

 - Pokud je měsíc > 50, jedná se o ženu (odečtěte 50 od měsíce)
 - Jinak muž
5. Vypište výsledek:
 ```
 === ANALÝZA RODNÉHO ČÍSLA ===
 Rodné číslo: 9501152345
 Platnost: VALIDNÍ

 Datum narození: 15.01.1995
 Pohlaví: Muž

 Kontrolní součet: PLATNÝ
 ```

**Bonusová část:** Zkontrolujte dělitelnost 11:

- Převeďte rodné číslo na `int` a zkontrolujte: `int(birth_num) % 11 == 0`

---

### BONUS 2: Analýza a čištění lékařských záznamů

Napište program pro zpracování CSV dat z databáze pacientů.

**Zadání:**

1. Vytvořte string s CSV daty (každý řádek = jeden pacient):

 ```python
 data = """ JAN NOVÁK , 9501152345, DIABETES
 MARIE SVOBODOVÁ,9652253456,HYPERTENZE
 PETR Dvořák,8803154567, Astma """
 ```

2. Rozdělte data na jednotlivé řádky pomocí `.split("\n")`
3. Pro každý řádek:

	 - Rozdělte na části pomocí `.split(",")`
	 - Očistěte každou část:
		 - Odstraňte mezery (`.strip()`)
		 - Převeďte jméno na title case (první písmeno každého slova velké)
		 - Normalizujte diagnózu na malá písmena
	 - Validujte rodné číslo:
		 - Zkontrolujte délku (musí být 10)
		 - Zkontrolujte, zda obsahuje pouze číslice
	 - Vypište ve formátu:

 ```
 Pacient 1: Jan Novák
 RČ: 9501152345 [VALIDNÍ]
 Diagnóza: diabetes

 Pacient 2: Marie Svobodová
 RČ: 9652253456 [VALIDNÍ]
 Diagnóza: hypertenze

 Pacient 3: Petr Dvořák
 RČ: 8803154567 [VALIDNÍ]
 Diagnóza: astma
 ```

4. Na konci vypište statistiku:

	 - Počet zpracovaných pacientů
	 - Počet validních/nevalidních rodných čísel
	 - Seznam všech unikátních diagnóz (bonus: použijte `set()`)

**Hint:** Pro rozdělení víceřádkového stringu:
```python
lines = data.split("\n")
for i, line in enumerate(lines, start=1):
 parts = line.split(",")
 name = parts[0].strip().title()
 # ... pokračuj zpracováním
```

# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Tuple a list comprehension

**1. Co platí pro `tuple`?**

- a) Je to seznam, který můžeš libovolně měnit
- b) Je to neměnitelná kolekce
- c) Vždy obsahuje jen čísla
- d) Nelze ho projít cyklem

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Je to neměnitelná kolekce
</details>

**2. Co udělá rozbalení níže?**

```python
item_id, quantity, price = ("A101", 4, 99)
```

- a) Vytvoří slovník
- b) Přiřadí 3 hodnoty do 3 proměnných
- c) Seřadí tuple podle velikosti
- d) Vyhodí chybu vždy

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Přiřadí 3 hodnoty do 3 proměnných
</details>

**3. Co vrací `enumerate([10, 20])` v cyklu?**

- a) Jen indexy
- b) Jen hodnoty
- c) Dvojice `(index, hodnota)` jako tuple
- d) Slovník

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Dvojice `(index, hodnota)` jako tuple
</details>

**4. Co udělá tento zápis?**


```python
values = [x * 2 for x in [1, 2, 3]]
```

- a) `[1, 2, 3]`
- b) `[2, 4, 6]`
- c) `[1, 4, 9]`
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `[2, 4, 6]`
</details>

**5. Co dělá podmínka ve výrazu `[..., if podminka]`?**

- a) Řadí seznam
- b) Filtruje položky, které podmínku splní
- c) Automaticky maže duplicity
- d) Přidá nulové hodnoty

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Filtruje položky, které podmínku splní
</details>

**6. Co je hlavní výhoda list comprehension oproti `for + append`?**

- a) Vždy je rychlejší o řády
- b) Je stručnější a často čitelnější pro jednoduché případy
- c) Umožní zapisovat bez závorek
- d) Nahrazuje všechny cykly

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Je stručnější a často čitelnější pro jednoduché případy
</details>

**7. Který zápis je správná list comprehension s podmínkou?**

- a) `[for x in data x if x > 0]`
- b) `[x if x > 0 for x in data]`
- c) `[x for x in data if x > 0]`
- d) `[x in data for if x > 0]`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `[x for x in data if x > 0]`
</details>

### Část B: Soubory

**8. Proč používat `with open(...) as file`?**

- a) Je to kratší zápis
- b) Automaticky zavře soubor
- c) Je to povinné jen pro JSON
- d) Přidá automaticky `strip()`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Automaticky zavře soubor
</details>

**9. K čemu je důležité `encoding="utf-8"`?**

- a) Zrychlí čtení o 50 %
- b) Pomáhá správně načítat české znaky
- c) Je nutné jen pro CSV
- d) Nahrazuje `delimiter`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Pomáhá správně načítat české znaky
</details>

**10. Co řeší `strip()` při čtení textu?**

- a) Seřadí řádky
- b) Odstraní bílé znaky na krajích (`\n`, mezery)
- c) Převádí text na lowercase
- d) Rozdělí řádek podle oddělovače

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Odstraní bílé znaky na krajích
</details>

**11. V sekci CSV se data čtou přes `open(...)` a `split(delimiter)`. Co je `delimiter`?**

- a) Název souboru
- b) Typ kódování
- c) Znak oddělující sloupce
- d) Typ proměnné

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Znak oddělující sloupce
</details>

**12. Co dělá `Path("data") / "soubor.txt"`?**

- a) Dělí text matematicky
- b) Bezpečně skládá cestu
- c) Maže soubor
- d) Vytvoří Git commit

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Bezpečně skládá cestu
</details>

**13. Co dělá `Path("data").glob("*.csv")`?**

- a) Spustí všechny CSV soubory
- b) Najde CSV soubory podle vzoru
- c) Převede CSV na JSON
- d) Otevře Excel

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Najde CSV soubory podle vzoru
</details>

**14. Co nejčastěji vrátí `json.load(...)`?**

- a) Jen textový řetězec
- b) Python `dict` nebo `list` podle obsahu JSON
- c) Vždy jen seznam
- d) Vždy jen slovník

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Python `dict` nebo `list` podle obsahu JSON
</details>

### Část C: PowerShell a Git

**15. Co vypíše `Get-Location` v PowerShellu?**

- a) Obsah složky
- b) Aktuální cestu
- c) Historii příkazů
- d) Verzi Pythonu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Aktuální cestu
</details>

**16. Který příkaz použiješ pro kontrolu změn před commitem?**

- a) `git clone`
- b) `git status`
- c) `git push`
- d) `git pull`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `git status`
</details>

**17. Jaký je správný minimální postup odevzdání?**

- a) `git push -> git add -> git commit`
- b) `git add -> git commit -> git push`
- c) `git commit -> git clone -> git push`
- d) `git pull -> git clone -> git status`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `git add -> git commit -> git push`
</details>

**18. Co dělá `git add .`?**

- a) Přidá všechny změny v aktuální složce a podsložkách
- b) Smaže repozitář
- c) Udělá commit
- d) Nahraje změny na GitHub

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Přidá všechny změny v aktuální složce a podsložkách
</details>

**19. Který příkaz v PowerShellu vypíše obsah textového souboru?**

- a) `Get-Location`
- b) `Get-Content`
- c) `Get-ChildItem`
- d) `Set-Content`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `Get-Content`
</details>

**20. Co typicky dělá `Get-ChildItem`?**

- a) Vypíše aktuální cestu
- b) Vytvoří novou složku
- c) Vypíše obsah složky
- d) Spustí Python skript

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Vypíše obsah složky
</details>

**21. Co je relativní cesta k souboru?**

- a) Cesta začínající od aktuální složky projektu
- b) Cesta vždy začínající od kořene disku
- c) Cesta, která nefunguje ve Windows
- d) Cesta bez přípony souboru

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Cesta začínající od aktuální složky projektu
</details>

**22. Co platí o instalaci Gitu v tomto kurzu?**

- a) Git se instaluje vždy i na školních počítačích
- b) Na školních počítačích je Git připravený, instalace je hlavně pro domácí PC
- c) Git není potřeba, stačí GitHub web
- d) Git je potřeba jen pro bonusové úkoly

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Na školních počítačích je Git připravený, instalace je hlavně pro domácí PC
</details>

**23. Které minimální nastavení je potřeba v Gitu udělat?**

- a) Jen `git config --global core.editor`
- b) Jen `git config --global init.defaultBranch main`
- c) `git config --global user.name` a `git config --global user.email`
- d) `git config --global pull.rebase true`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `git config --global user.name` a `git config --global user.email`
</details>

### Část D: Odevzdání a začátečnické chyby

**24. Co je první doporučený krok v Cíli 6 před spuštěním skriptu?**

- a) `pip install -r requirements.txt`
- b) `uv sync`
- c) `git push`
- d) `git pull`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `uv sync`
</details>

**25. Kdy je úkol považovaný za odevzdaný?**

- a) Jakmile vytvoříš soubor lokálně
- b) Po `git add`
- c) Po `git commit`
- d) Po `git push`, když je změna online na GitHubu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) Po `git push`, když je změna online na GitHubu
</details>

**26. Co uděláš jako první, když si nejsi jistý(á), co je špatně?**

- a) `git reset --hard`
- b) `git status`
- c) `git clone`
- d) `git branch`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `git status`
</details>

**27. Co je při práci v GitHub Classroom dobrý návyk?**

- a) Začít commitovat až na konci semestru
- b) Commitovat průběžně menší změny a pravidelně pushovat
- c) Upravovat i testy a podpůrné soubory
- d) Dělat vždy jen jeden commit bez zprávy

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Commitovat průběžně menší změny a pravidelně pushovat
</details>

---



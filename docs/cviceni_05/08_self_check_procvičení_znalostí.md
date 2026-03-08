# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Tuple a list comprehension

1. **Co platí pro <code>tuple</code>?**
   <ol type="a">
      <li>Je to seznam, který můžeš libovolně měnit</li>
      <li>Je to neměnitelná kolekce</li>
      <li>Vždy obsahuje jen čísla</li>
      <li>Nelze ho projít cyklem</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>tuple</code> je neměnitelná kolekce.

</details>

2. **Co udělá rozbalení níže?**
   ```python
   item_id, quantity, price = ("A101", 4, 99)
   ```
   <ol type="a">
      <li>Vytvoří slovník</li>
      <li>Přiřadí tři hodnoty do tří proměnných</li>
      <li>Seřadí tuple podle velikosti</li>
      <li>Vyhodí chybu vždy</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Přiřadí tří hodnoty do tří proměnných.

</details>

3. **Co vrací <code>enumerate([10, 20])</code> v cyklu?**
   <ol type="a">
      <li>Jen indexy</li>
      <li>Jen hodnoty</li>
      <li>Dvojice <code>(index, hodnota)</code> jako tuple</li>
      <li>Slovník</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Vrací dvojice <code>(index, hodnota)</code> jako tuple.

</details>

4. **Co udělá tento zápis?**
   ```python
   values = [x * 2 for x in [1, 2, 3]]
   ```
   <ol type="a">
      <li><code>[1, 2, 3]</code></li>
      <li><code>[2, 4, 6]</code></li>
      <li><code>[1, 4, 9]</code></li>
      <li>Chybu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Vytvoří nový seznam s hodnotami <code>[2, 4, 6]</code>.

</details>

5. **Co dělá podmínka ve výrazu <code>[..., if podminka]</code>?**
   <ol type="a">
      <li>Řadí seznam</li>
      <li>Filtruje položky, které podmínku splní</li>
      <li>Automaticky maže duplicity</li>
      <li>Přidá nulové hodnoty</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Filtruje položky, které podmínku splní.

</details>

6. **Co je hlavní výhoda list comprehension oproti <code>for + append</code>?**
   <ol type="a">
      <li>Vždy je rychlejší o řády</li>
      <li>Je stručnější a často čitelnější pro jednoduché případy</li>
      <li>Umožní zapisovat bez závorek</li>
      <li>Nahrazuje všechny cykly</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Je stručnější a často čitelnější pro jednoduché případy.

</details>

7. **Který zápis je správná list comprehension s podmínkou?**
   <ol type="a">
      <li><code>[for x in data x if x > 0]</code></li>
      <li><code>[x if x > 0 for x in data]</code></li>
      <li><code>[x for x in data if x > 0]</code></li>
      <li><code>[x in data for if x > 0]</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>[x for x in data if x > 0]</code>

</details>

---

### Část B: Soubory

8. **Proč používat <code>with open(...) as file</code>?**
   <ol type="a">
     <li>Je to kratší zápis</li>
     <li>Automaticky zavře soubor</li>
     <li>Je to povinné jen pro JSON</li>
     <li>Přidá automaticky <code>strip()</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Automaticky zavře soubor

</details>

9. **K čemu je důležité <code>encoding="utf-8"</code>?**
   <ol type="a">
     <li>Zrychlí čtení o 50 %</li>
     <li>Pomáhá správně načítat české znaky</li>
     <li>Je nutné jen pro CSV</li>
     <li>Nahrazuje <code>delimiter</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Pomáhá správně načítat české znaky

</details>

10. **Co řeší <code>strip()</code> při čtení textu?**
   <ol type="a">
     <li>Seřadí řádky</li>
     <li>Odstraní bílé znaky na krajích (<code>\n</code>, mezery)</li>
     <li>Převádí text na lowercase</li>
     <li>Rozdělí řádek podle oddělovače</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Odstraní bílé znaky na krajích

</details>

11. **V sekci CSV se data čtou přes <code>open(...)</code> a <code>split(delimiter)</code>. Co je <code>delimiter</code>?**
   <ol type="a">
     <li>Název souboru</li>
     <li>Typ kódování</li>
     <li>Znak oddělující sloupce</li>
     <li>Typ proměnné</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Znak oddělující sloupce

</details>

12. **Co dělá <code>Path("data") / "soubor.txt"</code>?**
   <ol type="a">
     <li>Dělí text matematicky</li>
     <li>Bezpečně skládá cestu</li>
     <li>Maže soubor</li>
     <li>Vytvoří Git commit</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Bezpečně skládá cestu

</details>

13. **Co dělá <code>Path("data").glob("*.csv")</code>?**
   <ol type="a">
     <li>Spustí všechny CSV soubory</li>
     <li>Najde CSV soubory podle vzoru</li>
     <li>Převede CSV na JSON</li>
     <li>Otevře Excel</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Najde CSV soubory podle vzoru

</details>

14. **Co nejčastěji vrátí <code>json.load(...)</code>?**
   <ol type="a">
     <li>Jen textový řetězec</li>
     <li>Python <code>dict</code> nebo <code>list</code> podle obsahu JSON</li>
     <li>Vždy jen seznam</li>
     <li>Vždy jen slovník</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Python <code>dict</code> nebo <code>list</code> podle obsahu JSON

</details>

---

### Část C: PowerShell a Git

15. **Co vypíše <code>Get-Location</code> v PowerShellu?**
   <ol type="a">
     <li>Obsah složky</li>
     <li>Aktuální cestu</li>
     <li>Historii příkazů</li>
     <li>Verzi Pythonu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Aktuální cestu

</details>

16. **Který příkaz použiješ pro kontrolu změn před commitem?**
   <ol type="a">
     <li><code>git clone</code></li>
     <li><code>git status</code></li>
     <li><code>git push</code></li>
     <li><code>git pull</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>git status</code>

</details>

17. **Jaký je správný minimální postup odevzdání?**
   <ol type="a">
     <li><code>git push → git add → git commit</code></li>
     <li><code>git add → git commit → git push</code></li>
     <li><code>git commit → git clone → git push</code></li>
     <li><code>git pull → git clone → git status</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>git add → git commit → git push</code>

</details>

18. **Co dělá <code>git add .</code>?**
   <ol type="a">
     <li>Přidá všechny změny v aktuální složce a podsložkách</li>
     <li>Smaže repozitář</li>
     <li>Udělá commit</li>
     <li>Nahraje změny na GitHub</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Přidá všechny změny v aktuální složce a podsložkách

</details>

19. **Který příkaz v PowerShellu vypíše obsah textového souboru?**
   <ol type="a">
     <li><code>Get-Location</code></li>
     <li><code>Get-Content</code></li>
     <li><code>Get-ChildItem</code></li>
     <li><code>Set-Content</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>Get-Content</code>

</details>

20. **Co typicky dělá <code>Get-ChildItem</code>?**
   <ol type="a">
     <li>Vypíše aktuální cestu</li>
     <li>Vytvoří novou složku</li>
     <li>Vypíše obsah složky</li>
     <li>Spustí Python skript</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Vypíše obsah složky

</details>

21. **Co je relativní cesta k souboru?**
   <ol type="a">
     <li>Cesta začínající od aktuální složky projektu</li>
     <li>Cesta vždy začínající od kořene disku</li>
     <li>Cesta, která nefunguje ve Windows</li>
     <li>Cesta bez přípony souboru</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Cesta začínající od aktuální složky projektu

</details>

22. **Co platí o instalaci Gitu v tomto kurzu?**
   <ol type="a">
     <li>Git se instaluje vždy i na školních počítačích</li>
     <li>Na školních počítačích je Git připravený, instalace je hlavně pro domácí PC</li>
     <li>Git není potřeba, stačí GitHub web</li>
     <li>Git je potřeba jen pro bonusové úkoly</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Na školních počítačích je Git připravený, instalace je hlavně pro domácí PC

</details>

23. **Které minimální nastavení je potřeba v Gitu udělat?**
   <ol type="a">
     <li><code>git config --global core.editor</code></li>
     <li><code>git config --global init.defaultBranch main</code></li>
     <li><code>git config --global user.name</code> a <code>git config --global user.email</code></li>
     <li><code>git config --global pull.rebase true</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>git config --global user.name</code> a <code>git config --global user.email</code>

</details>

---

### Část D: Odevzdání a začátečnické chyby

24. **Co je první doporučený krok v Cíli 6 před spuštěním skriptu?**
   <ol type="a">
     <li><code>pip install -r requirements.txt</code></li>
     <li><code>uv sync</code></li>
     <li><code>git push</code></li>
     <li><code>git pull</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>uv sync</code>

</details>

25. **Kdy je úkol považovaný za odevzdaný?**
   <ol type="a">
     <li>Jakmile vytvoříš soubor lokálně</li>
     <li>Po <code>git add</code></li>
     <li>Po <code>git commit</code></li>
     <li>Po <code>git push</code>, když je změna online na GitHubu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Po <code>git push</code>, když je změna online na GitHubu

</details>

26. **Co uděláš jako první, když si nejsi jistý(á), co je špatně?**
   <ol type="a">
     <li><code>git reset --hard</code></li>
     <li><code>git status</code></li>
     <li><code>git clone</code></li>
     <li><code>git branch</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>git status</code>

</details>

27. **Co je při práci v GitHub Classroom dobrý návyk?**
   <ol type="a">
     <li>Začít commitovat až na konci semestru</li>
     <li>Commitovat průběžně menší změny a pravidelně pushovat</li>
     <li>Upravovat i testy a podpůrné soubory</li>
     <li>Dělat vždy jen jeden commit bez zprávy</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Commitovat průběžně menší změny a pravidelně pushovat

</details>

---

# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## CÍL 6: ZADÁNÍ A ODEVZDÁNÍ ÚKOLU

### ZADÁNÍ

#### ÚKOL: [Analýza buněk](https://classroom.github.com/a/touYQP1y)

Tahle úloha simuluje jednoduchou datovou analýzu, jakou bys řešil(a) třeba v laboratorní praxi: dostaneš měření v čase, 
ověříš kvalitu dat a připravíš výstup, který může jít dál do reportu nebo vizualizace. 
Cílem není jen „aby to prošlo testy", ale hlavně procvičit kompletní tok práce s daty od načtení po uložení výsledků.

### ❗❗ POVINNÉ ODEVZDÁNÍ

<ul style="color:#c62828;">
  <li>Pro splnění cvičení je nezbytné odevzdat řešení do repozitáře v GitHub Classroom.</li>
  <li>Správnost řešení bude kontrolována pomocí automatických testů.</li>
  <li>Řešení bude kontrolováno na přítomnost plagiátů mezi studenty.</li>
  <li>Odevzdání a případné úpravy v repozitáři je nutné provést nejpozději do konce cvičení.</li>
</ul>

---

### GitHub Classroom

GitHub Classroom je systém, přes který budeme v předmětu zadání přijímat i odevzdávat. Každý úkol dostaneš jako odkaz od vyučujícího.

Po kliknutí na odkaz se ti automaticky vytvoří vlastní repozitář pro daný úkol. Ten si potom naklonuješ do počítače a pracuješ v něm stejně jako v běžném Git repozitáři.

Když máš hotovo, změny uložíš přes `git add` + `git commit` a odešleš přes `git push` na GitHub. Tím je odevzdání online a vyučující ho může vidět.

Po odevzdání se obvykle spustí automatická kontrola. Testy zkontrolují správnost tvého kódu a uvidíš, co prošlo a co je potřeba ještě opravit.

### Jak vhodně postupovat pro odevzdání

0. Připrav prostředí v repozitáři:
   ```powershell
   uv sync
   ```
1. Zkontroluj stav repozitáře:
   ```powershell
   git status
   ```
2. Přidej jen požadovaný soubor:
   ```powershell
   git add assignment.py
   ```
3. Ulož změnu do commitu:
   ```powershell
   git commit -m "Pridani assignment.py"
   ```
4. Odešli změnu na GitHub:
   ```powershell
   git push origin main
   ```
5. Tímto krokem úkol odevzdáváš (změna je online na GitHubu) a hned to zkontroluj v repozitáři na GitHubu.
6. Když odevzdání nebo testy neprojdou, iteruj hlavně body **1 → 2 → 3 → 4 → 5**. Po opravě kódu je zopakuj znovu ve stejném pořadí.

> **Tip:** Po `git push` otevři repozitář na GitHubu a ověř, že je tam nový commit i soubor `assignment.py`.

> **⚠️ Pozor:** Když `git status` ukazuje více změn, nepřidávej je všechny naslepo přes `git add .`. Pro odevzdání přidej jen to, co zadání opravdu chce.

---

### Časté problémy začátečníků (a rychlé řešení)

- **Jsi ve špatné složce**
    - Příznak: `git status` hlásí, že nejsi v repozitáři.
    - Řešení:
       ```powershell
       pwd
       cd .\NAZEV_REPOZITARE
       git status
       ```

- **Není připravené prostředí pro Python**
    - Příznak: skript nejde spustit nebo chybí balíčky.
    - Řešení:
       ```powershell
       uv sync
       uv run python .\assignment.py
       ```

- **Zapomněl(a) jsi `git add` před commitem**
    - Příznak: commit napíše „nothing to commit“.
    - Řešení:
       ```powershell
       git status
       git add assignment.py
       git commit -m "Doplneni reseni"
       ```

> **Tip:** Když si nejsi jistý(á), vždy začni `git status`. Ve většině případů ti hned napoví, co udělat dál.

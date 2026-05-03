# CVIČENÍ 9: ZÁKLADY GIT A GITHUB

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Základy Gitu

**1. Co udělá příkaz `git init`?**

- a) Naklonuje vzdálený repozitář
- b) Vytvoří nový prázdný gitový repozitář v aktuální složce
- c) Nainstaluje Git
- d) Odstraní repozitář

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Vytvoří nový prázdný gitový repozitář v aktuální složce (vytvoří skrytou složku `.git`)
</details>

**2. Co znamená, když `git status` zobrazí soubor červeně?**

- a) Soubor obsahuje chybu
- b) Soubor je smazaný
- c) Soubor je změněný nebo nesledovaný (není ve stage)
- d) Soubor je připravený ke commitu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Soubor je změněný nebo nesledovaný – musíš ho nejdřív přidat do stage pomocí `git add`
</details>

**3. Jaký je správný postup pro uložení změn do Gitu?**

- a) `git add` → `git commit`
- b) `git commit` → `git add`
- c) `git push` → `git commit`
- d) `git save`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Nejdřív `git add soubor` (přidá do stage), pak `git commit -m "popis"` (vytvoří revizi)
</details>

**4. Co dělá příkaz `git diff`?**

- a) Zobrazí rozdíl mezi dvěma větvemi
- b) Přejmenuje soubor
- c) Smaže rozdíly mezi soubory
- d) Zobrazí změny v souborech oproti poslednímu commitu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) Zobrazí změny v souborech, které ještě nejsou ve stage – červené řádky s `-` byly odebrány, zelené s `+` přibyly
</details>

**5. K čemu slouží soubor `.gitignore`?**

- a) Ignoruje chyby v kódu
- b) Zamyká soubory před úpravami
- c) Skrývá historii commitů
- d) Říká Gitu, které soubory a složky nemá sledovat

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) `.gitignore` říká Gitu, které soubory a složky nemá sledovat – např. `.venv/`, `__pycache__/`, `.idea/`
</details>

**6. K čemu slouží příkaz `gitk --all`?**

- a) Smaže všechny větve
- b) Otevře grafický prohlížeč historie Gitu se všemi větvemi
- c) Vytvoří novou větev
- d) Naklonuje repozitář

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `gitk --all` otevře grafické okno, kde přehledně vidíš celou historii revizí, větve a jejich sloučení
</details>

**7. Co je `git gui`?**

- a) Příkaz pro smazání repozitáře
- b) Příkaz pro zobrazení konfliktu
- c) Editor zdrojového kódu
- d) Grafické rozhraní Gitu, které nahrazuje příkazy `git add`, `git commit` a `git push`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) `git gui` je grafické rozhraní, ve kterém můžeš přehledně přidávat soubory do stage, psát commit zprávy a nahrávat změny – vše klikáním místo psaní příkazů
</details>

---

### Část B: Větvení

**8. Co je větev (branch) v Gitu?**

- a) Samostatná linie vývoje, kde můžeš dělat změny nezávisle na hlavní větvi
- b) Kopie celého repozitáře
- c) Záloha souborů
- d) Název pro commit

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Samostatná linie vývoje – můžeš na ní experimentovat, aniž bys ovlivnil/a hlavní větev `main`
</details>

**9. Jaký je rozdíl mezi `git branch nazev` a `git switch -c nazev`?**

- a) Žádný, dělají totéž
- b) `git branch` smaže větev
- c) `git switch -c` je zastaralý příkaz
- d) `git branch` pouze vytvoří větev, `git switch -c` ji vytvoří A přepne na ni

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) `git branch nazev` jen vytvoří větev (zůstaneš kde jsi), `git switch -c nazev` vytvoří větev a rovnou na ni přepne
</details>

**10. Co se stane, když spustíš `git merge` a na stejných řádcích jsou různé změny?**

- a) Git automaticky vybere novější verzi
- b) Git smaže oba soubory
- c) Vznikne konflikt, který musíš vyřešit ručně
- d) Merge se automaticky zruší

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Vznikne **merge conflict** – Git do souboru vloží značky (`<<<<<<<`, `=======`, `>>>>>>>`) a musíš ručně rozhodnout, kterou verzi ponechat
</details>

**11. Co znamenají značky ve merge konfliktu?**

```
<<<<<<< HEAD
    print("verze A")
=======
    print("verze B")
>>>>>>> feature
```

- a) Obě verze jsou špatně
- b) `HEAD` je tvá aktuální verze, `feature` je verze z druhé větve
- c) Git vybral verzi A
- d) Soubor je poškozený

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Mezi `<<<<<<< HEAD` a `=======` je tvá aktuální verze, mezi `=======` a `>>>>>>> feature` je verze z větve `feature`. Vyber co chceš zachovat a smaž značky.
</details>

**12. Co udělá `git branch -d test`?**

- a) Vytvoří větev `test`
- b) Přepne na větev `test`
- c) Smaže větev `test` (pokud je sloučená)
- d) Přejmenuje větev na `test`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Smaže větev `test`, ale pouze pokud už byla sloučena do aktuální větve. Git tě tím chrání před ztrátou práce.
</details>

---

### Část C: Spolupráce přes GitHub

**13. Co je rozdíl mezi `git clone` a `git init`?**

- a) `git clone` vytvoří kopii existujícího vzdáleného repozitáře, `git init` vytvoří nový prázdný repozitář
- b) Žádný
- c) `git init` je novější verze `git clone`
- d) `git clone` funguje jen na GitHubu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `git clone URL` stáhne existující repozitář (včetně celé historie), `git init` založí nový prázdný repozitář od nuly
</details>

**14. Co je fork na GitHubu?**

- a) Smazání repozitáře
- b) Stažení repozitáře do počítače
- c) Sloučení dvou repozitářů
- d) Vytvoření vlastní kopie cizího repozitáře na tvém GitHub účtu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) Fork vytvoří tvou vlastní kopii cizího repozitáře na GitHubu – můžeš v ní dělat změny, aniž bys zasáhl/a do originálu
</details>

**15. Co je pull request?**

- a) Příkaz pro stažení změn
- b) Automatický test kódu
- c) Způsob, jak smazat větev
- d) Žádost o začlenění tvých změn do původního repozitáře

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

d) Pull request je žádost o začlenění tvých změn – majitel repozitáře je zkontroluje (code review) a rozhodne, zda je začlení
</details>

**16. Jaký je rozdíl mezi `git push` a `git pull`?**

- a) Žádný
- b) `git push` nahraje tvé commity na vzdálený repozitář, `git pull` stáhne změny od ostatních
- c) `git pull` nahraje změny, `git push` je stáhne
- d) `git push` funguje jen s forkem

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `git push` = odeslání tvých revizí na GitHub, `git pull` = stažení a sloučení změn, které nahrál někdo jiný
</details>

---

### Část D: Praktické situace

**17. Napsal/a jsi kód, který nefunguje. Co uděláš, abys viděl/a, co jsi od posledního commitu změnil/a?**

- a) `git diff`
- b) `git status`
- c) `git log`
- d) `git show`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `git diff` – ukáže přesně které řádky se změnily oproti poslednímu commitu. Chyba musí být na některém z nich. (`git status` jen ukáže názvy změněných souborů, ne jejich obsah.)
</details>

**18. Chceš začít pracovat na nové funkci, aniž bys riskoval/a rozbití hlavního kódu. Co uděláš?**

- a) Pracuješ přímo na větvi `main`
- b) Smažeš repozitář a začneš znovu
- c) Vytvoříš novou větev: `git switch -c nova_funkce`
- d) Zkopíruješ si složku ručně

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Vytvoříš novou větev – pracuješ na ní izolovaně a hlavní větev `main` zůstane nedotčená. Až bude funkce hotová, sloučíš ji zpět pomocí `git merge`.
</details>

**19. Co musíš udělat PŘED přepnutím na jinou větev?**

- a) Smazat všechny soubory
- b) Ujistit se, že máš všechny změny uložené v commitu (nebo že working tree je čistý)
- c) Odpojit se od internetu
- d) Nic, můžeš přepínat kdykoli

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Před přepnutím si ověř `git status` – pokud máš neuložené změny, buď je commitni, nebo je dočasně ulož přes `git stash`
</details>

**20. Jaká je správná zpráva k commitu?**

- a) `Add function for BMI calculation`
- b) `asdf`
- c) `changes`
- d) `update`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) `Add function for BMI calculation` – dobrá commit zpráva začíná velkým písmenem, je stručná (do 50 znaků), v činném rodě a popisuje **co** bylo změněno
</details>

**21. Kolega ti poslal odkaz na repozitář na GitHubu. Chceš si stáhnout kód a pracovat na něm lokálně. Jaký příkaz použiješ?**

- a) `git init`
- b) `git pull`
- c) `git clone URL`
- d) `git fork URL`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `git clone URL` – vytvoří lokální kopii vzdáleného repozitáře včetně celé jeho historie. (`git fork` jako příkaz neexistuje – fork se dělá přes webové rozhraní GitHubu.)
</details>

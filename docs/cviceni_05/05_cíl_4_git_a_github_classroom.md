# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## CÍL 4: GIT A GITHUB

Kód dnes nestačí jen napsat, musíš ho umět verzovat a sdílet.

Git je v praxi standard skoro všude, kde se dělá software:

- ve firmách,
- ve výzkumu,
- v open-source projektech,
- ve školních projektech a domácích úkolech.

Když Git neumíš, narážíš při každé týmové práci.
Když ho umíš, máš okamžitě lepší kontrolu nad kódem.

Proč je Git + GitHub tak super:

- mít historii změn,
- vrátit se bezpečně o krok zpět, když něco rozbiješ,
- neztratit práci,
- spolupracovat s ostatními bez chaosu v souborech,
- mít jasný přehled kdo, co a kdy změnil,
- sdílet a odevzdat řešení přes GitHub.

V tomhle cvičení nejde o teorii navíc.
Jde o návyk, který budeš používat prakticky v každém dalším projektu.
Je dobré začít Git používat hned, ať si na ten workflow zvykneš co nejdřív.

---

### 4.0 Příprava na GitHub

Aby ti zbytek CÍLE 4 šel hladce, drž se tohoto pořadí:

1. Povinné: zkontroluj, že máš GitHub účet.
   - [Doplněk: Založení GitHub účtu](07_doplnek_github_ucet.md)
2. Doma: pokud Git nemáš, nainstaluj ho podle doplňku (viz minimální nastavení níže).
   - [Doplněk: Instalace Gitu (jen pro domácí počítač)](09_doplnek_instalace_gitu.md)
3. Povinné: nastav minimální Git identitu (`jméno`, `email`).
   - tenhle krok udělej i když Git neinstaluješ (např. už Git máš).
4. Volitelné: požádej o studentský GitHub benefit.
   - [Doplněk: GitHub Student Developer Pack (nepovinné)](08_doplnek_github_student_pack.md)

#### Minimální nastavení Gitu (jméno + email)

Instalaci Gitu najdeš v doplňku:  
[Doplněk: Instalace Gitu (jen pro domácí počítač)](09_doplnek_instalace_gitu.md)

Na školních počítačích je Git už připravený.

Nejdřív ověř, že Git funguje:

```powershell
git --version
```

Pak nastav minimální identitu (uděláš jednou):

```powershell
git config --global user.name "Tvoje Jmeno"
git config --global user.email "tvuj@email.cz"
```

Kontrola:

```powershell
git config --global --list
```

---

### 4.1 Co je Git a co je GitHub?

**Git** je systém pro verzování kódu.

- běží lokálně na tvém počítači,
- pamatuje si změny v čase,
- dovolí ti vrátit se k předchozí verzi.

**GitHub** je webová služba nad Gitem.

- ukládá repozitáře online,
- umožní sdílení a spolupráci,
- používá se pro sdílení i odevzdání.

Krátce:

- Git = „motor“ verzování.
- GitHub = „online místo“, kam ten motor posílá historii.

---

### 4.2 Základní princip práce s Gitem

Základní tok práce s Gitem:

- `clone` = stáhneš si zadání k sobě,
- `add` = vybereš konkrétní změny, které chceš odevzdat,
- `commit` = uložíš checkpoint své práce,
- `push` = nahraješ checkpoint na GitHub,
- `pull` = stáhneš novější změny z GitHubu.

`commit` je jako „uložený stav projektu“.  
Neukládá jen jeden soubor, ale celý stav změn, které předtím označíš přes `git add`.

---

### 4.3 Co znamenají hlavní příkazy

`git status`

- řekne, co je změněné,
- je to první diagnostický příkaz, když si nejsi jistý.

`git clone <URL>`

- vytvoří lokální kopii repozitáře.

`git add <soubor>`

- označí změny, které chceš dát do dalšího commitu.

`git add .`

- označí všechny změny v aktuální složce a podsložkách,
- je rychlé, ale pro odevzdání bývá bezpečnější přidat jen konkrétní soubor(y) podle zadání.

`git commit -m "zprava"`

- uloží checkpoint změn s komentářem.

`git push`

- pošle lokální commity na GitHub.

`git pull`

- stáhne změny z GitHubu do tvé lokální kopie.

---

### 4.4 Základní workflow na GitHubu

```powershell
git clone <URL_REPOZITARE>
cd <NAZEV_REPOZITARE>
git status
git add assignment.py
git commit -m "Doplneni reseni ukolu"
git push origin main
```

Když potřebuješ stáhnout nové změny:

```powershell
git pull origin main
```

---

### 4.5 Co vždy zkontrolovat před commitem/pushem

1. Jsi ve správné složce repozitáře?
2. Upravuješ správný soubor podle zadání?
3. Co přesně ukazuje `git status`?

> **Tip:** Obvykle upravuješ jen soubor(y) určené zadáním.  
> Testy ani jiné podpůrné soubory neupravuj.

---

### 4.6 Když se něco rozbije: jednoduchý záchranný postup

Tohle je důležitý trik pro začátečníky.

Když je repozitář rozbitý nebo jsi ztracený v chybách:

1. Vytvoř si novou čistou složku.
2. Znovu proveď `git clone`.
3. Pokud máš v původní složce důležité změny, zkopíruj si je bokem.
4. Přetáhni ten jeden soubor (nebo pár souborů) do nové čisté složky.
5. Udělej `git status`, `git add`, `git commit`, `git push`.

Tohle je často rychlejší a bezpečnější než dlouhé „zachraňování“ rozbitého stavu.

> **Pozor:** Než starou složku smažeš, vždy si z ní vytáhni soubory, které chceš zachovat.

---

### 4.7 Typický scénář

1. Vytvoříš repozitář nebo ho zkopíruješ na GitHubu.
2. Naklonuješ repozitář.
3. Doplníš řešení.
4. `git add`, `git commit`, `git push`.
5. Na GitHubu ověříš, že se změny propsaly.

---

> **💡 Poznámka:** Git umí výrazně víc než základní `add/commit/push` — třeba větve (`branch`), spojování změn (`merge`), přepis historie (`rebase`), dočasné odložení práce (`stash`) nebo návrat k předchozímu stavu. V tomhle cíli držíme jednoduchý základ, pokročilé možnosti si ukážeme později.


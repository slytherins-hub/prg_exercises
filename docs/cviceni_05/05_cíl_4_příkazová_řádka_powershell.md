# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## CÍL 4: PŘÍKAZOVÁ ŘÁDKA (POWERSHELL, BASH, TERMINAL)
 
V praxi ji používáš, když:

- spouštíš CLI nástroje (CLI = *Command-Line Interface*, tedy nástroje ovládané příkazy, např. `uv`, testy, build),
- potřebuješ rychle pracovat se soubory bez klikaní,
- chceš stejný postup zopakovat přesně znovu.

Editor řeší psaní kódu. Terminál řeší práci kolem kódu.

Co ti to dá v praxi:

- ušetří čas: místo 20 kliknutí použiješ 1-2 příkazy,
- sníží chyby: stejný příkaz = stejný výsledek,
- zlepší spolupráci: postup můžeš jednoduše poslat kolegovi,
- umožní automatizaci: vytvoříš skript (`.ps1`, `.sh`), který vše udělá za tebe.

Typické situace, kde to běžný programátor řeší:

- připravit projekt po stažení repozitáře,
- spustit testy nebo build jedním příkazem,
- hromadně zpracovat soubory ve složce,
- rychle ověřit, co se v projektu změnilo.

Dnes navíc často využiješ i AI: necháš si navrhnout příkazy pro složitější úkol.  
Když umíš terminál, poznáš, co příkaz dělá, upravíš si ho a použiješ bezpečně.

> **Pozor:** Příkazy od AI nikdy nespouštěj naslepo. Nejdřív zkontroluj, co přesně změní.

---

### 4.1 Co je terminal a co je shell?

- **Terminal** = aplikace/okno, kam píšeš příkazy.
- **Shell** = program uvnitř terminálu, který příkazy vykonává.

Typicky:

- **Windows Terminal** + **PowerShell**
- **macOS Terminal** + **zsh** (bash příkazy fungují velmi podobně)
- **Linux terminal** + **bash**

> **Poznámka:** Když se učíš bash příkazy, využiješ je na Linuxu, macOS i v Git Bash/WSL na Windows.

---

### 4.2 Proč se vyplatí znát i bash?

Bash je velmi rozšířený standard na Linuxu a serverech.

Praktický dopad:

- návody na internetu jsou často psané v bash syntaxi,
- deployment skripty bývají v bash,
- když se někdy připojíš na server, bash se bude hodit.

PowerShell je skvělý ve Windows. Bash je skvělý pro přenositelnost mezi systémy.

---

### 4.3 Základní orientace v terminálu

> **Poznámka:** Příkazová řádka je dostupná i přímo v PyCharmu (spodní panel **Terminal**), takže nemusíš odcházet z editoru.

| Co chceš udělat               | PowerShell (Windows) | Bash (Linux/macOS/Git Bash/WSL) | cmd (Windows)     | Co to dělá                                                                 |
| ----------------------------- | -------------------- | ------------------------------- | ----------------- | -------------------------------------------------------------------------- |
| Zjistit, kde právě jsi        | `pwd`                | `pwd`                           | `cd`              | Vypíše aktuální složku (working directory).                                |
| Vypsat obsah složky           | `ls`                 | `ls`                            | `dir`             | Zobrazí soubory a podsložky v aktuální složce.                             |
| Přejít do složky `cviceni_05` | `cd .\cviceni_05`    | `cd ./cviceni_05`               | `cd .\cviceni_05` | Změní aktuální složku na `cviceni_05`.                                     |
| Vrátit se o složku výš        | `cd ..`              | `cd ..`                         | `cd ..`           | Přesune tě do nadřazené složky (parent directory).                         |
| Vytvořit složku `data`        | `mkdir .\data`       | `mkdir -p ./data`               | `mkdir .\data`    | Vytvoří novou složku `data` (v bash `-p` nehlásí chybu, když už existuje). |

---

### 4.4 Spuštění Python skriptu

V tomto repozitáři používej `uv`:

=== "PowerShell"
    ```powershell
    uv run python .\analyza.py
    ```

=== "Bash"
    ```bash
    uv run python ./analyza.py
    ```

Když má cesta mezery, dej ji do uvozovek:

=== "PowerShell"
    ```powershell
    uv run python ".\moje slozka\analyza.py"
    ```

=== "Bash"
    ```bash
    uv run python "./moje slozka/analyza.py"
    ```

> **Poznámka:** Obecně se Python skripty spouští přes `python soubor.py`. V tomhle repozitáři ale používej `uv run python soubor.py`, protože chceš běžet v projektovém prostředí. `uv` si Python vybere podle nastavení projektu (hlavně `requires-python` v `pyproject.toml`) a použije kompatibilní verzi.

---

### 4.5 Praktické triky, které šetří čas

#### Otevření terminálu přímo ve složce

- V Průzkumníku otevři složku projektu.
- Klikni do adresního řádku, napiš `powershell` (nebo `wt`) a potvrď Enter.
- Alternativa: Shift + pravé tlačítko ve složce → otevřít terminál zde.

#### Další užitečné návyky

- `Tab` doplňuje názvy souborů a složek.
- Šipka nahoru vrací poslední příkazy.
- `Ctrl + C` zastaví běžící proces.
- Soubory můžeš přetáhnout myší do terminálu a cesta se vloží sama.

**BONUS: Terminálový warm-up (dobrovolné)**

1. Otevři terminál přímo ve složce projektu (ne přes ruční `cd` z jiné náhodné složky).
2. Vypiš aktuální složku a její obsah.
3. Vytvoř složku `temp_data`.
4. V PyCharmu vytvoř soubor `temp_data/hello.py` a zapiš do něj program `print("Hello world")`.
5. Spusť `temp_data/hello.py` z terminálu (v tomhle repozitáři přes `uv run python ...`).

---

# CVIČENÍ 9: ZÁKLADY GIT A GITHUB

Algoritmizace a programování

## ÚVOD

V tomto cvičení se blíže seznámíš se systémem Git, který už znáš z domácích úkolů. Git je univerzální nástroj pro správu
a synchronizaci dat v souborech. Je to verzovací nástroj – zaznamenává změny prováděné v souborech v průběhu času, 
takže můžeš kdykoli obnovit konkrétní verzi.

Naučíš se Git nakonfigurovat, inicializovat repozitář, sledovat soubory, připravovat je k zápisu (stage),
zapisovat revize (commit) a vytvářet větve (branches). Seznámíš se také s platformou GitHub pro správu vzdálených repozitářů.

### Proč se učit Git?

Představ si, že pracuješ na analýze pacientských dat. Máš skript, který funguje perfektně – a pak ho „vylepšíš"
a všechno se rozbije. Bez Gitu máš smůlu. S Gitem se prostě vrátíš k verzi, která fungovala.

Git v praxi používá skoro každý, kdo píše kód:

- vývojáři ve firmách,
- vědci analyzující data z klinických studií,
- bioinformatici sdílející genomické analýzy,
- studenti odevzdávající domácí úkoly.

Kód bez Gitu je jako laboratorní deník bez datumů – nevíš, co jsi kdy změnil/a a proč.

### Co se v tomto cvičení naučíš?

1. **Základy práce s Git:**
    * Globální nastavení Gitu (jméno, email)
    * Inicializace repozitáře (`git init`)
    * Sledování souborů (`git add`)
    * Vytváření revizí (`git commit`)
    * Zobrazení změn (`git diff`, `git status`)
    * Procházení historie (`git log`, `git show`)

2. **Větvení v Gitu:**
    * Vytváření větví (`git branch`)
    * Přepínání mezi větvemi (`git switch`)
    * Slučování větví (`git merge`)
    * Řešení konfliktů při slučování

3. **Spolupráce přes GitHub:**
    * Klonování repozitáře (`git clone`)
    * Fork a pull request
    * Nahrávání změn (`git push`)
    * Stahování změn (`git pull`)
    * Code review workflow

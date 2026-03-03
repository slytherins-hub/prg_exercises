# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## ÚVOD

Ve cvičení 3 jsi poznal základ funkcí.  
Teď na to navážeme praktičtěji:

- budeš psát funkce s čistým rozhraním,
- rozdělíš program do více souborů (modulů),
- naučíš se, co je dobrá základní struktura Python repozitáře,
- pochopíš, jak fungují automatické testy a proč bez nich nejde dělat větší projekty.

Hlavní praktický příklad bude program, který určí, jestli se dvě kružnice protínají.

<p style="color:#c62828; font-size:1.25rem;"><strong>❗ Cvičení je nezbytné odevzdat do e-learningu.</strong></p>

### Co se v tomto cvičení naučíte?

1. **Rozšířená práce s funkcemi:**

- povinné a nepovinné parametry,
- pojmenované argumenty,
- návrat více hodnot,
- lokální a globální proměnné.

2. **Moduly a importy:**

- proč dělit kód do více souborů,
- různé styly importu,
- kdy použít `if __name__ == "__main__":`.

3. **Modulární mini-projekt:**

- výpočet průniku kružnic přes více funkcí a souborů.

4. **Testy v Pythonu (teoreticky):**

- jak přemýšlet o testovacích případech,
- jak číst výstup testů,
- jak testy zapadají do běžného workflow.

5. **Standardní struktura Python repozitáře:**

- co kam patří (`src/`, `tests/`, `README.md`, `pyproject.toml`),
- proč je to důležité pro čitelnost a spolupráci.

> **💡 Tip:** Cílem tohoto cvičení není napsat co nejvíc kódu, ale naučit se lepší organizaci kódu. Tohle využiješ v každém větším úkolu.

### Jak tímhle cvičením projít prakticky

1. V Cíli 1 si natrénuj volání funkcí (poziční vs pojmenované argumenty) na malých příkladech.
2. V Cíli 2 rozděl kód do dvou souborů a ověř, že import funguje bez chyb.
3. V Cíli 3 postav mini-projekt s kružnicemi krok po kroku: nejdřív výpočtové funkce, pak hlavní skript.
4. V Cíli 4 si ujasni testovací myšlení: jak navrhnout test case a jak číst fail výpis.

> **💡 Tip:** Po každém kroku spusť kód hned v terminálu. Rychlá zpětná vazba je pro začátečníky nejrychlejší cesta.

---

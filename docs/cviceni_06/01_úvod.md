# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## ÚVOD

Ve cvičení 3 jsme se naučili, jak psát funkce a jak je používat. Teď je čas posunout se dál a naučit se, jak psát funkce,
které jsou dobře organizované a snadno použitelné. 

V tomto cvičení se naučíš:

- jak psát funkce s čistým rozhraním,
- jak rozdělit program do více souborů (modulů),
- jaká je dobrá základní struktura Python repozitáře,
- jak fungují automatické testy a proč jsou nezbytné pro větší projekty.

Praktický příklad, který budeme řešit, je určení, jestli se dvě kružnice protínají. Tento problém je dostatečně 
jednoduchý na to, abychom se mohli soustředit na organizaci kódu a práci s funkcemi, ale zároveň dostatečně komplexní, 
aby nám umožnil ukázat výhody modulárního přístupu a testování.

<p style="color:#c62828; font-size:1.25rem;"><strong>❗❗ Cvičení je nezbytné odevzdat do e-learningu.</strong></p>

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

> **Tip:** Cílem tohoto cvičení není napsat co nejvíc kódu, ale naučit se lepší organizaci kódu. Tohle využiješ v každém větším úkolu.

---

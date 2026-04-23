# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 6: UKÁZKY – AI V PRAXI

V této části si vyzkoušíš práci s AI agentem na praktických úkolech. Cílem není naučit se novou syntaxi – cílem je naučit se **efektivně komunikovat s AI** a používat ho jako nástroj pro řešení reálných úloh.

> **💡 Než začneš:** Předpokládá se, že už máš nainstalovaného agenta podle **[Cíle 5 — Instalace AI nástrojů](06_cil_5_instalace_ai.md)**. Pokud ještě ne, projdi nejdřív tu stránku — zabere ti to pár minut.

---

### 6.1 Úkol 1: Analýza textu

Vytvoř novou složku pro tento úkol a otevři ji v PyCharmu (nebo spusť agenta v terminálu v této složce).

**📝 ÚKOL: Řekni agentovi (přirozeným jazykem):**

> *Vytvoř Python skript, který:*
> *1. Načte od uživatele text z klávesnice (input).*
> *2. Spočítá počet slov, vět a unikátních slov.*
> *3. Najde 5 nejčastějších slov (bez ohledu na velikost písmen).*
> *4. Výsledky vypíše do konzole v přehledné tabulce.*
> *Otestuj ho na tomto textu: "Kočka sedí na plotě. Pes sedí pod plotem. Kočka a pes jsou kamarádi. Kočka má ráda ryby."*

**Co sleduj:**

- Jak agent kód strukturuje? Vytvořil funkce, nebo je vše v jednom bloku?
- Spustil kód sám a ukázal výstup?
- Je výstup správný? Zkontroluj počty ručně.

**Doplňující úkoly (řekni agentovi):**

- *„Přidej do výstupu i průměrnou délku slova."*
- *„Uprav skript tak, aby uměl načíst text ze souboru místo z klávesnice."*
- *„Přidej sloupcový graf 5 nejčastějších slov pomocí matplotlib."*

---

### 6.2 Úkol 2: Práce s daty

**📝 ÚKOL: Řekni agentovi:**

> *Vytvoř CSV soubor `pacienti.csv` s 20 náhodnými záznamy pacientů. Každý záznam bude mít: jméno, věk (18–90), výška v cm (150–200), váha v kg (50–120), krevní tlak systolický (90–180).*
>
> *Potom vytvoř skript, který:*
> *1. Načte tento CSV soubor.*
> *2. Vypočítá BMI pro každého pacienta.*
> *3. Rozdělí pacienty do kategorií podle BMI (podváha, normální, nadváha, obezita).*
> *4. Vykreslí histogram BMI hodnot.*
> *5. Vykreslí scatter plot: věk vs. krevní tlak.*

**Co sleduj:**

- Vytvořil agent CSV soubor i skript, nebo jen skript?
- Jsou BMI kategorie správné? (podváha < 18.5, normální 18.5–25, nadváha 25–30, obezita > 30)
- Jak vypadají grafy? Jsou čitelné, mají popisky os?

**Doplňující úkoly:**

- *„Přidej do scatter plotu barevné rozlišení podle BMI kategorie."*
- *„Ulož grafy jako PNG soubory do složky output/."*
- *„Přidej výpis průměrného BMI a krevního tlaku pro každou věkovou skupinu (18–30, 31–50, 51–70, 71+)."*

---

### 6.3 Úkol 3: Vizualizace – od nuly po hotový graf

**📝 ÚKOL: Řekni agentovi:**

> *Vytvoř vizualizaci, která ukáže vývoj denní teploty v Brně za jeden týden. Vymysli realistická data pro leden (nízké teploty) a červenec (vysoké teploty). Zobraz obě křivky v jednom grafu s legendou, popisky os a nadpisem. Leden modře, červenec červeně.*

**Pak iteruj – přidávej požadavky postupně:**

1. *„Přidej šedý pás znázorňující rozmezí 'komfortní teploty' (18–24 °C)."*
2. *„Přidej do grafu minimální a maximální teplotu jako anotace (šipky s textem)."*
3. *„Vytvoř druhý graf (subplot) pod prvním, který ukáže rozdíl teplot mezi červencem a lednem pro každý den."*

**Co sleduj:**

- Jak agent reaguje na postupné přidávání požadavků? Zachovává předchozí práci?
- Jsou grafy vizuálně kvalitní bez dalších instrukcí?

---

### 6.4 Úkol 4: Oprava chybného kódu

Tento úkol je jiný – začneš s kódem, který nefunguje, a necháš agenta najít a opravit chyby.

**📝 ÚKOL: Vytvoř soubor `buggy.py` s tímto obsahem (ručně nebo řekni agentovi, ať ho vytvoří):**

```python
def prumer(seznam):
    soucet = 0
    for cislo in seznam:
        soucet = soucet + cislo
    return soucet / len(seznam)

def median(seznam):
    serazeny = seznam.sort()
    n = len(serazeny)
    if n % 2 == 0:
        return (serazeny[n//2 - 1] + serazeny[n//2]) / 2
    else:
        return serazeny[n//2]

def statistiky(data):
    print(f"Průměr: {prumer(data)}")
    print(f"Medián: {median(data)}")
    print(f"Minimum: {min(data)}")
    print(f"Maximum: {max(data)}")
    print(f"Rozsah: {max(data) - min(data)}")

cisla = [4, 7, 2, 9, 1, 5, 8, 3, 6]
statistiky(cisla)
```

**Pak řekni agentovi:**

> *Spusť soubor buggy.py. Dostávám chybu. Najdi všechny chyby v kódu, oprav je a znovu spusť.*

**Co sleduj:**

- Najde agent hlavní bug? (Funkce `list.sort()` vrací `None`, ne seřazený seznam – správně je `sorted(seznam)` nebo `seznam.sort()` bez přiřazení.)
- Najde i vedlejší problémy? (Funkce `prumer` spadne na prázdný seznam.)
- Vysvětlí, proč chyba nastala?

---

### 6.5 Úkol 5: Commitování přes agenta

**📝 ÚKOL:**

1. Ujisti se, že máš složku inicializovanou jako git repozitář (`git init`).
2. Řekni agentovi:

> *Podívej se, jaké soubory mám v projektu. Přidej je do Gitu, commitni s rozumnou zprávou a ukaž mi historii commitů.*

**Co sleduj:**

- Agent provede `git add`, `git commit` a `git log` sám?
- Je commit zpráva rozumná a popisná?
- Požádal tě o potvrzení před spuštěním příkazů? (Měl by.)

---

### 6.6 Bonusový úkol: Hra

**📝 ÚKOL: Řekni agentovi:**

> *Vytvoř jednoduchou hru v Pythonu s grafickým oknem. Had se pohybuje po mřížce, sbírá jídlo a roste. Ovládání šipkami. Použij tkinter nebo pygame.*

Až hra funguje, zadej modifikaci:

> *Uprav hru tak, aby had začínal dlouhý (alespoň 10 článků) a při sebrání jídla se o jeden článek zkrátil. Pokud had dosáhne délky 1, hra končí výhrou.*

Cílem není naprogramovat hru – cílem je vidět, jak agent zvládá **iterativní vývoj** většího projektu a jak ho efektivně navádět.

> **💡 Tip:** Pokud hra nefunguje nebo má chyby, řekni agentovi přesně co vidíš. Neřeš to ručně – nech ho, ať to opraví sám.

> **💡 Tip — dej agentovi „oči":** Agent ve výchozím stavu nevidí, jak hra vypadá — neumí spustit GUI okno. Řekni mu, ať si **sám zprovozní způsob, jak hru vizuálně zkontrolovat**: třeba pomocný skript, který v každém kroku uloží snapshot herní mřížky do PNG (`pygame.image.save()` nebo `tkinter.PostScript`), nebo si nasadí MCP server pro screenshoty (např. [Playwright MCP](https://github.com/microsoft/playwright-mcp), který umí ovládat a fotit okna). Agent pak může sám kontrolovat, jestli se had hýbe správně, jestli zmizí po sebrání jídla atd. — bez toho, abys ty musel hru pořád pouštět a popisovat mu, co vidíš.

---

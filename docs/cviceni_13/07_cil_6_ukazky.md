# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 6: UKÁZKY – AI V PRAXI

> **⚠️ Stav: duben 2026.** Vývoj AI nástrojů jde velmi rychle — agenti se chovají jinak než před půl rokem a doporučené postupy se rychle vyvíjejí. Příklady ber jako orientační, ne jako zaručeně reprodukovatelný recept.

V této části si vyzkoušíš práci s AI agentem na praktických úkolech. Cílem není naučit se novou syntaxi – cílem je naučit se **efektivně komunikovat s AI** a používat ho jako nástroj pro řešení reálných úloh.

> **💡 Než začneš:** Předpokládá se, že už máš nainstalovaného agenta podle **[Cíle 5 — Instalace AI nástrojů](06_cil_5_instalace_ai.md)**. Pokud ještě ne, projdi nejdřív tu stránku — zabere ti to pár minut.

> **📁 Pro každý úkol si vytvoř samostatnou složku** (např. `ukol_1`, `ukol_2`, …) a otevři ji v PyCharmu nebo v ní spusť agenta v terminálu. Každý úkol má jinou strukturu souborů a v jedné společné složce by se ti projekty míchaly. Tip: hned po vytvoření udělej `git init` — pak můžeš jednoduše vrátit změny, kdyby agent něco rozbil.

---

### 6.1 Úkol 1: Analýza textu

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

### 6.2 Úkol 2: Vizualizace – od nuly po hotový graf

**📝 ÚKOL: Řekni agentovi:**

> *Vytvoř vizualizaci, která ukáže vývoj denní teploty v Brně za jeden týden. Vymysli realistická data pro leden (nízké teploty) a červenec (vysoké teploty). Zobraz obě křivky v jednom grafu s legendou, popisky os a nadpisem. Leden modře, červenec červeně.*

**Pak iteruj – přidávej požadavky postupně:**

1. *„Přidej šedý pás znázorňující rozmezí 'komfortní teploty' (18–24 °C)."*
2. *„Přidej do grafu minimální a maximální teplotu jako anotace (šipky s textem)."*
3. *„Vytvoř druhý graf (subplot) pod prvním, který ukáže rozdíl teplot mezi červencem a lednem pro každý den."*
4. *„Místo vymyšlených dat stáhni reálné historické teploty pro Brno za stejné období z veřejného API (např. open-meteo.com — archive endpoint nevyžaduje klíč) a překresli graf z reálných dat."*

**Co sleduj:**

- Jak agent reaguje na postupné přidávání požadavků? Zachovává předchozí práci?
- Jsou grafy vizuálně kvalitní bez dalších instrukcí?

---

### 6.3 Úkol 3: Oprava chybného kódu

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

### 6.4 Úkol 4: Commitování přes agenta

Tento úkol dělej **ve složce z předchozího úkolu** (Oprava chybného kódu) — máš tam opravený `buggy.py` a chceme změny dostat do Gitu.

**📝 ÚKOL:**

1. Ujisti se, že máš složku inicializovanou jako git repozitář (`git init`, pokud jsi to neudělal už na začátku).
2. Řekni agentovi:

> *Podívej se, jaké soubory mám v projektu. Přidej je do Gitu, commitni s rozumnou zprávou a ukaž mi historii commitů.*

**Co sleduj:**

- Agent provede `git add`, `git commit` a `git log` sám?
- Je commit zpráva rozumná a popisná?
- Požádal tě o potvrzení před spuštěním příkazů? (Měl by.)

---

### 6.5 Úkol 5: Klonování, řešení a push přes GitHub Classroom

Tenhle úkol je **ukázka, co všechno agent zvládne sám**: přijmout zadání z GitHub Classroom, naklonovat repozitář, vyřešit úlohu, ověřit ji automatickými testy a pushnout zpátky na GitHub. Cílem je vidět celý workflow v jednom průchodu — **ne** simulovat skutečné odevzdání úkolu.

**📝 ÚKOL:**

1. Otevři odkaz na zadání: **<https://classroom.github.com/a/oRTzDTsI>** a přijmi ho (`Accept this assignment`). Classroom ti vytvoří vlastní privátní repozitář s kostrou úlohy a sadou automatických testů.
2. Po vytvoření repozitáře si zkopíruj jeho URL (něco jako `https://github.com/<organizace>/<úloha>-<tvůj-username>`).
3. Vytvoř si pro tento úkol novou složku, otevři v ní agenta a řekni mu (do prompta vlož URL svého repozitáře):

> *Naklonuj si repozitář `<sem-vlož-URL>`, podívej se na zadání v README a strukturu projektu. Vyřeš úlohu, průběžně si ověřuj řešení spouštěním automatických testů (pytest nebo to, co je v repozitáři nastavené), a až všechny testy projdou, commitni změny s rozumnou zprávou a pushni je zpátky na GitHub.*

**Co sleduj:**

- Naklonoval si agent repozitář správně a začal číst README/zadání **dřív**, než začal kódit?
- Spouštěl si průběžně testy, nebo „naslepo" odevzdal první pokus?
- Když testy spadly, opravil chybu na základě reálného chybového výstupu?
- Je commit zpráva popisná a odpovídá změnám?

> **⚠️ Tohle je jen ukázka schopností agenta — takhle úkol odevzdat NEMŮŽEŠ.** Necháváš agenta vyřešit celé zadání bez toho, abys do něj sám zasáhl, a pak to pushneš pod svým jménem. Podle pravidel akademické integrity (viz **[Cíl 7](08_cil_7_bezpecnost_a_pravidla.md)**) je tohle špatně — za odevzdané ručíš ty a musíš mu rozumět. V rámci téhle ukázky je to OK, protože jde o cvičný úkol bez hodnocení a smyslem je vidět, co agent dokáže od konce do konce. Když budeš podobný workflow používat naostro, **musíš** kódu rozumět, být schopný ho obhájit a uvést, že jsi AI použil.

---

### 6.6 Bonusový úkol 1: Hra

**📝 ÚKOL: Řekni agentovi:**

> *Vytvoř jednoduchou hru v Pythonu s grafickým oknem. Had se pohybuje po mřížce, sbírá jídlo a roste. Ovládání šipkami. Použij tkinter nebo pygame.*

Až hra funguje, zadej modifikaci:

> *Uprav hru tak, aby had začínal dlouhý (alespoň 10 článků) a při sebrání jídla se o jeden článek zkrátil. Pokud had dosáhne délky 1, hra končí výhrou.*

Cílem není naprogramovat hru – cílem je vidět, jak agent zvládá **iterativní vývoj** většího projektu a jak ho efektivně navádět.

> **💡 Tip:** Pokud hra nefunguje nebo má chyby, řekni agentovi přesně co vidíš. Neřeš to ručně – nech ho, ať to opraví sám.

> **💡 Tip — dej agentovi „oči":** Agent ve výchozím stavu nevidí, jak hra vypadá — neumí spustit GUI okno. Řekni mu, ať si **sám zprovozní způsob, jak hru vizuálně zkontrolovat**: třeba pomocný skript, který v každém kroku uloží snapshot herní mřížky do PNG (`pygame.image.save()` nebo `tkinter.PostScript`), nebo si nasadí MCP server pro screenshoty (např. [Playwright MCP](https://github.com/microsoft/playwright-mcp), který umí ovládat a fotit okna). Agent pak může sám kontrolovat, jestli se had hýbe správně, jestli zmizí po sebrání jídla atd. — bez toho, abys ty musel hru pořád pouštět a popisovat mu, co vidíš.

---

### 6.7 Bonusový úkol 2: Prezentace přes Marp (neprogramovací)

Tenhle úkol není o kódu — necháš agenta naklonovat repozitář s podklady ke cvičení, vytáhnout z nich obsah o AI nástrojích a sepsat z něj krátkou prezentaci pomocí [Marp](https://marp.app/) (nástroj, který z Markdownu vyrobí slidy v PDF/HTML). Ukazuje, že agent zvládne i „kancelářské" úkoly: zorientovat se v cizím repozitáři, vytáhnout klíčové body a naformátovat je do prezentačního formátu.

**📝 ÚKOL: Řekni agentovi:**

> *Naklonuj mi <https://github.com/slytherins-hub/prg_exercises.git> a udělej mi prezentaci o AI nástrojích podle toho co je ve cvičení 13. Použij nástroj Marp a udělej pdf i html.*

**Co sleduj:**

- Naklonoval si agent repozitář a skutečně si přečetl podklady ze složky `docs/cviceni_13/`, nebo začal psát „od oka"?
- Odpovídají body opravdu obsahu cvičení, nebo si agent vymýšlí?
- Vejde se klíčový obsah na slide bez přetečení?
- Funguje vygenerované PDF i HTML? Pokud ne, řekni agentovi co je špatně a nech ho to opravit.

> **💡 Tip — dej agentovi „oči" i tady:** Stejně jako u hry agent nevidí, jak prezentace vypadá. Řekni mu, ať si **napíše krátký skript pro vizuální kontrolu** — třeba že každý slide z PDF vyrenderuje na PNG (`pdf2image` nebo `pdftoppm`) a pak si obrázky sám prohlédne (čte je rovnou). Díky tomu může sám zkontrolovat, jestli text netrčí přes okraj, jestli nejsou prázdné slidy, jestli se nepřekrývají bloky — bez toho, abys mu to musel popisovat ty.

> **💡 Tip — Marp nemusí být jediná volba.** Pokud tě zajímá experiment, řekni agentovi, ať použije jiný nástroj a porovnej výsledky:
> - **[Quarto](https://quarto.org/docs/presentations/)** — vědecky orientovaný, umí Markdown → HTML/PDF/PowerPoint, s podporou kódu a citací.
> - **[Reveal.js](https://revealjs.com/)** — JavaScriptový framework pro interaktivní HTML prezentace s animacemi a přechody.
> - **Čisté vlastní HTML/CSS** — žádný framework, jen HTML soubor se slidy. Nejvíc volnosti, nejvíc práce — dobré pro porovnání, jak agent zvládá design „od nuly".

---

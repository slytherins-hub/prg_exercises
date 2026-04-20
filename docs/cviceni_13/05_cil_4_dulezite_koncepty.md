# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 4: DŮLEŽITÉ KONCEPTY AI NÁSTROJŮ

Než začneš s AI agentem pracovat na reálných úkolech, je potřeba rozumět několika konceptům. Nejsou složité, ale bez nich se budeš zbytečně ztrácet.

---

### 4.1 Pracuj v jednom repozitáři pro daný úkol

AI agent (Claude Code, Copilot, Codex) pracuje s **celým projektem** – vidí všechny soubory ve složce, ve které běží. Proto je důležité mít pro každý úkol nebo projekt **vlastní složku (repozitář)**.

**Proč?**

- Agent se orientuje podle souborů kolem sebe. Pokud máš v jedné složce 15 nesouvisejících skriptů, agent nebude vědět, co k čemu patří.
- Když agent čte nebo upravuje soubory, chceš mít jistotu, že pracuje jen s tím, co k úkolu patří.

**Prakticky:**

```
# Špatně – všechno v jedné složce
D:/škola/
├── ukol1.py
├── ukol2.py
├── pokus.py
├── prezentace.pptx
├── data.csv
└── random_test.py

# Dobře – každý projekt má vlastní složku
D:/škola/
├── ukol_bmi/
│   ├── bmi.py
│   └── data.csv
├── ukol_dna/
│   ├── dna_analysis.py
│   └── sequences.txt
└── projekt_vizualizace/
    ├── main.py
    └── patients.csv
```

> **💡 Tip:** Když spustíš AI agenta, spusť ho přímo ve složce projektu. Například v terminálu: `cd D:/škola/ukol_dna && claude` nebo v PyCharmu otevři složku jako projekt.

---

### 4.2 Verzování – proč a jak

Verzování znamená ukládání historie změn v projektu. Nástroj na to je **Git** – už ho znáš z předchozích cvičení.

**Proč je to důležité při práci s AI?**

AI agent může upravit víc souborů najednou. Pokud výsledek nevyhovuje, chceš se vrátit k předchozí verzi. Bez Gitu to znamená ručně hledat, co se změnilo, a doufat, že si pamatuješ původní stav. S Gitem stačí jeden příkaz.

**Základní workflow:**

```bash
# 1. Před prací s agentem – commitni aktuální stav
git add .
git commit -m "před úpravou přes AI"

# 2. Nech agenta pracovat...

# 3. Podívej se, co agent změnil
git diff

# 4a. Pokud jsi spokojený – commitni
git add .
git commit -m "přidána analýza DNA sekvencí (AI)"

# 4b. Pokud ne – vrať změny
git checkout .
```

> **💡 Tip:** Commituj často. Před každou větší interakcí s agentem je dobrý nápad commitnout, abys měl bod, ke kterému se můžeš vrátit.

> **💡 Tip:** Git příkazy nemusíš psát sám – řekni agentovi třeba *„commitni aktuální stav s rozumnou zprávou"* a on to udělá za tebe.

---

### 4.3 Instrukční soubor projektu

Každý agent umí na začátku práce přečíst speciální soubor s instrukcemi pro daný projekt. Je to tvůj způsob, jak agentovi říct:

- jaký je to projekt a co dělá,
- jaké konvence používáš (pojmenování souborů, jazyk komentářů, ...),
- co má a nemá dělat.

**Příklad:**

```markdown
# Projekt: Analýza biomedicínských dat

- Jazyk: Python 3.10+
- Komentáře a proměnné pojmenováváme anglicky
- Pro grafy používáme matplotlib
- Data jsou ve složce data/, výstupy ve složce output/
- Testy spouštíme příkazem: pytest tests/
```

Agent tento soubor přečte automaticky a přizpůsobí svou práci. Nemusíš mu pokaždé opakovat stejné instrukce.

Každý nástroj používá jiný název souboru:

| Nástroj | Soubor |
|---------|--------|
| Claude Code | `CLAUDE.md` |
| OpenAI Codex | `AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Cursor | `.cursorrules` |

> **💡 Tip:** `AGENTS.md` (používaný Codexem) se postupně stává obecnějším standardem — některé nástroje ho umí číst vedle svého vlastního formátu. Pokud chceš jeden soubor pro více agentů, `AGENTS.md` je dobrá volba. Do ostatních souborů (např. `CLAUDE.md`) pak stačí napsat jen odkaz: *„Instrukce jsou v AGENTS.md"*.

---

### 4.4 Kontext – co agent vidí a proč na tom záleží

Když s agentem komunikuješ, všechno co napíšeš ty a co odpoví on se ukládá do **kontextu** (někdy se říká „kontextové okno"). Agent při každé odpovědi čte celý tento kontext – tvoje zprávy, jeho odpovědi, výstupy z terminálu, obsah souborů, které četl.

**Proč na tom záleží?**

- Kontext má **omezenou velikost** (závisí na modelu – typicky desítky až stovky tisíc tokenů). Když se zaplní, agent začne zapomínat starší části konverzace.
- **Příliš velký kontext může snížit efektivitu** – agent se v záplavě informací hůř orientuje a jeho odpovědi mohou být méně přesné. I když se kontext ještě nezaplnil, kratší kontext často vede k lepším výsledkům.

**Komprese kontextu:**

Agenti mají mechanismus **komprese kontextu** – když se kontext blíží limitu, agent starší části konverzace shrne do kratšího souhrnu a pokračuje dál. Některé nástroje to dělají automaticky, u jiných můžeš kompresi vyvolat ručně (např. v Claude Code příkazem `/compact`). Komprese zachová klíčové informace, ale detaily se mohou ztratit.

**Co s tím?**

- **Začni novou konverzaci** – když přecházíš na nový úkol nebo je konverzace už hodně dlouhá. Neboj se toho – agent má přístup k souborům v projektu, takže kontext předchozí práce si přečte z kódu. Nová konverzace s čistým kontextem může často výsledek **zlepšit**, protože agent se nemusí probíjet záplavou starších zpráv.
- **Nech agenta zapisovat poznámky** – pokud pracuješ na složitějším úkolu, řekni agentovi ať si průběžně zapisuje poznámky do `.md` souboru (třeba `notes.md` nebo `TODO.md`). Při další konverzaci si je přečte a nemusíš mu vše vysvětlovat znovu.
- **Instrukční soubor jako trvalá paměť** – důležité informace o projektu (konvence, struktura, pravidla) patří do instrukčního souboru (viz 1.3). Agent ho čte automaticky na začátku každé konverzace, ale nezabírá zbytečně místo v kontextu při běžné práci.

> **💡 Tip:** Pokud agent začne odpovídat nepřesně nebo „zapomíná" co jsi mu řekl před chvílí, je to často znak přeplněného kontextu. Začni novou konverzaci – často to samo o sobě problém vyřeší.

---

### 4.5 Skills (dovednosti)

Některé AI nástroje podporují **skills** – předpřipravené sady instrukcí pro specializované úlohy. Klíčové je, že agent si skill **načte do kontextu sám, jen když ho potřebuje** – instrukce tam jsou připravené, ale nezabírají místo, dokud je agent nepoužije.

**Jak to funguje:**

Skill je v podstatě textový soubor s popisem, jak má agent provést konkrétní úkol. Když agent dostane úkol, který odpovídá nějakému skillu, sám si ho najde a načte. Nemusíš mu říkat „použij skill X" – agent to pozná z kontextu.

Můžeš je ale vyvolat i ručně zkratkou:

| Příkaz | Co udělá |
|--------|---------|
| `/commit` | Podívá se na změny, napíše commit message a commitne |
| `/review` | Zrecenzuje pull request |
| `/init` | Vytvoří instrukční soubor pro aktuální projekt |

Výhoda oproti tomu, kdyby všechny instrukce byly napsané přímo v instrukčním souboru: agent si do kontextu načte **jen to, co právě potřebuje**, a zbytek mu nezabírá místo.

> **💡 Tip:** Skills jsou dostupné v Claude Code. Jiní agenti mají podobné koncepty pod jinými názvy (Copilot má „slash commands" v chatu).

---

### 4.6 MCP servery – rozšíření schopností agenta

**MCP** (Model Context Protocol) je standard, který umožňuje AI agentovi **připojit se k externím nástrojům a službám**. Představ si to jako „zásuvky", do kterých můžeš agenta zapojit.

**Bez MCP:** Agent umí pracovat se soubory a terminálem.

**S MCP:** Agent navíc umí:

- pracovat s **databází** (číst, zapisovat, dotazovat se),
- prohlížet **webové stránky**,
- pracovat s **Google Drive, Slack, GitHub Issues** a dalšími službami,
- volat **specializované API**.

**Jak to funguje?**

MCP server je malý program, který běží na pozadí a překládá mezi AI agentem a konkrétní službou. Agent řekne „chci přečíst soubor z Google Drive" a MCP server to za něj udělá.

**Příklad konfigurace (Claude Code):**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/cesta/k/datům"]
    }
  }
}
```

> **💡 Poznámka:** MCP servery jsou pokročilejší téma. Pro začátek je nepotřebuješ – agent si vystačí se soubory a terminálem. Ale je dobré vědět, že tahle možnost existuje, protože rozšiřuje to, co AI dokáže, daleko za hranice pouhého psaní kódu.

---

### 4.7 Jak s agentem efektivně pracovat

Tady je shrnutí nejdůležitějších pravidel, která platí bez ohledu na to, jaký nástroj používáš.

#### Jak se ptát

**Buď konkrétní.** Místo *„Udělej mi graf"* raději: *„Vytvoř sloupcový graf počtu výskytů každého písmene v řetězci 'AACGTTGCA'. Osa X písmena, osa Y počty. Použij matplotlib."* Čím víc kontextu dáš, tím přesnější výsledek.

**Iteruj.** AI nedá vždy perfektní výsledek napoprvé – a to je v pořádku. Zadej co chceš, podívej se na výsledek, řekni co je špatně, opakuj.

**Popisuj, co vidíš.** Neříkej jen „to je špatně". Řekni konkrétně: *„Graf se zobrazuje, ale chybí popisky os"* nebo *„Funkce vrací 0.5, ale pro vstup 'AACG' by měla vrátit 0.25"*.

**Ptej se na chyby přímo.** Dostaneš chybovou hlášku? Nemusíš ji analyzovat sám – zkopíruj ji agentovi a zeptej se co znamená.

**Nech agenta, ať se doptává.** Pokud agent potřebuje víc informací, nech ho se zeptat. Nemusíš na začátku předvídat všechno – dobrý agent se sám zeptá na to, co mu chybí.

#### Jak organizovat práci

**Pracuj po malých krocích.** Nejčastější chyba začátečníků: zadat obrovský úkol najednou. Velké generování kódu vrší chyby na sebe a výsledek je těžké opravit. Místo toho: zadej malý kus, otestuj, commitni, pokračuj dalším.

**Napřed plán, pak implementace.** Řekni agentovi: *„Napiš mi do souboru plan.md plán a TODO list toho, co bude potřeba udělat."* Zkontroluj plán, uprav ho, a pak nech agenta pracovat podle něj krok po kroku. Co je sepsané v `.md` souboru, tam zůstane a jde použít znovu — na rozdíl od kontextu konverzace, který se časem „zastarává" nebo ztratí.

**Důležité informace sepisuj do `.md` souborů.** Kontext konverzace se ztratí – když začneš novou konverzaci, agent neví nic z té předchozí. Ale soubory v projektu zůstávají. Proto: rozhodnutí, požadavky, poznámky, TODO listy nech agenta zapisovat do souborů. Při další konverzaci si je přečte sám.

**Verzuj.** Commituj před každou větší interakcí s agentem. Pokud agent udělá něco, co nechceš, můžeš se snadno vrátit.

#### Co kontrolovat

**Nech agenta spouštět kód a testy.** Největší výhoda agentů oproti chatbotům je, že kód spustí, přečtou chybu a opraví ji sami. Ještě lepší je, když agentovi řekneš ať **napíše testy** a spustí je — kvalita výstupu dramaticky roste, když má agent způsob, jak sám ověřit, že výsledek funguje.

**Důvěřuj, ale prověřuj.** K AI výstupu přistupuj jako ke kódu od juniornějšího kolegy – přečti si ho, zeptej se proč to udělal takhle, zkontroluj okrajové případy. Studie ukazují, že AI kód má výrazně víc bezpečnostních chyb než kód psaný člověkem. Pozor na **tiché chyby** – kód, který vypadá správně a běží bez chyb, ale vrací špatné výsledky.

**Čti, co agent dělá.** Zejména u terminálových příkazů – agent ti vždy ukáže, co chce spustit. Přečti si to. Rozumět nemusíš každému detailu, ale měl bys vědět, jestli instaluje balíček, maže soubory, nebo posílá data na internet.

#### Učení s AI

**AI ti pomáhá se učit — ne se učí místo tebe.** Když ti agent vygeneruje kód, přečti si ho a porozuměj mu. Pokud něčemu nerozumíš, zeptej se — agent ti to vysvětlí. Slepé přijímání AI výstupu bez porozumění (tzv. „vibe coding") ti v učení nepomůže.

**Zkus to napřed sám.** Zvlášť u úkolů, které procvičují nové koncepty — zkus nejdřív napsat řešení sám a teprve pak ho porovnej s tím, co navrhne AI. Tím si budíš dovednosti, které budeš potřebovat i bez AI.

> **⚠️ Bezpečnost:** Nikdy nedávej AI agentovi přístup k citlivým datům (hesla, API klíče, osobní údaje pacientů), pokud přesně nevíš, co s nimi udělá. Data odeslaná do AI služby opouštějí tvůj počítač.

---

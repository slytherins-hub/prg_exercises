# CVIČENÍ 13B: AI NÁSTROJE PRO PROGRAMOVÁNÍ

Algoritmizace a programování

## CÍL 1: DŮLEŽITÉ KONCEPTY

Než začneš s AI agentem pracovat na reálných úkolech, je potřeba rozumět několika konceptům. Nejsou složité, ale bez nich se budeš zbytečně ztrácet.

---

### 1.1 Pracuj v jednom repozitáři pro daný úkol

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

### 1.2 Verzování – proč a jak

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

---

### 1.3 Co je CLAUDE.md (a proč na něm záleží)

`CLAUDE.md` je speciální soubor, který AI agent (konkrétně Claude Code) přečte vždy, když začne pracovat v daném projektu. Je to tvůj způsob, jak agentovi říct:

- jaký je to projekt a co dělá,
- jaké konvence používáš (pojmenování souborů, jazyk komentářů, ...),
- co má a nemá dělat.

**Příklad jednoduchého CLAUDE.md:**

```markdown
# Projekt: Analýza biomedicínských dat

- Jazyk: Python 3.10+
- Komentáře a proměnné pojmenováváme anglicky
- Pro grafy používáme matplotlib
- Data jsou ve složce data/, výstupy ve složce output/
- Testy spouštíme příkazem: pytest tests/
```

Agent tento soubor přečte automaticky a přizpůsobí svou práci. Nemusíš mu pokaždé opakovat stejné instrukce.

> **💡 Tip:** CLAUDE.md funguje v Claude Code. Jiní agenti mají podobné mechanismy – například Cursor má `.cursorrules`, GitHub Copilot čte `.github/copilot-instructions.md`.

---

### 1.4 Skills (dovednosti)

Některé AI nástroje podporují **skills** – předpřipravené příkazy, které rozšiřují schopnosti agenta o specializované úlohy.

**Co to prakticky znamená:**

Místo abys agentovi složitě popisoval, co má udělat, použiješ zkratku:

| Příkaz | Co udělá |
|--------|---------|
| `/commit` | Podívá se na změny, napíše commit message a commitne |
| `/review` | Zrecenzuje pull request |
| `/init` | Vytvoří CLAUDE.md pro aktuální projekt |

Skills jsou jako „recepty" – agent ví přesně, jak daný úkol provést, protože má předpřipravený postup.

> **💡 Tip:** Skills jsou dostupné v Claude Code. Jiní agenti mají podobné koncepty pod jinými názvy (Copilot má „slash commands" v chatu).

---

### 1.5 MCP servery – rozšíření schopností agenta

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

### 1.6 Obecná doporučení pro práci s AI

Tady je shrnutí nejdůležitějších pravidel, která platí bez ohledu na to, jaký nástroj používáš:

**Začni jednoduše.**
Nepokoušej se hned zadat složitý úkol na 500 řádků. Začni s něčím malým – jednou funkcí, jedním grafem. Když vidíš, že to funguje, přidávej složitost postupně.

**Nech agenta spouštět kód.**
Největší výhoda agentů oproti chatbotům je, že kód spustí, přečtou chybu a opraví ji sami. Nevypínej jim tuto schopnost – je to jejich hlavní síla.

**Popisuj, co vidíš.**
Když výsledek nesedí, neříkej jen „to je špatně". Řekni konkrétně: *„Graf se zobrazuje, ale chybí popisky os"* nebo *„Funkce vrací 0.5, ale pro vstup 'AACG' by měla vrátit 0.25"*.

**Nepiš kód, když nemusíš.**
Pokud máš k dispozici agenta, nemusíš psát kód ručně. Popiš co chceš přirozeným jazykem a nech agenta pracovat. Tvá úloha je zadávat, kontrolovat a navádět – ne psát syntaxi.

**Verzuj.**
Commituj před každou větší interakcí s agentem. Pokud agent udělá něco, co nechceš, můžeš se snadno vrátit.

**Čti, co agent dělá.**
Zejména u terminálových příkazů – agent ti vždy ukáže, co chce spustit. Přečti si to. Rozumět nemusíš každému detailu, ale měl bys vědět, jestli instaluje balíček, maže soubory, nebo posílá data na internet.

> **⚠️ Bezpečnost:** Nikdy nedávej AI agentovi přístup k citlivým datům (hesla, API klíče, osobní údaje pacientů), pokud přesně nevíš, co s nimi udělá. Data odeslaná do AI služby opouštějí tvůj počítač.

---

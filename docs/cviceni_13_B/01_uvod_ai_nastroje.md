# CVIČENÍ 13B: AI NÁSTROJE PRO PROGRAMOVÁNÍ

Algoritmizace a programování

## ÚVOD – PŘEHLED AI NÁSTROJŮ

### Co se v tomto cvičení naučíš?

1. Jaké AI nástroje dnes existují a čím se liší.
2. Co je chatbot, AI IDE a AI agent – a proč na tom záleží.
3. Jak AI nástroje efektivně používat – ptát se, iterovat, kontrolovat.
4. Důležité koncepty: repozitář, verzování, skills, MCP servery.
5. Praktické ukázky práce s AI agentem.

---

### Proč se o AI nástroje zajímat?

Pokud jsi někdy kopíroval kód do ChatGPT, čekal na odpověď, kopíroval ji zpátky do editoru, spustil, dostal chybu a celý cyklus opakoval – víš, jak je to pomalé. AI nástroje pro programování tento cyklus dramaticky zkracují nebo úplně odstraňují.

Nejde jen o to psát kód rychleji. AI nástroje dnes umí:

- **vysvětlit** existující kód, který jsi nenapsal ty,
- **najít a opravit** chyby v programu,
- **navrhnout** strukturu projektu,
- **napsat testy**, dokumentaci, vizualizace,
- **spustit kód**, přečíst výstup a samy se opravit.

A to vše bez toho, abys musel přepínat mezi prohlížečem a editorem.

---

### Čtyři kategorie AI nástrojů

> **🖥️ Slide:** Celý přehled nástrojů si můžeš otevřít jako [samostatný slide](04_slide_prehled.md){target="_blank"}.

AI nástroje pro programování se dají rozdělit do čtyř hlavních kategorií. Každá má jiné silné stránky:

#### 1. Chatboti

| Nástroj | Popis |
|---------|-------|
| **Claude** | Anthropic, silné uvažování, dlouhý kontext |
| **ChatGPT** | OpenAI, nejrozšířenější, GPT-4o / o3 |
| **Gemini** | Google, napojení na Google ekosystém |
| **Grok** | xAI |
| **DeepSeek** | open-source, silný na kód |

**Jak to funguje:** Otevřeš prohlížeč, napíšeš otázku, dostaneš odpověď. Kód si zkopíruješ ručně.

**Kdy je to vhodné:** Rychlé otázky, vysvětlení konceptů, jednorázové úryvky kódu. Funguje bez instalace – stačí prohlížeč.

**Nevýhoda:** Ruční kopírování tam a zpět. Chatbot nevidí tvůj projekt, neví co máš v souborech, neumí spustit kód.

---

#### 2. Online nástroje

| Nástroj | Popis |
|---------|-------|
| **Google AI Studio** | experimentování s Gemini modely, prototypování |
| **Lovable** | generování webových aplikací z popisu |
| **Replit** | online IDE s AI asistentem |
| **Firebase Studio** | Google, prostředí pro vývoj s AI přímo v prohlížeči |

**Jak to funguje:** Vše běží v prohlížeči. Napíšeš co chceš a nástroj vytvoří celý projekt – kód, náhled, někdy i deployment.

**Kdy je to vhodné:** Rychlé prototypy, webové aplikace, experimenty bez lokální instalace.

**Nevýhoda:** Omezená kontrola nad kódem, závislost na internetovém připojení, obtížnější práce s vlastními daty a existujícími projekty.

---

#### 3. AI IDE (vývojová prostředí s AI)

| Nástroj | Popis |
|---------|-------|
| **Cursor** | fork VS Code s vestavěnou AI, velmi populární |
| **Windsurf** | podobný koncept jako Cursor |

**Jak to funguje:** Vypadá jako normální editor kódu (VS Code), ale AI je přímo součástí – navrhuje změny, edituje soubory, rozumí celému projektu.

**Kdy je to vhodné:** Každodenní programování. AI vidí všechny soubory v projektu a navrhuje změny v kontextu.

**Nevýhoda:** Vyžaduje instalaci. Placené (po zkušební době).

---

#### 4. AI agenti

| Nástroj | Cena | Vhodný pro |
|---------|------|-----------|
| **Claude Code** | ~$25/měs (Claude Pro) | komplexní vícekrokové úlohy, nejlepší uvažování |
| **GitHub Copilot** | ~$10/měs (studentská varianta zdarma, ale bez nejnovějších modelů) | denní použití v IDE, bezpečný start |
| **OpenAI Codex** | ~$25/měs (ChatGPT Plus) | rychlé skripty, integrace s ChatGPT |

**Jak to funguje:** Agent má přístup k tvému terminálu a souborům. Nejen že *mluví* o kódu – skutečně ho *píše, spouští, čte chyby a opravuje je*. Pracuje autonomně, dokud úkol nesplní nebo ho nezastavíš.

**Kdy je to vhodné:** Složitější úkoly, které vyžadují víc kroků – napsat kód, spustit ho, opravit chyby, upravit podle výsledku.

**Proč je to zásadní skok:** Rozdíl mezi chatbotem a agentem je asi tak velký jako rozdíl mezi tím, když někomu *popíšeš* cestu, a když ho *odvezeš*. Agent věci skutečně dělá.

---

### Co umí AI agent – a co chatbot ne

| | Chatbot | AI agent |
|---|---------|----------|
| Vidí tvůj projekt | Ne – musíš kopírovat | Ano – čte soubory přímo |
| Spouští kód | Ne | Ano – a čte výstup |
| Opravuje chyby | Navrhne opravu textem | Opraví, spustí znovu, ověří |
| Instaluje balíčky | Ne | Ano (`pip install ...`) |
| Pracuje s terminálem | Ne | Ano (git, spouštění skriptů, ...) |
| Edituje soubory | Ne – kopíruješ ručně | Ano – přímo zapisuje změny |

---

### Tři způsoby, jak AI agenta spustit

#### Desktopová aplikace
- Běží lokálně na tvém počítači, hezké grafické rozhraní.
- Zatím hlavně **Claude Code** (Claude Desktop).
- Nejjednodušší volba – žádný terminál, žádné nastavování.
- Ideální první krok, pokud jsi nikdy nepoužíval příkazový řádek.

#### Terminál (CLI)
- Vždy nejnovější funkce.
- Běží všude – ve VS Code terminálu, přes SSH, na serverech.
- Nejvýkonnější způsob použití.
- Příkaz `claude` spustí Claude Code přímo v terminálu.

#### Rozšíření v IDE (doporučeno)
- Claude Code, GitHub Copilot, Cursor a další – přímo ve VS Code nebo PyCharmu.
- Agent mód + chat přímo v editoru, diffy jedním klikem.
- **GitHub Copilot** navíc nabízí doplňování řádků při psaní – navrhuje kód v reálném čase, ty jen stiskneš Tab.

> **💡 Tip:** Pro tento kurz doporučujeme **GitHub Copilot v PyCharmu** (zdarma pro studenty) nebo **Claude Code** (desktopová aplikace nebo terminál). Obojí zvládneš zprovoznit za pár minut.

---

### Jak se AI ptát – základní pravidla

AI nástroje jsou silné, ale výsledek závisí na tom, **jak se ptáš**. Tady je pár zásad, které platí pro všechny kategorie:

**1. Buď konkrétní.**

Místo:
> *Udělej mi graf.*

raději:
> *Vytvoř sloupcový graf, který ukazuje počet výskytů každého písmene v řetězci "AACGTTGCA". Osa X budou písmena, osa Y počty. Použij matplotlib.*

Čím víc kontextu dáš, tím přesnější výsledek dostaneš.

**2. Iteruj.**

AI nedá vždy perfektní výsledek napoprvé – a to je v pořádku. Fungující postup:

1. Zadej, co chceš.
2. Podívej se na výsledek.
3. Řekni, co je špatně nebo co chceš jinak.
4. Opakuj, dokud to nesedí.

**3. Rozděl větší úkol na kroky.**

Místo:
> *Vytvoř kompletní webovou aplikaci pro správu pacientů.*

raději:
> *Nejdřív vytvoř funkci, která načte CSV soubor s daty pacientů a vrátí seznam slovníků. Pak přidáme vizualizaci.*

**4. Ptej se na chyby přímo.**

Pokud dostaneš chybovou hlášku, nemusíš ji analyzovat sám. Zkopíruj ji a zeptej se:
> *Dostávám tuto chybu: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. Co to znamená a jak to opravit?*

**5. Kontroluj výsledky.**

AI může udělat chybu. Vždy si přečti, co navrhuje, a ověř, že výsledek dává smysl. Zejména u agentů, kteří mohou spouštět příkazy v terminálu – vždy si přečti, co chtějí udělat, než to potvrdíš.

> **⚠️ Důležité:** AI je nástroj, ne oracle. Může se mýlit, může „halucinovat" (vymyslet si funkci, která neexistuje), může navrhnout řešení, které funguje ale není správné. Tvoje úloha je výsledek vždy zkontrolovat a pochopit.

---

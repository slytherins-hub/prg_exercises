# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 3: PŘEHLED AI NÁSTROJŮ

Druhá polovina cvičení se věnuje **AI nástrojům pro programování**. V tomhle cíli projdeme přehled toho,
co dnes existuje, jak se jednotlivé kategorie nástrojů liší a proč nás nejvíc zajímají **AI agenti**.

> **⚠️ Pozor — rychlý vývoj:** Tato část popisuje stav AI nástrojů v roce 2026. AI agenti pro programování se ve velkém objevili v průběhu roku 2025 a oblast se vyvíjí extrémně rychle — konkrétní nástroje, ceny, možnosti i doporučené postupy se mohou za půl roku výrazně změnit. Berte tyto informace jako aktuální průvodce, ne jako trvalou referenci.

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

> **🖥️ Slide:** Celý přehled nástrojů si můžeš otevřít jako [samostatný slide](08_slide_prehled.md){target="_blank"}.

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
| **Claude Code** | ~$25/měs (Claude Pro) | komplexní vícekrokové úlohy, **nejvýkonnější uvažování** |
| **GitHub Copilot** | ~$10/měs (studentská varianta zdarma, ale bez nejnovějších modelů) | denní použití v IDE, **napovídání kódu při psaní** |
| **OpenAI Codex** | ~$25/měs (ChatGPT Plus) | skripty, opravy, agentní úlohy, integrace s ChatGPT |

**Jak to funguje:** Agent má přístup k tvému terminálu a souborům. Nejen že *mluví* o kódu – skutečně ho *píše, spouští, čte chyby a opravuje je*. Pracuje autonomně, dokud úkol nesplní nebo ho nezastavíš.

**Kdy je to vhodné:** Složitější úkoly, které vyžadují víc kroků – napsat kód, spustit ho, opravit chyby, upravit podle výsledku.

**Důležité:** AI agent není model – je to program, který umí volat libovolný AI model (Claude, GPT, Gemini…), ale navíc má přístup k souborům, terminálu a dalším nástrojům. Model je „mozek", agent je celý „pracovník". Práce s různými agenty je přitom velmi podobná – nástroje se liší v detailech, ale základní princip je u všech stejný.

**Ceny:** Uvedené částky jsou měsíční předplatné s omezeným množstvím spotřebovaných tokenů (= objem textu a kódu, který AI zpracuje). Všechny nástroje nabízejí i dražší tarify s vyššími limity nebo přímou platbu za spotřebované tokeny přes API.

> **Skok z chatbota na AI agenta je zhruba tak velký, jako když jste poprvé zkusili ChatGPT.**

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

### „Vibe coding" vs. AI-assisted programování

Andrej Karpathy v roce 2025 pojmenoval přístup, kdy programátor přijímá AI výstup bez porozumění – jen „vibes", pocit že to vypadá správně. Říká se tomu **vibe coding**.

Pro rychlé prototypy nebo jednorázové skripty to může fungovat. Ale pro učení je to **škodlivé** – pokud nerozumíš tomu, co AI vytvořilo, nebudíš si schopnosti, které budeš potřebovat.

Rozdíl:

| | Vibe coding | AI-assisted programování |
|---|------------|--------------------------|
| Rozumíš kódu? | Ne – prostě to funguje | Ano – chápeš proč |
| Učíš se? | Ne | Ano – AI ti vysvětlí a ty se ptáš |
| Chyby najdeš? | Těžko | Ano – víš co hledat |
| Kdy je to OK? | Jednorázový skript, prototyp | Vždy |

> **⚠️ Pravidlo pro tento kurz:** AI používej jako nástroj, který ti **pomáhá se učit** – ne jako nástroj, který se učí **místo tebe**. Když ti agent vygeneruje kód, přečti si ho a porozuměj mu. Pokud něčemu nerozumíš, zeptej se agenta – vysvětlí ti to.

---

# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## DOPLNĚK: UŽITEČNÉ MCP SERVERY A SKILLY

> **⚠️ Stav: červen 2026.** MCP i skill ekosystém roste extrémně rychle — názvy, servery i odkazy se mění. Ber to jako rozcestník, ne jako referenci, a aktuální stav si ověř.

**MCP servery** rozšiřují agenta za hranice „soubory + terminál" — připojí ho k databázím, webu, dokumentaci, hardwaru a dalším službám (viz [Cíl 4.6](05_cil_4_dulezite_koncepty.md)). Tady je výběr nejzajímavějších pro tenhle kontext: věda, datová analýza, Python, ML, Arduino/RPi, výuka, články a závěrečné práce.

> **💡 Jak je přidat:** Konfiguraci nemusíš psát ručně — **nech to na agentovi** („najdi a nastav mi MCP server na X"). A **drž jich málo** (~3–6 aktivních) — každý žere kontext při každém dotazu.

---

### Datová analýza a Python

- **[Jupyter MCP](https://github.com/datalayer/jupyter-mcp-server)** (datalayer) — agent **živě edituje a spouští buňky** v notebooku, vidí výstupy a iteruje. Pro práci v Jupyteru ideální.
- **Pandas MCP** — operace nad DataFrame + grafy: [marlonluo2018](https://github.com/marlonluo2018/pandas-mcp-server) (nejvíc funkcí, interaktivní grafy) nebo [laurensanp](https://www.pulsemcp.com/servers/) (nejjednodušší na rychlé shrnutí CSV/Parquet).
- **[E2B](https://e2b.dev/)** — **bezpečné (sandbox) spouštění Pythonu** v cloudu; agent kód reálně spustí, aniž by sáhl na tvůj systém.
- **DuckDB MCP** — bleskové SQL agregace nad CSV/Parquet (klidně GB dat lokálně).
- **PostgreSQL / SQLite** (oficiální) — dotazy přímo nad databází, bez tahání všeho do pandas.

### Machine learning

- **[Hugging Face oficiální](https://hf.co/mcp)** — přístup k 900k+ modelům, 200k+ datasetům, paperům a Spaces.
- **HF Dataset Viewer** — prozkoumávání datasetů (splits, info, první řádky, hledání).
- **scikit-learn MCP** — trénování, predikce a evaluace modelů přes nástroje.
- **Ollama MCP** — napojení na lokálně běžící modely.

### Věda, články a závěrečné práce

- **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** — hledání a stahování z **arXiv, PubMed, bioRxiv, Semantic Scholar, Crossref, OpenAlex** a desítek dalších (nejširší pokrytí). Skvělé na rešerše.
- **[Zotero MCP](https://github.com/54yyyu/zotero-mcp)** — propojí tvoji **Zotero knihovnu**: sémantické hledání, extrakce anotací z PDF, generování citací (BibTeX…). Top pro psaní práce.
- **[Overleaf MCP](https://github.com/mjyoo2/overleafmcp)** — agent **čte a edituje tvůj LaTeX projekt na Overleafu** (přes Git integraci): rozumí struktuře sekcí, umí přepsat konkrétní část a pushnout změnu zpět. Plná CRUD varianta: [tamirsida/overleaf_mcp](https://mcpservers.org/servers/tamirsida/overleaf_mcp). *(Vyžaduje Overleaf s Git integrací = placený plán; Git token je citlivý.)*
- **[arXiv MCP](https://github.com/blazickjp/arxiv-mcp-server)** — hledání + stažení paperu jako markdown + analýza obsahu.
- **PubMed MCP** — biomedicínská literatura (pokud děláš zdravotnické téma).
- **[MarkItDown MCP](https://github.com/microsoft/markitdown)** (Microsoft) — převod PDF/Office/obrázků **do Markdownu** (sedí k radě „PDF → `.md`").

### Arduino / Raspberry Pi (hardware)

- **Arduino MCP** (FastMCP + `arduino-cli`) — agent zvládne *list boards → compile → upload → serial*, tedy **rovnou nahraje sketch** a čte sériovou linku.
- **MCP na Raspberry Pi / edge** — vystaví **GPIO/I2C senzory jako nástroje** (`read_temperature`, `toggle_relay`, `get_motion_status`); agent čte data a ovládá zařízení lokálně, bez cloudu.

### Obecně užitečné (výuka, web, soubory)

- **[Context7](https://github.com/upstash/context7)** — aktuální dokumentace knihoven (proti zastaralým trénovacím datům).
- **[Playwright / Browser MCP](https://github.com/microsoft/playwright-mcp)** — agent ovládá prohlížeč, dělá screenshoty, iteruje UI (i scraping).
- **[Filesystem](https://github.com/modelcontextprotocol/servers)** + **GitHub MCP** — práce se soubory a repem (issues, PR).
- **Fetch / Brave Search MCP** — stahování webových stránek a vyhledávání.

### Používej s rozmyslem

- **AI „humanizer"** (např. [Text2Go AI Humanizer](https://github.com/Text2Go/ai-humanizer-mcp-server), Humanizer PRO) — přepíše AI text, aby zněl „lidštěji" a obešel detektory (Turnitin, GPTZero). Legitimní třeba na marketingový text, ať nezní roboticky.
  > **⚠️ Pozor u školních a závěrečných prací:** snaha „obejít detektor" jde proti **akademické integritě** a pravidlům VUT (viz [Cíl 7](08_cil_7_bezpecnost_a_pravidla.md)). Odpovědnost za odevzdaný text neseš ty — humanizer z plagiátu nedělá poctivou práci.

---

## Užitečné skilly (dovednosti)

**Skill** = složka se souborem `SKILL.md` (plus volitelné skripty a šablony), kterou si agent **načte sám jen ve chvíli, kdy ji potřebuje** (viz [Cíl 4.5](05_cil_4_dulezite_koncepty.md)). Stejný formát funguje napříč Claude Code, Codex, Antigravity i Cursor.

> **💡 Nejlepší skill je často ten vlastní** — nech agenta, ať si ho vytvoří (rada „opakovaný úkol → vytvoř skill" v [Nejdůležitějších radách](14_nejdulezitejsi_rady.md)). Instaluje se obvykle přes `npx skills add <org>/<repo>` nebo přes plugin marketplace.

### Vybrané skilly pro tenhle kontext

- **[Anthropic document skills](https://github.com/anthropics/skills)** (`docx`, `pptx`, `xlsx`, `pdf`) — tvorba a editace Wordu, PowerPointu, Excelu a PDF. Skvělé na **reporty z dat** („udělej z téhle CSV kvartální report ve Wordu/PDF s grafy").
- **DuckDB skills** — dotazování a čtení dat (CSV/Parquet) přímo z agenta.
- **frontend-design** (Anthropic) — kvalitní vizuál a UI; hodí se na HTML reporty a stránky.
- **[Excalidraw skill](https://github.com/anthropics/skills)** — vygeneruje **diagram/schéma z přirozeného jazyka** a vyrenderuje do PNG (diagramy do práce, výuky).
- **Karpathy behavioral skill** — pravidla proti typickým chybám AI kódu (tiché domněnky, over-engineering, zbytečné zásahy).
- **Valyu / [Firecrawl](https://www.firecrawl.dev/)** — web search a **specializované datové zdroje** (PubMed, ClinicalTrials, akademické) / scraping webu s výsledky do souborů.
- **Remotion** — programatické video (animované vizualizace, výukové klipy).

### Kde skilly hledat

- **[anthropics/skills](https://github.com/anthropics/skills)** — oficiální, production-ready (nejbezpečnější zdroj).
- **[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** — 1000+ skillů napříč nástroji (Claude Code, Codex, Antigravity, Cursor…).
- **awesome-claude-skills**, **[agent-skills.cc](https://agent-skills.cc/)** — procházitelné kurátorské katalogy.

> **🔒 Bezpečnost:** používej skilly **jen z důvěryhodných zdrojů** (vlastní nebo od Anthropic) — škodlivý skill může agenta navést ke spuštění kódu mimo svůj deklarovaný účel.

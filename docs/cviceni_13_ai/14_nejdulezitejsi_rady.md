# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## NEJDŮLEŽITĚJŠÍ RADY

Stručný tahák — nejužitečnější návyky pro práci s AI agenty na jednom místě.

> **🧠 Úplně nejdůležitější je práce s kontextem** — dělej si zápisky (do souborů), často mazej kontext a místo dlouhých popisů používej skilly. Kdo umí hospodařit s kontextem, dostane z agenta výrazně víc.

> **Není to jen o programování** — prakticky na jakýkoliv úkol je agent lepší než obyčejný chatbot (vidí soubory, spouští nástroje, sám se opraví).

### Git a repozitář

- **Používej Git** — a nech s ním pracovat agenta (commituj před každou větší změnou, ať se můžeš vrátit).
- **Nech agenta psát commit messages, README a dokumentaci** — píše je rád a dobře.
- **Pro každý úkol čistá prázdná složka** — ať se agentovi nepletou nesouvisející soubory.
- **Nech agenta navrhnout strukturu repozitáře** podle sebe — většinou to udělá rozumně.
- **Nech vytvořit obsah repozitáře** (index) s odkazy na jednotlivé soubory.
- **Snaž se mít všechny informace v repozitáři** — co je jen v kontextu modelu, snadno zmizí (kontext často mažeš).
- **Statickou stránku online** zveřejníš zdarma přes **GitHub Pages**.

### Plánování a postup

- **Nech agenta, ať se tě doptá** na chybějící informace.
- **Piš v jazyce, který ovládáš** — lepší **dobrá čeština než špatná angličtina**. Nepřesné zadání = nepřesný výsledek.
- **Mluv hlasem / diktuj** místo psaní dlouhých promptů — mluvení je zhruba 3× rychlejší, takže prompty vyjdou delší a detailnější (autor používá **[OpenWhispr](https://openwhispr.com/)**).
- **Nejdřív plán, pak teprve tvorba** — nech celou věc naplánovat a plán si zkontroluj.
- **Nech navrhnout 2–3 přístupy a vyber**, než začne kódit (u rozhodnutí, kde si nejsi jistý).
- **U větší věci napiš (nebo nech napsat) specifikaci / PRD** — do souboru (`SPEC.md`, `PRD.md`) sepiš, co přesně má vzniknout: cíl, vstupy a výstupy, požadavky, okrajové případy. Agent pak pracuje podle ní a ty máš co kontrolovat.
- **Odděluj „co" od „jak"** — popiš jednoznačně pozorovatelné chování (cíl), ale způsob řešení nech na agentovi.
- **Začni nejjednodušší verzí, co funguje (MVP)**, a teprve pak přidávej — snáz se ladí i commituje.
- **Rozsáhlou věc dělej po krocích** — na každý krok podle plánu pusť čistého (nového) agenta.
- **Často to trvá dlouho** — nauč se trochu multitasking (rozdělaná práce na pozadí).
- **Pro paralelní práci na jedné věci použij `git worktrees`** — stačí říct agentovi, ať to použije.

### Modely a náklady

- **Levný/rychlý model jako výchozí, silný jen na složité** — běžné edity a dotazy zvládne levný model (~80 % práce za zlomek ceny), na náročný refaktor, architekturu a plánování přepni nejsilnější.
- **V příkazové řádce snadno přepínáš mezi agenty** — ovládání je u všech podobné, takže můžeš střídat Claude Code, Codex i Antigravity a **využít free tokeny od různých platforem** (když jeden vyčerpá limit, pokračuj druhým).

### Který agent a co si pořídit

- **Claude Code je aktuálně nejschopnější na složité věci.** Obecně v tom ale není velký rozdíl — ostatní jsou tak dva měsíce pozadu a pořadí se průběžně mění.
- **Antigravity CLI (Gemini) má velmi rychlý model** — hodně rychlé reakce (Flash), skvělé na jednoduché úkoly a rychlé iterace.
- **GitHub Copilot umí navíc doplňování kódu při psaní** (Tab) přímo v editoru.
- **Co si pořídit:** placené základní varianty stojí dost podobně — **kolem 25 $/měsíc** (na intenzivní každodenní používání ale nemusí stačit, narazíš na limity). **Pokročilejší předplatné s vyššími limity vyjde zhruba na 100 $/měsíc.**
- **CESNET (e-INFRA) dává modely zadarmo a prakticky neomezeně** — napojí se do Claude Code, ale modely jsou výrazně horší než placená špička. Postup je v [Cíli 5 — Instalace](06_cil_5_instalace_ai.md).

### Kontext a paměť

- **Často mazej kontext** — nad ~100k tokenů začíná agent „hloupnout".
- **Když si zrovna moc nerozumíte a agent nedělá, co chceš → `/clear` a začni s čistou konverzací.** Nová konverzace bez balastu obvykle pomůže víc než další dohadování.
- **`/clear` je většinou lepší než `/compact`** — komprese zachová jen klíčové informace a přenese do nové konverzace i „šum". `/compact` použij jen tehdy, když víš, že kontext nemáš dobře uložený v souborech.
- **Jakmile agent jede špatným směrem, hned ho přeruš** (Esc / Stop) a naveď znovu — nebo se vrať na checkpoint (Esc Esc / `/rewind`). Špatná úvaha jinak zůstává v kontextu a agent se jí dál drží.
- **Než kontext smažeš, nech zapsat poznámky**, ať neztratíš informace.
- **Nech agenta dělat si poznámky** — `.md` pro agenta, **HTML pro tebe** (čitatel = člověk).
- **Nech zapsat důležitá pravidla**, která má dodržovat (jaký nástroj použít, oblíbená struktura kódu) — do instrukčního souboru.
- **Chceš trvale upravit chování agenta? Nech ho pravidlo rovnou zapsat do instrukčního souboru** (`CLAUDE.md`, resp. `AGENTS.md` / `GEMINI.md` podle agenta) — příště se podle něj řídí sám, nemusíš to opakovat.
- **Používáš víc agentů (Claude Code, Codex, Antigravity)? Měj jeden hlavní `AGENTS.md`** se specifikací a pravidly a z ostatních souborů (`CLAUDE.md`…) na něj jen odkazuj — neudržuješ totéž dvakrát.
- **Když agent opakuje stejnou chybu, zapiš pravidlo do instrukčního souboru** — příště ji neudělá.

### Kontrola a ověřování

- **Dej agentovi způsob, jak si práci sám ověří** — test, build, linter nebo porovnání screenshotu s návrhem, který vrací „prošlo/neprošlo". Bez měřitelného signálu se agent zastaví, jakmile to „vypadá hotově".
- **Vyžaduj důkaz, ne tvrzení** — ať ti ukáže výstup testu, spuštěný příkaz s výsledkem nebo screenshot, ne jen „hotovo".
- **Po vygenerování nech kód zjednodušit / zrefaktorovat** — první verze bývá ukecaná.

### Zdroje a vstupy

- **Poskytni zdroje** (PDF, dataset, články), nebo nech agenta, ať si je sám stáhne.
- **Na soubory se dá jednoduše odkazovat cestou** (často i přes `@cesta/k/souboru`) — napiš agentovi cestu a on si soubor sám přečte.
- **Nech agenta vyhledat aktuální info na webu** — když jde o novinky nebo verze, na které trénovací data nestačí.
- **Nech ze zdrojů udělat souhrn** s obsahem a odkazy.
- **PDF nech přepsat do `.md`** — lépe se s ním pak pracuje.
- **Používej obrázky** — fotky nákresů, printscreeny, schémata. Často rychlejší než popisovat slovy.
- **Čistě textové formáty jsou nejlepší** (`.md` je lepší než `.docx`…).
- **Na poznámky je skvělý [Obsidian](https://obsidian.md/)** — ukládá je jako obyčejné `.md` soubory, takže se v nich AI snadno vyzná a může je celé pročíst (stačí jí ukázat složku s vaultem).

### MCP servery — rozšíření agenta

- **Pro aktuální dokumentaci knihovny přidej Context7 MCP** (do promptu napiš „use context7"), nebo dokumentaci dodej přes `@Docs` — trénovací data jsou zastaralá a agent si jinak vymýšlí neexistující API nových knihoven.
- **Neinstaluj všechny MCP servery najednou** — drž se ~3–6 serverů a pod ~40 nástroji, nepoužívané vypínej. Definice nástrojů se načítají do kontextu při každém dotazu a nad ~30–50 nástroji začne agent volit špatný nástroj.
- **Na frontend připoj Playwright MCP** — agent si sám otevře stránku, udělá screenshot a iteruje, dokud to nevypadá a nefunguje správně.

### Opakování a paralelizace

- **Opakovaný úkol → vytvoř skill** a příště ho jen vyvoláš.
- **Chceš víckrát stejnou věc → řekni, ať použije subagenty.**
- **Nech subagenty udělat třeba 10 variant** a vyber si tu, která ti vyhovuje.
- **Kód nech zkontrolovat NEZÁVISLÝM druhým agentem** (klidně jiným modelem) v čisté session, který vidí jen výsledný diff a má adversariální roli — „hledej chyby, nechval". Agent, který kód napsal, ho skoro vždy schválí.
- **Subagent ať vrací jen stručné shrnutí** (ne celý průběh), výstupy slučuj postupně po jednom a po každém sloučení pusť celou sadu testů.
- **Nech agenta psát automatické testy** — kvalita výsledku tím výrazně roste.

### Prostředí a nástroje

- **Nauč se pár příkazů svého agenta** (`/help`, přepnutí modelu, přerušení) — ušetří spoustu času.
- **Nech agenta provádět instalování, nastavování a veškerou práci v příkazové řádce** — nemusíš příkazy hledat ani psát sám. Neboj se ho nechat **instalovat nástroje a chystat prostředí** (Pythonní prostředí už nikdy nemusíš chystat ručně).
- **Znej úrovně povolování akcí agenta** — kromě potvrzování po každém kroku bývá k dispozici **auto mód** (kontrolně se ptá jiného agenta), běh v **sandboxu** (např. Docker) nebo **povolit vše**. Komplexnější věci agent dělá klidně hodiny — s dotazem na každý krok by to nešlo reálně používat.
- **VS Code je super** — univerzální napříč programovacími jazyky, což se hodí (často dává smysl přepnout na jiný jazyk).
- **Nauč se Docker** — když zavřeš agenta do bezpečného kontejneru, můžeš ho nechat bezpečně pracovat bez neustálého povolování.
- **Funguje i přes SSH na serveru** — neboj se agenta využít i pro příkazy na vzdáleném stroji, rovnou ti je vymyslí a spustí (skvělé v kombinaci s VS Code a jeho Remote-SSH).
- **Najdi si svoje oblíbené CLI nástroje a nech je agenta používat** (`gh` CLI, `arduino-cli`, PrusaSlicer CLI…).
- **Cokoliv, co má CLI variantu, je v kombinaci s agentem super** — agent nástroj rovnou ovládá. A když přímá CLI varianta není, většinou už existuje **MCP server**, přes který ho ovládneš taky.
- **Arduino → `arduino-cli`** — agent pak zvládne rovnou nahrát vytvořený kód do Arduina.
- **Na jakýkoliv drobný úkol nech vytvořit skript** (PowerShell, Bash, Python…) — přejmenovat soubory, převést formát, stáhnout data… co děláš opakovaně rukou, zvládne skript za vteřinu.
- **GUI umí agent velmi dobře** — neboj se nechat udělat malý nástroj i na „blbost".
- **Co se MUSÍ stát pokaždé** (formátování, lint, kontrola) nedávej do instrukčního souboru, ale nastav jako **hook** — instrukci agent dodrží jen asi v 80 % případů, hook se spustí vždy.
- **Python instaluj přes [uv](https://docs.astral.sh/uv/)** — je super rychlé a umí spravovat i různé verze Pythonu; stačí agentovi říct, ať ho používá, a o nic se nestaráš.
- **Neboj se jiného programovacího jazyka** — vyber podle úlohy:
    - rychle a jednoduše / zpracování dat → **Python**
    - je to pomalé → přepiš do **Rust / C++**
    - souvisí to s webem → **JavaScript / TypeScript**
    - hodně paralelních operací → **Go**

### Výstupy podle úkolu

- **Jakýkoliv dokument dnes může být místo PDF rovnou HTML** — každý ho snadno otevře v prohlížeči a dá se v něm udělat úplně cokoliv, klidně **interaktivně**: tlačítka, šoupátka, živé grafy, 3D vizualizace… Pro výsledky a reporty je proto HTML nejlepší volba (případně **Jupyter notebook**, pokud ti vyhovuje).
- **Prezentace** → **[Quarto](https://quarto.org/)** nebo **[Marp](https://marp.app/)**, popřípadě **LaTeX**.
- **PDF** → **LaTeX**. Jde rozjet i workflow Overleaf → GitHub → lokální kopie, tam upravovat agentem a nahrát zpět.
- **3D modely pro tisk** → **[CadQuery](https://github.com/CadQuery/cadquery)** / **[OpenSCAD](https://openscad.org/)** na modelování, **[Three.js](https://threejs.org/)** na zobrazení na míru v prohlížeči, **PrusaSlicer CLI** ať ti dá rovnou g-code.

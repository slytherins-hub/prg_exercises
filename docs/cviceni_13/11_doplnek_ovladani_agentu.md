# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## DOPLNĚK: OVLÁDÁNÍ AI AGENTŮ

> **⚠️ Stav: květen 2026.** Konkrétní příkazy, klávesové zkratky a názvy přepínačů se v jednotlivých nástrojích **mění velmi rychle** (v řádu týdnů). Bere to jako rychlou orientaci, **ne jako referenci**. Pro aktuální stav vždy:
>
> - spusť nástroj a zadej `/help` (nebo ekvivalent),
> - spusť ho s přepínačem `--help` v terminálu,
> - mrkni na oficiální dokumentaci.

Tato stránka srovnává čtyři dnes nejpoužívanější agentní nástroje – jak je spustit, jak je nechat běžet bez ptaní (tzv. „YOLO mód"), jak navázat na předchozí konverzaci a co jsou nejdůležitější příkazy během běžné práce.

---

=== "Claude Code"

    ### Spuštění

    Po instalaci stačí napsat v terminálu (v adresáři projektu):

    ```bash
    claude
    ```

    Otevře se interaktivní rozhraní v terminálu. Píšeš zadání jako běžnou zprávu, agent ti odpovídá a rovnou navrhuje úpravy souborů, příkazy do terminálu apod.

    ### YOLO mód (bez potvrzování)

    Standardně se Claude Code ptá na potvrzení u každé akce, která mění soubory nebo spouští příkazy. Pokud chceš, ať pracuje bez ptaní (typicky v izolovaném prostředí jako sandbox/kontejner), použij:

    ```bash
    claude --dangerously-skip-permissions
    ```

    > **⚠️ Pozor:** YOLO mód agentovi povoluje **mazat soubory, instalovat balíčky, spouštět libovolné příkazy** bez tvého potvrzení. Používej **jen v sandboxu, kontejneru nebo na jednorázovém repozitáři**, ne v projektu, na kterém ti záleží.

    ### Návrat do předchozí konverzace

    ```bash
    claude --continue        # pokračuje v poslední konverzaci v aktuální složce
    claude -c                # zkratka pro --continue
    claude --resume          # ukáže seznam předchozích konverzací – vybereš
    ```

    ### Nejdůležitější příkazy

    | Příkaz | Co dělá |
    |--------|---------|
    | `/clear` | Vymaže kontext a začne novou konverzaci (preferuj před `/compact`) |
    | `/compact` | Zkomprimuje aktuální kontext, pokračuje dál |
    | `/init` | Vytvoří `CLAUDE.md` (instrukční soubor projektu) |
    | `/model` | Přepne použitý model (Opus / Sonnet / Haiku) |
    | `/cost` | Ukáže útratu v aktuální session |
    | `/help` | Nápověda – seznam všech příkazů |
    | `Esc` | Přeruší aktuální generování odpovědi |
    | `Esc Esc` | Skok zpět – uprav předchozí zprávu a pokračuj odtamtud |
    | `Shift + Tab` | Cyklicky přepíná režimy: normální → auto-accept → plan mode |

=== "Gemini CLI"

    ### Spuštění

    Po instalaci a přihlášení Google účtem:

    ```bash
    gemini
    ```

    Spustí interaktivní rozhraní. Stejně jako Claude Code dokáže číst a upravovat soubory, spouštět příkazy, atd.

    ### YOLO mód (bez potvrzování)

    ```bash
    gemini --yolo
    gemini -y                # zkratka
    ```

    > **⚠️ Pozor:** Stejně jako u Claude Code – používej **jen v sandboxu**.

    ### Návrat do předchozí konverzace

    Od verze **0.20.0** se konverzace ukládají **automaticky** – nemusíš nic ručně savovat. Sessions jsou per-projekt (`~/.gemini/tmp/<project_hash>/chats/`).

    ```bash
    gemini --resume               # rovnou obnoví poslední session
    gemini --resume 5             # konkrétní session podle indexu
    gemini --resume <UUID>        # konkrétní session podle ID
    ```

    Uvnitř běžícího CLI navíc funguje:

    ```
    /resume                       # interaktivní browser sessionů (chronologicky, s vyhledáváním)
    ```

    > **💡 Tip:** Pokud chceš naopak session **nezachovat** (jednorázový dotaz, citlivá data), spusť ji a před koncem použij přepínač `--delete`.

    > **ℹ️ Starší verze:** Před v0.20.0 bylo nutné konverzace pojmenovat ručně přes `/chat save <jmeno>` a obnovit přes `/chat resume <jmeno>`. To pořád funguje, ale není už potřeba.

    ### Nejdůležitější příkazy

    | Příkaz | Co dělá |
    |--------|---------|
    | `/clear` | Vymaže kontext a začne novou konverzaci |
    | `/compress` | Zkomprimuje kontext (Gemini ekvivalent /compact) |
    | `/chat save <jmeno>` | Uloží aktuální konverzaci pod jménem |
    | `/chat resume <jmeno>` | Obnoví uloženou konverzaci |
    | `/memory add <text>` | Přidá informaci do trvalé paměti (`GEMINI.md`) |
    | `/tools` | Vypíše, jaké nástroje má agent k dispozici |
    | `/mcp` | Spravuje připojené MCP servery |
    | `/help` | Nápověda |
    | `/quit` nebo `/exit` | Ukončí session |

=== "Codex (OpenAI)"

    ### Spuštění

    Po instalaci (`npm install -g @openai/codex`) a přihlášení:

    ```bash
    codex
    ```

    Spustí interaktivní rozhraní v terminálu, podobně jako Claude Code.

    ### YOLO mód (bez potvrzování)

    Codex má několik úrovní:

    ```bash
    codex --full-auto                                # auto-schvaluje běžné akce
    codex --dangerously-bypass-approvals-and-sandbox # úplný YOLO – vše bez ptaní
    ```

    Pro neinteraktivní spuštění (např. ze skriptu nebo CI):

    ```bash
    codex exec "tvoje zadání"
    ```

    > **⚠️ Pozor:** `--dangerously-bypass-approvals-and-sandbox` vypíná i sandbox – agent může cokoli na tvém systému. Sandbox.

    ### Návrat do předchozí konverzace

    ```bash
    codex resume             # ukáže seznam, vybereš
    codex resume --last      # rovnou pokračuje v poslední
    ```

    ### Nejdůležitější příkazy

    | Příkaz | Co dělá |
    |--------|---------|
    | `/new` | Nová konverzace (ekvivalent /clear) |
    | `/model` | Přepne model |
    | `/diff` | Ukáže rozdíly v souborech, které agent změnil |
    | `/approvals` | Změní úroveň schvalování (read-only / auto / full) |
    | `/help` | Nápověda |
    | `/quit` | Ukončí session |
    | `Esc Esc` | Skok zpět – uprav předchozí zprávu |

=== "GitHub Copilot CLI"

    ### Spuštění

    Po instalaci (`npm install -g @github/copilot`) a přihlášení GitHub účtem stačí v terminálu napsat:

    ```bash
    copilot
    ```

    Otevře se interaktivní rozhraní – stejně jako u Claude Code nebo Codexu. Agent vidí soubory v aktuální složce, navrhuje úpravy, spouští příkazy.

    ### YOLO mód (bez potvrzování)

    Standardně se ptá na potvrzení u akcí, které mění soubory nebo spouští příkazy. Pro auto-schvalování:

    ```bash
    copilot --allow-all-tools          # auto-schvaluje volání nástrojů
    copilot --allow-all-paths          # auto-schvaluje přístup ke všem cestám
    ```

    Případně oba přepínače naráz pro plný YOLO. Stejné riziko jako u ostatních – **používej jen v sandboxu**.

    ### Návrat do předchozí konverzace

    ```bash
    copilot --resume         # ukáže seznam, vybereš
    copilot --continue       # pokračuje v poslední konverzaci
    ```

    ### Nejdůležitější příkazy

    | Příkaz | Co dělá |
    |--------|---------|
    | `/clear` | Vymaže kontext a začne novou konverzaci |
    | `/model` | Přepne použitý model |
    | `/mcp` | Spravuje připojené MCP servery |
    | `/help` | Nápověda – seznam příkazů |
    | `/exit` nebo `/quit` | Ukončí session |

    > **💡 Alternativa pro rychlé dotazy:** Pokud chceš jen rychle vygenerovat / vysvětlit shell příkaz (ne celý agent flow), je tu rozšíření pro GitHub CLI:
    >
    > ```bash
    > gh copilot suggest "smaž všechny .pyc soubory rekurzivně"
    > gh copilot explain "git rebase -i HEAD~3"
    > ```
    >
    > Na rozdíl od `copilot` to není agent – je to jednorázový dotaz a odpověď.

---

## Posílání obrázků a screenshotů agentovi

Agenti **rozumí obrázkům** – screenshot chyby z UI, vykresleného grafu, návrhu, schémata na tabuli, fotku zápisku. Často je to **rychlejší cesta** než popisovat slovy, co vidíš ("graf je rozbitý" → screenshot grafu agentovi víc poví).

### Tři způsoby, jak agentovi obrázek dát

| Způsob | Funguje vždy? | Jak |
|--------|---------------|-----|
| **Cesta k souboru v promptu** | ✅ Ano, na všech nástrojích a OS | Ulož screenshot do souboru a v promptu napiš cestu (`Tady je chyba: ./error.png`). Nejspolehlivější. |
| **Drag & drop souboru do terminálu** | ✅ Ano, na všech nástrojích | Vyfoť, ulož, přetáhni soubor z Finder/Exploreru do okna terminálu. Vloží se cesta. |
| **Vložení z clipboardu (`Ctrl+V`)** | ⚠️ Jen někde | Funguje konzistentně **jen na macOS**. Na Windows obvykle nefunguje (bitmapa se ztratí), na Linuxu závisí na terminálu. |

### Konkrétně podle nástroje

| Nástroj | Cesta v promptu | Drag & drop | Clipboard paste |
|---------|-----------------|-------------|-----------------|
| **Claude Code** | ✅ `Analyze /path/img.png` | ✅ | macOS: `Ctrl+V` (ne Cmd+V!), Windows: ne |
| **Gemini CLI** | ✅ `@./img.png` (nebo `@./slozka/`) | ✅ | ❌ zatím ne |
| **Codex CLI** | ✅ `-i img.png` (CLI flag) nebo cesta v promptu | ✅ | macOS: `Ctrl+V`, Windows: ne |
| **GitHub Copilot CLI** | ✅ `@./img.png` | ✅ | ❌ zatím ne |

> **💡 Praktický workflow na Windows** (kde clipboard paste obvykle nejde):
>
> 1. `Win + Shift + S` – výřez obrazovky do clipboardu.
> 2. Otevři **Vystřižky** (Snipping Tool) nebo **Malování**, `Ctrl+V`, `Ctrl+S` jako PNG do složky projektu (např. `screenshots/error.png`).
> 3. V agentovi napiš: *„Tady je chyba: `./screenshots/error.png` – vysvětli mi co znamená a oprav to."*
>
> Po několika takových úkonech to máš v ruce a jde to rychle.

### K čemu se to typicky hodí

- **Chyba v běžícím UI / hra / okně** – screenshot „rozbitého stavu" víc řekne než popis.
- **Vykreslený graf** – agent vidí osy, popisky, anomálie a může poradit, co opravit.
- **Návrh / wireframe** – „udělej HTML stránku, co vypadá jako tenhle obrázek".
- **Foto rukopisu / tabule** – diagram třídy, vzorec, schéma. Agent ho přečte a vytvoří podle něj kód.
- **Dej agentovi „oči" sám** – pokud děláš UI/grafický výstup (jako Bonusový úkol 1 ve [Cíli 6](07_cil_6_ukazky.md)), nech agenta, aby si **sám ukládal screenshoty výstupu** (např. `pygame.image.save()`, headless render přes Playwright MCP) a kontroloval si svou práci. Tím se z „popíšeš mu výstup" stává „agent se podívá sám".

> **⚠️ Velikost a privacy:** Obrázek se odešle poskytovateli stejně jako text. Větší obrázky (>5 MB) Codex/Claude Code někdy odmítnou – zmenši rozlišení nebo komprimuj. **Citlivá data na obrázku** (jména, hesla, obličeje) ošetři **před odesláním** – clearly visible údaje jsou stejně problematické jako kdybys je napsal do textu.

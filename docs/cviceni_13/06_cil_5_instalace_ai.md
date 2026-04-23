# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 5: INSTALACE AI NÁSTROJŮ

> **⚠️ Stav: duben 2026.** Vývoj AI nástrojů jde velmi rychle — instalační příkazy, ceny, free tiery i názvy modelů se můžou rychle měnit. Pro aktuální stav vždy zkontroluj oficiální dokumentaci (odkazy v každé záložce).

V minulých cílech jsi se dozvěděl, **co** AI agenti umí a **jaké koncepty** jsou kolem nich důležité. Teď si jednoho nainstaluješ, abys ho mohl v dalším cíli použít na praktické úkoly.

> **⭐ Než začneš — povinný odkaz:** VUT má vlastní rozcestník **[vut.cz/ai](https://www.vut.cz/ai)**, který je pro studenty VUT **nejlepší jednotný zdroj** k AI nástrojům. Najdeš tam aktuální přehled licencí, postupy přihlášení, **i přístup do e-INFRA / MetaCentra** (viz záložka „Claude Code + e-INFRA" níže). Než budeš cokoli platit nebo instalovat, projdi si nejdřív tuhle stránku — ušetří ti čas i peníze.

> **⚠️ Pozor:** Hlavní volby — **Claude Code**, **GitHub Copilot**, **OpenAI Codex** a **Gemini CLI** — jsou dnes srovnatelně kvalitní a v zásadě dělají totéž. Nemá smysl vybírat „ten nejlepší" — vyber **ten, ke kterému máš nejjednodušší přístup** (předplatné, studentské benefity, školní zdroje, free tier).

> **🎓 Co se použije přímo na cvičení:** **Gemini CLI** — defaultně dává **1 000 požadavků/den zdarma** s libovolným osobním Google účtem, model Gemini 3.1 Pro s 1M kontextem. Pro výuku ideální: nikdo nepotřebuje předplatné ani MetaCentrum, instalace zabere minutu. Postup je v [záložce „Gemini CLI"](#instalace-vyber-si-jednu-z-peti-zalozek) v sekci 5.3.

---

### 5.1 Tři způsoby, jak agenta spustit

Ať už zvolíš kteréhokoliv z nich, můžeš ho použít **třemi způsoby**. Liší se jen rozhraním — „mozek" (model) a chování agenta jsou stejné.

| Způsob | Rozhraní | Kdy se hodí |
|--------|----------|-------------|
| **Desktopová aplikace** | Vlastní okno mimo editor | První pokusy bez terminálu, rychlé otázky |
| **Plugin v IDE** (PyCharm / VS Code) | Postranní panel přímo v editoru, navíc *našeptávání kódu při psaní* | Každodenní programování |
| **Terminál (CLI)** | Příkaz `claude` / `codex` / `copilot` v terminálu | Univerzální použití, servery, SSH, Linux, vždy nejnovější funkce |

> **💡 Tip:** Pokud máš platné předplatné Claude Pro nebo ChatGPT Plus, máš v něm **automaticky** zahrnutý i přístup k odpovídajícímu agentovi (Claude Code / Codex) — bez příplatku, jen s limitem požadavků za 5 hodin.

---

### 5.2 Plugin v IDE — doporučená první volba

Plugin v PyCharmu nebo VS Code je **nejpříjemnější varianta pro běžné programování**:

- hezké grafické rozhraní s chatem přímo vedle kódu,
- diffy zobrazené ve formátu, na který jsi v editoru zvyklý,
- jedním klikem přijmeš nebo zamítneš změnu,
- a navíc **našeptávání kódu při psaní** (Tab dokončí návrh) — to umí hlavně **GitHub Copilot** a **JetBrains AI Assistant / Junie**.

#### GitHub Copilot v PyCharmu (a VS Code)

1. V PyCharmu otevři `File → Settings → Plugins` (na macOS `PyCharm → Settings`).
2. V tabu **Marketplace** vyhledej **GitHub Copilot** a klikni **Install**.
3. Restartuj IDE.
4. V menu `Tools → GitHub Copilot → Login to GitHub` se přihlaš (otevře se prohlížeč s device code).
5. Otevři postranní panel **Copilot Chat** a v něm přepni na **Agent** mód.

> **💡 Tip:** Copilot je zdarma pro studenty (viz 5.3) a od března 2026 je **agent mode dostupný i v JetBrains IDE** v plné verzi (GA), ne jen v VS Code. Ve VS Code se Copilot nainstaluje stejně přes `Extensions → GitHub Copilot`.

> **📚 Víc info:** [Copilot v JetBrains — plugin marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer) · [Copilot ve VS Code](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) · [oficiální setup návod](https://docs.github.com/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment)

#### JetBrains AI Assistant + Junie

PyCharm má i vlastní AI plugin **JetBrains AI Assistant** (chat + našeptávání) a **Junie** (autonomní agent). Aktivuje se z postranního panelu **AI Assistant** přihlášením přes JetBrains účet — noví uživatelé dostanou **30denní AI Pro trial**, po něm zůstane omezený **AI Free tier**.

> **📚 Víc info:** [AI Assistant — plugin marketplace](https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant) · [Junie — plugin marketplace](https://plugins.jetbrains.com/plugin/26104-junie-the-ai-coding-agent-by-jetbrains) · [AI Assistant install guide](https://www.jetbrains.com/help/ai-assistant/installation-guide-ai-assistant.html) · [Junie install guide](https://www.jetbrains.com/help/junie/install-junie.html) · [JetBrains AI plány a ceny](https://www.jetbrains.com/ai-ides/buy/)

#### Claude Code / Codex v IDE

Oba mají vlastní plugin (`Claude Code` v JetBrains Marketplace, `OpenAI Codex` v JetBrains AI chatu od PyCharm 2026.1, oba i ve VS Code Marketplace). Najdou se přes stejné okno `Plugins` jako Copilot.

> **📚 Víc info:** [Claude Code ve VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) · [Claude Code dokumentace](https://code.claude.com/docs/en/setup) · [Codex VS Code extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt) · [Codex v JetBrains — blog post](https://blog.jetbrains.com/ai/2026/01/codex-in-jetbrains-ides/) · [Codex IDE dokumentace](https://developers.openai.com/codex/ide)

---

### 5.3 Univerzální volba — terminál (CLI) ⭐ tohle si dnes vyzkoušíme

> **🎯 Tohle je varianta, kterou si v tomhle cvičení nainstaluješ a pak v Cíli 6 použiješ na praktické úkoly.** Plugin v IDE výše má hezčí UI, ale CLI je univerzálnější — funkce přicházejí dřív, běží to všude (i přes SSH) a postup instalace platí napříč nástroji. Zkušenost s CLI ti pak velmi snadno přenese na plugin, opačně to ale neplatí.

Terminál vypadá strohá oproti pluginu, ale má dvě velké výhody:

- **Funguje všude** — Linux, macOS, Windows, vzdálený SSH server, WSL, terminál uvnitř PyCharmu.
- **Nové funkce přicházejí jako první do CLI** a teprve s odstupem do pluginů.

#### Rozhodovací pravidlo: kterého agenta nainstalovat?

Než budeš cokoli instalovat, projdi tenhle krátký rozhodovací strom:

```
Máš platné předplatné některého z agentů?
│
├── ANO, Claude Pro / Max               →  Claude Code (záložka „Claude Code")
│
├── ANO, ChatGPT Plus / Pro             →  OpenAI Codex (záložka „Codex")
│
├── ANO, GitHub Copilot Pro / Pro+      →  GitHub Copilot CLI (záložka „Copilot")
│
├── ANO, Google AI Pro / Ultra          →  Gemini CLI (záložka „Gemini CLI")
│
└── NE
    │
    ├── Máš jen Google účet (gmail / školní Workspace)?  ⭐ DOPORUČENO
    │       →  Gemini CLI free (záložka „Gemini CLI")
    │          (1000 req/den zdarma, Gemini 3.1 Pro s 1M kontextem,
    │           žádné kreditky, žádná verifikace — ideální start)
    │
    ├── Máš účet v české akademické federaci eduID/CESNET (např. VUT)?
    │       →  Claude Code napojený na e-INFRA (záložka „Claude Code + e-INFRA")
    │          (k dispozici jen open-source modely typu Qwen, GPT-OSS, DeepSeek
    │           — slabší než placené Claude Sonnet / GPT-5)
    │
    └── Jsi student a máš ověřený GitHub Education Pack?
            →  GitHub Copilot Student / Free (záložka „Copilot")
               (bez nejnovějších premium modelů — Claude Opus/Sonnet, GPT-5.4 ti nejsou
                dostupné, dostáváš jen starší/menší modely přes Auto mode)
```

> **💡 Tip:** Pokud máš víc možností (např. studentský Copilot + předplatné Claude), klidně si nainstaluj víc agentů vedle sebe. Nepřekáží si — každý si řídí vlastní login a vlastní složku v `~/`.

#### Instalace — vyber si jednu z pěti záložek

=== "Gemini CLI ⭐ demo"

    > **📚 Víc info:** [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) · [release notes](https://geminicli.com/docs/changelogs/) · [oficiální setup návod](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) · [Google blog — Introducing Gemini CLI](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/)

    **Předplatné:** **žádné** — stačí libovolný osobní Google účet (gmail i školní Workspace). Free tier dává **60 požadavků/min** a **1 000 požadavků/den** s modelem Gemini 3.1 Pro (1M kontext). Pro vyšší limity Google AI Pro / Ultra, případně Vertex AI s placeným Google Cloud projektem.

    **Tohle je nástroj, který si ukážeme přímo na cvičení** — má nejméně překážek pro start a free tier vystačí na celý semestr běžného použití.

    **Instalace (Windows, PowerShell — vyžaduje Node.js 20+):**

    ```powershell
    npm install -g @google/gemini-cli
    ```

    **Instalace (macOS, Linux, WSL):**

    ```bash
    npm install -g @google/gemini-cli
    # nebo bez globální instalace:
    npx @google/gemini-cli
    # nebo přes Homebrew (macOS, Linux):
    brew install gemini-cli
    ```

    Pokud Node.js nemáš, nainstaluj ho přes [nodejs.org/download](https://nodejs.org/en/download) nebo `winget install OpenJS.NodeJS.LTS` / `brew install node`.

    **Spuštění a přihlášení:**

    ```bash
    gemini          # spustí agenta v aktuální složce
    ```

    Při prvním spuštění vyber **„Sign in with Google"** — otevře se prohlížeč s OAuth flow, přihlas se a vrať se do terminálu. Hotovo.

    > **💡 Tip:** Pokud chceš agentovi v projektu sdělit konvence (jazyk komentářů, struktura, …), vytvoř v kořeni projektu soubor `GEMINI.md` — funguje stejně jako `CLAUDE.md` u Claude Code (viz cíl 4.3).

=== "Claude Code"

    > **📚 Víc info:** [oficiální setup ­— code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) · [quickstart](https://code.claude.com/docs/en/quickstart) · [Anthropic — Claude Code](https://www.anthropic.com/claude-code) · [troubleshooting](https://code.claude.com/docs/en/troubleshooting)

    **Předplatné:** Claude Pro / Max (pokud chceš zdarma přes e-INFRA, použij vedlejší záložku „Claude Code + e-INFRA").

    **Instalace (Windows, PowerShell):**

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    **Instalace (macOS, Linux, WSL):**

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Alternativy:** `winget install Anthropic.ClaudeCode`, `brew install --cask claude-code`, nebo `npm install -g @anthropic-ai/claude-code` (vyžaduje Node.js 18+).

    **Spuštění a přihlášení:**

    ```bash
    claude          # spustí agenta v aktuální složce; první spuštění otevře prohlížeč pro login
    ```

    Verzi ověříš `claude --version`, kompletní diagnostiku `claude doctor`. Native instalace se sama udržuje aktuální na pozadí.

    > **💡 Tip:** Native Windows instalace vyžaduje [Git for Windows](https://git-scm.com/downloads/win). Pokud běháš v WSL, není potřeba.

=== "Claude Code + e-INFRA"

    > **📚 Víc info:** [docs.cerit.io — LLM Integration (e-INFRA)](https://docs.cerit.io/en/docs/ai-as-a-service/llm-integration) · [e-INFRA AI Chat](https://chat.ai.e-infra.cz) · [docs.cerit.io — Chat AI / API](https://docs.cerit.io/en/docs/ai-as-a-service/chat-ai) · [MetaCentrum účty](https://metavo.metacentrum.cz/) · [Claude Code setup](https://code.claude.com/docs/en/setup)

    **Předplatné:** žádné — pro studenty českých VŠ s eduID/CESNET účtem zdarma. Cesnet (skrz [e-INFRA AI Chat](https://chat.ai.e-infra.cz)) provozuje OpenAI-kompatibilní endpoint, který umí Claude Code využít místo placeného Anthropic API.

    **Postup:**

    1. Přihlas se na [chat.ai.e-infra.cz](https://chat.ai.e-infra.cz) **svým školním účtem**:

        - **MUNI**: stačí univerzitní login — MUNI má vlastní integraci, **MetaCentrum účet pro to nepotřebuješ**.
        - **VUT a ostatní VŠ v eduID/CESNET federaci**: potřebuješ **účet v [MetaCentru](https://metavo.metacentrum.cz/)**. Pokud ho ještě nemáš, registruj se na [metavo.metacentrum.cz](https://metavo.metacentrum.cz/) — je to zdarma pro studenty a zaměstnance českých VŠ a verifikace probíhá přes eduID/CESNET.

    2. Na [chat.ai.e-infra.cz](https://chat.ai.e-infra.cz) si vygeneruj **API klíč** ve formátu `sk-...` — najdeš ho v **Settings → Account → API Keys** (klikni na své jméno vpravo nahoře → *Settings*).
    3. Nainstaluj Claude Code (jeden příkaz podle tvého OS):

        ```powershell
        # Windows (PowerShell)
        irm https://claude.ai/install.ps1 | iex
        ```

        ```bash
        # macOS, Linux, WSL
        curl -fsSL https://claude.ai/install.sh | bash
        ```

    4. **Spusť poprvé `claude`, abys vytvořil konfigurační soubor `~/.claude.json`.** Při prvním spuštění tě Claude Code provede onboardingem (chce přihlášení přes anthropic.com), ale ty chceš jet přes e-INFRA, ne přes Anthropic — onboarding tedy přerušíš:

        ```bash
        claude
        ```

        Otevře se interaktivní úvodní průvodce v terminálu. **Postupně třikrát stiskni `Ctrl+C`**: poprvé přeruší aktuální dialog, podruhé další vrstvu, potřetí ukončí celý průvodce a vrátíš se do shellu. (V Claude Code je úvodní wizard ve 3 vnořených vrstvách, proto tři stisky.)

        Tím se vytvoří soubor `~/.claude.json`. Otevři ho v editoru a **dovnitř JSON objektu** doplň klíč:

        ```json
        "hasCompletedOnboarding": true
        ```

        > **⚠️ Pozor — nezapomeň na čárku!** JSON je striktní formát: pokud tenhle řádek vkládáš mezi existující klíče, musí mít čárku **na předchozím i tomto řádku** (kromě posledního klíče v objektu, ten čárku nemá).

        Bez `hasCompletedOnboarding: true` by se ti při každém spuštění znovu otevíral onboarding wizard.

    5. **Vytvoř konfigurační soubor `~/.claude/settings.json`** — přepne Claude Code z Anthropic API na e-INFRA natrvalo, takže nemusíš nastavovat env proměnné při každém spuštění.

        > **⚠️ Složku `~/.claude/` ani soubor `settings.json` Claude Code automaticky nevytvoří** — vytvoř je sám (jakýmkoliv způsobem: terminál, file manager, editor s funkcí „nový soubor"). Na Windows je cesta `C:\Users\<jméno>\.claude\settings.json`.

        Do souboru vlož tento obsah:

        ```json
        {
          "env": {
            "ANTHROPIC_BASE_URL": "https://llm.ai.e-infra.cz/",
            "ANTHROPIC_AUTH_TOKEN": "sk-...",
            "ANTHROPIC_DEFAULT_OPUS_MODEL": "thinker",
            "ANTHROPIC_DEFAULT_SONNET_MODEL": "agentic",
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": "mini",
            "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
          }
        }
        ```

        Toto je celý obsah nového souboru — žádné čárky navíc neřešíš.

    6. Spusť `claude` znovu, **už v projektové složce**. Tentokrát se nepřihlašuje k Anthropic API, místo toho použije e-INFRA endpoint a tvůj `sk-...` klíč. Můžeš začít pracovat.

    **Dostupné modely na e-INFRA:**

    | Alias | Vhodný pro |
    |-------|------------|
    | `agentic` (default) | Běžná agentní práce — psaní kódu, edity souborů |
    | `thinker` | Náročnější uvažování, návrhy architektury |
    | `mini` | Drobné rychlé úkoly |
    | `qwen3-coder-next`, `qwen3-coder` | Specializované coding modely |
    | `gpt-oss-120b`, `deepseek-r1` | Otevřené alternativy |

    > **🔒 Bezpečné pro univerzitní data:** e-INFRA běží v infrastruktuře CESNET / českých akademických institucí. Provozovatel deklaruje, že **data neopouštějí prostředí e-INFRA** (žádné odesílání ke komerčním poskytovatelům typu Anthropic / OpenAI / Google). Pro běžnou univerzitní práci — výukové materiály, studentské projekty, neveřejný interní VUT/MUNI obsah — je proto **vhodnější volba než komerční cloudoví agenti**.

    > **⚠️ Co i tak nikdy neposílej:** Pravidla z cíle 7 platí dál — hesla, API klíče, osobní údaje pacientů, citlivá data podléhající GDPR či smluvním závazkům **nepatří do žádné AI služby, ani do té univerzitní**. Bezpečné prostředí ≠ povolení posílat cokoliv.

    > **💡 Tip:** Plnou aktuální dokumentaci k integracím (VS Code, JetBrains, Jupyter) najdeš na [docs.cerit.io](https://docs.cerit.io/en/docs/ai-as-a-service/llm-integration). Širší přehled modelů (Claude, GPT, Gemini, open-source na e-INFRA) je v [Doplňku — aktuální AI modely](10_doplnek_modely.md).

    > **🔄 Stejný princip pro Codex:** **OpenAI Codex** lze obdobně napárovat na e-INFRA — stačí mu nastavit `OPENAI_BASE_URL=https://llm.ai.e-infra.cz` a `OPENAI_API_KEY=sk-...` (stejný klíč jako pro Claude Code). Spouští se pak třeba `codex --model qwen3-coder-next --full-auto`. Postup je popsaný v [oficiální dokumentaci e-INFRA k integraci LLM](https://docs.cerit.io/en/docs/ai-as-a-service/llm-integration). Princip je univerzální — kterýkoli agent s podporou OpenAI-kompatibilního endpointu se dá přepnout na e-INFRA jen přes proměnné prostředí.

=== "OpenAI Codex"

    > **📚 Víc info:** [github.com/openai/codex](https://github.com/openai/codex) · [oficiální dokumentace developers.openai.com/codex](https://developers.openai.com/codex) · [config reference](https://developers.openai.com/codex/config-reference) · [IDE integrace](https://developers.openai.com/codex/ide)

    **Předplatné:** ChatGPT Plus / Pro / Business / Edu / Enterprise (model `gpt-5.3-codex`).

    **Instalace (Windows, PowerShell):**

    ```powershell
    winget install --id OpenAI.Codex
    ```

    **Instalace (macOS, Linux, WSL):**

    ```bash
    brew install --cask codex
    # nebo
    npm install -g @openai/codex
    ```

    **Spuštění a přihlášení:**

    ```bash
    codex           # spustí agenta; v menu vyber „Sign in with ChatGPT"
    ```

    > **⚠️ Pozor:** Native Windows podpora je u Codexu zatím **experimentální** — sandbox není tak izolovaný jako na Linuxu/macOS. Pro vážnější použití OpenAI doporučuje **WSL2**. Pokud nemáš WSL, ber to jako varovný signál a neudílej agentovi přístup k citlivým souborům.

=== "GitHub Copilot CLI"

    > **📚 Víc info:** [github.com/github/copilot-cli](https://github.com/github/copilot-cli) · [oficiální setup návod (GitHub Docs)](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) · [Getting started — GitHub Docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-getting-started) · [features/copilot/cli](https://github.com/features/copilot/cli/) · [GitHub Education Pack](https://education.github.com/pack)

    **Předplatné:** Copilot Free (omezené), **Copilot Student** (zdarma pro ověřené studenty) nebo Copilot Pro / Pro+. Pokud máš studentský e-mail, projdi nejdřív [GitHub Education Pack](https://education.github.com/pack) — verifikace trvá obvykle 48–72 h.

    **Instalace (Windows, PowerShell):**

    ```powershell
    winget install --id GitHub.Copilot -e --source winget
    ```

    **Instalace (macOS, Linux, WSL):**

    ```bash
    npm install -g @github/copilot
    ```

    Vyžaduje **Node.js 22+** (winget si Node nezatáhne automaticky — pokud ho nemáš, doinstaluj `winget install OpenJS.NodeJS.LTS`). Alternativy: `brew install gh-copilot`, nebo standalone instalátor.

    **Spuštění a přihlášení:**

    ```bash
    copilot         # spustí agenta; uvnitř napiš /login a přihlas se přes prohlížeč
    ```

    Implicitní model je **Claude Sonnet 4.5**, přepneš ho příkazem `/model`. Copilot CLI je od února 2026 obecně dostupný (GA) a sdílí předplatné s pluginem v IDE.

    > **⚠️ Pozor:** Od **20. dubna 2026** GitHub dočasně **pozastavil nové registrace** pro Copilot Pro, Pro+ i Student. Pokud jsi už ověřený student z dřívějška, máš účet automaticky převedený do nového „Copilot Student" plánu a vše funguje. Pokud ne, sleduj [GitHub changelog](https://github.blog/changelog/) — pauza by měla být dočasná.

---

### 5.4 Ověření, že to funguje

Po instalaci spusť agenta v testovací složce a vyzkoušej:

```bash
# vytvoř si testovací složku, ať agent nepřepíše nic důležitého
mkdir test_ai && cd test_ai
git init

# spusť agenta (nahraď podle toho, co jsi instaloval)
claude        # nebo: codex, copilot
```

V chatu napiš:

> *„Vytvoř soubor `hello.py`, který vypíše `Ahoj, AI!`, spusť ho a ukaž mi výstup."*

Pokud agent:

- vytvoří soubor,
- spustí ho příkazem `python hello.py` (a požádá o potvrzení),
- ukáže ti výstup,

…máš hotovo a můžeš pokračovat na **[Cíl 6 — Ukázky](07_cil_6_ukazky.md)**.

> **💡 Tip:** Pokud agent po prvním pokusu nereaguje rozumně, často stačí spustit ho v jiné (čistě nové) složce — pomalá nebo přeplněná domovská složka mívá vliv.

---

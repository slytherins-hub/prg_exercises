# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## DOPLNĚK: AKTUÁLNÍ AI MODELY (KVĚTEN 2026)

> **⚠️ Tahle stránka stárne velmi rychle.** Přehled je zachycený k **květnu 2026**. Modely se mění průměrně každé 2–3 měsíce, ceny i dostupnost přes Copilot/Codex se mění ještě častěji. Pokud něco důležitého plánuješ, vždy si nejdřív ověř aktuální stav přímo u poskytovatele. Tato stránka má sloužit jako **orientační mapa**, ne jako referenční specifikace.

V agentech (Claude Code, Codex, Copilot CLI, e-INFRA) se setkáš se jmény jako *Sonnet 4.6*, *Opus 4.7*, *GPT-5.5*, *Gemini 3.1 Pro*, *agentic*, *thinker* a podobně. Tahle stránka ti dá jednoduchý přehled, **co je co a kdy si který vybrat**.

---

### Tři hlavní laby — kdo dnes vyrábí špičkové modely

#### Anthropic — rodina Claude

Tři velikostní třídy, číslování `4.X`, kde vyšší X = novější verze v rámci téže velikosti.

| Model | Vydání | Pro co je | Kontext |
|-------|--------|-----------|---------|
| **Claude Opus 4.7** | 16. 4. 2026 | Nejvýkonnější model Anthropicu, „step-change" v agentním kódování. Ideální na složité refaktoringy, návrh architektury, dlouhé úkoly. | 200K (1M v betě) |
| **Claude Sonnet 4.6** | 17. 2. 2026 | Vyvážený „pracovní kůň" — v Claude Code uživatelé preferovali Sonnet 4.6 nad starším Sonnet 4.5 v 70 % případů, dokonce i nad Opus 4.5 v 59 % případů. **Defaultní volba pro běžné programování.** | 1M (standardně) |
| **Claude Haiku 4.5** | 2025 | Nejlevnější a nejrychlejší. Drobné úpravy, rychlé otázky. Nehodí se na složitější uvažování. | 200K |

> **💡 Pravidlo palce:** Pokud nevíš, vyber **Sonnet 4.6**. Opus jen na úkoly, kde Sonnet zjevně nestačí (běží 3× déle a stojí 3× víc).

**Kde Claude modely uvidíš:** Claude Code (default), GitHub Copilot CLI (Pro/Pro+), API.

#### OpenAI — rodina GPT-5.X

Rok 2026 přinesl spojení reasoning a coding do jednoho modelu (GPT-5.4 → GPT-5.5).

| Model | Vydání | Pro co je | Kontext |
|-------|--------|-----------|---------|
| **GPT-5.5** (Thinking) | 23. 4. 2026 | **Aktuální flagship.** Velký skok proti 5.4 v agentním kódování (Terminal-Bench 2.0: 82,7 %). Nový default v Codexu pro Plus/Pro/Business/Enterprise/Edu. | **1M** v API, 400K v Codexu |
| **GPT-5.5 Pro** | 23. 4. 2026 | Maximální přesnost na nejtěžší úkoly. Jen ChatGPT Pro / Business / Enterprise. | 1M / 400K |
| **GPT-5.4** (Thinking) | 2026 | Předchozí flagship, stále dostupný v Codexu/API. | 272K (1M experimentálně) |
| **GPT-5.4 Pro** | 2026 | Předchozí Pro varianta. | 272K |
| **GPT-5.4 mini** | 2026 | Levnější, rychlejší varianta na lehčí úkoly nebo jako sub-agent. | — |
| **GPT-5.3-Codex** | 2025 | Specializovaný coding model (předchůdce). Pořád aktivní, hlavně v Copilot CLI. | — |
| **GPT-5.3-Codex-Spark** | 2025 | Research preview pro téměř okamžité interaktivní úpravy. Jen ChatGPT Pro. | — |

> **💡 GPT-5.5 v Codexu má „Fast mode"** — generuje tokeny ~1,5× rychleji za ~2,5× cenu. Hodí se na interaktivní úpravy, kde chceš okamžitou odezvu.

> **💡 Reasoning effort** u GPT-5.5: `none / low / medium (default) / high / xhigh`. Vyšší úroveň = víc přemýšlení, ale dražší a pomalejší.

> **💡 Co je „retired" k dubnu 2026:** GPT-4o, GPT-4.1, o4-mini, GPT-5 (Instant + Thinking), GPT-5.1 — pokud někde uvidíš tyhle názvy v dokumentaci, jde o starší materiály.

**Kde GPT modely uvidíš:** OpenAI Codex (default postupně `gpt-5.5`), GitHub Copilot CLI, ChatGPT, API.

#### Google — rodina Gemini 3

Velký skok v reasoning a v multimodalitě (text, obraz, audio, video).

**Pro modely (placené, flagship):**

| Model | Pro co je | Kontext |
|-------|-----------|---------|
| **Gemini 3.1 Pro** | Aktuální flagship (vydáno 19. 2. 2026). 2× lepší reasoning než Gemini 3 Pro. Excelentní na práci s velkými repozitáři, dlouhými PDF, videem. **Pozor:** Gemini 3 Pro Preview byl shutdownut 9. 3. 2026. | **1M tokenů** (vstup), 64K výstup |
| **Gemini 3 Pro** | Předchozí flagship, stále dostupný. | 1M |
| **Gemini 3 Deep Think** | Speciální „přemýšlí déle" mód v AI Ultra. | 1M |

**Flash a Lite modely (zajímavé pro free tier):**

| Model | Pro co je | Kontext |
|-------|-----------|---------|
| **Gemini 3.1 Flash-Lite Preview** | Aktuální nejrychlejší/nejlevnější model 3.x generace. Vhodný pro krátké dotazy, jednoduché úkoly, batch zpracování. **Free-eligible** v API. | 1M |
| **Gemini 3.1 Flash Live Preview** | Optimalizovaný pro live (streaming) interakce. **Free-eligible**. | 1M |
| **Gemini 3 Flash Preview** | Vyvážený rychlost/kvalita poměr v 3.x generaci. **Free-eligible**. | 1M |
| **Gemini 2.5 Flash** | Stabilní default na free tieru – „pracovní kůň" pro běžné kódování a chat. | 1M |
| **Gemini 2.5 Flash-Lite** | Nejvyšší propustnost na free tieru. Pro masové/levné použití. | 1M |
| **Gemini 2.5 Pro** | Stále zdarma na free tieru, ale s extrémně nízkou kvótou. | 1M |

> **💡 Síla Gemini:** **kontextové okno 1M tokenů** (≈ 1 500 stran textu, 30 000 řádků kódu, 8 hodin audia, 1 hodina videa). Když potřebuješ AI ukázat opravdu hodně dat najednou, Gemini je přirozená volba – a to **i na free tieru**.

##### Free tier konkrétně (květen 2026)

Free tier dostal **dvě výrazná zpřísnění**: v 12/2025 snížení limitů o 50–80 % a od **1. 4. 2026 odstraněny Pro modely** z free výběru (kromě 2.5 Pro s drasticky sníženou kvótou).

**Aktuální stav přes API klíč (zdarma, bez kreditní karty):**

| Model | RPM (req/min) | RPD (req/den) |
|-------|---------------|---------------|
| Gemini 2.5 Flash-Lite | 15 | 1 000 |
| Gemini 2.5 Flash | 10 | 500 |
| Gemini 2.5 Pro | 5 | 100 |
| Gemini 3.x Flash / Flash-Lite Preview | proměnlivé | proměnlivé (free-eligible v některých routes) |

Universal cap přes všechny modely: **250 000 TPM** (tokens per minute).

**Přes Antigravity CLI s přihlášením Google účtem** (jiná autentizace než API klíč, nástupce Gemini CLI):

- Free tier napříč všemi modely; po přechodu z Gemini CLI na Antigravity jsou limity **přísnější** než dřív — aktuální čísla viz [oficiální dokumentace](https://antigravity.google/docs/cli-install)
- Default model: Gemini Flash (Pro je velmi omezený – pár dotazů, pak fallback na Flash)

> **💡 Doporučení pro tohle cvičení:** Pro úkoly z Cíle 6 a běžnou výuku **úplně stačí free tier Antigravity CLI** přihlášený Google účtem. Flash modely jsou pro učení Pythonu více než dost; když narazíš na denní limit, přepni na jiný free nástroj (Codex free, Copilot Free, Claude Code přes e-INFRA).

> **⚠️ Deprecated k 06/2026:** Gemini 2.0 Flash byl ukončen 3. 3. 2026, **2.0 Flash-Lite shutdownuje 1. 6. 2026**. Pokud máš někde napsané `gemini-2.0-flash-lite`, do 1. 6. přepiš na `2.5-flash-lite`.

**Kde Gemini modely uvidíš:** **Antigravity CLI** (nativní, defaultní volba – zdarma, nástupce Gemini CLI), GitHub Copilot CLI (přes `/model`), gemini.google.com, AI Studio, Vertex AI.

---

### Open-source modely (důležité pro e-INFRA / lokální nasazení)

Vývoj otevřených modelů zrychlil natolik, že jsou v mnoha úlohách jen pár měsíců za uzavřenou špičkou. Pro běžné kódování často stačí.

| Model | Tvůrce | Pro co je |
|-------|--------|-----------|
| **Qwen3-Coder** (`qwen3-coder`, `qwen3-coder-480B`) | Alibaba | Špičkový open-source coding model. Default „agent" volba na e-INFRA. |
| **DeepSeek V3.2** | DeepSeek | Reasoning + general-purpose. Od ledna 2026 nahradil DeepSeek R1 na e-INFRA. Varianta `deepseek-v3.2-thinking` je vždy v reasoning módu. |
| **GPT-OSS-120B** | OpenAI (open weights) | 120 miliardový open model od OpenAI. |
| **GLM-4.7** | Zhipu AI | Default v reasoning módu. |
| **Llama 3.3** (`llama3.3:70b`) | Meta | Klasická open volba. |
| **MedGemma 27B** | Google | Specializovaný na medicínský doménový text. |

> **⚠️ Realita:** Otevřené modely jsou výborné, ale na ty nejtěžší agentní úlohy (komplikované refaktoringy přes desítky souborů) zpravidla **stále zaostávají** za Opus / GPT-5.4 / Gemini 3.1. Pro výuku a běžné cvičení jsou ale **víc než dost**.

---

### Co přesně dostaneš v jednotlivých nástrojích

| Nástroj | Defaultní model | Co lze přepnout |
|---------|----------------|------------------|
| **Antigravity CLI (free)** | Gemini Flash (Pro je velmi omezený – pár dotazů, pak fallback na Flash) | Gemini varianty přes `/model`; podle plánu i Claude / GPT-OSS |
| **Antigravity CLI (Google AI Pro / Ultra)** | Gemini 3.1 Pro | Gemini varianty (Flash, Flash-Lite, Pro) přes `/model`; podle plánu i Claude / GPT-OSS |
| **Claude Code (placený)** | Sonnet 4.6 | Opus 4.7, Haiku 4.5 (`/model`) |
| **Claude Code + e-INFRA** | `agentic` (= Qwen3-Coder / Sonnet-class open model) | `thinker` (Opus-class), `mini` (Haiku-class) — viz tabulka pod záložkou „Claude Code + e-INFRA" |
| **OpenAI Codex** | GPT-5.5 (Codex) | GPT-5.5 Pro (jen Pro plán), GPT-5.4, GPT-5.3-Codex, GPT-5.3-Codex-Spark |
| **GitHub Copilot CLI (Pro+)** | Sonnet 4.5 (`/model` přepne) | Claude Opus 4.6/4.7, Sonnet 4.4-4.6, Haiku 4.5, **GPT-5.5**, GPT-5.4, GPT-5.3-Codex, **Gemini 3 Flash, Gemini 3.1 Pro**, Grok Code Fast 1 |
| **GitHub Copilot Student / Free** | Auto mode | Bez ručního výběru — Auto mode routuje, ale Opus/Sonnet/GPT-5.5 nemůžeš zvolit ručně. Premium modely jen přes Auto. |

> **💡 Tip — `/model` v terminálu:** Prakticky všichni tři CLI agenti (`claude`, `codex`, `copilot`) přijímají uvnitř session příkaz `/model` — vypíše dostupné modely a umožní přepnout. Vyzkoušej hned po prvním přihlášení, ať vidíš svoji nabídku.

> **💡 Tip — auto mode:** Copilot CLI má od dubna 2026 funkci „auto" — agent sám vybírá model podle náročnosti úlohy. Šetří kvótu premium requestů (~10 % sleva oproti ručnímu výběru). Pro každodenní práci je obvykle **lepší volba než pevný výběr**.

---

### Když narazíš na „premium request" / „kvótu"

GitHub Copilot a OpenAI Codex počítají požadavky pomocí **multiplierů**:

| Model | Multiplier (Copilot) | Co to znamená |
|-------|---------------------|---------------|
| Claude Haiku 4.5 | 0.33× | 3 dotazy = 1 premium request |
| Claude Sonnet 4.6, GPT-5.3-Codex, GPT-5.4, GPT-5.5 | 1× | 1:1 |
| Claude Opus 4.6 | 3× | 1 dotaz = 3 premium requesty |
| Claude Opus 4.7 | 7.5× (do 30. 4. 2026) | Promo cena, normálně dražší |

Pokud agent přestane reagovat nebo začne hlásit „rate limit", obvykle pomůže **přepnout na lehčí model** (Haiku, Sonnet, GPT-5.4 mini), případně **začít novou konverzaci** (kratší kontext = méně tokenů).

---

### Jak si ověřit, co je k dispozici **právě teď**

Modely přibývají a mizí téměř měsíčně. Spolehlivé zdroje:

- **Claude:** [docs.claude.com/.../models/overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- **OpenAI:** [developers.openai.com/api/docs/models](https://developers.openai.com/api/docs/models)
- **Gemini:** [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)
- **GitHub Copilot:** [docs.github.com/.../supported-models](https://docs.github.com/en/copilot/reference/ai-models/supported-models)
- **e-INFRA / CESNET:** [docs.cerit.io/.../chat-ai](https://docs.cerit.io/en/docs/ai-as-a-service/chat-ai) nebo přímo dotaz na API:

    ```bash
    curl -H "Authorization: Bearer sk-..." https://llm.ai.e-infra.cz/v1/models
    ```

- **Souhrnný přehled pro studenty VUT:** [vut.cz/ai](https://www.vut.cz/ai) — i tahle stránka je aktualizovaná průběžně.

---

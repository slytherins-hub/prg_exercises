# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## DOPLNĚK: AKTUÁLNÍ AI MODELY (DUBEN 2026)

> **⚠️ Tahle stránka stárne velmi rychle.** Přehled je zachycený k **dubnu 2026**. Modely se mění průměrně každé 2–3 měsíce, ceny i dostupnost přes Copilot/Codex se mění ještě častěji. Pokud něco důležitého plánuješ, vždy si nejdřív ověř aktuální stav přímo u poskytovatele. Tato stránka má sloužit jako **orientační mapa**, ne jako referenční specifikace.

V agentech (Claude Code, Codex, Copilot CLI, e-INFRA) se setkáš se jmény jako *Sonnet 4.6*, *Opus 4.7*, *GPT-5.4*, *Gemini 3.1 Pro*, *agentic*, *thinker* a podobně. Tahle stránka ti dá jednoduchý přehled, **co je co a kdy si který vybrat**.

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

Rok 2026 přinesl spojení reasoning a coding do jednoho modelu (GPT-5.4).

| Model | Pro co je | Kontext |
|-------|-----------|---------|
| **GPT-5.4** (Thinking) | Aktuální flagship — spojuje reasoning z GPT-5.3 s coding ze GPT-5.3-Codex. **Defaultní volba v Codexu.** | 272K (1M experimentálně v Codexu) |
| **GPT-5.4 Pro** | Maximální výkon na nejtěžší úkoly, jen v ChatGPT Pro a Enterprise. | 272K |
| **GPT-5.4 mini** | Levnější, rychlejší varianta na lehčí úkoly nebo jako sub-agent. | — |
| **GPT-5.3-Codex** | Specializovaný coding model (předchůdce GPT-5.4 v Codexu). Pořád aktivní, hlavně v Copilot CLI. | — |
| **GPT-5.3-Codex-Spark** | Research preview pro téměř okamžité interaktivní úpravy. Jen ChatGPT Pro. | — |

> **💡 Co je „retired" k dubnu 2026:** GPT-4o, GPT-4.1, o4-mini, GPT-5 (Instant + Thinking), GPT-5.1 — pokud někde uvidíš tyhle názvy v dokumentaci, jde o starší materiály.

**Kde GPT modely uvidíš:** OpenAI Codex (default `gpt-5.4`), GitHub Copilot CLI, ChatGPT, API.

#### Google — rodina Gemini 3

Velký skok v reasoning a v multimodalitě (text, obraz, audio, video).

| Model | Pro co je | Kontext |
|-------|-----------|---------|
| **Gemini 3.1 Pro** | Aktuální flagship (vydáno 19. 2. 2026). 2× lepší reasoning než Gemini 3 Pro. Excelentní na práci s velkými repozitáři, dlouhými PDF, videem. **Pozor:** Gemini 3 Pro Preview byl shutdownut 9. 3. 2026. | **1M tokenů** (vstup), 64K výstup |
| **Gemini 3 Pro** | Předchozí flagship, stále dostupný. | 1M |
| **Gemini 3 Deep Think** | Speciální „přemýšlí déle" mód v AI Ultra. | 1M |

> **💡 Síla Gemini:** **kontextové okno 1M tokenů** (≈ 1 500 stran textu, 30 000 řádků kódu, 8 hodin audia, 1 hodina videa). Když potřebuješ AI ukázat opravdu hodně dat najednou, Gemini je přirozená volba.

**Kde Gemini modely uvidíš:** **Gemini CLI** (nativní, defaultní volba), GitHub Copilot CLI (přes `/model`), gemini.google.com, AI Studio, Vertex AI.

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
| **Gemini CLI (free)** | Gemini 3.1 Pro | Mezi Gemini variantami; pevně v rámci Google rodiny |
| **Claude Code (placený)** | Sonnet 4.6 | Opus 4.7, Haiku 4.5 (`/model`) |
| **Claude Code + e-INFRA** | `agentic` (= Qwen3-Coder / Sonnet-class open model) | `thinker` (Opus-class), `mini` (Haiku-class) — viz tabulka pod záložkou „Claude Code + e-INFRA" |
| **OpenAI Codex** | GPT-5.4 (Codex) | GPT-5.4 Pro (jen Pro plán), GPT-5.3-Codex, GPT-5.3-Codex-Spark |
| **GitHub Copilot CLI (Pro+)** | Sonnet 4.5 (`/model` přepne) | Claude Opus 4.6/4.7, Sonnet 4.4-4.6, Haiku 4.5, **GPT-5.4**, GPT-5.3-Codex, **Gemini 3 Flash, Gemini 3.1 Pro**, Grok Code Fast 1 |
| **GitHub Copilot Student / Free** | Auto mode | Bez ručního výběru — Auto mode routuje, ale Opus/Sonnet/GPT-5.4 nemůžeš zvolit ručně. Premium modely jen přes Auto. |

> **💡 Tip — `/model` v terminálu:** Prakticky všichni tři CLI agenti (`claude`, `codex`, `copilot`) přijímají uvnitř session příkaz `/model` — vypíše dostupné modely a umožní přepnout. Vyzkoušej hned po prvním přihlášení, ať vidíš svoji nabídku.

> **💡 Tip — auto mode:** Copilot CLI má od dubna 2026 funkci „auto" — agent sám vybírá model podle náročnosti úlohy. Šetří kvótu premium requestů (~10 % sleva oproti ručnímu výběru). Pro každodenní práci je obvykle **lepší volba než pevný výběr**.

---

### Když narazíš na „premium request" / „kvótu"

GitHub Copilot a OpenAI Codex počítají požadavky pomocí **multiplierů**:

| Model | Multiplier (Copilot) | Co to znamená |
|-------|---------------------|---------------|
| Claude Haiku 4.5 | 0.33× | 3 dotazy = 1 premium request |
| Claude Sonnet 4.6, GPT-5.3-Codex, GPT-5.4 | 1× | 1:1 |
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

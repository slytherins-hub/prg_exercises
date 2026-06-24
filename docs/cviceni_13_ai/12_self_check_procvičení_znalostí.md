# CVIČENÍ 13 (JEN AI): AI NÁSTROJE PRO PROGRAMOVÁNÍ

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: AI nástroje — přehled

1. **Co je hlavní rozdíl mezi chatbotem (např. ChatGPT v prohlížeči) a AI agentem (např. Claude Code)?**
    <ol type="a">
       <li>Chatbot je vždy zdarma, agent placený</li>
       <li>Agent funguje jen na Linuxu</li>
       <li>Chatbot je vždy přesnější než agent</li>
       <li>Agent vidí soubory v projektu, spouští kód, edituje soubory; chatbot jen odpovídá textem</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Klíčový rozdíl: agent má přístup k souborům a terminálu — opravdu pracuje na projektu. Chatbot jen píše text v prohlížeči, kód musíš ručně kopírovat tam a zpět.

</details>

2. **Co znamená věta „agent ≠ model"?**
    <ol type="a">
       <li>Agent je model, jen má jiné jméno</li>
       <li>Agent je rychlejší než model</li>
       <li>Model je „mozek" (LLM), agent je program (smyčka + nástroje), který model volá — proto stejného agenta můžeš napárovat na různé modely</li>
       <li>Modely fungují jen v cloudu, agenti jen lokálně</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Agent je smyčka „zavolej model → přečti odpověď → spusť nástroj → zopakuj". Model je oddělená vrstva. Proto např. Claude Code lze napojit na Anthropic API, e-INFRA, Bedrock i Ollama — model se mění, agent zůstává.

</details>

3. **Která z následujících kategorií AI nástrojů je *zdarma* s libovolným osobním Google účtem?**
    <ol type="a">
       <li>Claude Code</li>
       <li>OpenAI Codex</li>
       <li>Antigravity CLI (Google, nástupce Gemini CLI)</li>
       <li>Cursor</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Antigravity CLI (nástupce Gemini CLI) funguje zdarma s libovolným Google účtem, modely z rodiny Gemini 3 (1M kontext) — ideální start pro studenty bez předplatného. Navíc nepotřebuje Node.js. Proto se používá přímo na cvičení.

</details>

4. **Co je „vibe coding" a proč je problematický při studiu?**
    <ol type="a">
       <li>Programování bez IDE</li>
       <li>Programování při poslechu hudby</li>
       <li>Speciální funkce v Cursoru</li>
       <li>Přijímání AI výstupu bez porozumění — „funguje to" stačí. Při studiu škodí, protože se nenaučíš to, co máš</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Termín pojmenoval Andrej Karpathy. Pro jednorázový prototyp to může fungovat, ale při studiu se míjíš s celým vzdělávacím cílem — odevzdáš funkční kód, ale nic se nenaučíš.

</details>

---

### Část B: Klíčové koncepty AI nástrojů

5. **Proč je dobrý nápad mít pro každý úkol/projekt vlastní složku (repozitář)?**
    <ol type="a">
       <li>Aby agent rozuměl, co k čemu patří, a nepletl se mu nesouvisející soubory</li>
       <li>Protože Git jinak nefunguje</li>
       <li>Protože každá složka stojí jinak peněz</li>
       <li>Aby projekt zabíral více místa na disku</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Agent se orientuje podle souborů kolem sebe. Pokud má v jedné složce 15 nesouvisejících skriptů, neví, co k čemu patří. Vlastní složka per úkol mu dává čistý kontext.

</details>

6. **Jak se jmenuje instrukční soubor projektu pro Claude Code, OpenAI Codex a GitHub Copilot?**
    <ol type="a">
       <li><code>README.md</code>, <code>README.md</code>, <code>README.md</code></li>
       <li><code>.env</code>, <code>.env</code>, <code>.env</code></li>
       <li><code>config.json</code>, <code>config.json</code>, <code>config.json</code></li>
       <li><code>CLAUDE.md</code>, <code>AGENTS.md</code>, <code>.github/copilot-instructions.md</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Každý nástroj používá vlastní soubor: Claude Code → <code>CLAUDE.md</code>, Codex → <code>AGENTS.md</code>, Copilot → <code>.github/copilot-instructions.md</code>. <code>AGENTS.md</code> se postupně stává obecnějším standardem.

</details>

7. **Co je „kontextové okno" agenta a co se stane, když se zaplní?**
    <ol type="a">
       <li>Pomocná složka na disku, do které agent ukládá data</li>
       <li>Speciální okno IDE, kde agent zobrazuje grafy</li>
       <li>Veškerý text, který agent při odpovědi čte (zprávy, výstupy, obsah souborů). Když se zaplní, agent začne zapomínat starší části nebo se část komprimuje do souhrnu</li>
       <li>Funkce, která blokuje internet</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Kontext má omezenou velikost. Když přijde k limitu, agent buď zapomíná, nebo komprimuje (např. v Claude Code příkazem <code>/compact</code>). Začít novou konverzaci je často nejrychlejší řešení a může výsledek i zlepšit.

</details>

8. **K čemu slouží MCP servery?**
    <ol type="a">
       <li>Jsou to fyzické servery v Microsoftu</li>
       <li>Umožňují agentovi připojit se k externím nástrojům a službám (databáze, web, Google Drive, GitHub)</li>
       <li>Šifrují kontext mezi modelem a uživatelem</li>
       <li>Slouží jen ke spouštění Pythonu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> MCP (Model Context Protocol) je standard, který funguje jako „zásuvka" pro agenta — rozšiřuje jeho schopnosti za hranice pouhého psaní kódu. Bez MCP agent vidí jen soubory a terminál.

</details>

9. **Agent se „zacyklí" a opakovaně padá na stejné chybě. Co je doporučený první krok podle cvičení?**
    <ol type="a">
       <li>Okamžitě restartovat počítač</li>
       <li>Smazat celý projekt</li>
       <li>Říct agentovi „Stop. Žádné další změny. Popiš v 3 větách, kde teď přesně jsme a co je rozbité."</li>
       <li>Přepnout počítač do letového režimu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Donutit agenta zastavit se a popsat stav je nejlevnější krok — často sám prozradí, kde dělá chybu. Až když to nepomůže, přichází na řadu zúžení zadání, návrat přes <code>git checkout</code>, nová konverzace nebo přepnutí modelu.

</details>

---

### Část C: Instalace AI nástrojů

10. **Který AI agent se ve cvičení používá pro praktické ukázky a proč?**
    <ol type="a">
       <li>Cursor — protože je ze všech nejnovější</li>
       <li>Antigravity CLI — funguje zdarma s Google účtem, žádné předplatné, instalace zabere minutu a nepotřebuje Node.js</li>
       <li>JetBrains AI Assistant — je předinstalovaný v PyCharmu</li>
       <li>Windsurf — funguje jen v učebnách VUT</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Antigravity CLI (nástupce Gemini CLI) má nejméně překážek pro start: stačí libovolný Google účet, žádná kreditka, instaluje se jedním skriptem a nepotřebuje Node.js. Proto je ideální pro výuku.

</details>

11. **Co je nezbytný předpoklad pro instalaci OpenAI Codex (nebo GitHub Copilot CLI) přes `npm`?**
    <ol type="a">
       <li>Java 17+</li>
       <li>Docker</li>
       <li>Mít účet v MetaCentru</li>
       <li>Node.js 20+ (kvůli <code>npm</code> / <code>npx</code>)</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Bez Node.js 20+ <code>npm</code> ani <code>npx</code> nepoběží a instalace selže. V učebně bez admin práv je k dispozici pomocný PowerShell skript, který Node.js stáhne do uživatelského profilu. (Pozn.: Antigravity CLI je výjimka — je to binárka v Go a Node.js nepotřebuje.)

</details>

12. **K čemu slouží konfigurace Claude Code přes e-INFRA (CESNET)?**
    <ol type="a">
       <li>Umožňuje studentům českých VŠ používat Claude Code zdarma s open-source modely (Qwen, GPT-OSS, DeepSeek) přes OpenAI-kompatibilní endpoint</li>
       <li>Je to placená alternativa k Anthropic API</li>
       <li>Spouští Claude Code na MetaCentrum úložišti</li>
       <li>Přidává Claude Code podporu pro Windows</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> CESNET provozuje OpenAI-kompatibilní endpoint, který Claude Code umí volat místo Anthropic API. Pro studenty s eduID/CESNET účtem je to zdarma, data zůstávají v české akademické infrastruktuře.

</details>

---

### Část D: Bezpečnost a pravidla

13. **Která data NIKDY nepatří do AI agenta nebo chatu?**
    <ol type="a">
       <li>Veřejně dostupný kód z GitHubu</li>
       <li>Vlastní zápisky z přednášky</li>
       <li>Hesla, API klíče, osobní údaje pacientů, data podléhající GDPR</li>
       <li>Ukázková sekvence DNA z výukového textu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Data odeslaná do AI služby opouštějí tvůj počítač. Pravidlo platí i pro „bezpečnější" prostředí (e-INFRA) — bezpečné prostředí ≠ povolení posílat cokoliv.

</details>

14. **Doplň chybějící slovo z pravidel VUT pro použití AI: „Za škody i za kvalitu odevzdaných výstupů odpovídá ten, kdo AI ___."**
    <ol type="a">
       <li>nainstaloval</li>
       <li>použil</li>
       <li>zaplatil</li>
       <li>vyvinul</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Princip „odpovědnost za výstup" je první a nejdůležitější bod stanoviska VUT. AI nemůže být omluvou za chybu — odpovědnost nese uživatel.

</details>

15. **Který přístup je podle cvičení správný při použití AI ve studiu?**
    <ol type="a">
       <li>Zkopíruj zadání do AI, vygenerované řešení odevzdej beze změn</li>
       <li>Zkus úkol napřed sám, AI použij na vysvětlení/opravy, rozuměj výslednému kódu, uveď že jsi AI použil</li>
       <li>Použij AI jen na opravu překlepů</li>
       <li>AI použij vždy a nepřiznávej to, šetří to čas</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Tento postup je popsaný v Cíli 7 jako příklad správného přístupu. Odpovědnost (rozumíš odevzdanému), transparentnost (uvedeš nástroj) a učení (AI ti pomáhá, ne nahrazuje myšlení) jsou tři klíčové pilíře.

</details>

16. **Proč je při práci s AI agentem důležité commitovat před každou větší interakcí?**
    <ol type="a">
       <li>Aby agent věděl, co dělat</li>
       <li>Git ti slouží jako záchranná síť — když agent něco rozbije, <code>git diff</code> ukáže, co změnil, a <code>git checkout .</code> všechno vrátí</li>
       <li>Bez commitu agent nemůže číst soubory</li>
       <li>Commit zrychluje agenta</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Agent může upravit více souborů najednou. Bez Gitu bys ručně hledal, co se změnilo. S Gitem je návrat k předchozí verzi otázkou jednoho příkazu — proto se říká „verzování jako záchranná brzda".

</details>

---

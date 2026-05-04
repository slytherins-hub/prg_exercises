# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Dědičnost v Pythonu

1. **Co je hlavní důvod, proč v OOP používáme dědičnost?**
   <ol type="a">
      <li>Společný kód napíšeme jednou v rodičovské třídě a potomci ho automaticky zdědí</li>
      <li>Aby kód běžel rychleji</li>
      <li>Dědičnost je povinná v každém Python programu</li>
      <li>Aby se třídy nemusely ukládat na disk</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Dědičnost odstraňuje duplikaci — společné chování (atributy, metody) napíšeš jednou v rodiči a všichni potomci ho dostanou „zdarma". Když pak chybu opravíš v rodiči, oprava se promítne do všech potomků.

</details>

2. **Jak v Pythonu syntakticky řekneš, že třída `ECGSignal` dědí od třídy `Signal`?**
   <ol type="a">
      <li><code>class ECGSignal extends Signal:</code></li>
      <li><code>class ECGSignal inherits Signal:</code></li>
      <li><code>class ECGSignal(Signal):</code></li>
      <li><code>class ECGSignal -> Signal:</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Závorka za názvem třídy říká, od jaké třídy se dědí. Klíčová slova jako <code>extends</code> nebo <code>inherits</code> jsou z jiných jazyků (Java), Python je nepoužívá.

</details>

3. **K čemu slouží volání `super().__init__(name, values)` v konstruktoru potomka?**
   <ol type="a">
      <li>Zavolá <code>__init__</code> rodičovské třídy a nastaví společné atributy</li>
      <li>Vytvoří nový objekt rodičovské třídy</li>
      <li>Smaže atributy potomka</li>
      <li>Spustí všechny metody rodiče</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> <code>super().__init__(...)</code> zavolá konstruktor rodiče, takže se nastaví společné atributy (např. <code>self.name</code>, <code>self.values</code>) bez toho, abys ten kód musel kopírovat. Teprve pak v potomkovi přidáš jeho specifické atributy.

</details>

4. **Co vypíše tento kód?**
   ```python
   class Sequence:
       def __init__(self, name, sequence):
           self.name = name
           self.sequence = sequence.upper()
       def length(self):
           return len(self.sequence)

   class DNASequence(Sequence):
       pass

   dna = DNASequence("test", "acgt")
   print(dna.length())
   ```
   <ol type="a">
      <li><code>AttributeError</code> — <code>DNASequence</code> nemá metodu <code>length</code></li>
      <li><code>0</code></li>
      <li><code>"acgt"</code></li>
      <li><code>4</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>DNASequence</code> dědí <code>__init__</code> i <code>length()</code> ze <code>Sequence</code>, takže metoda funguje automaticky a vrátí délku sekvence (4).

</details>

5. **Proč jsou výjimky `ValueError`, `TypeError` a `IndexError` zachyceny pomocí `except Exception:`?**
   <ol type="a">
      <li>Python automaticky převádí všechny chyby na <code>Exception</code></li>
      <li>Je to náhoda, jen u těchto tří</li>
      <li>Funguje to jen v Pythonu 3.12+</li>
      <li>Všechny dědí od třídy <code>Exception</code>, a potomci se chytí spolu s rodičem</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Hierarchie výjimek je praktická ukázka dědičnosti. Když odchytíš rodiče (<code>Exception</code>), zachytíš i všechny jeho potomky.

</details>

---

### Část B: Úkol DNA a RNA sekvence

6. **Proč třída `Sequence` v `__init__` volá `sequence.upper()`?**
   <ol type="a">
      <li>Protože malá písmena Python nepodporuje</li>
      <li>Aby se sekvence zkrátila na polovinu</li>
      <li>Aby všechny metody dál pracovaly s konzistentním tvarem (velká písmena), bez ohledu na vstup</li>
      <li>Je to jen estetický doplněk bez funkčního významu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Pravidlo „vždy velká písmena" se uplatní jednou v konstruktoru a platí pro celý objekt. Metody <code>gc_content</code>, <code>base_counts</code> atd. pak mohou bezpečně počítat s <code>"G"</code>, <code>"C"</code> a nemusí řešit varianty <code>"g"</code> nebo <code>"c"</code>.

</details>

7. **Co vrátí `gc_content()` pro sekvenci `"AAAA"`?**
   <ol type="a">
      <li><code>0.0</code></li>
      <li><code>0.5</code></li>
      <li><code>1.0</code></li>
      <li><code>4.0</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> GC obsah je podíl bází G a C. V sekvenci samých adeninů žádné G ani C nejsou, takže výsledek je <code>0.0</code>.

</details>

8. **Co je hlavní biologický rozdíl mezi DNA a RNA, který se promítá do tříd `DNASequence` a `RNASequence`?**
   <ol type="a">
      <li>RNA je dvouvláknová, DNA jednovláknová</li>
      <li>DNA neobsahuje bázi A (adenin)</li>
      <li>RNA má vždy přesně 64 bází</li>
      <li>RNA používá místo báze T (thymin) bázi U (uracil)</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> V RNA se každé T z DNA píše jako U. Proto <code>DNASequence.to_rna()</code> jen nahradí T za U a vrátí nový objekt <code>RNASequence</code>.

</details>

9. **Co vypíše tento kód?**
   ```python
   rna = RNASequence("mini", "AUGGCUUAA")
   print(rna.codons())
   ```
   <ol type="a">
      <li><code>["A", "U", "G", "G", "C", "U", "U", "A", "A"]</code></li>
      <li><code>["AU", "GG", "CU", "UA", "A"]</code></li>
      <li><code>"AUGGCUUAA"</code></li>
      <li><code>["AUG", "GCU", "UAA"]</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Metoda <code>codons()</code> rozdělí sekvenci na trojice (kodony). Sekvence má 9 bází a vznikají právě tři kodony: AUG, GCU, UAA.

</details>

10. **Najdi chybu v této metodě `is_valid()` ve třídě `RNASequence`:**
    ```python
    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "T"}
    ```
    <ol type="a">
       <li>Operátor <code>&lt;=</code> nelze použít na množiny</li>
       <li>Chybí <code>self</code> v parametru</li>
       <li>RNA nesmí obsahovat T — povolené báze jsou A, C, G, U</li>
       <li>Metoda by měla vracet <code>None</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> RNA používá U (uracil) místo T (thymin). Správná povolená sada je <code>{"A", "C", "G", "U"}</code>. Pro DNA verzi metody by tam naopak T patřilo.

</details>

11. **Metoda `to_rna()` ve třídě `DNASequence` vrací nový objekt `RNASequence`. Co o tom platí?**
    <ol type="a">
       <li>IDE může jméno <code>RNASequence</code> podtrhnout, ale Python ho hledá až při volání metody — takže to funguje, pokud jsou obě třídy ve stejném souboru</li>
       <li>Tento zápis Python nepovoluje — třída se musí definovat dřív, než se na ni odkáže</li>
       <li>Vrací nový objekt <code>DNASequence</code>, ne <code>RNASequence</code></li>
       <li>Funguje jen pokud <code>RNASequence</code> dědí od <code>DNASequence</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Python jména v těle metody vyhodnocuje až při volání, ne při definici. Stačí, aby v okamžiku volání <code>RNASequence</code> existovala — tedy aby byla definovaná v tom samém souboru.

</details>

---

### Část C: AI nástroje — přehled

12. **Co je hlavní rozdíl mezi chatbotem (např. ChatGPT v prohlížeči) a AI agentem (např. Claude Code)?**
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

13. **Co znamená věta „agent ≠ model"?**
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

14. **Která z následujících kategorií AI nástrojů je *zdarma* s libovolným osobním Google účtem (1000 req/den)?**
    <ol type="a">
       <li>Claude Code</li>
       <li>OpenAI Codex</li>
       <li>Gemini CLI</li>
       <li>Cursor</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Gemini CLI dává free tier 60 req/min a 1000 req/den s modelem Gemini 3.1 Pro (1M kontext) — ideální start pro studenty bez předplatného. Proto se používá přímo na cvičení.

</details>

15. **Co je „vibe coding" a proč je problematický při studiu?**
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

### Část D: Klíčové koncepty AI nástrojů

16. **Proč je dobrý nápad mít pro každý úkol/projekt vlastní složku (repozitář)?**
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

17. **Jak se jmenuje instrukční soubor projektu pro Claude Code, OpenAI Codex a GitHub Copilot?**
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

18. **Co je „kontextové okno" agenta a co se stane, když se zaplní?**
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

19. **K čemu slouží MCP servery?**
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

20. **Agent se „zacyklí" a opakovaně padá na stejné chybě. Co je doporučený první krok podle cvičení?**
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

### Část E: Instalace AI nástrojů

21. **Který AI agent se ve cvičení používá pro praktické ukázky a proč?**
    <ol type="a">
       <li>Cursor — protože je ze všech nejnovější</li>
       <li>Gemini CLI — má free tier 1000 req/den, žádné předplatné, instalace zabere minutu</li>
       <li>JetBrains AI Assistant — je předinstalovaný v PyCharmu</li>
       <li>Windsurf — funguje jen v učebnách VUT</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Gemini CLI má nejméně překážek pro start: stačí libovolný Google účet, žádná kreditka, free tier vystačí na celý semestr. Proto je ideální pro výuku.

</details>

22. **Co je nezbytný předpoklad pro instalaci Gemini CLI nebo OpenAI Codex přes `npm`?**
    <ol type="a">
       <li>Java 17+</li>
       <li>Docker</li>
       <li>Mít účet v MetaCentru</li>
       <li>Node.js 20+ (kvůli <code>npm</code> / <code>npx</code>)</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Bez Node.js 20+ <code>npm</code> ani <code>npx</code> nepoběží a instalace selže. V učebně bez admin práv je k dispozici pomocný PowerShell skript, který Node.js stáhne do uživatelského profilu.

</details>

23. **K čemu slouží konfigurace Claude Code přes e-INFRA (CESNET)?**
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

### Část F: Bezpečnost a pravidla

24. **Která data NIKDY nepatří do AI agenta nebo chatu?**
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

25. **Doplň chybějící slovo z pravidel VUT pro použití AI: „Za škody i za kvalitu odevzdaných výstupů odpovídá ten, kdo AI ___."**
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

26. **Který přístup je podle cvičení správný při použití AI ve studiu?**
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

27. **Proč je při práci s AI agentem důležité commitovat před každou větší interakcí?**
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

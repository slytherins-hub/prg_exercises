---
template: standalone.html
title: AI nástroje pro programování — přehled
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: #f5f5f7;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.slide { max-width: 1100px; width: 100%; }

h1 { text-align: center; font-size: 2.2rem; font-weight: 800; color: #1a1a2e; margin-bottom: 0.3em; }
.subtitle { text-align: center; font-size: 1rem; color: #666; margin-bottom: 2.2rem; font-weight: 400; }

.tool-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.1rem; margin-bottom: 2.5rem; }
@media (max-width: 820px) { .tool-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 480px) { .tool-grid { grid-template-columns: 1fr; } }

.tool-card { position: relative; border: 2px solid #d42a2a; border-radius: 14px; padding: 1.1rem 1.1rem 2.8rem; background: #fff; box-shadow: 0 4px 16px rgba(0,0,0,.07); display: flex; flex-direction: column; transition: transform .15s, box-shadow .15s; }
.tool-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,.12); }
.tool-card-title { display: block; color: #d42a2a; font-size: .95rem; font-weight: 700; border-bottom: 1px solid rgba(212,42,42,.3); padding-bottom: .35rem; margin-bottom: .7rem; text-transform: uppercase; letter-spacing: .04em; }
.tool-card-foot { position: absolute; left: 1rem; right: 1rem; bottom: .7rem; font-size: .78rem; color: #888; font-style: italic; border-top: 1px dashed rgba(212,42,42,.2); padding-top: .4rem; text-align: center; }

.tool-list { list-style: none; display: flex; flex-direction: column; gap: .4rem; padding: 0; margin: 0; }
.tool-list li { display: flex; align-items: center; justify-content: center; gap: .55rem; padding: .4rem .7rem; background: #fafafa; border: 1px solid rgba(212,42,42,.15); border-radius: 8px; min-height: 2.6rem; transition: background .12s; }
.tool-list li:hover { background: #fff0f0; }
.tool-list li img { height: 1.6rem; max-height: 1.6rem; max-width: 80%; width: auto; object-fit: contain; }
.tool-list li.icon img { height: 1.5rem; max-width: 1.7rem; flex: 0 0 auto; }
.tool-name { font-size: .82rem; font-weight: 600; color: #222; }
.tool-suffix { font-size: .72rem; font-weight: 500; color: #555; }

.compare { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,.07); margin-bottom: 2rem; font-size: .88rem; }
.compare th { background: #d42a2a; color: #fff; font-weight: 700; padding: .75rem 1rem; text-align: left; }
.compare td { padding: .7rem 1rem; background: #fff; border-bottom: 1px solid #eee; vertical-align: top; }
.compare tr:last-child td { border-bottom: none; }
.compare tr.highlight td { background: #fff5f5; }
.compare .logo-cell { display: flex; align-items: center; gap: .5rem; font-weight: 600; }
.compare .logo-cell img { height: 1.3rem; }
.badge { display: inline-block; font-size: .65rem; font-weight: 700; background: #d42a2a; color: #fff; padding: .15em .5em; border-radius: 4px; margin-left: .4rem; vertical-align: middle; text-transform: uppercase; }
.badge-free { background: #16a34a; }

.vs-section { max-width: 1100px; width: 100%; margin-bottom: 2rem; }
.vs-section h2 { font-size: 1.4rem; font-weight: 700; color: #1a1a2e; margin-bottom: 1rem; text-align: center; }
.vs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }
@media (max-width: 600px) { .vs-grid { grid-template-columns: 1fr; } }
.vs-card { border-radius: 14px; padding: 1.3rem 1.4rem; box-shadow: 0 4px 16px rgba(0,0,0,.07); }
.vs-card.chatbot { background: #f0f0f5; border: 2px solid #bbb; }
.vs-card.agent { background: #fff5f5; border: 2px solid #d42a2a; }
.vs-card h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: .6rem; }
.vs-card.chatbot h3 { color: #555; }
.vs-card.agent h3 { color: #d42a2a; }
.vs-card ul { list-style: none; padding: 0; }
.vs-card li { padding: .3rem 0; font-size: .88rem; color: #333; }
.vs-card li::before { margin-right: .4rem; font-size: .85rem; }
.vs-card.chatbot li::before { content: "—"; color: #999; }
.vs-card.agent li::before { content: "✓"; color: #d42a2a; font-weight: 700; }

.iface-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; margin-bottom: 1.5rem; }
@media (max-width: 700px) { .iface-grid { grid-template-columns: 1fr; } }
.iface-card { background: #fff; border: 2px solid #ddd; border-radius: 14px; padding: 1.2rem; box-shadow: 0 4px 16px rgba(0,0,0,.06); text-align: center; }
.iface-card.best { border-color: #d42a2a; box-shadow: 0 4px 20px rgba(212,42,42,.15); }
.iface-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: .5rem; color: #1a1a2e; }
.iface-card.best h3 { color: #d42a2a; }
.iface-card ul { list-style: none; padding: 0; text-align: left; font-size: .82rem; color: #444; }
.iface-card li { padding: .2rem 0; }
.iface-card li::before { content: "· "; color: #999; }

.slide-footer { text-align: center; font-size: .8rem; color: #aaa; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e0e0e0; }

.cta-section { max-width: 1100px; width: 100%; margin-bottom: 2rem; text-align: center; }
.cta-hero { background: linear-gradient(135deg, #fff5f5, #f0f0f5); border: 2px solid #d42a2a; border-radius: 16px; padding: 2rem 2.5rem; margin-bottom: 1.2rem; }
.cta-hero .big { font-size: 1.3rem; font-weight: 700; color: #1a1a2e; line-height: 1.5; }
.cta-list { text-align: left; max-width: 700px; margin: 1.2rem auto 0; font-size: .92rem; color: #333; line-height: 1.7; }
.cta-list li { margin-bottom: .3rem; }
.cta-list li strong { color: #d42a2a; }

.note-box { background: #f8f8fa; border-left: 4px solid #d42a2a; border-radius: 0 8px 8px 0; padding: .8rem 1.2rem; margin-bottom: 1.5rem; font-size: .88rem; color: #444; line-height: 1.5; }
.note-box strong { color: #1a1a2e; }

.iface-shot-stack { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2rem; margin-bottom: 1.5rem; }
@media (max-width: 700px) { .iface-shot-stack { grid-template-columns: 1fr; } }
.iface-shot-card { text-align: center; }
.iface-shot-card img { width: 100%; border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,.12); border: 1px solid #e0e0e0; cursor: pointer; transition: transform .2s; }
.iface-shot-card img:hover { box-shadow: 0 8px 32px rgba(0,0,0,.2); }
.iface-shot-card .caption { font-size: .85rem; font-weight: 600; color: #555; margin-top: .4rem; }

.lightbox-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,.85); z-index: 9999; justify-content: center; align-items: center; cursor: zoom-out; }
.lightbox-overlay.active { display: flex; }
.lightbox-overlay img { max-width: 95vw; max-height: 95vh; border-radius: 8px; box-shadow: 0 0 60px rgba(0,0,0,.5); }
</style>

<div class="slide" markdown="0">
  <h1>AI nástroje pro programování</h1>
  <p class="subtitle">přehled kategorií a nástrojů · stav 2026 · vývoj jde rychle</p>

  <div class="tool-grid">
    <div class="tool-card">
      <span class="tool-card-title">Chatboti</span>
      <ul class="tool-list">
        <li><img src="../ai_logos/claude_ai_wordmark.svg" alt="Claude"></li>
        <li><img src="../ai_logos/openai_wordmark.svg" alt="OpenAI"><span class="tool-suffix">ChatGPT</span></li>
        <li><img src="../ai_logos/gemini_wordmark.svg" alt="Gemini"></li>
        <li><img src="../ai_logos/grok_wordmark.svg" alt="Grok"></li>
        <li><img src="../ai_logos/deepseek_wordmark.svg" alt="DeepSeek"></li>
      </ul>
      <span class="tool-card-foot">copy-paste · ptej se přirozeným jazykem</span>
    </div>

    <div class="tool-card">
      <span class="tool-card-title">Online nástroje</span>
      <ul class="tool-list">
        <li class="icon"><img src="../ai_logos/aistudio.png" alt=""><span class="tool-name">Google AI Studio</span></li>
        <li class="icon"><img src="../ai_logos/lovable.svg" alt=""><span class="tool-name">Lovable</span></li>
        <li><img src="../ai_logos/replit_wordmark.svg" alt="Replit"></li>
        <li class="icon"><img src="../ai_logos/firebase_studio.svg" alt=""><span class="tool-name">Firebase Studio</span></li>
      </ul>
      <span class="tool-card-foot">v prohlížeči · nejrychlejší start</span>
    </div>

    <div class="tool-card">
      <span class="tool-card-title">AI IDE</span>
      <ul class="tool-list">
        <li><img src="../ai_logos/cursor_wordmark.svg" alt="Cursor"></li>
        <li><img src="../ai_logos/google_antigravity_wordmark.svg" alt="Google Antigravity"></li>
        <li><img src="../ai_logos/windsurf_wordmark.svg" alt="Windsurf"></li>
      </ul>
      <span class="tool-card-foot">desktopové IDE s vestavěnou AI</span>
    </div>

    <div class="tool-card">
      <span class="tool-card-title">AI agenti</span>
      <ul class="tool-list">
        <li><img src="../ai_logos/claude_ai_wordmark.svg" alt="Claude"><span class="tool-suffix">Code</span></li>
        <li><img src="../ai_logos/openai_wordmark.svg" alt="OpenAI"><span class="tool-suffix">Codex</span></li>
        <li class="icon"><img src="../ai_logos/github_copilot.svg" alt=""><span class="tool-name">GitHub Copilot</span></li>
      </ul>
      <span class="tool-card-foot">autonomní · terminál / IDE / CI</span>
    </div>
  </div>

  <div class="vs-section">
    <h2>Chatbot vs. AI agent</h2>
    <div class="vs-grid">
      <div class="vs-card chatbot">
        <h3>Chatbot</h3>
        <ul>
          <li>Nevidí tvůj projekt — musíš kopírovat</li>
          <li>Nespouští kód</li>
          <li>Navrhne opravu textem</li>
          <li>Neinstaluje balíčky</li>
          <li>Nemá přístup k terminálu</li>
          <li>Needituje soubory — kopíruješ ručně</li>
        </ul>
      </div>
      <div class="vs-card agent">
        <h3>AI agent</h3>
        <ul>
          <li>Vidí celý projekt — čte soubory přímo</li>
          <li>Spouští kód a čte výstup</li>
          <li>Opraví, spustí znovu, ověří</li>
          <li>Instaluje si co potřebuje</li>
          <li>Plný přístup k terminálu</li>
          <li>Přímo zapisuje změny do souborů</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="vs-section">
    <h2>Kterého agenta si vybrat?</h2>
    <table class="compare">
      <thead>
        <tr><th>Nástroj</th><th>Cena</th><th>Vhodný pro</th><th>Poznámky</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><div class="logo-cell"><img src="../ai_logos/claude_ai_wordmark.svg" alt="Claude"><span class="tool-suffix">Code</span></div></td>
          <td>~$25/měs (Claude Pro)<br>vyšší tarify pro náročnější použití</td>
          <td>komplexní vícekrokové úlohy, refaktoring, velké projekty</td>
          <td><strong>nejvýkonnější uvažování</strong>; zvládá velké codebase</td>
        </tr>
        <tr>
          <td><div class="logo-cell"><img src="../ai_logos/github_copilot.svg" alt="" style="height:1.3rem"><span class="tool-name">GitHub Copilot</span></div></td>
          <td>~$10/měs<br>studentská varianta zdarma (bez nejnovějších modelů)</td>
          <td>denní použití v IDE, bezpečný start</td>
          <td><strong>napovídání kódu při psaní</strong>; výběr modelů (Claude, GPT, Gemini)</td>
        </tr>
        <tr>
          <td><div class="logo-cell"><img src="../ai_logos/openai_wordmark.svg" alt="OpenAI"><span class="tool-suffix">Codex</span></div></td>
          <td>~$25/měs (ChatGPT Plus)</td>
          <td>skripty, opravy, agentní úlohy</td>
          <td>těsná integrace s ChatGPT; funkční agent</td>
        </tr>
      </tbody>
    </table>
    <div class="note-box">
      <strong>AI agent není model</strong> — je to program, který umí volat libovolný AI model (Claude, GPT, Gemini…), ale navíc má přístup k souborům, terminálu a dalším nástrojům. Model je „mozek", agent je celý „pracovník".
    </div>
    <div class="note-box">
      <strong>Práce s různými agenty je velmi podobná</strong> — zadáváte úkol přirozeným jazykem, agent píše kód, spouští ho a opravuje chyby. Nástroje se liší v detailech, ale základní princip je u všech stejný. Jsou v mnoha ohledech ekvivalentní.
    </div>
    <div class="note-box">
      <strong>Uvedené ceny jsou měsíční předplatné</strong> s omezeným množstvím spotřebovaných tokenů (= objem textu a kódu, který AI zpracuje). Všechny nástroje nabízejí i dražší tarify s vyššími limity nebo přímou platbu za spotřebované tokeny přes API.
    </div>
  </div>

  <div class="vs-section">
    <h2>Tři způsoby, jak spustit AI agenta</h2>
    <div class="iface-grid">
      <div class="iface-card">
        <h3>Desktopová aplikace</h3>
        <ul>
          <li>Běží lokálně, hezké GUI</li>
          <li>Zatím hlavně Claude Code</li>
          <li>Nejjednodušší volba</li>
          <li>Žádný terminál, žádné nastavování</li>
        </ul>
      </div>
      <div class="iface-card">
        <h3>Terminál (CLI)</h3>
        <ul>
          <li>Vždy nejnovější funkce</li>
          <li>Běží všude — VS Code, SSH, servery</li>
          <li>Nejvýkonnější způsob</li>
          <li>Bez vazby na konkrétní editor</li>
        </ul>
      </div>
      <div class="iface-card best">
        <h3>Rozšíření v IDE</h3>
        <ul>
          <li>Claude Code, Copilot, Cursor a další</li>
          <li>Agent mód + chat přímo v editoru</li>
          <li>Diffy jedním klikem</li>
          <li>Copilot navíc nabízí doplňování řádků při psaní</li>
        </ul>
      </div>
    </div>
    <div class="iface-shot-stack">
      <div class="iface-shot-card">
        <img src="../calude_rozhrani/claude_app.png" alt="Claude — desktopová aplikace" onclick="openLightbox(this)">
        <div class="caption">Claude — desktopová aplikace</div>
      </div>
      <div class="iface-shot-card">
        <img src="../calude_rozhrani/claude_terminal.png" alt="Claude Code — terminál" onclick="openLightbox(this)">
        <div class="caption">Claude Code — terminál</div>
      </div>
      <div class="iface-shot-card">
        <img src="../calude_rozhrani/claude_plugin_vscode.png" alt="Claude Code — VS Code" onclick="openLightbox(this)">
        <div class="caption">Claude Code — rozšíření ve VS Code</div>
      </div>
    </div>
    <div class="lightbox-overlay" id="lightbox" onclick="closeLightbox()">
      <img id="lightbox-img" src="" alt="">
    </div>
    <script>
    function openLightbox(el) {
      document.getElementById('lightbox-img').src = el.src;
      document.getElementById('lightbox').classList.add('active');
    }
    function closeLightbox() {
      document.getElementById('lightbox').classList.remove('active');
    }
    </script>
  </div>

  <div class="cta-section">
    <div class="cta-hero">
      <div class="big">Skok z <strong>chatbota</strong> na <strong>AI agenta</strong> je zhruba tak velký,<br>jako když jste poprvé zkusili ChatGPT.</div>
    </div>
  </div>

  <div class="vs-section">
    <h2>„Vibe coding" vs. AI-assisted programování</h2>
    <div class="vs-grid">
      <div class="vs-card chatbot">
        <h3>Vibe coding</h3>
        <ul>
          <li>Přijímáš AI výstup bez porozumění</li>
          <li>„Funguje to" = hotovo</li>
          <li>Neučíš se — přeskakuješ základy</li>
          <li>Chyby těžko najdeš</li>
          <li>OK pro jednorázový prototyp</li>
        </ul>
      </div>
      <div class="vs-card agent">
        <h3>AI-assisted programování</h3>
        <ul>
          <li>Rozumíš co a proč AI vytvořilo</li>
          <li>Čteš kód, ptáš se, učíš se</li>
          <li>AI ti zrychluje práci, ne nahrazuje myšlení</li>
          <li>Chyby najdeš — víš co hledat</li>
          <li>Správný přístup pro studium i praxi</li>
        </ul>
      </div>
    </div>
    <div class="note-box">
      <strong>AI používej jako nástroj, který ti pomáhá se učit</strong> — ne jako nástroj, který se učí místo tebe.
    </div>
  </div>

  <p class="slide-footer">Algoritmizace a programování · Cvičení 13B</p>
</div>

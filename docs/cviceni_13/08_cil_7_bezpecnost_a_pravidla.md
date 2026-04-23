# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 7: BEZPEČNOST A PRAVIDLA POUŽÍVÁNÍ AI

AI agent je mocný nástroj — vidí tvé soubory, spouští tvé příkazy a tvá data posílá přes internet. Než
ho pustíš na ostrou práci, je potřeba rozumět třem věcem: **co se děje s tvými daty**, **jaká pravidla
platí při studiu** a **jak zabránit tomu, aby agent něco nevratně pokazil**. O tom je tento cíl.

---

### 7.1 Co AI služby dělají s tvými daty

Když používáš AI agenta, tvůj kód, data a konverzace se odesílají na servery poskytovatele (Anthropic, OpenAI, GitHub, Google…). Je důležité rozumět, co se s nimi děje:

- **Kód a text se odesílají přes internet** – opouštějí tvůj počítač.
- **Poskytovatelé obvykle data nepoužívají k trénování modelů** (v placených plánech), ale vždy si přečti podmínky konkrétní služby.
- **Data mohou být dočasně uložena** na serverech poskytovatele (logování, bezpečnostní monitoring).

**Co z toho plyne:**

- **Nikdy neposílej hesla, API klíče, tokeny nebo přístupové údaje** do AI chatu nebo agenta.
- **Opatrně s osobními údaji** – jména pacientů, rodná čísla, zdravotní záznamy nemají co dělat v AI konverzaci.
- **Firemní/univerzitní data** – než pošleš interní kód nebo data do AI služby, ověř si, jestli to pravidla tvé organizace dovolují.

> **💡 Tip:** Pokud potřebuješ AI pomoc s kódem, který pracuje s citlivými daty, použij **zástupné/syntetické hodnoty** místo skutečných dat.

---

### 7.2 Pravidla používání AI na univerzitě

> **📜 Závazná pravidla VUT:** Plné znění je na **[vut.cz/ai/pravidla-ai](https://www.vut.cz/ai/pravidla-ai)** (a oficiální stanovisko na [úřední desce VUT](https://www.vut.cz/uredni-deska/ai)). Čti **dřív, než AI použiješ na zápočťák, semestrálku nebo závěrečnou práci** — porušení může mít disciplinární následky.

#### Co říká stanovisko VUT — krátce

VUT bere generativní AI jako **asistenční a konzultační nástroj** (ne jako náhradu vlastní práce) a nastavuje k jejímu použití tyto závazné principy:

1. **Odpovědnost za výstup** — Za škody i za kvalitu odevzdaných výstupů odpovídá ten, kdo AI použil. AI nemůže být „omluvou" za chybu v práci.
2. **Povinnost ověřovat** — Musíš důsledně ověřit **správnost, pravdivost i nezávadnost** všeho, co AI vyprodukuje. Halucinace = tvoje chyba.
3. **Ochrana dat** — Nesmíš do AI nástrojů svěřovat osobní údaje, obchodní tajemství, ani jiná chráněná data, pokud na to nemáš výslovné oprávnění. Vždy zvaž, co odesíláš.
4. **Soulad s předpisy** — AI lze používat jen tam, kde to neodporuje obecně závazným zákonům **a vnitřním předpisům VUT** (včetně etického kodexu).
5. **Transparentnost** — *„Nesprávné či nepřiznané použití generativní AI může být považováno za porušení etických zásad ve smyslu ghost-writing nebo contract-cheating."* Použití AI vždy v práci přiznej (viz 7.3 Akademická integrita).
6. **Autorská práva** — Při použití výstupů z AI dbáš na autorská práva a podmínky poskytovatele dané AI služby. Některé výstupy mohou mít licenční omezení.
7. **Hodnotové směřování** — AI má sloužit ke zlepšování kvality života, udržitelnosti a řešení reálných problémů, **ne** k obcházení vlastního studia.

> **💡 Praktický překlad pro tohle cvičení:** AI ti smí pomoct kód napsat, opravit nebo vysvětlit. Co odevzdáš, musíš **ty sám rozumět** a umět vysvětlit u tabule nebo v diskusi. A do agenta nikdy nelep cizí osobní údaje, hesla ani interní materiály VUT.

> **⚠️ Toto je jen orientační výtah — závazné je znění VUT.** Souhrn 7 bodů výše je didaktické zjednodušení, ne přesné parafrázování. Závazný zdroj je vždy oficiální stanovisko VUT na **[vut.cz/ai/pravidla-ai](https://www.vut.cz/ai/pravidla-ai)** — pokud řešíš konkrétní hraniční situaci, čti přímo tam.

> **🎯 Vždy si zjisti pravidla konkrétního předmětu a projektu — to je nejdůležitější.** Univerzitní stanovisko stanovuje rámec, ale **konkrétní povolení a omezení nastavuje každý vyučující sám pro svůj předmět** (sylabus, zadání úkolu, pokyny k závěrečné práci, podmínky zkoušky). Stejné pravidlo platí pro projekty mimo školu — vždy se zeptej, **co je pro tenhle konkrétní úkol povolené**, než AI použiješ. Když si nejsi jistý, zeptej se vyučujícího/vedoucího — je to rychlejší než řešit pak průšvih.

Obecné zásady, které **typicky** platí napříč předměty (znova: ne závazně, ale jako vodítko):

**AI je povolený nástroj, ne zakázaný — ale s pravidly:**

- **Rozuměj tomu, co odevzdáváš.** I když kód napsal AI agent, zodpovědnost za výsledek neseš ty. Pokud neumíš vysvětlit, jak tvůj kód funguje, je to problém.
- **Uveď, že jsi AI použil.** Většina předmětů vyžaduje transparentnost – napiš do komentáře nebo do dokumentace, jaký nástroj jsi použil a jak.
- **AI nesmí nahradit učení.** Cílem úkolů je, abys pochopil koncept. Pokud AI udělá celý úkol za tebe a ty se nic nenaučíš, míjíš se s účelem studia.
- **Nepoužívej AI u zkoušek a testů**, pokud to není explicitně povoleno.

**Příklad správného přístupu:**

1. Zkus úkol napřed vyřešit sám.
2. Tam kde se zasekneš, požádej AI o pomoc – vysvětlení konceptu, nápovědu, ukázku.
3. Porozuměj řešení a dopiš/uprav ho vlastními silami.
4. Do komentáře napiš: *„Při řešení jsem použil GitHub Copilot / Claude Code pro [co konkrétně]."*

**Příklad špatného přístupu:**

1. Zkopíruješ zadání do AI.
2. AI vygeneruje celé řešení.
3. Odevzdáš ho beze změn a bez porozumění.

---

### 7.3 Akademická integrita

Použití AI bez uvedení zdroje může být posuzováno jako **plagiát** – podobně jako kdybys opsal od spolužáka. Klíčový rozdíl mezi legitimním použitím a podvodem:

| Legitimní použití | Podvod |
|-------------------|--------|
| AI pomůže pochopit koncept, ty napíšeš řešení | AI napíše řešení, ty ho odevzdáš |
| Uvedeš jaký nástroj jsi použil | Zatajíš použití AI |
| Umíš vysvětlit každý řádek svého kódu | Neumíš vysvětlit co kód dělá |
| AI použiješ k odladění konkrétní chyby | AI použiješ k obejití celého úkolu |

> **⚠️ Důležité:** Pravidla se liší předmět od předmětu a univerzita od univerzity. Vždy si přečti pravidla konkrétního předmětu a pokud si nejsi jistý, zeptej se vyučujícího.

---

### 7.4 Bezpečnost kódu generovaného AI

AI může generovat kód, který obsahuje bezpečnostní chyby. Studie ukazují, že AI kód má výrazně víc bezpečnostních zranitelností než kód psaný člověkem. Na co si dávat pozor:

- **Hardcoded credentials** – AI může do kódu vložit ukázkové heslo nebo API klíč. Nikdy to neodevzdávej do Gitu.
- **SQL injection, XSS** – AI ne vždy správně ošetřuje uživatelské vstupy.
- **Zastaralé knihovny** – AI může navrhnout verze balíčků se známými zranitelnostmi.
- **Příliš volná oprávnění** – AI může navrhnout řešení, které funguje, ale dává víc přístupu než je nutné.

**Co s tím:**

- Vždy zkontroluj, jestli kód neobsahuje hardcoded hesla nebo klíče.
- U webových aplikací zkontroluj ošetření vstupů.
- Používej `.gitignore` pro soubory s citlivými údaji (`.env`, `credentials.json`).

---

### 7.5 Sandbox a Docker – proč je důležité omezit agenta

AI agent má přístup k tvému terminálu a souborům. To znamená, že **může udělat cokoli, co bys udělal ty** – smazat soubory, přepsat kód, nainstalovat balíčky, spustit libovolný příkaz. Většina agentů se před rizikovými akcemi ptá na potvrzení, ale:

- Při rychlé práci je lákavé potvrzovat všechno bez čtení.
- Některé nástroje nabízí „auto-approve" / „YOLO" mód, kde agent dělá vše bez ptaní.
- Agent může udělat chybu – smazat soubory, přepsat konfiguraci, provést `git push --force`.

**Řešení: sandbox (izolované prostředí)**

Sandbox znamená, že agent běží v omezeném prostředí, kde nemůže poškodit tvůj systém:

| Přístup | Co to je | Kdy použít |
|---------|----------|-----------|
| **Potvrzování příkazů** | Agent se ptá před každou akcí | Výchozí nastavení, vhodné pro začátečníky |
| **Dedikovaný projekt/složka** | Agent pracuje jen v jedné složce, zbytek disku je v bezpečí | Vždy – proto pracuj v repozitáři per úkol |
| **Docker kontejner** | Agent běží v izolovaném virtuálním prostředí, nemá přístup k tvému systému | Produkční použití, práce s cizím kódem |
| **Git jako záchranná síť** | Commitni před prací s agentem, vrať změny pokud se něco pokazí | Vždy |

**Docker** je nástroj, který vytvoří izolovaný kontejner – jako „počítač v počítači". Agent v něm může dělat cokoli, ale nemůže ovlivnit tvůj skutečný systém. Pro pokročilejší použití (zejména když chceš nechat agenta pracovat autonomně bez potvrzování) je Docker prakticky nutnost.

> **⚠️ Pravidlo:** Dokud přesně nevíš co děláš, **nevypínej potvrzování příkazů**. Vždy čti, co agent chce spustit, než to potvrdíš. Auto-approve mód je jen pro zkušené uživatele v izolovaném prostředí.

---

### 7.6 Shrnutí pravidel

1. **Data:** Neposílej citlivé údaje do AI služeb.
2. **Transparentnost:** Uveď, že jsi AI použil.
3. **Porozumění:** Rozuměj všemu, co odevzdáváš.
4. **Pravidla předmětu:** Ověř si, co je povoleno.
5. **Bezpečnost kódu:** Kontroluj AI výstup na bezpečnostní chyby.
6. **Izolace:** Nech agenta pracovat v omezeném prostředí a nevypínej potvrzování příkazů.

---

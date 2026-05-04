# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 7: BEZPEČNOST A PRAVIDLA POUŽÍVÁNÍ AI

> **⚠️ Stav: duben 2026.** Vývoj AI nástrojů i univerzitních pravidel jde velmi rychle. Pro závazné znění pravidel se vždy řiď aktuální oficiální stránkou své instituce ([vut.cz/ai/pravidla-ai](https://www.vut.cz/ai/pravidla-ai) pro VUT) a podmínkami konkrétního předmětu.

Tato kapitola má dvě části:

- **Pravidla** — co o použití AI říká VUT a co z toho prakticky plyne pro tvoji práci ve škole.
- **Rizika** — co se děje s tvými daty a jak zabránit tomu, aby agent něco nevratně pokazil.

---

## A) PRAVIDLA

### A.1 Závazný zdroj — VUT

Plné a závazné znění pravidel VUT najdeš na **[vut.cz/ai/pravidla-ai](https://www.vut.cz/ai/pravidla-ai)** (a oficiální stanovisko na [úřední desce VUT](https://www.vut.cz/uredni-deska/ai)). Čti **dřív, než AI použiješ na zápočťák, semestrálku nebo závěrečnou práci** — porušení může mít disciplinární následky.

VUT bere generativní AI jako **asistenční a konzultační nástroj** (ne jako náhradu vlastní práce). Cokoli zde uvádíme níže je didaktické zjednodušení — pro hraniční situace se vždy podívej do oficiálního zdroje.

### A.2 Krátké shrnutí (7 principů VUT)

1. **Odpovědnost za výstup** — Za kvalitu i škody odpovídá ten, kdo AI použil. AI není omluva.
2. **Povinnost ověřovat** — Správnost, pravdivost i nezávadnost výstupu si musíš ověřit. Halucinace = tvoje chyba.
3. **Ochrana dat** — Žádné osobní údaje, obchodní tajemství ani chráněná data bez výslovného oprávnění.
4. **Soulad s předpisy** — AI lze používat jen tam, kde to neodporuje zákonům a vnitřním předpisům VUT.
5. **Transparentnost** — Nepřiznané použití AI může být posuzováno jako ghost-writing / contract-cheating. Vždy přiznej.
6. **Autorská práva** — Respektuj licence výstupů AI a podmínky poskytovatele.
7. **Hodnotové směřování** — AI má pomáhat řešit reálné problémy, ne obcházet vlastní studium.

### A.3 Pravidla v praxi

**Vždy si zjisti pravidla konkrétního předmětu a úkolu.** Univerzitní stanovisko stanovuje rámec, ale **konkrétní povolení a omezení nastavuje každý vyučující sám** (sylabus, zadání úkolu, pokyny k závěrečné práci). Když si nejsi jistý, zeptej se vyučujícího — je to rychlejší než řešit pak průšvih.

**Doporučený postup u úkolu:**

1. Zkus úkol napřed vyřešit sám.
2. Tam kde se zasekneš, požádej AI o vysvětlení konceptu, nápovědu nebo ukázku.
3. Porozuměj řešení a dopiš/uprav ho vlastními silami.
4. Do komentáře napiš, co konkrétně jsi s AI dělal: *„Při řešení jsem použil GitHub Copilot / Claude Code pro [co konkrétně]."*

**Legitimní použití vs. podvod:**

| Legitimní použití | Podvod |
|-------------------|--------|
| AI pomůže pochopit koncept, ty napíšeš řešení | AI napíše řešení, ty ho odevzdáš |
| Uvedeš, jaký nástroj jsi použil | Zatajíš použití AI |
| Umíš vysvětlit každý řádek svého kódu | Neumíš vysvětlit, co kód dělá |
| AI použiješ k odladění konkrétní chyby | AI použiješ k obejití celého úkolu |

> **📌 Tři věci, které si musíš odnést:**
>
> 1. **Rozuměj tomu, co odevzdáváš.** Když to neumíš obhájit u tabule, není to tvoje práce.
> 2. **Za odevzdané ručíš ty, ne AI.** „Tohle mi vygeneroval Copilot" není omluva.
> 3. **U každého úkolu si zjisti pravidla.** Pokud chybí v zadání, zeptej se **dřív**, než AI použiješ.

### A.4 Proč se pravidla liší — analogie s kalkulačkou

Jestli je AI povolená, omezená, nebo úplně zakázaná, záleží na tom, **k čemu konkrétní předmět nebo úkol slouží**. Dobrá analogie je kalkulačka:

- **V první třídě je kalkulačka u písemky zakázaná.** Ne proto, že by byla špatná — ale protože celý smysl cvičení je naučit se sčítat v hlavě. Kdyby ji učitelka dovolila, dítě zmáčkne pár tlačítek, dostane správný výsledek a **nic se nenaučí**.
- **Ve čtvrtém ročníku inženýrství je kalkulačka (a Matlab, a numerické knihovny) povinnou výbavou.** Když počítáš statiku mostu, nikdo nečeká, že budeš násobit matice na papíře — cíl je **dostat správný výsledek v rozumném čase**.

S AI je to úplně stejné. V předmětech, kde se učíš **základy** (jako tady v Algoritmizaci a programování), je cílem pochopit, jak se rozkládá problém na funkce a jak počítač přemýšlí. Kdyby všechno napsala AI, **mineš celý vzdělávací cíl** — i když odevzdáš funkční kód. V projektových předmětech, na bakalářce nebo v praxi je naopak cílem **dodat fungující řešení** a AI je standardní pracovní nástroj jako kompilátor.

**Proto se musíš u každého úkolu ptát.** Stejné zadání („napiš program, který…") může mít opačné pravidlo podle toho, jestli si máš procvičit základy, nebo dodat výsledek.

---

## B) RIZIKA

### B.1 Co AI služby dělají s tvými daty

Když používáš AI agenta, tvůj kód, data a konverzace se odesílají na servery poskytovatele (Anthropic, OpenAI, GitHub, Google…). Je důležité rozumět, co se s nimi děje:

- **Kód a text se odesílají přes internet** – opouštějí tvůj počítač.
- **Poskytovatelé obvykle data nepoužívají k trénování modelů** (v placených plánech), ale vždy si přečti podmínky konkrétní služby.
- **Data mohou být dočasně uložena** na serverech poskytovatele (logování, bezpečnostní monitoring).

**Co z toho plyne:**

- **Nikdy neposílej hesla, API klíče, tokeny nebo přístupové údaje** do AI chatu nebo agenta.
- **Opatrně s osobními údaji** – jména pacientů, rodná čísla, zdravotní záznamy nemají co dělat v AI konverzaci.
- **Firemní/univerzitní data** – než pošleš interní kód nebo data do AI služby, ověř si, jestli to pravidla tvé organizace dovolují.

> **💡 Tip:** Pokud potřebuješ AI pomoc s kódem, který pracuje s citlivými daty, použij **zástupné/syntetické hodnoty** místo skutečných dat.

> **🇨🇿 Tip — e-INFRA / CESNET:** Pro univerzitní data je doporučená varianta **[chat.ai.e-infra.cz](https://chat.ai.e-infra.cz)** — chatbot provozovaný v české akademické infrastruktuře CESNET. Pro studenty s eduID/CESNET účtem (přes [MetaCentrum](https://metavo.metacentrum.cz/)) je **zdarma** a provozovatel deklaruje, že **data neopouštějí prostředí e-INFRA** (žádné odesílání ke komerčním poskytovatelům typu Anthropic / OpenAI / Google). Vedle webového chatbota nabízí i OpenAI-kompatibilní API endpoint, který lze použít v Claude Code (viz Cíl 5). Pro běžnou univerzitní práci — výukové materiály, studentské projekty, neveřejný interní obsah — vhodnější volba než komerční cloudoví agenti.

### B.2 Bezpečnost kódu generovaného AI

AI kód má statisticky víc bezpečnostních zranitelností než kód psaný člověkem. Typické problémy: **hardcoded hesla a API klíče**, špatně ošetřené vstupy (SQL injection, XSS), zastaralé knihovny se známými chybami a zbytečně volná oprávnění.

**Co s tím:** přečti si výstup, než ho commitneš. Hesla a klíče drž mimo repozitář (`.gitignore`, `.env`).

### B.3 Sandbox a Docker — proč omezit agenta

AI agent může udělat cokoli, co bys udělal ty — smazat soubory, přepsat kód, spustit libovolný příkaz. Většina agentů se před rizikovou akcí ptá, ale auto-approve / „YOLO" mód toto vypíná a agent může chybu provést bez tvého vědomí.

| Přístup | Co to je | Kdy použít |
|---------|----------|-----------|
| **Potvrzování příkazů** | Agent se ptá před každou akcí | Výchozí — vhodné pro začátečníky |
| **Dedikovaný projekt/složka** | Agent pracuje jen v jedné složce | Vždy — pracuj v repozitáři per úkol |
| **Docker kontejner** | Agent běží v izolovaném prostředí, nemůže ovlivnit tvůj systém | Pokročilé použití, autonomní běh, cizí kód |
| **Git jako záchranná síť** | Commitni před prací s agentem | Vždy |

> **⚠️ Pravidlo:** Dokud přesně nevíš, co děláš, **nevypínej potvrzování příkazů**. Auto-approve je jen pro zkušené uživatele v izolovaném prostředí (typicky Docker).

---

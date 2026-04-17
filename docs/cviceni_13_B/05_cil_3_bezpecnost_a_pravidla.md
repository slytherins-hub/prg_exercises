# CVIČENÍ 13B: AI NÁSTROJE PRO PROGRAMOVÁNÍ

Algoritmizace a programování

## CÍL 3: BEZPEČNOST A PRAVIDLA POUŽÍVÁNÍ AI

### 3.1 Co AI služby dělají s tvými daty

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

### 3.2 Pravidla používání AI na univerzitě

Používání AI nástrojů při studiu se řídí pravidly tvé univerzity a konkrétního předmětu. Tady jsou obecné zásady, které typicky platí:

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

### 3.3 Akademická integrita

Použití AI bez uvedení zdroje může být posuzováno jako **plagiát** – podobně jako kdybys opsal od spolužáka. Klíčový rozdíl mezi legitimním použitím a podvodem:

| Legitimní použití | Podvod |
|-------------------|--------|
| AI pomůže pochopit koncept, ty napíšeš řešení | AI napíše řešení, ty ho odevzdáš |
| Uvedeš jaký nástroj jsi použil | Zatajíš použití AI |
| Umíš vysvětlit každý řádek svého kódu | Neumíš vysvětlit co kód dělá |
| AI použiješ k odladění konkrétní chyby | AI použiješ k obejití celého úkolu |

> **⚠️ Důležité:** Pravidla se liší předmět od předmětu a univerzita od univerzity. Vždy si přečti pravidla konkrétního předmětu a pokud si nejsi jistý, zeptej se vyučujícího.

---

### 3.4 Bezpečnost kódu generovaného AI

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

### 3.5 Shrnutí pravidel

1. **Data:** Neposílej citlivé údaje do AI služeb.
2. **Transparentnost:** Uveď, že jsi AI použil.
3. **Porozumění:** Rozuměj všemu, co odevzdáváš.
4. **Pravidla předmětu:** Ověř si, co je povoleno.
5. **Bezpečnost kódu:** Kontroluj AI výstup na bezpečnostní chyby.

---

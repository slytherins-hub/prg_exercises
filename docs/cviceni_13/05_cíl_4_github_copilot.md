# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 4: GITHUB COPILOT – AGENT MÓD

### 4.1 Co je GitHub Copilot a proč ho použít

GitHub Copilot je AI asistent přímo integrovaný do PyCharmu. Znáš ho pravděpodobně z doplňování kódu při psaní – navrhne řádek nebo funkci, ty přijmeš nebo odmítneš. To je ale jen jedna z jeho schopností.

Možná už AI používáš přes prohlížeč – ChatGPT, Claude nebo jiný chatbot. Postup bývá zhruba takový: zkopíruješ kód do okna chatu, napíšeš co chceš, zkopíruješ odpověď zpátky do editoru, spustíš, dostaneš chybu, zkopíruješ chybu do chatu… Funguje to, ale je to pomalé a náchylné na chyby – při každém kopírování se něco může ztratit nebo rozhodit kontext.

Copilot přímo v PyCharmu tohle celé odstraní:

- **vidí tvůj kód přímo** – nemusíš nic kopírovat, ví co máš otevřené,
- **píše změny přímo do souborů** – nemusíš nic přenášet zpátky,
- **spouští kód sám** – nemusíš přepínat okna,
- **čte chybové hlášky sám** – nemusíš je kopírovat do chatu,
- **pamatuje si celou konverzaci** – kontext se neztratí.

**Agent mód** (*Copilot Agent*) tohle dotahuje ještě dál. Místo aby jen doplňoval kód nebo odpovídal na otázky, Copilot v agent módu:

- rozumí celé konverzaci a navazuje na předchozí zprávy,
- **sám spouští kód** a čte výstup (výsledek, chybovou hlášku),
- **iteruje** – když kód selže, přečte chybu a zkusí ji opravit,
- **edituje soubory** – nejen navrhne změnu, ale přímo ji zapíše,
- **spouští terminálové příkazy** – instalace balíčků, git příkazy,
- pracuje na úkolu autonomně, dokud ho v průběhu nezastavíš.

Jinými slovy: místo cyklu „zkopíruj → vlož do chatu → zkopíruj zpět → spusť → zkopíruj chybu…" stačí napsat co chceš a Copilot celý cyklus projde sám.

---

### 4.2 Instalace pluginu

GitHub Copilot není v PyCharmu předinstalovaný – přidáš ho jako plugin:

1. Otevři `File → Settings` (nebo `Ctrl+Alt+S`).
2. Jdi do sekce **Plugins**.
3. Vyhledej **GitHub Copilot** a klikni **Install**.
4. Po instalaci restartuj PyCharm.
5. Přihlas se ke svému GitHub účtu – PyCharm otevře přihlašovací stránku v prohlížeči.

> **💡 Tip:** Plugin je zdarma pro studenty registrované v [GitHub Education](https://education.github.com/). Pokud máš školní e-mail, registrace trvá pár minut.

### 4.3 Jak agent mód otevřít

1. V PyCharmu otevři panel **GitHub Copilot Chat** (ikona Copilota na pravém panelu, nebo přes menu `View → Tool Windows → GitHub Copilot Chat`).
2. V horní části chatu přepni režim na **Agent**.
3. Copilot teď vidí tvůj projekt, otevřené soubory a může spouštět terminál.

> **💡 Tip:** V běžném chat módu Copilot jen odpovídá textem. V „Agent" módu má přístup k nástrojům – editaci souborů, terminálu, spouštění kódu. Je to zásadní rozdíl.

---

### 4.3 Jak s ním efektivně pracovat

**Piš zadání jako konverzaci, ne jako příkazy.** Místo:

> *write a function that calculates gc content*

zkus:

> *Přidej do třídy DNASequence metodu gc_content(), která vrátí podíl bází G a C. Otestuj ji na třech různých sekvencích.*

Čím víc kontextu dáš, tím přesnější výsledek.

**Ptej se na chyby přímo.** Pokud vidíš chybovou hlášku, nemusíš ji ručně hledat. Zkopíruj ji nebo prostě napiš:

> *Dostávám tuto chybu: [vložíš chybovou hlášku]. Co to znamená a jak to opravit?*

Copilot přečte chybu, podívá se na kód a navrhne opravu.

**Iteruj.** Copilot nedá vždy dokonalý výsledek napoprvé – to je v pořádku a platí to i pro lidi. Fungující postup je:

1. Zadej, co chceš.
2. Copilot napíše kód a spustí ho.
3. Podívej se na výsledek. Pokud nesedí, řekni co je špatně.
4. Copilot opraví a znovu spustí.
5. Opakuj, dokud to nefunguje.

**Rozděl větší úkol na kroky.** Místo:

> *Vytvoř kompletní aplikaci s GUI pro analýzu EKG.*

raději:

> *Nejdřív vytvoř třídu ECGSignal s atributy name, values, sampling_rate a metodou plot(). Pak přidáme GUI.*

**Kontroluj, co Copilot dělá.** Agent mód dává Copilotovi velkou autonomii. Vždy si přečti, co chce udělat (zejména u terminálových příkazů), než to potvrdíš. PyCharm ti vždy před akcí ukáže návrh a čeká na souhlas.

> **⚠️ Pozor – YOLO mód:** V nastavení Copilota existuje možnost „Auto-approve" neboli **YOLO mód** – Copilot v něm spouští všechny terminálové příkazy bez potvrzení. Pro rychlou práci to může být lákavé, ale **nedoporučujeme ho zapínat**, dokud přesně nevíš, co děláš. Copilot v YOLO módu může bez upozornění smazat soubory, přepsat kód nebo provést `git push` na sdílený repozitář. Výchozí nastavení – kdy se u každého příkazu ptá na souhlas – je bezpečnější a pro začátek vždy lepší volba.

---

### 4.4 Efektivní vzory práce

Copilot tě nejlépe nahradí v rutinních, opakujících se nebo šablonovitých úkolech:

| Situace | Co říct Copilotovi |
|---------|-------------------|
| Chceš přidat metodu | *„Přidej metodu X, která dělá Y."* |
| Kód ti padá s chybou | *„Dostávám AttributeError na řádku 42, oprav to."* |
| Chceš vidět výstup | *„Spusť tento kód a ukaž mi výstup."* |
| Chceš otestovat | *„Vytvoř testovací volání pro všechny metody třídy."* |
| Chceš vysvětlení | *„Vysvětli, co dělá tento blok kódu."* |
| Chceš refaktoring | *„Přepiš tuto funkci tak, aby byla přehlednější."* |

---

### 4.5 Úkoly

**📝 ÚKOL 1: Celý úkol přes Copilota**

Otevři AI Assistant v PyCharmu v agent módu a splň zadání z předchozích cílů **výhradně pomocí konverzace s Copilotem**. Ty jen říkáš co chceš – Copilot píše kód, spouští ho a opravuje chyby.

Konkrétně:

1. Řekni Copilotovi, ať vytvoří třídy `Sequence` a `DNASequence` podle zadání z cíle 3.
2. Požádej ho, ať metody otestuje na alespoň 3 sekvencích a výstup vypiše do konzole.
3. Řekni mu, ať přidá vizualizaci `plot_composition()` a spustí ji.
4. Commitni a pushni výsledek na GitHub – taky přes Copilota (požádej ho o `git add`, `git commit`, `git push`).

Celý úkol by měl jít splnit bez toho, abys napsal jediný řádek kódu ručně.

> **💡 Tip:** PyCharm se v agent módu ptá na potvrzení před každou akcí v terminálu. Vždy si přečti, co Copilot navrhuje udělat, než klikneš Potvrdit.

---

**📝 ÚKOL 2: Hra Snake s Copilotem**

Tento úkol je trochu jiný – procvičíš řízení Copilota na větším projektu.

Zadej Copilotovi v AI Assistantu (agent mód) toto:

> *Vytvoř jednoduchou hru Snake v Pythonu s grafickým oknem. Použij tkinter (nebo pygame). Had i jídlo se vykreslují jako barevné čtverce na mřížce. Hra musí být hratelná šipkami na klávesnici. Had se pohybuje sám.*

Copilot hru vytvoří. Spusť ji a ověř, že funguje.

Pak hru nech **modifikovat** – zadej:

> *Uprav hru tak, aby had začínal dlouhý (alespoň 10 článků) a při sebrání jídla se o jeden článek **zkrátil**. Pokud had dosáhne délky 1, hra končí výhrou.*

Tím se pravidla obrátí: místo aby had rostl, musíš ho zkrmit na nič. Hra skončí výhrou místo prohry ze standardního Snaka.

Cílem úkolu není perfektní hra – cílem je si vyzkoušet, jak Copilot zvládá iterativní úpravy většího projektu a jak ho efektivně navádět konverzací.

> **💡 Tip:** Pokud hra nefunguje nebo má chyby, řekni Copilotovi přesně co vidíš – chybovou hlášku, nebo popiš co se děje špatně. Neopravuj nic ručně – nech ho, ať to opraví sám a poté znovu spustí.

---

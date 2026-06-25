# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## NEJDŮLEŽITĚJŠÍ RADY

Stručný tahák — nejužitečnější návyky pro práci s AI agenty na jednom místě.

### Git a repozitář

- **Používej Git** — a nech s ním pracovat agenta (commituj před každou větší změnou, ať se můžeš vrátit).
- **Pro každý úkol čistá prázdná složka** — ať se agentovi nepletou nesouvisející soubory.
- **Nech agenta navrhnout strukturu repozitáře** podle sebe — většinou to udělá rozumně.
- **Nech vytvořit obsah repozitáře** (index) s odkazy na jednotlivé soubory.
- **Snaž se mít všechny informace v repozitáři** — co je jen v kontextu modelu, snadno zmizí (kontext často mažeš).
- **Pro paralelní práci na jedné věci použij `git worktrees`** — stačí říct agentovi, ať to použije.
- **Statickou stránku online** zveřejníš zdarma přes **GitHub Pages**.

### Plánování a postup

- **Nech agenta, ať se tě doptá** na chybějící informace.
- **Nejdřív plán, pak teprve tvorba** — nech celou věc naplánovat a plán si zkontroluj.
- **Rozsáhlou věc dělej po krocích** — na každý krok podle plánu pusť čistého (nového) agenta.
- **Často to trvá dlouho** — nauč se trochu multitasking (rozdělaná práce na pozadí).

### Kontext a paměť

- **Často mazej kontext** — nad ~100k tokenů začíná agent „hloupnout".
- **Než kontext smažeš, nech zapsat poznámky**, ať neztratíš informace.
- **Nech agenta dělat si poznámky** — `.md` pro agenta, **HTML pro tebe** (čitatel = člověk).
- **Nech zapsat důležitá pravidla**, která má dodržovat (jaký nástroj použít, oblíbená struktura kódu) — do instrukčního souboru.

### Zdroje a vstupy

- **Poskytni zdroje** (PDF, dataset, články), nebo nech agenta, ať si je sám stáhne.
- **Nech ze zdrojů udělat souhrn** s obsahem a odkazy.
- **PDF nech přepsat do `.md`** — lépe se s ním pak pracuje.
- **Používej obrázky** — fotky nákresů, printscreeny, schémata. Často rychlejší než popisovat slovy.
- **Čistě textové formáty jsou nejlepší** (`.md` je lepší než `.docx`…).

### Opakování a paralelizace

- **Opakovaný úkol → vytvoř skill** a příště ho jen vyvoláš.
- **Chceš víckrát stejnou věc → řekni, ať použije subagenty.**
- **Nech subagenty udělat třeba 10 variant** a vyber si tu, která ti vyhovuje.
- **Nech agenta psát automatické testy** — kvalita výsledku tím výrazně roste.

### Nástroje a jazyky

- **Najdi si svoje oblíbené CLI nástroje a nech je agenta používat** (`gh` CLI, `arduino-cli`, PrusaSlicer CLI…).
- **GUI umí agent velmi dobře** — neboj se nechat udělat malý nástroj i na „blbost".
- **Neboj se jiného programovacího jazyka** — vyber podle úlohy:
    - rychle a jednoduše / zpracování dat → **Python**
    - je to pomalé → přepiš do **Rust / C++**
    - souvisí to s webem → **JavaScript / TypeScript**
    - hodně paralelních operací → **Go**

### Výstupy

- **Pro výsledky je nejlepší HTML** (může být interaktivní), případně **Jupyter notebook**, pokud ti vyhovuje.

# CVIČENÍ 12: JUPYTER, NUMPY, MATPLOTLIB

Algoritmizace a programování

## CÍL 1: PYTHON EKOSYSTÉM

### Co se v tomto cíli naučíš?

Než se vrhneme na NumPy a grafy, hodí se mít přehled o tom, **jak se Python vlastně instaluje, jak se spravují balíčky a kde se vůbec píše kód**. Existuje spousta nástrojů a začátečníci se v nich snadno ztratí.

Tento cíl je **čistě teoretický** – žádný kód. Cílem je, abys věděl, co používáš a proč, a aby ti dávala smysl volba nástroje pro konkrétní situaci.

---

### 🧩 Základní pojmy

Než se pustíme do srovnání nástrojů, ujasníme si tři základní pojmy, které se budou opakovat.

#### Co je balíček (package)?

Python sám o sobě umí relativně málo – základní operace, cykly, funkce, soubory. Pro vše ostatní existují **balíčky**: hotové knihovny kódu, které někdo napsal a zveřejnil, abys nemusel vynalézat kolo.

Balíček si představ jako **rozšíření, které stáhneš a pak importuješ**:

```python
import numpy        # balíček pro numerické výpočty
import matplotlib   # balíček pro grafy
import pandas       # balíček pro tabulková data
```

Balíčky jsou uložené na internetu ve **repozitářích** – centrálních skladech knihoven. Existují dva hlavní:

- **PyPI** (Python Package Index, [pypi.org](https://pypi.org/)) – přes 500 000 čistě Pythonovských knihoven. Stahují odtud nástroje pip a uv.
- **conda-forge** – repozitář ekosystému conda, obsahuje nejen Python balíčky, ale i non-Python závislosti (C knihovny, CUDA, R…). Stahuje odtud conda a Mamba.

Oba repozitáře obsahují oblíbené knihovny jako NumPy nebo Matplotlib, ale conda balíčky jsou navíc otestované na vzájemnou kompatibilitu.

---

#### Co je virtuální prostředí (virtual environment)?

Představ si, že pracuješ na dvou projektech:

- **Projekt A** potřebuje `numpy` verze 1.24,
- **Projekt B** potřebuje `numpy` verze 2.0.

Pokud máš všechny balíčky nainstalované „globálně" (pro celý systém), nastane konflikt – oba projekty sdílí jednu instalaci a jeden z nich přestane fungovat.

**Virtuální prostředí** je **izolovaná složka**, která obsahuje:
- svoji verzi Pythonu,
- svoji sadu nainstalovaných balíčků.

Každý projekt má svoje prostředí, takže se vzájemně neovlivňují.

```
projekt_A/
  .venv/          ← virtuální prostředí projektu A (numpy 1.24)
  main.py

projekt_B/
  .venv/          ← virtuální prostředí projektu B (numpy 2.0)
  main.py
```

Správci balíčků jako pip, uv nebo conda tato prostředí umí vytvářet a spravovat.

---

#### Co je IDE?

**IDE** (Integrated Development Environment, česky: integrované vývojové prostředí) je program, ve kterém **píšeš kód**. Není to jen textový editor – IDE ti navíc nabízí:

- **zvýraznění syntaxe** – klíčová slova, chyby, typy jsou barevně odlišeny,
- **doplňování kódu** – napíšeš `np.` a IDE ti nabídne dostupné funkce,
- **debugger** – můžeš kód zastavit uprostřed, zkontrolovat proměnné a zjistit, kde je chyba,
- **terminál** – spustíš příkaz, aniž bys přepínal okna,
- **integraci s Gitem** – vidíš změny, commitneš rovnou z editoru.

Bez IDE bys mohl psát kód v Poznámkovém bloku a spouštět ho v terminálu – funguje to, ale je to nepraktické.

---

### 📦 Správa balíčků a prostředí

Než začneš psát `import numpy`, musíš mít numpy nainstalovaný. K tomu slouží **správci balíčků** – nástroje, které stáhnou knihovny a udrží je v pořádku.

#### pip

**pip** je výchozí správce balíčků pro Python. Instaluje balíčky z [PyPI](https://pypi.org/) – největšího repozitáře Python knihoven (přes 500 000 balíčků).

```bash
pip install numpy
pip install numpy matplotlib pandas
pip uninstall numpy
```

| Výhody | Nevýhody |
|--------|----------|
| Součást každé instalace Pythonu | Neřeší konflikty verzí automaticky |
| Jednoduchý, dobře zdokumentovaný | Neinstaluje samotný Python |
| Obrovský výběr balíčků na PyPI | Virtuální prostředí musíš spravovat ručně (`venv`) |

**Popularita:** pip je nejpoužívanější nástroj vůbec – každý Python projekt ho zná.

---

#### uv ⭐ *(používáme v tomto kurzu)*

**uv** je moderní nástroj napsaný v Rustu, navržený jako kompletní náhrada za pip + venv + pip-tools. Je **extrémně rychlý** (10–100× rychlejší než pip) a zároveň řeší i instalaci samotného Pythonu.

```bash
uv sync              # nainstaluje závislosti ze souboru pyproject.toml
uv add numpy         # přidá balíček do projektu
uv run python script.py  # spustí skript ve správném prostředí
```

| Výhody | Nevýhody |
|--------|----------|
| Velmi rychlý (Rust backend) | Relativně nový – komunita menší než pip |
| Spravuje Python i balíčky i prostředí | Jiný workflow než klasický pip |
| Reprodukovatelné projekty (`pyproject.toml`) | Některé starší tutoriály ho neznají |
| Detekuje konflikty závislostí | |

**Popularita:** Rychle roste – od roku 2024 je preferovanou volbou v moderních Python projektech.

> **💡 Proč používáme uv?** Protože nám řeší vše na jednom místě: instalaci Pythonu, virtuální prostředí i závislosti projektu. Jednou napíšeš `uv sync` a prostředí funguje na každém počítači stejně.

---

#### conda / Anaconda / Miniconda

**conda** je správce balíčků a prostředí zaměřený na **vědecké výpočty**. Na rozdíl od pipu umí nainstalovat i non-Python závislosti (C knihovny, CUDA, R…). Přichází ve dvou hlavních variantách:

- **Anaconda** (~3 GB) – plná distribuce: conda + Python + 250+ předinstalovaných vědeckých balíčků. Vše funguje hned po instalaci, ale zabere hodně místa.
- **Miniconda** (~100 MB) – minimální distribuce: jen conda + Python. Doinstaluj si pouze co skutečně potřebuješ.

```bash
conda create -n moje_prostredi python=3.12
conda activate moje_prostredi
conda install numpy matplotlib
```

| Výhody | Nevýhody |
|--------|----------|
| Řeší komplikované závislosti (NumPy, TensorFlow, CUDA) | Anaconda je těžká (~3 GB) |
| Funguje i na Windows bez kompilátoru | conda a pip v jednom prostředí mohou způsobit problémy |
| Populární ve vědeckém prostředí | Pomalejší než uv |
| Miniconda je odlehčená varianta | Jiný ekosystém než pip/PyPI |

**Popularita:** Stále velmi rozšířená ve vědeckém a akademickém prostředí, ale postupně nahrazována `uv` + pip kombinací.

> **💡 Poznámka:** Pro pokročilejší uživatele existují ještě **Mamba** (přepsaná conda v C++ – výrazně rychlejší řešení závislostí, stejné příkazy) a **Micromamba** (ultralehká verze bez conda backendu, oblíbená v CI/CD a kontejnerech).

---

#### Rychlé srovnání

| Nástroj | Rychlost | Spravuje Python? | Virtuální prostředí | Vědecké balíčky | Popularita |
|---------|----------|------------------|---------------------|-----------------|------------|
| pip | střední | ❌ | manuálně (`venv`) | přes PyPI | ⭐⭐⭐⭐⭐ základ všeho |
| **uv** | ⚡ nejrychlejší | ✅ | automaticky | přes PyPI | ⭐⭐⭐⭐ rychle roste |
| conda | pomalá | ✅ | automaticky | nativní podpora | ⭐⭐⭐⭐ věda a akademie |

---

### 🖥️ IDE a editory

**IDE** (Integrated Development Environment) = prostředí, kde píšeš kód. Nabízí zvýraznění syntaxe, doplňování kódu, debugger, terminál a mnoho dalšího.

#### PyCharm ⭐ *(používáme v tomto kurzu)*

**PyCharm** od JetBrains je IDE navržené přímo pro Python. Existuje ve dvou verzích: **Community** (zdarma, plně funkcionalní pro Python) a **Professional** (placená, navíc web, databáze, Jupyter podpora).

| Výhody | Nevýhody |
|--------|----------|
| Nejlepší Python-specifická podpora (refaktoring, analýza kódu) | Náročný na paměť (500 MB+) |
| Výborný debugger | Pomalejší start |
| Integrovaná podpora pro venv | Professional je placená |
| Automatická detekce chyb | Trochu strmější křivka učení |

**Popularita:** Nejoblíbenější IDE specificky pro Python vývoj.

---

#### VS Code

**Visual Studio Code** od Microsoftu je lehký **univerzální editor** rozšiřitelný přes pluginy. Na Windows je přirozenou volbou – nativní Microsoftí produkt s výbornou integrací do systému, WSL a Azure, a GitHub Copilot přímo v editoru.

| Výhody | Nevýhody |
|--------|----------|
| Zdarma, velmi rychlý start | Python podpora horší než v PyCharmu |
| **Univerzální** – Python, JS, Rust, Go, C++, … | Vyžaduje ruční konfiguraci přes rozšíření |
| **Výborná integrace na Windows** (WSL, Azure, Git) | Debugger méně pohodlný než v PyCharmu |
| Integrovaná podpora Jupyter notebooků | |
| GitHub Copilot přímo v editoru | |
| Největší komunita rozšíření | |

**Popularita:** Nejpopulárnější editor vůbec (Stack Overflow 2024: 73 % vývojářů). Pro Python druhý nejpoužívanější po PyCharmu.

---

#### Jupyter Notebook / JupyterLab

**Jupyter Notebook** je webové prostředí pro interaktivní Python v prohlížeči. Spustíš lokální server a přistupuješ přes `http://localhost:8888`. **JupyterLab** je modernější verze se záložkami a integrovaným průzkumníkem souborů.

| Výhody | Nevýhody |
|--------|----------|
| Ideální pro exploraci dat a vizualizace | Není IDE – chybí refactoring, silný debugger |
| Výstup (grafy, tabulky) přímo v dokumentu | Soubory `.ipynb` hůře verzovatelné v Gitu |
| Standard ve vědeckém výpočetnictví | Pořadí spuštění buněk může způsobit problémy |
| Exportovatelné do PDF, HTML, Markdown | |

**Popularita:** Standard v datové vědě a akademickém výzkumu.

---

#### Rychlé srovnání IDE

| Nástroj | Typ | Nejsilnější stránka | Nevýhoda | Popularita |
|---------|-----|---------------------|----------|------------|
| **PyCharm** | IDE | Python podpora, debugger | Těžší, placená Pro verze | ⭐⭐⭐⭐⭐ Python #1 |
| **VS Code** | Editor + pluginy | Univerzalita, Windows integrace, Copilot | Nutná konfigurace | ⭐⭐⭐⭐⭐ celkově #1 |
| **Jupyter Notebook** | Interaktivní prostředí | Vizualizace, explorativní analýza | Není plnohodnotné IDE | ⭐⭐⭐⭐ datová věda |

> **💡 Další alternativy:**
> - **Google Colab** – Jupyter v cloudu, zdarma GPU, žádná instalace; podrobněji v Cíli 2.
> - **Spyder** – IDE inspirované MATLABem (panel proměnných, konzole), součást Anacondy; vhodné pro přecházející z MATLABu, jinak niche.
> - **Zed** – nový ultrarychlý editor v Rustu (2024), zatím bez Windows verze.
> - **Cursor** – VS Code fork s AI editací přímo v kódu; roste popularita v ML komunitě.

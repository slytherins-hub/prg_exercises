# CVIČENÍ 12: JUPYTER, NUMPY, MATPLOTLIB

Algoritmizace a programování

## CÍL 2: `uv` TROCHU PODROBNĚJI

Doteď jsi z `uv` používal jen tři příkazy: `uv init`, `uv sync` a `uv add`. V tomhle cíli se podíváme
o kousek dál — hlavně na **dva soubory, které `uv` spravuje za tebe** (`pyproject.toml` a `uv.lock`),
pár dalších příkazů a taky to, jak `uv` umí spravovat **globální nástroje** a **verze Pythonu**.

---

### 2.1 `pyproject.toml` — jediný zdroj pravdy

**`pyproject.toml`** je **nejdůležitější soubor projektu**. Popisuje, co projekt je a co potřebuje:

```toml
[project]
name = "moje-analyza"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "jupyter>=1.0",
    "numpy>=2.0",
    "matplotlib>=3.8",
]
```

Tři věci, které si z toho zapamatuj:

- **`dependencies`** — seznam balíčků, které tvůj projekt potřebuje. Když zavoláš `uv add numpy`,
  řádek se sem dopíše automaticky. Nemusíš ten seznam upravovat ručně, ale je dobré ho umět přečíst.
- **`requires-python`** — kterou verzi Pythonu projekt vyžaduje. `uv` podle toho vybere správný interpret.
- **Přenositelnost.** Pošleš-li `pyproject.toml` kolegovi (nebo ho nahraješ na GitHub), stačí mu
  po klonování spustit `uv sync` a má přesně to samé prostředí jako ty. **Žádné `requirements.txt`,
  žádný manuál „nainstaluj si tohle a tamto".**

> **💡 Pravidlo:** `pyproject.toml` **vždy commituj do Gitu**. Je to popis projektu — bez něj se projekt
> nedá reprodukovat.

---

### 2.2 `uv.lock` — přesné verze pro reprodukovatelnost

Zatímco `pyproject.toml` říká „potřebuju numpy **≥ 2.0**", **`uv.lock`** zaznamenává přesně
**která verze byla skutečně nainstalovaná** — včetně všech tranzitivních závislostí:

```
numpy==2.3.3
matplotlib==3.10.8
contourpy==1.3.1   # závislost matplotlib
pillow==11.0.0     # závislost matplotlib
...
```

Proč to `uv` dělá?

- **Reprodukovatelnost.** Když pošleš projekt kolegovi, `uv sync` si přečte `uv.lock` a nainstaluje
  **úplně stejné verze**, jaké máš ty. Bez lockfile by ti `uv` mohl dát jinou minor verzi numpy než kolegovi
  — a pak se někde objeví tajemný rozdíl ve výsledcích.
- **Rychlost.** `uv sync` nemusí opakovaně řešit „která verze splňuje všechna omezení"; prostě čte
  výsledek z lockfile.

> **💡 Pravidlo:** `uv.lock` **také commituj do Gitu** (stejně jako `pyproject.toml`). Tím zaručíš,
> že každý, kdo projekt naklonuje, dostane bit-identické prostředí.

---

### 2.3 Další praktické příkazy

| Příkaz | K čemu |
|--------|--------|
| `uv add <balíček>` | Přidá balíček do `pyproject.toml` **a** nainstaluje ho. |
| `uv remove <balíček>` | Opak `uv add` — odebere balíček z `pyproject.toml` a odinstaluje. |
| `uv sync` | Nainstaluje přesně to, co je v `uv.lock`. Používáš **po klonování** nebo **po `git pull`**, pokud se změnily závislosti. |
| `uv run <příkaz>` | Spustí příkaz uvnitř virtuálního prostředí projektu. Např. `uv run python main.py`, `uv run jupyter notebook`. |
| `uv tree` | Zobrazí strom závislostí — uvidíš, co kterou knihovnu drží v projektu. |

**Ukázka `uv tree`:**

```
moje-analyza v0.1.0
├── jupyter v1.1.1
│   ├── ipykernel v6.29.5
│   │   ├── ipython v8.30.0
│   │   └── ...
│   └── ...
├── matplotlib v3.10.8
│   ├── contourpy v1.3.1
│   ├── pillow v11.0.0
│   └── ...
└── numpy v2.3.3
```

Hned vidíš, že `pillow` (obrázková knihovna) se dostala do projektu **jako tranzitivní závislost
matplotlibu** — sám sis ji nepřidal. Právě takové závislosti potřebuje `uv.lock` „uzamknout",
aby je u kolegy nainstaloval ve stejné verzi.

---

### 2.4 Vývojové závislosti (`--dev`)

Některé balíčky potřebuješ **jen při vývoji**, ne za běhu. Typicky testovací framework (`pytest`),
linter (`ruff`), formátovač (`black`). Uživatel, který tvůj projekt jen používá, je instalovat nemusí.
`uv` na to má přepínač `--dev`:

```bash
uv add --dev pytest ruff
```

V `pyproject.toml` se místo do `dependencies` dopíšou zvlášť do skupiny `dev`:

```toml
[dependency-groups]
dev = ["pytest>=8.0", "ruff>=0.6"]
```

`uv sync` ve výchozím nastavení instaluje i `dev` závislosti. Pokud chceš jen produkční sadu
(třeba při nasazení), použij `uv sync --no-dev`.

---

### 2.5 Globální nástroje (`uv tool`, `uvx`)

Občas chceš použít **CLI nástroj** (formátovač, linter), který **nepatří k jednomu projektu** —
chceš ho mít dostupný všude. Na to `uv` nabízí samostatný mechanismus, oddělený od projektových závislostí.

**`uvx <nástroj>` — jednorázové spuštění bez instalace:**

```bash
uvx ruff check .        # spustí linter ruff v aktuálním adresáři
uvx cowsay "Ahoj"       # funguje i na zábavné věci
```

`uv` nástroj stáhne, spustí jednou a zahodí. Ideální pro rychlé vyzkoušení nebo nástroj,
který používáš jednou za čas.

**`uv tool install <nástroj>` — trvalá globální instalace:**

```bash
uv tool install ruff
ruff check .            # už stačí volat jen ruff
uv tool list            # ukáže všechny globálně nainstalované nástroje
uv tool uninstall ruff  # odinstalace
```

**Rozdíl proti `uv add`:**

| `uv add numpy` | `uv tool install ruff` |
|----------------|------------------------|
| Přidá do **projektu** (zapíše do `pyproject.toml`) | Nainstaluje **globálně** pro tvého uživatele |
| Dostupné jen `uv run python …` v projektu | Dostupné jako příkaz odkudkoliv v terminálu |
| Vhodné pro knihovny (`numpy`, `matplotlib`) | Vhodné pro CLI nástroje (`ruff`, `black`, `httpie`) |

Projektový a nástrojový prostor jsou **striktně oddělené** a nepletou se — což je proti klasickému
`pip install -g` (globální pip) velká výhoda.

---

### 2.6 Verze Pythonu (`uv python`)

`uv` umí spravovat i **samotné verze Pythonu** — nemusíš je instalovat přes installer z python.org:

```bash
uv python list            # ukáže všechny dostupné i nainstalované verze
uv python install 3.13    # stáhne a nainstaluje Python 3.13
uv python install 3.12    # můžeš mít i víc verzí vedle sebe
```

Když pak v projektu `pyproject.toml` obsahuje `requires-python = ">=3.13"`, `uv` si sám vybere
(a případně stáhne) správnou verzi při prvním `uv sync`. Pro studenta to znamená: **nemusíš
řešit „která verze Pythonu mi běží v terminálu"** — `uv` to dopočítá podle projektu.

---

### 2.7 Co **ne**commitovat

Složka **`.venv/`** obsahuje skutečně nainstalované balíčky (stovky MB dat). Do Gitu **nepatří** —
generuje se lokálně z `pyproject.toml` + `uv.lock`:

```
# .gitignore
.venv/
__pycache__/
```

> **💡 Shrnutí cíle:**
>
> - `pyproject.toml` + `uv.lock` → **commit do Gitu** (popis projektu + přesné verze)
> - `.venv/` → **`.gitignore`** (generuje se z prvních dvou příkazem `uv sync`)
> - **Projekt** (`uv add`) × **globální nástroje** (`uv tool install` / `uvx`) jsou oddělené světy
> - **Verze Pythonu** si `uv` stáhne sám (`uv python install`)
>
> Díky tomu je repozitář malý a každý, kdo ho naklonuje, dostane přesně stejné prostředí.

---

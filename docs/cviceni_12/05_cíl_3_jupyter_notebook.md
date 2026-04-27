# CVIČENÍ 12: JUPYTER, NUMPY, MATPLOTLIB

Algoritmizace a programování

## CÍL 3: JUPYTER NOTEBOOK

### Co je Jupyter Notebook?

Doteď jsi psal Python skripty – soubory `.py`, které spustíš a dostaneš výstup v terminálu. To funguje dobře
pro programy, které něco dělají. Ale pro **explorativní analýzu dat** je to nepraktické: chceš vidět výstup hned
po každém kroku, přidávat poznámky, měnit parametry a znovu spouštět jen kus kódu.

Přesně k tomu slouží **Jupyter Notebook** – soubor `.ipynb`, který kombinuje:

- **buňky s kódem** – spustíš je jednotlivě a výstup se zobrazí přímo pod nimi,
- **markdown buňky** – text, nadpisy, rovnice, obrázky přímo vedle kódu,
- **interaktivní výstup** – grafy, tabulky, hodnoty se zobrazí bez přepínání oken.

Výsledkem je **dokument, který je zároveň kód i jeho dokumentace** – vidíš přesně, jak jsi k výsledku došel. 
Proto jsou notebooky standardem ve vědeckém výpočetním prostředí, datové analýze i strojovém učení.

---

### IPython vs Python

Jupyter Notebook nespouští klasický Python interpret, ale **IPython** – vylepšený interaktivní Python.

|               | Klasický Python   | IPython / Jupyter                            |
|---------------|-------------------|----------------------------------------------|
| Spuštění      | celý soubor naráz | po jednotlivých buňkách                      |
| Výstup        | jen `print()`     | poslední výraz v buňce se vypíše automaticky |
| Vizualizace   | otevře nové okno  | grafy se zobrazí přímo v notebooku           |
| Nápověda      | `help(np.array)`  | `np.array?` nebo `np.array??`                |
| Shell příkazy | ne                | `!pip list`, `!ls`                           |

> **⚠️ Pozor:** Buňky **sdílí stav**. Proměnná vytvořená v buňce 1 je dostupná v buňce 5. Pokud buňku smažeš
> nebo spustíš v jiném pořadí, proměnná může stále existovat v paměti – a kód zdánlivě funguje, ale po restartu kernelu
> to spadne. Zvyk: před odevzdáním vždy spusť **Restart & Run All**.

---

### Instalace balíčků pomocí `uv`

Jupyter není součástí standardní instalace Pythonu — je to samostatný balíček, který musíš přidat do
svého projektu. Použij `uv` (ze cvičení 1 a Cíle 1):

```bash
# uvnitř složky tvého projektu
uv add jupyter numpy matplotlib
```

Tím se do `pyproject.toml` přidají tři balíčky najednou:

- **`jupyter`** — samotný Jupyter (klient, kernel, IPython),
- **`numpy`** — numerické výpočty (budeš potřebovat v dalším cíli),
- **`matplotlib`** — vykreslování grafů.

`uv` také zajistí, že se nainstalují do virtuálního prostředí projektu (`.venv/`), ne globálně.

> **💡 Kontrola:** V terminálu spusť `uv run jupyter --version` — měla by vypsat verze
> nainstalovaných komponent (jupyter-core, jupyter-client, notebook, …). Pokud ne, balíček
> se správně nepřidal.

---

### Jak spustit notebook v PyCharmu

1. Vytvoř nový soubor s příponou `.ipynb` (`File → New → Jupyter Notebook`).
2. PyCharm nabídne výběr kernelu – vyber Python interpret ze svého projektu (`.venv`), ve kterém jsi právě Jupyter
   nainstaloval.
3. Nahoře se zobrazí panel s tlačítky pro spouštění buněk.
4. Novou buňku přidáš klávesou `B` (below) nebo `A` (above) v příkazovém módu, nebo tlačítkem `+`.
5. Buňku spustíš `Shift+Enter` – spustí buňku a přejde na další.

> **Tip:** Pokud kernel nereaguje nebo dává divné výsledky, zkus `Kernel → Restart` (tlačítko ↺ v panelu). 
> Tím vymažeš celý stav paměti a začneš čistě.

> **💡 Spuštění z terminálu:** Jupyter umíš spustit i bez PyCharmu — `uv run jupyter notebook` otevře
> rozhraní v prohlížeči (typicky na `http://localhost:8888`). Hodí se, když chceš pracovat v editoru
> dle svého výběru nebo si notebook jen rychle prohlédnout.

---

### Google Colab

[Google Colab](https://colab.research.google.com/) je Jupyter Notebook běžící přímo v prohlížeči – nepotřebuješ nic instalovat, vše běží na Googlu.

| Výhody                             | Nevýhody                                     |
|------------------------------------|----------------------------------------------|
| Žádná instalace – funguje okamžitě | Pomalejší než lokální stroj                  |
| Zdarma přístup k GPU/TPU           | Session se odpojí po době nečinnosti         |
| Sdílení jako Google Doc            | Omezená RAM a disk                           |
| Předinstalované vědecké knihovny   | Data musíš nahrát nebo připojit Google Drive |

Pro toto cvičení budeme pracovat v PyCharmu, ale pro sdílení analýz nebo trénování modelů (kde potřebuješ GPU) 
je Colab skvělá volba.

---

### ÚKOL: První notebook

Vytvoř nový notebook `cviceni_12_uvod.ipynb` a projdi následující kroky:

**1. Markdown buňka – nadpis a popis**

Přidej markdown buňku (změň typ buňky z `Code` na `Markdown`) s nadpisem a krátkým popisem, co notebook dělá:

```markdown
# Moje první analýza

Tento notebook procvičuje práci s Jupyter Notebooky, numpy a matplotlib.
```

**2. Code buňky – IPython výhody**

Přidej code buňku a vyzkoušej automatický výstup (bez `print()`):

```python
# automatický výstup poslední hodnoty v buňce
jmeno = "Jupyter"
verze = 4.2
verze
```

**3. Nápověda stylem IPython**

```python
# zkus nápovědu – spusť a prohlédni si výstup
len?
```

**4. Shell příkaz přímo v notebooku**

```python
# vypiš balíčky nainstalované v projektu
!uv pip list
```

Vykřičník `!` řekne Jupyteru, že má zbytek řádku poslat shellu — ne Pythonu. Hodí se na rychlou
kontrolu prostředí, instalace balíčků (`!uv add pandas`) nebo třeba výpis souborů.

**5. Záměrné rozbití stavu**

- V buňce A nastav `x = 42`.
- V buňce B vypiš `print(x)` – funguje.
- Smaž buňku A.
- Spusť buňku B – stále funguje (proč?).
- Restartuj kernel (`Kernel → Restart`) a spusť znovu buňku B – co se stane?

> **Nápověda:** Toto cvičení ukazuje, proč je Restart & Run All tak důležitý.

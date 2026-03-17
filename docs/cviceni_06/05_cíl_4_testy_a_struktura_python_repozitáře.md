# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## CÍL 4: TESTY A STANDARDNÍ STRUKTURA PYTHON REPOZITÁŘE

Test v Pythonu je kód, který ověřuje, že funkce nebo část programu funguje správně.
Tedy že pro daný vstup vrací očekávaný výstup.

Testování je klíčová součást vývoje, protože ti pomáhá rychle zjistit, jestli se něco nerozbilo po úpravě kódu.
Dnes je testování standardní praxí a je to dovednost, kterou by měl znát každý programátor.

---

### 4.1 Proč jsou testy důležité v praxi

Bez testů:

- po úpravě nevíš, co jsi rozbil,
- chyby objevíš pozdě,
- opravy jsou pomalejší.

S testy:

- máš rychlou zpětnou vazbu,
- snadno odhalíš regresi,
- úpravy děláš jistěji.

> **📘 Co je regrese?** Regrese je situace, kdy nová změna rozbije staré funkční chování.

---

### 4.2 Základní pojmy v testování

- **test case**: konkrétní scénář s daným vstupem a očekávaným výstupem,
- **assertion**: výraz, který ověřuje, že výstup odpovídá očekávání (např. `assert function(input) == expected_output`),
- **test suite**: sada test cases pro ověření funkčnosti celé části kódu,
- **pass/fail**: výsledek testu, který říká, jestli test case prošel (pass) nebo ne (fail).

Praktický příklad test case:

- vstup: `radius_sum(2, 3)`
- očekávaný výstup: `5`
- assertion: `assert radius_sum(2, 3) == 5`

---

### 4.3 Návrh testovacích případů

U každé funkce testuj různé typy vstupů, abys pokryl různé scénáře:

1. **běžný případ** (typický vstup, např. dvě kružnice s dvěma průniky),
2. **hraniční případ** (např. dotyk kružnic),
3. **negativní případ** (např. bez průniku).

Pro `has_intersection(...)` to může být:

- `{"x": 0, "y": 0, "r": 2}` a `{"x": 0, "y": 3, "r": 1}` → 1 průnik,
- `{"x": 0, "y": 0, "r": 2}` a `{"x": 0, "y": 3, "r": 2}` → 2 průniky,
- `{"x": 2, "y": -1, "r": 1}` a `{"x": 1.2, "y": 5, "r": 3}` → 0 průniků.

---

### 4.4 Implementace testů v Pythonu s `pytest`

Testování v Pythonu pomocí knihovny pytest je velmi jednoduché. Základem je psát funkce, které obsahují `assert`
– tedy kontrolu, že výstup odpovídá očekávání.

Například pro funkci `radius_sum` můžeš napsat test case takto:

```python
from circles_stats import radius_sum


def test_radius_sum_basic():
    assert radius_sum(2, 3) == 5
```

U funkcí, které vrací více hodnot (např. slovník), testujeme jednotlivé části výsledku, například pro `has_intersection`:

```python
from circles_stats import has_intersection


def test_has_intersection_basic():
    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 0, "y": 3, "r": 1}

    result = has_intersection(circle_1, circle_2)

    assert result["intersects"] is True
    assert result["intersections_count"] == 1
```

Pokud chceš testovat více případů, můžeš použít `pytest.mark.parametrize` pro parametrizaci testů:

```python
import pytest
from circles_stats import has_intersection


@pytest.mark.parametrize(
    ("circle_1", "circle_2", "expected_intersects", "expected_count"),
    [
        ({"x": 0, "y": 0, "r": 2}, {"x": 0, "y": 3, "r": 1}, True, 1),
        ({"x": 0, "y": 0, "r": 2}, {"x": 0, "y": 3, "r": 2}, True, 2),
        ({"x": 2, "y": -1, "r": 1}, {"x": 1.2, "y": 5, "r": 3}, False, 0),
    ],
)
def test_has_intersection(circle_1, circle_2, expected_intersects, expected_count):
    result = has_intersection(circle_1, circle_2)

    assert result["intersects"] is expected_intersects
    assert result["intersections_count"] == expected_count
```

`@pytest.mark.parametrize(...)` znamená, že `pytest` spustí stejnou testovací funkci
opakovaně pro každý řádek vstupních dat. To je užitečné pro testování více scénářů bez duplikace kódu.

---

**Instalace a spuštění:**

```powershell
uv add pytest
uv run pytest
```

Co udělá `uv run pytest`:

- spustí všechny testy, které najde v aktuálním projektu,
- typicky ve složce `tests/` a v souborech pojmenovaných jako `test_*.py`.

Spuštění konkrétního souboru:

```powershell
uv run pytest tests/test_circles_stats.py
```

---

### 4.5 Pojmy: knihovna, balíček, repozitář

Než půjdeme na strukturu projektu, hodí se rozlišit tyto pojmy:

- **modul**: jeden `.py` soubor s funkcemi a třídami (např. `circles_stats.py`),
- **balíček**: složka s `__init__.py`, která může obsahovat více modulů (např. `circles_project`),
- **knihovna**: soubor modulů a balíčků pro konkrétní účel (např. `matplotlib` pro grafy),
- **balíček**: Python package - složka s `__init__.py`, která může obsahovat více modulů (např. `matplotlib.pyplot`),
- **repozitář**: místo, kde máš uložený celý svůj projekt, včetně kódu, testů, dokumentace a historie změn (např. na GitHubu).

Stručně:

- knihovna/balíček ti dává funkce, které používáš v programu,
- repozitář je místo, kde máš uložený celý svůj projekt.

---

### 4.6 Standardní struktura Python repozitáře

Minimum, které je dobré držet:

<pre>
project_name/
├─ README.md
├─ pyproject.toml
├─ .gitignore
├─ src/
│  └─ circles_project/
│     ├─ __init__.py
│     ├─ circles_stats.py
│     ├─ circles_intersection_draw.py
│     └─ circles_intersection.py
<span style="color:#8a8f98;">├─ docs/                      (volitelné)</span>
<span style="color:#8a8f98;">│  └─ index.md                (volitelné)</span>
└─ tests/
   └─ test_circles_stats.py
</pre>

Co kam patří:

- `src/...` → produkční kód,
- `tests/...` → testy,
- `README.md` → popis projektu, spuštění a rychlá orientace,
- `pyproject.toml` → závislosti a konfigurace.

---

### 4.7 Je potřeba `__init__.py`?

`__init__.py` je speciální soubor, který říká: „Tahle složka je Python balíček (package).“

Co je dobré vědět:

- může být úplně prázdný,
- často v něm jen sjednotíš importy nebo metadata balíčku,
- u začátečnických projektů ho typicky necháš prázdný.

Praktické pravidlo pro tento předmět:

- v balíčku pod `src/` ho nech (`src/circles_project/__init__.py`),
- v `tests/` ho většinou nepotřebuješ.

Technicky to bez `__init__.py` někdy funguje, ale explicitní varianta je čitelnější a stabilnější.

---

### 4.8 A co složka `docs/`?

Složka `docs/` je místo pro dokumentaci projektu.
Není to „kód aplikace“, ale texty, návody a vysvětlení pro uživatele nebo vývojáře.

Typicky se tam dává:

- popis architektury,
- podrobnější návody k použití,
- technické poznámky a obrázky.

`docs/` není povinná pro každý malý projekt.

Přidej ji, když:

- chceš psát delší dokumentaci,
- projekt má více uživatelů,
- chceš web dokumentaci (např. přes MkDocs).

U malého školního úkolu často stačí kvalitní `README.md`.

---

### 4.9 Poznámka k `README.md` a `docs/`: používej Markdown

`README.md` i stránky ve složce `docs/` jsou soubory v Markdownu (`.md`).
Markdown je jednoduchý značkovací jazyk pro formátování textu, který se dobře čte i bez vykreslení.

Ukázka jednoho malého Markdown souboru:

=== "Kód (Markdown)"
    ````markdown
    # Analýza EKG signálu

    Krátký přehled projektu pro cvičení 6.

    ## Co skript dělá

    - načte data z `ekg_signal.txt`,
    - spočítá min, max a průměr,
    - vykreslí signál přes `matplotlib`.

    ## Spuštění

    ```powershell
    uv run python .\use_signal_plot_ops.py
    ```

    ## Malý výpočet

    \[
    d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
    \]

    ![Malý náhled grafu](../assets/cviceni_06/maly_nahled.svg)

    Více informací je v [přehledu cvičení](./README.md).
    ````

=== "Vykreslení"
    # Analýza EKG signálu

    Krátký přehled projektu pro cvičení 6.

    ## Co skript dělá

    - načte data z `ekg_signal.txt`,
    - spočítá min, max a průměr,
    - vykreslí signál přes `matplotlib`.

    ## Spuštění

    ```powershell
    uv run python .\use_signal_plot_ops.py
    ```

    ## Malý výpočet

    \[
    d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
    \]

    ![Malý náhled grafu](../assets/cviceni_06/maly_nahled.svg)

    Více informací je v [přehledu cvičení](./README.md).


> **Tip:** Když něco popisuješ, drž text stručný a akční. Začátečník by měl po přečtení hned vědět, co má udělat.
 
---

### 4.10 Změna importů pro testy

Pokud změníš strukturu projektu, přesuneš kód do `src/circles_project/` a testy dáš do `tests/`, budeš muset upravit 
importy v testech, aby odpovídaly nové struktuře.

Například místo:

```python
from circles_stats import radius_sum
```
budeš mít:

```python
from circles_project.circles_stats import radius_sum
```

Před spuštěním testů s `pytest` bude nutné balíček nainstalovat do prostředí, aby `pytest` věděl, kde hledat moduly. 
Balíček nainstaluj v kořeni projektu pomocí:

```powershell
uv pip install -e .
```
To vytvoří tzv. „editable install“, což znamená, že `pytest` bude hledat kód přímo v `src/` a nebudeš muset znovu instalovat po každé změně.

Teď můžeš spustit testy a měly by fungovat s novou strukturou:

```powershell
uv run pytest
```

---

#### ÚKOL: Praktický návrh testů a struktury

1. Navrhni strukturu repozitáře pro projekt s kružnicemi.
2. Napiš 5 test cases pro `has_intersection`:

    - 2 běžné,
    - 2 hraniční,
    - 1 negativní.

3. Přidej ještě 1 samostatný test case pro `radius_sum`.

4. U každého test case napiš:

    - vstup,
    - očekávaný výstup,
    - proč je důležitý.

5. Vytvoř `README.md` k projektu a napiš do něj:

    - co projekt dělá,
    - jak projekt spustit,
    - jak spustit testy.

**💻 Zkus:** Schválně nastav špatný *expected output* u jednoho testu a trénuj čtení neúspěšného testu, abys věděl, jak rychle najít problém.

#### ÚKOL: Nahraj projekt na GitHub

1. Na GitHubu vytvoř nový repozitář a nastav:

    - `Repository name`: stejný název jako má tvoje lokální složka projektu,
    - `Visibility`: `Public` (pokud zadání nevyžaduje `Private`),
    - nezaškrtávej `Add a README file`, `.gitignore` ani `Choose a license` (tyhle soubory už máš lokálně).

2. V kořeni projektu nejdřív ověř, jestli už existuje `.git`
   (`uv` projekt ji automaticky vytvoří, jinak by bylo potřeba nejdřív zavolat `git init`):

    ```powershell
    git status
    ```

3. Pokud `git status` funguje, pokračuj takto:

    ```powershell
    git add .
    git commit -m "Initial project structure, tests and README"
    git branch -M main
    git remote add origin <URL_TVEHO_REPOZITARE>
    git push -u origin main
    ```

4. Ověř na GitHubu, že se nahrály minimálně složky `src/`, `tests/` a soubor `README.md`.

5. Další změny nahrávej přes běžný cyklus:

    - `git add .`
    - `git commit -m "popis změny"`
    - `git push`

---

<h2 style="color:#c62828;">❗❗ POVINNÉ ODEVZDÁNÍ</h2>
<ul style="color:#c62828;">
  <li>Pro splnění cvičení je nezbytné odevzdat do e-learningu funkční odkaz na repozitář.</li>
  <li>Správnost řešení nebude kontrolována, ale odevzdání úkolu je povinné a projekt musí obsahovat alespoň základní rysy požadovaného řešení.</li>
  <li>Odevzdání a modifikace v repozitáři je nutné provést nejpozději do konce cvičení.</li>
  <li>Ověř, že repozitář je <code>Public</code> (jde otevřít i z anonymního okna prohlížeče).</li>
</ul>

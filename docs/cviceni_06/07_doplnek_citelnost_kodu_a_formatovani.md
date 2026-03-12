# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## DOPLNĚK: ČITELNOST KÓDU A FORMÁTOVÁNÍ

Formátování není kosmetika.
Je to praktický nástroj, který ti zrychlí čtení, ladění i opravy kódu.

Pro základní styl Pythonu vycházej z doporučení **PEP 8**:
https://peps.python.org/pep-0008/

V tomhle doplňku máš praktický výběr pravidel, která se vyplatí držet hned od začátku.

---

### Kdy rozdělit zápis do více řádků

Rozdělení do více řádků použij hlavně, když:

1. řádek je dlouhý a špatně čitelný,
2. máš více parametrů nebo položek,
3. chceš zvýraznit strukturu dat (co přesně vracíš/předáváš).

---

### 1) Funkce s více parametry

```python
def analyze_round_scores(
    scores,
    low_limit,
    high_limit,
    player="player",
    round_to=2,
    include_raw_scores=False,
):
    ...
```

---

### 2) Volání funkce s více argumenty

```python
result = analyze_round_scores(
    [1200, 980, 1430, 1600, 890],
    1000,
    1400,
    player="NinjaFox",
    round_to=1,
    include_raw_scores=True,
)
```

---

### 3) Delší seznamy

```python
scores = [
    1200,
    980,
    1430,
    1600,
    890,
]
```

---

### 4) Návrat více hodnot (`return (...)`)

```python
return (
    has_outliers,
    outlier_count,
    min_value,
    max_value,
    avg_value,
    summary_line,
    scores,
)
```

Tohle je dobrý standard, když vracíš víc položek.

> **💡 Poznámka k čárce na konci:** U víceřádkového zápisu nech i poslední položku s čárkou (`trailing comma`).
> Když potom přidáš další položku, v Gitu se obvykle změní jen jeden nový řádek.
> Review je přehlednější a bývá méně merge konfliktů.

---

### Standard prázdných řádků

1. **Mezi funkcemi nech 2 prázdné řádky** (na úrovni souboru).
2. **Uvnitř funkce odděluj logické bloky 1 prázdným řádkem**.
3. **Nedávej několik prázdných řádků za sebou** bez důvodu.
4. **Používej 4 mezery pro odsazení** (ne taby).

Tohle přímo odpovídá doporučením z PEP 8 a pomáhá držet konzistentní styl napříč projektem.

---

### Standard délky řádku (PEP 8)

1. **Kód drž ideálně do 79 znaků na řádek**.
2. **Komentáře a docstringy drž ideálně do 72 znaků na řádek**.
3. Když je řádek delší, zalamuj ho uvnitř závorek `()`, `[]`, `{}`.
4. Nepoužívej zalomení přes `\`, pokud to jde vyřešit závorkami.

Tohle je bezpečný základ, který ti pomůže udržet kód čitelný i v menším okně editoru.

Ukázka zalomení přes `\`:

```python
total = first_value + \
    second_value + \
    third_value
```

Stejný zápis je obvykle lepší psát přes závorky:

```python
total = (
    first_value
    + second_value
    + third_value
)
```

---

### Další důležité drobnosti

1. **Importy piš na začátek souboru**, ne doprostřed logiky.
2. **Neponechávej mezery na konci řádků** (trailing whitespace).
3. **Každý soubor ukonči jedním prázdným řádkem**.

---

### Dokumentační řetězec (Google format)

Docstring piš hned pod hlavičku funkce.
V Google formátu drž hlavně sekce `Args:` a `Returns:`.
Když funkce může padnout na chybě, přidej i `Raises:`.

```python
def compute_score_delta(score, baseline, multiplier=1.0, round_to=2):
    """Spočítá rozdíl skóre vůči baseline a aplikuje násobitel.

    Args:
        score (float): Aktuální hodnota skóre.
        baseline (float): Referenční hodnota, od které počítáš rozdíl.
        multiplier (float): Násobitel výsledného rozdílu.
        round_to (int): Počet desetinných míst pro zaokrouhlení.

    Returns:
        float: Zaokrouhlený rozdíl skóre.

    Raises:
        ValueError: Pokud je `round_to` záporné.
    """
    if round_to < 0:
        raise ValueError("round_to musí být >= 0")
    return round((score - baseline) * multiplier, round_to)
```

Co by měl docstring minimálně obsahovat:

1. Co funkce dělá (jedna stručná věta).
2. Jaké má vstupy (`Args`) a co znamenají.
3. Co vrací (`Returns`).
4. Jaké chyby může vyvolat (`Raises`), pokud je to relevantní.

> **💡 Tip:** Čitelnost kódu je týmová dovednost. Kód by měl být jasný i člověku, který ho čte poprvé.

---

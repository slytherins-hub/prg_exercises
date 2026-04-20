# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 5: TŘÍDA StudentsGrades

V této části aplikuješ právě probranou teorii OOP na konkrétní úlohu: evidenci výsledků testu. 
Napíšeš si třídu `StudentsGrades`, která drží výsledky studentů (jméno → body) a postupně do ní přidáš metody pro 
získání známky, vyhledávání a řazení.

### 5.1 Úloha

Dostals výsledky testu pro celou skupinu studentů — pro každého studenta máš jeho **jméno** a **počet bodů** v rozsahu 0–100. 
Body se podle následující tabulky převádí na písmennou známku (ECTS):

| Body   | Známka |
|--------|--------|
| 90–100 | A      |
| 80–89  | B      |
| 70–79  | C      |
| 60–69  | D      |
| 50–59  | E      |
| 0–49   | F      |

Potřebuješ nad daty dělat různé operace: získat body konkrétního studenta, spočítat počet studentů, zjistit písmennou
známku, najít studenty s určitým výsledkem a seřadit výsledky od nejhoršího po nejlepšího. Bez OOP bys každé funkci 
pořád dokola předával slovník `grades`. S třídou `StudentsGrades` si výsledky „pamatuje" samotný objekt.

> **Proč slovník a ne dva samostatné seznamy?** Kdybys držel jména v jednom seznamu a body v druhém, museli bys pořád
> hlídat, že jsou stejně dlouhé a že index 3 v jednom odpovídá indexu 3 v druhém. Slovník `{jméno: body}` má vazbu
> jméno–body přímo v sobě.

---

### 5.2 Připravený základ

Vytvoř si modul `student_grades.py` a zkopíruj do něj následující základ. Jde o minimální třídu — `__init__`
+ dvě jednoduché metody. Postupně si ji rozšíříš.

```python
class StudentsGrades:
    def __init__(self, grades=None):
        if grades is None:
            grades = {}
        self.grades = grades

    def get_score(self, name):
        return self.grades[name]

    def count(self):
        return len(self.grades)
```

Co která část dělá:

- **`__init__(self, grades=None)`** — při vytvoření objektu uloží předaný **slovník** `{jméno: body}` do atributu `self.grades`.
  Parametr `grades` je **nepovinný** — pokud ho nepředáš, objekt začne s prázdným slovníkem. Hodí se to, když 
  budeš chtít data doplnit později (třeba načtením ze souboru).
- **`get_score(self, name)`** — vrátí počet bodů studenta podle jména.
- **`count(self)`** — vrátí počet studentů (délku slovníku).

> **Proč `grades=None` a ne `grades={}`?** Použít prázdný slovník jako výchozí hodnotu parametru by v Pythonu byla
> chyba — **všechny objekty by sdílely tentýž slovník** (výchozí hodnota se vytvoří jen jednou, při definici funkce).
> Standardní postup je dát tam `None` a uvnitř funkce si prázdný slovník vyrobit znovu.

> **💡 Připomenutí konvence:** Třída je v `PascalCase` (`StudentsGrades`), zatímco soubor (`student_grades.py`),
> metody (`get_score`, `count`), atribut (`self.grades`) i budoucí instance (`results`) jsou v `snake_case`.

Vyzkoušej použití:

```python
results = StudentsGrades({
    "Ilona Funkce":   85,
    "Petr Metoda":    42,
    "Anna Trida":     91,
    "Jakub Modul":    67,
    "Eva Promenna":   50,
    "Tomas Seznam":   73,
    "Lucie Slovnik":  100,
    "Martin Cyklus":  38,
    "Katka Podminka": 58,
})

print(results.count())                      # 9
print(results.get_score("Anna Trida"))      # 91
print(results.grades)                       # celý slovník
```

Všimni si, že `grades` je **atribut** (čteš ho bez závorek), zatímco `count()` a `get_score()` jsou **metody** (volání se závorkami).

---

#### ÚKOL: Udělení známky - metoda `get_grade()`

Doplň do třídy metodu `get_grade()`, která vrátí **písmennou známku** studenta podle jeho jména.

1. Metoda má jeden parametr — `name` studenta.
2. Pomocí `self.grades[name]` (nebo `self.get_score(name)`) získej počet bodů.
3. Podle tabulky v úvodu vrať odpovídající písmeno (`"A"` až `"F"`).
4. Ověř z `main()`:

    ```python
    print(results.get_grade("Anna Trida"))     # A (91 bodů)
    print(results.get_grade("Lucie Slovnik"))  # A (100 bodů)
    print(results.get_grade("Martin Cyklus"))  # F (38 bodů)
    ```

> **Nápověda:** Použij `if` / `elif` / `else`. Na pořadí podmínek záleží — začni od nejvyššího rozsahu (90+) a postupuj dolů, nebo naopak.

---

#### ÚKOL: Vyhledávání studentů s konkrétním počtem bodů - metoda `find()`

Do třídy doplň metodu `find()`, která najde všechny studenty s **přesně** zadaným počtem bodů. Použiješ stejný princip
jako **sekvenční vyhledávání** z minulého cvičení — projdeš celý slovník a sesbíráš jména, u kterých sedí hledaná hodnota.

1. Metoda má jeden parametr — hledaný počet bodů.
2. Projdi `self.grades` a najdi **všechna jména**, kterým odpovídá hledaná hodnota.
3. Vrať seznam jmen. Pokud žádný student neodpovídá, vrať prázdný seznam.
4. Ověř z `main()`:

    ```python
    print(results.find(100))  # ['Lucie Slovnik']
    print(results.find(50))   # ['Eva Promenna']
    print(results.find(77))   # []
    ```

> **Nápověda:** Slovník můžeš procházet přes `for name, score in self.grades.items():` — v každém kroku máš k dispozici dvojici jméno + body.

---

#### ÚKOL: Seřazení výsledků - metoda `get_sorted()`

Do třídy doplň metodu `get_sorted()`, která vrátí **nový** seřazený seznam výsledků (vzestupně podle bodů). Každá položka
seznamu je dvojice `(jméno, body)`. Použij vlastní implementaci Bubble Sortu — **kód z funkce `bubble_sort()` v `sorting.py`
si do metody přímo zkopíruj** a uprav tak, aby řadil dvojice podle druhé hodnoty (počet bodů).

1. Metoda nemá žádný parametr (kromě `self`).
2. Na začátku si ze slovníku vyrob seznam dvojic: `items = list(self.grades.items())`. 
   Tím máš seznam typu `[("Ilona Funkce", 85), ("Petr Metoda", 42), ...]`, který můžeš řadit jako obyčejný seznam.
3. Do těla metody zkopíruj logiku Bubble Sortu a uprav porovnání — místo `items[j] > items[j+1]` porovnávej
   **body**, tedy `items[j][1] > items[j+1][1]`.
4. Vrať seřazený seznam dvojic.
5. Ověř z `main()`:

    ```python
    for name, score in results.get_sorted():
        print(name, score)
    # Martin Cyklus 38
    # Petr Metoda 42
    # Eva Promenna 50
    # ...
    # Lucie Slovnik 100
    ```

> **Poznámka:** Přímé zkopírování kódu z funkce do metody není ideální řešení — kód je pak napsaný dvakrát. 
> V praxi bys metodu nechal volat původní funkci. Teď ale chceme, abys viděl, že algoritmus **může** žít přímo 
> uvnitř objektu jako jeho metoda. K lepší organizaci kódu se ještě vrátíme.

---

#### ÚKOL: Demonstrace třídy

V hlavní funkci `main()` použij třídu `StudentsGrades` tak, aby předvedla všechny své metody:

1. Vytvoř objekt `results = StudentsGrades({...})` s devíti studenty z příkladu výše.
2. Vypiš, kolik studentů psalo test (využij `count()`).
3. V cyklu vypiš pro každého studenta jeho jméno, počet bodů a písmennou známku. Očekávaný výstup by měl vypadat třeba takto:

    ```
    Ilona Funkce         85 points - B
    Petr Metoda          42 points - F
    Anna Trida           91 points - A
    ...
    ```

    > **Tip:** Slovník můžeš procházet jednoduše přes `for name in results.grades:`.

4. Najdi a vypiš jména studentů, kteří měli plný počet bodů (100).
5. Vypiš seřazené výsledky od nejhoršího po nejlepšího (pomocí `get_sorted()`).
6. **Vyzkoušej třídu i na větších datech ze souboru.** Data nachystáš pomocí další metody třídy — 
   tu si naimplementuješ v následujícím úkolu.

---

#### ÚKOL: Načtení CSV - metoda `from_csv()`

Stáhni si soubor [`grades.csv`](../assets/cviceni_11/grades.csv) s výsledky celé třídy (50 studentů) a ulož ho vedle 
svých `.py` souborů. Soubor má dva sloupce oddělené čárkou — `name` a `score`:

```
name,score
Ilona Funkce,85
Petr Metoda,42
Anna Trida,91
...
```

Díky nepovinnému parametru v `__init__` už umíš vyrobit prázdný objekt — `results = StudentsGrades()`. 
Teď do něj doplníš metodu `from_csv(path)`, která výsledky **načte ze souboru a doplní je do `self.grades`**.

1. Do třídy `StudentsGrades` přidej metodu `from_csv(self, path)`:

    ```python
    def from_csv(self, path):
        # ... tady načti soubor a naplň self.grades ...
    ```

2. Uvnitř `from_csv()` otevři soubor, projdi ho řádek po řádku a naplň `self.grades`:

    - První řádek je hlavička (`name,score`) — přeskoč ho. Pomoz si `enumerate()` a podmínkou `if i == 0: continue`.
    - Každý další neprázdný řádek rozděl podle čárky: `name, score = line.split(",")`.
    - `score` je text z CSV, převeď ho na číslo pomocí `int(score)`.
    - Výsledek přidej do slovníku: `self.grades[name] = int(score)`.

3. Použij v `main()`:

    ```python
    big_results = StudentsGrades()
    big_results.from_csv("grades.csv")

    print(big_results.count())            # 50
    for name, score in big_results.get_sorted():
        print(name, score)
    ```

---

### 5.7 Bonusy (dobrovolné)

Pokud máš čas a chuť, rozšiř třídu o další metody. Každý bonus je samostatný úkol — můžeš si vybrat, které tě zaujmou.

#### Bonus 1: `average()`

Vrátí průměrné skóre skupiny. Hodí se `sum(self.grades.values())` a `len(self.grades)`.

---

#### Bonus 2: `best()` a `worst()`

Vrátí dvojici `(jméno, body)` nejlepšího a nejhoršího studenta. Nejjednodušší cesta je využít `get_sorted()`.

---

#### Bonus 3: `pass_rate()`

Vrátí podíl studentů, kteří **nedostali** F (tj. měli alespoň 50 bodů). Výstup je číslo v rozsahu 0.0 až 1.0.

---

#### Bonus 4: `__str__(self)`

Další **speciální metoda** jako `__init__`. Pokud ji definuješ, Python ji zavolá automaticky při `print(results)` 
a místo výchozího výstupu ve stylu `<__main__.StudentsGrades object at 0x00012a3...>` dostaneš tvůj vlastní 
čitelný text. Metoda musí vracet řetězec, například:

```python
def __str__(self):
    return f"StudentsGrades: {self.count()} students, average {self.average():.1f}"
```

Pak stačí napsat `print(results)` a Python se postará o zbytek.

---

#### Bonus 5: `plot_histogram()`

Vykreslí histogram rozdělení bodů pomocí `matplotlib`. Na malých datech (9 studentů) nemá histogram moc 
výpovědní hodnotu, ale na datech z `grades.csv` (50 studentů) už uvidíš pěkné rozložení.

Základní použití `plt.hist()` vypadá takhle:

```python
import matplotlib.pyplot as plt

values = [12, 15, 18, 22, 25, 27, 30, 31, 33, 35, 40, 45]
plt.hist(values, bins=5)
plt.show()
```

Parametr `bins` říká, kolik sloupců chceš — nebo místo čísla můžeš předat **seznam hranic** intervalů,
třeba `bins=[0, 10, 20, 30, 40, 50]`. Graf si pak doladíš barvou (`color=...`), okrajem sloupců
(`edgecolor="black"`), titulkem a popisky os.

Úkol pro tebe:

1. Doplň metodu `plot_histogram()`, která z `self.grades` vytáhne seznam bodů a zavolá nad ním `plt.hist()`.
2. Zvol vhodné `bins` tak, aby výsledný histogram ukazoval rozložení známek A–F.
3. Bonus: přepiš popisky osy X tak, aby místo čísel ukazovaly písmena `A`–`F` (podívej se na `plt.xticks()`).

---

# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 5: TŘÍDA StudentsGrades

V této části aplikuješ právě probranou teorii OOP na konkrétní úlohu: evidenci výsledků testu. 
Napíšeš si třídu `StudentsGrades`, která drží seznam bodů (0–100) a postupně do ní přidáš metody pro získání známky,
vyhledávání a řazení.

### 5.1 Úloha

Dostals výsledky testu pro celou skupinu studentů — pro každého jen počet bodů v rozsahu 0–100. Body se podle následující
tabulky převádí na písmennou známku (ECTS):

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
pořád dokola předával seznam `scores`. S třídou `StudentsGrades` si seznam „pamatuje" samotný objekt.

---

### 5.2 Připravený základ

Vytvoř si modul `student_grades.py` a zkopíruj do něj následující základ. Jde o minimální třídu — `__init__`
+ dvě jednoduché metody. Postupně si ji rozšíříš.

```python
class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)
```

Co která část dělá:

- **`__init__(self, scores)`** — při vytvoření objektu uloží předaný seznam bodů do atributu `self.scores`.
- **`get_by_index(self, index)`** — vrátí počet bodů studenta na zadané pozici.
- **`count(self)`** — vrátí počet studentů (délku seznamu).

> **💡 Připomenutí konvence:** Třída je v `PascalCase` (`StudentsGrades`), zatímco soubor (`student_grades.py`),
> metody (`get_by_index`, `count`), atribut (`self.scores`) i budoucí instance (`results`) jsou v `snake_case`.

Vyzkoušej použití:

```python
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
```

Všimni si, že `scores` je **atribut** (čteš ho bez závorek), zatímco `count()` a `get_by_index()` jsou **metody** (volání se závorkami).

---

#### ÚKOL: Udělení známky - metoda `get_grade()`

Doplň do třídy metodu `get_grade()`, která vrátí **písmennou známku** studenta podle jeho indexu.

1. Metoda má jeden parametr — `index` studenta.
2. Pomocí `self.scores[index]` (nebo `self.get_by_index(index)`) získej počet bodů.
3. Podle tabulky v úvodu vrať odpovídající písmeno (`"A"` až `"F"`).
4. Ověř z `main()`:

    ```python
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    ```

> **Nápověda:** Použij `if` / `elif` / `else`. Na pořadí podmínek záleží — začni od nejvyššího rozsahu (90+) a postupuj dolů, nebo naopak.

---

#### ÚKOL: Vyhledávání studentů s konkrétním počtem bodů - metoda `find()`

Do třídy doplň metodu `find()`, která najde všechny studenty s **přesně** zadaným počtem bodů. Použiješ stejný princip
jako **sekvenční vyhledávání** z minulého cvičení — projdeš celý seznam a sesbíráš pozice, na kterých sedí hledaná hodnota.

1. Metoda má jeden parametr — hledaný počet bodů.
2. Prohledej `self.scores` a najdi **všechny indexy**, na kterých se hledaná hodnota nachází.
3. Vrať seznam indexů. Pokud žádný student neodpovídá, vrať prázdný seznam.
4. Ověř z `main()`:

    ```python
    print(results.find(100))  # [6]
    print(results.find(50))   # [4]
    print(results.find(77))   # []
    ```

---

#### ÚKOL: Seřazení výsledků - metoda `get_sorted()`

Do třídy doplň metodu `get_sorted()`, která vrátí **nový** seřazený seznam bodů (vzestupně). Použij vlastní implementaci
Bubble Sortu — **kód z funkce `bubble_sort()` v `sorting.py` si do metody přímo zkopíruj** a uprav tak, aby pracoval se
`self.scores`.

1. Metoda nemá žádný parametr (kromě `self`).
2. Na začátku vytvoř lokální kopii seznamu, aby `self.scores` zůstalo beze změny — třeba `scores = list(self.scores)`, `scores = self.scores[:]` nebo `scores = self.scores.copy()`.
3. Do těla metody zkopíruj logiku Bubble Sortu a uprav ji tak, aby řadila proměnnou `scores` (místo parametru funkce).
4. Vrať seřazenou kopii.
5. Ověř z `main()`:

    ```python
    print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    ```

> **Poznámka:** Přímé zkopírování kódu z funkce do metody není ideální řešení — kód je pak napsaný dvakrát. 
> V praxi bys metodu nechal volat původní funkci (`return bubble_sort(self.scores)`). Teď ale chceme, abys viděl, 
> že algoritmus **může** žít přímo uvnitř objektu jako jeho metoda. K lepší organizaci kódu se ještě vrátíme.

---

#### ÚKOL: Demonstrace třídy

V hlavní funkci `main()` použij třídu `StudentsGrades` tak, aby předvedla všechny své metody:

1. Vytvoř objekt `results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])`.
2. Vypiš, kolik studentů psalo test (využij `count()`).
3. V cyklu vypiš pro každého studenta jeho pořadí (index), počet bodů a písmennou známku. Očekávaný výstup by měl vypadat třeba takto:

    ```
    Student 0: 85 points – B
    Student 1: 42 points – F
    Student 2: 91 points – A
    ...
    ```

4. Najdi a vypiš indexy studentů, kteří měli plný počet bodů (100).
5. Vypiš seřazené výsledky od nejhoršího po nejlepšího (pomocí `get_sorted()`).
6. **Vyzkoušej třídu i na náhodných datech.** Importuj si `random_numbers()` ze `sorting.py` a vytvoř druhý objekt:

    ```python
    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())
    ```

    Pusť `main()` víckrát — pokaždé dostaneš jinou skupinu a uvidíš, jak si třída poradí s různými daty.

---

### 5.7 Bonusy (dobrovolné)

Pokud máš čas a chuť, rozšiř třídu o další metody:

- **`average()`** — vrátí průměrné skóre skupiny.
- **`best()` a `worst()`** — vrátí nejvyšší a nejnižší skóre (hodí se využít `get_sorted()`).
- **`pass_rate()`** — vrátí podíl studentů, kteří **nedostali** F (tj. měli alespoň 50 bodů). Výstup v rozsahu 0.0 až 1.0.
- **`__str__(self)`** — další **speciální metoda** jako `__init__`. Pokud ji definuješ, Python ji zavolá automaticky 
  při `print(results)` a místo výchozího výstupu ve stylu `<__main__.StudentsGrades object at 0x00012a3...>` 
  dostaneš tvůj vlastní čitelný text. Metoda musí vracet řetězec, například:

  ```python
  def __str__(self):
      return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"
  ```
    
  Pak stačí napsat `print(vysledky)` a Python se postará o zbytek.

---

### 5.8 Bonus: `find_sorted()` s pamětí

Metoda `find()` pracuje v lineárním čase — prochází celý seznam. Kdybys dokázal nad **seřazeným** seznamem udělat
**binární vyhledávání** (z minulého cvičení), bude vyhledávání výrazně rychlejší: $O(\log n)$ místo $O(n)$.

Problém je, že řazení samotné trvá dlouho. Pokud budeš `find_sorted()` volat víckrát po sobě, nechceš data řadit pokaždé
znova. Trik je v tom, že si seřazenou verzi **jednou spočítáš a zapamatuješ** — při dalším volání ji jen použiješ.

#### ÚKOL: Implementace `find_sorted()` s cache

1. Do `__init__` přidej nový atribut pro cache:

    ```python
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None   # zatím nic neseřazené
    ```

2. Vytvoř metodu `find_sorted(score)`:

    - Pokud je cache prázdný (`self._sorted_scores is None`), **jednorázově** ho naplň:
      ```python
      self._sorted_scores = self.get_sorted()
      ```
    - Potom proveď **binární vyhledávání** nad `self._sorted_scores`. Kód binárního vyhledávání zkopíruj přímo do metody
      (stejně jako u `get_sorted`).
    - Vrať index v seřazeném seznamu, nebo `None`, pokud skóre neexistuje.

3. Abys viděl, že se řazení provede opravdu jen jednou, dej si na začátek if bloku třeba `print("sorting…")`. 
   Zavolej `find_sorted()` několikrát za sebou s různými skóre — hláška se objeví jen poprvé.

   ```python
   results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
   
   print(results.find_sorted(91))   # sorting…  → index 7
   print(results.find_sorted(50))   # → index 2 (už neřadí)
   print(results.find_sorted(77))   # → None  (77 tam není)
   ```

> **Poznámka — caching:** Tomuhle přístupu se říká **caching** (nebo **memoizace**) — výsledek drahého výpočtu si 
> zapamatuješ a příště ho jen vrátíš. Atribut `self._sorted_scores` začíná podtržítkem, což je v Pythonu konvence pro
> „vnitřní" atributy, které by vnější kód neměl přímo používat.

> **💡 Upozornění:** Cache platí jen dokud se `self.scores` nezmění. Pokud bys do třídy později přidal metodu, 
> která mění obsah `self.scores`, musela by taková metoda **invalidovat** cache — tedy nastavit 
> `self._sorted_scores = None` zpátky na prázdno. Jinak bys pracoval s neaktuálními seřazenými daty.

> **💡 Kdy co použít:** `find()` je rychlejší, když hledáš **jednorázově** nebo jen párkrát — netrpí tě s řazením. 
> `find_sorted()` s cache se vyplatí, když ve stejných datech hledáš **opakovaně** — jednorázová investice do řazení
> se vrátí na rychlosti všech dalších volání.

---

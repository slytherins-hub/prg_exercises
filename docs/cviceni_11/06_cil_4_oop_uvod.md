# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 4: OOP – TEORIE

Až dosud jsi pracoval hlavně s **funkcemi** — funkce dostala data jako argumenty, zpracovala je a vrátila výsledek.  
Objektově orientované programování (**OOP**) nabízí trochu jiný pohled: **data a operace nad nimi drží pohromadě v jednom objektu**.

### 4.1 Python je objektový jazyk

V Pythonu je úplně všechno objekt. Číslo `42` je objekt třídy `int`, řetězec `"ACGT"` je objekt třídy `str`, 
seznam `[1, 2, 3]` je objekt třídy `list`. Kdykoli voláš metodu, už s OOP pracuješ:

```python
text = "acgt"
text.upper()          # metoda upper() na objektu třídy str — vrátí "ACGT"

numbers = [1, 2, 3]
numbers.append(4)     # metoda append() na objektu třídy list — rozšíří seznam na [1, 2, 3, 4]
```

Stejné platí i pro knihovny. Abys externím knihovnám dobře rozuměl (a tušil, proč má `.sort()` závorky),
pomáhá vědět, co to vlastně objekt a metoda jsou.

---

### 4.2 K čemu je OOP dobré

Představ si, že chceš pracovat obdelníky, které představují pozemky. Pro každý obdelník chceš počítat jejich obsah, 
obvod a třeba i cenu za oplocení pozemku. **Bez OOP** bys pro každý obdélník potřeboval zvlášť šířku a výšku a každé
funkci je ručně předával:

```python
width_1 = 3
height_1 = 5
width_2 = 10
height_2 = 20
width_3 = 1
height_3 = 1

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def fencing_cost(width, height, price_per_meter):
    return perimeter(width, height) * price_per_meter

print(area(width_1, height_1))                 # 15
print(perimeter(width_2, height_2))            # 60
print(fencing_cost(width_3, height_3, 250))    # 1000
```

Funguje to. Ale s každým dalším obdélníkem přibývají proměnné (`width_4`, `height_4`, …) a šance na záměnu — pošleš
do `area()` šířku jednoho obdélníka a výšku druhého a máš hloupou chybu. A pokud bys k obdélníku chtěl přidat další 
informaci (třeba barvu), musíš projít všechny funkce a přidat další argument.

S **OOP** patří data a operace k sobě — do jedné třídy. Nejdřív se podíváme, jak taková třída vypadá:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter
```

Co z ní plyne v praxi? Data (`width`, `height`) jsou uložená přímo v objektu a metody k nim přistupují přes `self`.
Použití se tím dramaticky zjednoduší:

```python
r1 = Rectangle(3, 5)
r2 = Rectangle(10, 20)
r3 = Rectangle(1, 1)

print(r1.area())              # 15
print(r2.perimeter())         # 60
print(r3.fencing_cost(250))   # 1000
```

Všimni si dvou věcí:

- `area()` a `perimeter()` nemají žádné argumenty (kromě `self`) — všechno potřebné si objekt nese s sebou.
- `fencing_cost()` naopak argument má — **`price_per_meter`**. Metody můžou přijímat vstup úplně stejně jako normální funkce. 
  Navíc uvnitř volá `self.perimeter()`, takže využívá jinou metodu stejné třídy.

A pro víc obdélníků naráz:

```python
rectangles = [
    Rectangle(3, 5),
    Rectangle(10, 20),
    Rectangle(1, 1),
    Rectangle(7, 2),
    Rectangle(4, 8),
]

for rect in rectangles:
    print(rect.area())
```

---

### 4.3 Základní pojmy

| Pojem       | Vysvětlení                    | Příklad                        |
| ----------- | ----------------------------- | ------------------------------ |
| **třída**   | šablona pro vytváření objektů | `Rectangle`                    |
| **objekt**  | konkrétní instance třídy      | `r = Rectangle(3, 5)`          |
| **atribut** | hodnota uložená v objektu     | `r.width`, `r.height`          |
| **metoda**  | funkce patřící objektu        | `r.area()`, `r.fencing_cost()` |

> **Poznámka:** Třídu si můžeš představit jako formulář. Atributy jsou políčka formuláře (šířka, výška). 
> Objekt je jeden konkrétně vyplněný formulář. Metody jsou akce, které s vyplněným formulářem můžeš provést — spočítat
> obsah, spočítat obvod, spočítat cenu oplocení.

---

### 4.4 Rozbor třídy `Rectangle`

Vrať se na chvíli k definici třídy v předchozí sekci. Tři věci, kterých si hned všimni:

- Třída začíná klíčovým slovem **`class`** a názvem třídy.
- Metody jsou **odsazené** uvnitř třídy — jsou její součástí.
- Každá metoda má jako první parametr **`self`** — za chvíli vysvětlíme proč.

> **💡 Konvence pojmenování: `PascalCase` vs. `snake_case`.** V Pythonu se dodržují dvě hlavní konvence:
>
> - **`PascalCase`** (velké písmeno na začátku každého slova, bez mezer a podtržítek) — pro **třídy**: `Rectangle`, `HodnoceniStudentu`, `BiomedicalSignal`.
> - **`snake_case`** (malá písmena, slova oddělená podtržítkem) — pro všechno ostatní:
>     - **proměnné**: `my_list`, `price_per_meter`,
>     - **funkce**: `bubble_sort`, `random_numbers`,
>     - **objekty / instance**: `small_rect`, `big_rect`, `results`,
>     - **metody**: `get_by_index`, `area`, `fencing_cost`,
>     - **atributy**: `self.width`, `self.scores`.
>
> Díky těmto konvencím na první pohled poznáš, jestli pracuješ se třídou (velké začáteční písmeno), nebo s objektem / funkcí / proměnnou (malé).

---

### 4.5 Co je `__init__`

`__init__` je **speciální metoda** — Python ji zavolá automaticky pokaždé, když vytváříš nový objekt. 
Slouží k **inicializaci** objektu: nastaví jeho atributy na základě hodnot, které předáš při vytvoření.

Podívej se, co se stane při tomto řádku:

```python
r = Rectangle(3, 5)
```

Python udělá toto:

1. Vytvoří nový prázdný objekt třídy `Rectangle`.
2. Zavolá `__init__` a předá mu `width=3`, `height=5`.
3. `__init__` nastaví atributy objektu pomocí `self.width = 3` a `self.height = 5`.
4. Výsledný objekt uloží do proměnné `r`.

`__init__` tedy říká Pythonu, **jak objekt postavit** z předaných dat. Dvojité podtržítka (`__`) jsou Pythonova konvence
pro speciální metody — ty je jen definuješ, Python je volá sám.

---

### 4.6 Co je `self`

`self` je **odkaz na konkrétní objekt**, se kterým právě pracuješ. Díky `self` metoda ví, ke kterému objektu patří a ke kterým datům má přistupovat.

Zkus vytvořit dva různé objekty:

```python
small_rect = Rectangle(2, 3)
big_rect = Rectangle(10, 20)

print(small_rect.area())   # 6
print(big_rect.area())     # 200
```

Oba objekty sdílí **stejnou definici metody** `area()`, ale díky `self` každý pracuje se svými vlastními daty.

`self` se píše jako první parametr každé metody, ale při volání ho **nikdy nepředáváš** — Python ho doplní sám. 
Zápis `small_rect.area()` je zkratka za `Rectangle.area(small_rect)`.

Zjednodušeně: `self.width` = „šířka tohoto konkrétního obdélníka".

---

### 4.7 Atributy vs metody

- **Atributy** čteš **bez** závorek: `r.width`, `r.height`.
- **Metody** voláš **se** závorkami a případnými argumenty: `r.area()`, `r.perimeter()`, `r.fencing_cost(250)`.

> **Tip:** Závorky = voláš funkci/metodu. Bez závorek = čteš hodnotu. Když omylem napíšeš `r.area` bez závorek, 
> Python ti neukáže výsledek výpočtu, ale informaci o tom, že jde o metodu.

---

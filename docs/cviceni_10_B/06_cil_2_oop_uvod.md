# CVIČENÍ 10B: ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 2: OOP – TEORIE

Až dosud jsi pracoval hlavně s **funkcemi** — funkce dostala data jako argumenty, zpracovala je a vrátila výsledek. Objektově orientované programování (**OOP**) nabízí trochu jiný pohled: **data a operace nad nimi drží pohromadě v jednom objektu**.

### 4.1 Python je objektový jazyk

V Pythonu je úplně všechno objekt. Číslo `42` je objekt třídy `int`, řetězec `"ACGT"` je objekt třídy `str`, seznam `[1, 2, 3]` je objekt třídy `list`. Kdykoli voláš metodu, už s OOP pracuješ:

```python
"ACGT".upper()        # metoda upper() na objektu třídy str
[1, 2, 3].append(4)   # metoda append() na objektu třídy list
```

Stejné platí i pro knihovny. Abys externím knihovnám dobře rozuměl (a tušil, proč má `.append()` závorky a `.shape` nemá), pomáhá vědět, co to vlastně objekt a metoda jsou.

---

### 4.2 K čemu je OOP dobré

Představ si, že chceš pracovat s obdélníky — počítat jejich obsah, obvod a třeba i cenu za oplocení pozemku. **Bez OOP** bys pro každý obdélník potřeboval zvlášť šířku a výšku a každé funkci je ručně předával:

```python
sirka_1 = 3
vyska_1 = 5
sirka_2 = 10
vyska_2 = 20
sirka_3 = 1
vyska_3 = 1

def obsah(sirka, vyska):
    return sirka * vyska

def obvod(sirka, vyska):
    return 2 * (sirka + vyska)

def oplocit(sirka, vyska, cena_za_metr):
    return obvod(sirka, vyska) * cena_za_metr

print(obsah(sirka_1, vyska_1))              # 15
print(obvod(sirka_2, vyska_2))              # 60
print(oplocit(sirka_3, vyska_3, 250))       # 1000
```

Funguje to. Ale s každým dalším obdélníkem přibývají proměnné (`sirka_4`, `vyska_4`, …) a šance na záměnu — pošleš do `obsah()` šířku jednoho obdélníka a výšku druhého a máš hloupou chybu. A pokud bys k obdélníku chtěl přidat další informaci (třeba barvu), musíš projít všechny funkce a přidat další argument.

S **OOP** patří data a operace k sobě — do jedné třídy. Nejdřív se podíváme, jak taková třída vypadá:

```python
class Obdelnik:
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska

    def obsah(self):
        return self.sirka * self.vyska

    def obvod(self):
        return 2 * (self.sirka + self.vyska)

    def oplocit(self, cena_za_metr):
        return self.obvod() * cena_za_metr
```

Co z ní plyne v praxi? Data (`sirka`, `vyska`) jsou uložená přímo v objektu a metody k nim přistupují přes `self`. Použití se tím dramaticky zjednoduší:

```python
o1 = Obdelnik(3, 5)
o2 = Obdelnik(10, 20)
o3 = Obdelnik(1, 1)

print(o1.obsah())           # 15
print(o2.obvod())           # 60
print(o3.oplocit(250))      # 1000
```

Všimni si dvou věcí:

- `obsah()` a `obvod()` nemají žádné argumenty (kromě `self`) — všechno potřebné si objekt nese s sebou.
- `oplocit()` naopak argument má — **`cena_za_metr`**. Metody můžou přijímat vstup úplně stejně jako normální funkce. Navíc uvnitř volá `self.obvod()`, takže využívá jinou metodu stejné třídy.

A pro víc obdélníků naráz:

```python
obdelniky = [
    Obdelnik(3, 5),
    Obdelnik(10, 20),
    Obdelnik(1, 1),
    Obdelnik(7, 2),
    Obdelnik(4, 8),
]

for o in obdelniky:
    print(o.obsah())
```

Čistý kód, minimum šance na záměnu dat.

---

### 4.3 Základní pojmy

| Pojem | Vysvětlení | Příklad |
|-------|-----------|---------|
| **třída** | šablona (plán) pro vytváření objektů | `Obdelnik` |
| **objekt** | konkrétní instance třídy | `o = Obdelnik(3, 5)` |
| **atribut** | hodnota uložená v objektu | `o.sirka`, `o.vyska` |
| **metoda** | funkce patřící objektu, pracuje s jeho daty | `o.obsah()`, `o.oplocit(250)` |

> **💡 Poznámka:** Třídu si můžeš představit jako formulář. Atributy jsou políčka formuláře (šířka, výška). Objekt je jeden konkrétně vyplněný formulář. Metody jsou akce, které s vyplněným formulářem můžeš provést — spočítat obsah, spočítat obvod, spočítat cenu oplocení.

---

### 4.4 Rozbor třídy Obdelnik

Vrať se na chvíli k definici třídy v předchozí sekci. Tři věci, kterých si hned všimni:

- Třída začíná klíčovým slovem **`class`** a názvem třídy.
- Metody jsou **odsazené** uvnitř třídy — jsou její součástí.
- Každá metoda má jako první parametr **`self`** — za chvíli vysvětlíme proč.

> **💡 Konvence: PascalCase.** Názvy tříd se v Pythonu píšou v tzv. **PascalCase** — každé slovo začíná velkým písmenem a mezi slovy není mezera ani podtržítko: `Obdelnik`, `HodnoceniStudentu`, `BiomedicalSignal`. Proměnné a funkce naopak používají `snake_case` (`my_list`, `bubble_sort`, `cena_za_metr`). Je to zvyklost, kterou dodržuje celá Python komunita — pomáhá na první pohled poznat, že pracuješ se třídou.

---

### 4.5 Co je `__init__`

`__init__` je **speciální metoda** — Python ji zavolá automaticky pokaždé, když vytváříš nový objekt. Slouží k **inicializaci** objektu: nastaví jeho atributy na základě hodnot, které předáš při vytvoření.

Podívej se, co se stane při tomto řádku:

```python
o = Obdelnik(3, 5)
```

Python udělá toto:

1. Vytvoří nový prázdný objekt třídy `Obdelnik`.
2. Zavolá `__init__` a předá mu `sirka=3`, `vyska=5`.
3. `__init__` nastaví atributy objektu pomocí `self.sirka = 3` a `self.vyska = 5`.
4. Výsledný objekt uloží do proměnné `o`.

`__init__` tedy říká Pythonu, **jak objekt postavit** z předaných dat. Dvojité podtržítka (`__`) jsou Pythonova konvence pro speciální metody — ty je jen definuješ, Python je volá sám.

---

### 4.6 Co je `self`

`self` je **odkaz na konkrétní objekt**, se kterým právě pracuješ. Díky `self` metoda ví, ke kterému objektu patří a ke kterým datům má přistupovat.

Zkus vytvořit dva různé objekty:

```python
maly  = Obdelnik(2, 3)
velky = Obdelnik(10, 20)

print(maly.obsah())    # self = maly  → 6
print(velky.obsah())   # self = velky → 200
```

Oba objekty sdílí **stejnou definici metody** `obsah()`, ale díky `self` každý pracuje se svými vlastními daty.

`self` se píše jako první parametr každé metody, ale při volání ho **nikdy nepředáváš** — Python ho doplní sám. Zápis `maly.obsah()` je zkratka za `Obdelnik.obsah(maly)`.

Zjednodušeně: `self.sirka` = „šířka tohoto konkrétního obdélníka".

---

### 4.7 Atributy vs. metody

- **Atributy** čteš **bez** závorek: `o.sirka`, `o.vyska`.
- **Metody** voláš **se** závorkami a případnými argumenty: `o.obsah()`, `o.obvod()`, `o.oplocit(250)`.

> **💡 Tip:** Závorky = voláš funkci/metodu. Bez závorek = čteš hodnotu. Když omylem napíšeš `o.obsah` bez závorek, Python ti neukáže výsledek výpočtu, ale informaci o tom, že jde o metodu.

---

V další části si tohle všechno vyzkoušíš v praxi. Napíšeš si vlastní třídu `HodnoceniStudentu` pro evidenci bodů z testu a postupně do ní přidáš vyhledávání i řazení.

---

# CVIČENÍ 10: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## CÍL 3: MĚŘENÍ ČASU

V předchozích cílech jsi odhadoval asymptotickou složitost teoreticky. To je důležité, ale v praxi si často chceš ověřit i to, jak se algoritmus chová na reálných datech. V Pythonu můžeš dobu běhu programu měřit třeba pomocí modulu `time`.

Teoretická složitost a reálný čas běhu nejsou totéž:

- asymptotická složitost popisuje, jak rychle roste náročnost s velikostí vstupu,
- měření času ukazuje, jak se konkrétní implementace chová na konkrétním počítači.

Oba pohledy se dobře doplňují. Když je spojíš, uvidíš nejen to, **který algoritmus je lepší teoreticky**, ale i **kdy se ten rozdíl začne projevovat v praxi**.

### 3.1 Jak měřit smysluplně

Aby měření dávalo smysl, je dobré držet několik jednoduchých pravidel:

1. Porovnávej algoritmy na více velikostech vstupu, ne jen na jednom seznamu.
2. Pro každou velikost proveď více pokusů a výsledky zprůměruj.
3. Měř samotnou funkci, ne ruční vypisování do terminálu.
4. Dávej pozor, aby jsi srovnával srovnatelné situace.

U binárního vyhledávání je důležité si uvědomit, že funguje nad **seřazenými daty**. Pokud chceš porovnávat sekvenční a binární vyhledávání opravdu fér, musíš si ujasnit, co přesně měříš:

- jen samotné vyhledání hodnoty,
- nebo i cenu za předchozí seřazení dat.

Obě varianty dávají smysl, ale odpovídají na trochu jinou otázku.

Jako další zajímavé srovnání můžeš přidat i **vyhledávání v množině (`set`)**. To bývá v Pythonu velmi rychlé, protože množina je postavená na hashovací tabulce. Místo postupného procházení prvků se tedy typicky rovnou spočítá, kam se má hledaná hodnota zařadit.

> **💡 Poznámka:** Množina v Pythonu používá **hashovací tabulku**. To znamená, že se z hodnoty nejdřív spočítá její hash a podle něj se velmi rychle určí, kde se má prvek v tabulce hledat. U seznamu naproti tomu obvykle procházíš prvky jeden po druhém. Proto bývá `x in some_set` v průměru přibližně $O(1)$, zatímco `x in some_list` je typicky $O(n)$. Je to ale vykoupené **vyšší paměťovou náročností**, protože hashovací tabulka si musí držet rezervu a pomocnou strukturu pro rychlý přístup. Na $O(n)$ se hledání v množině může zhoršit v krajním případě tehdy, když vznikne hodně **kolizí**, tedy když mnoho různých hodnot padá do stejných míst tabulky a Python je pak musí rozlišovat postupně.

### 3.2 Měření pomocí `time.perf_counter()`

Pro jednoduché měření je vhodný například `time.perf_counter()`, protože nabízí jemnější rozlišení než běžný systémový čas.

Narazit můžeš i na základní funkci `time.time()`, která vrací aktuální čas. I s ní se dá doba běhu měřit, ale pro krátké úseky kódu bývá `time.perf_counter()` obvykle vhodnější.

Úplně jednoduchý ukázkový skript může vypadat třeba takto:

```python
import time

numbers = [4, 8, 15, 16, 23, 42, 55, 78, 91, 120]
target = 78

start = time.perf_counter()

for number in numbers:
	if number == target:
		break

end = time.perf_counter()

duration = end - start
print(f"Měření trvalo {duration:.8f} s")
```

Tady se prostě změří čas mezi začátkem a koncem vybraného bloku kódu. Je to nejjednodušší možný princip, na kterém si můžeš měření rychle vyzkoušet.

> **💡 Tip:** U velmi rychlých operací bývá jedno měření hodně krátké a kolísavé. Proto je při poctivějším experimentu lepší celý test několikrát zopakovat a výsledky zprůměrovat.

### 3.3 Uložení výsledků měření

Při experimentu se hodí ukládat si výsledky postupně do seznamů. Jeden seznam může obsahovat velikosti vstupu a další seznamy naměřené časy.

Například:

```python
sizes = [100, 500, 1000, 5000, 10000]
linear_times = []
binary_times = []
```

Pro každou velikost vstupu pak:

1. vygeneruješ data,
2. spustíš měření,
3. uložíš výsledek do odpovídajícího seznamu.

### 3.4 Vykreslení grafu pomocí `matplotlib`

Když máš výsledky uložené, můžeš je zobrazit do grafu. Pro podobné úlohy je velmi praktická knihovna `matplotlib`.

Pokud ji v prostředí ještě nemáš, nainstaluj ji přes:

```powershell
uv add matplotlib
```

Jednoduchý ukázkový graf může vypadat třeba takto:

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

plt.plot(sizes, times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()
```

Tohle je záměrně jen jeden jednoduchý příklad. Dál si ho upravíš podle toho, co budeš opravdu měřit a kolik různých algoritmů budeš chtít porovnat.

#### ÚKOL: Měření času běhu

1. Vytvoř si generátor vlastních sekvencí o různé délce, například `100`, `500`, `1000`, `5000` a `10000` prvků.
2. Případně do modulu `searching.py` importuj už připravené generátory z modulu `generators.py`, který je dostupný na e-learningu.
3. Porovnej sekvenční a binární vyhledávání.
4. Ulož si výsledky do seznamů podle velikosti vstupu.
5. Pomocí `matplotlib` vykresli graf závislosti času běhu na velikosti vstupu.
6. Do grafu přidej popisky os, legendu a smysluplný název.
7. Dobrovolně: Přidej do srovnání i test členství v množině (`set`) a porovnej, jak se chová vůči seznamu.
8. Krátce slovně okomentuj, jestli výsledky odpovídají teoretické asymptotické složitosti.
9. Dobrovolně: Pro každou velikost vstupu proveď více měření stejné funkce a spočítej průměrný čas běhu.

> **💡 Tip:** U velmi krátkých seznamů může být rozdíl mezi algoritmy téměř neviditelný. Zajímavější výsledky často dostaneš až u větších vstupů.

> **💡 Tip:** Pokud jsou výsledky hodně „roztřesené“, zvyš počet opakování pro jednu velikost vstupu.

> **⚠️ Pozor:** Měření doby běhu kódu ovlivňují i další procesy systému. Neber proto jednotlivá čísla jako absolutní pravdu, ale spíš jako přibližné srovnání trendů.

---
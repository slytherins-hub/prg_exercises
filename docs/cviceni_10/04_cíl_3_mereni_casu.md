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

### 3.2 Měření pomocí `time.perf_counter()`

Pro jednoduché měření je vhodný například `time.perf_counter()`, protože nabízí jemnější rozlišení než běžný systémový čas.

Ukázka jednoduché pomocné funkce:

```python
import time


def measure_call(function, *args, repeats=20):
	durations = []

	for _ in range(repeats):
		start = time.perf_counter()
		function(*args)
		end = time.perf_counter()
		durations.append(end - start)

	return sum(durations) / len(durations)
```

Taková funkce vrátí průměrný čas jednoho volání. U velmi rychlých funkcí budou výsledky často vycházet v řádu mikrosekund nebo milisekund, což je v pořádku.

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

Jednoduchý příklad vykreslení závislosti času běhu na velikosti vstupu:

```python
import matplotlib.pyplot as plt

plt.plot(sizes, linear_times, marker="o", label="Sekvenční vyhledávání")
plt.plot(sizes, binary_times, marker="s", label="Binární vyhledávání")

plt.xlabel("Velikost vstupu")
plt.ylabel("Průměrný čas [s]")
plt.title("Porovnání doby běhu algoritmů vyhledávání")
plt.legend()
plt.grid(True)
plt.show()
```

Z grafu pak můžeš lépe odhadnout, jak se jednotlivé algoritmy škálují s rostoucí velikostí vstupu.

#### ÚKOL: Měření času běhu

1. Vytvoř si generátor vlastních sekvencí o různé délce, například `100`, `500`, `1000`, `5000` a `10000` prvků.
2. Případně do modulu `searching.py` importuj už připravené generátory z modulu `generators.py`, který je dostupný na e-learningu.
3. Vyber si alespoň dva algoritmy, které chceš porovnat, například sekvenční a binární vyhledávání.
4. Pro každou velikost vstupu proveď více měření stejné funkce a spočítej průměrný čas běhu.
5. Ulož si výsledky do seznamů podle velikosti vstupu.
6. Pomocí `matplotlib` vykresli graf závislosti času běhu na velikosti vstupu.
7. Do grafu přidej popisky os, legendu a smysluplný název.
8. Krátce slovně okomentuj, jestli výsledky odpovídají teoretické asymptotické složitosti.

#### ÚKOL: Porovnání s a bez ceny za seřazení

Zkus porovnat dvě různé situace:

1. měříš pouze samotné binární vyhledávání nad už seřazenými daty,
2. měříš seřazení dat a až potom binární vyhledávání.

Na závěr napiš, ve které situaci dává binární vyhledávání největší smysl.

> **💡 Tip:** U velmi krátkých seznamů může být rozdíl mezi algoritmy téměř neviditelný. Zajímavější výsledky často dostaneš až u větších vstupů.

> **💡 Tip:** Pokud jsou výsledky hodně „roztřesené“, zvyš počet opakování pro jednu velikost vstupu.

> **⚠️ Pozor:** Měření doby běhu kódu ovlivňují i další procesy systému. Neber proto jednotlivá čísla jako absolutní pravdu, ale spíš jako přibližné srovnání trendů.

---
# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## CÍL 2: MODULY, IMPORTY A `__main__`

Jakmile máš víc funkcí, je lepší je rozdělit do více souborů.

---

### 2.1 Co je modul a co je skript

- **modul**: soubor s funkcemi, které chceš importovat jinde,
- **skript**: soubor, který primárně spouštíš.

---

### 2.2 Kompletní ukázka implementace

#### Krok 1: vytvoř modul `signal_ops.py`

```python
def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


if __name__ == "__main__":
    demo_values = [72, 75, 71, 89, 77]
    print("signal_min:", signal_min(demo_values))
    print("signal_max:", signal_max(demo_values))
    print("signal_avg:", round(signal_avg(demo_values), 2))
```

Tady je dole testovací volání přes `print(...)`, ne přes `assert`.

#### Krok 2: vytvoř skript `use_signal_ops.py`

```python
import signal_ops

values = [72, 75, 71, 89, 77]

print("MIN:", signal_ops.signal_min(values))
print("MAX:", signal_ops.signal_max(values))
print("AVG:", round(signal_ops.signal_avg(values), 2))
```

---

### 2.3 Různé styly importu

`import modul`

```python
import signal_ops
print(signal_ops.signal_min([1, 2, 3]))
```

`import modul as alias`

```python
import signal_ops as ops
print(ops.signal_max([1, 2, 3]))
```

`from modul import funkce`

```python
from signal_ops import signal_avg
print(signal_avg([1, 2, 3]))
```

`from modul import *`

```python
from signal_ops import *
print(signal_min([1, 2, 3]))
```

> **⚠️ Pozor:** `from modul import *` importuje všechna veřejná jména do aktuálního souboru.
>
> V běžném kódu to nepoužívej, protože:
> - zhorší čitelnost: nepoznáš, odkud která funkce přišla,
> - hrozí kolize názvů: dvě funkce se stejným jménem se můžou přepsat,
> - hůř se ladí chyby a hůř funguje našeptávání v editoru.

> **💡 Tip:**
>
> Kdy použít který styl:
>
> - `import modul` když používáš víc funkcí z modulu a chceš mít jasně vidět původ (`modul.funkce()`),
> - `import modul as alias` když má modul dlouhý název nebo ho voláš hodně často,
> - `from modul import funkce` když reálně používáš jen jednu (max pár) konkrétních funkcí.

---

### 2.4 K čemu je `if __name__ == "__main__":`

Každý Python soubor má speciální proměnnou `__name__`.

- když soubor spustíš přímo (`python soubor.py`), `__name__` je `"__main__"`,
- když soubor importuješ (`import soubor`), `__name__` je název modulu (např. `"signal_ops"`).

Důležité: při `import` se Pythonem projde celý soubor a vykoná se kód na nejvyšší úrovni
(to, co není uvnitř funkce/třídy).

Bez bloku `if __name__ == "__main__":` by se při importu spouštěly i testovací výpisy,
pomocný demo kód nebo dočasné experimenty.
To je problém, protože:

- import modulu má jen zpřístupnit funkce, ne spouštět vedlejší akce,
- při větším projektu by se ti při importu vypisoval nechtěný text.

Proč ten blok chceme v praxi:

- při přímém spuštění modulu si můžeš rychle otestovat funkce přes pár `print(...)`,
- při importu do jiného souboru se tyto testy nespustí.

Díky tomu máš jeden soubor, který jde pohodlně vyvíjet i znovu používat.

---

### 2.5 Built-in vs externí knihovny

V Pythonu skoro nikdy nepíšeš všechno od nuly. Používáš knihovny.

- **modul** = jeden `.py` soubor,
- **knihovna / balíček** = víc modulů dohromady pro jedno téma.

Proč knihovny v Pythonu používáme:

- šetří čas, protože používáš hotové funkce,
- používáš ověřený kód místo vlastních „rychlých“ řešení,
- kód je čitelnější a snáz se udržuje.

Odkud se knihovny „berou“:

- **built-in / standardní knihovna** je součást Pythonu (např. `math`, `random`, `pathlib`) a jen ji importuješ,
- **externí knihovny** vytváří komunita, firmy nebo vědecké týmy a instalují se zvlášť (typicky z PyPI),
- můžeš mít i **vlastní interní knihovny** v projektu.

Co s knihovnami reálně získáš:

- práci s čísly a statistikou,
- načítání a ukládání dat,
- grafy a vizualizace,
- komunikaci s webem/API,
- testování a automatizaci.

> **💡 Tip:** Síla Pythonu je hlavně v ekosystému knihoven, ne jen v „holém“ jazyce.

Instalace externí knihovny v tomto repu:

```powershell
uv add matplotlib
```

Ukázky importu `matplotlib.pyplot`:

`import matplotlib.pyplot as plt` (nejčastější varianta)

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [3, 1, 4])
plt.show()
```

`from matplotlib import pyplot as plt`

```python
from matplotlib import pyplot as plt

plt.plot([1, 2, 3], [3, 1, 4])
plt.show()
```

`import matplotlib.pyplot`

```python
import matplotlib.pyplot

matplotlib.pyplot.plot([1, 2, 3], [3, 1, 4])
matplotlib.pyplot.show()
```

> **💡 Tip:** V praxi nejčastěji používej `import matplotlib.pyplot as plt`.

---

**📝 ÚKOL: Udělej stejný pattern na vlastním modulu**

1. Vytvoř modul `signal_plot_ops.py` s funkcemi:

   - `load_signal_from_txt(path)`,
   - `signal_min(values)`,
   - `signal_max(values)`,
   - `signal_avg(values)`,
   - `plot_signal(values)`.

2. Použij přiložený soubor se signálem:

   - `ekg_signal.txt`
   - [Stáhni soubor `ekg_signal.txt`](../assets/cviceni_06/ekg_signal.txt)
   - ulož ho do stejné složky jako tvůj skript.

3. Ve funkci `load_signal_from_txt(path)` načti hodnoty z `.txt` souboru
   (jedna číselná hodnota na řádek) a vrať je jako `list[float]`.

4. Ve funkci `plot_signal(values)` použij `matplotlib.pyplot` a vykresli jednoduchý čárový graf signálu.

5. Na konec modulu dej testovací blok:

   - `if __name__ == "__main__":`

6. V testovacím bloku:

   - načti hodnoty přes `load_signal_from_txt(...)`,
   - vypiš minimum, maximum a průměr přes `print(...)`,
   - zavolej `plot_signal(...)`.

7. Vytvoř skript `use_signal_plot_ops.py`, který modul importuje a zavolá aspoň:

   - `load_signal_from_txt(...)`,
   - `signal_avg(...)`,
   - `plot_signal(...)`.

8. Spusť oba soubory a porovnej, co se stane:

   - při přímém spuštění modulu,
   - při spuštění skriptu s importem.

**💻 Zkus:** Dočasně dej jeden `print(...)` mimo `if __name__ == "__main__":` a ověř, proč je to při importu nevhodné.

---

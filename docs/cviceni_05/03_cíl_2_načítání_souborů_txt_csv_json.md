# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## CÍL 2: NAČÍTÁNÍ A ZAPISOVÁNÍ SOUBORŮ (TXT, CSV, JSON)

Při reálném použití program obvykle nepracuje jen s daty „natvrdo“ v kódu.  
Častý scénář je:

1. Načti vstupní data ze souboru.
2. Zpracuj je.
3. Ulož výsledek do dalšího souboru (report, přehled, export).

Přesně takhle vypadá běžná práce s daty v praxi.

**Testovací soubory ke stažení:**
- [lab_notes.txt](../assets/cviceni_05/cil_2_data/lab_notes.txt)
- [measurements.csv](../assets/cviceni_05/cil_2_data/measurements.csv)
- [dodavatel_alfa.csv](../assets/cviceni_05/cil_2_data/dodavatel_alfa.csv)
- [dodavatel_beta.csv](../assets/cviceni_05/cil_2_data/dodavatel_beta.csv)
- [dodavatel_gamma.csv](../assets/cviceni_05/cil_2_data/dodavatel_gamma.csv)
- [limits.json](../assets/cviceni_05/cil_2_data/limits.json)
- [Balíček všech souborů (.zip)](../assets/cviceni_05/cil_2_data/cil_2_data.zip)

Soubor(y) si dej do složky `data` vedle svého skriptu.

---

### 2.1 Proč je potřeba soubor otevřít (a proč `with open(...)`)?

Soubor je uložený na disku, zatímco program běží v paměti.  
Než může Python data číst nebo zapisovat, musí soubor otevřít přes `open(...)`.

Tím zároveň říkáš systému, že se souborem aktivně pracuješ. Podle režimu otevření pak systém může omezit souběžný zápis z jiného programu, aby se snížilo riziko kolizí a poškození dat.

Tím Pythonu řekneš:

- který soubor chceš použít,
- v jakém režimu (`r`, `w`, `a`),
- případně další volby otevření souboru.

V zápisu `with open("...", "režim") as file:` je `file` objekt souboru, přes který pak voláš `read()`, `write()` atd.

Používej právě `with open(...) as file`, protože se soubor po skončení bloku zavře automaticky.

Základní režimy:

- `r` = čtení,
- `w` = zápis od nuly (přepíše obsah),
- `a` = přidání na konec.
- `x` = vytvoří nový soubor, ale spadne, pokud už existuje.

Čtení:

```python
with open("data/notes.txt", "r") as file:
   content = file.read()
print(content)
```

Zápis:

```python
with open("data/report.txt", "w") as file:
   file.write("Pacient: P001\n")
   file.write("Tep: 78\n")
```

Přidání na konec:

```python
with open("data/report.txt", "a") as file:
   file.write("SpO2: 97\n")
```

> **Tip:** `with` po skončení bloku soubor automaticky zavře.

> **Poznámka:** Když pracuješ s češtinou nebo se znaky mimo ASCII, použij `encoding="utf-8"`.

> **Pozor:** Režim `w` smaže původní obsah souboru.

---

### 2.2 `read()`, `readline()`, `readlines()` - kdy co použít

`read()` načte celý soubor jako jeden řetězec:

```python
with open("data/lab_notes.txt", "r") as file:
   text = file.read()
print(text)
```

`readline()` načte jeden řádek:

```python
with open("data/lab_notes.txt", "r") as file:
   first_line = file.readline()
   second_line = file.readline()
print(first_line)
print(second_line)
```

`readlines()` načte všechny řádky do seznamu:

```python
with open("data/lab_notes.txt", "r") as file:
   lines = file.readlines()
print(lines)
```

Čtení po řádcích v cyklu (doporučené u větších souborů):

```python
with open("data/lab_notes.txt", "r") as file:
   for line in file:
      print(line)
```

Prakticky:

- malý soubor a chceš vše najednou -> `read()`,
- chceš číst postupně po řádcích (např. první N řádků) -> `readline()` (voláš opakovaně),
- chceš seznam řádků -> `readlines()`,
- větší soubor -> čti po řádcích v cyklu `for line in file`.

`file` si drží aktuální pozici (kurzor).  
Když jednou načteš celý soubor, jsi na konci a další čtení vrací prázdný výsledek.

---

### 2.3 Starší zápis bez context manageru

> **💡 Poznámka:**
>
> Starší zápis (jen pro orientaci):
>
> ```python
> file = open("data/notes.txt", "r")
> content = file.read()
> print(content)
> file.close()
> ```
>
> Dnes preferuj `with open(...)`, protože je bezpečnější a kratší. Tenhle styl je dnes už spíš „legacy“ (historický zápis) a když zapomeneš `close()`, můžeš si zadělat na problémy se souborem.

---

### 2.4 Cesty k souborům

Relativní cesta:

```python
with open("data/patients.txt", "r") as file:
   content = file.read()
```

Absolutní cesta:

```python
with open(r"D:\BPC-PRG\cviceni_05\data\patients.txt", "r") as file:
   content = file.read()
```

Ve Windows se používá `\`, ale v Python řetězcích má `\` speciální význam:

- `\n` = nový řádek,
- `\t` = tabulátor,
- `\"` = uvozovka uvnitř řetězce.

Takovým znakům se říká escape sekvence.  
Proto máš u cest tři bezpečné možnosti:

```python
path_1 = "data\\patients.txt"   # dvojité lomítko
path_2 = r"data\patients.txt"   # raw string = ber text doslova
path_3 = "data/patients.txt"    # dopředné lomítko
```

> **Pozor:** Raw string nesmí končit jedním `\` (např. `r"C:\data\"` je špatně).

---

### 2.5 `pathlib`: doporučený způsob práce s cestami

`pathlib` znamená: cesta není obyčejný text, ale objekt, se kterým se líp pracuje.

Nejdřív úplný základ:

- `Path("data")` = složka `data`,
- `Path("data") / "patients.txt"` = cesta k souboru ve složce `data`.

`/` tady není dělení, ale bezpečné skládání cesty.

Krok 1: vytvoř cestu a načti soubor.

```python
from pathlib import Path

file_path = Path("data") / "patients.txt"

with open(file_path, "r") as file:
   content = file.read()
print(content)
```

Krok 2: vytvoř složku a ulož výstup.

```python
from pathlib import Path

reports_dir = Path("data") / "reports"
reports_dir.mkdir(parents=True, exist_ok=True)

output_path = reports_dir / "summary.txt"
with open(output_path, "w") as file:
   file.write("Hotovo.\n")
```

Doporučení do praxe:

- používej relativní cesty v projektu,
- cesty skládej přes `Path(...) / "soubor.ext"`,
- soubory otevírej přes `with open(...) as file`.

**`glob`: jak najít více souborů najednou**

`glob` hledá soubory podle vzoru.

- `*.csv` = všechny CSV soubory v jedné složce,
- `dodavatel_*.csv` = všechny CSV soubory dodavatelů,
- `*.txt` = všechny TXT soubory v jedné složce.

```python
from pathlib import Path

for csv_path in Path("data").glob("dodavatel_*.csv"):
   print(csv_path.name)
```

> **💡 Tip:** Když chceš procházet i podsložky, použij `rglob("*.csv")`.

---

**ÚKOL: První práce se souborem**

1. Načti soubor `data/lab_notes.txt`.
2. Vypiš první dva řádky (použij `readline()`).
3. Znovu načti stejný soubor a spočítej počet neprázdných řádků.
4. Výsledek ulož do `data/notes_summary.txt`.

---

### 2.6 Formáty CSV a JSON

CSV se hodí, když máš tabulku:

- každý řádek je jeden záznam,
- sloupce mají stejnou strukturu,
- snadno se otevírá v Excelu nebo LibreOffice.

JSON se hodí, když ukládáš strukturovaná data:

- je to v podstatě slovník (případně seznam slovníků) uložený do souboru,
- hodí se na limity, konfiguraci a souhrnné výsledky,
- pro ukládání výsledků programu je JSON často optimální formát.

---

### 2.7 CSV: co nejjednodušeji přes `open(...)`

V tomhle cvičení budeme CSV brát jako obyčejný textový soubor, kde:

- každý řádek je jeden záznam,
- hodnoty v řádku bývají oddělené čárkou `,`.

Čtení CSV přes `open(...)`:

```python
with open("data/products_comma.csv", "r") as file:
   lines = file.readlines()

header = lines[0].strip().split(",")
rows = [line.strip().split(",") for line in lines[1:]]

print(header)
print(rows[0])
```

Když chceš s hodnotami dál počítat, převeď je na čísla:

```python
first_row = rows[0]
heart_rate = int(first_row[1])
spo2 = int(first_row[2])
print(heart_rate, spo2)
```

Jednoduchý zápis CSV přes `open(...)`:

```python
risk_rows = [
   ["id", "heart_rate", "spo2"],
   ["P003", "105", "92"],
   ["P005", "112", "91"],
]

with open("data/risk_patients.csv", "w") as file:
   for row in risk_rows:
   file.write(",".join(row) + "\n")
```

> **💡 Poznámka:** V praxi můžeš narazit i na jiné oddělovače. Teoreticky je TSV soubor oddělený tabulátorem (`\t`), ale soubory se středníkem `;` se často i tak pojmenovávají jako `.csv`. Princip zůstává stejný, jen změníš znak ve `split(...)` a `join(...)`.

---

### 2.8 JSON: slovník uložený v souboru

JSON si představ jako slovník uložený do textového souboru.

Načtení JSON:

```python
import json

with open("data/limits.json", "r") as file:
   limits = json.load(file)

print(limits)
print(type(limits))
```

`limits` je po načtení běžný Python `dict`, se kterým pracuješ normálně.

Zápis JSON:

```python
import json

summary = {
   "total_records": 5,
   "risk_records": 2,
   "limit_keys": ["heart_rate_min", "heart_rate_max", "spo2_min"],
}

with open("data/summary.json", "w") as file:
   json.dump(summary, file, indent=2)
```

Pro ukládání výsledků je JSON velmi praktický:

- zůstane struktura dat,
- výstup je čitelný pro člověka i program,
- snadno se znovu načítá přes `json.load(...)`.

---

**ÚKOL: Načti, zpracuj a ulož laboratorní data**

1. Stáhni si testovací soubory z odkazů na začátku této stránky a ulož je do složky `data`.
2. Načti `data/lab_notes.txt` a vytvoř seznam neprázdných řádků bez koncových znaků.
3. Načti `data/measurements.csv` přes `open(...)` a rozděl řádky pomocí `split(";")` (v tomhle úkolu ber data oddělená středníkem).
4. Zkontroluj počet datových řádků (bez hlavičky).
5. Načti `data/limits.json` a použij limity pro označení rizikových pacientů.
6. Ulož rizikové pacienty do `data/risk_patients.csv` přes `open(...)` se středníkem jako oddělovačem.
7. Ulož souhrn výsledků do `data/summary.json` (počty záznamů + použité limity).

---

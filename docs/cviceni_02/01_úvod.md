# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## ÚVOD

Vítejte u druhého cvičení! V minulé lekci jsme se naučili základy – instalaci prostředí, první programy, práci s proměnnými a řízení toku programu. Možná si říkáte: "Dobře, umím vypsat text. Ale k čemu mi je práce s textem v medicíně?"

Odpověď vás možná překvapí: **Téměř všechna data v medicíně začínají jako text nebo ho vyžadují ke zpracování.**

### Proč je práce s textem a datovými typy klíčová?

#### Text není jen "slova" – je to datová struktura

**Praktické využití v medicíně a bioinženýrství:**

- **Lékařské zprávy a databáze:** Jména pacientů, diagnózy (ICD-10 kódy), anamnézy
- **Bioinformatika:** DNA sekvence jsou řetězce (např. `"ACGTTAGC"`)
- **Elektronické zdravotní záznamy (EHR):** Zpracování strukturovaných i nestrukturovaných dat
- **Komunikace se zařízeními:** Příkazy pro diagnostické přístroje (často textové protokoly)
- **Analýza textů:** Natural Language Processing (NLP) pro automatickou analýzu lékařských zpráv

**Konkrétní příklady:**
```python
# Validace rodného čísla
birth_number = "9501152345"
is_valid = len(birth_number) == 10 and birth_number.isdigit()

# Normalizace jména pacienta
name = " NOVÁK Jan "
clean_name = name.strip().title() # "Novák Jan"

# Analýza DNA sekvence
dna = "ACGTTAGCTA"
gc_content = (dna.count("G") + dna.count("C")) / len(dna) * 100 # GC obsah v %

# Formátování výstupu z měřícího přístroje
temperature = 37.5
result = f"Teplota pacienta: {temperature:.1f} °C"
```

> **Klíčový poznatek:** Text nejsou jen "slova" – v programování je text **datová struktura**, se kterou musíme umět efektivně pracovat.

### Co jsou datové typy a proč na nich záleží?

Hodnota `120` v paměti může znamenat:

- **Systolický krevní tlak** (120 mmHg)
- **Tepová frekvence** (120 úderů/min)
- **Hladina glukózy** (120 mg/dL)
- **Číslo pacienta** (ID #120)
- **Text** (znak "x" v ASCII má kód 120)

Bez informace o **datovém typu** nevíme, jak data interpretovat!

Všechna data počítač ukládá jako **binární sekvence** (řady nul a jedniček), ale potřebuje vědět, **jak je interpretovat**.

**Datový typ** je **pravidlo**, které říká: "Tato sekvence bitů znamená *tohle*."

Počítač ukládá například sekvenci `01011001`. Co to může znamenat?

```python
# Jako celé číslo (int):
89

# Jako znak (str) v ASCII:
"Y"

# Jako barva pixelu (hodnota jasu 0–255):
Středně světlá šedá

# Jako True/False posloupnost bitů:
[False, True, False, True, True, False, False, True]
```

#### Binární soustava – jak počítač "myslí"

Zatímco my počítáme v desítkové soustavě (0–9), počítač používá pouze **0** a **1** (bity).

**Proč?** Elektronické obvody rozpoznají jen dva stavy: proud teče / neteče, napětí vysoké / nízké.

Každý bit představuje mocninu dvojky:

| Pozice | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---------------|-----|----|----|----|----|----|----|----|
| **Bit** | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| **Mocnina 2** | 2⁷ | 2⁶ | 2⁵ | 2⁴ | 2³ | 2² | 2¹ | 2⁰ |
| **Hodnota** | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

**Výpočet:** 0×128 + 1×64 + 0×32 + 1×16 + 1×8 + 0×4 + 0×2 + 1×1 = **64 + 16 + 8 + 1 = 89**

**8 bitů** = **1 byte** = dokáže uložit **256 různých hodnot** (0 až 255).

> **Vyzkoušej:**
> ```python
> print(bin(89)) # Převod čísla na binární: '0b1011001'
> print(int('1011001', 2)) # Zpět na číslo: 89
> ```

> **Proč je to užitečné v medicíně?** CT a MR snímky používají 8-bitové (256 odstínů šedi) nebo 16-bitové (65 536 odstínů) reprezentace – větší rozsah = vyšší detaily v obrazu.

#### Rozsah a přesnost – proč záleží na velikosti?

Čím více bitů, tím větší rozsah nebo přesnost:

| Datový typ | Počet bitů | Rozsah |
|--------------------|------------|---------------------------------|
| 8-bit int (byte) | 8 | 0 až 255 (nebo -128 až 127) |
| 16-bit int (short) | 16 | -32 768 až 32 767 |
| 32-bit int | 32 | -2,1 miliard až 2,1 miliard |
| 64-bit float | 64 | ±10³⁰⁸ (s desetinnou přesností) |

**Proč to řešit?**
Když zpracováváš miliony obrázků z CT skeneru, rozdíl mezi použitím 8-bitových a 32-bitových čísel může znamenat:

- **4× méně paměti** (1 GB vs. 4 GB)
- **Rychlejší výpočty** (méně dat = rychlejší zpracování)
- **Úspora nákladů** na cloudové úložiště

V datové vědě a AI je optimalizace klíčová – nemůžeš si dovolit plýtvat pamětí!

### Primitivní datové typy v Pythonu

Python je **dynamicky typovaný jazyk** – nemusíš předem říkat, jaký typ proměnná má.

**Co to znamená?** Python "uhádne" typ podle hodnoty:
```python
x = 42 # Python vidí: "Aha, celé číslo → int"
x = 3.14 # Python vidí: "Aha, desetinné číslo → float"
x = "ahoj" # Python vidí: "Aha, text → str"
```

To usnadňuje začátek, ale může vést k chybám, pokud nevíš, co děláš!

#### Základní typy

| Typ | Klíčové slovo | Rozsah | Příklad použití v medicíně |
|---------------------|---------------|------------------|----------------------------------------|
| **Celé číslo** | `int` | Prakticky ∞ | Počet pacientů, ID záznamu |
| **Desetinné číslo** | `float` | ±10³⁰⁸ | Teplota (37.5), tlak (120.5) |
| **Logická hodnota** | `bool` | `True` / `False` | Má pacient alergii? Je test pozitivní? |
| **Text** | `str` | ~1 milion znaků | Jméno pacienta, diagnóza, DNA sekvence |

```python
# Python automaticky určí typ
age = 25 # int
price = 19.99 # float
is_student = True # bool
name = "Alice" # str

# Ověření typu
print(type(age)) # <class 'int'>
print(isinstance(price, float)) # True
```

#### Python vs jiné jazyky

**Staticky typované jazyky** (C, Java, C++) vyžadují deklaraci typu:
```c
int age = 25; // Musíte říct, že "age" je int
float price = 19.99; // Musíte říct, že "price" je float
```

**Python** (dynamický):
```python
age = 25 # Automaticky int
age = "dvacet pět" # Teď je to str - žádná chyba!
```

**Výhoda Pythonu:** Rychlejší psaní kódu, jednodušší start.
**Nevýhoda:** Chyby typů se objeví až při běhu programu (ne při psaní).

**Příklad problému:**
```python
# Python ti to dovolí, ale výsledek může být nečekaný
age = "25" # Text, ne číslo!
next_year = age + 1 # ❌ CHYBA: TypeError: can only concatenate str to str

# Musíš explicitně převést
age = int("25") # Teď je to číslo
next_year = age + 1 # Funguje: 26
```

### Textové řetězce a Unicode

#### Proč Unicode?

V 80. letech minulého století každá země měla své vlastní kódování znaků:

- **ASCII** (USA) – 128 znaků (jen angličtina, bez háčků a čárek)
- **ISO-8859-2** (Česko) – 256 znaků (latinské jazyky)
- **Shift-JIS** (Japonsko) – tisíce znaků (hieroglyfy)

**Problém:** Když Čech poslal e-mail s "č" Američanovi, viděl nesmysl (`Ä`, `ř`...).

**Řešení:** **Unicode** (od 1991) – jeden standard pro **všechny jazyky světa**:

- Obsahuje 149 000+ znaků (latina, čínština, arabština, emoji...)
- Python ho používá nativně (od verze 3.0)
- Kódování **UTF-8**: každý znak zabírá 1–4 byty

```python
# Python umí všechny jazyky
text = "Hello 你好 مرحبا Привет 🐍"
print(len(text)) # 21 znaků (emoji = 1 znak!)

# Převod znaku na číslo a zpět
print(ord("ž")) # 382 (pozice v Unicode)
print(chr(382)) # "ž"
```

**Praktické využití v medicíně a vědě:**

```python
# Speciální symboly v lékařských zprávách
symbols = "°C, µg/mL, ±2.5, α-helix, β-sheet, Δ (delta)"

# Matematické symboly
math = "∑ (suma), ∫ (integrál), √ (odmocnina), ∞ (nekonečno)"

# Chemické vzorce
chemistry = "H₂O, CO₂, Ca²⁺, Fe³⁺"

# DNA sekvence (IUPAC kódy)
dna = "ACGT (A=Adenin, C=Cytosin, G=Guanin, T=Thymin)"

print("Teplota pacienta: 37.5 °C")
print("Dávkování: 500 µg/mL")
print("Změna: ±2 %")
```

> **Vyzkoušej:**
> ```python
> # Najdi Unicode kódy těchto symbolů
> print(ord("°")) # Stupeň
> print(ord("µ")) # Mikro
> print(ord("±")) # Plus-mínus
> print(chr(8364)) # Jaký znak to je? (€)
> ```

#### Immutabilita – řetězce jsou nezměnitelné

**Důležité:** V Pythonu **nemůžete změnit řetězec**, jen vytvořit nový!

```python
name = "alice"
name.upper() # Vrátí "ALICE", ale nezmění původní!
print(name) # Stále "alice"

# Správně:
name = name.upper() # Přiřadíme novou hodnotu
print(name) # "ALICE"
```

**Analogie:** Řetězec je jako **tištěná kniha** – nemůžete přepsat slova, jen vytvořit novou verzi.

```python
# Zpracování záznamu pacienta
patient_id = "P12345"

# ❌ CHYBA - Řetězec se nezmění!
patient_id.replace("P", "ID")
print(patient_id) # Stále "P12345"

# SPRÁVNĚ - Přiřadit nový řetězec
patient_id = patient_id.replace("P", "ID")
print(patient_id) # "ID12345"

# Proto jsou metody bezpečné - nemění původní data
original_name = "JAN NOVÁK"
lowercase = original_name.lower() # "jan novák"
titlecase = original_name.title() # "Jan Novák"

# Originál zůstal nedotčený
print(original_name) # Stále "JAN NOVÁK"
```

### Self-check: Rozumíš textovýcm řetězcům a datovým typům?

Než se vrhneme na praktické příklady, zkontroluj porozumění:

| Otázka | Odpověď |
|------------------------------------------|----------------------------------------------------|
| Co je binární sekvence `10110010`? | Záleží na typu! Může být číslo 178, znak, barva... |
| Kolik hodnot dokáže uložit 1 byte? | 256 (od 0 do 255, nebo -128 až 127) |
| Je `"123"` číslo nebo text? | Text (str), protože je v uvozovkách |
| Co vrátí `"hello".upper()`? | `"HELLO"` (nový řetězec) |
| Změní `text.upper()` proměnnou `text`? | NE – řetězce jsou immutable |
| Proč Python používá Unicode místo ASCII? | Unicode umí všechny jazyky světa (150k znaků) |

> **Tip:** Pokud některé odpovědi nejsou jasné, vrať se k příslušné sekci a přečti ji znovu. Tyto základy jsou klíčové pro celý kurz!

---


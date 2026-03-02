# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE A SLOVNÍKY

Algoritmizace a programování

## CÍL 4: PROCVIČOVÁNÍ

---

#### ÚKOL 1: Hra – hádání čísla

Navrhni minihru pro hádání náhodného čísla v programu `guessing_game.py`.

1. Importuj modul `random` - na začátek programu přidej `import random`.
2. Vylosuj tajné číslo v rozsahu 1-20 pomocí `random.randint(1, 20)`.
3. Umožni uživateli hádat tak dlouho, dokud číslo netrefí.
4. Po každém tipu vypiš nápovědu:
   * `"Vyšší!"` když je tip nižší než tajné číslo,
   * `"Nižší!"` když je tip vyšší než tajné číslo.

5. Vstup ošetři pomocí `try/except ValueError`, aby program nespadl na nečíselném vstupu.
6. Po trefě vypiš správnou odpověď i počet pokusů.

**Tip:** Použij `while True` + `break` při úspěchu.

**Očekávaný výstup:**
```
Hádej číslo (1-20): abc
Zadej prosím celé číslo!
Hádej číslo (1-20): 10
Vyšší!
Hádej číslo (1-20): 15
Nižší!
Hádej číslo (1-20): 13
Správně! Uhádl jsi číslo 13 na 3. pokus.
```

---

### ÚKOL 2: Zpracování datového streamu

Vytvoř program `stream_analysis.py`.

1. Definuj funkci `process_stream()`, která:
   * Přijímá jeden parametr typu `list` obsahující čísla a speciální řetězce (`"null"` a `"error"`).
   * Funkce projde seznam postupně pomocí `while` a indexace:
     * Pokud je prvek `"null"`, přeskoč ho (neinkrementuj počet zpracovaných).
     * Pokud je prvek `"error"`, ihned přestaň zpracovávat a vrať dosavadní výsledky.
     * Pokud je prvek číslo, aktualizuj statistiky: počet kladných, počet záporných, součet všech.
   * Funkce vrátí hodnotu typu `dict`: `{"positive": int, "negative": int, "sum": int, "processed": int}` kde
     * `positive` — počet kladných čísel,
     * `negative` — počet záporných čísel,
     * `sum` — součet všech zpracovaných čísel,
     * `processed` — počet zpracovaných čísel (čísla, ne `"null"`).

2. Vytvoř seznam `data_stream`:
```python
data_stream = [0, 3, 10, "null", -5, 23, "null", -8, "error", 13, 0, 0]
```

3. Zavolej `process_stream(data_stream)` a vypiš výsledky.

**Očekávaný výstup:**
```
=== ANALÝZA DATOVÉHO STREAMU ===
Stream: [0, 3, 10, 'null', -5, 23, 'null', -8, 'error', 13, 0, 0]

Počet kladných čísel: 3
Počet záporných čísel: 1
Součet zpracovaných čísel: 23
Počet zpracovaných položek: 5
```

---

#### ÚKOL 3: Translace mRNA na aminokyselinovou sekvenci

Vytvoř program `dna_translation.py` pro analýzu a translaci mRNA sekvence.

1. Definuj funkci `build_genetic_code():
   * Funkce nemá žádný vstupní parametr.
   * Funkce vrátí hodnotu typu `dict` mapující kodony (tří znakové řetězce, např. `"AUG"`) na aminokyseliny (jednopísmenné nebo `"STOP"`).
   * Zahrň tyto kodony: `AUG → M`, `UUU → F`, `UUC → F`, `GCU → A`, `GCC → A`, `GAU → D`, `GAA → E`, `UGG → W`, `UAA → STOP`, `UAG → STOP`, `UGA → STOP`.

2. Definuj funkci `translate()`:
   * Funkce přijímá dva parametry:
     * RNA sekvence (typ `str`),
     * genetický kód (typ `dict`).
   * Funkce projde sekvenci po trojicích znaků (kodonech):
     * Pokud je poslední kodon kratší než 3 znaky, ignoruj ho.
     * Pokud kodon není v `genetic_code`, přeskoč ho a pokračuj.
     * Pokud je výsledek `"STOP"`, překlad se ihned zastaví (STOP se nevrací).
   * Funkce vrátí hodnotu typu `str` představující sekvenci jednopísmenných zkratek aminokyselin v pořadí překladu.

3. Definuje funkci `analyze_aa():
   * Funkce přijímá jeden parametr typu `str` představujícíc sekvenci aminokyselin.
   * Funkce vrátí hodnotu typu `dict` se statistikami o aminokyselinách. Klíče ve slovníku:
     * `"aa_count"` — počet aminokyselin v sekvenci,
     * `"contains_M"` — `True`/`False` (zda je přítomen methionin `"M"` v sekvenci),
     * `"A_count"` — počet alaninů `"A"` v sekvenci,
     * `"unique_aa"` — seznam všech unikátních aminokyselin.

4. Hlavní program:
   * Definuj RNA sekvenci: `rna_sequence = "AUGGCCUUUGAAUGGGAUGCUUUCGAAGCCGAUUGGUGAUAAUUCGCC"`
   * Zavolej `genetic_code = build_genetic_code()`.
   * Zavolej `aa_sequence = translate(rna_sequence, genetic_code)`.
   * Zavolej `stats = analyze(aa_sequence)`.
   * Vypíš výsledky v přehledném formátu.

**Očekávaný výstup:**
```
=== TRANSLACE mRNA NA AMINOKYSELINY ===
mRNA sekvence: AUGGCCUUUGAAUGGGAUGCUUUCGAAGCCGAUUGGUGAUAAUUCGCC
Sekvence aminokyselin: MAFEWDAFEADW

STATISTIKA:
Počet aminokyselin: 12
Obsahuje methionin (M): True
Počet alaninu (A): 3
Unikátní aminokyseliny: ['M', 'E', 'W', 'A', 'F', 'D']
```

---

# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE A SLOVNÍKY

Algoritmizace a programování

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou dobrovolné a slouží pro další procvičení navíc.

---

#### BONUS 1: Validační menu – vitální funkce

Cíl: bezpečně načítat a opakovaně validovat tři vitální funkce pacienta (teplota, tep, saturace).

Vytvoř program `bonus_vitals.py` s následujícími funkcemi:

1) Funkce `validate_range(name, min_val, max_val)`:

 * Vstupy:
   - `name` — popis hodnoty (řetězec, např. `"Teplota"`)
   - `min_val` — minimální povolená hodnota
   - `max_val` — maximální povolená hodnota

 * Výstup: vrátí validní hodnotu (číslo)

 * Chování:
   - V cyklu `while True` žádej uživatele o vstup: `"Zadej {name} ({min_val}-{max_val}): "`
   - Pokusí se vstup převést na číslo (`int` nebo `float`). Pokud převod selže, vypiš `"Neplatné číslo!"` a pokračuj
   - Pokud číslo není v rozsahu `[min_val, max_val]`, vypiš `"Hodnota musí být mezi {min_val} a {max_val}!"` a pokračuj
   - Jakmile je číslo validní, vrať ho a skonči cyklus

2) Funkce `collect_vitals()`:

 * Bez vstupních parametrů

 * Výstup: slovník s klíči `"temperature"`, `"heart_rate"`, `"saturation"`

 * Chování:
   - Zavolej `validate_range()` třikrát pro:
     - teplota: `"Teplota"`, 35.0, 42.0
     - tep: `"Tep"`, 40, 180
     - saturace: `"Saturace"`, 80, 100
   - Vrať slovník: `{"temperature": teplota, "heart_rate": tep, "saturation": saturace}`

3) Hlavní program (bez funkcí `main()`, jen přímý kód):

 * Zavolej `collect_vitals()` a ulož výsledek do proměnné
 * Vypíš naměřené hodnoty v pěkném formátu:
   ```
   === MĚŘENÉ VITÁLNÍ FUNKCE ===
   Teplota: 37.2 °C
   Tep: 72 bpm
   Saturace: 98 %
   ```

**Očekávaný průběh:**
```
Zadej Teplota (35.0-42.0): abc
Neplatné číslo!
Zadej Teplota (35.0-42.0): 37.2
Zadej Tep (40-180): 72
Zadej Saturace (80-100): 98

=== MĚŘENÉ VITÁLNÍ FUNKCE ===
Teplota: 37.2 °C
Tep: 72 bpm
Saturace: 98 %
```

---

#### BONUS 2: Správa účastníků přednášek na VŠ

Cíl: spravovat seznamy studentů na různých přednáškách a zjišťovat, kdo se zúčastnil více přednášek, pomocí **množin**.

Vytvoř program `bonus_lectures.py`:

**Data (připravená ve vnořeném seznamu):**

```python
lectures_data = [
    ("Programování", ["Petr", "Marie", "Jan", "Pavel"]),
    ("Matematika", ["Petr", "Anna"]),
    ("Fyzika", ["Marie", "Anna", "Pavel", "Karel", "Eva"]),
    ("Chemie", ["Petr", "Jan"])
]
```

Každá položka je tuple: `(název_přednášky, seznam_studentů)`

1) Funkce `load_lectures(lectures_data)`:

 * Vstup:
   - `lectures_data` — seznam tuples (název přednášky, seznam studentů)

 * Výstup: slovník přednášek ve formátu `{název_přednášky: set(studenti), ...}`

 * Chování:
   - Procházej `lectures_data` pomocí `for` cyklu
   - Každou položku rozlož na `(lecture_name, students)`
   - Vytvoř množinu ze seznamu studentů
   - Ulož do slovníku: `lectures[lecture_name] = set(students)`
   - Vrať hotový slovník

2) Funkce `show_statistics(lectures)`:

 * Vstup:
   - `lectures` — slovník přednášek (klíč = název, hodnota = množina studentů)

 * Výstup: nic (jen tiskne)

 * Chování:
   - Vypíš seznam všech přednášek a počet studentů na každé
   - Pomocí **množinových operací** zjistí a vypíše:
     - **Sjednocení** — kolik je celkem unikátních studentů? (všechny přednášky dohromady)
     - **Průnik** — kdo se zúčastnil všech přednášek?
     - **Rozdíly** — u každé přednášky: kdo chodil jen na tuto přednášku a nikam jinde?

3) Hlavní program:

 * Uprav `lectures_data` výše (nebo si stáhni data z připravené proměnné)
 * Zavolej `lectures = load_lectures(lectures_data)`
 * Zavolej `show_statistics(lectures)`

**Očekávaný výstup:**
```
=== STATISTIKA PŘEDNÁŠEK ===

Počet studentů na každé přednášce:
Programování: 4 studentů
Matematika: 2 studentů
Fyzika: 5 studentů
Chemie: 2 studentů

Všichni studenti (sjednocení): 8 (Petr, Marie, Jan, Pavel, Anna, Karel, Eva)

Studenti na všech přednáškách (průnik): Petr

Studenti pouze na jedné přednášce:
- Pouze na Programování: Marie, Jan
- Pouze na Matematika: Anna
- Pouze na Fyzika: Karel, Eva
- Pouze na Chemie: (žádný)
```

**Procvičovaná témata:**
- **seznamy a tuples** — práce s vnořenými daty
- **slovníky** — uložení přednášek a jejich účastníků
- **množiny** — průnik (všichni společně), sjednocení (kolik lidí celkem), rozdíl (koho vidíme jen u jedné přednášky)
- **for cykly** — iterace přes data
- **množinové operace** — `&` (průnik), `|` (sjednocení), `-` (rozdíl)

---


---




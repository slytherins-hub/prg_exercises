# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE A SLOVNÍKY

Algoritmizace a programování

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou dobrovolné a slouží pro další procvičení navíc.

---

#### BONUS 1: Validační menu – vitální funkce

Vytvoř program `bonus_vitals.py` s následujícími funkcemi, který bude bezpečně načítat a validovat vstupy pro vitální funkce pacienta (teplota, tep, saturace):

1. Funkce `validate_range(name, min_val, max_val)`:

  * Vstupy:
    - `name` — popis hodnoty (řetězec, např. `"Teplota"`)
    - `min_val` — minimální povolená hodnota
    - `max_val` — maximální povolená hodnota

  * Výstup: vrátí validní hodnotu (číslo)

  * Chování:
    - V cyklu `while True` žádej uživatele o vstup: `"Zadej {name} ({min_val}-{max_val}): "`.
    - Pokusí se vstup převést na číslo (`int` nebo `float`). Pokud převod selže, vypiš `"Neplatné číslo!"` a pokračuj.
    - Pokud číslo není v rozsahu `[min_val, max_val]`, vypiš `"Hodnota musí být mezi {min_val} a {max_val}!"` a pokračuj.
    - Jakmile je číslo validní, vrať ho a skonči cyklus.

2. Funkce `collect_vitals()`:

   * Bez vstupních parametrů

   * Výstup: slovník s klíči `"temperature"`, `"heart_rate"`, `"saturation"`

   * Chování:
     - Zavolej `validate_range()` třikrát pro:
       - teplota: `"Teplota"`, minimum: 35.0, maximum: 42.0,
       - tep: `"Tep"`, minimum: 40, maximum: 180,
       - saturace: `"Saturace"`, minimum: 80, maximum: 100.
     - Vrať slovník: `{"temperature": teplota, "heart_rate": tep, "saturation": saturace}`.

3. Hlavní program:

   * Zavolej `collect_vitals()` a ulož výsledek do proměnné.
   * Vypiš naměřené hodnoty v přehledném formátu:
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

#### BONUS 2: Statistika akcí v logu

Cíl: zpracovávat log akcí uživatele, počítat jejich výskyty a zastavit se na speciální značce.

Vytvoř program `bonus_log.py` s následujícími funkcemi, který bude analyzovat záznamy akcí a vypisovat statistiky:

1. Funkce `analyze_log(log)`:

   * Vs~~tupy:
     - `log` — seznam řetězců obsahující akce (např. `["login", "click", "logout", "error", "END"]`)

   * Výstup: tuple `(counts, processed)` kde:
     - `counts` — slovník počtů akcí (např. `{"login": 2, "click": 3, "logout": 1, "error": 1}`)
     - `processed` — celkový počet zpracovaných záznamů (do a včetně `"END"`)

   * Chování:
     - Procházej log pomocí `while` cyklu s indexem
     - Pro každou akci:
       - Pokud je `"END"`, zvyš počítadlo `processed`, vypiš `"Log zpracován."`, a ukonči cyklus.
       - Pokud je `"error"`, vypiš varování `"Varování: error zaznamenán!"`, ale stále ji počítej do `counts`.
       - Všechny ostatní akce jen přidej/zvyš počitadlo ve slovníku `counts`.~~

2. Funkce `find_most_common(counts)`:

   * Vstupy:
     - `counts` — slovník počtů akcí

   * Výstup: řetězec s názvem nejčastější akce a jejím počtem (např. `"click (3x)"`)

   * Chování:
     - Projdi slovník `counts` a najdi akci s nejvyšším počtem.
     - Vrať řetězec ve formátu: `"{action} ({count}x)"`.
     - Pokud je slovník prázdný, vrať `None`

3. Hlavní program:

   * Připrav data do proměnné `log`:
     ```python
     log = ["login", "click", "click", "logout", "login", "error", "click", "END", "login"]
     ```
   * Zavolej `counts, processed = analyze_log(log)`.
   * Zavolej `most_common = find_most_common(counts)`.
   * Vypíš výsledky v přehledném formátu.

**Očekávaný průběh:**
```
Varování: error zaznamenán!
Log zpracován.

=== STATISTIKA LOGU ===

Počet akcí:
- login: 2
- click: 3
- logout: 1
- error: 1

Nejčastější akce: click (3x)
Zpracováno záznamů: 8
```

---


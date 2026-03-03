# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE, MNOŽINY A SLOVNÍKY

Algoritmizace a programování

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou dobrovolné a slouží pro další procvičení navíc.

---

#### BONUS 1: Validační menu – vitální funkce

Vytvoř program `bonus_vitals.py` s následujícími funkcemi, který bude bezpečně načítat a validovat vstupy pro vitální funkce pacienta (teplota, tep, saturace):

1. Funkce `validate_range()`:
    * Funkce přijímá tři parametry:
        * popis hodnoty (typ `str`, např. `"Teplota"`),
        * minimální povolená hodnota (typ `int` nebo `float`),
        * maximální povolená hodnota (typ `int` nebo `float`).
    * Funkce bude v nekonečném cyklu:
        * žádet uživatele o vstup: `"Zadej {name} ({min_val}-{max_val}): "`.
        * Pokusí se vstup převést na číslo (`int` nebo `float`). Pokud převod selže, vypiš `"Neplatné číslo!"` a pokračuj.
        * Pokud číslo není v rozsahu `[min_val, max_val]`, vypiš `"Hodnota musí být mezi {min_val} a {max_val}!"` a pokračuj.
        * Jakmile je číslo validní, vrať ho a skonči cyklus.
    * Funkce vrátí validní hodnotu typu `int` nebo `float`.

2. Funkce `collect_vitals()`:
    * Funkce nemá žádný vstupní parametr.
    * Funkce zavolá `validate_range()` pro tři různé vitální funkce:
        * teplota: `"Teplota"`, minimum: 35.0, maximum: 42.0,
        * tep: `"Tep"`, minimum: 40, maximum: 180,
        * saturace: `"Saturace"`, minimum: 80, maximum: 100.
    * Funkce vrátí slovník s klíči `"temperature"`, `"heart_rate"`, `"saturation"` a jejich odpovídajícími validními hodnotami.

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

Vytvoř program `bonus_log.py` s následujícími funkcemi, který bude analyzovat záznamy akcí a vypisovat statistiky:

1. Funkce `analyze_log(log)`:
    * Funkce přijímá jeden parametr typu `list` obsahující řetězce představující akce (např. `"login"`, `"click"`, `"logout"`, `"error"`, a speciální akci `"END"`).
    * Funkce projde seznam pomocí `while` cyklu a indexace:
        * Pokud narazí na akci `"END"`, zvyš počítadlo zpracovaných záznamů, vypiš `"Log zpracován."`, a ukonči cyklus.
        * Pokud narazí na akci `"error"`, vypiš varování `"Varování: error zaznamenán!"`, ale stále ji počítej do statistik.
        * Pro všechny ostatní akce aktualizuj slovník počtů (`counts`) pro danou akci (zvyš počet o 1).
    * Funkce vrátí tuple `(counts, processed)` kde:
        * `counts` — slovník počtů akcí (např. `{"login": 2, "click": 3, "logout": 1, "error": 1}`)
        * `processed` — celkový počet zpracovaných záznamů (do a včetně `"END"`).

2. Funkce `find_most_common()`:
    * Funkce přijímá jeden parametr typu `dict` obsahující počty akcí (např. `{"login": 2, "click": 3, "logout": 1, "error": 1}`).
    * Funkce projde slovník a najde akci s nejvyšším počtem výskytů.
    * Funkce vrátí řetězec ve formátu: `"{action} ({count}x)"` kde `action` je název akce s nejvyšším počtem a `count` je její počet.
    * Pokud je slovník prázdný, vrať `None`.

3. Hlavní program:
    * Vytvoř proměnnou `log` obsahující seznam akcí:
      ```python
      log = ["login", "click", "click", "logout", "login", "error", "click", "END", "login"]
      ```
    * Zavolej `counts, processed = analyze_log(log)`.
    * Zavolej `most_common = find_most_common(counts)`.
    * Vypiš výsledky v přehledném formátu.

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


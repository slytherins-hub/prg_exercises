# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

### 1. Co je hlavní výhoda rozdělení programu do modulů?

- a) Python běží automaticky 2× rychleji
- b) Kód je přehlednější a znovupoužitelný
- c) Není potřeba psát funkce
- d) Nemusíš řešit importy

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Moduly zlepšují organizaci kódu a umožní znovupoužití funkcí.
</details>

### 2. Co udělá `if __name__ == "__main__":`?

- a) Spustí se vždy při importu modulu
- b) Spustí se jen při přímém spuštění souboru
- c) Zakáže import modulu
- d) Spustí testy z `pytest`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Blok se vykoná jen při přímém spuštění souboru.
</details>

### 3. Které volání správně míchá poziční a pojmenované argumenty?

- a) `compute_score_delta(score=1540, 1200, round_to=1)`
- b) `compute_score_delta(1540, baseline=1200, round_to=1)`
- c) `compute_score_delta(1540, 1200, score=1800)`
- d) `compute_score_delta(round_to=1, 1540, 1200)`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Poziční argumenty jdou nejdřív, pojmenované až za nimi.
</details>

### 4. Kdy je vhodné preferovat pojmenované argumenty?

- a) Když má funkce víc parametrů nebo default hodnoty
- b) Nikdy, vždy jen poziční
- c) Jen u funkcí bez parametrů
- d) Jen když používáš `pytest`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Volání je čitelnější a je jasné, co která hodnota znamená.
</details>

### 5. Jaké je doporučení pro globální proměnné v tomhle cvičení?

- a) Používat je co nejvíc, aby se nemusely předávat parametry
- b) Používat je hlavně pro konstanty
- c) Vždy je měnit přes `global`
- d) Používat jen v testech

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Pro měnitelná data je lepší předávání přes parametry a `return`.
</details>

### 6. Která varianta importu je obecně nejméně vhodná pro čitelnost?

- a) `import modul`
- b) `import modul as alias`
- c) `from modul import *`
- d) `from modul import jedna_funkce`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `from modul import *` zhoršuje přehled i ladění.
</details>

### 7. Jaká je doporučená reprezentace kružnice v Cíli 3?

- a) `[x, y, r]`
- b) `{"x": x, "y": y, "r": r}`
- c) `(x, y, r, color)`
- d) `"x,y,r"`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) V Cíli 3 se pracuje se slovníky s klíči `x`, `y`, `r`.
</details>

### 8. Co má vracet `has_intersection(...)`?

- a) Jen `bool` (`True/False`)
- b) Jen počet průniků jako `int`
- c) Slovník alespoň s klíči `is_intersection` a `intersections_count`
- d) Vždy `tuple` délky 2

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) V Cíli 3 je výstup funkce navržený jako slovník.
</details>

### 9. Proč je u desetinných výpočtů lepší tolerance (`isclose`) než ostré `==`?

- a) Protože `==` je v Pythonu zakázané
- b) Protože desetinná čísla mohou mít malé zaokrouhlovací odchylky
- c) Protože `isclose(...)` je vždy rychlejší
- d) Protože `isclose(...)` vrací text

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) U hraničních případů (např. dotyk kružnic) je tolerance spolehlivější.
</details>

### 10. Ve volitelné části 3.7: co znamená podmínka `d = |r_1 - r_2|`?

- a) Kružnice se neprotínají
- b) Kružnice mají dva průniky
- c) Kružnice mají jeden vnitřní dotyk
- d) Kružnice jsou totožné

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Jde o dotyk „zevnitř“.
</details>

### 11. Jaký je doporučený příkaz pro instalaci externí knihovny v tomhle repu?

- a) `pip install matplotlib`
- b) `python -m pip install matplotlib`
- c) `uv add matplotlib`
- d) `apt install matplotlib`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) V tomhle kurzu se používá `uv`.
</details>

### 12. Co udělá `uv run pytest`?

- a) Spustí všechny nalezené testy v projektu
- b) Spustí jen jeden test
- c) Jen vytvoří složku `tests/`
- d) Jen nainstaluje `pytest`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Typicky najde testy ve složce `tests/` a v souborech `test_*.py`.
</details>

### 13. Co nejlépe popisuje rozdíl „knihovna / balíček / repozitář“?

- a) Všechny tři pojmy znamenají totéž
- b) Knihovna a balíček jsou části kódu pro použití v programu, repozitář je celý verzovaný projekt
- c) Repozitář je jen složka `tests/`
- d) Balíček je vždy totéž co GitHub repozitář

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Repozitář obsahuje kód, testy, dokumentaci a historii změn.
</details>

### 14. Kde má být standardně testovací kód?

- a) Ve složce `tests/`
- b) Jen v `README.md`
- c) V `src/` mezi produkčním kódem
- d) Jen v CI na GitHubu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Oddělení `src/` a `tests/` zlepšuje přehlednost.
</details>

### 15. Co je pro splnění cvičení povinné?

- a) Odevzdat funkční odkaz na repozitář do e-learningu
- b) Mít 100% správné řešení bez jediné chyby
- c) Nepoužít vůbec žádné externí knihovny
- d) Odevzdat jen screenshot terminálu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Repozitář má být `Public` a odevzdání/modifikace proběhnou nejpozději do půlnoci v den cvičení.
</details>

---

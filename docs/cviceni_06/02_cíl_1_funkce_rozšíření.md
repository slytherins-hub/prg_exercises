# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## CÍL 1: FUNKCE – ROZŠÍŘENÍ A DOBRÉ NÁVYKY

---

### 1.1 Povinné a nepovinné parametry

Povinný parametr musíš vždy zadat při volání.
Nepovinný parametr má výchozí hodnotu.

```python
def average_value(values, round_to=2):
    return round(sum(values) / len(values), round_to)


print(average_value([1200, 980, 1430]))       # round_to=2
print(average_value([1200, 980, 1430], 1))    # round_to=1
```

> **⚠️ Pozor:** Nepovinné parametry patří v hlavičce až za povinné.

---

### 1.2 Poziční argumenty (positional)

Poziční argument se páruje podle pořadí:

```python
def convert_coins(value, from_currency, to_currency):
    if from_currency == "gold" and to_currency == "gems":
        return value / 100
    if from_currency == "gems" and to_currency == "gold":
        return value * 100
    return value


print(convert_coins(2500, "gold", "gems"))
```

Je to rychlé, ale u delších funkcí nemusí být hned jasné, co které číslo znamená.

---

### 1.3 Pojmenované argumenty (keyword)

U delších funkcí bývá čitelnější volání přes názvy parametrů:

```python
print(convert_coins(value=2500, from_currency="gold", to_currency="gems"))
```

Tohle se hodí hlavně při práci s default parametry.

---

### 1.4 Míchání pozičních a pojmenovaných argumentů

Míchat je můžeš, ale platí:

1. poziční argumenty musí být dřív,
2. stejný parametr nesmíš zadat 2x,
3. poziční argument za pojmenovaným je chyba.

Správně:

```python
def compute_score_delta(score, baseline, multiplier=1.0, round_to=2):
    return round((score - baseline) * multiplier, round_to)


print(compute_score_delta(1540, 1200, round_to=1))
print(compute_score_delta(1540, 1200, 0.5, round_to=3))
```

Špatně:

```python
# compute_score_delta(score=1540, 1200)         # SyntaxError
# compute_score_delta(1540, 1200, score=1800)   # TypeError
```

---

### 1.5 Kdy používat poziční vs pojmenované

Poziční argumenty používej hlavně když:

- máš 1-2 krátké vstupy,
- význam je zřejmý.

Pojmenované argumenty používej hlavně když:

- funkce má víc parametrů,
- máš více defaultů,
- chceš mít volání samo o sobě čitelné.

> **💡 Tip:** Parametry typu `True/False`, `mode`, `round_to`, `tolerance` volej radši pojmenovaně.

---

### 1.6 Volitelné parametry v praxi

```python
def normalize_signal(values, min_value=0, max_value=1):
    low = min(values)
    high = max(values)
    scale = high - low
    return [min_value + (v - low) * (max_value - min_value) / scale for v in values]


print(normalize_signal([2, 4, 6], max_value=100))
print(normalize_signal([2, 4, 6], 0, 100))
```

U volitelných parametrů preferuj pojmenované volání (`min_value=...`, `max_value=...`), protože je čitelnější.

---

### 1.7 Návrat více hodnot

Funkce může vrátit víc výsledků najednou:

```python
def basic_stats(values):
    return min(values), max(values), round(sum(values) / len(values), 2)


min_v, max_v, avg_v = basic_stats([1200, 980, 1430, 1600, 890])
print(min_v, max_v, avg_v)
```

Python vrací tuple, kterou můžeš rozbalit do proměnných.

Ukázka: návrat uložený do tuple a následná indexace:

```python
stats = basic_stats([1200, 980, 1430, 1600, 890])
print(stats)      # (890, 1600, 1220.0)
print(stats[0])   # min
print(stats[1])   # max
print(stats[2])   # avg
```

Ukázka: vytažení jednoho výstupu přímo při volání:

```python
avg_only = basic_stats([1200, 980, 1430, 1600, 890])[2]
print(avg_only)
```

> **💡 Poznámka:** Stejný styl rozbalení funguje jak pro tuple, tak pro list.
> Počet proměnných na levé straně ale musí odpovídat počtu vracených hodnot.
> Jinak dostaneš chybu při přiřazení.
>
> ```python
> stats_tuple = (890, 1600, 1220.0)
> min_v, max_v, avg_v = stats_tuple
>
> stats_list = [890, 1600, 1220.0]
> min_v, max_v, avg_v = stats_list
>
> # min_v, max_v = stats_tuple  # ValueError: too many values to unpack
> ```

---

### 1.8 Lokální vs globální proměnné

Každá proměnná žije v nějakém jmenném prostoru (scope).

- **lokální proměnná**: vzniká uvnitř funkce, mimo funkci k ní nevidíš,
- **globální proměnná**: je definovaná mimo funkce na úrovni souboru.

#### A) Lokální proměnná existuje jen uvnitř funkce

```python
def local_demo():
    value = "local"
    print("uvnitř funkce:", value)


local_demo()
# print(value)  # NameError: value mimo funkci neexistuje
```

#### B) Funkce může globální proměnnou číst

```python
DEFAULT_ROUND = 2


def round_value(value):
    return round(value, DEFAULT_ROUND)


print(round_value(12.3456))  # 12.35
```

#### C) Stejné jméno uvnitř funkce přepíše globální jen lokálně

```python
player_name = "GlobalPlayer"


def show_player():
    player_name = "LocalPlayer"
    print("ve funkci:", player_name)


show_player()
print("mimo funkci:", player_name)
```

Výsledek:
- ve funkci se vypíše `LocalPlayer`,
- mimo funkci zůstane `GlobalPlayer`.

Tomuhle chování se říká **stínování (shadowing)**.

#### D) Pokus o změnu globální proměnné uvnitř funkce (bez `global`)

```python
counter = 10


def increment_bad():
    # Python to chápe jako lokální proměnnou `counter`,
    # takže řádek níže spadne na UnboundLocalError.
    counter = counter + 1
    return counter
```

Tohle je častá začátečnická chyba.

#### E) Změna globální proměnné přes `global` (technicky jde, prakticky opatrně)

```python
counter = 10


def increment_global():
    global counter
    counter = counter + 1
    return counter


print(increment_global())  # 11
print(counter)             # 11
```

Tahle varianta funguje, ale v běžném kódu ji používej minimálně.

#### Doporučení do praxe

1. Globální proměnné používej hlavně pro **konstanty** (např. `DEFAULT_TIMEOUT`).
2. Data, která se mění, předávej funkcím přes parametry a vracej přes `return`.
3. Když musíš sdílet měnitelný stav, je lepší to řešit strukturovaněji (např. třídou) než přes `global`.

Proč jsou globální proměnné problém při ladění:

- bez globálních proměnných bývá chyba často izolovaná na jednu funkci,
- s globálními proměnnými může problém vzniknout „jinde“ a projevit se až ve vzdálené části kódu,
- hledání chyby se pak rozšiřuje z jedné funkce na celý program.

> **⚠️ Pozor:** Nadměrné používání globálních proměnných vede k hůře čitelnému kódu a nepříjemným chybám při ladění.

---

### Poznámka k formátování kódu

Praktické zásady čitelného odřádkování a formátování jsou v doplňku:
[DOPLNĚK: ČITELNOST KÓDU A FORMÁTOVÁNÍ](07_doplnek_citelnost_kodu_a_formatovani.md).

---

**📝 ÚKOL: Navrhni funkci pro kontrolu síly hesla**

Vytvoř soubor `function_design.py` a implementuj funkci `analyze_password`.

Požadavky:

1. Funkce má mít tyto vstupy:

    - `password` (povinný řetězec),
    - `min_length` (nepovinný, výchozí hodnota `8`),
    - `require_digit` (nepovinný, výchozí `True`),
    - `require_upper` (nepovinný, výchozí `True`),
    - `require_symbol` (nepovinný, výchozí `False`),
    - `banned_words` (nepovinný, výchozí `None`).

2. Funkce ověří pravidla:

    - minimální délka hesla (`min_length`),
    - přítomnost alespoň jedné číslice,
    - přítomnost alespoň jednoho velkého písmene,
    - přítomnost symbolu, pokud je `require_symbol=True`,
    - zákaz vybraných slov z `banned_words`.

3. Za symbol ber znaky jako:

    - `!@#$%^&*()-_=+[]{};:,.?`
    - stačí, aby heslo obsahovalo alespoň jeden z nich.

4. Pokud je `banned_words=None`, nastav uvnitř funkce vlastní výchozí seznam
   (např. `['heslo', 'password', '1234']`).

5. Funkce vrátí přesně 3 výstupy v tomto pořadí:

    - `is_strong` (`bool`)
    - `score_percent` (`int`, hodnota `0-100`)
    - `missing_rules` (`list[str]`, názvy nesplněných pravidel)

6. `is_strong` nastav na `True` jen tehdy, když heslo splní všechna aktivní pravidla.

7. `score_percent` spočítej jako podíl splněných pravidel vůči všem aktivním pravidlům.
   Výsledek zaokrouhli na celé číslo.

8. `missing_rules` vrať jako seznam stručných názvů pravidel, která heslo nesplnilo
   (např. `"min_length"`, `"digit"`, `"upper"`, `"symbol"`, `"banned_word"`).

9. Připrav minimálně 4 testovací volání funkce:

    - čistě poziční,
    - mix pozičních a pojmenovaných argumentů,
    - volání s vypnutým pravidlem pro symbol,
    - volání s vlastním seznamem `banned_words`.

10. Každé volání vypiš přes `print(...)` a pod výpis krátce napiš,
    proč je takové volání čitelné (nebo méně čitelné).

---

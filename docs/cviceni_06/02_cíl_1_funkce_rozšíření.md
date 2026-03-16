# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## CÍL 1: FUNKCE – ROZŠÍŘENÍ A DOBRÉ NÁVYKY

---

### 1.1 Povinné a nepovinné parametry

- **Povinný** parametr musíš vždy zadat při volání. 
- **Nepovinný** parametr má výchozí hodnotu. Když ho při volání vynecháš, použije se ta výchozí.

```python
def average_value(values, round_to=2):
    return round(sum(values) / len(values), round_to)


print(average_value([1200, 980, 1430]))       # round_to=2
print(average_value([1200, 980, 1430], 1))    # round_to=1
```

> **⚠️ Pozor:** Nepovinné parametry patří v hlavičce až za povinné.

---

### 1.2 Poziční argumenty (positional)

Poziční argumenty se zadávají bez názvu, jen podle pořadí.

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

> **Poznámka: Parametr vs argument**
> 
> - **parametr** je proměnná v definici funkce (např. `value`, `from_currency`),
> - **argument** je konkrétní hodnota, kterou předáváš při volání (např. `2500`, `"gold"`).
> 
> Pojmy se často zaměňují, ale je dobré vědět, že parametr je „místo pro hodnotu“ a argument je „konkrétní hodnota“.

---

### 1.3 Pojmenované argumenty (keyword)

U delších funkcí bývá čitelnější volání přes názvy parametrů. Pojmenované argumenty se zadávají s názvem parametru, 
takže je hned jasné, co který vstup znamená.

```python
print(convert_coins(value=2500, from_currency="gold", to_currency="gems"))
```

Tohle se hodí hlavně při práci s nepovinnými parametry, protože můžeš zadat jen ty, které chceš změnit, a zbytek nechat na výchozí hodnotě.

---

### 1.4 Míchání pozičních a pojmenovaných argumentů

Míchat je můžeš, ale platí:

1. poziční argumenty musí být vždy před pojmenovanými,
2. stejný parametr nesmíš zadat 2x,
3. poziční argument za pojmenovaným vede k chybě.

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

> **Tip:** Parametry typu `True/False`, `mode`, `round_to`, `tolerance` volej radši pojmenovaně.

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

Python vrací více hodnot jako tuple, který můžeš rozbalit do proměnných.

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

> **Poznámka:** Stejný styl rozbalení funguje jak pro tuple, tak pro list.
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

- **lokální proměnná**: vzniká uvnitř funkce, mimo funkci neexistuje,
- **globální proměnná**: je definovaná mimo funkce na úrovni souboru.

#### Lokální proměnná existuje jen uvnitř funkce

```python
def local_demo():
    value = "local"
    print("uvnitř funkce:", value)


local_demo()
# print(value)  # NameError: value mimo funkci neexistuje
```

#### Funkce může globální proměnnou číst

```python
DEFAULT_ROUND = 2


def round_value(value):
    return round(value, DEFAULT_ROUND)


print(round_value(12.3456))  # 12.35
```

#### Stejné jméno uvnitř funkce přepíše globální jen lokálně

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

#### Pokus o změnu globální proměnné uvnitř funkce (bez `global`)

```python
counter = 10


def increment_bad():
    # Python to chápe jako lokální proměnnou `counter`,
    # takže řádek níže spadne na UnboundLocalError.
    counter = counter + 1
    return counter
```

Tohle je častá začátečnická chyba.

#### Změna globální proměnné přes `global` (technicky jde, prakticky opatrně)

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

#### ÚKOL: Kontrola síly hesla

Vytvoř soubor `function_design.py` a implementuj funkci `analyze_password`.

1. Funkce má mít tyto parametry:

    - `password` – povinný řetězec s heslem
    - `min_length` – minimální délka hesla (nepovinný, výchozí hodnota `8`)
    - `require_digit` – zda musí heslo obsahovat číslici (nepovinný, výchozí `True`)
    - `require_upper` – zda musí heslo obsahovat velké písmeno (nepovinný, výchozí `True`)
    - `require_symbol` – zda musí heslo obsahovat symbol (nepovinný, výchozí `False`)
    - `banned_words` – seznam zakázaných slov (nepovinný, výchozí `None`)

2. Funkce ověří následující pravidla:

    - minimální délka hesla (`min_length`),
    - přítomnost alespoň jedné číslice, pokud je `require_digit=True`,
    - přítomnost alespoň jednoho velkého písmene, pokud je `require_upper=True`,
    - přítomnost alespoň jednoho symbolu, pokud je `require_symbol=True`,
      > Za symbol považuj znaky: `!@#$%^&*()-_=+[]{};:,.?`
    - heslo nesmí obsahovat žádné slovo ze seznamu `banned_words`.
      > Pokud je `banned_words=None`, nastav uvnitř funkce vlastní výchozí seznam (např. `['heslo', 'password', '1234']`).

3. Funkce vrátí tři výstupy v tomto pořadí:

    - `is_strong` (`bool`) - `True` pokud heslo splní všechna aktivní pravidla, jinak `False`,
    - `score_percent` (`int`, hodnota `0-100`) - procentuální podíl splněných pravidel vůči všem aktivním pravidlům,
    - `missing_rules` (`list[str]`, názvy nesplněných pravidel) - seznam pravidel, která heslo nesplnilo (např. `"min_length"`, `"digit"`, `"upper"`, `"symbol"`, `"banned_word"`).

4. Připrav minimálně 4 testovací volání funkce:

    - čistě poziční,
    - mix pozičních a pojmenovaných argumentů,
    - volání s vypnutým pravidlem pro symbol,
    - volání s vlastním seznamem `banned_words`.

5. Každé volání vypiš přes `print(...)` a pod výpis krátce napiš, proč je dané volání čitelné (nebo méně čitelné) a jaké jsou výhody nebo nevýhody zvoleného stylu.

---

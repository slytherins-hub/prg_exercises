# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 4: PRÁCE S VÍCE OBJEKTY

### 4.1 Jeden objekt je začátek, více objektů je praxe

V cílech 2 a 3 jsi pracoval s jedním nebo dvěma objekty. Takhle se věci dobře učí, ale v reálné práci máš málokdy data od jednoho pacienta nebo jednoho senzoru. Typicky máš:

- záznamy od desítek nebo stovek pacientů,
- sérii měření z různých senzorů najednou,
- výsledky experimentů ke srovnání.

Právě tady se OOP začíná vracet v plné síle. Místo toho, abys měl zvlášť seznam jmen, zvlášť seznam polí hodnot a zvlášť slovník metadat, máš **seznam objektů**. Každý objekt nese svá data i metody – a ty je pak snadno procházíš, filtruješ nebo řadíš.

### 4.2 Vytvoření seznamu objektů

Objekt je v Pythonu normální hodnota – dá se uložit do proměnné, do seznamu, do slovníku, předat jako argument funkci. Tady je pět signálů v jednom seznamu:

```python
signals = [
    BiomedicalSignal("EKG",       [0.5, 1.2, 1.8, 0.9, 2.1, 1.5, 0.7]),
    BiomedicalSignal("Tlak",      [80, 85, 90, 88, 92, 87, 84]),
    BiomedicalSignal("Saturace",  [98, 97, 96, 98, 99, 97, 98]),
    BiomedicalSignal("Teplota",   [36.5, 36.7, 37.1, 37.0, 36.8, 36.9, 37.2]),
    BiomedicalSignal("Respirace", [14, 16, 15, 18, 17, 16, 15]),
]
```

Pět objektů různých typů dat v jednom seznamu. Každý má jiná data, ale všechny umějí stejné metody – to je klíčová výhoda oproti pěti oddělěným proměnným.

### 4.3 Výpis a iterace

Díky `__str__` z cíle 3 je výpis přehledu triviální:

```python
for signal in signals:
    print(signal)
```

Výstup:

```
[EKG] n=7, průměr=1.24, rozsah=[0.50, 2.10]
[Tlak] n=7, průměr=86.57, rozsah=[80.00, 92.00]
[Saturace] n=7, průměr=97.57, rozsah=[96.00, 99.00]
[Teplota] n=7, průměr=36.89, rozsah=[36.50, 37.20]
[Respirace] n=7, průměr=15.86, rozsah=[14.00, 18.00]
```

### 4.4 Hledání maxima a minima

Funkce `max()` a `min()` umějí pracovat s objekty – musíš jim jen říct, **podle čeho** mají porovnávat:

```python
nejvetsi_prumer = max(signals, key=lambda s: s.mean_value())
print(f"Nejvyšší průměr: {nejvetsi_prumer}")

nejsirsi_rozsah = max(signals, key=lambda s: s.max_value() - s.min_value())
print(f"Nejširší rozsah hodnot: {nejsirsi_rozsah}")
```

`lambda s: s.mean_value()` je zkrácená anonymní funkce – dostane objekt `s` a vrátí hodnotu, podle níž se porovnává. `max()` pak vybere objekt s největší takovou hodnotou.

### 4.5 Filtrování

Chceš vybrat jen signály, jejichž průměr překračuje určitou mez? List comprehension s podmínkou:

```python
THRESHOLD = 50
vysoke = [s for s in signals if s.mean_value() > THRESHOLD]

print(f"Signálů s průměrem nad {THRESHOLD}: {len(vysoke)}")
for s in vysoke:
    print(f"  {s.name}: průměr = {s.mean_value():.2f}")
```

Výsledkem je nový seznam – původní `signals` zůstává beze změny.

### 4.6 Řazení

`sorted()` funguje stejným principem jako `max()`:

```python
# Od největšího průměru k nejmenšímu
podle_prumeru = sorted(signals, key=lambda s: s.mean_value(), reverse=True)

print("Signály seřazené podle průměru:")
for s in podle_prumeru:
    print(f"  {s.name:12s}  průměr = {s.mean_value():.2f}")
```

Výstup:

```
Signály seřazené podle průměru:
  Saturace     průměr = 97.57
  Tlak         průměr = 86.57
  Respirace    průměr = 15.86
  Teplota      průměr = 36.89
  EKG          průměr = 1.24
```

> **💡 Tip:** Práce se seznamem objektů je výrazně přehlednější než práce s několika paralelními seznamy. Porovnej `max(signals, key=lambda s: s.mean_value())` oproti hledání indexu maxima v odděleném seznamu hodnot a pak načtení jména z jiného seznamu zvlášť.

**📝 ÚKOL: Databáze měření**

1. Vytvoř alespoň 5 objektů `BiomedicalSignal` s různými daty (klidně vymyšlenými – EKG, tlak, saturace, teplota, dech nebo jiné).
2. Ulož je do seznamu a vypiš přehled všech pomocí `print()`.
3. Najdi signál s nejvyšší maximální hodnotou a vypiš jeho název.
4. Najdi signál s nejmenším rozptylem hodnot (rozsah = max − min).
5. Vyfiltruj signály, kde průměr překračuje hodnotu, kterou si sám zvolíš. Vypiš, kolik jich je.
6. Seřaď signály sestupně podle průměrné hodnoty a vypiš výsledek.

---
# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## CÍL 4: KOMBINACE CYKLU A PODMÍNEK

Nyní si ukážeme, jak spojit cykly s podmínkami. To je velmi mocný nástroj - umožňuje nám projít data a reagovat odlišně na každý prvek.

### 4.1 Podmínka uvnitř cyklu

Základní princip je jednoduchý: cyklem projdeme všechny prvky a podmínkou rozhodneme, co s nimi uděláme.

**Příklad: Detekce horečky u pacientů**

```python
# Seznam teplot pacientů
temperatures = [36.6, 38.5, 37.2, 39.1, 36.9]

# Projdeme všechny teploty
for temp in temperatures:
 if temp >= 38.0:
 print(f"Horečka: {temp} °C")
 else:
 print(f"V normě: {temp} °C")
```

Výstup:
```
V normě: 36.6 °C
Horečka: 38.5 °C
V normě: 37.2 °C
Horečka: 39.1 °C
V normě: 36.9 °C
```

**Příklad: Počítání problémových hodnot**

```python
# Seznam teplot
temperatures = [36.6, 38.5, 37.2, 39.1, 36.9, 38.2]

# Počítadlo pacientů s horečkou
fever_count = 0

for temp in temperatures:
 if temp >= 38.0:
 fever_count += 1 # Zkrácený zápis pro: fever_count = fever_count + 1

print(f"Celkem pacientů: {len(temperatures)}")
print(f"Pacientů s horečkou: {fever_count}")
```

> ** Operátor `+=`:** Zkrácený zápis pro přičítání. `x += 1` je totéž jako `x = x + 1`.

---

#### ÚKOL: Kontrola lékařských vzorků

V laboratoři máte vzorky s různými hodnotami glykémie (cukru v krvi).
Normální hodnota je 3.9-5.6 mmol/l.

Napište program, který:

1. Vytvoří seznam `glucose_levels = [4.5, 6.2, 3.8, 5.1, 7.5, 4.9]`
2. Projde všechny hodnoty pomocí cyklu
3. Pro každou hodnotu:

 - Pokud je **pod 3.9**: vypíše `"Hypoglykémie: X mmol/l"`
 - Pokud je **nad 5.6**: vypíše `"Hyperglykémie: X mmol/l"`
 - Jinak: vypíše `"V normě: X mmol/l"`

**Tip:** Budete potřebovat vnořené podmínky (`if` uvnitř `else`).

---


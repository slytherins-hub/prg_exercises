# CVIČENÍ 3: FUNKCE A SEZMANY

Algoritmizace a programování

## CÍL 3: PROCVIČOVÁNÍ

Nyní spojíme vše dohromady – seznamy, cykly, podmínky a funkce.

### 3.1 Filtrování seznamu pomocí funkce

```python
def has_fever(temperature):
 """Kontroluje, zda daná teplota znamená horečku."""
 return temperature >= 38.0

# Seznam měření
temperatures = [36.5, 37.2, 38.1, 36.8, 38.5, 37.0, 39.0]

# Filtrování - najdi všechny horečky
fevers = []
for temp in temperatures:
 if has_fever(temp):
 fevers.append(temp)

print(f"Horečky: {fevers}")
print(f"Počet horečnatých měření: {len(fevers)}")
```

---

#### ÚKOL: Analýza krevního tlaku

Vytvoř program `blood_pressure_analysis.py`, který:

1. Definuje funkci `classify_pressure(systolic, diastolic)`, která vrací kategorii:

 * systolický tlak menší než 120 a zároveň diastolický tlak menší než 80: `"Normální"`,
 * systolický tlak menší než 130 a zároveň diastolický tlak menší než 85: `"Vyšší normální"`,
 * systolický tlak menší než 140 a zároveň diastolický tlak menší než 90: `"Hypertenze 1. stupně"`,
 * jinak: `"Hypertenze 2. stupně"`.

2. Vytvoří seznam měření šesti pacientů:
 ```python
 measurements = [
 ["Jan", 118, 78],
 ["Marie", 135, 88],
 ["Petr", 125, 82],
 ["Anna", 145, 95],
 ["Tomáš", 119, 79],
 ["Eva", 142, 91]
 ]
 ```

3. Projde všechna měření a:

 * Vypíše jméno, hodnoty a kategorii.
 * Spočítá, kolik pacientů má hypertenzi (1. nebo 2. stupně).
 * Najde pacienta s nejvyšším systolickým tlakem.

**Očekávaný výstup:**
```
=== ANALÝZA KREVNÍHO TLAKU ===
Jan: 118/78 mmHg → Normální
Marie: 135/88 mmHg → Hypertenze 1. stupně
Petr: 125/82 mmHg → Vyšší normální
Anna: 145/95 mmHg → Hypertenze 2. stupně
Tomáš: 119/79 mmHg → Normální
Eva: 142/91 mmHg → Hypertenze 2. stupně

STATISTIKA:
Pacientů s hypertenzí: 3
Nejvyšší tlak: Anna (145/95 mmHg)
```

---

#### ÚKOL: Statistika DNA sekvence s funkcemi

Vytvoř program pro komplexní analýzu DNA sekvence s využitím funkcí.

1. Vytvoř funkci `analyze_dna()`:

 * Funkce přijímá jeden parametr typu `str` (DNA sekvence, např. `"ACGTTAGCTA"`).
 * Funkce spočítá počet jednotlivých nukleotidů (A, C, G, T)
 * Funkce vypočítá GC obsah v procentech: `(počet_G + počet_C) / celková_délka * 100`
 * Funkce vrátí hodnotu typu `list` s vypočítanými hodnotami v pořadí: *počet A, počet C, počet G, počet T, GC procenta*.

2. Vytvoř funkci `find_motifs()`:

 * Funkce přijímá dva parametry typu `str`:

 * DNA sekvenci,
 * hledaný motiv (podřetězec).
 * Funkce najde všechny výskyty zadaného motivu v DNA sekvenci. Tedy vyhledá všechny pozice (indexy), kde hledaný motiv začíná.
 * Funkce vrátí hodnotu typu `list` obsahující indexy nalezených výskytů.

3. Vytvoř funkci `complementary_strand()`:

 * Funkce přijímá jeden parametr typu `str` (DNA sekvence).
 * Funkce vytvoří komplementární řetězec podle pravidel párování bází (A ↔ T, C ↔ G).
 * Funkce vrátí hodnotu typu `str` (komplementární sekvence).

4. Hlavní program:
 ```python
 dna = "ACGTTAGCTAGCTAGCTAACGTA"

 # Analýza
 stats = analyze_dna(dna)
 print(f"=== ANALÝZA DNA ===")
 print(f"Sekvence: {dna}")
 print(f"Délka: {len(dna)} bp")
 print(f"A: {stats[0]}, C: {stats[1]}, G: {stats[2]}, T: {stats[3]}")
 print(f"GC obsah: {stats[4]:.1f}%")

 # Hledání motivu
 motif = "GCT"
 positions = find_motifs(dna, motif)
 print(f"\nMotiv '{motif}' nalezen na pozicích: {positions}")

 # Komplementární řetězec
 complement = complementary_strand(dna)
 print(f"\nKomplementární řetězec: {complement}")
 ```

**Očekávaný výstup:**
```
=== ANALÝZA DNA ===
Sekvence: ACGTTAGCTAGCTAGCTAACGTA
Délka: 23 bp
A: 8, C: 6, G: 5, T: 4
GC obsah: 47.8%

Motiv 'GCT' nalezen na pozicích: [4, 8, 12]

Komplementární řetězec: TGCAATCGATCGATCGATTGCAT
```

---


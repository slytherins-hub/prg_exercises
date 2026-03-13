# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 3: ÚKOL – TŘÍDA PRO DNA SEKVENCI

### 3.1 Zadání

V tomhle cíli navrhnete vlastní třídy pro práci s biologickými sekvencemi. Použiješ přitom dědičnost tak, jak jsi ji viděl v cíli 2.

Cíl je jasný: mít objekt, který obaluje DNA sekvenci a nabízí nad ní zajímavé operace – výpočet GC obsahu, počítání bází, vizualizaci složení.

---

### 3.2 Základní třída `Sequence`

Začni tímto základem – třída `Sequence` bude rodič pro libovolný typ biologické sekvence:

```python
class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()   # vždy uložíme velkými písmeny

    def length(self):
        return len(self.sequence)

    def __str__(self):
        return f"[{self.name}] délka={self.length()} nt, začátek: {self.sequence[:8]}..."
```

Ověř, že třída funguje dřív než jdeš dál:

```python
seq = Sequence("testovací", "acgtagctagc")
print(seq)           # [testovací] délka=11 nt, začátek: ACGTAGCT...
print(seq.length())  # 11
print(seq.sequence)  # ACGTAGCTAGC – automaticky převedeno na velká písmena
```

---

### 3.3 Odvozená třída `DNASequence`

**📝 ÚKOL: Vytvoř třídu `DNASequence`**

Odvoď třídu `DNASequence` od `Sequence`. Přidej do ní operace specifické pro DNA.

**Část 1 – základní metody**

1. Odvoď třídu `DNASequence` od `Sequence` zápisem `class DNASequence(Sequence)`.
   - `__init__` **nepiš** – zdědí ho ze `Sequence`, stačí.

2. Přidej metodu `gc_content()`, která vrátí podíl bází G a C jako číslo v rozsahu 0–1.

    ```
    "ACGT" → gc_content = 0.5   (2 ze 4 jsou G nebo C)
    "AAAA" → gc_content = 0.0
    "GCGC" → gc_content = 1.0
    ```

3. Přidej metodu `base_counts()`, která vrátí počty všech čtyř bází jako slovník.

    ```python
    {"A": 2, "C": 3, "G": 3, "T": 2}
    ```

4. Vytvoř alespoň 3 objekty `DNASequence` s různými sekvencemi (klidně vymyšlenými). Vypiš GC obsah každé z nich.

5. Ověř, že metody `length()` a `__str__()` fungují i na objektech `DNASequence` (jsou zděděné ze `Sequence` – nepsal jsi je znovu).

> **💡 Nápověda:** Pro výpočet GC obsahu ti postačí metoda `str.count()`:
> ```python
> gc = self.sequence.count("G") + self.sequence.count("C")
> gc_content = gc / len(self.sequence)
> ```

**Část 2 – vizualizace**

6. Přidej metodu `plot_composition()`, která vykreslí sloupcový graf složení bází. Každá báze (A, C, G, T) bude mít vlastní barevný sloupec.

    Výsledný graf by měl vypadat nějak takto: čtyři sloupce s nadpisem obsahujícím název sekvence, popsaná osa y s počty.

    Tip: použij `plt.bar()` s explicitním seznamem barev.

7. Vykresli složení bází pomocí `plot_composition()` pro alespoň 2 různé sekvence. Porovnej vizuálně, jak se liší.

**Část 3 – validace**

8. Přidej metodu `is_valid()`, která vrátí `True`, pokud sekvence obsahuje **pouze** platné báze (A, C, G, T), a `False`, pokud obsahuje neznámý znak.

    ```python
    dna1 = DNASequence("platná", "ACGCTAGCTAGC")
    dna2 = DNASequence("neplatná", "ACGCNTAGCTAGC")  # N = neznámá báze

    print(dna1.is_valid())  # True
    print(dna2.is_valid())  # False
    ```

    Nápověda: `set(self.sequence)` vrátí množinu různých znaků v sekvenci. Porovnej ji s `{"A", "C", "G", "T"}`.

> **💡 Tip:** GC obsah je biologicky zajímavá charakteristika. Bakterie *Mycobacterium tuberculosis* má GC obsah přes 65 %, zatímco kvasinky *Saccharomyces cerevisiae* kolem 38 %. Zkus vytvořit sekvence s různým GC obsahem a vizualizovat je.

---

### 3.4 Shrnutí toho, co jsi postavil

Po dokončení úkolu budeš mít:

- třídu `Sequence` – rodičovská třída s obecnými metodami pro libovolnou sekvenci,
- třídu `DNASequence` – odvozená třída s metodami specifickými pro DNA,
- ukázku dědičnosti v praxi: `length()` a `__str__()` jsi napsal jednou v rodiči a fungují v potomkovi automaticky,
- vizualizaci složení bází pomocí matplotlib přímo jako metodu třídy.

---

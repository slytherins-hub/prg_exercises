# CVIČENÍ 13: OOP A AI NÁSTROJE

Algoritmizace a programování

## CÍL 2: ÚKOL – TŘÍDY PRO DNA A RNA

Dědičnost si teď vyzkoušíš na úloze z bioinformatiky. Napíšeš **obecnou třídu `Sequence`** a od ní odvodíš
**dva potomky** — `DNASequence` a `RNASequence`. Uvidíš dvě věci, které dědičnost dělá hezky:

- společný kód v rodiči napíšeš **jednou** a oba potomci ho mají automaticky,
- každý potomek přidá jen to, co je **specifické** pro jeho typ sekvence.

Biologicky to dává smysl: DNA a RNA si jsou hodně podobné — liší se hlavně tím, že DNA používá bázi **T**
(thymin), zatímco RNA **U** (uracil). A jedna vzniká z druhé **transkripcí**.

---

### 2.1 Rodičovská třída `Sequence`

Začni tímto základem. `Sequence` bude sloužit jako rodič pro libovolnou biologickou sekvenci:

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

Ulož si ji do souboru `sequences.py` a ověř, že funguje:

```python
seq = Sequence("testovací", "acgtagctagc")
print(seq)            # [testovací] délka=11 nt, začátek: ACGTAGCT...
print(seq.length())   # 11
print(seq.sequence)   # ACGTAGCTAGC – automaticky převedeno na velká písmena
```

> **💡 Poznámka:** `sequence.upper()` v `__init__` je malý, ale důležitý detail. Zajišťuje, že všechny
> metody dál pracují s konzistentním tvarem (velká písmena) bez ohledu na to, jak uživatel data předá.
> Typická ukázka, proč jsou třídy praktické — pravidlo „vždy velká písmena" platí pro celý objekt
> a ty se o něj už nemusíš starat.

---

### 2.2 Odvozená třída `DNASequence`

Teď napíšeš třídu `DNASequence`, která **dědí od `Sequence`** a přidá operace specifické pro DNA.

#### 📝 Část 1: základní metody

1. Nad třídou `Sequence` (ve stejném souboru) vytvoř třídu `DNASequence` dědící ze `Sequence`:

    ```python
    class DNASequence(Sequence):
        ...
    ```

    **`__init__` psát nemusíš** — zdědí ho beze změny ze `Sequence`. Stejně tak `length()` a `__str__()`
    dostaneš zdarma.

2. Přidej metodu `gc_content()`, která vrátí **podíl bází G a C** jako číslo v rozsahu 0–1:

    ```
    "ACGT" → 0.5   (2 ze 4 jsou G nebo C)
    "AAAA" → 0.0
    "GCGC" → 1.0
    ```

    > **Nápověda:** Využij `str.count()`:
    > ```python
    > gc = self.sequence.count("G") + self.sequence.count("C")
    > return gc / len(self.sequence)
    > ```

3. Přidej metodu `base_counts()`, která vrátí počty všech čtyř bází jako slovník:

    ```python
    dna = DNASequence("mini", "ACCGGGTT")
    print(dna.base_counts())   # {"A": 1, "C": 2, "G": 3, "T": 2}
    ```

4. Vytvoř alespoň **tři objekty `DNASequence`** s různými sekvencemi (klidně vymyšlenými) a vypiš GC obsah
   každé z nich. Pro inspiraci: GC obsah kolem 65 % je typický pro *Mycobacterium tuberculosis*, kolem 38 %
   pro kvasinky *Saccharomyces cerevisiae*. Zkus sekvence s různým GC tak, aby ses na výsledcích o tom něco dozvěděl.

5. Ověř, že na objektech `DNASequence` fungují i zděděné `length()` a `__str__()` — **nepsal jsi je znovu**,
   a přesto fungují.

---

#### 📝 Část 2: vizualizace

6. Přidej metodu `plot_composition()`, která vykreslí **sloupcový graf složení bází**. Čtyři sloupce —
   A, C, G, T — každý v jiné barvě. Nadpis grafu ať obsahuje název sekvence.

    Kostra:

    ```python
    def plot_composition(self):
        counts = self.base_counts()
        bases = ["A", "C", "G", "T"]
        values = [counts[b] for b in bases]
        colors = ["tab:green", "tab:blue", "tab:orange", "tab:red"]

        plt.figure(figsize=(5, 3))
        plt.bar(bases, values, color=colors, edgecolor="black")
        plt.title(f"Složení bází: {self.name}")
        plt.ylabel("Počet")
        plt.tight_layout()
        plt.show()
    ```

7. Zavolej `plot_composition()` na dvou sekvencích s **výrazně různým GC obsahem** a porovnej vizuálně, jak
   se sloupce liší.

---

#### 📝 Část 3: validace

8. Přidej metodu `is_valid()`, která vrátí `True`, pokud sekvence obsahuje **pouze platné báze** (A, C, G, T),
   a `False` jinak:

    ```python
    dna1 = DNASequence("platná",   "ACGCTAGCTAGC")
    dna2 = DNASequence("neplatná", "ACGCNTAGCTAGC")   # N = neznámá báze

    print(dna1.is_valid())   # True
    print(dna2.is_valid())   # False
    ```

    > **Nápověda:** `set(self.sequence)` vrátí množinu různých znaků v sekvenci. Stačí ji porovnat
    > s `{"A", "C", "G", "T"}`:
    > ```python
    > return set(self.sequence) <= {"A", "C", "G", "T"}
    > ```
    > Operátor `<=` na množinách znamená „je podmnožinou".

---

### 2.3 Druhý potomek: `RNASequence`

V buňce z DNA vzniká **RNA** procesem, kterému se říká **transkripce**. Prakticky jde jen o jednu změnu:
každé **T** se v RNA píše jako **U** (uracil). Všechno ostatní (A, C, G) zůstává stejné.

To se hezky hodí pro OOP: `RNASequence` bude další potomek třídy `Sequence`, velmi podobný `DNASequence`,
ale pracuje s abecedou `A, C, G, U`. Navíc přidáme jednu opravdu RNA-specifickou věc — **kodony**.

> **💡 Co je kodon?** RNA (konkrétně mRNA) se čte po **trojicích bází** zvaných **kodony**. Každý kodon
> odpovídá jedné aminokyselině v bílkovině. Speciální kodon **`AUG`** („start kodon") označuje místo,
> kde ribozom začíná sekvenci číst.

---

#### 📝 Část 4: transkripce DNA → RNA

9. Přidej do třídy `DNASequence` metodu `to_rna()`, která vytvoří a **vrátí nový objekt `RNASequence`**
   s nahrazeným T za U. Jméno nech stejné, ať poznáš, že jde o přepis té samé sekvence:

    ```python
    def to_rna(self):
        return RNASequence(self.name, self.sequence.replace("T", "U"))
    ```

    Všimni si, že metoda **vrací objekt jiné třídy**. Jeden objekt takto může vyrobit druhý — podobně
    jako buňka „vyrobí" z DNA molekulu RNA.

    > **💡 Technická poznámka:** Definici `to_rna()` ti IDE nejspíš podtrhne, protože třída `RNASequence`
    > v tuhle chvíli ještě neexistuje. To nevadí — Python hledá jméno třídy **až při volání metody**,
    > ne při její definici. Jakmile si `RNASequence` v dalším bodě napíšeš, všechno bude fungovat.
    > Jen dbej, aby obě třídy byly ve **stejném souboru**.

---

#### 📝 Část 5: vlastní třída `RNASequence`

10. Pod třídou `DNASequence` vytvoř třídu `RNASequence`, která dědí ze `Sequence`:

    ```python
    class RNASequence(Sequence):
        ...
    ```

    `__init__`, `length()` i `__str__()` zase získáš zdarma ze `Sequence`. Dopíšeš tři nové metody.

11. **`is_valid()`** — vrátí `True`, pokud sekvence obsahuje pouze báze **A, C, G, U** (žádné T!):

    ```python
    RNASequence("správná",   "ACGUACGU").is_valid()   # True
    RNASequence("s thyminem","ACGTACGU").is_valid()   # False — T v RNA být nemá
    ```

12. **`codons()`** — rozdělí sekvenci na **trojice** a vrátí jejich seznam. Případný neúplný zbytek na konci
    (1 nebo 2 báze navíc) ignoruj:

    ```python
    rna = RNASequence("mini", "AUGGCUUAA")
    print(rna.codons())   # ["AUG", "GCU", "UAA"]

    rna2 = RNASequence("zbytek", "AUGGCUUA")
    print(rna2.codons())  # ["AUG", "GCU"]   — poslední dvě písmena netvoří celý kodon
    ```

    > **Nápověda:** List comprehension s krokem 3:
    > ```python
    > return [self.sequence[i:i+3] for i in range(0, len(self.sequence) - 2, 3)]
    > ```
    > `len(self.sequence) - 2` zajistí, že se neúplná trojice nepřidá.

13. **`find_start_codon()`** — vrátí **pozici** prvního výskytu `AUG`, nebo `-1` pokud v sekvenci není:

    ```python
    rna = RNASequence("gen", "CCAUGGCUUAA")
    print(rna.find_start_codon())   # 2   — AUG začíná na indexu 2
    ```

    > **Nápověda:** `str.find()` přesně tohle umí — viz
    > [dokumentace](https://docs.python.org/3/library/stdtypes.html#str.find).

---

#### 📝 Část 6: dej to dohromady

14. Vytvoř `DNASequence` s malou genovou sekvencí (klidně vymyšlenou — hlavní je, aby obsahovala `ATG`,
    což je DNA verze start kodonu) a projdi celý řetězec transkripce → hledání start kodonu → kodony:

    ```python
    dna = DNASequence("gen_01", "CCATGGCTTAA")

    rna = dna.to_rna()
    print(rna)                          # __str__ zděděné ze Sequence
    print(rna.is_valid())               # True
    print(rna.find_start_codon())       # pozice prvního AUG
    print(rna.codons())                 # seznam kodonů
    ```

15. Vytvoř si alespoň dva různé `DNASequence` objekty — jeden s jasným start kodonem a jeden bez něj —
    a ukaž, že pro každý dostaneš jiný výsledek `find_start_codon()`.

---

### 2.4 Co sis po cestě postavil

Po dokončení úkolu máš:

- třídu `Sequence` — obecný rodič s metodami `length()` a `__str__()`,
- třídu `DNASequence` — potomek s DNA-specifickými metodami (`gc_content`, `base_counts`,
  `plot_composition`, `is_valid`, `to_rna`),
- třídu `RNASequence` — druhý potomek s RNA-specifickými metodami (`is_valid`, `codons`, `find_start_codon`),
- konkrétní ukázku dědičnosti: `__init__`, `length()` a `__str__()` jsi napsal **jednou v rodiči**
  a fungují v **obou potomcích** automaticky,
- malou demonstraci toho, jak jeden objekt vyrobí jiný — `DNASequence.to_rna()` vrátí `RNASequence`,
  stejně jako v buňce z DNA vzniká RNA.

> **💡 K zamyšlení:** Všimni si, že `is_valid()` máš napsané ve dvou potomcích skoro stejně — jen se liší
> povolenými bázemi. To je malý zápach duplikace kódu. Způsobů, jak to v OOP řešit, je víc (sdílená metoda
> v rodiči, která se parametrizuje; třídní atribut s povolenými bázemi, …), ale to už je téma na pozdější
> kurz OOP. Pro teď je duplikace ve dvou metodách v pohodě.

---

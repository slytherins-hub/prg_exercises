# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## CÍL 3: ŘAZENÍ V PYTHONU

Vlastní Bubble Sort i Selection Sort jsou skvělé pro pochopení principu, ale v reálných projektech sáhneš po vestavěných 
nástrojích Pythonu. Jsou rychlejší, lépe otestované a napsané tak, aby zvládly i velké objemy dat.

### 3.1 `sort()` a `sorted()`

Python nabízí dva základní nástroje pro řazení: metodu `sort()` a funkci `sorted()`. Oba používají algoritmus 
**Timsort** s průměrnou i nejhorší časovou složitostí $O(n \log n)$.

Metoda `sort()` řadí **přímo uvnitř původního seznamu** — mění jeho pořadí a nic nevrací.

**💻 Zkus:** Zavolej `sort()` nad krátkým seznamem a podívej se, jak se změnila původní proměnná.

```python
my_list = [3, 8, 1, 2, 32]
my_list.sort()
print(my_list)   # [1, 2, 3, 8, 32]
```

Funkce `sorted()` naopak vytváří **nový** seřazený seznam. Původní data zůstávají beze změny.

**💻 Zkus:** Porovnej výstup `sorted()` s původním seznamem.

```python
my_list = [3, 8, 1, 2, 32]
new_list = sorted(my_list)
print(my_list)   # [3, 8, 1, 2, 32]   ← beze změny
print(new_list)  # [1, 2, 3, 8, 32]
```
> **Poznámka:** Funkce `sorted()` není omezená jen na seznamy. Můžeš ji použít pro jakoukoliv iterovatelnou sekvenci — třeba pro řetězce, n-tice nebo slovníky.

### 3.2 Argument `reverse`

Obě varianty přijímají nepovinný argument `reverse`. Ve výchozím stavu (`reverse=False`) se řadí vzestupně, s `reverse=True` sestupně.

```python
my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list, reverse=True)
print(my_list)   # [32, 8, 3, 2, 1]
```

### 3.3 Argument `key`

Argument `key` umožňuje nastavit **klíč**, podle kterého se řadí. Argument očekává funkci, která z každého prvku udělá hodnotu použitou pro porovnání.

**💻 Zkus:** Seřaď seznam řetězců podle jejich délky.

```python
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
print(list_of_words)   # ['MOO', 'woof', 'meeeoow', 'BZZZZZZ']
```

**💻 Zkus:** Seřaď seznam řetězců bez ohledu na velikost písmen.

```python
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=str.lower)
```

---

### 3.4 Souhrn a další algoritmy

Pojďme dát dohromady to, co už znáš, a přidat pár dalších algoritmů pro přehled. **Není nutné je znát zpaměti.** 
Důležitější je vědět, že různé algoritmy se hodí pro různé typy dat a různé situace.

| Algoritmus           | Nejlepší      | Nejhorší      | Průměrný      | Stabilní? |
|----------------------|---------------|---------------|---------------|-----------|
| **Selection Sort**   | $O(n^2)$      | $O(n^2)$      | $O(n^2)$      | ne        |
| **Bubble Sort**      | $O(n)$        | $O(n^2)$      | $O(n^2)$      | ano       |
| **Timsort** (Python) | $O(n)$        | $O(n \log n)$ | $O(n \log n)$ | ano       |
| Insertion Sort       | $O(n)$        | $O(n^2)$      | $O(n^2)$      | ano       |
| Merge Sort           | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | ano       |
| Heap Sort            | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | ne        |
| Quick Sort           | $O(n \log n)$ | $O(n^2)$      | $O(n \log n)$ | ne        |
| Radix Sort           | $O(nk)$       | $O(nk)$       | $O(nk)$       | ano       |

První tři řádky (tučně) jsou algoritmy z dnešního cvičení. Zbytek jsou další známé algoritmy, se kterými se můžeš setkat.
Python vnitřně používá **Timsort** — hybridní algoritmus odvozený od Merge Sortu a Insertion Sortu. Pro běžná data
dosahuje velmi dobrých výsledků a je stabilní.

> **Poznámka:** U různých implementací online si dávej pozor na kvalitu řešení. To, že nějaký kód „funguje", ještě 
> neznamená, že skutečně odpovídá deklarované asymptotické složitosti.

---

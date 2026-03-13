# CVIČENÍ 11: ŘADICÍ ALGORITMY

Algoritmizace a programování

## CÍL 2: ŘAZENÍ V PYTHONU A DALŠÍ ALGORITMY

### 2.1 Řazení v Pythonu

Základním nástrojem pro řazení v Pythonu je funkce `sorted()` a metoda `sort()`. Oba nástroje využívají **stabilní** algoritmus Timsort, který má v průměrném i nejhorším případě asymptotickou složitost $O(n \log n)$.

Metoda `sort()` mění pořadí hodnot přímo v původním seznamu. Hodí se tedy ve chvíli, kdy nepotřebuješ zachovat původní pořadí prvků a chceš pracovat přímo s jedním seznamem.

**💻 Zkus:** Zavolej metodu `sort()` nad krátkým seznamem a podívej se, jak se změní původní proměnná.

```python
my_list = [3, 8, 1, 2, 32]
my_list.sort()
```

Funkce `sorted()` naopak vytváří nový seřazený seznam z původní iterovatelné struktury. Původní data tak můžeš nechat beze změny.

**💻 Zkus:** Porovnej výsledek `sorted()` s původním seznamem a ověř, že původní hodnota zůstala zachovaná.

```python
my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list)
```

Oba nástroje umožňují použít nepovinné argumenty `reverse` a `key`.

**💻 Zkus:** Vyzkoušej řazení sestupně pomocí argumentu `reverse=True`.

```python
my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list, reverse=True)
```

Argument `key` umožňuje nastavit klíč, podle kterého bude sekvence seřazena.

**💻 Zkus:** Seřaď seznam řetězců podle jejich délky.

```python
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
```

**💻 Zkus:** Seřaď seznam řetězců bez ohledu na velikost písmen.

```python
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=str.lower)
```

> **💡 Tip:** V běžné praxi je téměř vždy lepší použít interní řazení Pythonu než ručně implementovat vlastní jednoduchý řadicí algoritmus.

**📝 ÚKOL: Porovnání vlastního a vestavěného řazení**

1. Vyber jednu z číselných řad, se kterou jsi pracoval v první části cvičení.
2. Seřaď ji vlastní implementací některého z algoritmů.
3. Stejnou posloupnost seřaď pomocí `sorted()`.
4. Porovnej, jestli oba výsledky odpovídají.
5. Stručně napiš, kdy dává v praxi smysl vlastní implementace a kdy je lepší použít vestavěné řazení.

---

### 2.2 Další řadicí algoritmy

Pro přehled uvádíme několik dalších základních algoritmů řazení s jejich asymptotickou časovou a prostorovou složitostí. Není nutné znát je zpaměti. Důležitější je vědět, že různé algoritmy se hodí pro různé typy dat a různé situace.

| Algoritmus | Nejlepší scénář | Nejhorší scénář | Průměrný scénář | Prostorová složitost |
| --- | --- | --- | --- | --- |
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| Heap Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ |
| Radix Sort | $O(nk)$ | $O(nk)$ | $O(nk)$ | $O(n + k)$ |
| Quick Sort | $O(n \log n)$ | $O(n^2)$ | $O(n \log n)$ | $O(n \log n)$ |

> **💡 Poznámka:** U různých implementací on-line si dávej pozor na kvalitu řešení. To, že nějaký kód „funguje“, ještě neznamená, že skutečně odpovídá deklarované asymptotické složitosti.

---
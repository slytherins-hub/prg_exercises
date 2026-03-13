# CVIČENÍ 11: ŘADICÍ ALGORITMY

Algoritmizace a programování

## ÚVOD

V minulém cvičení ses už seznámil s asymptotickou složitostí a s tím, proč záleží na tom, jak rychle algoritmus roste s velikostí vstupu.

Teď to využiješ na další velmi důležitou oblast: **řazení dat**.

Řadicí algoritmy mají za úkol uspořádat čísla, seznamy nebo jiné hodnoty do správného pořadí, třeba od nejmenšího po největší. Se seřazenými daty se pak mnohem lépe pracuje a často jsou důležité i pro další algoritmy, například pro vyhledávání.

Jednodušší řadicí algoritmy bývají krátké, dobře pochopitelné a řadí přímo uvnitř seznamu. Často ale mají časovou složitost typu $O(n^2)$, takže se hodí hlavně tam, kde není dat příliš mnoho. Sofistikovanější algoritmy dokážou pracovat rychleji, typicky kolem $O(n \log n)$.

### Co se v tomto cvičení naučíte?

1. **Stabilní a nestabilní řazení:**

- co znamená stabilita algoritmu,
- kdy je důležitá a kdy na ní nezáleží.

2. **Tři klasické řadicí algoritmy:**

- Selection Sort,
- Bubble Sort,
- Insertion Sort.

3. **Analýza složitosti řazení:**

- nejlepší a nejhorší scénář,
- porovnání algoritmů mezi sebou,
- vliv konkrétních operací nad seznamem.

4. **Řazení v Pythonu:**

- rozdíl mezi `sort()` a `sorted()`,
- jak fungují argumenty `reverse` a `key`,
- proč je interní řazení v Pythonu v praxi často nejlepší volba.

### Jak tímhle cvičením projít prakticky

1. Nejprve si připrav repozitář a data pro dnešní cvičení.
2. U každého algoritmu si nejdřív projdi princip na obrázku a teprve pak ho implementuj.
3. Po každé implementaci si funkci hned ověř na několika krátkých seznamech.
4. U analýzy se snaž přemýšlet, kolik porovnání nebo posunů algoritmus provede v nejlepším a nejhorším případě.
5. Nakonec porovnej vlastní implementace s tím, jak řazení řeší přímo Python.

> **💡 Tip:** U řadicích algoritmů se vyplatí vzít si papír a projít si několik kroků ručně. Často pak hned pochopíš, proč je jeden algoritmus rychlejší nebo stabilnější než jiný.

---
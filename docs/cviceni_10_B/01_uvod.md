# CVIČENÍ 10B: ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## ÚVOD

V minulém cvičení ses seznámil s algoritmy vyhledávání a s tím, jak analyzovat jejich časovou složitost. Dnes na to navážeš ze dvou stran najednou.

Nejprve přidáš k vyhledávání druhou klasickou úlohu — **řazení dat**. Se seřazenými hodnotami se pracuje mnohem pohodlněji a jsou základem pro efektivní vyhledávání. Podíváš se na jeden z nejjednodušších řadicích algoritmů (**Bubble Sort**) a hned poté na to, jak řazení řeší samotný Python.

Druhou částí cvičení je úvod do **objektově orientovaného programování (OOP)**. Jde o přístup, ve kterém data a operace nad nimi drží pohromadě v jednom balíčku — ve **třídě**. Až dosud jsi pracoval převážně s funkcemi, které dostávaly data jako argumenty. Teď uvidíš, jak se práce zjednoduší, když si data „pamatuje" samotný objekt.

Obě části propojíme jednou úlohou: evidencí bodů z testu. Napíšeš si k ní vlastní třídu `Data`, do které postupně doplníš vyhledávání (jako v minulém cvičení) i řazení pomocí Bubble Sortu.

### Co se v tomto cvičení naučíš?

1. Jak funguje řadicí algoritmus Bubble Sort.
2. Jak v Pythonu řadit pomocí `sort()` a `sorted()`, včetně argumentů `reverse` a `key`.
3. Co jsou třídy, objekty, atributy a metody.
4. K čemu slouží `__init__` a `self`.
5. Jak navrhnout vlastní třídu `Data` pro evidenci bodů z testu a doplnit do ní metody pro hledání a řazení.

### Jak tímhle cvičením projít prakticky

1. Úplně na začátku si vytvoř nový prázdný repozitář na GitHubu a naklonuj ho — postup najdeš v sekci [Odevzdání úkolu](02_odevzdani.md). Budeš mít hned kam commitovat.
2. Selection Sort si napíšeme společně na cvičení — doma ho nepiš.
3. Implementuj a vyzkoušej Bubble Sort jako samostatnou funkci.
4. Porovnej svou implementaci s vestavěným řazením v Pythonu.
5. Projdi si teorii OOP — na jednoduchém příkladu si uvědom, co je `__init__`, `self` a metoda.
6. Teprve potom se pusť do třídy `HodnoceniStudentu` a postupně ji rozšiřuj o nové metody.
7. Průběžně commituj, na konci nahraj finální verzi a odevzdej odkaz do e-learningu.

> **💡 Tip:** U Bubble Sortu se vyplatí vzít si papír a projít si pár kroků ručně — hned pak vidíš, proč se největší hodnota každou iterací „probublává" na konec seznamu.

---

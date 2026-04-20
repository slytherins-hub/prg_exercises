# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## ÚVOD

V minulém cvičení ses seznámil s algoritmy vyhledávání a s tím, jak analyzovat jejich časovou složitost. 
Dnes na to navážeme v několika směrech.

Nejprve přidáš k vyhledávání druhou klasickou úlohu — **řazení dat**. Se seřazenými hodnotami se pracuje mnohem 
pohodlněji a jsou základem pro efektivní vyhledávání. Podíváš se na jedny z nejjednodušších řadicích algoritmů 
(**Selection Sort** a **Bubble Sort**) a hned poté na to, jak řazení řeší samotný Python.

Druhou částí cvičení je úvod do **objektově orientovaného programování (OOP)**. Jde o přístup, ve kterém data a operace
nad nimi drží pohromadě v jednom balíčku — ve **třídě**. Až dosud jsi pracoval převážně s funkcemi, které dostávaly data
jako argumenty. Teď uvidíš, jak se práce zjednoduší, když si data „pamatuje" samotný objekt.

Obě části propojíme jednou úlohou: evidencí bodů z testu. Napíšeš si k ní vlastní třídu `Data`, do které postupně doplníš vyhledávání (jako v minulém cvičení) i řazení pomocí Bubble Sortu.

### Co se v tomto cvičení naučíš?

1. Jak fungují řadicí algoritmy Selection Sort a Bubble Sort.
2. Jak v Pythonu řadit pomocí `sort()` a `sorted()`, včetně argumentů `reverse` a `key`.
3. Co jsou třídy, objekty, atributy a metody.
4. K čemu slouží `__init__` a `self`.
5. Jak navrhnout vlastní třídu `Data` pro evidenci bodů z testu a doplnit do ní metody pro hledání a řazení.

### Co je potřeba splnit?

1. Úplně na začátku si vytvoř nový prázdný repozitář na GitHubu a naklonuj ho — postup najdeš v sekci [Odevzdání úkolu](02_odevzdani.md).
2. Implementuj a vyzkoušej Selection Sort jako samostatnou funkci.
3. Pokračuj Bubble Sortem a otestuj ho na náhodných datech.
4. Porovnej svou implementaci s vestavěným řazením v Pythonu.
5. Projdi si teorii OOP — na jednoduchém příkladu si uvědom, co je `__init__`, `self` a metoda.
6. Teprve potom se pusť do třídy `StudentsGrades` a postupně ji rozšiřuj o nové metody.
7. Průběžně commituj, na konci nahraj finální verzi a odevzdej odkaz do e-learningu.

---

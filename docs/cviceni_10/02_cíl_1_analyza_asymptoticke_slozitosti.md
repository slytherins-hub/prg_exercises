# CVIČENÍ 10: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## CÍL 1: ANALÝZA ASYMPTOTICKÉ SLOŽITOSTI

### ANALÝZA ASYMPTOTICKÉ SLOŽITOSTI

Odhad řádu růstu funkce $g(n)$ zkoumaného algoritmu lze provést řadou různých způsobů. Mezi základní řadíme například:

- $f(n) = O(g(n))$ – Big O notation  
	**Asymptotická horní mez** – algoritmus pro jakákoliv vstupní data asymptoticky nepřesáhne stanovenou funkci.

- $f(n) = \Omega(g(n))$ – Big Omega notation  
	**Asymptotická dolní mez** – algoritmus pro jakákoliv vstupní data asymptoticky nedosáhne lepší složitosti než je stanovená funkce.

- $f(n) = \Theta(g(n))$ – Big Theta notation  
	**Asymptotická těsná mez** – kde platí zároveň $O$ i $\Omega$.

Nás bude zajímat zejména odhad složitosti v nejhorším možném scénáři.
V tomto případě postupujeme zpravidla tak, že:

1. zanedbáme členy funkce $g(n)$ rostoucí stejně rychle nebo pomaleji než člen s nejrychlejším růstem,
2. zanedbáme konstanty funkce $g(n)$.

> **💡 Poznámka:** V praxi je kromě asymptotické složitosti nutné zohlednit také další parametry. Někdy tak může být výhodnější použít algoritmus s horší asymptotickou složitostí:
>
> - **Složitá implementace**  
>   Algoritmy s lepší asymptotickou složitostí jsou často více komplikované a mohou zvýšit čas potřebný na implementaci.
>
> - **Malá velikost vstupních dat**  
>   Pro malou velikost vstupních dat může vzrůst vliv konstant a výrazů nižšího řádu, které jsou u asymptotické složitosti zanedbány. Algoritmus s vyšší asymptotickou složitostí tedy může výpočetně překonat asymptoticky jednodušší algoritmus.
>
> - **Rozdíly mezi průměrným a nejhorším scénářem**  
>   V určitých případech může být výhodnější zvolit algoritmus, který má vyšší asymptotickou složitost pro nejhorší scénář, ale relativně nízkou složitost průměrnou (např. když víme, že nejhorší scénář nenastává příliš často). Naopak v kritických situacích (např. kontrolní systémy letadel) můžeme preferovat algoritmus s nižší průměrnou složitostí, pokud je jeho asymptotická složitost v nejhorším případě lepší než u jiného řešení.

---

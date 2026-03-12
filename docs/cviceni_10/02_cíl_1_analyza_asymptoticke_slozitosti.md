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

Nejvíc nás bude zajímat odhad složitosti v nejhorším možném scénáři.
V tom případě obvykle postupuješ tak, že:

1. zanedbáme členy funkce $g(n)$ rostoucí stejně rychle nebo pomaleji než člen s nejrychlejším růstem,
2. zanedbáme konstanty funkce $g(n)$.

> **💡 Poznámka:** V praxi je kromě asymptotické složitosti potřeba zohlednit i další parametry. Někdy tak může být výhodnější použít algoritmus s horší asymptotickou složitostí:
>
> - **Složitá implementace**  
>   Algoritmy s lepší asymptotickou složitostí bývají často složitější a mohou výrazně zvýšit čas potřebný na implementaci.
>
> - **Malá velikost vstupních dat**  
>   U malé velikosti vstupních dat může vzrůst vliv konstant a výrazů nižšího řádu, které se v asymptotické složitosti zanedbávají. Algoritmus s vyšší asymptotickou složitostí tak může v praxi běžet rychleji než asymptoticky jednodušší algoritmus.
>
> - **Rozdíly mezi průměrným a nejhorším scénářem**  
>   V určitých situacích může být výhodnější algoritmus, který má horší asymptotickou složitost pro nejhorší scénář, ale relativně nízkou složitost průměrnou, třeba když víš, že nejhorší scénář nastává jen zřídka. Naopak v kritických aplikacích může být důležitější chování v nejhorším případě než průměrný výkon.

---

# CVIČENÍ 10: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## ÚVOD

Čas, potřebný pro zpracování dat pomocí konkrétního algoritmu, zpravidla narůstá v závislosti na množství dat, které je nutné zpracovat (vliv má samozřejmě také konkrétní počítač, spuštěné procesy a další parametry). Aby bylo možné určit alespoň přibližný odhad výpočetního času, využívá se odhadu růstu funkce, která popisuje složitost v závislosti na velikosti vstupních dat. V algoritmizaci a programování se jedná o důležité téma, neboť nám umožňuje odpovědět na základní otázky:

- Jak dlouho program poběží pro zadaná vstupní data?
- Kolik paměťového prostoru program využije?
- Je zadaný problém řešitelný v požadovaném čase?

Schopnost analyzovat složitost algoritmu umožňuje programátorům porovnat mezi sebou více algoritmů a rozhodnout, který z nich pro daný problém použít, aby navržené řešení bylo maximálně výpočetně efektivní (asi nikdo z nás by nechtěl několik vteřin či dokonce minut čekat na odezvu programů, které denně používáme). Odhad složitosti algoritmu lze provést jak pro výpočetní čas, tak pro paměťové nebo jiné prostředky.

V téhle lekci si vyzkoušíš základy analýzy asymptotické složitosti na algoritmech vyhledávání. Jde o algoritmy, které jsou základem naprosté většiny programů a využíváš je prakticky na denní bázi, třeba při vyhledávání přes Google.

V praxi se jen málokdy setkáš s potřebou implementovat tyto algoritmy úplně od nuly, protože podobné operace často nabízí standardní knihovny, hotové metody nebo vhodně zvolené datové struktury. Jde ale o principiálně jednoduché postupy, na kterých se vliv asymptotické náročnosti na běh programu vysvětluje velmi dobře. Základní orientace mezi těmito algoritmy ti navíc pomůže zvolit vhodné řešení podle dat a problému, který řešíš. V kombinaci s vhodnou datovou strukturou tak můžeš **zrychlit program o několik řádů**.

### Co se v tomto cvičení naučíte?

1. Jak odhadovat asymptotickou složitost algoritmu.
2. Jak funguje sekvenční vyhledávání v neseřazeném seznamu.
3. Jak funguje vyhledávání vzorů v sekvenci.
4. Jak funguje binární vyhledávání na seřazeném seznamu.
5. Jak porovnat nejlepší a nejhorší scénář u různých algoritmů vyhledávání.

---

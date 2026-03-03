# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou pro ty, kteří chtějí procvičit nabyté znalosti nad rámec povinných úkolů.

### BONUS 1: Validátor rodného čísla

Napište program pro kontrolu českého rodného čísla a extrakci informací z něj.

**Zadání:**

1. Načtěte rodné číslo od uživatele pomocí `input()`
2. Zkontrolujte základní validitu:

 - Délka musí být přesně 10 znaků
 - Všechny znaky musí být číslice (použijte metodu `.isdigit()`)
3. Pokud je validní, extrahujte informace:

 - Rok narození: První 2 znaky (např. "95")
 - Měsíc: Znaky 2-4 (např. "01" pro muže, "51" pro ženy - u žen +50)
 - Den: Znaky 4-6 (např. "15")
4. Určete pohlaví:

 - Pokud je měsíc > 50, jedná se o ženu (odečtěte 50 od měsíce)
 - Jinak muž
5. Vypište výsledek:
 ```
 === ANALÝZA RODNÉHO ČÍSLA ===
 Rodné číslo: 9501152345
 Platnost: VALIDNÍ

 Datum narození: 15.01.1995
 Pohlaví: Muž

 Kontrolní součet: PLATNÝ
 ```

**Bonusová část:** Zkontrolujte dělitelnost 11:

- Převeďte rodné číslo na `int` a zkontrolujte: `int(birth_num) % 11 == 0`

---

### BONUS 2: Analýza a čištění lékařských záznamů

Napište program pro zpracování CSV dat z databáze pacientů.

**Zadání:**

1. Vytvořte string s CSV daty (každý řádek = jeden pacient):

 ```python
 data = """ JAN NOVÁK , 9501152345, DIABETES
 MARIE SVOBODOVÁ,9652253456,HYPERTENZE
 PETR Dvořák,8803154567, Astma """
 ```

2. Rozdělte data na jednotlivé řádky pomocí `.split("\n")`
3. Pro každý řádek:

	 - Rozdělte na části pomocí `.split(",")`
	 - Očistěte každou část:
		 - Odstraňte mezery (`.strip()`)
		 - Převeďte jméno na title case (první písmeno každého slova velké)
		 - Normalizujte diagnózu na malá písmena
	 - Validujte rodné číslo:
		 - Zkontrolujte délku (musí být 10)
		 - Zkontrolujte, zda obsahuje pouze číslice
	 - Vypište ve formátu:

 ```
 Pacient 1: Jan Novák
 RČ: 9501152345 [VALIDNÍ]
 Diagnóza: diabetes

 Pacient 2: Marie Svobodová
 RČ: 9652253456 [VALIDNÍ]
 Diagnóza: hypertenze

 Pacient 3: Petr Dvořák
 RČ: 8803154567 [VALIDNÍ]
 Diagnóza: astma
 ```

4. Na konci vypište statistiku:

	 - Počet zpracovaných pacientů
	 - Počet validních/nevalidních rodných čísel
	 - Seznam všech unikátních diagnóz (bonus: použijte `set()`)

**Hint:** Pro rozdělení víceřádkového stringu:
```python
lines = data.split("\n")
for i, line in enumerate(lines, start=1):
 parts = line.split(",")
 name = parts[0].strip().title()
 # ... pokračuj zpracováním
```


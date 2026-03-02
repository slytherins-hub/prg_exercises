# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou pro ty, kteří chtějí procvičit nabyté znalosti nad rámec povinných úkolů.

### BONUS 1: Analýza krevního tlaku

Napište program pro vyhodnocení krevního tlaku pacientů.

**Zadání:**

1. Vytvořte dva seznamy:

 - `systolic = [120, 140, 135, 110, 155, 125, 145]` (horní tlak)
 - `diastolic = [80, 90, 85, 70, 95, 82, 92]` (dolní tlak)
2. Vytvořte konstanty:

 - `NORMAL_SYS_LIMIT = 130` (hranice normálního horního tlaku)
 - `NORMAL_DIA_LIMIT = 85` (hranice normálního dolního tlaku)
3. Vytvořte počítadla: `normal_count = 0`, `high_count = 0`
4. Projděte všechny měření pomocí `range(len(systolic))`:

 - Vypište: `"Pacient X: 120/80 mmHg"`
 - Pokud je **ALESPOŇ JEDNO** z měření mimo normu (systolic >= 130 **nebo** diastolic >= 85):

 - Vypište: `" Zvýšený tlak"`
 - Zvyšte `high_count`
 - Jinak:

 - Vypište: `" Normální"`
 - Zvyšte `normal_count`
5. Na konci vypište statistiku:
 ```
 === SOUHRN ===
 Normální tlak: X pacientů
 Zvýšený tlak: Y pacientů
 ```

 **Použijte:** dva seznamy, indexaci, `range()`, logický operátor `or`, f-stringy

---

### BONUS 2: Výpočet průměrné srdeční frekvence

Napište program, který spočítá průměrnou srdeční frekvenci a najde extrémní hodnoty (minimální a maximální).

**Zadání:**

1. Vytvořte seznam měření: `heart_rates = [72, 85, 68, 105, 78, 92, 70, 88]`
2. Inicializujte proměnné:

 - `total = 0` (pro součet všech hodnot)
 - `min_rate = heart_rates[0]` (minimální hodnota - nejprve přiřadíme první hodnotu)
 - `max_rate = heart_rates[0]` (maximální hodnota - nejprve přiřadíme první hodnotu)
3. Projděte všechna měření cyklem:

 - Přičtěte hodnotu k `total`
 - Pokud je hodnota menší než `min_rate`, aktualizujte `min_rate`
 - Pokud je hodnota větší než `max_rate`, aktualizujte `max_rate`
4. Vypočítejte průměr: `average = total / len(heart_rates)`
5. Vypište výsledky:
 ```
 === ANALÝZA SRDEČNÍ FREKVENCE ===
 Počet měření: 8
 Průměrná hodnota: 82.2 tepů/min
 Minimum: 68 tepů/min
 Maximum: 105 tepů/min
 ```

 **Použijte:** seznamy, cyklus, podmínky, matematické operace, `len()`, formátování na 1 desetinné místo

**Hint:** Pro výpis s 1 des. místem: `f"{average:.1f}"`

---


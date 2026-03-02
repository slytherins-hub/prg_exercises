# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## ZÁVĚREČNÉ ÚKOLY

Nyní si vyzkoušíte vše, co jste se naučili v tomto cvičení. Vytvořte si nový soubor pro každý úkol.

### ÚKOL 1: Analýza teplot na oddělení

Napište program, který analyzuje teploty pacientů na oddělení za jeden den.

**Zadání:**

1. Vytvořte seznam měření: `temperatures = [36.6, 38.5, 37.2, 39.1, 36.9, 38.2, 37.5, 40.1]`
2. Vytvořte konstanty:

 - `FEVER_LIMIT = 38.0` (hranice pro horečku)
 - `HIGH_FEVER_LIMIT = 39.5` (hranice pro vysokou horečku)
3. Vytvořte počítadla: `normal_count = 0`, `fever_count = 0`, `high_fever_count = 0`
4. Projděte všechny teploty cyklem a pro každou:

 - Pokud je >= HIGH_FEVER_LIMIT: zvyšte `high_fever_count`
 - Pokud je >= FEVER_LIMIT (ale < HIGH_FEVER_LIMIT): zvyšte `fever_count`
 - Jinak: zvyšte `normal_count`
5. Vypište statistiku:
 ```
 === ANALÝZA TEPLOT ===
 Celkem měření: 8
 Normální teplota: 3
 Horečka: 3
 Vysoká horečka: 2
 ```

 **Použijte:** seznamy, cykly, podmínky, operátor `+=`, f-stringy

---

### ÚKOL 2: Kontrola BMI pacientů

Napište program, který vyhodnotí BMI (Body Mass Index) pro seznam pacientů.

**Zadání:**

1. Vytvořte seznamy:

 - `weights = [75, 68, 92, 58, 80]` (váhy v kg)
 - `heights = [1.80, 1.65, 1.90, 1.60, 1.75]` (výšky v metrech)
2. Vytvořte počítadlo: `overweight_count = 0`
3. Projděte všechny pacienty pomocí `range(5)`:

 - Vypočítejte BMI: `bmi = weights[i] / (heights[i] ** 2)`
 - Vypište: `"Pacient 1: BMI = 23.1"`
 - Pokud je BMI >= 25: zvyšte `overweight_count`
4. Na konci vypište: `"Počet pacientů s nadváhou: X"`

 **Použijte:** seznamy, indexaci, cyklus `range()`, matematické operace, podmínky

**Vzorec:** BMI = váha / (výška²)
**Hranice:** BMI >= 25 znamená nadváhu

---


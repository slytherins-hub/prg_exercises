# TODO: Self-check testy do zbývajících cvičení

## Kontext

Některá cvičení už mají na konci sekci **SELF-CHECK: PROCVIČENÍ ZNALOSTÍ**
(cv01, cv02, cv03, cv04, cv05, cv06, cv09). Ve zbývajících cvičeních
(**cv07, cv10, cv11, cv12, cv13**) tato sekce chybí a je potřeba ji
doplnit.

## Co udělat pro každé cvičení

1. **Důkladně projít CELÉ cvičení** – všechny soubory ve složce
   `docs/cviceni_XX/`. To znamená nejen úvod a hlavní soubory, ale
   všechny cíle, doplňky, README, případně i `.ipynb` notebooky a další
   doprovodné materiály. Pochopit, co se v cvičení učí, jaké koncepty
   jsou klíčové, na čem mohou studenti chybovat.
2. **Vymyslet otázky podle skutečného obsahu** – otázky musí pokrývat
   to, co studenti v cvičení reálně dělají a učí se. Žádné obecné
   Python otázky, které s daným cvičením nesouvisí.
3. **Dodržet formát ze stávajících self-checků** – viz dále.
4. **Vytvořit nový soubor** v dané složce s číslem za posledním
   existujícím:
   - `docs/cviceni_07/05_self_check_procvičení_znalostí.md`
   - `docs/cviceni_10/08_self_check_procvičení_znalostí.md`
   - `docs/cviceni_11/08_self_check_procvičení_znalostí.md`
   - `docs/cviceni_12/06_self_check_procvičení_znalostí.md`
   - `docs/cviceni_13/11_self_check_procvičení_znalostí.md`
5. **Přidat položku do navigace** v `mkdocs.yml` (do bloku daného
   cvičení, na konec).

## Formát self-checku

V repu existují dva varianty formátu. Pro nová cvičení použij **HTML
variantu** (jako v cv04, cv05, cv06) – je čitelnější a v kurzu
převažuje v novějších cvičeních.

### Hlavička souboru

```markdown
# CVIČENÍ X: NÁZEV CVIČENÍ

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Název tematického bloku
```

### Otázka s výběrem (HTML formát)

```markdown
1. **Otázka?**
   <ol type="a">
      <li>první možnost</li>
      <li>druhá možnost</li>
      <li>třetí možnost</li>
      <li>čtvrtá možnost</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Vysvětlení proč je správná možnost c)

</details>
```

### Otázka s kódem

````markdown
2. **Co vypíše tento kód?**
   ```python
   x = [1, 2, 3]
   print(x[1])
   ```
   <ol type="a">
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>Chybu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> 2 (indexuje se od 0)

</details>
````

## Pravidla pro otázky

- **Rozsah:** 15–25 otázek na cvičení (podle množství obsahu).
- **Členění:** rozdělit do **Částí A, B, C…** podle tematických celků
  (např. "Část A: NumPy základy", "Část B: Matplotlib", …).
- **Typy otázek:**
  - výběr z 4 možností (a–d) – většina otázek
  - "Co vypíše tento kód?" s kódovým blokem
  - "Najdi chybu" – studenti dostanou vadný kód a hádají, co je špatně
  - "Doplň kód" – uvidí kostru s `___` a mají napsat doplnění
- **Správné odpovědi rovnoměrně rozhozené** mezi a, b, c, d.
  **NESMÍ být všechny b)** – v repu se to už jednou řešilo, viz commit
  `47fead9`.
- **Odpověď v `<details>`** musí obsahovat krátké vysvětlení, ne jen
  písmeno – studenti si tak prověří, že chápou *proč*.
- **Český jazyk**, tykání studentovi (jako ve stávajících self-checcích).

## Aktualizace mkdocs.yml

Po vytvoření souboru přidej do `mkdocs.yml` do sekce daného cvičení
na konec (před další cvičení) položku ve formátu:

```yaml
  - Cvičení X:
    # ... existující položky ...
    - Self-check – procvičení znalostí: cviceni_XX/YY_self_check_procvičení_znalostí.md
```

## Reference – existující self-checky

Před prací si projdi alespoň 2–3 z těchto souborů, ať vidíš styl,
hloubku a typy otázek:

- `docs/cviceni_04/08_self_check_procvičení_znalostí.md` – HTML formát, různé typy
- `docs/cviceni_05/08_self_check_procvičení_znalostí.md` – HTML formát, dlouhý, dobré členění
- `docs/cviceni_06/06_self_check_procvičení_znalostí.md` – HTML formát, kratší
- `docs/cviceni_02/11_self_check_procvičení_znalostí.md` – markdown formát, hodně typů
- `docs/cviceni_01/09_self_check_procvičení_znalostí.md` – markdown formát, "Najdi chybu", "Doplň kód"

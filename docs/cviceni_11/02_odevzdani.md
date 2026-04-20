# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## ODEVZDÁNÍ ÚKOLU

V tomto cvičení si zkusíš něco nového: odevzdáš **vlastní nový repozitář** na GitHubu, ne fork. Jde o běžný postup, 
kdy začínáš nový projekt od nuly — třeba školní úkol, osobní experiment nebo vlastní knihovnu.

> **Poznámka:** První dvě části (vytvoření repa + klonování) udělej **hned teď**, než začneš pracovat na úkolech. 
> Ostatní (commit, push, checklist, e-learning) si projdi postupně během cvičení a na jeho konci.

### Vytvoření nového repozitáře na GitHubu

1. Přihlas se na [github.com](https://github.com).
2. Vpravo nahoře klikni na **`+`** a vyber **`New repository`**.
3. Vyplň:
    - **Repository name:** například `prg-exercise-11` (nebo libovolný smysluplný název).
    - **Visibility:** zvol **Public**.
    - Zatrhni **Add a README file** — repozitář se vytvoří s jedním počátečním souborem, aby nebyl úplně prázdný.
4. Klikni **Create repository**.

### Klonování a příprava

1. Na stránce repozitáře klikni na zelené tlačítko **`Code`** a zkopíruj HTTPS adresu.
2. V terminálu přejdi do složky s dnešním cvičením a naklonuj repozitář:

    ```
    git clone <adresa>
    cd <nazev-slozky>
    ```

### Vložení řešení a odevzdání

1. Do naklonované složky zkopíruj nebo rovnou v ní vytvoř:

    - modul `sorting.py` — bude obsahovat funkce `bubble_sort()`, `selection_sort()` a `random_numbers()`,
    - modul `student_grades.py` — bude obsahovat třídu `StudentsGrades` se všemi metodami,
    - modul `main.py` — pro ukázku použití (volitelně můžeš `main()` nechat přímo v `student_grades.py`),
    - soubor `grades.csv` — data třídy, která budeš načítat v `main.py` (stáhni ho z materiálů ke cvičení).

2. Ulož změny do Git historie:

    ```
    git add sorting.py student_grades.py main.py grades.csv
    git commit -m "Řešení cvičení 11"
    git push
    ```

3. Otevři svůj repozitář v prohlížeči a ověř, že se soubory objevily.

> **Tip:** Nečekej s commity až na úplný konec. Je lepší si ukládat rozumné mezikroky průběžně — třeba po dokončení 
> Bubble Sortu, po vytvoření třídy `StudentsGrades`, po dopsání jednotlivých metod.

### Checklist před odevzdáním

Před finálním odevzdáním si odškrtni:

- funkce `bubble_sort()` a `selection_sort()` jsou implementované a fungují na různých vstupech,
- třída `StudentsGrades` obsahuje alespoň `__init__`, `get_score()`, `count()`, `get_grade()`, `find()`, `get_sorted()` a `from_csv()`,
- `main()` ukazuje použití všech metod,
- všechny změny jsou commitnuté a nahrané na GitHub,
- repozitář je **Public** a jde otevřít i z anonymního okna prohlížeče.

### Odevzdání do e-learningu

<h2 style="color:#c62828;">❗❗ POVINNÉ ODEVZDÁNÍ</h2>
<ul style="color:#c62828;">
  <li>Pro splnění cvičení je nezbytné odevzdat do e-learningu funkční odkaz na repozitář.</li>
  <li>Cílem je mít v repozitáři vyplněné všechny úkoly z tohoto cvičení.</li>
  <li>Odevzdání a modifikace v repozitáři je nutné provést nejpozději do půlnoci v den cvičení.</li>
  <li>Ověř, že repozitář je <code>Public</code> a jde otevřít i z anonymního okna prohlížeče.</li>
</ul>

---

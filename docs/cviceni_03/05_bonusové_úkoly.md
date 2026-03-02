# CVIČENÍ 3: FUNKCE A SEZMANY

Algoritmizace a programování

## BONUSOVÉ ÚKOLY

Tyto úkoly jsou pro ty, kteří chtějí procvičit nabyté znalosti nad rámec povinných úkolů.

### Správa databáze pacientů

Napište program pro správu databáze pacientů s vnořenými seznamy a funkcemi.

**Zadání:**

1. Vytvořte funkci `add_patient()`:

 * Funkce přijímá čtyři parametry:

 * databázi typu `list`,
 * jméno pacienta typu `str`,
 * věk pacienta typu `int`,
 * diagnóza typu `str`.
 * Funkce vytvoří nový seznam reprezentující pacienta a přidá ho do databáze jako nový vnořený seznam.
 * Funkce vrátí hodnotu typu `list` představující aktualizovanou databázi.

2. Vytvořte funkci `find_patients_by_diagnosis()`:

 * Funkce přijímá dva parametry:

 * databázi typu `list`,
 * diagnózu typu `str`.
 * Funkce vyhledá v databázi všechny pacienty se zadanou diagnózou bez ohledu na velikost písmen (case-insensitive).
 * Funkce vrátí:

 * hodnotu typu `list` obsahující jména pacientů s požadovanou diagnózou,
 * nebo `None`, pokud žádní pacienti s danou diagnózou nejsou.

3. Vytvořte funkci `average_age_by_diagnosis()`:

 * Funkce přijímá dva parametry:

 * databázi typu `list`,
 * diagnózu typu `str`.
 * Funkce vyhledá v databázi všechny pacienty se zadanou diagnózou a spočítá jejich průměrný věk.
 * Funkce vrátí:

 * hodnotu typu `float` představující průměrný věk,
 * nebo `None`, pokud žádní pacienti s danou diagnózou nejsou.

4. Vytvořte funkci `print_database()`:

 * Funkce přijímá databázi typu `list`.
 * Funkce přehledně vypíše všechny pacienty v databázi (použijte funkci `enumerate()` pro číslování).
 * Funkce nic nevrací (`None`), pouze vypisuje data.

5. Hlavní program:
 ```python
 # Inicializace prázdné databáze
 patients_db = []

 # Přidání pacientů
 patients_db = add_patient(patients_db, "Jan Novák", 45, "Diabetes")
 patients_db = add_patient(patients_db, "Marie Svobodová", 32, "Hypertenze")
 patients_db = add_patient(patients_db, "Petr Dvořák", 28, "Diabetes")
 patients_db = add_patient(patients_db, "Anna Černá", 51, "Hypertenze")
 patients_db = add_patient(patients_db, "Tomáš Novotný", 39, "Diabetes")

 # Výpis databáze
 print("=== DATABÁZE PACIENTŮ ===")
 print_database(patients_db)

 # Vyhledání podle diagnózy
 print("\n=== PACIENTI S DIABETEM ===")
 diabetic_patients = find_patients_by_diagnosis(patients_db, "diabetes")
 for name in diabetic_patients:
 print(f"- {name}")

 # Statistika
 print("\n=== STATISTIKA ===")
 avg_diabetes = average_age_by_diagnosis(patients_db, "diabetes")
 avg_hypertension = average_age_by_diagnosis(patients_db, "hypertenze")
 print(f"Průměrný věk pacientů s diabetem: {avg_diabetes:.1f} let")
 print(f"Průměrný věk pacientů s hypertenzí: {avg_hypertension:.1f} let")
 ```

**Očekávaný výstup:**

```
=== DATABÁZE PACIENTŮ ===
1. Jan Novák (45 let) - Diabetes
2. Marie Svobodová (32 let) - Hypertenze
3. Petr Dvořák (28 let) - Diabetes
4. Anna Černá (51 let) - Hypertenze
5. Tomáš Novotný (39 let) - Diabetes

=== PACIENTI S DIABETEM ===
- Jan Novák
- Petr Dvořák
- Tomáš Novotný

=== STATISTIKA ===
Průměrný věk pacientů s diabetem: 37.3 let
Průměrný věk pacientů s hypertenzí: 41.5 let
```

---


# CVIČENÍ 11: ALGORITMY ŘAZENÍ A ZÁKLADY OOP

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Řadicí algoritmy obecně

1. **Co znamená, že je řadicí algoritmus <i>stabilní</i>?**
   <ol type="a">
      <li>Zachovává relativní pořadí prvků se stejnou hodnotou klíče</li>
      <li>Vždy doběhne v lineárním čase</li>
      <li>Nikdy nespadne na chybu při prázdném seznamu</li>
      <li>Pracuje pouze s celými čísly</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Stabilní algoritmus zachovává původní vzájemné pořadí prvků se stejným klíčem. Důležité je to hlavně tehdy, když řadíš objekty, ne jen samostatná čísla.

</details>

2. **Které dva algoritmy jsi v cvičení implementoval(a) ručně?**
   <ol type="a">
      <li>Quick Sort a Merge Sort</li>
      <li>Selection Sort a Bubble Sort</li>
      <li>Heap Sort a Radix Sort</li>
      <li>Timsort a Insertion Sort</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> V tomhle cvičení jsi naprogramoval(a) Selection Sort (nestabilní) a Bubble Sort (stabilní). Ostatní algoritmy se ve cvičení jen zmiňují v přehledové tabulce.

</details>

3. **Proč u řazení jenom čísel nezáleží na stabilitě algoritmu?**
   <ol type="a">
      <li>Čísla se v Pythonu řadí vždy stabilně</li>
      <li>Dvě stejná čísla od sebe nedokážeš rozlišit, takže výsledek bude stejný</li>
      <li>Selection Sort umí být dočasně stabilní</li>
      <li>Stabilita platí jen u řetězců</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Když máš dvě sedmičky, jsou nerozlišitelné, takže nezáleží, která je v seřazeném výstupu „první“. Stabilita má smysl, když řadíš složitější objekty se stejným klíčem.

</details>

4. **K čemu slouží funkce <code>random_numbers(count, low=0, high=100)</code> z modulu <code>sorting.py</code>?**
   <ol type="a">
      <li>Vrátí jediné náhodné číslo</li>
      <li>Seřadí náhodný seznam</li>
      <li>Vrátí slovník <code>{index: hodnota}</code></li>
      <li>Vrátí seznam <code>count</code> náhodných celých čísel v zadaném rozsahu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Funkce vrací seznam o délce <code>count</code> s náhodnými celými čísly v rozsahu <code>low</code> až <code>high</code> (včetně).

</details>

---

### Část B: Selection Sort

5. **Jaký je hlavní princip Selection Sortu?**
   <ol type="a">
      <li>Opakovaně prohazuje sousední dvojice prvků</li>
      <li>Rozdělí seznam na dvě poloviny a rekurzivně je seřadí</li>
      <li>Použije hash tabulku pro indexaci hodnot</li>
      <li>V každém průchodu najde minimum zbývající části a přesune ho na začátek</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Selection Sort v každém průchodu vyhledá nejmenší prvek v dosud nesetříděné části seznamu a prohodí ho s prvkem na aktuální pozici.

</details>

6. **Jaká je asymptotická časová složitost Selection Sortu v nejhorším případě?**
   <ol type="a">
      <li>$O(n)$</li>
      <li>$O(n^2)$</li>
      <li>$O(n \log n)$</li>
      <li>$O(\log n)$</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Selection Sort prochází vždy zbytek pole pro nalezení minima, takže má kvadratickou složitost $O(n^2)$ v nejhorším i v nejlepším scénáři.

</details>

7. **Proč je Selection Sort považován za <i>nestabilní</i> algoritmus?**
   <ol type="a">
      <li>Protože nepracuje na místě (in-place)</li>
      <li>Protože při velkém vstupu vrací chybný výsledek</li>
      <li>Prohození minima s aktuálním prvkem může přeskočit pořadí dvou stejných hodnot</li>
      <li>Protože používá rekurzi</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Při výměně nalezeného minima s prvkem na aktuální pozici se může relativní pořadí stejných hodnot porušit – proto Selection Sort není stabilní.

</details>

8. **Jak v Pythonu nejelegantněji prohodíš dva prvky seznamu bez pomocné proměnné?**
   <ol type="a">
      <li><code>swap(my_list[1], my_list[3])</code></li>
      <li><code>my_list[1], my_list[3] = my_list[3], my_list[1]</code></li>
      <li><code>my_list[1] = my_list[3]; my_list[3] = my_list[1]</code></li>
      <li><code>my_list.swap(1, 3)</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Python umožňuje výměnu hodnot pomocí jednořádkového rozbalení n-tice: <code>a, b = b, a</code>. To je mnohem čitelnější než řešení s pomocnou proměnnou.

</details>

9. **Co se stane, pokud zapomeneš na začátku <code>selection_sort()</code> vytvořit kopii vstupního seznamu (např. <code>numbers = numbers[:]</code>)?**
   <ol type="a">
      <li>Funkce zhavaruje s <code>TypeError</code></li>
      <li>Python si kopii udělá automaticky, takže se nic špatného nestane</li>
      <li>Funkce vrátí prázdný seznam</li>
      <li>Funkce sice vrátí správný výsledek, ale zároveň změní původní seznam volajícího</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Python předává seznam jako referenci. Když ho v těle funkce upravíš na místě, projeví se to i venku. Cvičení proto vyžaduje, aby původní seznam zůstal beze změny – musíš si vyrobit kopii.

</details>

---

### Část C: Bubble Sort

10. **Jaký je princip Bubble Sortu?**
    <ol type="a">
       <li>V každém kroku najde maximum a vloží ho na začátek</li>
       <li>Opakovaně porovnává sousední dvojice a prohazuje je, pokud jsou ve špatném pořadí</li>
       <li>Pracuje pomocí rozdělení a slučování</li>
       <li>Používá pivot a tři podseznamy</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Bubble Sort projíždí seznam a porovnává každou sousední dvojici, špatně seřazené prohodí. Po každém průchodu se největší zbývající hodnota „probublá“ na konec.

</details>

11. **Jaká může být složitost Bubble Sortu v nejlepším scénáři, pokud algoritmus po průchodu bez jediného prohození ukončí řazení?**
    <ol type="a">
       <li>$O(n^2)$</li>
       <li>$O(\log n)$</li>
       <li>$O(1)$</li>
       <li>$O(n)$</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Pokud je vstupní seznam už seřazený, stačí jeden průchod ($n - 1$ porovnání) a algoritmus zjistí, že nemusí nic prohazovat – složitost je $O(n)$.

</details>

12. **Co vypíše tento kód?**
    ```python
    def bubble_sort(numbers):
        numbers = numbers[:]
        n = len(numbers)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers

    data = [3, 1, 2]
    print(bubble_sort(data))
    print(data)
    ```
    <ol type="a">
       <li><code>[1, 2, 3]</code> a <code>[1, 2, 3]</code></li>
       <li><code>[3, 1, 2]</code> a <code>[1, 2, 3]</code></li>
       <li><code>[1, 2, 3]</code> a <code>[3, 1, 2]</code></li>
       <li><code>[3, 2, 1]</code> a <code>[3, 1, 2]</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Funkce si na začátku vyrobí kopii (<code>numbers = numbers[:]</code>), takže původní seznam <code>data</code> zůstane beze změny <code>[3, 1, 2]</code>, zatímco vrácená seřazená kopie je <code>[1, 2, 3]</code>.

</details>

13. **Proč v Bubble Sortu obvykle nemusíme znovu kontrolovat prvky na konci seznamu?**
    <ol type="a">
       <li>Python si konec optimalizuje sám</li>
       <li>Bubble Sort konec ignoruje pro úsporu paměti</li>
       <li>Konec seznamu je po každém průchodu už seřazený – největší prvek se „probublá“ na konec</li>
       <li>Protože konec seznamu obsahuje vždy <code>None</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> V každém průchodu Bubble Sortu se největší zbývající hodnota dostane na své finální místo na konci. Vnitřní cyklus tak může postupně zkracovat rozsah – obvykle <code>range(n - 1 - i)</code>.

</details>

14. **Co znamená v ukázce vizualizace řádek <code>colors[index_highlight1] = "tomato"</code>?**
    <ol type="a">
       <li>Smaže prvek na dané pozici</li>
       <li>Změní hodnotu prvku v seznamu <code>values</code></li>
       <li>Spustí novou animaci v matplotlibu</li>
       <li>Obarví aktuálně porovnávaný sloupec červeně</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Seznam <code>colors</code> obsahuje barvu pro každý sloupec grafu. Nastavení indexu právě porovnávaného prvku na <code>"tomato"</code> vykreslí ten sloupec červeně, takže ve vizualizaci hned vidíš, které dvě hodnoty algoritmus porovnává.

</details>

---

### Část D: Řazení v Pythonu

15. **Jaký je hlavní rozdíl mezi <code>list.sort()</code> a <code>sorted(list)</code>?**
    <ol type="a">
       <li><code>sort()</code> řadí na místě a nic nevrací; <code>sorted()</code> vrátí nový seznam a originál nemění</li>
       <li>Žádný, jsou to jen dvě jména pro totéž</li>
       <li><code>sort()</code> řadí jen čísla, <code>sorted()</code> jen řetězce</li>
       <li><code>sorted()</code> existuje jen v Pythonu 2</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Metoda <code>sort()</code> mění samotný seznam (in-place) a vrací <code>None</code>. Funkce <code>sorted()</code> vrací nový seřazený seznam a originál nechává beze změny.

</details>

16. **Co vypíše tento kód?**
    ```python
    my_list = [3, 8, 1, 2, 32]
    result = my_list.sort()
    print(result)
    ```
    <ol type="a">
       <li><code>[1, 2, 3, 8, 32]</code></li>
       <li><code>None</code></li>
       <li><code>[3, 8, 1, 2, 32]</code></li>
       <li>Vyhodí <code>TypeError</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Metoda <code>sort()</code> řadí na místě a nic nevrací – návratová hodnota je <code>None</code>. Pokud chceš výsledek do nové proměnné, použij <code>sorted()</code>.

</details>

17. **Co dělá argument <code>reverse=True</code> u <code>sorted()</code>?**
    <ol type="a">
       <li>Otočí pořadí prvků bez řazení</li>
       <li>Použije rychlejší algoritmus</li>
       <li>Spustí <code>sorted()</code> dvakrát</li>
       <li>Seřadí seznam sestupně (od největšího k nejmenšímu)</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> S <code>reverse=True</code> se data seřadí sestupně. Výchozí je <code>reverse=False</code>, tj. vzestupně.

</details>

18. **Co vypíše tento kód?**
    ```python
    list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
    print(sorted(list_of_words, key=len))
    ```
    <ol type="a">
       <li><code>['BZZZZZZ', 'meeeoow', 'woof', 'MOO']</code></li>
       <li><code>['MOO', 'BZZZZZZ', 'meeeoow', 'woof']</code></li>
       <li><code>['MOO', 'woof', 'meeeoow', 'BZZZZZZ']</code></li>
       <li><code>['woof', 'MOO', 'BZZZZZZ', 'meeeoow']</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Argument <code>key=len</code> řadí prvky podle jejich délky vzestupně: 3, 4, 7, 7 znaků. Výsledek je <code>['MOO', 'woof', 'meeeoow', 'BZZZZZZ']</code>.

</details>

19. **Jaký řadicí algoritmus používá Python interně pro <code>sort()</code> a <code>sorted()</code>?**
    <ol type="a">
       <li>Timsort</li>
       <li>Bubble Sort</li>
       <li>Quick Sort</li>
       <li>Radix Sort</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Python používá <b>Timsort</b> – stabilní hybridní algoritmus odvozený od Merge Sortu a Insertion Sortu. Jeho průměrná i nejhorší složitost je $O(n \log n)$.

</details>

---

### Část E: Základy OOP

20. **Co je to <i>třída</i> v objektovém programování?**
    <ol type="a">
       <li>Šablona, podle které se vytvářejí objekty</li>
       <li>Konkrétní instance objektu</li>
       <li>Speciální typ funkce bez návratové hodnoty</li>
       <li>Synonymum pro modul Pythonu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Třída je „šablona“ – předpis, podle kterého se dají vyrábět konkrétní objekty (instance). Sama o sobě ještě data neuchovává.

</details>

21. **K čemu v Pythonu slouží speciální metoda <code>__init__</code>?**
    <ol type="a">
       <li>Maže objekt z paměti</li>
       <li>Inicializuje atributy objektu při jeho vytvoření</li>
       <li>Importuje modul</li>
       <li>Vrací textovou reprezentaci objektu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Python <code>__init__</code> volá automaticky při vytvoření nového objektu. Slouží k inicializaci atributů – typicky přiřazení parametrů na <code>self.něco</code>.

</details>

22. **Co znamená parametr <code>self</code> v metodách?**
    <ol type="a">
       <li>Globální slovník Pythonu</li>
       <li>Klíčové slovo Pythonu, které nelze přejmenovat</li>
       <li>Odkaz na konkrétní instanci, na které byla metoda zavolána</li>
       <li>Speciální typ podobný <code>None</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>self</code> je odkaz na konkrétní objekt, který volá metodu. Díky němu metoda ví, ke kterým datům (atributům) má přistupovat. Při volání metody (<code>obj.metoda()</code>) ho Python doplňuje sám.

</details>

23. **Jaký je rozdíl mezi atributem a metodou?**
    <ol type="a">
       <li>Atribut je hodnota uložená v objektu (čte se bez závorek), metoda je funkce patřící objektu (volá se se závorkami)</li>
       <li>Atribut čteš s parametry, metoda bez nich</li>
       <li>Atribut existuje jen v <code>__init__</code>, metoda všude jinde</li>
       <li>Není mezi nimi rozdíl</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Atributy jsou data uložená v objektu (<code>r.width</code>) – čteš je bez závorek. Metody jsou akce nad objektem (<code>r.area()</code>) – musíš použít závorky, jinak Pythonu jen vrátí samotnou funkci.

</details>

24. **Která konvence pojmenování platí v Pythonu pro <i>třídy</i>?**
    <ol type="a">
       <li>VŠE_VELKÝMI</li>
       <li>kebab-case</li>
       <li>camelCase</li>
       <li>PascalCase (např. <code>Rectangle</code>, <code>StudentsGrades</code>)</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Třídy se v Pythonu zapisují v <code>PascalCase</code> – velké písmeno na začátku každého slova. Funkce, proměnné, metody i atributy naopak v <code>snake_case</code>.

</details>

25. **Najdi chybu v kódu:**
    ```python
    class Rectangle:
        def __init__(width, height):
            self.width = width
            self.height = height
    ```
    <ol type="a">
       <li>Třída musí mít jiné jméno než <code>Rectangle</code></li>
       <li><code>__init__</code> má pouze jedno podtržítko</li>
       <li>Chybí parametr <code>self</code> jako první parametr <code>__init__</code></li>
       <li>Atributy nelze nastavit přes <code>self.něco</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Každá metoda třídy musí mít jako první parametr <code>self</code>, jinak Python neví, kam má atributy uložit. Správně je <code>def __init__(self, width, height):</code>.

</details>

26. **Co je výsledkem volání <code>r.area()</code> u objektu třídy <code>Rectangle</code> vytvořeného jako <code>r = Rectangle(3, 5)</code>?**
    ```python
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height
    ```
    <ol type="a">
       <li><code>8</code></li>
       <li><code>15</code></li>
       <li><code>None</code></li>
       <li>Vyhodí chybu, protože chybí argument</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Metoda <code>area()</code> vrací <code>self.width * self.height</code>, tedy <code>3 * 5 = 15</code>. Argument <code>self</code> Python doplňuje automaticky.

</details>

---

### Část F: Třída StudentsGrades

27. **Co dělá metoda <code>count()</code> ve třídě <code>StudentsGrades</code>?**
    <ol type="a">
       <li>Spočítá průměrné skóre</li>
       <li>Spočítá počet studentů, kteří dostali A</li>
       <li>Vrátí pořadí studenta v žebříčku</li>
       <li>Vrátí počet studentů (délku <code>self.scores</code>)</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Metoda jen vrátí <code>len(self.scores)</code>, tedy počet studentů v evidenci. Není to počítadlo žádné konkrétní vlastnosti.

</details>

28. **Jakou písmennou známku vrátí <code>get_grade()</code> pro studenta s 67 body podle ECTS tabulky v cvičení?**
    <ol type="a">
       <li>C</li>
       <li>E</li>
       <li>D</li>
       <li>F</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Podle tabulky 60–69 bodů odpovídá známce <b>D</b>. (90+ A, 80+ B, 70+ C, 60+ D, 50+ E, 0–49 F.)

</details>

29. **Co vrátí volání <code>results.find(50)</code> nad objektem <code>results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])</code>?**
    <ol type="a">
       <li><code>50</code></li>
       <li><code>True</code></li>
       <li><code>4</code></li>
       <li><code>[4]</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Metoda <code>find()</code> hledá <b>všechny</b> indexy, na kterých se hledaná hodnota vyskytuje, a vrací je v seznamu. Hodnota <code>50</code> je v seznamu jen jednou, na indexu 4 – výsledek je tedy <code>[4]</code>.

</details>

30. **Co vrátí <code>results.find(77)</code>, pokud žádný student nemá 77 bodů?**
    <ol type="a">
       <li>Prázdný seznam <code>[]</code></li>
       <li><code>None</code></li>
       <li><code>-1</code></li>
       <li>Vyhodí <code>ValueError</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Když metoda <code>find()</code> nenajde žádnou shodu, vrací prázdný seznam <code>[]</code>. To je konzistentní s tím, že obecně vrací seznam všech nalezených indexů.

</details>

31. **Doplň chybějící řádek tak, aby metoda <code>get_sorted()</code> vracela <b>nový</b> seřazený seznam, ale původní <code>self.scores</code> nezměnila:**
    ```python
    def get_sorted(self):
        ___________________
        n = len(scores)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores
    ```
    <ol type="a">
       <li><code>scores = self.scores</code></li>
       <li><code>scores = self.scores.sort()</code></li>
       <li><code>scores = list(self.scores)</code></li>
       <li><code>scores = sorted(self)</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Pouze vytvoření kopie (<code>list(self.scores)</code>, případně <code>self.scores[:]</code> nebo <code>self.scores.copy()</code>) zajistí, že manipulace v metodě nezmění původní atribut. Varianta <code>scores = self.scores</code> by jen přiřadila stejnou referenci a originál by se přepsal.

</details>

32. **Proč je v bonusové metodě <code>find_sorted()</code> rozumné cachovat seřazenou kopii do <code>self._sorted_scores</code>?**
    <ol type="a">
       <li>Cachování je u OOP povinné</li>
       <li>Aby <code>self.scores</code> zůstalo seřazené</li>
       <li>Aby se snížila spotřeba paměti při binárním vyhledávání</li>
       <li>Aby se drahé řazení udělalo jen jednou a další volání byla rychlá</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Bez cache bys řadil seznam při každém volání. Cache (memoizace) ti umožní seřadit jednou a všechna další binární vyhledávání mají složitost $O(\log n)$. Pozor jen – kdyby se <code>self.scores</code> změnilo, je nutné cache invalidovat.

</details>

---

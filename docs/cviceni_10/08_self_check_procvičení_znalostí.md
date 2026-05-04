# CVIČENÍ 10: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Asymptotická složitost

1. **Co popisuje asymptotická složitost algoritmu?**
   <ol type="a">
      <li>Přesnou dobu běhu v sekundách na konkrétním počítači</li>
      <li>Počet řádků kódu, které algoritmus potřebuje</li>
      <li>Jak roste počet operací v závislosti na velikosti vstupu</li>
      <li>Velikost binárního souboru s programem</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Asymptotická složitost neřeší přesný čas, ale popisuje trend růstu počtu operací s rostoucí velikostí vstupu $n$.

</details>

2. **Jakou asymptotickou složitost má následující funkce?**
   ```python
   def compare_all_pairs(values):
       for left in values:
           for right in values:
               print(left, right)
   ```
   <ol type="a">
      <li>$O(n)$</li>
      <li>$O(n^2)$</li>
      <li>$O(\log n)$</li>
      <li>$O(n!)$</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Dva vnořené cykly nad stejnými daty znamenají $n \cdot n = n^2$ kombinací, tedy $O(n^2)$.

</details>

3. **Které tvrzení o zápisech $O$, $\Omega$ a $\Theta$ je správné?**
   <ol type="a">
      <li>Big O je vždy totéž co nejhorší scénář</li>
      <li>Big Omega je vždy totéž co nejlepší scénář</li>
      <li>Big Theta popisuje pouze konstantní funkce</li>
      <li>Big O je horní mez, Big Omega dolní mez a Big Theta těsná mez růstu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> $O$ říká, jak rychle algoritmus poroste maximálně, $\Omega$ jak rychle aspoň, a $\Theta$ ukazuje přesný řád růstu (zároveň horní i dolní mez).

</details>

4. **Co je nejtěsnější (nejpřesnější) zápis pro funkci $2n^2 + 10n + 1$?**
   <ol type="a">
      <li>$O(n^2)$</li>
      <li>$O(n^3)$</li>
      <li>$O(2^n)$</li>
      <li>$O(\log n)$</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Konstanty a pomalejší členy zanedbáváme, dominantní člen je $n^2$. Zápisy jako $O(n^3)$ nebo $O(2^n)$ jsou sice technicky pravdivé, ale nejsou těsné.

</details>

5. **Co znamená složitost $O(\log n)$ z hlediska chování algoritmu?**
   <ol type="a">
      <li>Počet kroků se rovná velikosti vstupu</li>
      <li>V každém kroku zahodíš velkou část problému (typicky polovinu)</li>
      <li>Algoritmus zkouší všechny možné kombinace</li>
      <li>Algoritmus poběží přesně 1 sekundu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Logaritmická složitost vzniká, když se v každém kroku problém zmenší na polovinu (nebo jinou část). Typicky binární vyhledávání.

</details>

6. **Které pořadí tříd složitosti je správné od nejpomaleji rostoucí po nejrychleji rostoucí?**
   <ol type="a">
      <li>$n! < 2^n < n^2 < n < \log n$</li>
      <li>$n < \log n < n^2 < 2^n < n!$</li>
      <li>$\log n < n < n \log n < n^2 < 2^n < n!$</li>
      <li>$n^2 < n < \log n < 2^n < n!$</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Správné orientační pořadí tříd růstu je $1 < \log n < \sqrt{n} < n < n \log n < n^2 < n^3 < 2^n < n!$.

</details>

---

### Část B: Sekvenční vyhledávání

7. **Jaká je asymptotická složitost sekvenčního vyhledávání v neseřazeném seznamu v nejhorším scénáři?**
   <ol type="a">
      <li>$O(1)$</li>
      <li>$O(\log n)$</li>
      <li>$O(n^2)$</li>
      <li>$O(n)$</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> V nejhorším případě (hledaný prvek na konci nebo není v seznamu) musíš projít všech $n$ prvků, tedy $O(n)$.

</details>

8. **Kdy nastane nejlepší scénář u sekvenčního vyhledávání?**
   <ol type="a">
      <li>Když je hledaný prvek hned na začátku seznamu</li>
      <li>Když je seznam seřazený</li>
      <li>Když je seznam prázdný</li>
      <li>Když hledaný prvek v seznamu vůbec není</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> V nejlepším scénáři narazíš na hledaný prvek hned v prvním porovnání, takže algoritmus skončí prakticky okamžitě – složitost je $\Theta(1)$.

</details>

9. **Co podle zadání úkolu má vrátit funkce `linear_search()`?**
   <ol type="a">
      <li>Pouze první nalezený index</li>
      <li>Slovník s klíči `positions` (seznam indexů) a `count` (počet výskytů)</li>
      <li>Pouze počet výskytů jako celé číslo</li>
      <li>Tuple `(index, hodnota)`</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Funkce `linear_search()` vrátí slovník se dvěma klíči – `positions` pro seznam pozic a `count` pro počet výskytů hledaného čísla.

</details>

10. **Proč se sekvenční vyhledávání nazývá také *naivní* algoritmus?**
    <ol type="a">
       <li>Protože se používá jen pro malá data</li>
       <li>Protože byl vymyšlený jako první v historii</li>
       <li>Protože není sofistikovaný ani výpočetně efektivní – prostě prochází všechny prvky</li>
       <li>Protože vždy vrací špatný výsledek</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Algoritmus není nijak chytrý ani efektivní, ale na neseřazených datech může být jediným použitelným řešením.

</details>

11. **Co vrátí funkce `read_data()` z úkolu, pokud zadaný klíč není v množině povolených?**
    <ol type="a">
       <li>Prázdný seznam `[]`</li>
       <li>Vyhodí výjimku `KeyError`</li>
       <li>Celý slovník z JSON souboru</li>
       <li>Hodnotu `None`</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Podle zadání úkolu má funkce při neplatném klíči vrátit `None` – až poté se načítá obsah JSON souboru.

</details>

---

### Část C: Binární vyhledávání

12. **Co je nutnou podmínkou pro použití binárního vyhledávání?**
    <ol type="a">
       <li>Data musí být seřazená</li>
       <li>Data musí být v množině (`set`)</li>
       <li>Data nesmí obsahovat duplicity</li>
       <li>Data musí být uložená v souboru `.json`</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Binární vyhledávání využívá toho, že z prostředního prvku lze rozhodnout, ve které polovině pokračovat – proto musí být data seřazená.

</details>

13. **Jakou asymptotickou složitost má binární vyhledávání v nejhorším scénáři?**
    <ol type="a">
       <li>$O(1)$</li>
       <li>$O(\log n)$</li>
       <li>$O(n)$</li>
       <li>$O(n \log n)$</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Po každém porovnání zůstane k prohledání polovina, čtvrtina, osmina atd. Celkový počet porovnání odpovídá $\log_2 n$, tedy $O(\log n)$.

</details>

14. **Do které skupiny algoritmů spadá binární vyhledávání?**
    <ol type="a">
       <li>Hrubá síla (brute force)</li>
       <li>Greedy algoritmy</li>
       <li>Rozděl a panuj (Divide and Conquer)</li>
       <li>Dynamické programování</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Binární vyhledávání rozděluje problém na menší části (poloviny prohledávané oblasti) a z dílčích řešení skládá celkový výsledek – to je princip Divide and Conquer.

</details>

15. **Proč je podle materiálů lepší držet si při implementaci binárního vyhledávání levý a pravý index místo toho, abys používal slicing seznamu?**
    <ol type="a">
       <li>Slicing v Pythonu vůbec nefunguje na seřazených datech</li>
       <li>S indexy lze prohledávat i řetězce, slicing ne</li>
       <li>Slicing vždy způsobí pád programu</li>
       <li>Slicing vytváří nové části seznamu, takže je méně efektivní; změna indexů je $O(1)$</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Slicing kopíruje data do nového seznamu, což stojí čas i paměť. Změnit dvě čísla (indexy) je naopak konstantní operace.

</details>

---

### Část D: Měření času

16. **Která funkce z modulu `time` je v materiálech doporučená pro jemnější měření krátkých úseků kódu?**
    <ol type="a">
       <li>`time.perf_counter()`</li>
       <li>`time.sleep()`</li>
       <li>`time.localtime()`</li>
       <li>`time.ctime()`</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> `time.perf_counter()` má jemnější rozlišení než běžný `time.time()` a hodí se pro měření krátkých bloků kódu.

</details>

17. **Proč se při měření doporučuje pro každou velikost vstupu provést více pokusů a výsledky zprůměrovat?**
    <ol type="a">
       <li>Protože jinak Python měření odmítne provést</li>
       <li>Protože jednotlivá měření jsou krátká a kolísavá – ovlivňují je další procesy systému</li>
       <li>Protože průměr je vždy přesnější než `perf_counter`</li>
       <li>Protože `matplotlib` přijímá jen průměry</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Krátká měření jsou citlivá na šum systému (jiné běžící procesy, plánovač). Průměr z více pokusů dá stabilnější výsledek.

</details>

18. **Jakou typickou složitost má test členství `x in some_set` v Pythonu a proč?**
    <ol type="a">
       <li>$O(n)$, protože množina prochází prvky jeden po druhém</li>
       <li>$O(\log n)$, protože množina je vnitřně seřazená</li>
       <li>Přibližně $O(1)$, protože množina je postavená na hashovací tabulce</li>
       <li>$O(n^2)$, protože musí porovnat všechny dvojice</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Množina používá hashovací tabulku – z hodnoty se spočítá hash a podle něj se rovnou určí místo. Test členství je proto v průměru konstantní, vykoupený vyšší paměťovou náročností.

</details>

---

### Část E: Vyhledávání vzorů

19. **Jaký princip používá naivní algoritmus vyhledávání vzoru v sekvenci?**
    <ol type="a">
       <li>Vzor seřadí abecedně a pak vyhledá pomocí binárního vyhledávání</li>
       <li>Spočítá hash celé sekvence a porovná ho s hashem vzoru</li>
       <li>Předem rozdělí sekvenci na disjunktní části o délce vzoru</li>
       <li>Postupně posouvá ukazatel po sekvenci o jednu pozici a porovnává podřetězec se vzorem</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Naivní algoritmus nastaví ukazatel na podřetězec délky $m$, porovná ho se vzorem a po každé iteraci posune ukazatel o jednu pozici doprava.

</details>

20. **Jaké je vylepšení naivního algoritmu vyhledávání vzoru popsané v cíli 4?**
    <ol type="a">
       <li>Při nalezení první neshody přerušíme porovnávání a posuneme se na další iteraci</li>
       <li>Vzor zkrátíme jen na první znak</li>
       <li>Sekvenci nejdřív seřadíme podle abecedy</li>
       <li>Použijeme rekurzi místo cyklu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Pokračovat v porovnávání po první neshodě nemá smysl – stačí přerušit vnitřní cyklus a posunout ukazatel o pozici doprava.

</details>

21. **Jaká je asymptotická složitost vylepšeného naivního vyhledávání vzoru v nejhorším scénáři, kde $n$ je délka sekvence a $m$ délka vzoru?**
    <ol type="a">
       <li>$O(n + m)$</li>
       <li>$O(n \cdot m)$</li>
       <li>$O(\log(n \cdot m))$</li>
       <li>$O(m^2)$</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> V nejhorším případě (např. shoda až na poslední znak v každé iteraci) provede algoritmus přibližně $n$ posunů a v každém až $m$ porovnání, dohromady $O(n \cdot m)$.

</details>

---

### Část F: Teoreticky zajímavé algoritmy

22. **Jaký problém řeší Dijkstrův algoritmus?**
    <ol type="a">
       <li>Násobení velkých čísel</li>
       <li>Přiřazení lidí k úlohám s minimální cenou</li>
       <li>Hledání nejkratší cesty v grafu s ohodnocenými hranami</li>
       <li>Rozklad signálu na frekvence</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Dijkstrův algoritmus hledá nejkratší cestu mezi uzly v grafu, kde každá hrana má svou cenu (váhu) – typicky plánování trasy v mapě.

</details>

23. **Jakou asymptotickou složitost má rychlá Fourierova transformace (FFT) ve srovnání s přímým výpočtem DFT?**
    <ol type="a">
       <li>FFT i DFT jsou stejně rychlé, oba $O(n)$</li>
       <li>FFT je $O(n^2)$, DFT je $O(n \log n)$</li>
       <li>FFT je $O(n!)$, DFT je $O(2^n)$</li>
       <li>DFT je $O(n^2)$, FFT je $O(n \log n)$</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Přímý výpočet diskrétní Fourierovy transformace je $O(n^2)$, zatímco FFT chytře rozdělí výpočet na menší části a dosáhne $O(n \log n)$.

</details>

24. **Co mají všechny teoreticky zajímavé algoritmy z cíle 5 (Dijkstra, Maďarský, FFT, Karacuba) společného?**
    <ol type="a">
       <li>Vznikly proto, že naivní řešení byla pro praxi příliš pomalá nebo nepraktická</li>
       <li>Všechny řeší problém vyhledávání v seřazeném seznamu</li>
       <li>Všechny mají složitost přesně $O(n \log n)$</li>
       <li>Všechny patří mezi algoritmy hrubé síly</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Každý z těchto algoritmů sice řeší jiný problém, ale všechny vznikly proto, aby vyřešily úlohu rychleji než naivní postup. To je přesně důvod, proč se učíme přemýšlet o asymptotické složitosti.

</details>

---

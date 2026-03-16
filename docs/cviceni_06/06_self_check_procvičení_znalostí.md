# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

1. **Co je hlavní výhoda rozdělení programu do modulů?**
   <ol type="a">
      <li>Python běží automaticky 2× rychleji</li>
      <li>Kód je přehlednější a znovupoužitelný</li>
      <li>Není potřeba psát funkce</li>
      <li>Nemusíš řešit importy</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Moduly zlepšují organizaci kódu a umožní znovupoužití funkcí.

</details>

2. **Co udělá <code>if __name__ == "__main__":</code>?**
   <ol type="a">
      <li>Spustí se vždy při importu modulu</li>
      <li>Spustí se jen při přímém spuštění souboru</li>
      <li>Zakáže import modulu</li>
      <li>Spustí testy z <code>pytest</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Blok se vykoná jen při přímém spuštění souboru.

</details>

3. **Které volání správně míchá poziční a pojmenované argumenty?**
   <ol type="a">
      <li><code>compute_score_delta(score=1540, 1200, round_to=1)</code></li>
      <li><code>compute_score_delta(1540, baseline=1200, round_to=1)</code></li>
      <li><code>compute_score_delta(1540, 1200, score=1800)</code></li>
      <li><code>compute_score_delta(round_to=1, 1540, 1200)</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Poziční argumenty jdou nejdřív, pojmenované až za nimi.

</details>

4. **Kdy je vhodné preferovat pojmenované argumenty?**
   <ol type="a">
      <li>Když má funkce víc parametrů nebo default hodnoty</li>
      <li>Nikdy, vždy jen poziční</li>
      <li>Jen u funkcí bez parametrů</li>
      <li>Jen když používáš <code>pytest</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Volání je čitelnější a je jasné, co která hodnota znamená.

</details>

5. **Jaké je doporučení pro globální proměnné v tomhle cvičení?**
   <ol type="a">
      <li>Používat je co nejvíc, aby se nemusely předávat parametry</li>
      <li>Používat je hlavně pro konstanty</li>
      <li>Vždy je měnit přes <code>global</code></li>
      <li>Používat jen v testech</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Pro měnitelná data je lepší předávání přes parametry a <code>return</code>.

</details>

6. **Která varianta importu je obecně nejméně vhodná pro čitelnost?**
   <ol type="a">
      <li><code>import modul</code></li>
      <li><code>import modul as alias</code></li>
      <li><code>from modul import *</code></li>
      <li><code>from modul import jedna_funkce</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>from modul import *</code> zhoršuje přehled i ladění.

</details>

7. **Jaká je doporučená reprezentace kružnice v Cíli 3?**
   <ol type="a">
      <li><code>[x, y, r]</code></li>
      <li><code>{"x": x, "y": y, "r": r}</code></li>
      <li><code>(x, y, r, color)</code></li>
      <li><code>"x,y,r"</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> V Cíli 3 se pracuje se slovníky s klíči <code>x</code>, <code>y</code>, <code>r</code>.

</details>

8. **Co má vracet <code>has_intersection(...)</code>?**
   <ol type="a">
      <li>Jen <code>bool</code> (<code>True</code>/<code>False</code>)</li>
      <li>Jen počet průniků jako <code>int</code></li>
      <li>Slovník alespoň s klíči <code>is_intersection</code> a <code>intersections_count</code></li>
      <li>Vždy <code>tuple</code> délky 2</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> V Cíli 3 je výstup funkce navržený jako slovník.

</details>

9. **Proč je u desetinných výpočtů lepší tolerance (<code>isclose</code>) než ostré <code>==</code>?**
   <ol type="a">
      <li>Protože <code>==</code> je v Pythonu zakázané</li>
      <li>Protože desetinná čísla mohou mít malé zaokrouhlovací odchylky</li>
      <li>Protože <code>isclose(...)</code> je vždy rychlejší</li>
      <li>Protože <code>isclose(...)</code> vrací text</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> U hraničních případů (např. dotyk kružnic) je tolerance spolehlivější.

</details>

10. **Ve volitelné části 3.7: co znamená podmínka <code>d = |r_1 - r_2|</code>?**
   <ol type="a">
      <li>Kružnice se neprotínají</li>
      <li>Kružnice mají dva průniky</li>
      <li>Kružnice mají jeden vnitřní dotyk</li>
      <li>Kružnice jsou totožné</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Jde o dotyk „zevnitř“.

</details>

11. **Jaký je doporučený příkaz pro instalaci externí knihovny v tomhle repu?**
   <ol type="a">
      <li><code>pip install matplotlib</code></li>
      <li><code>python -m pip install matplotlib</code></li>
      <li><code>uv add matplotlib</code></li>
      <li><code>apt install matplotlib</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> V tomhle kurzu se používá <code>uv</code>.

</details>

12. **Co udělá <code>uv run pytest</code>?**
   <ol type="a">
      <li>Spustí všechny nalezené testy v projektu</li>
      <li>Spustí jen jeden test</li>
      <li>Jen vytvoří složku <code>tests/</code></li>
      <li>Jen nainstaluje <code>pytest</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Typicky najde testy ve složce <code>tests/</code> a v souborech <code>test_*.py</code>.

</details>

13. **Co nejlépe popisuje rozdíl „knihovna / balíček / repozitář“?**
   <ol type="a">
      <li>Všechny tři pojmy znamenají totéž</li>
      <li>Knihovna a balíček jsou části kódu pro použití v programu, repozitář je celý verzovaný projekt</li>
      <li>Repozitář je jen složka <code>tests/</code></li>
      <li>Balíček je vždy totéž co GitHub repozitář</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Repozitář obsahuje kód, testy, dokumentaci a historii změn.

</details>

14. **Kde má být standardně testovací kód?**
   <ol type="a">
      <li>Ve složce <code>tests/</code></li>
      <li>Jen v <code>README.md</code></li>
      <li>V <code>src/</code> mezi produkčním kódem</li>
      <li>Jen v CI na GitHubu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Oddělení <code>src/</code> a <code>tests/</code> zlepšuje přehlednost.

</details>

15. **Co je pro splnění cvičení povinné?**
   <ol type="a">
      <li>Odevzdat funkční odkaz na repozitář do e-learningu</li>
      <li>Mít 100% správné řešení bez jediné chyby</li>
      <li>Nepoužít vůbec žádné externí knihovny</li>
      <li>Odevzdat jen screenshot terminálu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Repozitář má být <code>Public</code> a odevzdání/modifikace proběhnou nejpozději do půlnoci v den cvičení.

</details>

---

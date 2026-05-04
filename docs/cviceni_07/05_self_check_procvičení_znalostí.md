# CVIČENÍ 7: PROCVIČOVÁNÍ

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Aktivity podle akcelerometru

1. **Co je vstupem do programu v úloze s akcelerometrem?**
   <ol type="a">
      <li>Jen jedno číslo udávající rychlost</li>
      <li>Záznamy zrychlení ve třech osách (x, y, z)</li>
      <li>Souřadnice GPS</li>
      <li>Tepová frekvence v čase</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Akcelerometr na hrudním pásu měří zrychlení ve třech osách – z těchto dat se odvozují aktivity.

</details>

2. **Co je hlavním cílem úlohy s akcelerometrickými daty?**
   <ol type="a">
      <li>Rozpoznat základní typy aktivity (např. pohyb, stání, ležení)</li>
      <li>Spočítat počet kroků za den</li>
      <li>Vykreslit graf tepové frekvence</li>
      <li>Predikovat polohu uživatele na mapě</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Cílem je na základě jednoduchých pravidel rozhodnout, zda se člověk pohybuje, stojí nebo leží.

</details>

3. **Která datová struktura je vhodná pro uložení jednoho vzorku akcelerometru se třemi osami?**
   <ol type="a">
      <li><code>"1.2 0.3 9.8"</code> – jeden řetězec</li>
      <li><code>1.2</code> – jedno desetinné číslo</li>
      <li><code>{"jmeno": "Jan"}</code> – slovník bez čísel</li>
      <li><code>(1.2, 0.3, 9.8)</code> nebo <code>[1.2, 0.3, 9.8]</code> – tuple/seznam tří hodnot</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Tři hodnoty (x, y, z) přirozeně tvoří trojici, kterou lze reprezentovat jako tuple nebo seznam.

</details>

4. **Jak nejlépe poznat, že člověk se nehýbe (stojí nebo leží)?**
   <ol type="a">
      <li>Hodnoty zrychlení mezi vzorky se výrazně mění</li>
      <li>Hodnoty zrychlení v jednotlivých osách jsou v čase víceméně konstantní</li>
      <li>Hodnota osy z je vždy nulová</li>
      <li>Záznam má méně než 10 vzorků</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Při klidu se zrychlení v jednotlivých osách v čase téměř nemění – mění se hlavně při pohybu.

</details>

5. **Co je rozumný první krok při návrhu pravidla pro rozpoznání aktivity?**
   <ol type="a">
      <li>Rovnou začít psát složitou funkci pro všechny aktivity najednou</li>
      <li>Stáhnout si knihovnu pro strojové učení</li>
      <li>Podívat se na ukázková data a najít rozdíly v hodnotách os mezi aktivitami</li>
      <li>Smazat polovinu vzorků, ať je to rychlejší</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Pravidla se navrhují na základě pozorování dat – nejdřív koukni, čím se aktivity v hodnotách liší.

</details>

---

### Část B: Správce kontaktů

6. **Které informace má v zadání obsahovat jeden kontakt?**
   <ol type="a">
      <li>Jméno, telefonní číslo a e-mailová adresa</li>
      <li>Pouze jméno a heslo</li>
      <li>IP adresa a port</li>
      <li>Jméno, váha a výška</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Kontakt v této úloze obsahuje jméno, telefon a e-mail – stejně jako v mobilním telefonu.

</details>

7. **Jaká datová struktura je nejvhodnější pro reprezentaci jednoho kontaktu?**
   <ol type="a">
      <li>Seznam – <code>["Jan", "123456789", "jan@x.cz"]</code></li>
      <li>Číslo</li>
      <li>Slovník – <code>{"jméno": "Jan", "telefon": "123456789", "email": "jan@x.cz"}</code></li>
      <li>Jeden dlouhý řetězec</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Pojmenované klíče (jméno, telefon, e-mail) jsou čitelnější a méně náchylné k záměně než indexy v seznamu.

</details>

8. **Co vypíše tento kód?**
   ```python
   kontakty = {
       "Jan Novák": {"telefon": "123456789", "email": "jan@example.com"}
   }
   print(kontakty["Jan Novák"]["telefon"])
   ```
   <ol type="a">
      <li><code>jan@example.com</code></li>
      <li><code>Jan Novák</code></li>
      <li><code>KeyError</code></li>
      <li><code>123456789</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Nejdřív se vybere kontakt podle jména a pak z vnitřního slovníku hodnota klíče <code>"telefon"</code>.

</details>

9. **Které funkce typicky správce kontaktů potřebuje?**
   <ol type="a">
      <li>Jen vyhledávání</li>
      <li>Jen přidávání</li>
      <li>Jen ukládání do souboru</li>
      <li>Vyhledávání, přidávání, úprava i ukládání</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Zadání po tobě chce všechny tyto operace – přesně jako u kontaktů v mobilu.

</details>

10. **Jaký je problém s tímto kódem?**
    ```python
    def pridej_kontakt(kontakty, jmeno, telefon, email):
        kontakty[jmeno] = {"telefon": telefon, "email": email}
    ```
    Kontakt se jménem, který už existuje, byl předtím přidaný se starým telefonem.
    <ol type="a">
      <li>Vyhodí <code>KeyError</code></li>
      <li>Tiše přepíše původní kontakt – chybí kontrola duplicit</li>
      <li>Vytvoří dva kontakty se stejným jménem</li>
      <li>Vrátí <code>None</code> a nic nepřidá</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Slovníky mají unikátní klíče – přiřazení na existující klíč ho přepíše. Často je proto potřeba nejdřív zkontrolovat <code>if jmeno in kontakty:</code>.

</details>

11. **Jak nejlépe ověříš, že telefonní číslo obsahuje jen číslice?**
    <ol type="a">
      <li><code>telefon.isdigit()</code></li>
      <li><code>telefon == int</code></li>
      <li><code>type(telefon) == "číslo"</code></li>
      <li><code>telefon > 0</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Metoda <code>isdigit()</code> vrací <code>True</code>, pokud řetězec obsahuje jen číslice.

</details>

12. **Jaký formát souboru je vhodný pro uložení slovníku kontaktů?**
    <ol type="a">
      <li>JPG</li>
      <li>EXE</li>
      <li>JSON (struktura mapuje přirozeně na slovník)</li>
      <li>MP3</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> JSON je textový formát, který přesně odpovídá vnořeným slovníkům a seznamům v Pythonu – načtení/uložení je snadné přes <code>json.load</code> / <code>json.dump</code>.

</details>

---

### Část C: Datové struktury, validace a rozklad úlohy

13. **Co je v praxi nejdůležitější první krok u komplexnější slovní úlohy?**
    <ol type="a">
      <li>Hned napsat hlavní funkci na 100 řádků</li>
      <li>Rozložit zadání na menší části a ujasnit si, co která funkce má dělat</li>
      <li>Vygenerovat celé řešení AI a odevzdat</li>
      <li>Začít refaktorovat kód, který ještě neexistuje</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Rozklad na menší podproblémy je klíč – každou část pak vyřešíš samostatnou funkcí.

</details>

14. **Co vypíše tento kód?**
    ```python
    kontakty = {
        "Anna": {"telefon": "111", "email": "a@x.cz"},
        "Bob":  {"telefon": "222", "email": "b@x.cz"},
    }
    for jmeno, info in kontakty.items():
        print(jmeno, info["telefon"])
    ```
    <ol type="a">
      <li><code>Anna a@x.cz</code> a <code>Bob b@x.cz</code></li>
      <li><code>jmeno info</code></li>
      <li><code>KeyError</code></li>
      <li><code>Anna 111</code> a <code>Bob 222</code> na dvou řádcích</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>.items()</code> vrací páry (klíč, hodnota); pro každý kontakt se vypíše jméno a hodnota klíče <code>"telefon"</code>.

</details>

15. **Jaký je doporučený způsob přístupu ke kontaktu, který nemusí existovat?**
    <ol type="a">
      <li><code>kontakt = kontakty[jmeno]</code> – ať to vyhodí chybu, to je v pohodě</li>
      <li>Předem nejdřív zkontrolovat <code>if jmeno in kontakty:</code></li>
      <li>Použít <code>try/except IndexError</code></li>
      <li>Volat <code>kontakty.find(jmeno)</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Bezpečné je zkontrolovat existenci klíče přes <code>in</code> (případně použít <code>.get()</code>) – zabrání to <code>KeyError</code>.

</details>

16. **Najdi chybu:**
    ```python
    def pridej_kontakt(jmeno, telefon, email):
        kontakty[jmeno] = {"telefon": telefon, "email": email}

    pridej_kontakt("Jan", "123", "jan@x.cz")
    ```
    Chceš, aby funkce šla volat z více míst a fungovala bez globální proměnné.
    <ol type="a">
      <li>Funkce je úplně v pořádku</li>
      <li>Místo <code>def</code> má být <code>function</code></li>
      <li>Spoléhá na globální slovník <code>kontakty</code> – lepší je předat ho jako parametr</li>
      <li>Slovníky nelze přiřazovat přes hranaté závorky</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Funkce by měla data dostávat parametrem, ne brát z globálu – je pak testovatelná a znovupoužitelná.

</details>

17. **Proč je dobré validovat vstupní data (telefon, e-mail) před uložením?**
    <ol type="a">
      <li>Neexistuje žádný důvod, validace zdržuje</li>
      <li>Jen pro hezčí výpis</li>
      <li>Aby se do databáze nedostaly nesmyslné hodnoty, kvůli kterým by později selhaly další funkce</li>
      <li>Aby se kód spouštěl rychleji</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Validace zachytí chybu hned u zdroje – jinak by se chybné hodnoty propisovaly dál a zdroj problému by se hledal hůř.

</details>

18. **Jak nejjednodušeji zjistíš, jestli e-mail vypadá alespoň přibližně správně?**
    <ol type="a">
      <li>Zkontrolovat, že obsahuje znak <code>@</code></li>
      <li>Spustit ho jako Python kód</li>
      <li>Porovnat ho s každou položkou v seznamu kontaktů</li>
      <li>Převést ho na <code>int</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Pro účely cvičení stačí jednoduchá kontrola, např. že řetězec obsahuje <code>"@"</code>. Plná validace e-mailu je výrazně složitější.

</details>

---

### Část D: Doporučený postup, debugging a odevzdání

19. **Co znamená rada „nejdřív skript, pak funkce"?**
    <ol type="a">
      <li>Nikdy nepoužívej funkce</li>
      <li>Nejdřív problém vyřeš jednoduchým skriptem pro jeden konkrétní příklad a teprve pak ho přepiš do funkce</li>
      <li>Nejdřív napiš všechny funkce a pak žádný hlavní skript</li>
      <li>Funkce se píšou až týden po skriptu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Nejdřív si ověříš logiku „narovinu", a až když ji máš funkční, zabalíš ji do funkce s parametry.

</details>

20. **Co dělat, když funkce, na které tvoje další funkce závisí, ještě nefunguje?**
    <ol type="a">
      <li>Skončit s úkolem a nic dalšího nedělat</li>
      <li>Smazat testy</li>
      <li>Vytvořit ručně ukázkový výstup, jaký by ta funkce měla vrátit, a pokračovat dál</li>
      <li>Vyhodit chybu <code>raise NotImplementedError</code> v hlavním skriptu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Nakonec se ti tak podaří ukázat, že rozumíš zbytku zadání, i když jedna část nefunguje.

</details>

21. **Který příkaz spustí všechny pytest testy v projektu pomocí <code>uv</code>?**
    <ol type="a">
      <li><code>uv install pytest</code></li>
      <li><code>python pytest</code></li>
      <li><code>uv pytest run</code></li>
      <li><code>uv run pytest -v</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>uv run pytest -v</code> spustí všechny testy ve verbose módu – uvidíš, co prošlo a co spadlo.

</details>

22. **Co udělá <code>uv sync</code>?**
    <ol type="a">
      <li>Nainstaluje závislosti projektu podle <code>pyproject.toml</code> / lock souboru</li>
      <li>Nahraje změny na GitHub</li>
      <li>Vytvoří nový repozitář</li>
      <li>Spustí všechny testy</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> <code>uv sync</code> stáhne a nainstaluje závislosti tak, aby projekt šel rovnou používat.

</details>

23. **Při řešení test prochází, ale program se chová divně v některých situacích. Co zkusit?**
    <ol type="a">
      <li>Označit test jako vadný a smazat ho</li>
      <li>Vyzkoušet hraniční případy – prázdný seznam, neexistující kontakt, duplicitní jméno apod.</li>
      <li>Přepsat zadání</li>
      <li>Vypnout všechny <code>if</code> v kódu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Testy zachytí jen ty případy, které pokrývají – tvoje funkce ale musí fungovat i pro nečekaný vstup.

</details>

24. **Které chování je v souladu s pravidly cvičení?**
    <ol type="a">
      <li>Upravit testovací soubory tak, aby tvůj kód prošel</li>
      <li>Nechat AI vyřešit obě úlohy a po 5 minutách odejít</li>
      <li>Commitovat průběžně po každé funkci a upravovat jen svůj hlavní skript</li>
      <li>Odevzdat až po skončení cvičení e-mailem</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Testy se neupravují, AI nepoužíváš na řešení a odevzdává se průběžně do GitHub Classroom během cvičení.

</details>

25. **Co je minimum potřebné pro splnění cvičení 7?**
    <ol type="a">
      <li>Mít obě úlohy 100% kompletní s plným hodnocením</li>
      <li>Stačí naklonovat repozitář a nic neudělat</li>
      <li>Stačí napsat řešení lokálně, nepushovat</li>
      <li>Odevzdat řešení do GitHub Classroom tak, aby alespoň jeden úkol byl kompletně vyřešený a druhý alespoň částečně rozpracovaný</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Podle zadání cvičení musí být alespoň jeden úkol kompletní a druhý alespoň rozpracovaný – a vše odevzdané v GitHub Classroom do konce cvičení.

</details>

---

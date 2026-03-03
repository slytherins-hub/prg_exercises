# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE, MNOŽINY A SLOVNÍKY

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: While cykly

1. **Jaký je rozdíl mezi `for` a `while` cyklem?**
    <ol type="a">
      <li><code>for</code> je rychlejší</li>
      <li><code>for</code> se používá pro známý počet opakování, `while` pro neznámý počet</li>
      <li><code>while</code> je zastaralý</li>
      <li>Žádný rozdíl</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>for</code> se používá, když víš předem kolikrát se má opakovat (např. projdi seznam), <code>while</code> když opakuješ dokud platí podmínka (např. dokud uživatel nezadá správný vstup)

</details>

2. **Co způsobí tento kód?**
    ```python
    x = 0
    while x < 5:
        print(x)
    ```
    <ol type="a">
      <li>Vypíše: 0 1 2 3 4</li>
      <li>Vypíše: 0 1 2 3 4 5</li>
      <li>Nekonečný cyklus</li>
      <li>Chybu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Nekonečný cyklus - <code>x</code> se nikdy nezmění, podmínka <code>x < 5</code> bude pořád pravdivá

</details>

3. **Co dělá klíčové slovo <code>break</code>?**
    <ol type="a">
      <li>Přeskočí aktuální iteraci a pokračuje další</li>
      <li>Ukončí celý cyklus okamžitě</li>
      <li>Ukončí program</li>
      <li>Vyhodí chybu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Ukončí celý cyklus okamžitě a pokračuje kódem za cyklem

</details>

4. **Co dělá klíčové slovo <code>continue</code>?**
    <ol type="a">
      <li>Ukončí celý cyklus</li>
      <li>Přeskočí zbytek aktuální iterace a pokračuje další iterací</li>
      <li>Nic, je zastaralé</li>
      <li>Ukončí funkci</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Přeskočí zbytek aktuální iterace a pokračuje další iterací

</details>

5. **Kdy je vhodné použít <code>while True</code>?**
    <ol type="a">
      <li>Nikdy, vždycky způsobí nekonečný cyklus</li>
      <li>Když chceš cyklus, který se ukončí pomocí <code>break</code> uvnitř</li>
      <li>Jen pro začátečníky</li>
      <li>Nahrazuje if podmínku</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>while True</code> s <code>break</code> uvnitř je běžný vzor pro menu nebo validaci vstupu - cyklus běží dokud nenastane nějaká vnitřní podmínka

</details>

---

### Část B: Slovníky - základy

6. **Co je pravda o slovnících?**
    <ol type="a">
      <li>Indexují se pomocí pozic (0, 1, 2...)</li>
      <li>Indexují se pomocí klíčů</li>
      <li>Mohou mít duplicitní klíče</li>
      <li>Jsou immutable</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Slovníky používají klíče místo číselných indexů. Klíče musí být unikátní!

</details>

7. **Co vypíše tento kód?**
    ```python
    patient = {"name": "Jan", "age": 45}
    print(patient["age"])
    ```
    <ol type="a">
      <li>age</li>
      <li>45</li>
      <li>Jan</li>
      <li>KeyError</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> 45 – <code>patient["age"]</code> vrací hodnotu pro klíč <code>"age"</code>

</details>

8. **Co se stane při tomto kódu?**
    ```python
    data = {"name": "Jan"}
    data["name"] = "Marie"
    print(data)
    ```

    <ol type="a">
      <li><code>{"name": "Jan", "name": "Marie"}</code></li>
      <li><code>{"name": "Marie"}</code></li>
      <li>Chyba</li>
      <li><code>{"name": "Jan"}</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>{"name": "Marie"}</code> – přiřazení na existující klíč ho přepíše, klíče musí být unikátní

</details>

9. **Co se stane při přístupu <code>slovnik["klic"]</code>, když klíč neexistuje?**

    <ol type="a">
      <li>Vrátí <code>None</code></li>
      <li>Vytvoří klíč automaticky</li>
      <li>Vyhodí chybu <code>KeyError</code></li>
      <li>Vrátí prázdný řetězec</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Při přístupu <code>slovnik["klic"]</code> Python vyhodí chybu <code>KeyError</code>, pokud klíč ve slovníku není.

</details>

10. **Co vrací metoda <code>.items()</code>?**

    <ol type="a">
      <li>Jen klíče</li>
      <li>Jen hodnoty</li>
      <li>Páry (klíč, hodnota) – ideální pro for cyklus</li>
      <li>Počet prvků</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>.items()</code> vrací páry (klíč, hodnota), nejužitečnější pro iteraci:

<code>for klic, hodnota in slovnik.items():</code>

</details>

---

### Část C: Slovníky - pokročilé

11. **Co vypíše tento kód?**

    ```python
    codons = {"AUG": "Methionin", "UUU": "Fenylalanin"}
    for codon in codons:
        print(codon)
    ```

    <ol type="a">
      <li>Methionin, Fenylalanin</li>
      <li>AUG, UUU</li>
      <li>AUG: Methionin, UUU: Fenylalanin</li>
      <li>Chybu</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> AUG, UUU – při iteraci <code>for x in slovnik</code> dostáváš jen klíče (ne hodnoty!)

</details>

12. **Jak správně přidat nový klíč do slovníku?**

    <ol type="a">
      <li><code>my_dict.add("new_key", "value")</code></li>
      <li><code>my_dict["new_key"] = "value"</code></li>
      <li><code>my_dict.append("new_key": "value")</code></li>
      <li><code>my_dict.insert("new_key", "value")</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Prostě přiřaď:

<code>my_dict["new_key"] = "value"</code>

Pokud klíč neexistuje, vytvoří se.

</details>

13. **Co dělá metoda <code>.pop("key")</code>?**

    <ol type="a">
      <li>Jen vrátí hodnotu</li>
      <li>Jen smaže klíč</li>
      <li>Smaže klíč a vrátí jeho hodnotu</li>
      <li>Nic</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b><code>.pop()</code> odstraní klíč a vrátí jeho hodnotu.

Můžeš dát default:

<code>.pop("key", "default")</code>

</details>

14. **Proč jsou slovníky užitečnější než seznamy pro databázi pacientů?**

    <ol type="a">
      <li>Jsou rychlejší</li>
      <li>Zabírají méně paměti</li>
      <li>Můžeš vyhledávat podle ID místo pozice</li>
      <li>Vypadají lépe</li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Se slovníkem můžeš napsat:

<code>patients["P001"]</code>

Místo pamatovat si, že P001 je na pozici 5 v seznamu. Klíče jsou čitelnější než indexy.

</details>

15. **Co je lepší vzor pro kontrolu existence klíče?**

    <ol type="a">
      <li>
       <pre><code>if "key" in my_dict:
       value = my_dict["key"]</code></pre>
      </li>
      <li><code>value = my_dict["key"]</code></li>
      <li>Není potřeba kontrolovat klíč nikdy</li>
      <li>Klíč vždy raději odstraň přes <code>pop()</code></li>
    </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Kontrola <code>if "key" in my_dict:</code> je bezpečný způsob, jak se vyhnout <code>KeyError</code>.

</details>

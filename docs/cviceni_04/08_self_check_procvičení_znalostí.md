# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE A SLOVNÍKY

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: While cykly

**1. Jaký je rozdíl mezi `for` a `while` cyklem?**

- a) `for` je rychlejší
- b) `for` se používá pro známý počet opakování, `while` pro neznámý počet
- c) `while` je zastaralý
- d) Žádný rozdíl

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `for` se používá, když víš předem kolikrát se má opakovat (např. projdi seznam), `while` když opakuješ dokud platí podmínka (např. dokud uživatel nezadá správný vstup)
</details>

**2. Co způsobí tento kód?**
```python
x = 0
while x < 5:
    print(x)
```

- a) Vypíše 0 1 2 3 4
- b) Vypíše 0 1 2 3 4 5
- c) Nekonečný cyklus
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Nekonečný cyklus - `x` se nikdy nezmění, podmínka `x < 5` bude pořád pravdivá
</details>

**3. Co dělá klíčové slovo `break`?**

- a) Přeskočí aktuální iteraci a pokračuje další
- b) Ukončí celý cyklus okamžitě
- c) Ukončí program
- d) Vyhodí chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Ukončí celý cyklus okamžitě a pokračuje kódem za cyklem
</details>

**4. Co dělá klíčové slovo `continue`?**

- a) Ukončí cyklus
- b) Přeskočí zbytek aktuální iterace a pokračuje další iterací
- c) Nic, je zastaralé
- d) Ukončí funkci

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Přeskočí zbytek aktuální iterace a skočí na začátek další iterace
</details>

**5. Kdy je vhodné použít `while True`?**

- a) Nikdy, vždycky způsobí nekonečný cyklus
- b) Když chceš cyklus, který se ukončí pomocí `break` uvnitř
- c) Jen pro začátečníky
- d) Nahrazuje if podmínku

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `while True` s `break` uvnitř je běžný pattern pro menu nebo validaci vstupu - cyklus běží dokud nenastane nějaká vnitřní podmínka
</details>

### Část B: Slovníky - základy

**6. Co je pravda o slovnících?**

- a) Indexují se pomocí pozic (0, 1, 2...)
- b) Indexují se pomocí klíčů
- c) Mohou mít duplicitní klíče
- d) Jsou immutable

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Slovníky používají klíče místo číselných indexů. Klíče musí být unikátní!
</details>

**7. Co vypíše tento kód?**
```python
patient = {"name": "Jan", "age": 45}
print(patient["age"])
```

- a) "age"
- b) 45
- c) Jan
- d) KeyError

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) 45 - `patient["age"]` vrací hodnotu pro klíč "age"
</details>

**8. Co se stane při tomto kódu?**
```python
data = {"name": "Jan"}
data["name"] = "Marie"
print(data)
```

- a) `{"name": "Jan", "name": "Marie"}`
- b) `{"name": "Marie"}`
- c) Chyba
- d) `{"name": "Jan"}`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) `{"name": "Marie"}` - přiřazení na existující klíč ho přepíše, klíče musí být unikátní
</details>

**9. Co se stane při přístupu `slovnik["klic"]`, když klíč neexistuje?**

- a) Vrátí `None`
- b) Vytvoří klíč automaticky
- c) Vyhodí chybu `KeyError`
- d) Vrátí prázdný řetězec

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Při přístupu `slovnik["klic"]` Python vyhodí chybu `KeyError`, pokud klíč ve slovníku není.
</details>

**10. Co vrací metoda `.items()`?**

- a) Jen klíče
- b) Jen hodnoty
- c) Páry (klíč, hodnota) - ideální pro for cyklus
- d) Počet prvků

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `.items()` vrací páry (klíč, hodnota), nejužitečnější pro iteraci: `for klic, hodnota in slovnik.items()`
</details>

### Část C: Slovníky - pokročilé

**11. Co vypíše tento kód?**
```python
codons = {"AUG": "Methionin", "UUU": "Fenylalanin"}
for codon in codons:
    print(codon)
```

- a) Methionin, Fenylalanin
- b) AUG, UUU
- c) AUG: Methionin, UUU: Fenylalanin
- d) Chybu

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) AUG, UUU - při iteraci `for x in slovnik` dostáváš jen klíče (ne hodnoty!)
</details>

**12. Jak správně přidat nový klíč do slovníku?**

- a) `my_dict.add("new_key", "value")`
- b) `my_dict["new_key"] = "value"`
- c) `my_dict.append("new_key": "value")`
- d) `my_dict.insert("new_key", "value")`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

b) Prostě přiřaď: `my_dict["new_key"] = "value"` - pokud klíč neexistuje, vytvoří se
</details>

**13. Co dělá metoda `.pop("key")`?**

- a) Jen vrátí hodnotu
- b) Jen smaže klíč
- c) Smaže klíč a vrátí jeho hodnotu
- d) Nic

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) `.pop()` odstraní klíč a vrátí jeho hodnotu. Můžeš dát default: `.pop("key", "default")`
</details>

**14. Proč jsou slovníky užitečnější než seznamy pro databázi pacientů?**

- a) Jsou rychlejší
- b) Zabírají méně paměti
- c) Můžeš vyhledávat podle ID místo pozice
- d) Vypadají lépe

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

c) Se slovníkem můžeš napsat `patients["P001"]` místo pamatovat si, že P001 je na pozici 5 v seznamu. Klíče jsou čitelnější než indexy!
</details>

**15. Co je lepší pattern pro kontrolu existence klíče?**

- a)
```python
if "key" in my_dict:
    value = my_dict["key"]
```

- b)
```python
value = my_dict["key"]
```

- c) Není potřeba kontrolovat klíč nikdy
- d) Klíč vždy raději odstraň přes `pop()`

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

a) Kontrola `if "key" in my_dict:` je bezpečný způsob, jak se vyhnout `KeyError`.

---
</details>

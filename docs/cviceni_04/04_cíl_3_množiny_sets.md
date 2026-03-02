# CVIČENÍ 4: VÝJIMKY, CYKLY WHILE, MNOŽINY A SLOVNÍKY

Algoritmizace a programování

## CÍL 3: MNOŽINY (SETS)

### Proč řešit množiny?

Množiny (`set`) se hodí, když potřebuješ pracovat s **unikátními hodnotami** a rychle ověřovat, jestli nějaká hodnota existuje.

Typické situace v praxi:

- seznam unikátních alergenů pacienta,
- odstranění duplicit ze seznamu laboratorních kódů,
- unikátní hashtagy pod příspěvkem,
- odstranění duplicitních e-mailů při rozesílce,
- rychlé ověření, jestli je uživatelské jméno na blacklistu.

> **📘 Co je množina (`set`)?**
> `set` je datová struktura, která se chová jako **matematická množina**: nemá duplicity a podporuje operace jako sjednocení, průnik a rozdíl.

---

### 3.1 Unikátnost a hashování

`set` je v Pythonu postavený na **hashování**.

Můžeš si to představit tak, že existuje **hashovací funkce**, která z hodnoty (např. řetězce) vyrobí číslo.

- Výstupy vypadají trochu **chaoticky** (nejdou jednoduše odhadnout z hlavy).
- Ale jsou **deterministické**: pro stejný vstup dostaneš stejný hash.
- Díky tomu Python rychle najde správné místo, kam prvek uložit nebo kde ho hledat.

> **⚠️ Pozor:** Dvě různé hodnoty můžou výjimečně skončit na stejném místě (tzv. **kolize**). Python to umí interně vyřešit.

Zjednodušený nákres pro `set` (bez hodnot, jen prvky):

![Nákres hashování v setu](../assets/cviceni_04/set_hashing_diagram.svg)

> **💡 Poznámka:** U `set` se ukládají jen samotné prvky (na rozdíl od slovníku, kde je dvojice klíč–hodnota).

Krátký model:

```text
hash("latex") -> 151
hash("pyl")   -> 11
hash("latex") -> 151  (stejný vstup, stejný výstup)
```

Jednoduchý nákres, co se děje uvnitř:

```text
"latex"  -> hash("latex")  -> přihrádka 2
"pyl"    -> hash("pyl")    -> přihrádka 7
"latex"  -> hash("latex")  -> přihrádka 2 (už tam je, nepřidá se znovu)
```

> **💡 Poznámka:** Proto bývá kontrola `x in mnozina` rychlá — Python jde rovnou do „správné přihrádky“ místo procházení celé kolekce.

```python
kody_oddeleni = {"A", "B", "A", "C"}
print(kody_oddeleni)  # {'A', 'B', 'C'} (pořadí se může lišit)

if "A" in kody_oddeleni:
   print("Oddělení A existuje")
```

> **⚠️ Pozor:** Množina není seřazená kolekce. Pořadí prvků se může lišit.

---

### 3.2 Operace: sjednocení, průnik, rozdíl

```python
alergie_pacient_a = {"penicilin", "latex", "pyl"}
alergie_pacient_b = {"latex", "orechy"}

sjednoceni = alergie_pacient_a | alergie_pacient_b   # všechny alergie
prunik = alergie_pacient_a & alergie_pacient_b       # společné alergie
rozdil = alergie_pacient_a - alergie_pacient_b       # jen u pacienta A

print(sjednoceni)
print(prunik)
print(rozdil)

# Stejné operace pomocí metod
sjednoceni_metoda = alergie_pacient_a.union(alergie_pacient_b)
prunik_metoda = alergie_pacient_a.intersection(alergie_pacient_b)
rozdil_metoda = alergie_pacient_a.difference(alergie_pacient_b)

print(sjednoceni_metoda)
print(prunik_metoda)
print(rozdil_metoda)
```

> **💡 Tip:** Když řešíš „co je společné“, „co je navíc“ nebo „co je unikátní“, je `set` často jednodušší než seznam.

---

### 3.3 Převod mezi list a set

```python
mereni = ["EKG", "EEG", "EKG", "MRI", "EEG"]
unikatni_mereni = set(mereni)
print(unikatni_mereni)

# Když potřebuješ zpět seznam:
mereni_bez_duplikat = list(unikatni_mereni)
print(mereni_bez_duplikat)
```

---

**📝 ÚKOL 1: Unikátní diagnózy**

Máš seznam diagnóz:

```python
diagnozy = ["I10", "E11", "I10", "J45", "E11", "N39"]
```

1. Vytvoř množinu unikátních diagnóz.
2. Vypiš počet unikátních diagnóz.
3. Ověř, jestli je v seznamu diagnóza `"J45"`.

---

**📝 ÚKOL 2: Společné hashtagy**

Máš dva příspěvky na sociální síti a u každého množinu hashtagů:

```python
hashtagy_a = {"python", "programovani", "ai", "tips"}
hashtagy_b = {"ai", "data", "python", "vizualizace"}
```

Vypiš:

1. všechny hashtagy (sjednocení),
2. společné hashtagy (průnik),
3. hashtagy jen z prvního příspěvku (rozdíl).

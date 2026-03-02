# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## CÍL 6: ZÁKLADY DEBUGOVÁNÍ V PYCHARM

### 6.1 Co je debugování?

Debugování = **hledání a oprava chyb** v kódu. V minulém cvičení jsme používali `print()`, ale PyCharm má **mnohem mocnější nástroje**:

- **Breakpointy** – zastavení programu na konkrétním řádku
- **Krokování** – spuštění programu řádek po řádku
- **Inspekce proměnných** – zobrazení hodnot v reálném čase

### 6.2 Nastavení breakpointu

**Breakpoint** = červená tečka na okraji editoru, která říká: "Zastav program **PŘED** provedením tohoto řádku".

#### Jak nastavit:

1. Otevři soubor v PyCharmu
2. Klikni na **levý okraj** (na číslo řádku)
3. Objeví se **červená tečka** 🔴

**Příklad:**
```python
name = input("Zadej jméno: ") # 🔴 Breakpoint zde
age = int(input("Zadej věk: "))
print(f"{name} je {age} let.")
```

### 6.3 Spuštění v debug módu

**Normální spuštění:** Zelené tlačítko ▶️ (Shift+F10)
**Debug mód:** 🐞 Zelený brouček (Shift+F9)

**Co se stane:**

1. Program se **zastaví** na breakpointu
2. Spodní panel zobrazí **hodnoty proměnných**
3. Můžeš program **krokovat** (procházet řádek po řádku)

### 6.4 Ovládání debuggeru

| Klávesa | Akce | Popis |
|--------------|-----------|-------------------------------------|
| **Shift+F9** | Debug | Spusť debuggování |
| **F8** | Step Over | Proveď aktuální řádek |
| **F9** | Resume | **Pokračuj** do dalšího breakpointu |
| **Ctrl+F2** | Stop | **Zastav** debugování |

### 6.5 Praktický příklad: Debugování for cyklu

```python
text = "Python"
vowels = "aeiouAEIOU"
count = 0

for char in text: # 🔴 Nastavte breakpoint ZDE
 if char in vowels:
 count += 1
 print(f"Kontroluji: {char}, počet samohlásek: {count}")

print(f"Celkem samohlásek: {count}")
```

**Postup debugování:**

1. **Nastav breakpoint** na řádek `for char in text:`
2. **Spusť debug** (🐞 nebo Shift+F9)
3. Program se zastaví před prvním průchodem cyklu
4. V panelu **Variables** uvidíš hodnoty proměnných:
 ```
 text = "Python"
 vowels = "aeiouAEIOU"
 count = 0
 ```
5. Stiskni **F8** (Step Over) → provede se `for char in text:`
6. Teď uvidíš `char = "P"`
7. Stiskni **F8** znovu a sleduj, jak se mění `count`
8. Stiskni **F9** (Resume) → program doběhne do konce

### 6.6 Časté debugovací situace

**Problém 1: Špatná hodnota/datový typ proměnné**
```python
temperature = input("Teplota: ") # Uživatel zadal "37.5"
if temperature > 38: # 🔴 Breakpoint
 print("Horečka!")
```
- Debugger ukáže: `temperature = "37.5"` (TEXT!)
- Chyba: Porovnáváš string s číslem
- Oprava: `temperature = float(input(...))`

**Problém 2: Index out of range**
```python
patients = ["Jan", "Marie", "Petr"]
print(patients[3]) # 🔴 Breakpoint
```
- Debugger ukáže: `len(patients) = 3`
- Indexy jsou 0, 1, 2 → index 3 neexistuje!

**💻 Praktický úkol - debugování:**

Vytvoř soubor `debug_practice.py` s tímto kódem a vyzkoušej debugování:

```python
text = "Python is great!"
vowel_count = 0
consonant_count = 0

for char in text:
 if char.isalpha(): # Pouze písmena
 if char.lower() in "aeiou":
 vowel_count += 1
 else:
 consonant_count += 1

print(f"Samohlásky: {vowel_count}")
print(f"Souhlásky: {consonant_count}")
```

**Postup:**

- Nastav breakpoint na řádek `for char in text:`
- Spusť debug mód (🐞 nebo Shift+F9)
- Krokuj (F8) prvními průchody
- Sleduj, jak se mění proměnné `char`, `vowel_count`, `consonant_count`

**Tip:** Debugování **šetří čas**! Místo 10× print a opakovaného spouštění stačí JEDNOU projít debuggerem.

---


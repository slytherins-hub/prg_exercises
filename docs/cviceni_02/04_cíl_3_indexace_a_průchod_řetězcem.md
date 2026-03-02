# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## CÍL 3: INDEXACE A PRŮCHOD ŘETĚZCEM

### 3.1 Indexování znaků

Každý znak má své **pořadí** (index), které začíná od **0**:

```python
word = "Python"
# 012345

first = word[0] # "P"
third = word[2] # "t"
last = word[5] # "n"
```

**Záporné indexy** počítají odzadu:

```python
last = word[-1] # "n"
second_last = word[-2] # "o"
```

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|---------|----|----|----|----|----|----|
| Znak | P | y | t | h | o | n |
| Záporný | -6 | -5 | -4 | -3 | -2 | -1 |

**Praktický příklad:** Projití více indexů pomocí cyklu

```python
word = "Python"

# Vypíšeme znaky na pozicích 0, 2, 4
for i in [0, 2, 4]:
 print(f"Znak na indexu {i}: {word[i]}")

# Nebo můžeme projít všechny indexy
for i in range(len(word)):
 print(f"Index {i}: {word[i]}")
```

**💻 Zkus:**
```python
# Vytvoř proměnnou school = "Hogwarts" a vypiš 4. znak (index 3)
school = "Hogwarts"
print(school[3]) # "w"

# Vypiš poslední znak pomocí záporného indexu
print(school[-1]) # "s"

# Napiš cyklus, který projde indexy 1, 3, 5, 7 a vypíše znaky na těchto pozicích
for i in [1, 3, 5, 7]:
 print(f"Index {i}: {school[i]}")
```

### 3.2 Slicing (Řezání)

Pomocí `[start:end]` vyřízneme část řetězce:

```python
text = "Slytherin beats Gryffindor"
# 0123456789

team = text[0:9] # "Slytherin"
team = text[:9] # Totéž (začátek lze vynechat)
rest = text[9:] # " beats Gryffindor" (konec lze vynechat)
```

**Pozor:** Konečný index (`end`) **není zahrnut**!

**Krok (step):**
```python
text = "0123456789"
print(text[::2]) # "02468" (každý druhý znak)
print(text[::-1]) # "9876543210" (otočení)
```

**Kompletní slicing s všemi parametry:**
```python
text = "0123456789"
print(text[1:8:2]) # "1357" (od indexu 1 do 8, každý druhý)
print(text[2:9:3]) # "258" (od indexu 2 do 9, každý třetí)
```

**💻 Zkus:**
```python
print("abcdefgh"[2:6]) # "cdef"
print("abcdefgh"[::3]) # "adg"
print("Python"[::-1]) # "nohtyP" (otočení)
print("Programming"[1:10:2]) # "rgamn" (od 1 do 10, každý druhý)

# Praktické použití - kontrola DNA sekvence
dna = "ACGTTAGCTA"
first_codon = dna[0:3] # První kodon: "ACG"
print(f"První kodon: {first_codon}")

# Otočení řetězce (reverzní sekvence)
reversed_dna = dna[::-1]
print(f"Reverzní sekvence: {reversed_dna}")
```

---

#### ÚKOL: Extrakce data narození z rodného čísla

České rodné číslo má formát: RRMMDDXXXX (např. "9501152345")
- První 2 znaky = rok (95)
- Znaky 2-4 = měsíc (01)
- Znaky 4-6 = den (15)

Vytvoř program, který:

1. Načte rodné číslo
2. Pomocí slicingu extrahuje rok, měsíc a den
3. Vypíše: `"Datum narození: DD.MM.RR"`

---

### 3.3 For cyklus přes znaky

Řetězec můžeme procházet znak po znaku pomocí `for`:

```python
word = "Python"

for character in word:
 print(character)
```

Výstup:
```
P
y
t
h
o
n
```

**💻 Zkus:**

**1) Vypiš každý druhý znak:**
```python
text = "Programming"
for i in range(0, len(text), 2): # 0, 2, 4, 6, ...
 print(text[i])
# Výstup: P, o, r, m, i, g
```

**2) Spočítej počet malých písmen:**
```python
text = "Hello World"
count = 0

for char in text:
 if char.islower():
 count += 1

print(f"Počet malých písmen: {count}") # 8
```

**3) Bonusový úkol - spočítej výskyty "a":**
```python
text = "banana"
count = 0

for char in text:
 if char == "a":
 count += 1

print(f"Písmeno 'a' se vyskytuje {count}×") # 3

# Nebo jednoduše pomocí metody:
print(text.count("a")) # 3
```

---

#### ÚKOL: Kontrola GC obsahu v DNA

V bioinformatice je důležitý GC obsah (% bází G a C v sekvenci).

Vytvoř program, který:

1. Vytvoří proměnnou `dna` s nějakou sekvencí (např. `"ACGTTAGCTA"`)
2. Pomocí for cyklu projde všechny znaky
3. Spočítá, kolikrát se objevuje `"G"` nebo `"C"`
4. Vypíše: `"GC obsah: X znaků"`

---


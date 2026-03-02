# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## CÍL 1: DATOVÉ TYPY A KONVERZE

Než se pustíme do práce s řetězci, musíme rozumět **datovým typům** a jak převádět mezi nimi.

### 1.1 Základní datové typy

| Typ | Název | Příklad |
|---------|----------------------|-----------------------|
| `int` | Celé číslo | `42`, `-10`, `0` |
| `float` | Desetinné číslo | `3.14`, `-0.5` |
| `str` | Řetězec | `"Hello"`, `'Python'` |
| `bool` | Pravdivostní hodnota | `True`, `False` |

### 1.2 Ověření typu

```python
value = "123"

print(type(value)) # <class 'str'>
print(isinstance(value, str)) # True
print(isinstance(value, int)) # False
```

### 1.3 Převod typů

**Text → Číslo:**
```python
age_text = "25"
age = int(age_text)
print(type(age_text)) # <class 'str'>
print(type(age)) # <class 'int'>
print(age + 5) # 30

price_text = "19.99"
price = float(price_text)
print(type(price_text)) # <class 'str'>
print(type(price)) # <class 'float'>
print(price * 2) # 39.98
```

**Číslo → Text:**
```python
score = 100
print(type(score)) # <class 'int'>
message = "Skóre: " + str(score)
print(type(message)) # <class 'str'>
print(message) # "Skóre: 100"
```


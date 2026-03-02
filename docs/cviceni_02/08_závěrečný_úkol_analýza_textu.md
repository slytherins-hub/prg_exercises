# CVIČENÍ 2: DATOVÉ TYPY TEXTOVÉ ŘETĚZCE

Algoritmizace a programování

## ZÁVĚREČNÝ ÚKOL: ANALÝZA TEXTU

Vytvoř program `text_analyzer.py`, který:

1. **Načte větu** od uživatele
2. **Vypíše statistiku:**

 - Počet znaků (včetně mezer)
 - Počet slov
 - Počet samohlásek (a, e, i, o, u - bez ohledu na velikost)
3. **Vypíše větu pozpátku**
4. **Pokud věta obsahuje slovo "python"** (bez ohledu na velikost písmen), vypíše gratulaci

**Příklad výstupu:**
```
Zadej větu: Python je super jazyk!

=== STATISTIKA ===
Počet znaků: 22
Počet slov: 4
Počet samohlásek: 7

Věta pozpátku: !kyzaj repus ej nohtyP

Gratulujeme! Vaše věta obsahuje slovo 'python'! 🐍
```

**Nápověda:**

- Samohlásky můžeš uložit jako: `vowels = "aeiouAEIOUáéíóúůÁÉÍÓÚŮ"`

---


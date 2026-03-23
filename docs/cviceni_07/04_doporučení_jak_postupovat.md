# CVIČENÍ 7: PROCVIČOVÁNÍ

Algoritmizace a programování

## DOPORUČENÍ: JAK POSTUPOVAT

Tato stránka shrnuje praktické rady, jak si práci s úkoly usnadnit a nenaseknout se zbytečně na technikáliích.

---

## 🔧 Naklonování repozitáře

Zadání dostaneš přes GitHub Classroom. Odkaz najdeš v [e-learningu](https://moodle.vut.cz/course/section.php?id=127417).

Po přijetí zadání získáš vlastní repozitář – ten si naklonuj do počítače:

```bash
git clone https://github.com/<tvuj-repozitar>.git
```

> **💡 Tip:** U testu budeš mít k dispozici pouze PyCharm. Terminál v PyCharmu otevřeš přes **View → Tool Windows → Terminal** (nebo záložka *Terminal* dole). Použij ho k naklonování repozitáře a spouštění testů – úplně stejně jako kdykoli jinde.

---

## 📤 Příkazy pro Git

Po každé smysluplné změně kód uložíš a odešleš na GitHub:

**Přidat konkrétní soubor ke commitu:**
```bash
git add nazev_souboru.py
```

**Přidat všechny změněné soubory najednou:**
```bash
git add .
```

**Vytvořit commit:**
```bash
git commit -m "Stručný popis změny"
```

**Odeslat na GitHub:**
```bash
git push
```

> **💡 Tip:** Commituj průběžně – po každé funkci, ne až na konci. Uvidíš historii práce a v případě chyby se můžeš vrátit.

---

## 🧪 Příkazy pro pytest

Testy jsou připravené v repozitáři a ověřují, zda tvoje funkce fungují správě.

**Instalace závislostí:**
```bash
uv sync
```

**Spuštění všech testů:**
```bash
uv run pytest -v
```

**Spuštění konkrétního souboru s testy:**
```bash
uv run pytest tests/name_of_the_test_file.py
```

---

## 💡 Jak efektivně řešit úkoly

### 1. Nejdřív skript, pak funkce

Nezačínej rovnou psát funkci. Nejprve si napiš jednoduchý skript, který daný problém vyřeší „narovinu" – bez parametrů, jen pro jeden konkrétní příklad. Až když vidíš, že logika funguje, přepiš ji do funkce.

### 2. Připrav si ukázkový vstup

Než začneš psát kód, vymysli si co nejjednodušší příklad vstupu a očekávaný výstup. Ukázkový vstup si můžeš vzít i přímo z testovacího souboru – testy jsou dobrý zdroj toho, jak má funkce fungovat.

```python
# Příklad: ručně definovaný vstup pro ladění
kontakty = {
    "Jan Novák": {"telefon": "123456789", "email": "jan@example.com"}
}
```

### 3. Testuj funkci hned po napsání

Po dokončení každé funkce ji ihned otestuj spuštěním odpovídajícího testu. Nečekej, až napíšeš celý program – chyby se pak hledají mnohem hůř.

```bash
uv run pytest tests/test_1_check_phone_number.py -v
```

### 4. Pokud předchozí funkce nefunguje, pokračuj dál

Pokud se ti nepodaří dokončit jednu funkci a další na ní závisí, nevázni. Vytvoř si ručně ukázkový výstup, který by ta nefunkční funkce vrátila, a pracuj s ním dál. Tak aspoň ukážeš, že rozumíš zbytku zadání.

```python
# Simulovaný výstup předchozí funkce (pro případ, že ještě nefunguje)
nactene_kontakty = [
    {"jméno": "Jana Dvořáková", "telefon": "987654321", "email": "jana@example.com"}
]
```

### 5. Čti chybové hlášky pozorně

Když test selže, pytest ti vypíše přesně, co čekal a co dostal. Čti výstup pečlivě – bývá tam přímý návod, kde je chyba.

### 6. Spouštěj kód průběžně po každém kroku

Při psaní každé funkce si kód spouštěj co nejčastěji – ideálně po každém novém řádku. Tak okamžitě vidíš, co kód dělá, a nečekáš s hledáním chyby na konec. Kratší smyčka „napíšu → spustím → opravím" tě posune mnohem rychleji než psaní většího celku najednou.

### 7. Zakomentuj nepotřebné části, pomocné věci dej do extra souboru

Pokud ti nějaká část kódu pro aktuální krok překáží (např. ještě nefunkční funkce, testovací výpisy nebo nedopsaná logika), zakomentuj ji a pokračuj dál. Nemusíš ji mazat – stačí ji dočasně vypnout.

```python
# result = funkce_ktera_zatim_nefunguje(vstup)
result = ["testovaci", "data"]  # dočasná náhrada
```

Pokud potřebuješ oddělit pomocný kód od hlavního řešení, vytvoř si pomocný soubor (např. `scratch.py`). Nezapomeň ho pak přidat do commitu:

```bash
git add scratch.py
git commit -m "Přidán pomocný soubor pro ladění"
```

> **⚠️ Pozor:** Upravuj pouze svůj hlavní skript. Neupravuj testovací soubory ani jiné soubory v repozitáři – testy musí zůstat tak, jak jsou, aby správně ověřovaly tvoje řešení.

### 8. Jeden problém v jednu chvíli

Neřeš najednou načtení dat, výpočet i výpis. Rozlož úkol na malé kroky a každý krok zvlášť ověř. Debuguj po malých kouscích.

> **⚠️ Pozor:** Pokud test prochází, ale program se chová divně v jiných situacích, vyzkoušej hranační případy – prázdný seznam, neexistující kontakt, duplicitní jméno apod.

---

## ✅ Shrnutí doporučeného postupu

1. Naklonuj repozitář (`git clone ...`)
2. Přečti si zadání a testy – zjisti, co funkce mají dělat
3. Připrav si ukázkový vstup
4. Napiš nejdřív skript, pak přepiš na funkci
5. Po každé funkci spusť odpovídající test
6. Spouštěj kód průběžně – po každém novém řádku
7. Zakomentuj si části, které zatím nepotřebuješ; pomocné věci dej do extra souboru
8. Upravuj pouze svůj hlavní skript – testovací soubory nech být
9. Commituj průběžně (`git add`, `git commit`, `git push`)
10. Pokud jedna funkce nefunguje, nevázni – pokračuj dál s ručním vstupem

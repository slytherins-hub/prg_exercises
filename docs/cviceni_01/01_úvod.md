# CVIČENÍ 1: PRVNÍ KROKY S PYTHONEM

Algoritmizace a programování

## ÚVOD

Vítejte v kurzu programování! Možná si říkáte: "Proč bych se měl učit programovat, když existují AI nástroje?" nebo "Já budu v medicíně, k čemu mi to bude?" Odpověď je jednoduchá: **umět programovat znamená umět řešit problémy systematicky** – a to je dovednost, kterou využijete všude.

### Proč umět programovat?

#### Programování v medicíně a bioinženýrství

Pokud chcete dělat zajímavou a perspektivní práci, programování je klíčové:

**Lékařská diagnostika a analýza:**

- Detekce nádorů a tkání v CT či MR obrazech
- Umělá inteligence pro diagnostiku onemocnění
- Biometrie a zpracování biologických signálů
- Algoritmy pro laboratorní, diagnostické a terapeutické přístroje

**Mobilní a nositelné technologie:**

- Aplikace pro zdravotnickou záchrannou službu
- Sport technology a fitness trackery
- Wearable devices (chytré hodinky, senzory)
- Monitorování pacientů na dálku

**A kam se programování ještě vejde?**

Podívejte se na svůj rozvrh – **programování se v něm objeví znovu a znovu**:

| 1. ročník | 2. ročník | 3. ročník |
|----------------------------------|---------------------------------------|-----------------------------------------|
| **Algoritmizace a programování** | Úvod do medicínské informatiky | Umělá inteligence v medicíně |
| | Číslicové zpracování signálů a obrazů | Modely v biologii a epidemiologii |
| | Bioinformatika | Praktika z bioinformatiky |
| | Analýza biologických signálů | Semestrální práce, **Bakalářská práce** |

> **Vyhnout se programování nejde.** Buď se ho naučíte teď pořádně, nebo budete trpět později.

### Co je to algoritmus?

Než začneme psát kód, musíme pochopit, co vlastně programujeme. **Algoritmus** je **přesně definovaný postup**, jak dojít od vstupu k výstupu.

**Příklad z běžného života:**
```
Vstup: Ingredience (mouka, vejce, mléko)
Algoritmus: Recept na palačinky (smíchej, ohřej pánev, smaž...)
Výstup: Hotové palačinky
```

#### Základní požadavky na algoritmus

Dobrý algoritmus musí splňovat 5 vlastností:

| Vlastnost | Význam | Příklad (špatně → dobře) |
|--------------------|--------------------------------------|-------------------------------------------------------|
| **Vstup a výstup** | 0 nebo více vstupů, alespoň 1 výstup | "Udělej něco" → "Sečti čísla a vrať výsledek" |
| **Efektivita** | Minimální nároky na paměť a čas | Hledání v seznamu: projít vše vs. binární vyhledávání |
| **Jednoznačnost** | Každý krok přesně definován | "Ohřej trochu" → "Ohřej na 180 °C" |
| **Univerzálnost** | Řeší celou třídu problémů | "Sečti 5+3" → "Sečti dvě čísla" |
| **Konečnost** | Musí skončit po konečném počtu kroků | "Opakuj, dokud..." → "Opakuj 5×" |

**Příklad špatného algoritmu:**

```
1. Vezmi dva kousíčky
2. Smíchej je trochu
3. Opakuj, dokud to nebude dobré
```
Proč je špatný? Není jednoznačný ("kousíčky" = kolik?), není jasná konečnost ("dokud to nebude dobré" = kdy?).

**Dobrý algoritmus:**

```python
1. Načti dvě čísla: a, b
2. Sečti je: vysledek = a + b
3. Vrať vysledek
```
Splňuje vše: jasný vstup (a, b), jednoznačné kroky, skončí po 3 krocích, funguje pro libovolná čísla.

**Praktický příklad z medicíny:** Algoritmus pro detekci horečky

```python
# Špatně - nejasné
"Pokud má pacient teplotu, zavolej doktora"

# Dobře - přesné
1. Načti teplotu pacienta (°C)
2. Je teplota >= 38.0?
 ANO: Zašli upozornění lékaři
 NE: Pokračuj v monitorování
3. Zapiš měření do databáze
```

Tento algoritmus má jasný vstup (teplota), jednoznačné kroky (konkrétní hodnota 38.0 °C), vždy skončí a funguje univerzálně pro všechny pacienty.

### Proč Python?

Existují desítky programovacích jazyků (C, Java, JavaScript, R...). Proč zrovna Python?

#### 1. Jednoduchá syntaxe
Python vypadá skoro jako angličtina. Porovnejte **stejný program** v různých jazycích:

**Python:**
```python
temperatures = [36.5, 37.2, 38.1, 37.8]
average = sum(temperatures) / len(temperatures)
print(f"Průměrná teplota: {average} °C")
```

**Java:**
```java
double[] temperatures = {36.5, 37.2, 38.1, 37.8};
double sum = 0;
for (double temp : temperatures) {
 sum += temp;
}
double average = sum / temperatures.length;
System.out.printf("Průměrná teplota: %.1f °C\n", average);
```

**C:**
```c
#include <stdio.h>
int main() {
 double temps[] = {36.5, 37.2, 38.1, 37.8};
 double sum = 0;
 int n = sizeof(temps) / sizeof(temps[0]);
 for (int i = 0; i < n; i++) {
 sum += temps[i];
 }
 printf("Průměrná teplota: %.1f °C\n", sum / n);
 return 0;
}
```

**JavaScript:**
```javascript
const temperatures = [36.5, 37.2, 38.1, 37.8];
const average = temperatures.reduce((a, b) => a + b) / temperatures.length;
console.log(`Průměrná teplota: ${average.toFixed(1)} °C`);
```

Všimněte si: Python má **3 řádky**, Java 7, C 10. Python je nejčitelnější.

#### 2. Nejpoužívanější jazyk
Podle žebříčků TIOBE (2024–2026) je Python nejpoužívanější jazyk světa. Na GitHubu je 2. nejčastější.

**Stručná historie Pythonu:**

```
1991 ━━ Guido van Rossum vydává Python 0.9.0
 "Monty Python" → název jazyka 🐍

2000 ━━ Python 2.0 (list comprehensions, Unicode)

2008 ━━ Python 3.0 (zlom kompatibility)

2015 ━━ Boom v datové vědě (Pandas, NumPy)

2018 ━━ AI revoluce (TensorFlow, PyTorch mainstream)

2024 ━━ Python #1 na TIOBE
 Většina AI modelů běží na Pythonu
```

**Kdo používá Python?**
- **Google** – vyhledávání, YouTube, Gmail
- **Meta** – Instagram (Django framework)
- **Netflix** – doporučovací systémy
- **Spotify** – analýza dat, doporučení hudby
- **NASA** – analýza dat z vesmíru
- **CERN** – analýza dat z urychlovače částic

#### 3. Flexibilita
Python umí **všechno**:

- **Vědecké výpočty** (NumPy, SciPy)
- **Datová analytika** (Pandas, Matplotlib)
- **Umělá inteligence** (TensorFlow, PyTorch)
- **Webové aplikace** (Django, Flask)
- **Automatizace** (skripty pro úkoly)

#### 4. Obrovská komunita
- **Stack Overflow** – 5. největší komunita (miliony odpovědí)
- **GitHub** – statisíce open-source projektů
- Pokud máte problém, někdo už ho vyřešil a odpověď je na Google

### Role AI nástrojů (GitHub Copilot)

Programování se mění a nástroje jako **GitHub Copilot** se stávají průmyslovým standardem. Je **velmi důležité**, abyste se s nimi v budoucnu naučili pracovat.

> **⚠️ Důležité pro začátečníky:**
> I když jsou AI asistenti skvělí, **první kroky musíte zvládnout sami**. Pokud si základy (proměnné, cykly, podmínky) "neodřete" vlastním psaním a chybováním, nenaučíte se algoritmicky myslet. Bez pevných základů navíc nedokážete poznat, kdy AI udělala chybu – a to se stává častěji, než si myslíte. **Berte AI jako kalkulačku: je skvělá, ale musíte vědět, co počítáte.**

### Jak se naučit programovat?

**Programování se naučíte jedině programováním.** Je to dovednost jako sport nebo hra na hudební nástroj. Můžete přečíst stohy knih a zhlédnout hodiny videí, ale dokud nezačnete sami psát kód, dělat chyby a opravovat je, neposunete se. Žádná zkratka neexistuje, chce to jen čas a trpělivost.

**Kam se obrátit, když nevíte rady?**

| Zdroj | Kdy/jak použít |
|--------------------|------------------------------------------|
| **Vyučující** | Nejrychlejší pomoc při cvičení |
| **Dokumentace** | `help(funkce)` v Pythonu, oficiální docs |
| **Google** | "how to find minimum in array Python" |
| **Stack Overflow** | Téměř každý problém už někdo řešil |
| **AI asistenti** | Po zvládnutí základů |

### Self-check: Jsi připravený?

Než začneme programovat, zkontroluj, zda rozumíš základním konceptům:

| Otázka | Odpověď |
|--------------------------------------------|--------------------------------------------------------|
| Co je algoritmus? | Přesně definovaný postup s konečným počtem kroků |
| Musí mít algoritmus vstup? | Ne, ale musí mít alespoň 1 výstup |
| Je `"Zahřej trochu"` dobrý krok algoritmu? | NE – není jednoznačný (kolik = trochu?) |
| Proč používáme Python? | Jednoduchá syntaxe, obrovská komunita, AI/data science |
| Můžu používat AI hned od začátku? | NE – nejdřív základy ručně, pak AI |
| Jak se naučím programovat? | Pouze programováním (praxe > teorie) |

---


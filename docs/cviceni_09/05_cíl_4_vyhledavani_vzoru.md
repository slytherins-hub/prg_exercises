# CVIČENÍ 9: ALGORITMY VYHLEDÁVÁNÍ

Algoritmizace a programování

## CÍL 4: VYHLEDÁVÁNÍ VZORŮ

V předchozích částech jsi vyhledával vždy jen jeden konkrétní prvek. V celé řadě případů je ale potřeba vyhledávat 
posloupnost prvků, tedy vzor. V tomhle cíli si rozšíříš předchozí úlohy na vyhledávání vzorů v sekvenci DNA.

### 4.1 Vyhledávání vzorů v sekvenci

Měj data opět uložená v iterovatelné datové struktuře, tentokrát v textovém řetězci. Naivní algoritmus hledání vzoru 
opět spočívá v tom, že postupně projdeš sekvenci a porovnáváš vzor s aktuálním podřetězcem prohledávané sekvence.

![Vyhledávání vzoru](../assets/cviceni_10/09_pattern_matching_diagram.png)

Základní princip algoritmu pro nalezení pozic vzoru v sekvenci může vypadat např. takto:

1. Nastav ukazatel v analyzované sekvenci na podřetězec o délce $m$, kde $m$ je délka vzoru.
2. Porovnej shodu prvků mezi vzorem a aktuálním podřetězcem.
3. Pokud jsou všechny prvky shodné, ulož pozici začátku nalezeného výskytu vzoru.
4. Posuň ukazatel o jednu pozici doprava.
5. Opakuj předchozí kroky dokud existuje oblast, která ještě nebyla prohledána.

#### ÚKOL: Vyhledávání vzorů v DNA

Implementuj algoritmus sekvenčního vyhledávání vzorů, který v řetězci DNA najde pozice výskytu zadaného vzoru. 
Délka vzoru může být různá.

1. V modulu `searching.py` vytvoř funkci `pattern_search()`.
2. Funkce bude mít dva vstupní parametry:
   - prohledávanou sekvenci,
   - hledaný vzor.
3. Funkce vrátí množinu, ve které budou uložené pozice (indexy) výskytu vzoru v sekvenci.
4. Volání funkce a korektnost implementace ověř z hlavní funkce `main()`.
5. V hlavní funkci definuj vyhledávaný vzor, například `ATA`. 
6. Prohledávanou sekvenci získej ze souboru `sequential.json` pod klíčem `dna_sequence`.
7. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

---

### 4.2 Upravené vyhledávání vzorů

V naivním algoritmu z předchozího úkolu jsme v každé iteraci provedli až $m$ operací (porovnání), kde $m$ je délka vzoru.
To můžeš ještě trochu vylepšit.

Porovnání jednotlivých prvků v jedné iteraci má totiž smysl provádět jen do té doby, dokud jsou prvky shodné. 
Ve chvíli, kdy nalezneš první neshodu, nemá smysl v porovnání dalších prvků pokračovat a můžeš se přesunout rovnou 
na další iteraci.

#### ÚKOL: Vylepšení vyhledávání vzorů

1. Uprav algoritmus ve funkci `pattern_search()` tak, aby při nalezení první neshody automaticky pokračoval další iterací.
2. Při pokračování proveď posun indexu o jednu pozici doprava a porovnej nový podřetězec.
3. Vytvoř novou revizi (`commit`) a změny nahraj na svůj vzdálený repozitář (`push`).

---

### 4.3 Analýza algoritmu vyhledávání vzorů

Proveď analýzu naivního „vylepšeného“ algoritmu vyhledávání vzorů a odhadni jeho asymptotickou složitost pro 
případy uvedené v tabulce níže. Pro zápis uvažuj: $n$ – délka analyzované sekvence; $m$ – délka vzoru.

|                 | Kdy nastane? | Asymptotická složitost |
|-----------------|--------------|------------------------|
| Nejlepší scénář |              |                        |
| Nejhorší scénář |              |                        |

---
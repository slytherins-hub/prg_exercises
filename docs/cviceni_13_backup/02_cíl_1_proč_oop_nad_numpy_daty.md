# CVIČENÍ 13: OOP

Algoritmizace a programování

## CÍL 1: PROČ OOP

### 1.1 Kdy začíná být samotná funkce málo

Představ si, že máš nějaká data uložená v `numpy` poli. Jako konkrétní příklad vezměme měřený signál:

```python
import numpy as np

ekg = np.array([0.12, 0.15, 0.11, 0.52, 1.10, 0.48, 0.16, 0.10])
sampling_rate = 250
signal_name = "EKG"
patient_id = "P-102"
```

Na první pohled je to jednoduché. Jenže časem budeš chtít:

- spočítat průměr,
- signál normalizovat,
- vyříznout úsek,
- vykreslit ho,
- uložit k němu další metadata.

Pokud všechno necháš jako volné proměnné a samostatné funkce, začne se kód rychle rozpadat do spousty částí, které spolu souvisí jen „v hlavě programátora“.

### 1.2 Co objekt řeší

Objekt ti dovolí držet pohromadě:

- samotná data,
- popis dat,
- operace, které s nimi chceš dělat.

Místo několika nesouvisejících proměnných pak můžeš mít třeba objekt `Signal`, který ví:

- jaké hodnoty obsahuje,
- jaká je vzorkovací frekvence,
- jaký má název,
- jak si spočítat průměr nebo maximum.

### 1.3 Co si zkusíš

V dalších částech cvičení vytvoříš dvě ukázkové třídy:

1. třídu nad signálovými daty,
2. třídu nad sekvenčními daty.

Obě budou používat `numpy` tam, kde to dává praktický smysl, ale hlavním tématem zůstává návrh tříd, atributů a metod.

**📝 ÚKOL: Kdy by se ti objekt hodil?**

1. Vezmi si příklad signálu nebo sekvence.
2. Sepiš alespoň 4 údaje, které o datech potřebuješ držet pohromadě.
3. Sepiš alespoň 3 operace, které nad těmito daty chceš opakovaně provádět.
4. Zkus jednou větou popsat, proč by tady objekt dával smysl.

> **💡 Poznámka:** Tohle je důležitější než samotná syntaxe. Když pochopíš, proč objekt vzniká, bude se ti pak mnohem líp psát i samotný kód.

---
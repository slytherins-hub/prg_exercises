# CVIČENÍ 12: JUPYTER, NUMPY, MATPLOTLIB

Algoritmizace a programování

## CÍL 4: ÚKOL – ANALÝZA BIOSIGNÁLŮ

### 4.1 Zadání

V tomto cíli zpracuješ dataset krátkých biosignálů a odpovíš na konkrétní otázky pomocí numpy a matplotlib. Celé zpracování bude v Jupyter Notebooku – kód i komentáře.

---

### 4.2 Data

Generuj data přímo v notebooku – tato funkce vytvoří sadu realistických signálů pro skupinu pacientů:

```python
import numpy as np

def generate_patient_data(n_patients=20, duration=10, fs=250, seed=42):
    """
    Vygeneruje sadu simulovaných biosignálů pro skupinu pacientů.

    Args:
        n_patients: počet pacientů
        duration:   délka záznamu v sekundách
        fs:         vzorkovací frekvence v Hz
        seed:       seed pro reprodukovatelnost

    Returns:
        signals:    2D pole (n_patients × n_samples) – EKG-like signály
        heart_rates: 1D pole – průměrné tepové frekvence (BPM)
        ages:       1D pole – věk pacientů
        labels:     1D pole – 0 = zdravý, 1 = pacient s arytmií
    """
    rng = np.random.default_rng(seed)
    n_samples = duration * fs
    t = np.linspace(0, duration, n_samples)

    signals = np.zeros((n_patients, n_samples))
    heart_rates = rng.integers(55, 100, size=n_patients).astype(float)
    ages = rng.integers(25, 80, size=n_patients)
    labels = (rng.random(n_patients) > 0.65).astype(int)   # ~35 % arytmie

    for i in range(n_patients):
        hr = heart_rates[i]
        rr = 60 / hr   # délka R-R intervalu v sekundách
        # Umístění R-peaků s malým jitterem
        peaks = np.arange(rr / 2, duration, rr)
        if labels[i] == 1:   # arytmie – nepravidelné R-R intervaly
            peaks += rng.uniform(-0.15, 0.15, size=len(peaks))

        sig = np.zeros(n_samples)
        for p in peaks:
            idx = int(p * fs)
            if 0 < idx < n_samples:
                window = np.arange(max(0, idx - 20), min(n_samples, idx + 20))
                local_t = (window - idx) / fs
                sig[window] += (
                    1.5 * np.exp(-(local_t ** 2) / 0.0005)
                    - 0.3 * np.exp(-((local_t + 0.02) ** 2) / 0.0003)
                )
        sig += rng.normal(0, 0.06, n_samples)
        signals[i] = sig

    return signals, heart_rates, ages, labels

signals, heart_rates, ages, labels = generate_patient_data()
print(f"Signály: {signals.shape}  ({signals.shape[0]} pacientů × {signals.shape[1]} vzorků)")
print(f"Tepové frekvence: min={heart_rates.min():.0f}, max={heart_rates.max():.0f}, průměr={heart_rates.mean():.1f} BPM")
print(f"Zdraví: {(labels == 0).sum()}, s arytmií: {(labels == 1).sum()}")
```

---

### 4.3 Úkoly

Vytvoř nový notebook `cviceni_12_analyza.ipynb`. Na začátek vlož funkci `generate_patient_data()` a vygeneruj data. Pak řeš postupně:

**Část 1 – Přehled dat**

1. Vypiš základní statistiky tepových frekvencí: průměr, medián, min, max, směrodatnou odchylku (použij numpy funkce).
2. Vykresli histogram tepových frekvencí. Zvol vhodný počet košů (bins), přidej popisky os a nadpis.
3. Vykresli boxplot srovnávající tepové frekvence skupiny *zdraví* (label 0) vs. *arytmie* (label 1). Jsou skupiny vizuálně odlišné?

**Část 2 – Vizualizace signálů**

4. Vykresli první 3 sekundy záznamu pro **jednoho zdravého** a **jednoho pacienta s arytmií** – oba grafy pod sebou (použij `plt.subplots(2, 1, sharex=True)`). Nadpis každého grafu uveď věk pacienta a jeho diagnózu.
5. Vykresli heatmapu `imshow()` prvních 10 pacientů – osy budou čas (x) a číslo pacienta (y). Zvol vhodnou colormap, přidej colorbar. Lze z heatmapy vizuálně odlišit zdravé od pacientů s arytmií?

**Část 3 – Numpy analýza**

6. Pro každý signál spočítej průměrnou absolutní hodnotu (`np.abs(signal).mean()`) – říká se jí MAV (*mean absolute value*) a používá se jako jednoduchá míra aktivity signálu. Výsledkem je 1D pole délky 20. Vykresli ho jako sloupcový graf (`plt.bar()`), sloupce obarvi podle diagnózy (zdravý = modrá, arytmie = červená).
7. Spočítej korelaci mezi věkem a tepovou frekvencí (`np.corrcoef(ages, heart_rates)[0, 1]`). Vykresli scatter plot (věk × tepová frekvence), body obarvi podle diagnózy. Do nadpisu přidej hodnotu korelačního koeficientu.

**Část 4 – Shrnutí**

8. Na konci notebooku přidej markdown buňku se stručným shrnutím: co jsi zjistil z dat? Jaké jsou rozdíly mezi skupinami? Co by bylo potřeba udělat pro skutečnou analýzu (více dat, validace, statistické testy…)?

---

### 4.4 Co odevzdat

Pushni do repozitáře GitHub Classroom oba notebooky:

- `cviceni_12_numpy.ipynb` – úkoly z cíle 2 a 3,
- `cviceni_12_analyza.ipynb` – úkoly z cíle 4.

Před pushnutím spusť v každém notebooku **Restart & Run All** a ověř, že vše proběhne bez chyb.

> **💡 Tip:** Jupyter Notebook se ukládá jako JSON soubor obsahující kód i výstupy (grafy, textové výstupy). Když ho pushneš na GitHub, GitHub ho automaticky vykreslí i s grafiky – přímo v prohlížeči bez spouštění.

---


# CVIČENÍ 12: JUPYTER, NUMPY, MATPLOTLIB

Algoritmizace a programování

## ODEVZDÁNÍ ÚKOLU

Podobně jako v minulém cvičení odevzdáš **vlastní nový repozitář** na GitHubu. Tentokrát v něm budou
**Jupyter Notebooky** (`.ipynb`) s vyplněnými úkoly — GitHub je umí přímo v prohlížeči vykreslit
i s grafy, takže reviewer uvidí tvé výsledky bez spuštění.

> **Poznámka:** První dvě části (vytvoření repa + klonování) udělej **hned teď**, než začneš pracovat
> na úkolech. Ostatní (commit, push, checklist, e-learning) si projdi postupně během cvičení
> a na jeho konci.

### Vytvoření nového repozitáře na GitHubu

1. Přihlas se na [github.com](https://github.com).
2. Vpravo nahoře klikni na **`+`** a vyber **`New repository`**.
3. Vyplň:
    - **Repository name:** například `prg-exercise-12` (nebo libovolný smysluplný název).
    - **Visibility:** zvol **Public**.
    - Zatrhni **Add a README file** — repozitář se vytvoří s jedním počátečním souborem, aby nebyl úplně prázdný.
4. Klikni **Create repository**.

### Klonování a příprava

1. Na stránce repozitáře klikni na zelené tlačítko **`Code`** a zkopíruj HTTPS adresu.
2. V terminálu přejdi do složky s dnešním cvičením a naklonuj repozitář:

    ```
    git clone <adresa>
    cd <nazev-slozky>
    ```

3. Do naklonované složky stáhni a rozbal data pro úkoly (odkazy najdeš v hlavičce každého
   notebooku — sekce Cíl 3–6). Po rozbalení budeš mít vedle notebooků složky `skupina_a/`,
   `skupina_b/`, `ekg_klid/`, `ekg_zatez/` a soubory `pacienti.npy`, `mpl_data.npz`.

### Vložení řešení a odevzdání

1. Do naklonované složky vlož vyplněné notebooky:

    - `cviceni_12_uvod.ipynb` — tvůj první notebook z Cíle 2,
    - `cviceni_12_numpy.ipynb` — vyplněný úkol z Cíle 3 (analýza dat klinické studie),
    - `cviceni_12_matplotlib.ipynb` — vyplněný úkol z Cíle 4 (zátěžový test),
    - `cviceni_12_segmentace.ipynb` — vyplněný úkol z Cíle 5 (segmentace snímků),
    - `cviceni_12_ekg.ipynb` — vyplněný úkol z Cíle 6 (detekce R-vrcholů a TF).

2. Před commitem v každém notebooku spusť **Restart & Run All** a ověř, že všechny buňky
   proběhnou bez chyby. GitHub pak vykreslí uložené výstupy (grafy, čísla) přímo v prohlížeči.

3. Ulož změny do Git historie (včetně datových souborů — repozitář má být spustitelný sám o sobě):

    ```
    git add *.ipynb pacienti.npy mpl_data.npz skupina_a/ skupina_b/ ekg_klid/ ekg_zatez/
    git commit -m "Řešení cvičení 12"
    git push
    ```

4. Otevři svůj repozitář v prohlížeči, klikni na libovolný `.ipynb` a ověř, že se notebook
   vykreslí včetně grafů.

> **Tip:** Commituj průběžně — po dokončení každého notebooku. Mezikroky se lépe kontrolují
> a při případné chybě se můžeš vrátit.

### Checklist před odevzdáním

Před finálním odevzdáním si odškrtni:

- všechny 4 cílové notebooky (`numpy`, `matplotlib`, `segmentace`, `ekg`) mají vyplněné poslední buňky s řešením,
- v každém notebooku proběhne **Restart & Run All** bez chyb,
- grafy a výstupy jsou uložené v notebooku (vidíš je na GitHubu v prohlížeči),
- u segmentace a EKG je vyplněná závěrečná **Interpretace**,
- všechna data potřebná pro spuštění jsou v repozitáři,
- repozitář je **Public** a jde otevřít i z anonymního okna prohlížeče.

### Odevzdání do e-learningu

<h2 style="color:#c62828;">❗❗ POVINNÉ ODEVZDÁNÍ</h2>
<ul style="color:#c62828;">
  <li>Pro splnění cvičení je nezbytné odevzdat do e-learningu funkční odkaz na repozitář.</li>
  <li>Cílem je mít v repozitáři vyplněné všechny úkoly z tohoto cvičení.</li>
  <li>Odevzdání a modifikace v repozitáři je nutné provést nejpozději do půlnoci v den cvičení.</li>
  <li>Ověř, že repozitář je <code>Public</code> a jde otevřít i z anonymního okna prohlížeče.</li>
</ul>

---

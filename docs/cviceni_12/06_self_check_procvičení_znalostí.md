# CVIČENÍ 12: JUPYTER, NUMPY, MATPLOTLIB

Algoritmizace a programování

## SELF-CHECK: PROCVIČENÍ ZNALOSTÍ

Tato část je dobrovolná a slouží jen pro rychlé ověření, že máš hlavní koncepty jisté.

### Část A: Python ekosystém a uv

1. **Co je virtuální prostředí (virtual environment)?**
   <ol type="a">
      <li>Speciální verze Pythonu pro Windows</li>
      <li>Cloudová služba pro spouštění Python kódu</li>
      <li>Izolovaná složka s vlastním Pythonem a sadou balíčků pro daný projekt</li>
      <li>Náhrada za Jupyter Notebook</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Virtuální prostředí je izolovaná složka (typicky <code>.venv/</code>), která má vlastní verzi Pythonu a vlastní sadu nainstalovaných balíčků. Díky tomu se projekty navzájem neovlivňují (např. dva projekty mohou používat různé verze numpy).

</details>

2. **Který soubor obsahuje seznam přímých závislostí projektu a měl by se commitovat do Gitu?**
   <ol type="a">
      <li><code>pyproject.toml</code></li>
      <li><code>.venv/</code></li>
      <li><code>requirements.txt</code></li>
      <li><code>__pycache__/</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> <code>pyproject.toml</code> je hlavní popis projektu — obsahuje sekci <code>dependencies</code>, verzi Pythonu a metadata. Vždy se commituje do Gitu, aby se projekt dal reprodukovat.

</details>

3. **K čemu slouží soubor `uv.lock`?**
   <ol type="a">
      <li>Zamyká projekt proti dalším úpravám</li>
      <li>Obsahuje hesla pro připojení k PyPI</li>
      <li>Je dočasný cache soubor a nemá se commitovat</li>
      <li>Zaznamenává přesné verze všech (i tranzitivních) závislostí pro reprodukovatelné prostředí</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>uv.lock</code> obsahuje přesné verze všech balíčků, které byly skutečně nainstalované — včetně tranzitivních závislostí. Díky tomu kolega po <code>uv sync</code> dostane bit-identické prostředí. Také se commituje do Gitu.

</details>

4. **Který příkaz správně přidá novou knihovnu `pandas` do projektu spravovaného přes uv?**
   <ol type="a">
      <li><code>pip install pandas</code></li>
      <li><code>uv add pandas</code></li>
      <li><code>uv install pandas</code></li>
      <li><code>uv tool install pandas</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>uv add pandas</code> přidá balíček do <code>pyproject.toml</code> a zároveň ho nainstaluje do virtuálního prostředí projektu. <code>uv tool install</code> je naopak pro globální CLI nástroje (např. <code>ruff</code>).

</details>

5. **Co znamená rozdíl mezi `uv add numpy` a `uv tool install ruff`?**
   <ol type="a">
      <li><code>uv add</code> přidá balíček do projektu (do <code>pyproject.toml</code>), <code>uv tool install</code> nainstaluje globální CLI nástroj dostupný odkudkoliv</li>
      <li>Není žádný — oba přidají balíček do projektu</li>
      <li><code>uv add</code> stahuje z PyPI, <code>uv tool install</code> z conda-forge</li>
      <li><code>uv add</code> je novější verze <code>uv tool install</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> <code>uv add</code> je pro projektové závislosti (knihovny jako numpy, matplotlib, které potřebuješ v Python kódu). <code>uv tool install</code> je pro globální CLI nástroje (linters, formátovače) — nainstalují se zvlášť a nemíchají se s projektovými prostředími.

</details>

6. **Která složka by NEMĚLA být commitnutá do Gitu (patří do `.gitignore`)?**
   <ol type="a">
      <li><code>pyproject.toml</code></li>
      <li>složka s tvými notebooky</li>
      <li><code>uv.lock</code></li>
      <li><code>.venv/</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>.venv/</code> obsahuje stovky MB nainstalovaných balíčků. Generuje se lokálně z <code>pyproject.toml</code> + <code>uv.lock</code> příkazem <code>uv sync</code>, takže se necommituje. Repozitář pak zůstává malý.

</details>

---

### Část B: Jupyter Notebook

7. **Jakou koncovku mají Jupyter Notebooky?**
   <ol type="a">
      <li><code>.py</code></li>
      <li><code>.jpy</code></li>
      <li><code>.ipynb</code></li>
      <li><code>.ipy</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Notebooky se ukládají jako <code>.ipynb</code> (IPython Notebook). Je to JSON soubor obsahující buňky s kódem, výstupy a markdown.

</details>

8. **Co se stane, když v buňce A nastavíš `x = 42`, spustíš ji, pak buňku A smažeš a v buňce B napíšeš `print(x)` a spustíš ji?**
   <ol type="a">
      <li>Vyhodí <code>NameError</code> — proměnná byla smazána spolu s buňkou</li>
      <li>Vypíše <code>42</code>, dokud nerestartuješ kernel — proměnná zůstává v paměti</li>
      <li>Vypíše <code>None</code></li>
      <li>Notebook spadne</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Buňky sdílí stav v kernelu. Smazání buňky neodstraní proměnnou z paměti — ta tam zůstane, dokud nerestartuješ kernel. Právě proto je důležité před odevzdáním spustit <strong>Restart &amp; Run All</strong>.

</details>

9. **Co dělá vykřičník `!` na začátku řádku v buňce notebooku, např. `!uv add cowsay`?**
   <ol type="a">
      <li>Označí buňku jako důležitou</li>
      <li>Spustí příkaz dvakrát rychleji</li>
      <li>Pošle zbytek řádku do shellu (operačního systému) místo do Pythonu</li>
      <li>Vyvolá výjimku</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> Vykřičník v IPython/Jupyteru znamená „spusť tohle v shellu, ne v Pythonu". Hodí se na rychlou instalaci balíčků (<code>!uv add ...</code>), výpis souborů (<code>!ls</code>) nebo kontrolu prostředí.

</details>

10. **Co vypíše tato buňka po spuštění `Shift+Enter`?**
    ```python
    a = 3
    b = 4
    c = (a**2 + b**2) ** 0.5
    c
    ```
    <ol type="a">
      <li>Nic — chybí <code>print()</code></li>
      <li>Chybu, protože proměnná musí být <code>print(c)</code></li>
      <li><code>None</code></li>
      <li><code>5.0</code> — IPython automaticky vypíše hodnotu posledního výrazu v buňce</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> Jednou z výhod IPython oproti klasickému Pythonu je, že hodnota posledního výrazu v buňce se vypíše automaticky bez nutnosti psát <code>print()</code>.

</details>

---

### Část C: NumPy

11. **Proč jsou NumPy pole rychlejší než Python listy pro numerické operace?**
    <ol type="a">
      <li>NumPy používá vlákna a běží paralelně</li>
      <li>NumPy ukládá data v kompaktním bloku paměti stejného typu a operace jsou implementované v C/Fortran</li>
      <li>NumPy je napsaný v Rustu</li>
      <li>Python listy mají záměrně zpomalený přístup</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> NumPy ndarray drží data jako souvislý blok paměti se stejným dtype (např. <code>float64</code>). Vektorizované operace (<code>a * 2</code>, <code>a + b</code>) běží v kompilovaném C/Fortran kódu — bez Python smyčky. Výsledek je často 10–100× rychlejší.

</details>

12. **Co vrátí `np.linspace(0, 1, 6)`?**
    <ol type="a">
      <li>Šest rovnoměrně rozložených hodnot od 0 do 1 včetně, tj. <code>[0. , 0.2, 0.4, 0.6, 0.8, 1. ]</code></li>
      <li>Hodnoty <code>[0, 1, 2, 3, 4, 5]</code></li>
      <li>Hodnoty <code>[0, 1, 2, 3, 4, 5, 6]</code></li>
      <li>Šest náhodných hodnot z intervalu &lt;0, 1&gt;</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> <code>np.linspace(start, stop, num)</code> vytvoří <code>num</code> rovnoměrně rozložených hodnot včetně obou krajních. Hodí se např. pro vytvoření časové osy. Naopak <code>np.arange(start, stop, krok)</code> jde po krocích a stop nezahrnuje.

</details>

13. **Co vypíše tento kód?**
    ```python
    import numpy as np
    data = np.array([10, 20, 30, 40, 50])
    print(data[data > 25])
    ```
    <ol type="a">
      <li><code>[True False True True True]</code></li>
      <li>Chybu</li>
      <li><code>[30 40 50]</code></li>
      <li><code>[25 30 40 50]</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>data > 25</code> vrátí logickou masku <code>[False, False, True, True, True]</code>. Použití této masky jako indexu (boolean indexing) vrátí jen prvky, kde je maska <code>True</code>, tedy <code>[30, 40, 50]</code>.

</details>

14. **Co znamená `axis=0` u funkce `mereni.mean(axis=0)` na 2D matici, kde řádky jsou pacienti a sloupce ukazatele (systola, diastola, TF)?**
    <ol type="a">
      <li>Spočítá průměr každého řádku (jeden průměr na pacienta)</li>
      <li>Spočítá průměr přes sloupce — agreguje přes řádky, výsledkem je hodnota pro každý sloupec (každý ukazatel)</li>
      <li>Spočítá globální průměr přes všechna data</li>
      <li>Vyhodí chybu, <code>axis</code> musí být 1</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> <code>axis=0</code> agreguje přes řádky — pro každý sloupec dostaneš jednu hodnotu. U matice pacientů tak získáš průměr každého ukazatele (systola, diastola, TF). <code>axis=1</code> by naopak průměrovalo každý řádek (průměr na pacienta).

</details>

15. **Co vrací funkce `np.argmax(tf)` pro pole `tf = np.array([72, 90, 65, 88])`?**
    <ol type="a">
      <li>Hodnotu <code>90</code> (samotné maximum)</li>
      <li>Pole <code>[72, 90, 65, 88]</code> seřazené sestupně</li>
      <li>Index <code>3</code></li>
      <li>Index <code>1</code> (pozici, na které leží maximum)</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>argmax</code> nevrací hodnotu, ale <strong>index</strong>, na kterém maximum leží. Hodí se vždy, když potřebuješ vědět „kde" — třeba pacient s nejvyšší TF nebo čas R-vrcholu. Hodnotu pak získáš přes <code>tf[tf.argmax()]</code>.

</details>

16. **Najdi chybu v tomto kódu, který má z 1D pole `flat = np.arange(12)` udělat matici 3×4:**
    ```python
    matice = flat.reshape(3, 5)
    ```
    <ol type="a">
      <li>Chybí <code>import numpy</code></li>
      <li>Funkce by se měla jmenovat <code>resize</code></li>
      <li>3 × 5 = 15, ale pole má 12 prvků — počet prvků se musí rovnat součinu rozměrů</li>
      <li>Reshape vyžaduje pojmenovaný argument <code>shape=</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>reshape</code> vyžaduje, aby součin nových rozměrů byl roven počtu prvků. 12 prvků → můžeš použít (3, 4), (4, 3), (2, 6), (12, 1)… ale ne (3, 5). Správně je <code>flat.reshape(3, 4)</code>. Můžeš taky použít <code>-1</code> pro automatický dopočet, např. <code>flat.reshape(3, -1)</code>.

</details>

17. **K čemu slouží formát `.npz` v NumPy?**
    <ol type="a">
      <li>Pro uložení obrázků ve formátu PNG</li>
      <li>Pro export dat do Excelu</li>
      <li>Pro uložení jednoho 1D pole jako textový soubor</li>
      <li>Pro uložení více pojmenovaných polí v jednom binárním souboru</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> <code>.npz</code> je archiv obsahující více pojmenovaných NumPy polí. Ukládáš přes <code>np.savez("data.npz", x=cas, y=signal)</code> a přístup pak vypadá jako u slovníku: <code>d = np.load("data.npz"); d["x"]</code>. Pro jediné pole stačí <code>.npy</code>.

</details>

---

### Část D: Matplotlib

18. **Který přístup je doporučovaný pro tvorbu více grafů a přesnou kontrolu?**
    <ol type="a">
      <li>Globální funkce <code>plt.plot()</code>, <code>plt.title()</code>…</li>
      <li>Přímá práce s objekty: <code>fig, ax = plt.subplots()</code> a pak metody <code>ax.plot()</code>, <code>ax.set_title()</code></li>
      <li>Použít místo Matplotlibu knihovnu <code>print()</code></li>
      <li>Vždy <code>plt.figure()</code> bez <code>subplots</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Objektově orientovaný přístup (<code>fig, ax = plt.subplots()</code>) je přehlednější, lépe se škáluje na víc grafů a dává plnou kontrolu nad každou osou zvlášť. Globální <code>plt.plot()</code> stačí jen pro jednoduché jednorázové grafy.

</details>

19. **K čemu slouží funkce `ax.imshow()`?**
    <ol type="a">
      <li>K vykreslení spojnicového grafu</li>
      <li>K uložení grafu do souboru</li>
      <li>K zobrazení 2D pole jako obrázku nebo heatmapy (každá hodnota je pixel)</li>
      <li>K vykreslení histogramu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>imshow</code> zobrazí 2D NumPy pole jako obrázek — každý prvek pole odpovídá pixelu. Hodí se pro medicínské snímky (MRI, CT), korelační matice nebo segmentační masky. Barvy řídíš přes <code>cmap=</code> (např. <code>"gray"</code>, <code>"viridis"</code>).

</details>

20. **Který typ grafu je nejvhodnější pro srovnání rozložení tepové frekvence mezi skupinou v klidu a při zátěži?**
    <ol type="a">
      <li>Boxplot (<code>boxplot</code>) — ukáže medián, kvartily a outliers obou skupin</li>
      <li>Výsečový graf (<code>pie</code>)</li>
      <li>Spojnicový graf (<code>plot</code>)</li>
      <li><code>imshow</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Boxplot je standard pro srovnání rozložení hodnot napříč několika skupinami — ukazuje medián, kvartily, vousy a odlehlé hodnoty. Pro srovnání dvou nebo víc kategorií dat (klid vs. zátěž) je ideální.

</details>

21. **Co dělá `plt.subplots(2, 1, sharex=True)`?**
    <ol type="a">
      <li>Vytvoří dva grafy vedle sebe</li>
      <li>Vytvoří jeden graf rozdělený na dvě poloviny</li>
      <li>Sloučí dva existující grafy do jednoho</li>
      <li>Vytvoří dva grafy pod sebou se sdílenou osou X</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>d.</b> První argument je počet řádků, druhý počet sloupců → <code>(2, 1)</code> jsou dva grafy pod sebou. <code>sharex=True</code> propojí jejich osu X — ideální pro srovnání více signálů s společným časem (EKG + dech, EKG + tlak…).

</details>

---

### Část E: Úkoly EKG a segmentace

22. **V úkolu EKG použijeme `np.diff(nad_prahem.astype(int)) == -1`. Co tato podmínka detekuje?**
    <ol type="a">
      <li>Náběžnou hranu (přechod z hodnoty pod prahem na hodnotu nad prahem)</li>
      <li>Sestupnou hranu (přechod z hodnoty nad prahem zpět pod prah, tj. konec R-vlny)</li>
      <li>Přesný vrchol R-vlny — bod, kde je první derivace nulová</li>
      <li>Šum v signálu</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>b.</b> Po převedení masky na 0/1 znamená rozdíl <code>-1</code> přechod z <code>1</code> (nad prahem) na <code>0</code> (pod prahem) — tedy sestupnou hranu, kde R-vlna končí. Tím se z každé skupiny <code>True</code> hodnot vybere přesně jeden bod a vyhneš se vícenásobným detekcím téhož úderu.

</details>

23. **Jak se spočítá tepová frekvence v BPM z časů R-vrcholů `cas_vrcholu`?**
    <ol type="a">
      <li><code>tf = len(cas_vrcholu) * 60</code></li>
      <li><code>tf = cas_vrcholu.mean() / 60</code></li>
      <li><code>tf = 60 / np.diff(cas_vrcholu).mean()</code></li>
      <li><code>tf = np.diff(cas_vrcholu).sum()</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>np.diff(cas_vrcholu)</code> vrátí R-R intervaly v sekundách. Průměrný R-R interval (v sekundách na úder) převedeš na BPM (úderů za minutu) vydělením 60: jeden úder za T sekund znamená 60/T úderů za minutu.

</details>

24. **V úkolu segmentace načítáš PNG snímky přes `plt.imread("skupina_a/snimek_00.png")`. Jaký objekt dostaneš?**
    <ol type="a">
      <li>2D NumPy pole intenzit tvaru <code>(64, 64)</code> s hodnotami 0–1</li>
      <li>Cestu k souboru jako řetězec</li>
      <li>Otevřený soubor, který musíš ručně zavřít</li>
      <li>Slovník s metadaty obrázku</li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>a.</b> Pro snímky v odstínech šedi vrátí <code>plt.imread</code> přímo 2D NumPy pole intenzit (typicky <code>float</code> od 0 do 1). Můžeš na něj rovnou aplikovat NumPy operace — boolean indexing, prahování, výpočet průměru atd.

</details>

25. **Jak v úkolu segmentace spočítáš poměrnou plochu pixelů nad prahem (v procentech) z masky `maska = snimek > PRAH`?**
    <ol type="a">
      <li><code>podil = maska.mean()</code></li>
      <li><code>podil = maska.size / maska.sum()</code></li>
      <li><code>podil = 100 * maska.sum() / maska.size</code></li>
      <li><code>podil = len(maska)</code></li>
   </ol>

<details class="answer-details">
<summary>Zobrazit správnou odpověď</summary>

<b>c.</b> <code>maska.sum()</code> sečte <code>True</code> hodnoty (každá se počítá jako 1) — počet pixelů ve struktuře. <code>maska.size</code> je celkový počet pixelů. Podíl × 100 dává procenta. Šlo by i <code>100 * maska.mean()</code>, protože průměr 0/1 hodnot je rovněž podíl jedniček.

</details>

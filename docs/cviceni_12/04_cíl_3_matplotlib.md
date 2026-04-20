# CÍL 3: MATPLOTLIB

> Táto stránka byla nahrazena interaktivním Jupyter Notebookem.
> Viz navigace → **Cíl 3 – Matplotlib**.


### 3.1 Základní struktura matplotlib

Matplotlib je nejrozšířenější vizualizační knihovna pro Python. Skoro každý vědecký graf, který jsi viděl v Pythonu, byl nejspíš vytvořen právě v ní.

Dvě vrstvy rozhraní:

- **`plt.plot()`** – rychlé volání globálních funkcí, dobré pro jeden jednoduchý graf,
- **`fig, ax = plt.subplots()`** – přímá práce s objekty Figure a Axes, doporučovaný přístup jakmile máš víc grafů nebo chceš přesnější kontrolu.

Budeme používat druhý přístup – je přehlednější a lépe se škáluje:

```python
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4))   # fig = celé okno, ax = jeden graf
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])      # data
ax.set_title("Můj první graf")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("Amplituda")
ax.grid(True)
plt.tight_layout()
plt.show()
```

---

### 3.2 Vykreslení signálu

Spojnicový graf je základní vizualizace pro časové řady – EKG, dech, tlak, teplotu:

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulace EKG – Gaussovy pulzy + šum
t = np.linspace(0, 2, 1000)   # 2 sekundy, 1000 vzorků (500 Hz)
ekg = (
    np.exp(-((t - 0.5) ** 2) / 0.001) * 1.5
    + np.exp(-((t - 1.2) ** 2) / 0.001) * 1.5
    + np.sin(2 * np.pi * 1.2 * t) * 0.1
    + np.random.normal(0, 0.04, len(t))
)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(t, ekg, color="steelblue", linewidth=0.8, label="EKG")
ax.axhline(ekg.mean(), color="tomato", linestyle="--", linewidth=1, label="průměr")
ax.set_title("Simulované EKG (2 s, 500 Hz)")
ax.set_xlabel("Čas (s)")
ax.set_ylabel("Amplituda (mV)")
ax.legend()
ax.grid(True, alpha=0.4)
plt.tight_layout()
plt.show()
```

Více grafů pod sebou – srovnání více signálů:

```python
resp = np.sin(2 * np.pi * 0.3 * t) + np.random.normal(0, 0.05, len(t))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5), sharex=True)

ax1.plot(t, ekg, color="steelblue", linewidth=0.8)
ax1.set_ylabel("EKG (mV)")
ax1.grid(True, alpha=0.4)

ax2.plot(t, resp, color="seagreen", linewidth=1)
ax2.set_ylabel("Respirace")
ax2.set_xlabel("Čas (s)")
ax2.grid(True, alpha=0.4)

fig.suptitle("Pacientský záznam")
plt.tight_layout()
plt.show()
```

---

### 3.3 Zobrazení matice / obrazu

`imshow()` zobrazí 2D numpy pole jako obrázek nebo heatmapu – každá hodnota odpovídá barvě pixelu. Hodí se pro:

- medicínské snímky (MRI, CT, histologie),
- korelační matice,
- síťové váhy v neuronových sítích.

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulace jednoduché MRI-like matice (64×64 pixelů)
x = np.linspace(-3, 3, 64)
y = np.linspace(-3, 3, 64)
X, Y = np.meshgrid(x, y)

# Gaussův profil jako model průřezu tkáně
image = np.exp(-(X**2 + Y**2) / 2)
# Přidáme drobné struktury (simulace heterogenní tkáně)
image += 0.3 * np.exp(-((X - 1)**2 + (Y + 1)**2) / 0.3)
image += 0.2 * np.exp(-((X + 1.5)**2 + (Y - 0.5)**2) / 0.5)
image += np.random.normal(0, 0.03, image.shape)

fig, axes = plt.subplots(1, 3, figsize=(13, 4))

# Různé barevné palety (colormaps)
cmaps = ["gray", "viridis", "hot"]
titles = ["Stupně šedi (gray)", "Viridis", "Hot"]

for ax, cmap, title in zip(axes, cmaps, titles):
    im = ax.imshow(image, cmap=cmap, origin="lower")
    ax.set_title(title)
    ax.axis("off")
    fig.colorbar(im, ax=ax, fraction=0.046)

fig.suptitle("Simulovaný MRI průřez – různé colormaps")
plt.tight_layout()
plt.show()
```

> **💡 Tip:** Pro medicínské obrazy se nejčastěji používá `cmap="gray"`. `viridis` je dobrou volbou pro vědecké heatmapy – je perceptuálně uniformní (stejné rozdíly v datech odpovídají stejně vnímaným rozdílům v barvě) a čitelná i při výtisku nebo pro barvoslepé.

---

### 3.4 Boxplot – statistické srovnání skupin

Boxplot je ideální, když chceš srovnat rozložení hodnot napříč skupinami – například různé pacienty, různé podmínky měření, různé skupiny.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulace tepové frekvence: klid, lehká zátěž, střední zátěž, maximální zátěž
groups = {
    "Klid":       np.random.normal(70, 8,  30),
    "Chůze":      np.random.normal(95, 10, 30),
    "Běh":        np.random.normal(140, 12, 30),
    "Sprint":     np.random.normal(175, 8,  30),
}
labels = list(groups.keys())
data   = list(groups.values())

fig, ax = plt.subplots(figsize=(9, 5))

bp = ax.boxplot(data, labels=labels, patch_artist=True, notch=False)

colors = ["#90caf9", "#a5d6a7", "#ffcc80", "#ef9a9a"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

ax.set_title("Tepová frekvence při různé zátěži")
ax.set_ylabel("Tepová frekvence (BPM)")
ax.yaxis.grid(True, linestyle="--", alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()
```

Boxplot ukazuje:

- **střední čára** = medián,
- **hranice boxu** = 1. a 3. kvartil (IQR),
- **vousy** = 1.5× IQR od kvartilů,
- **body za vousy** = odlehlé hodnoty (outliers).

---

### 3.5 Histogram – rozložení hodnot

Histogram ukazuje, jak jsou hodnoty rozloženy. Hodí se pro první pohled na data – je rozložení symetrické? Má outliers? Odpovídá normálnímu rozložení?

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

# Glykémie: zdravá populace vs. diabetici
zdravi    = np.random.normal(5.2, 0.5, 200)   # mmol/l
diabetici = np.random.normal(9.1, 1.8, 200)

fig, ax = plt.subplots(figsize=(9, 4))

ax.hist(zdravi,    bins=30, alpha=0.6, color="steelblue", label="Zdravá populace")
ax.hist(diabetici, bins=30, alpha=0.6, color="tomato",    label="Diabetici")
ax.axvline(7.0, color="black", linestyle="--", linewidth=1.5, label="Diagnostická mez 7.0 mmol/l")

ax.set_title("Glykémie nalačno – srovnání skupin")
ax.set_xlabel("Glykémie (mmol/l)")
ax.set_ylabel("Počet pacientů")
ax.legend()
plt.tight_layout()
plt.show()
```

---

**📝 ÚKOL: Vizualizace v notebooku**

Pokračuj v notebooku `cviceni_12_numpy.ipynb`. Přidej nové buňky:

1. Vygeneruj sinusový signál délky 3 sekundy, vzorkovací frekvence 200 Hz, frekvence 2 Hz. Přidej Gaussův šum (std = 0.15). Vykresli ho jako spojnicový graf s popsanými osami a nadpisem.

2. Vytvoř 2D numpy pole (50 × 50) obsahující vzdálenosti každého bodu od středu – `dist[i, j] = sqrt((i-25)^2 + (j-25)^2)`. Zobraz ho pomocí `imshow()` s colorbar a colormap `plasma`.

3. Vygeneruj data pro 4 skupiny pacientů – hodnoty krevního tlaku (systolický) pro skupiny: mladí zdraví, starší zdraví, mladí s hypertenzí, starší s hypertenzí. Vykresli boxplot srovnávající všechny 4 skupiny. Přidej vodorovnou čáru na hodnotě 140 (diagnostická mez hypertenze).

4. Přidej markdownovou buňku s krátkým komentářem ke každému grafu – co zobrazuje a co z něj lze vyčíst.

---


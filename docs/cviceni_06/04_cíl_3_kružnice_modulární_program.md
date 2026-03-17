# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## CÍL 3: 📝 ÚKOL – MODULÁRNÍ PROGRAM: PRŮNIK KRUŽNIC

<div class="fmt-task-block" markdown="1">

V tomhle cíli spojíš funkce a moduly do menšího projektu.
Výsledek bude přehledný program rozdělený do logických částí.

---

### 3.1 Co bude výstup programu

Cílem je napsat program, který určí, jestli se dvě kružnice protínají, a pokud ano, kolik mají průniků (dva, jeden nebo žádný).

Program bude provádět následující:

- zjistí, jestli se kružnice protínají,
- vrátí výsledek jako slovník (např. `{"intersects": True, "intersections_count": 2}`),
- vypíše stručný textový výstup do terminálu (např. „Kružnice se protínají a mají 2 průniky“),
- vykreslí obě kružnice v grafu.

---

### 3.2 Matematický základ

Kružnice je definovaná středem a poloměrem:

\[
k:\ S = (x, y),\ r
\]

\[
x, y \in \mathbb{R},\quad r > 0
\]

Pro dvě kružnice pak:

\[
k_1:\ S_1 = (x_1, y_1),\ r_1
\]

\[
k_2:\ S_2 = (x_2, y_2),\ r_2
\]

Kružnice \(k_1\) je tedy definovaná středem \((x_1, y_1)\) a poloměrem \(r_1\).
Kružnice \(k_2\) je definovaná středem \((x_2, y_2)\) a poloměrem \(r_2\).

**Nejdřív spočítej dvě klíčové hodnoty:**

Vzdálenost středů:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Součet poloměrů:

\[
r_s = r_1 + r_2
\]

**Rozhodnutí o průniku:**

\[
\begin{aligned}
d &> r_s &\Rightarrow&\ 0\ \text{průniků} \\
d &= r_s &\Rightarrow&\ 1\ \text{průnik (dotyk)} \\
d &< r_s &\Rightarrow&\ 2\ \text{průniky}
\end{aligned}
\]

---

### 3.3 Doporučený postup implementace

Kružnice budeš reprezentovat jako slovník s klíči `x`, `y` a `r`:

```python
circle_1 = {"x": x1, "y": y1, "r": r1}
circle_2 = {"x": x2, "y": y2, "r": r2}
```

Konkrétní příklad s čísly:

```python
circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}
```

1. Nejprve vytvoř funkce pro výpočty (součet poloměrů, Euklidovská vzdálenost).
2. Napiš funkci, která rozhodne o průniku na základě těchto výpočtů.
3. Ověř funkce přes několik testovacích volání a výpisů.
4. Následně napiš hlavní skript s výpisem.
5. Nakonec přidej vykreslení.

> **Tip:** Debuguj vždy po kouscích. Nečekej, až bude celý program hotový, ale testuj každou funkci zvlášť, abys měl 
> jistotu, že funguje správně.

---

### 3.4 Modul `circles_stats.py`

Vytvoř modul `circles_stats.py` a v něm tyto funkce:

1. `radius_sum(r1, r2)` - vrátí součet poloměrů.
2. `euclid_distance(x1, y1, x2, y2)` - vrátí Euklidovskou vzdálenost mezi dvěma body.
3. `has_intersection(circle_1, circle_2)` - vrátí slovník s informací o průniku
   (např. `{"intersects": ..., "intersections_count": ...}`).

> **⚠️ Pozor:** U desetinných čísel neporovnávej hraniční případ přes ostré `==`.
> Využij toleranci (např. přes `isclose(...)` z Python modulu `math`), aby program správně rozpoznal dotyk dvou 
> kružnic v jednom bodě.

---

### 3.5 Hlavní skript programu

Vytvoř `circles_intersection.py`, ve kterém:

1. Naimportuješ funkci `has_intersection` z modulu `circles_stats`.
2. Definuješ dvě kružnice jako slovníky s konkrétními hodnotami.
3. Zavoláš funkci pro zjištění průniku.
4. Podle výsledku vypíšeš, jestli se kružnice protínají a kolik mají průniků.

---

### 3.6 Modul `circles_intersection_draw.py`

Vytvoř modul `circles_intersection_draw.py` s funkcí `draw_data(...)`:

- Tato funkce bude přijímat dva parametry: `circle_1` a `circle_2` (stejně jako v `has_intersection(...)`).
- Funkce vykreslí obě kružnice do grafu pomocí knihovny `matplotlib`.

Instalace knihovny pro vykreslení:

```powershell
uv add matplotlib
```

Nejjednodušší ukázka vykreslení jedné kružnice:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # připravení okna pro vykreslení

circle = plt.Circle((0, 0), 2, fill=False, color="blue")  # vytvoření kružnice
ax.add_patch(circle)  # přidání kružnice do okna

ax.set_xlim(-5, 5) # nastavení rozsahu os, aby bylo vidět celý graf
ax.set_ylim(-5, 5)

ax.set_aspect("equal")  # nastavení stejného poměru os, aby kružnice vypadala jako kruh
plt.show()  # zobrazení okna s kružnicí
```

---

### 3.7 Vnitřní poloha kružnic (volitelně)

V základní verzi řešíš hlavně případy podle porovnání \(d\) a \(r_1 + r_2\). Nicméně, existuje i další situace,
kdy se kružnice „neprotínají“, ale jedna je celá uvnitř druhé. 
To nastane, když je vzdálenost středů \(d\) menší než absolutní hodnota rozdílu poloměrů \(|r_1 - r_2|\).

Rozšiř funkci `has_intersection(...)` tak, aby správně řešila i vnitřní případy:

- když \(d < |r_1 - r_2|\), kružnice se neprotínají (jedna je uvnitř druhé),
- když \(d = |r_1 - r_2|\), mají jeden průnik (dotyk),
- když \(|r_1 - r_2| < d < r_1 + r_2\), mají dva průniky.

---

</div>

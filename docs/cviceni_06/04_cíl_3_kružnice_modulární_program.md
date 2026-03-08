# CVIČENÍ 6: FUNKCE, MODULY A TESTY

Algoritmizace a programování

## CÍL 3: 📝 ÚKOL – MODULÁRNÍ PROGRAM: PRŮNIK KRUŽNIC

<div class="fmt-task-block" markdown="1">

V tomhle cíli spojíš funkce a moduly do menšího projektu.
Výsledek bude přehledný program rozdělený do logických částí.

---

### 3.1 Co bude výstup programu

Pro dvě kružnice chceš určit:

- jestli se protínají,
- kolik mají průniků (0/1/2),
- výsledek vracet jako slovník,
- a zároveň připravit stručný textový výstup do terminálu.
- vykreslení kružnic v grafu.

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

**Nejdřív spočti:**

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

Reprezentace kružnic v kódu:

```python
circle_1 = {"x": x1, "y": y1, "r": r1}
circle_2 = {"x": x2, "y": y2, "r": r2}
```

Konkrétní příklad s čísly:

```python
circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}
```

1. Napiš nejdřív čisté výpočtové funkce (`radius_sum`, `euclid_distance`).
2. Napiš rozhodovací funkci `has_intersection(...)`.
3. Ověř funkce přes několik testovacích volání a výpisů.
4. Teprve potom napiš hlavní skript s výpisem.
5. Nakonec přidej vykreslení.

> **💡 Tip:** Když něco nefunguje, debuguj vždy nejdřív malé funkce, ne celý program najednou.

---

### 3.4 Modul `circle_stats.py`

V modulu vytvoř tyto funkce:

1. `radius_sum(r1, r2)` -> vrátí součet poloměrů.
2. `euclid_distance(x1, y1, x2, y2)` -> vrátí Euklidovskou vzdálenost.
3. `has_intersection(circle_1, circle_2, tolerance=...)` -> vrátí slovník s výsledkem
   (např. `{"is_intersection": ..., "intersections_count": ...}`).

> **⚠️ Pozor:** U desetinných čísel neporovnávej hraniční případ přes ostré `==`.
> Využij toleranci (např. přes `isclose(...)`), aby dotyk fungoval spolehlivě.

---

### 3.5 Hlavní skript programu

Vytvoř `circle_intersection.py`, ve kterém:

1. Naimportuješ `has_intersection`.
2. Definuješ dvě kružnice jako slovníky (`x`, `y`, `r`).
3. Zavoláš funkci a výsledek načteš ze slovníku (`result["is_intersection"]`, `result["intersections_count"]`).
4. Vypíšeš výsledek uživatelsky srozumitelně.

---

### 3.6 Vykreslení kružnic

Vytvoř soubor `circles_intersection_draw.py` s funkcí `draw_data(...)`.

Instalace:

```powershell
uv add matplotlib
```

Nejjednodušší ukázka vykreslení jedné kružnice:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # připravení okna pro vykreslení

circle = plt.Circle((0, 0), 2, fill=False, color="blue")  # vytvoření kružnice
ax.add_patch(circle)  # přidání kružnice do okna

ax.set_aspect("equal")  # nastavení stejného poměru os, aby kružnice vypadala jako kruh
plt.show()  # zobrazení okna s kružnicí
```

---

### 3.7 Vnitřní poloha kružnic (volitelně)

V základní verzi řešíš hlavně případy podle porovnání \(d\) a \(r_1 + r_2\).
Ještě existuje situace, kdy je jedna kružnice celá uvnitř druhé.
Tam je potřeba navíc sledovat i rozdíl poloměrů \(|r_1 - r_2|\).

Rozšiř funkci `has_intersection(...)` tak, aby správně řešila i vnitřní případy:

- když \(d < |r_1 - r_2|\), kružnice se neprotínají (jedna je uvnitř druhé),
- když \(d = |r_1 - r_2|\), mají jeden vnitřní dotyk,
- když \(|r_1 - r_2| < d < r_1 + r_2\), mají dva průniky.

---

</div>

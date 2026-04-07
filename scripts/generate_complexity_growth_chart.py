from math import sqrt
from math import factorial, log2
from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_PATH = Path("docs/assets/cviceni_10/complexity_growth.png")


def generate_chart() -> None:
    moderate_ns = list(range(1, 101))
    line_styles = {
        "O(1)": "solid",
        "O(log n)": "dashed",
        "O(sqrt(n))": "dotted",
        "O(n)": "dashdot",
        "O(n log n)": (0, (5, 1)),
        "O(n^2)": (0, (3, 1, 1, 1)),
        "O(n^3)": (0, (7, 2)),
        "O(2^n)": (0, (1, 1)),
        "O(n!)": (0, (10, 2, 2, 2)),
    }

    all_series = {
        "O(1)": [1 for n in moderate_ns],
        "O(log n)": [log2(n) for n in moderate_ns],
        "O(sqrt(n))": [sqrt(n) for n in moderate_ns],
        "O(n)": [n for n in moderate_ns],
        "O(n log n)": [n * log2(n) for n in moderate_ns],
        "O(n^2)": [n**2 for n in moderate_ns],
        "O(n^3)": [n**3 for n in moderate_ns],
        "O(2^n)": [2**n for n in moderate_ns],
        "O(n!)": [factorial(n) if n <= 12 else None for n in moderate_ns],
    }

    plt.style.use("seaborn-v0_8-whitegrid")
    figure, main_axis = plt.subplots(figsize=(12.5, 6.5), constrained_layout=True)

    for label, values in all_series.items():
        xs = [n for n, value in zip(moderate_ns, values) if value is not None]
        ys = [value for value in values if value is not None]
        main_axis.plot(xs, ys, label=label, linewidth=2.2, linestyle=line_styles[label])

    main_axis.set_title("Porovnání typických tříd složitosti")
    main_axis.set_xlabel("Velikost vstupu n")
    main_axis.set_ylabel("Relativní počet kroků")
    main_axis.set_xlim(1, 100)
    main_axis.set_ylim(0, 200)
    main_axis.legend(ncol=2)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT_PATH, dpi=160, bbox_inches="tight")


if __name__ == "__main__":
    generate_chart()
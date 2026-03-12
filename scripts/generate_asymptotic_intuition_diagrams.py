from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


ASSET_DIR = Path(__file__).resolve().parents[1] / "docs" / "assets" / "cviceni_10"
CONSTANT_PATH = ASSET_DIR / "asymptotic_constant_intuition.png"
LINEAR_PATH = ASSET_DIR / "asymptotic_linear_intuition.png"

PRIMARY = "#0f4c5c"
ACCENT = "#d1495b"
SOFT = "#efe8d8"
TEXT = "#1f2933"
MUTED = "#6b7280"
BG = "#fffdf8"

plt.rcParams["font.family"] = ["Segoe UI", "DejaVu Sans", "sans-serif"]


def draw_cells(ax, values, highlight_index=None, start_x=0.8, y=0.9, width=0.95, height=0.8, fontsize=16):
    centers = []
    for index, value in enumerate(values):
        x = start_x + index * (width + 0.12)
        facecolor = SOFT
        edgecolor = PRIMARY
        linewidth = 2.0
        if highlight_index == index:
            facecolor = ACCENT
            edgecolor = ACCENT
            linewidth = 2.4

        ax.add_patch(
            Rectangle(
                (x, y),
                width,
                height,
                facecolor=facecolor,
                edgecolor=edgecolor,
                linewidth=linewidth,
                joinstyle="round",
            )
        )
        ax.text(
            x + width / 2,
            y + height / 2,
            str(value),
            ha="center",
            va="center",
            fontsize=fontsize,
            color="white" if highlight_index == index else TEXT,
            weight="bold" if highlight_index == index else "normal",
        )
        centers.append((x + width / 2, y + height / 2))
    return centers


def setup_figure(width, height):
    fig, ax = plt.subplots(figsize=(width, height), dpi=180)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    return fig, ax


def save_constant_diagram():
    values = [8, 3, 1, 5, 1, 0, 3, 2, 5, 6]
    fig, ax = setup_figure(12, 3.8)
    centers = draw_cells(ax, values, highlight_index=0, y=1.05)

    ax.text(0.8, 3.0, "Konstantní složitost: vždy čteš stejnou pozici", fontsize=20, weight="bold", color=TEXT)
    ax.text(0.8, 2.55, "Například první prvek seznamu. Počet kroků se s délkou seznamu nemění.", fontsize=12.5, color=MUTED)
    ax.text(0.8, 0.35, "základní operace: values[0]", fontsize=13, color=PRIMARY, weight="bold")

    arrow = FancyArrowPatch(
        posA=(centers[0][0], 2.25),
        posB=(centers[0][0], 1.92),
        arrowstyle="simple",
        mutation_scale=18,
        color=ACCENT,
    )
    ax.add_patch(arrow)
    ax.text(centers[0][0] + 0.25, 2.05, "čtu právě tenhle prvek", fontsize=12, color=ACCENT, weight="bold")

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.4)
    fig.tight_layout(pad=0.5)
    fig.savefig(CONSTANT_PATH, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def save_linear_diagram():
    fig = plt.figure(figsize=(14, 7), dpi=180)
    fig.patch.set_facecolor(BG)
    grid = fig.add_gridspec(1, 2, width_ratios=[1.35, 1], wspace=0.14)
    ax_left = fig.add_subplot(grid[0, 0])
    ax_right = fig.add_subplot(grid[0, 1])

    for axis in (ax_left, ax_right):
        axis.set_facecolor(BG)

    ax_left.axis("off")
    ax_left.text(0.0, 0.96, "Lineární složitost: čím delší seznam, tím víc porovnání", fontsize=19, weight="bold", color=TEXT, transform=ax_left.transAxes)
    ax_left.text(0.0, 0.90, "V nejhorším případě projdeš celý seznam. Proto pro délky 3, 5 a 10 dostaneš právě 3, 5 a 10 porovnání.", fontsize=12, color=MUTED, transform=ax_left.transAxes)
    ax_left.text(0.0, 0.05, "základní operace: values[i] == 8", fontsize=12.5, color=PRIMARY, weight="bold", transform=ax_left.transAxes)

    examples = [
        (3, [2, 4, 8], 2, 4.6),
        (5, [1, 3, 5, 7, 8], 4, 3.2),
        (10, [3, 1, 5, 1, 0, 4, 9, 7, 2, 8], 9, 1.8),
    ]

    plot_points = []
    for length, values, highlight_index, y in examples:
        ax_left.text(0.15, y + 0.62, f"délka {length}", fontsize=12.5, color=PRIMARY, weight="bold")
        centers = draw_cells(ax_left, values, highlight_index=highlight_index, start_x=1.05, y=y, width=0.55, height=0.5, fontsize=10.5)

        for index in range(highlight_index):
            ax_left.add_patch(
                FancyArrowPatch(
                    posA=(centers[index][0], y + 0.78),
                    posB=(centers[index][0], y + 0.56),
                    arrowstyle="-|>",
                    mutation_scale=9,
                    linewidth=1.3,
                    color=PRIMARY,
                )
            )

        ax_left.add_patch(
            FancyArrowPatch(
                posA=(centers[highlight_index][0], y + 0.82),
                posB=(centers[highlight_index][0], y + 0.56),
                arrowstyle="simple",
                mutation_scale=13,
                color=ACCENT,
            )
        )
        ax_left.text(centers[-1][0] + 0.45, y + 0.14, f"{length} porovnání", fontsize=11.5, color=ACCENT, weight="bold")
        plot_points.append((length, length))

    ax_left.set_xlim(0, 8.2)
    ax_left.set_ylim(0.4, 5.5)

    ax_right.spines[["top", "right"]].set_visible(False)
    ax_right.spines[["left", "bottom"]].set_color(TEXT)
    ax_right.spines[["left", "bottom"]].set_linewidth(1.6)
    ax_right.set_xlim(0, 10.8)
    ax_right.set_ylim(0, 10.8)
    ax_right.set_xticks([3, 5, 10])
    ax_right.set_yticks([3, 5, 10])
    ax_right.tick_params(labelsize=10.5, colors=TEXT)
    ax_right.set_xlabel("délka seznamu n", fontsize=11.5, color=TEXT, labelpad=8)
    ax_right.set_ylabel("počet porovnání", fontsize=11.5, color=TEXT, labelpad=8)
    ax_right.set_title("Body, které vytvářejí lineární graf", fontsize=13, color=PRIMARY, pad=12, weight="bold")

    x_values = [point[0] for point in plot_points]
    y_values = [point[1] for point in plot_points]
    ax_right.plot(x_values, y_values, color=ACCENT, linewidth=2.5)
    ax_right.scatter(x_values, y_values, color=ACCENT, s=44, zorder=3)

    for x_value, y_value in plot_points:
        ax_right.text(x_value + 0.18, y_value + 0.22, f"({x_value}, {y_value})", fontsize=10.5, color=ACCENT)

    fig.subplots_adjust(left=0.04, right=0.98, top=0.94, bottom=0.08, wspace=0.14)
    fig.savefig(LINEAR_PATH, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def main():
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    save_constant_diagram()
    save_linear_diagram()


if __name__ == "__main__":
    main()
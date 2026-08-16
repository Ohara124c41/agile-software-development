from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

INK = "#314251"
CYAN = "#00B5E5"
GOLD = "#E6B800"
SLATE = "#718096"
PALE = "#E9F3F7"


def burndown() -> None:
    days = np.arange(0, 11)
    ideal = np.linspace(40, 0, len(days))
    remaining = np.array([40, 37, 34, 32, 28, 25, 22, 17, 12, 7, 0])
    fig, ax = plt.subplots(figsize=(8.8, 4.9), dpi=200)
    fig.patch.set_facecolor("white")
    ax.plot(days, ideal, color="#A0AEC0", linewidth=2.2, linestyle="--", label="Ideal trend")
    ax.plot(days, remaining, color=CYAN, linewidth=3.8, marker="o", markersize=6.5, label="Remaining work")
    ax.fill_between(days, remaining, ideal, where=remaining >= ideal, color=GOLD, alpha=0.18)
    ax.annotate("On track", xy=(9, 7), xytext=(6.1, 14), color=INK, fontsize=10,
                arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.1})
    ax.set_title("Sprint Burndown | 40 story points", loc="left", color=INK, fontweight="bold", fontsize=15, pad=14)
    ax.set_xlabel("Sprint day", color=INK, fontsize=11)
    ax.set_ylabel("Story points remaining", color=INK, fontsize=11)
    ax.set_xlim(0, 10); ax.set_ylim(0, 44)
    ax.set_xticks(days); ax.set_yticks([0, 10, 20, 30, 40])
    ax.grid(axis="y", color="#D9E2E8", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#A0AEC0")
    ax.tick_params(colors=INK)
    ax.legend(frameon=False, loc="upper right", labelcolor=INK)
    fig.tight_layout()
    fig.savefig(OUT / "sprint_burndown.png", transparent=False, bbox_inches="tight")
    plt.close(fig)


def cumulative_flow() -> None:
    days = np.arange(0, 11)
    done = np.array([0, 1, 2, 4, 6, 8, 11, 14, 17, 20, 24])
    test = np.array([0, 1, 2, 3, 3, 4, 4, 3, 3, 3, 2])
    build = np.array([2, 3, 4, 4, 5, 4, 3, 3, 3, 2, 2])
    ready = np.array([10, 9, 8, 7, 5, 4, 3, 2, 1, 1, 0])
    fig, ax = plt.subplots(figsize=(8.8, 4.9), dpi=200)
    ax.stackplot(days, done, test, build, ready, labels=["Done", "Test", "Build", "Ready"],
                 colors=[CYAN, GOLD, SLATE, PALE], alpha=0.98)
    ax.axhline(8, color=INK, linewidth=1.2, linestyle="--")
    ax.text(0.15, 8.55, "Build + Test WIP limit", color=INK, fontsize=10, fontweight="bold")
    ax.annotate("Test queue narrows", xy=(8, 20), xytext=(5.1, 27), color=INK, fontsize=10,
                arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.1})
    ax.set_title("Cumulative Flow | work moves to Done", loc="left", color=INK, fontweight="bold", fontsize=15, pad=14)
    ax.set_xlabel("Sprint day", color=INK, fontsize=11)
    ax.set_ylabel("Work items", color=INK, fontsize=11)
    ax.set_xlim(0, 10); ax.set_ylim(0, 32)
    ax.set_xticks(days); ax.set_yticks([0, 8, 16, 24, 32])
    ax.grid(axis="y", color="#D9E2E8", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#A0AEC0")
    ax.tick_params(colors=INK)
    legend = ax.legend(frameon=False, loc="upper left", ncol=4, bbox_to_anchor=(0, 1.03))
    for text in legend.get_texts(): text.set_color(INK)
    fig.tight_layout()
    fig.savefig(OUT / "cumulative_flow.png", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    burndown()
    cumulative_flow()

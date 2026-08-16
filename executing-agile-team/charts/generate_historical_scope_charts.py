from pathlib import Path

import matplotlib.pyplot as plt


OUT = Path(__file__).parent / "historical-scope-charts"
OUT.mkdir(exist_ok=True)

SPRINTS = list(range(7))
REMAINING = [126, 106, 83, 61, 39, 21, 5]
CUMULATIVE = [0, 20, 43, 65, 87, 110, 131]
SCOPE = [126, 126, 126, 126, 126, 131, 136]
COMMITTED = [20, 23, 22, 22, 23, 21]
DELIVERED = [20, 23, 22, 22, 23, 21]

plt.rcParams.update({"font.family": "Arial", "font.size": 10})


def finish(ax, title, ymax=160):
    ax.set_title(title, weight="bold", pad=10)
    ax.set_xlabel("Sprint")
    ax.set_ylabel("Story Points")
    ax.set_xticks(SPRINTS)
    ax.set_ylim(0, ymax)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)


def burn_down(last_sprint, filename):
    fig, ax = plt.subplots(figsize=(8.7, 4.75), dpi=160)
    x = SPRINTS[: last_sprint + 1]
    y = REMAINING[: last_sprint + 1]
    ax.plot(x, y, color="#4472C4", marker="o", linewidth=2.5)
    for xi, yi in zip(x, y):
        ax.annotate(str(yi), (xi, yi), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=9)
    finish(ax, f"Burn Down Through Sprint {last_sprint}")
    ax.set_xticks(x)
    ax.set_xlim(-0.1, last_sprint + 0.1)
    fig.tight_layout()
    fig.savefig(OUT / filename, transparent=False, facecolor="white")
    plt.close(fig)


for sprint in (3, 4, 5, 6):
    burn_down(sprint, f"burn_down_through_sprint_{sprint}.png")

fig, ax = plt.subplots(figsize=(10.1, 4.9), dpi=160)
ax.plot(SPRINTS, REMAINING, color="#2E75B6", marker="o", linewidth=2.5, label="Remaining")
for x, y in zip(SPRINTS, REMAINING):
    ax.annotate(str(y), (x, y), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=9)
finish(ax, "Burn-Down: Remaining Story Points")
ax.legend(frameon=False, loc="lower center", ncol=1)
fig.tight_layout()
fig.savefig(OUT / "management_burn_down.png", facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(10.1, 4.9), dpi=160)
ax.plot(SPRINTS, CUMULATIVE, color="#2E75B6", marker="o", linewidth=2.5, label="Cumulative Delivered")
ax.plot(SPRINTS, SCOPE, color="#ED7D31", marker="o", linewidth=2.5, label="Total Scope")
finish(ax, "Burn-Up: Cumulative Delivered vs. Total Scope")
ax.legend(frameon=False, loc="lower center", ncol=2)
fig.tight_layout()
fig.savefig(OUT / "management_burn_up.png", facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(10.1, 4.9), dpi=160)
x = list(range(1, 7))
width = 0.35
ax.bar([i - width / 2 for i in x], COMMITTED, width, color="#ED7D31", label="Committed")
ax.bar([i + width / 2 for i in x], DELIVERED, width, color="#70AD47", label="Delivered")
ax.set_xticks(x)
ax.set_xlabel("Sprint")
ax.set_ylabel("Story Points")
ax.set_ylim(0, 26)
ax.set_title("Committed vs. Delivered Story Points", weight="bold", pad=10)
ax.grid(axis="y", color="#D9D9D9", linewidth=0.8)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(OUT / "committed_vs_delivered.png", facecolor="white")
plt.close(fig)

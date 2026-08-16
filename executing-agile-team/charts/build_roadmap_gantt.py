from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


OUT = Path(__file__).with_name("six-sprint-roadmap-gantt.png")


def main() -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(16, 9), dpi=180)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    work = [
        ("S1", "Core commerce", "Browse, cart, account", "20 points", "#2F6FAF"),
        ("S2", "Purchase flow", "Payment + offers", "23 points", "#2F6FAF"),
        ("S3", "Service tools", "Search + publishing", "22 points", "#2F6FAF"),
        ("S4", "Cyber Shield", "Security scan, Git + approval", "22 points", "#C88A18"),
        ("S5", "Customer\nFast Lane", "Responsive site", "23 points", "#287A56"),
        ("S6", "Flash Sale\nLaunch", "BOGO + launch prep", "21 points", "#B5434D"),
    ]

    # Timeline grid: six two-week sprints across a 12-week delivery window.
    for week in range(13):
        ax.axvline(week, ymin=0.14, ymax=0.83, color="#D9DEE7", lw=1, zorder=0)
    for y in range(7):
        ax.hlines(y, 0, 12, color="#D9DEE7", lw=1, zorder=0)

    for sprint in range(6):
        center = sprint * 2 + 1
        ax.text(center, 6.2, f"SPRINT {sprint + 1}", ha="center", va="bottom",
                fontsize=12, fontweight="bold", color="#25344D")
        ax.text(center, 5.92, f"Weeks {sprint * 2 + 1}-{sprint * 2 + 2}", ha="center", va="bottom",
                fontsize=9, color="#69758A")

    for row, (code, name, detail, points, color) in enumerate(work):
        y = 5 - row
        # Gantt bar: sharp rectangular edges and a restrained fill.
        ax.add_patch(Rectangle((row * 2, y + 0.12), 2, 0.76, facecolor=color,
                               edgecolor=color, linewidth=0, zorder=2))
        ax.text(-0.25, y + 0.50, code, ha="right", va="center", fontsize=12,
                fontweight="bold", color="#25344D")
        ax.text(row * 2 + 0.12, y + 0.64, name, ha="left", va="center", fontsize=10.2,
                fontweight="bold", color="white")
        ax.text(row * 2 + 0.12, y + 0.31, detail, ha="left", va="center", fontsize=7.8,
                color="white")
        ax.text(row * 2 + 1.88, y + 0.18, points, ha="right", va="center", fontsize=8.5,
                fontweight="bold", color="white")

    # End-of-roadmap release gate: a connected milestone, not a decorative arrow.
    ax.vlines(12, -0.2, 6.05, color="#172033", lw=2.2, zorder=3)
    ax.scatter(12, -0.20, marker="D", s=90, color="#172033", zorder=4)
    ax.text(12.18, -0.10, "MVP beta release gate", ha="left", va="bottom", fontsize=11,
            fontweight="bold", color="#172033")
    ax.text(12.18, -0.42, "10% automatic canary; 90% opt-in", ha="left", va="bottom", fontsize=9.5,
            color="#4E5B70")

    ax.text(0, 7.28, "The A-Team MVP Roadmap", fontsize=23, fontweight="bold", color="#172033")
    ax.text(0, 6.88, "Six two-week sprints | 12 weeks | value-based scope changes made visible",
            fontsize=11.5, color="#5E6B80")
    ax.text(0, -1.06,
            "Deferred after Sprint 6: one 5-point customer-review analysis story. The MVP scope prioritizes security, responsiveness, availability, and the BOGO request.",
            fontsize=10.5, color="#4E5B70")

    ax.set_xlim(-1.2, 16.2)
    ax.set_ylim(-1.35, 7.75)
    ax.axis("off")
    fig.subplots_adjust(left=0.06, right=0.97, top=0.92, bottom=0.12)
    fig.savefig(OUT, dpi=180, facecolor="#FFFFFF")
    print(OUT)


if __name__ == "__main__":
    main()

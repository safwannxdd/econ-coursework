import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def add_group_circle(ax, center, r, title, items, color,
                     title_pad=0.16, alpha=0.10):
    cx, cy = center

    ax.add_patch(
        Circle((cx, cy), r,
               linewidth=2.2,
               edgecolor=color,
               facecolor=color,
               alpha=alpha)
    )

    ax.text(
        cx, cy + r + title_pad,
        title,
        ha="center", va="bottom",
        fontsize=12.5,
        fontweight="semibold",
        color=color,
        linespacing=1.15
    )

    if items:
        text = "\n".join([f"• {it}" for it in items])
        ax.text(
            cx, cy,
            text,
            ha="center", va="center",
            fontsize=11.3,
            color="#1a1a1a",
            linespacing=1.25
        )

# ----------------------------
# Figure
# ----------------------------
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 160

fig, ax = plt.subplots(figsize=(13, 7.5))
ax.set_aspect("equal")
ax.axis("off")

PUBLIC  = "#2E7D32"
PRIVATE = "#1565C0"

R = 2.35
public_center  = (-3.0, 0.0)
private_center = ( 3.0, 0.0)

ax.add_patch(Circle(public_center,  R, linewidth=3, edgecolor=PUBLIC,  facecolor="none"))
ax.add_patch(Circle(private_center, R, linewidth=3, edgecolor=PRIVATE, facecolor="none"))

ax.text(public_center[0],  public_center[1] + R + 0.45, "PUBLIC",
        ha="center", va="bottom", fontsize=22, fontweight="bold", color=PUBLIC)
ax.text(private_center[0], private_center[1] + R + 0.45, "PRIVATE",
        ha="center", va="bottom", fontsize=22, fontweight="bold", color=PRIVATE)

ax.plot([0, 0], [-3.3, 3.3], color="#333", linewidth=2, alpha=0.15)

# ----------------------------
# PUBLIC (FIXED: push top group DOWN, and push affirmative-action DOWN too)
# ----------------------------

# Mainstream moved down (y: 1.0 -> 0.70)
add_group_circle(
    ax,
    center=(public_center[0] - 0.6, 0.70),
    r=0.78,
    title="Mainstream\nNational\nSchools",
    items=["SMK", "SMJK"],
    color=PUBLIC
)

# ✅ Affirmative-Action Schools moved DOWN + RIGHT (bottom-centre)
add_group_circle(
    ax,
    center=(public_center[0] - 0.3, -1.40),  # << moved here
    r=0.75,
    title="Affirmative-\nAction\nSchools",
    items=["SBP", "MRSM"],
    color=PUBLIC
)

# Public religious stays on right
add_group_circle(
    ax,
    center=(public_center[0] + 1.1, -0.15),
    r=0.55,
    title="Public\nReligious\nSchools",
    items=["SMKA", "Mission-based schools"],
    color=PUBLIC
)

# ----------------------------
# PRIVATE (same as your latest good layout)
# ----------------------------
ax.text(
    private_center[0] - 1.15, 1.35,
    "Private\nNational\nCurriculum\nSchools",
    ha="center", va="center",
    fontsize=12.5,
    fontweight="semibold",
    color=PRIVATE,
    linespacing=1.1
)

# International Schools — moved slightly toward centre
add_group_circle(
    ax,
    center=(private_center[0] - 0.45, -0.70),  # was -0.90, now closer to centre
    r=0.65,
    title="International\nSchools",
    items=["British Curriculum", "American Curriculum"],
    color=PRIVATE
)

add_group_circle(
    ax,
    center=(private_center[0] + 1.1, 0.65),
    r=0.70,
    title="Private\nReligious\nSchools",
    items=["Mission-based schools", "Tahfiz"],
    color=PRIVATE
)

ax.set_xlim(-6.8, 6.8)
ax.set_ylim(-3.6, 3.7)

plt.tight_layout()
plt.show()

# Optional save:
# plt.savefig("malaysia_education_layout_fixed_left.png", dpi=300, bbox_inches="tight")

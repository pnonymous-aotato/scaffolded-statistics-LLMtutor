"""
Generate a paired-change arrow plot showing individual T1->T3 trajectories
for each Likert item, faceted by course.

Design:
- Two panels: Course A (top), Course B (bottom)
- Within each panel: 11 rows (one per item, Q1-Q11)
- For each item: one arrow per student from T1 to T3
- Arrows slightly jittered vertically so overlapping students are visible
- Green arrows for improvement, red for decline, gray for unchanged
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

BASE = "./data/raw_canvas_exports"

LIKERT_MAP = {
    "Strongly Disagree": 1, "Strongly disagree": 1,
    "Disagree": 2, "disagree": 2,
    "Neutral": 3, "neutral": 3,
    "Neither Agree nor Disagree": 3, "Neither Agree Nor Disagree": 3,
    "Agree": 4, "agree": 4,
    "Strongly Agree": 5, "Strongly agree": 5, "strongly agree": 5,
    "": None,
}

ITEM_SHORT = [
    "Q1 Enhance", "Q2 CritThink", "Q3 Recall", "Q4 UserFriendly",
    "Q5 FdbkVsInst", "Q6 PromptsHelp", "Q7 Equity", "Q8 PrepLect",
    "Q9 UnderstEx", "Q10 ReduceExtRes", "Q11 AwareAI",
]

def load_likert(path):
    out = {}
    with open(path) as f:
        reader = csv.reader(f); next(reader)
        for row in reader:
            if not row or not row[0]: continue
            vals = [LIKERT_MAP.get(row[i].strip() if i < len(row) else "", None)
                    for i in range(2, 24, 2)]
            out[row[0]] = vals
    return out

t1_A = load_likert(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 2200.csv")
t3_A = load_likert(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 2200.csv")
t1_B = load_likert(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 4200.csv")
t3_B = load_likert(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 4200.csv")

def get_paired_data(t1_dict, t3_dict):
    """For each item (0-10), return list of (v1, v3, sid) for paired students."""
    common = sorted(set(t1_dict.keys()) & set(t3_dict.keys()))
    out = []
    for item_idx in range(11):
        item_data = []
        for sid in common:
            v1 = t1_dict[sid][item_idx]
            v3 = t3_dict[sid][item_idx]
            if v1 is not None and v3 is not None:
                item_data.append((v1, v3, sid))
        out.append(item_data)
    return out

data_A = get_paired_data(t1_A, t3_A)
data_B = get_paired_data(t1_B, t3_B)

# Generate figure
fig, (ax_A, ax_B) = plt.subplots(2, 1, figsize=(9, 10), sharex=True)

def plot_panel(ax, data, title):
    """Draw arrows for each item."""
    for item_idx in range(11):
        item_data = data[item_idx]
        # y-position for this item (lower = top of plot)
        y_base = 10 - item_idx  # Q1 at top (y=10), Q11 at bottom (y=0)
        n = len(item_data)
        # Jitter each arrow so overlaps visible
        if n > 0:
            jitters = np.linspace(-0.32, 0.32, n)
        for j, (v1, v3, sid) in enumerate(item_data):
            y = y_base + jitters[j] if n > 1 else y_base
            diff = v3 - v1
            if diff > 0:
                color = (0.1, 0.55, 0.2, 0.75)  # green
            elif diff < 0:
                color = (0.75, 0.15, 0.15, 0.75)  # red
            else:
                color = (0.55, 0.55, 0.55, 0.5)   # gray
            if diff == 0:
                # Draw a small dot for unchanged
                ax.plot(v1, y, 'o', color=color, markersize=4)
            else:
                arrow = FancyArrowPatch(
                    (v1, y), (v3, y),
                    arrowstyle='->', mutation_scale=9,
                    color=color, linewidth=1.1,
                )
                ax.add_patch(arrow)

    ax.set_yticks(range(11))
    ax.set_yticklabels(ITEM_SHORT[::-1], fontsize=8)
    ax.set_xlim(0.7, 5.3)
    ax.set_ylim(-0.6, 10.6)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(["SD\n(1)", "D\n(2)", "N\n(3)", "A\n(4)", "SA\n(5)"], fontsize=8)
    ax.set_title(title, fontsize=10, loc='left', pad=6)
    ax.grid(True, axis='x', linestyle=':', alpha=0.4, linewidth=0.5)
    ax.tick_params(axis='both', length=3)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    ax.set_axisbelow(True)

plot_panel(ax_A, data_A, "Course A — paired T1→T3 trajectories (n=13)")
plot_panel(ax_B, data_B, "Course B — paired T1→T3 trajectories (n=16)")

# Unified legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=(0.1,0.55,0.2), lw=1.5, label='Improvement (T3 > T1)'),
    Line2D([0], [0], color=(0.75,0.15,0.15), lw=1.5, label='Decline (T3 < T1)'),
    Line2D([0], [0], marker='o', color='none', markerfacecolor=(0.55,0.55,0.55),
           markersize=5, label='Unchanged (T3 = T1)'),
]
ax_A.legend(handles=legend_elements, loc='upper left',
            bbox_to_anchor=(0.0, -0.08), ncol=3, frameon=False, fontsize=8)

ax_B.set_xlabel("Likert response (1=Strongly Disagree, 5=Strongly Agree)", fontsize=9)

plt.tight_layout()
plt.savefig("./paper/figure5.pdf", bbox_inches='tight', dpi=200)
plt.savefig("./paper/figure5.png", bbox_inches='tight', dpi=200)
print("Saved figure5.pdf and figure5.png")

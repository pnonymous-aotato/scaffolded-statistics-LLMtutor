"""
Generate diverging stacked bar charts for Courses A and B in our visual style.
Color palette and typography match our Figure 5 (CONSORT) and Figure 6 (arrow plot).
Centered at Neutral midpoint per Robbins & Heiberger (2011) convention.
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

BASE = "./data/raw_canvas_exports"

LIKERT_MAP = {
    "Strongly Disagree": 1, "Strongly disagree": 1,
    "Disagree": 2, "disagree": 2,
    "Neutral": 3, "neutral": 3,
    "Agree": 4, "agree": 4,
    "Strongly Agree": 5, "Strongly agree": 5, "strongly agree": 5,
    "": None,
}

ITEM_LABELS = [
    ("Q1", "Enhanced learning"),
    ("Q2", "Encourages critical thinking"),
    ("Q3", "Recall/apply prior concepts"),
    ("Q4", "User-friendly & accessible"),
    ("Q5", "Feedback as helpful as instructor"),
    ("Q6", "Instructor prompts help use"),
    ("Q7", "Supports learning (equity)"),
    ("Q8", "Prepared before lecture"),
    ("Q9", "Understand lecture examples"),
    ("Q10", "Reduce need for other resources"),
    ("Q11", "Aware of university AI efforts"),
]

# Palette — same saturation family as our Fig 5 CONSORT diagram
# Darker cool = disagree, warmer = agree; neutral center = light gray
COLORS = {
    1: "#7a2828",   # Strongly Disagree — deep red
    2: "#c46b4a",   # Disagree — orange-red
    3: "#d9d9d9",   # Neutral — light gray
    4: "#4c8bc4",   # Agree — mid blue (matches our Course A blue #2E6FAB family)
    5: "#1f4e79",   # Strongly Agree — deep blue
}
LABEL_MAP = {1: "Strongly Disagree", 2: "Disagree", 3: "Neutral", 4: "Agree", 5: "Strongly Agree"}


def load_wave(path):
    """Return dict[sid] -> list of 11 ints (or None)."""
    out = {}
    with open(path) as f:
        reader = csv.reader(f); next(reader)
        for row in reader:
            if not row or not row[0]:
                continue
            vals = []
            for i in range(2, 24, 2):
                if i < len(row):
                    vals.append(LIKERT_MAP.get(row[i].strip(), None))
                else:
                    vals.append(None)
            out[row[0]] = vals
    return out


def proportions_per_wave(wave_dict):
    """Return {item_idx: {1: n, 2: n, 3: n, 4: n, 5: n, 'total': n}}."""
    result = {}
    for item_idx in range(11):
        counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        total = 0
        for sid, vals in wave_dict.items():
            v = vals[item_idx]
            if v is not None:
                counts[v] += 1
                total += 1
        result[item_idx] = {**counts, "total": total}
    return result


def draw_diverging_panel(ax, props_by_wave, course_label, n_by_wave):
    """
    Draw 11 items × 3 waves as diverging stacked bars.
    Each item gets 3 rows (T1 top, T2 middle, T3 bottom).
    Bars centered at Neutral's midpoint. Q1 rendered at top.
    """
    y_pos = 0
    item_label_ys = []
    all_y = []
    for item_idx in range(11):  # Q1 first, Q11 last — Q1 ends up at top after invert
        ys_for_item = []
        for wave in ["T1", "T2", "T3"]:
            props = props_by_wave[wave][item_idx]
            total = props["total"]
            if total == 0:
                y_pos += 1
                continue
            pct = {k: 100.0 * props[k] / total for k in [1, 2, 3, 4, 5]}
            left_edge = -(pct[1] + pct[2] + pct[3] / 2)
            ax.barh(y_pos, pct[1], left=left_edge, color=COLORS[1], height=0.7,
                    edgecolor='white', linewidth=0.3)
            left_edge += pct[1]
            ax.barh(y_pos, pct[2], left=left_edge, color=COLORS[2], height=0.7,
                    edgecolor='white', linewidth=0.3)
            left_edge += pct[2]
            ax.barh(y_pos, pct[3], left=left_edge, color=COLORS[3], height=0.7,
                    edgecolor='white', linewidth=0.3)
            left_edge += pct[3]
            ax.barh(y_pos, pct[4], left=left_edge, color=COLORS[4], height=0.7,
                    edgecolor='white', linewidth=0.3)
            left_edge += pct[4]
            ax.barh(y_pos, pct[5], left=left_edge, color=COLORS[5], height=0.7,
                    edgecolor='white', linewidth=0.3)
            ax.text(-108, y_pos, wave, va='center', ha='right', fontsize=7.5, color='#555555')
            ax.text(107, y_pos, f"n={total}", va='center', ha='left', fontsize=7.5, color='#555555')
            ys_for_item.append(y_pos)
            all_y.append(y_pos)
            y_pos += 1
        if ys_for_item:
            item_label_ys.append((np.mean(ys_for_item), item_idx))
        y_pos += 0.6

    # Left-side item labels — put them above the T1 row for each item, not centered
    for y_center, item_idx in item_label_ys:
        qcode, qname = ITEM_LABELS[item_idx]
        # Use the top (minimum) y position for this item — that's where T1 is
        # (we render T1 first so it has the smallest y value in the item's group)
        y_label = y_center - 1.2
        ax.text(-150, y_label, f"{qcode}: {qname}", va='center', ha='left',
                fontsize=9.5, color='#222222', fontweight='bold')

    ax.axvline(0, color='#666666', linewidth=0.7, zorder=5)
    ax.set_xlim(-100, 100)
    ax.set_xticks([-100, -50, 0, 50, 100])
    ax.set_xticklabels(["100%", "50%", "0", "50%", "100%"], fontsize=8)
    ax.set_ylim(-1.5, max(all_y) + 1)
    ax.set_yticks([])
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.invert_yaxis()
    ax.set_title(f"Course {course_label}: Likert response distributions by wave\n(diverging stacked, centered on Neutral midpoint)",
                 fontsize=11, loc='left', pad=10)
    from matplotlib.patches import Patch
    handles = [Patch(color=COLORS[k], label=LABEL_MAP[k]) for k in [1, 2, 3, 4, 5]]
    ax.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, -0.05),
              ncol=5, frameon=False, fontsize=8.5)


for course_key, course_name, ending in [("A", "A (Course A, Intro)", "2200"),
                                        ("B", "B (Course B, Advanced)", "4200")]:
    t1 = load_wave(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report {ending}.csv")
    t2 = load_wave(f"{BASE}/AI Use Survey _ 02 Survey Student Analysis Report {ending}.csv")
    t3 = load_wave(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report {ending}.csv")
    props = {"T1": proportions_per_wave(t1),
             "T2": proportions_per_wave(t2),
             "T3": proportions_per_wave(t3)}
    n_by = {"T1": max(props["T1"][i]["total"] for i in range(11)),
            "T2": max(props["T2"][i]["total"] for i in range(11)),
            "T3": max(props["T3"][i]["total"] for i in range(11))}
    fig, ax = plt.subplots(1, 1, figsize=(11, 13.5))
    draw_diverging_panel(ax, props, course_name, n_by)
    plt.subplots_adjust(left=0.28, right=0.93, top=0.95, bottom=0.06)
    out_path = f"./figures/supplementary/divergingBars_course{course_key}.png"
    plt.savefig(out_path, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"saved {out_path}")

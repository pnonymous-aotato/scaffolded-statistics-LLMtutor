"""
Generate Q8 / Q9 / Q7 individual-student trajectory plots AND
T1 to T3 transition heatmaps, in our visual style.
Palette and typography match our Figure 5 (CONSORT) and Figure 6 (arrow plot).
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

ITEM_LABELS = {
    0: ("Q1", "Enhanced learning"),
    1: ("Q2", "Encourages critical thinking"),
    2: ("Q3", "Recall/apply prior concepts"),
    3: ("Q4", "User-friendly and accessible"),
    4: ("Q5", "Feedback as helpful as instructor"),
    5: ("Q6", "Instructor prompts help use"),
    6: ("Q7", "Supports learning (equity)"),
    7: ("Q8", "Prepared before lecture"),
    8: ("Q9", "Understand lecture examples"),
    9: ("Q10", "Reduce need for other resources"),
    10: ("Q11", "Aware of university AI efforts"),
}

COLOR_A = "#2E6FAB"
COLOR_B = "#E59423"


def load_wave(path):
    out = {}
    with open(path) as f:
        reader = csv.reader(f); next(reader)
        for row in reader:
            if not row or not row[0]:
                continue
            vals = [LIKERT_MAP.get(row[i].strip() if i < len(row) else "", None)
                    for i in range(2, 24, 2)]
            out[row[0]] = vals
    return out


def get_complete_case_trajectories(t1, t2, t3, item_idx):
    """Return list of (sid, v1, v2, v3) for students in all three waves."""
    common = set(t1.keys()) & set(t2.keys()) & set(t3.keys())
    out = []
    for sid in sorted(common):
        v1 = t1[sid][item_idx]
        v2 = t2[sid][item_idx]
        v3 = t3[sid][item_idx]
        if v1 is not None and v2 is not None and v3 is not None:
            out.append((sid, v1, v2, v3))
    return out


def get_paired_T1T3(t1, t3, item_idx):
    common = set(t1.keys()) & set(t3.keys())
    out = []
    for sid in sorted(common):
        v1 = t1[sid][item_idx]
        v3 = t3[sid][item_idx]
        if v1 is not None and v3 is not None:
            out.append((v1, v3))
    return out


def draw_trajectory(ax, data, course_color, title, n):
    """Render individual trajectories with median overlay."""
    xs = [1, 2, 3]
    for sid, v1, v2, v3 in data:
        # Jitter slightly for visibility
        jit = np.random.uniform(-0.08, 0.08, 3)
        ax.plot([1 + jit[0], 2 + jit[1], 3 + jit[2]], [v1, v2, v3],
                color=course_color, alpha=0.35, linewidth=1.2)
        ax.plot([1 + jit[0], 2 + jit[1], 3 + jit[2]], [v1, v2, v3],
                'o', color=course_color, alpha=0.55, markersize=3.5)
    # Median line
    if data:
        med_v1 = np.median([v[1] for v in data])
        med_v2 = np.median([v[2] for v in data])
        med_v3 = np.median([v[3] for v in data])
        ax.plot([1, 2, 3], [med_v1, med_v2, med_v3],
                'D-', color='#BA2C2C', markersize=8, linewidth=2.2,
                label=f'Median (n={n})', markerfacecolor='#BA2C2C',
                markeredgecolor='white', markeredgewidth=1.2, zorder=10)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["T1", "T2", "T3"], fontsize=10)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["SD", "D", "N", "A", "SA"], fontsize=9)
    ax.set_ylim(0.7, 5.3)
    ax.set_xlim(0.6, 3.4)
    ax.set_title(title, fontsize=10, pad=6)
    ax.grid(True, axis='y', linestyle=':', alpha=0.4, linewidth=0.5)
    ax.legend(loc='lower right', fontsize=8.5, frameon=False)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis='both', length=3)
    ax.set_axisbelow(True)


def make_trajectory_fig(item_idx, out_path):
    qcode, qname = ITEM_LABELS[item_idx]
    t1_A = load_wave(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 2200.csv")
    t2_A = load_wave(f"{BASE}/AI Use Survey _ 02 Survey Student Analysis Report 2200.csv")
    t3_A = load_wave(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 2200.csv")
    t1_B = load_wave(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 4200.csv")
    t2_B = load_wave(f"{BASE}/AI Use Survey _ 02 Survey Student Analysis Report 4200.csv")
    t3_B = load_wave(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 4200.csv")
    data_A = get_complete_case_trajectories(t1_A, t2_A, t3_A, item_idx)
    data_B = get_complete_case_trajectories(t1_B, t2_B, t3_B, item_idx)
    np.random.seed(42)
    fig, (ax_A, ax_B) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    draw_trajectory(ax_A, data_A, COLOR_A, f"Course A (Intro)", len(data_A))
    draw_trajectory(ax_B, data_B, COLOR_B, f"Course B (Advanced)", len(data_B))
    fig.suptitle(f"{qcode}: {qname} — complete-case student trajectories",
                 fontsize=11.5, y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(out_path, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"saved {out_path}")


def draw_transition(ax, pairs, course_label, color_course, n):
    """Draw T1->T3 transition heatmap with count annotations."""
    M = np.zeros((5, 5), dtype=int)
    for v1, v3 in pairs:
        M[v1 - 1, v3 - 1] += 1
    # Invert vertical so higher values (SA) are at top
    M_display = M[::-1]
    # Use a blue colormap for consistency with our aesthetic
    im = ax.imshow(M_display, cmap='Blues', aspect='equal', vmin=0, vmax=max(M.max(), 1))
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels(["SD", "D", "N", "A", "SA"], fontsize=9)
    ax.set_yticklabels(["SA", "A", "N", "D", "SD"], fontsize=9)
    ax.set_xlabel("T3 response", fontsize=9.5)
    ax.set_ylabel("T1 response", fontsize=9.5)
    ax.set_title(f"Course {course_label} (n={n})", fontsize=10, pad=6)
    for i in range(5):
        for j in range(5):
            c = M_display[i, j]
            if c > 0:
                text_color = 'white' if c > M.max() * 0.5 else '#222222'
                ax.text(j, i, str(c), ha='center', va='center',
                        fontsize=10, color=text_color, fontweight='bold')
    ax.tick_params(axis='both', length=3)


def make_transition_fig(item_idx, out_path):
    qcode, qname = ITEM_LABELS[item_idx]
    t1_A = load_wave(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 2200.csv")
    t3_A = load_wave(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 2200.csv")
    t1_B = load_wave(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 4200.csv")
    t3_B = load_wave(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 4200.csv")
    pairs_A = get_paired_T1T3(t1_A, t3_A, item_idx)
    pairs_B = get_paired_T1T3(t1_B, t3_B, item_idx)
    fig, (ax_A, ax_B) = plt.subplots(1, 2, figsize=(10, 4))
    draw_transition(ax_A, pairs_A, "A", COLOR_A, len(pairs_A))
    draw_transition(ax_B, pairs_B, "B", COLOR_B, len(pairs_B))
    fig.suptitle(f"{qcode}: {qname} — T1 to T3 transitions",
                 fontsize=11.5, y=0.99)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(out_path, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"saved {out_path}")


# Trajectories for Q8, Q9 (our strong effects) and Q7 (the equity decline)
make_trajectory_fig(7, "./figures/supplementary/trajectory_Q8.png")
make_trajectory_fig(8, "./figures/supplementary/trajectory_Q9.png")
make_trajectory_fig(6, "./figures/supplementary/trajectory_Q7.png")

# Transitions for Q8, Q7
make_transition_fig(7, "./figures/supplementary/transitions_Q8.png")
make_transition_fig(6, "./figures/supplementary/transitions_Q7.png")

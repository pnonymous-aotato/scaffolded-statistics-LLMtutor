"""
Generate CONSORT-style participation flow figure.
Shows attendance pattern of each student across T1, T2, T3 per course.
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = "./data/raw_canvas_exports"

LIKERT_MAP = {
    "Strongly Disagree": 1, "Strongly disagree": 1,
    "Disagree": 2, "disagree": 2,
    "Neutral": 3, "neutral": 3,
    "Agree": 4, "agree": 4,
    "Strongly Agree": 5, "Strongly agree": 5, "strongly agree": 5,
    "": None,
}

def load_ids(path):
    ids = set()
    with open(path) as f:
        reader = csv.reader(f); next(reader)
        for row in reader:
            if row and row[0]:
                ids.add(row[0])
    return ids

# Per course, compute pattern
patterns = {"A": {}, "B": {}}

for course in ["A", "B"]:
    ending = "2200" if course == "A" else "4200"
    t1 = load_ids(f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report {ending}.csv")
    t2 = load_ids(f"{BASE}/AI Use Survey _ 02 Survey Student Analysis Report {ending}.csv")
    t3 = load_ids(f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report {ending}.csv")
    demo = load_ids(f"{BASE}/Demographic Survey (BONUS POINTS) Survey Student Analysis Report {ending}.csv")

    all_students = t1 | t2 | t3 | demo
    for sid in all_students:
        pattern = ""
        pattern += "T1" if sid in t1 else "--"
        pattern += "T2" if sid in t2 else "--"
        pattern += "T3" if sid in t3 else "--"
        patterns[course][pattern] = patterns[course].get(pattern, 0) + 1

print("Course A patterns:", patterns["A"])
print("Course B patterns:", patterns["B"])

# Calculate totals for summary
n_A = len({s for s in patterns["A"]})
total_A = sum(patterns["A"].values())
total_B = sum(patterns["B"].values())
complete_A = patterns["A"].get("T1T2T3", 0)
complete_B = patterns["B"].get("T1T2T3", 0)

# Build figure
fig, ax = plt.subplots(1, 1, figsize=(9, 4.5))

# Collect all patterns, ordered most-common first
all_patterns_A = sorted(patterns["A"].items(), key=lambda kv: -kv[1])
all_patterns_B = sorted(patterns["B"].items(), key=lambda kv: -kv[1])

# Build a unified list: course A rows first, then B
rows = []
for p, c in all_patterns_A:
    rows.append(("A", p, c))
for p, c in all_patterns_B:
    rows.append(("B", p, c))

y_positions = list(range(len(rows), 0, -1))  # top-to-bottom

color_A = "#2E6FAB"
color_B = "#E59423"

for y, (course, pattern, count) in zip(y_positions, rows):
    color = color_A if course == "A" else color_B
    ax.barh(y, count, color=color, height=0.65, alpha=0.9, edgecolor='white', linewidth=0.5)
    # Add count label
    ax.text(count + 0.15, y, str(count), va='center', fontsize=10, color='#222222')

# Y-axis labels
labels = [f"Course {course}: {pattern}" for course, pattern, _ in rows]
ax.set_yticks(y_positions)
ax.set_yticklabels(labels, fontsize=9)

ax.set_xlim(0, max(complete_A, complete_B) + 3)
ax.set_xlabel("Number of students", fontsize=10)
ax.set_title("Participation patterns across survey waves", fontsize=11, pad=8)

# Legend
from matplotlib.patches import Patch
handles = [Patch(color=color_A, label=f"Course A (Intro) — {total_A} unique students, {complete_A} complete"),
           Patch(color=color_B, label=f"Course B (Adv) — {total_B} unique students, {complete_B} complete")]
ax.legend(handles=handles, loc='lower right', fontsize=9, frameon=False)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.tick_params(axis='both', length=3)
ax.grid(True, axis='x', linestyle=':', alpha=0.35, linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("./paper/figure6.pdf", bbox_inches='tight', dpi=200)
plt.savefig("./paper/figure6.png", bbox_inches='tight', dpi=200)
print("Saved figure6.pdf and figure6.png")
print(f"Totals: A={total_A} unique ({complete_A} complete), B={total_B} unique ({complete_B} complete)")
print(f"Grand total: {total_A + total_B} students, {complete_A + complete_B} complete cases "
      f"= {100*(complete_A+complete_B)/(total_A+total_B):.1f}%")

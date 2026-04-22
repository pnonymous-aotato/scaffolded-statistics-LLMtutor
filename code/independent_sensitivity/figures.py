"""
figures.py
==========
Produce the publication-ready figures:
  Fig A: Diverging stacked bar chart per item per wave, per course
         (Robbins & Heiberger 2011, the standard for Likert)
  Fig B: Individual trajectory "spaghetti" plots for the complete-case
         sample (Q8 + Q9 which show the strongest signals)
  Fig C: Sankey-like transition heatmap (T1->T3 category shifts)
         for Q8 (Prepared before lecture)
  Fig D: Participation flow diagram (text-based -> svg optional)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

HERE = Path('./survey/survey')
OUT = HERE / 'analysis_out'
OUT.mkdir(exist_ok=True)

long = pd.read_csv(HERE / 'long.csv')
meta = pd.read_csv(HERE / 'meta.csv')

ITEM_LABELS = {
    1: "Enhanced learning",
    2: "Encourages critical thinking",
    3: "Recall/apply prior concepts",
    4: "User-friendly & accessible",
    5: "Feedback as helpful as instructor",
    6: "Instructor prompts help use",
    7: "Supports learning regardless of background",
    8: "Prepared before lecture",
    9: "Understand lecture examples",
    10: "Reduce need for other resources",
    11: "Aware of university AI efforts",
}

# ---- Fig A: Diverging stacked bar per course ----
# Scheme: SD/D go LEFT (negative), Neutral split at 50%, A/SA go RIGHT.
COLORS = {1: '#b2182b', 2: '#ef8a62', 3: '#f7f7f7', 4: '#67a9cf', 5: '#2166ac'}

def diverging_stacked(course, outfile):
    fig, axes = plt.subplots(11, 1, figsize=(10, 14), sharex=True)
    fig.suptitle(f'Course {course}: Likert response distributions by wave '
                 '(diverging stacked, Robbins & Heiberger 2011)',
                 fontsize=11, y=1.00)

    for idx, q in enumerate(range(1, 12)):
        ax = axes[idx]
        for wi, w in enumerate(['T3', 'T2', 'T1']):  # top-to-bottom T1, T2, T3
            sub = long.query("course == @course and qnum == @q "
                             "and wave == @w and response_ord.notna()")
            v = sub['response_ord'].astype(int).values
            n = len(v)
            if n == 0: continue
            props = {k: (v == k).sum() / n for k in range(1, 6)}
            # center at zero between Neutral's left and right halves
            # Left of zero: -SD - D - 0.5*N
            # Right of zero: 0.5*N + A + SA
            left_start = -(props[1] + props[2] + 0.5*props[3])
            segments = [
                (1, -props[1] - props[2] - 0.5*props[3], props[1]),
                (2, -props[2] - 0.5*props[3],            props[2]),
                (3, -0.5*props[3],                        props[3]),  # neutral
                (4, 0.5*props[3],                         props[4]),
                (5, 0.5*props[3] + props[4],              props[5]),
            ]
            y = wi
            for lvl, start, width in segments:
                if width > 0:
                    ax.barh(y, width, left=start, color=COLORS[lvl],
                            edgecolor='white', linewidth=0.5)
            ax.text(1.02, y, f"n={n}", va='center', fontsize=7)

        ax.set_yticks([0, 1, 2])
        ax.set_yticklabels(['T3', 'T2', 'T1'], fontsize=8)
        ax.set_xlim(-1.15, 1.15)
        ax.axvline(0, color='grey', lw=0.5)
        ax.set_title(f"Q{q}: {ITEM_LABELS[q]}", fontsize=9, loc='left')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xticks([-1, -0.5, 0, 0.5, 1])
        ax.set_xticklabels(['100%', '50%', '0', '50%', '100%'], fontsize=7)
        ax.tick_params(axis='y', length=0)
    # legend
    patches = [mpatches.Patch(color=COLORS[k],
                              label=['Strongly Disagree','Disagree','Neutral',
                                     'Agree','Strongly Agree'][k-1])
               for k in range(1,6)]
    fig.legend(handles=patches, loc='lower center', ncol=5,
               bbox_to_anchor=(0.5, -0.005), fontsize=8, frameon=False)
    fig.tight_layout(rect=[0, 0.02, 1, 0.98])
    fig.savefig(outfile, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('wrote', outfile)

diverging_stacked('A', OUT / 'figA_diverging_courseA.png')
diverging_stacked('B', OUT / 'figA_diverging_courseB.png')

# ---- Fig B: Paired trajectory for Q8 (Prepared) and Q9 (Understand) ----
# These are the two items where we expect to see the strongest signals.
def trajectory_plot(qnum, outfile):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    for ai, c in enumerate(['A', 'B']):
        ax = axes[ai]
        cc_ids = meta.query("course == @c and n_waves == 3")['anon_id'].tolist()
        sub = long.query("course == @c and qnum == @qnum "
                         "and anon_id in @cc_ids")
        piv = sub.pivot(index='anon_id', columns='wave',
                        values='response_ord')[['T1', 'T2', 'T3']]
        # jitter for readability
        rng = np.random.default_rng(qnum*1000 + ai)
        for _, row in piv.iterrows():
            jy = rng.uniform(-0.15, 0.15, size=3)
            ax.plot([1, 2, 3], row.values + jy, '-', color='steelblue',
                    alpha=0.35, lw=0.8)
            ax.plot([1, 2, 3], row.values + jy, 'o', color='steelblue',
                    alpha=0.5, ms=3)
        # median trajectory
        med = piv.median()
        ax.plot([1, 2, 3], med.values, 'D-', color='firebrick',
                lw=2, ms=7, label=f'Median (n={len(piv)})')
        ax.set_xticks([1, 2, 3]); ax.set_xticklabels(['T1', 'T2', 'T3'])
        ax.set_ylim(0.5, 5.5)
        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(['SD', 'D', 'N', 'A', 'SA'])
        ax.set_title(f"Course {c}", fontsize=10)
        ax.legend(loc='lower right', fontsize=8, frameon=False)
        ax.grid(axis='y', alpha=0.2)
    fig.suptitle(f"Q{qnum}: {ITEM_LABELS[qnum]} - complete-case trajectories",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('wrote', outfile)

trajectory_plot(8, OUT / 'figB_trajectory_Q8.png')
trajectory_plot(9, OUT / 'figB_trajectory_Q9.png')

# ---- Fig C: Participation flow ----
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
patterns = ['T1T2T3', 'T1--T3', 'T1T2--', 'T1----', '----T3', '--T2--', '----T1']
bar_data = []
for c in ['A', 'B']:
    for p in patterns:
        n = ((meta['course']==c) & (meta['pattern']==p)).sum()
        if n > 0:
            bar_data.append((c, p, n))

labels = [f"{c}: {p}" for c, p, n in bar_data]
ns = [n for _, _, n in bar_data]
colors = ['tab:blue' if c=='A' else 'tab:orange' for c, _, _ in bar_data]
ax.barh(range(len(labels)), ns, color=colors)
for i, n in enumerate(ns):
    ax.text(n + 0.1, i, str(n), va='center', fontsize=9)
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel('Number of students')
ax.set_title('Participation patterns across waves')
a_patch = mpatches.Patch(color='tab:blue', label='Course A (Intro)')
b_patch = mpatches.Patch(color='tab:orange', label='Course B (Adv)')
ax.legend(handles=[a_patch, b_patch], loc='lower right', frameon=False)
fig.tight_layout()
fig.savefig(OUT / 'figC_participation_flow.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print('wrote', OUT / 'figC_participation_flow.png')

# ---- Fig D: Transition heatmap T1 -> T3 for Q8 ----
def transition_heatmap(qnum, outfile):
    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    for ai, c in enumerate(['A', 'B']):
        ax = axes[ai]
        cc_ids = meta.query("course == @c and n_waves == 3")['anon_id'].tolist()
        sub = long.query("course == @c and qnum == @qnum "
                         "and anon_id in @cc_ids")
        piv = sub.pivot(index='anon_id', columns='wave',
                        values='response_ord')[['T1', 'T3']].dropna()
        tbl = np.zeros((5, 5), dtype=int)
        for _, row in piv.iterrows():
            i = int(row['T1']) - 1
            j = int(row['T3']) - 1
            tbl[i, j] += 1
        im = ax.imshow(tbl, cmap='Blues', vmin=0,
                       vmax=max(1, tbl.max()), aspect='auto')
        for i in range(5):
            for j in range(5):
                if tbl[i, j] > 0:
                    ax.text(j, i, str(tbl[i,j]),
                            ha='center', va='center',
                            color='white' if tbl[i,j] > tbl.max()/2 else 'black',
                            fontsize=10)
        ax.set_xticks(range(5)); ax.set_yticks(range(5))
        ax.set_xticklabels(['SD','D','N','A','SA'])
        ax.set_yticklabels(['SD','D','N','A','SA'])
        ax.set_xlabel('T3 response')
        ax.set_ylabel('T1 response')
        ax.set_title(f"Course {c} (n={len(piv)})")
    fig.suptitle(f"Q{qnum}: {ITEM_LABELS[qnum]} - T1 to T3 transitions",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('wrote', outfile)

transition_heatmap(8, OUT / 'figD_transition_Q8.png')
transition_heatmap(9, OUT / 'figD_transition_Q9.png')

print('\nDone.')

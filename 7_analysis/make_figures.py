"""Draws Figures 1-4 from Supplementary Data S2.

Usage: python make_figures.py Supplementary_Data_S2.xlsx out_dir
Writes figN.pdf (vector) and figN.png (600 dpi) for N = 1..4.
"""
import sys, os
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from openpyxl import load_workbook

plt.rcParams.update({"font.family": "Liberation Sans", "font.size": 9,
                     "pdf.fonttype": 42, "axes.spines.top": False,
                     "axes.spines.right": False})
INK, GREY, LIGHT = "#222222", "#888888", "#d9d9d9"
SHADES = ["#1b1b1b", "#4d4d4d", "#7a7a7a", "#a6a6a6", "#cfcfcf", "#ffffff"]

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
wb = load_workbook(src, data_only=True)


def rows(sheet):
    r = list(wb[sheet].iter_rows(values_only=True))
    hi = next(i for i, x in enumerate(r[:10]) if x and ("SID" in x or "Study_ID" in x))
    H = r[hi]
    return H, [x for x in r[hi + 1:] if x and x[0]]


def save(fig, n):
    fig.savefig(f"{out}/fig{n}.pdf", bbox_inches="tight")
    fig.savefig(f"{out}/fig{n}.png", dpi=600, bbox_inches="tight")
    plt.close(fig)


H, core = rows("Extraction_Core75")
col = lambda name: H.index(name)
SH, sens = rows("Sensitivity_Set13")

# Figure 1: PRISMA 2020 flow diagram
fig, ax = plt.subplots(figsize=(7.2, 7.8))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")


def box(x, y, w, h, txt, bold=False, fill="white", fs=7.1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1",
                                fc=fill, ec=INK, lw=0.8))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", linespacing=1.35)


def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK, mutation_scale=8, shrinkA=0, shrinkB=0))


def line(xs, ys):
    ax.plot(xs, ys, color=INK, lw=0.8, solid_capstyle="butt")


ax.text(33, 98.5, "Studies identified via databases", ha="center", fontsize=8.2, fontweight="bold")
ax.text(82.5, 98.5, "Studies identified via other methods", ha="center", fontsize=8.2, fontweight="bold")
for y, lab in [(87, "Identification"), (66, "Screening"), (40, "Eligibility"), (9, "Included")]:
    ax.text(1, y, lab, rotation=90, ha="center", va="center", fontsize=7.8, fontweight="bold", color=GREY)
# database column (A) and exclusions (B)
box(4, 80, 30, 14, "Records identified from six databases\n(n = 3,880)\nIEEE Xplore 346; Scopus 590;\nSpringerLink 785; ScienceDirect 1,147;\nWeb of Science 305; arXiv 707", fs=6.6)
box(40, 82, 22, 10, "Duplicates removed\n(n = 1,164)")
box(4, 61, 30, 10, "Records screened on\ntitle and abstract (n = 2,716)")
box(40, 61, 22, 10, "Records excluded\n(n = 2,591)")
box(4, 40, 30, 12, "Candidates assessed for\neligibility and quality (n = 125)\nfull text 65; abstract only 60")
box(40, 40, 22, 12, "Excluded (n = 51)\nassessed in full text 16;\nassessed on abstract 35")
box(4, 22, 30, 10, "All criteria met on full text\n(n = 56: 49 + 7 full texts\nobtained on second attempt)")
box(40, 22, 22, 10, "All criteria met on\nabstract only (n = 18)")
arrow(34, 87, 40, 87); arrow(19, 80, 19, 71); arrow(34, 66, 40, 66); arrow(19, 61, 19, 52)
arrow(34, 46, 40, 46); arrow(19, 40, 19, 32)
line([30, 30, 51], [40, 36, 36]); arrow(51, 36, 51, 32)
# other methods (C)
box(68, 80, 28, 14, "Backward snowballing\n(n = 14)\ncore 6; sensitivity 1; excluded 7")
box(68, 61, 28, 12, "Forward snowballing\n(n = 25)\ncore 10; excluded 15")
box(68, 40, 28, 14, "Second full-text retrieval for\nthe 19 abstract-only studies:\n6 full texts obtained and\nmoved to the core set")
for y in (87, 67, 47):
    line([96, 98.5], [y, y])
line([98.5, 98.5], [87, 17])
# included sets
box(4, 3, 30, 11, "Core set, full text\n(n = 75)", bold=True, fill="#efefef", fs=8)
box(40, 3, 22, 11, "Sensitivity set,\nabstract-level evidence\n(n = 13)", bold=True, fill="#efefef", fs=7.6)
line([98.5, 51], [17, 17]); arrow(51, 17, 51, 14)
line([51, 26], [17, 17]); arrow(26, 17, 26, 14)
arrow(12, 22, 12, 14)
ax.text(13, 18.2, "3 removed at\nfinal verification", fontsize=6.6, va="center", color=INK)
ax.text(66, 19.2, "+22 to core (6 + 10 + 6); +1 to sensitivity set;\n6 leave the sensitivity set", fontsize=6.6, ha="left", va="center")
arrow(51, 22, 51, 17.6)
save(fig, 1)

# Figure 2: core studies per year by archetype
years = [2022, 2023, 2024, 2025, 2026]
arcs = ["T1", "T2", "T3", "T4", "T5", "E"]
names = {"T1": "T1 Fine-tuned specialist", "T2": "T2 Prompted generalist", "T3": "T3 Iterative repair loop",
         "T4": "T4 Agentic orchestrator", "T5": "T5 Configuration remediator", "E": "E Evaluation study"}
cnt = Counter((int(r[col("Year")]), r[col("Archetype")]) for r in core)
fig, ax = plt.subplots(figsize=(6.0, 3.4))
bottom = [0] * len(years)
for a, shade in zip(arcs, SHADES):
    vals = [cnt[(y, a)] for y in years]
    ax.bar([str(y) for y in years], vals, bottom=bottom, color=shade, edgecolor=INK, lw=0.6, label=names[a], width=0.62)
    bottom = [b + v for b, v in zip(bottom, vals)]
for i, t in enumerate(bottom):
    ax.text(i, t + 0.6, str(t), ha="center", fontsize=8)
ax.set_ylabel("Core studies"); ax.set_xlabel("Publication year")
ax.set_ylim(0, max(bottom) + 4)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
save(fig, 2)

# Figure 3: model families
fam = Counter()
for r in core:
    for f in str(r[col("Model_Families")]).split(";"):
        if f.strip():
            fam[f.strip()] += 1
items = fam.most_common()[::-1]
fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.barh([k for k, _ in items], [v for _, v in items], color="#7a7a7a", edgecolor=INK, lw=0.6, height=0.65)
for i, (_, v) in enumerate(items):
    ax.text(v + 0.5, i, str(v), va="center", fontsize=8)
ax.set_xlabel("Core studies using the model family (n = 75; a study can use several)")
save(fig, 3)

# Figure 4: strongest validation criterion, core vs sensitivity set
levels = [("0  Similarity or LLM judge", ("0",)), ("1  Human judgement", ("1 Human",)), ("1  Compilation or syntax", ("1 Comp",)),
          ("2  Static re-scan", ("2",)), ("3  Test execution", ("3",)), ("4  Formal verification", ("4",)),
          ("5  Exploit-based or dynamic", ("5",)), ("Not stated in abstract", ("NR",))]


def share(rs, idx):
    out = []
    for _, keys in levels:
        n = sum(1 for r in rs if str(r[idx]).startswith(keys))
        out.append(100 * n / len(rs))
    return out


c_sh, s_sh = share(core, col("Strongest_Validation")), share(sens, SH.index("Strongest_Validation"))
fig, ax = plt.subplots(figsize=(6.2, 3.6))
ys = range(len(levels))
ax.barh([y + 0.2 for y in ys], c_sh, height=0.38, color="#4d4d4d", edgecolor=INK, lw=0.6, label="Core set, full text (n = 75)")
ax.barh([y - 0.2 for y in ys], s_sh, height=0.38, color="white", edgecolor=INK, lw=0.6, hatch="////", label="Sensitivity set, abstracts (n = 13)")
for y, v in zip(ys, c_sh):
    ax.text(v + 0.8, y + 0.2, f"{v:.0f}%", va="center", fontsize=7.5)
for y, v in zip(ys, s_sh):
    ax.text(v + 0.8, y - 0.2, f"{v:.0f}%", va="center", fontsize=7.5)
ax.set_yticks(list(ys)); ax.set_yticklabels([l for l, _ in levels])
ax.set_xlabel("Share of studies (%)"); ax.set_xlim(0, 60); ax.set_ylabel("Rank and fix criterion")
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
save(fig, 4)
print("figures written to", out)

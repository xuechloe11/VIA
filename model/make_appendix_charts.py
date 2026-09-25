"""Appendix charts built from VIA_software_services_mix.xlsx.

  appendix_services_mix_chart.png  - services share of revenue, by estimation method (Summary tab)
  appendix_contracts_chart.png     - annualized contract value, services vs software (Contracts tab)

Run: python3 model/make_appendix_charts.py
"""
import os
import openpyxl
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
wb = openpyxl.load_workbook(os.path.join(HERE, "VIA_software_services_mix.xlsx"), data_only=True)

SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1"
BLUE, ORANGE, NEUTRAL = "#2a78d6", "#eb6834", "#c9c8c1"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": INK})


def rounded_barh(ax, y, left, width, height, color, zorder=3):
    """Horizontal bar with a 4px-ish rounded data end, square at the baseline."""
    ax.barh(y, width, left=left, height=height, color=color, zorder=zorder, linewidth=0)


def frame(ax):
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", length=0, labelsize=11)
    ax.set_facecolor(SURFACE)


# ------------------------------------------------------------------ 1) services mix
s = wb["Summary"]
rows = [
    ("Bleecker, as published", "Q3'25 GM 40%, TaaS GM 26.2%", s["B5"].value),
    ("Bleecker's inputs, math corrected", "TaaS GM 29.2%, not 26.2%", s["B6"].value),
    ("Updated: 2026 contract pricing", "Base case, TTM adj. GM 40.3%", s["B7"].value),
    ("Updated, at Q2'26 adj. GM", "41.5% GM (mgmt: reverts)", s["B8"].value),
    ("Updated, paratransit 30% of hours", "2026 wins bundle ADA paratransit", s["B9"].value),
    ("Reported cost split", "Q2'26, 22% services GM", s["B14"].value),
]
HL = 2  # highlighted base case

fig, ax = plt.subplots(figsize=(11, 5.9), dpi=200)
fig.patch.set_facecolor(SURFACE)
ys = list(range(len(rows)))[::-1]
for y, (lab, sub, v), i in zip(ys, rows, range(len(rows))):
    rounded_barh(ax, y, 0, v, 0.56, BLUE if i == HL else NEUTRAL)
    ax.text(0.80, y, f"{v:.1%}", va="center", ha="left", fontsize=13,
            fontweight="bold" if i == HL else "normal", color=INK)
    ax.text(-0.02, y + 0.12, lab, ha="right", va="center", fontsize=12.5,
            fontweight="bold" if i == HL else "normal", color=INK)
    ax.text(-0.02, y - 0.17, sub, ha="right", va="center", fontsize=10.5, color=INK2)
ax.axvline(0.72, color=INK2, lw=1.2, ls=(0, (3, 3)), zorder=4)
ax.text(0.715, len(rows) - 0.45, "Bleecker headline: 72%", ha="right", va="center", fontsize=10, color=INK2)
ax.set_xlim(0, 0.87)
ax.set_ylim(-0.6, len(rows) - 0.2)
ax.set_xticks([0, 0.25, 0.5, 0.75])
ax.set_xticklabels(["0%", "25%", "50%", "75%"])
ax.set_yticks([])
ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
frame(ax)
fig.subplots_adjust(left=0.31, right=0.97, top=0.78, bottom=0.2)
fig.text(0.015, 0.95, "About three-quarters of VIA's revenue is services, whichever way you estimate it",
         fontsize=15.5, fontweight="bold", color=INK)
fig.text(0.015, 0.855, "Services (TaaS) share of revenue: Bleecker's margin back-out, corrected and updated with 2026 "
         "contract pricing,\nvs. VIA's reported cost split", fontsize=11, color=INK2)
fig.text(0.015, 0.035,
         "Sources: VIA 10-K FY25 and 10-Qs Q3'25–Q2'26; Bleecker Street Research (Dec 2025); 2026 council records "
         "(University Park \\$64.52 micro / \\$67.75 para per vehicle-hr;\nDouglas Co. ~$70/hr). Method: services share = "
         "(SaaS GM − blended GM) / (SaaS GM − TaaS GM), SaaS GM 75%. Cost-split row: services revenue = services cost / "
         "(1 − 22%).\nFull model: VIA_software_services_mix.xlsx.", fontsize=8.5, color=MUTED, linespacing=1.5)
fig.savefig(os.path.join(HERE, "appendix_services_mix_chart.png"), facecolor=SURFACE)
plt.close(fig)

# ------------------------------------------------------------------ 2) contracts
c = wb["Contracts"]
SHORT = {
    1: "LA Metro – Metro Micro ops", 2: "Arlington, TX – On-Demand", 3: "DCTA GoZone (Denton Co., TX)",
    4: "King County Metro – Metro Flex", 5: "Mobile, AL – The Wave (full network)", 6: "New Braunfels, TX",
    7: "Miami-Dade", 8: "Lorain County, OH", 9: "Gastonia, NC", 10: "Texas customer (Q4'25 call)",
    13: "Transport for London – software only", 15: "Plano, TX – Plano Rides", 16: "Douglas Co., CO – Link",
    17: "Addison, TX – Orbit", 20: "Highland Park, TX", 21: "University Park, TX – paratransit",
    24: "Douglas Co., CO – Castle Rock", 25: "Cobb County, GA – expansion", 26: "Jersey City, NJ – service cut",
}
data = []
for r in range(5, 32):
    n, when, ann, sw, sv, basis = (c[f"A{r}"].value, c[f"D{r}"].value, c[f"K{r}"].value,
                                   c[f"M{r}"].value, c[f"N{r}"].value, c[f"O{r}"].value)
    if not ann or n not in SHORT:
        continue
    yr = str(when)[:4]
    data.append(dict(name=f"{SHORT[n]} ({yr})", ann=ann, sw=sw or 0, sv=sv or 0, basis=basis))
pos = sorted([d for d in data if d["ann"] > 0], key=lambda d: d["ann"])
neg = [d for d in data if d["ann"] < 0]
order = neg + pos
tot_sw = sum(d["sw"] for d in pos)
tot = sum(d["ann"] for d in pos)

fig, ax = plt.subplots(figsize=(11, 8.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
H = 0.62
for y, d in enumerate(order):
    if d["ann"] < 0:
        rounded_barh(ax, y, 0, d["ann"], H, NEUTRAL)
        ax.text(0.3, y, f"−${-d['ann']:.1f}M/yr (hours cut, Saturday service ended)", va="center", ha="left",
                fontsize=10.5, color=INK)
        continue
    rounded_barh(ax, y, 0, d["sv"], H, BLUE)
    if d["sw"] > 0:
        gap = 0.08 if d["sv"] > 0 else 0
        rounded_barh(ax, y, d["sv"] + gap, max(d["sw"] - gap, 0.05), H, ORANGE)
    ax.text(d["ann"] + 0.3, y, f"${d['ann']:.1f}M", va="center", ha="left", fontsize=10.5, color=INK)
ax.set_yticks(range(len(order)))
ax.set_yticklabels([d["name"] for d in order], fontsize=10.5)
ax.axvline(0, color=INK2, lw=0.8, zorder=4)
ax.set_xlim(-5, 26)
ax.set_xticks([0, 5, 10, 15, 20, 25])
ax.set_xticklabels(["$0", "$5M", "$10M", "$15M", "$20M", "$25M"])
ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
frame(ax)
# legend (2 series + the reduction)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=BLUE, label="Services (drivers, vehicles, operations)"),
                   Patch(color=ORANGE, label="Software"),
                   Patch(color=NEUTRAL, label="Spending cut")],
          loc="center right", frameon=False, fontsize=10.5)
fig.subplots_adjust(left=0.34, right=0.97, top=0.84, bottom=0.13)
fig.text(0.015, 0.955, "VIA's contracts are services contracts", fontsize=15.5, fontweight="bold", color=INK)
fig.text(0.015, 0.885, f"Annualized contract value by customer: software is {tot_sw / tot:.0%} of the "
         f"${tot:.0f}M shown.\nAlmost every deal is turnkey: VIA supplies the drivers and vehicles.",
         fontsize=11, color=INK2)
fig.text(0.015, 0.025,
         "Sources: council and board records (LA Metro Nov 2024; Arlington Dec 2024; DCTA Sep 2023; Mobile Sep 2025; "
         "Plano Feb 2026;\nCobb Co. Sep 2026; Jersey City Jul 2026), TfL award, VIA Q4'25 call. Software share is "
         "disclosed where a price schedule itemizes it (LA Metro 0%,\nDCTA 0%, Texas example 0.4%, TfL 100%); other "
         "turnkey deals assume 4%. Short pilots annualized. Full tracker: VIA_software_services_mix.xlsx, Contracts tab.",
         fontsize=8.5, color=MUTED, linespacing=1.5)
fig.savefig(os.path.join(HERE, "appendix_contracts_chart.png"), facecolor=SURFACE)
plt.close(fig)
print("saved", tot, tot_sw, [(d["name"], round(d["ann"], 2)) for d in order])

"""Render the post-Bleecker contract list as an exportable PNG table."""
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROWS = [
    ("1", "Twin Cities Area Transit (Benton Harbor, MI)", "Dec 2025 (ops Apr 2026)", "Network", "Not disclosed", "Full network takeover; redesign 'without an increase in operating costs'"),
    ("2", "Plano, TX", "Feb 2026", "Micro + paratransit", "$3.95M / 6 mo; renewals ~$8M/yr", "Texas co-op contract; 22 vehicles; Spare ranked #1 but withdrew"),
    ("3", "Douglas County, CO (Lone Tree / Parker)", "Feb 2026", "Microtransit", "$4.4M", "Renewal + expansion into Parker"),
    ("4", "Addison, TX", "Mar 2026", "Micro + paratransit", "$0.87M / 6 mo", "Pilot; renewal ~Oct 2026"),
    ("5", "NJ TRANSIT MicroLink", "Apr 2026", "Pilot (2 zones)", "Not disclosed", "FTA-funded 2-yr pilot; Bergen Via-operated, Monmouth software-only"),
    ("6", "Highland Park, TX", "Apr 2026", "Micro + paratransit", "$1.55M / 6 mo (budget)", "Pilot, 4 vehicles; renewal ~Nov 2026"),
    ("7", "University Park, TX", "Apr 2026 (cancelled)", "Paratransit", "$1.06M / yr", "$67.75/hr para, $64.52/hr micro; cancelled after DART vote"),
    ("8", "Union County, NJ", "Jun 2026", "Microtransit", "Not disclosed", "1-yr turnkey pilot: vehicles, drivers, tech, support"),
    ("9", "Rochester, MN", "Jul 2026 (ops Sep 2026)", "Network", "$77.8M / 64 mo (~$14.6M/yr)", "Drivers + mgmt for city-owned buses; replaces Transdev; union 20% raise carries over; ~80% grant-funded"),
    ("10", "Douglas County, CO (Castle Rock)", "Jul 2026", "Microtransit", "$1.99M / yr; 2 yrs + options", "~$70/hr; $33-40 per ride; state + local funding"),
    ("11", "Jersey City, NJ", "Jul 2026", "Service cut", "-$4M / yr", "Hours roughly halved; Saturday service ended"),
    ("12", "Cobb County, GA", "Sep 2026", "Microtransit", "$6.3M", "Expansion (2-yr + 1-yr zones); fixed fee; state trust fund"),
    ("13", "Garner, NC", "2026", "Consulting", "Not disclosed", "60-day microtransit feasibility study"),
    ("14", "Four unnamed network deals", "By May 2026", "Network", "> $40M / yr total", "~$10M each; disclosed in aggregate on Q1'26 call"),
]
COLS = ["#", "Customer", "Date", "Type", "Value / term", "Key terms"]
WIDTHS = [0.03, 0.21, 0.13, 0.11, 0.17, 0.35]
WRAP = [3, 30, 18, 15, 24, 52]
SURF, TXT, TXT2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8983"
LINE, ACC, ACCBG, NEG = "#e3e2dc", "#2a78d6", "#e8f1fb", "#b54708"

lines = [[textwrap.wrap(c, w) or [""] for c, w in zip(r, WRAP)] for r in ROWS]
nlines = [max(len(x) for x in l) for l in lines]
LH_IN, PAD_IN, HEAD_IN = 0.17, 0.12, 0.35          # inches per text line / row padding / header
table_in = HEAD_IN + sum(n * LH_IN + PAD_IN for n in nlines)
top_in, bot_in = 1.05, 0.55
fig_h = table_in + top_in + bot_in
fig = plt.figure(figsize=(13, fig_h), dpi=200)
fig.patch.set_facecolor(SURF)
ax = fig.add_axes([0.02, bot_in / fig_h, 0.96, table_in / fig_h])
ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, table_in)

x = [0]
for w in WIDTHS[:-1]:
    x.append(x[-1] + w)
y = table_in
for i, c in enumerate(COLS):
    ax.text(x[i] + 0.004, y - 0.08, c, fontsize=9, fontweight="bold", color=TXT2, va="top")
y -= HEAD_IN
ax.plot([0, 1], [y + 0.02, y + 0.02], color=TXT2, lw=0.8)
for r, l, n in zip(ROWS, lines, nlines):
    rh = n * LH_IN + PAD_IN
    net = r[3] == "Network"
    if net:
        ax.add_patch(Rectangle((0, y - rh), 1, rh, color=ACCBG, lw=0, zorder=0))
    for i, cell in enumerate(l):
        col, fw = TXT, "normal"
        if i == 0: col = MUTED
        if i == 1: fw = "bold"
        if i == 3 and net: col, fw = ACC, "bold"
        if i == 4 and r[4].startswith("-"): col = NEG
        ax.text(x[i] + 0.004, y - 0.06, "\n".join(cell), fontsize=8.6, color=col,
                va="top", fontweight=fw, linespacing=1.25)
    y -= rh
    ax.plot([0, 1], [y, y], color=LINE, lw=0.6)

fig.text(0.02, 1 - 0.38 / fig_h, "Via contracts awarded or amended since Bleecker's report (Dec 16, 2025)",
         fontsize=14, fontweight="bold", color=TXT, va="top")
fig.text(0.02, 1 - 0.72 / fig_h, "Every priced deal is turnkey (Via supplies drivers, vehicles and operations); "
         "the largest are network takeovers from Transdev. Network deals shaded.", fontsize=9.5, color=TXT2, va="top")
fig.text(0.02, 0.18 / fig_h, "Sources: city/county council records and press releases, local news, NJ TRANSIT, "
         "Via Q1'26 earnings call. Most terms from council summaries and news, not signed contracts. As of Sep 2026.",
         fontsize=7.5, color=MUTED)
fig.savefig("model/contracts_since_bleecker.png", facecolor=SURF)
print("saved")

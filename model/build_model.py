from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter as L

wb = Workbook()
F = "Arial"
BLUE = Font(name=F, color="0000FF", size=10)
BLK = Font(name=F, size=10)
GRN = Font(name=F, color="008000", size=10)
B = Font(name=F, bold=True, size=10)
H = Font(name=F, bold=True, size=12)
T = Font(name=F, bold=True, size=14)
HDRFILL = PatternFill("solid", fgColor="D9E1F2")
YEL = PatternFill("solid", fgColor="FFFF00")
thin = Side(style="thin", color="999999")
BOT = Border(bottom=thin)
USD = '$#,##0.0;($#,##0.0);-'
PCT = '0.0%;(0.0%);-'
WRAP = Alignment(wrap_text=True, vertical="top")

def hdr(ws, r, labels, c0=1):
    for i, t in enumerate(labels):
        c = ws.cell(r, c0 + i, t); c.font = B; c.fill = HDRFILL; c.alignment = WRAP; c.border = BOT

def put(ws, ref, v, font=BLK, fmt=None, fill=None):
    c = ws[ref]; c.value = v; c.font = font
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    return c

# ---------------- Sources ----------------
SRC = {
 "S1": ("Via S-1/A (FY2024 revenue $337.6M; FY2024 cost of revenue split)", "https://www.sec.gov/Archives/edgar/data/1603015/000160301525000012/viatransportationinc-sx1a.htm"),
 "S2": ("Via 10-Q Q3 2025 (Q3 and 9M 2025 cost of revenue split; H1 2025 figures)", "https://www.sec.gov/Archives/edgar/data/1603015/000160301525000042/via-20250930.htm"),
 "S3": ("Via 10-K FY2025 (FY2025 revenue $434.337M; FY cost of revenue split)", "https://www.sec.gov/Archives/edgar/data/1603015/000160301526000008/via-20251231.htm"),
 "S4": ("Via 10-Q Q1 2026", "https://www.sec.gov/Archives/edgar/data/0001603015/000160301526000014/via-20260331.htm"),
 "S5": ("Via 10-Q Q2 2026", "https://www.sec.gov/Archives/edgar/data/0001603015/000160301526000026/via-20260630.htm"),
 "S6": ("Via Q4/FY2025 press release (ARR $476M)", "https://www.sec.gov/Archives/edgar/data/1603015/000160301526000002/viaq425pressrelease.htm"),
 "S7": ("Via Q2 2026 press release (ARR $543M, adj. GM 41%)", "https://www.sec.gov/Archives/edgar/data/1603015/000160301526000027/viaq226pressrelease.htm"),
 "S8": ("Bleecker Street Research, 'Via Transportation (VIA): Road to Nowhere' (Dec 16, 2025)", "https://www.bleeckerstreetresearch.com/research/via"),
 "S9": ("Yahoo Finance / Insider Monkey summary of Bleecker bear case", "https://finance.yahoo.com/news/via-transportation-inc-via-bear-133548863.html"),
 "S10": ("Investing.com: stock falls after short report", "https://www.investing.com/news/stock-market-news/via-transportation-stock-falls-after-short-seller-questions-business-model-93CH-4552465"),
 "S11": ("Plano council item ($3,952,247, 6 months + three 1-yr renewals)", "https://content.civicplus.com/api/assets/tx-plano/a163970f-6ef0-4df2-80fa-dfefc1bc37be"),
 "S12": ("Branch Herald: Addison approves Via ($872,231, 6 months)", "https://www.branchherald.com/stories/addison-approves-contract-with-via-for-mobility-services,81030"),
 "S13": ("People Newspapers: Highland Park microtransit/paratransit ($1.55M FY26 budget amendment)", "https://www.peoplenewspapers.com/news/2026/05/microtransit-and-paratransit-get-rolling-in-highland-park/"),
 "S14": ("People Newspapers: University Park cancels Via agreement", "https://www.peoplenewspapers.com/news/2026/05/up-cancels-alternate-paratransit-agreement-following-dart-vote/"),
 "S15": ("NJ TRANSIT press release: MicroLink pilot (Bergen: Via-operated; Monmouth: NJT-operated on Via software)", "https://www.njtransit.com/press-releases/nj-transit-pilot-microtransit-shuttle-service-monmouth-and-bergen-counties"),
 "S16": ("Union County NJ press release (River North Transit, turnkey)", "https://ucnj.org/press-releases/public-info/2026/06/01/union-county-announces-new-on-demand-micro-transit-pilot-program-to-expand-transportation-access/"),
 "S17": ("Colorado Politics: DougCo approves $2M Link On Demand expansion (River North Transit, $1,991,720)", "https://www.coloradopolitics.com/2026/07/14/dougco-approves-2m-rideshare-expansion-to-castle-rock/"),
 "S18": ("East Cobb News: Cobb approves microtransit expansion ($6.3M)", "https://eastcobbnews.com/cobb-approves-josh-traffic-project-microtransit-expansion/"),
 "S19": ("Hudson County View: Jersey City cutting Via hours, ~$4M savings", "http://hudsoncountyview.com/jersey-city-cutting-via-weekday-hours-saturday-service-claims-4m-savings/"),
 "S20": ("Via / BusinessWire: TCATA selects Via (turnkey network, ops from Apr 1, 2026)", "https://www.businesswire.com/news/home/20260122315817/en/TCATA-Selects-Via-to-Modernize-and-Revitalize-the-Twin-Cities-Public-Transit-Network"),
 "S21": ("Q1 2026 earnings call: four network deals >$40M ACV YTD 2026", "https://www.fool.com/earnings/call-transcripts/2026/05/12/via-via-q1-2026-earnings-call-transcript/"),
 "S22": ("Citizen Portal: Garner NC 60-day feasibility contract with Via", "https://citizenportal.ai/articles/8927043/north-carolina/wake-county/garner/garner-to-study-microtransit-with-60day-feasibility-contract-with-via"),
 "S23": ("Chronicle-Telegram: Lorain County ViaLC extension ($2.2M, through Jul 2026)", "https://chroniclet.com/news/435879/lorain-county-to-continue-vialc-microtransit-program-in-lorain-elyria-into-2026/"),
 "S24": ("LA Metro board report 2024-0989 (Nomad Transit IDIQ)", "https://datamade-metro-pdf-merger.s3.amazonaws.com/2024-0989.pdf"),
 "S25": ("UK Contracts Finder: TfL Dial-a-Ride software, £2,307,950, Dec 2022–Dec 2027", "https://www.contractsfinder.service.gov.uk/Notice/eba395d5-84f0-449e-8e22-be61afd32fe4"),
 "S27": ("People Newspapers: University Park approves Via agreement: paratransit $67.75/veh-hr, microtransit $64.52/veh-hr (Apr 21, 2026)", "https://www.peoplenewspapers.com/news/2026/04/up-city-council-approves-paratransit-contract/"),
 "S28": ("Plano agenda memo: purchased via 791 Cooperative Contract No. 791202505008", "https://plano.novusagenda.com/agendapublic/CoverSheet.aspx?ItemID=10595&MeetingID=3668"),
 "S29": ("Via 10-K FY2025, G&A definition: includes insurance expenses and customer support costs", "https://www.sec.gov/Archives/edgar/data/1603015/000160301526000008/via-20251231.htm"),
 "S30": ("Via Q2'26 press release: adjusted gross profit reconciliation", "https://www.sec.gov/Archives/edgar/data/1603015/000160301526000027/viaq226pressrelease.htm"),
 "S31": ("Search extract citing Douglas County: Link On Demand costs ~$70/hr to operate", "https://www.castlerocknewspress.net/news/article_00161854-4419-43e6-a43d-43dd24d19169.html"),
 "S32": ("Bleecker exhibits 'Illustrative TaaS Unit Economics' and 'TaaS vs SaaS Mix Analysis' (images in report)", "https://www.bleeckerstreetresearch.com/research/via"),
 "S33": ("Colorado Politics: DougCo Feb 2026 $4.4M contract to continue/expand Link On Demand (Lone Tree, Highlands Ranch, Parker)", "https://www.coloradopolitics.com/2026/07/14/dougco-approves-2m-rideshare-expansion-to-castle-rock/"),
 "S34": ("Bloomberg BST consensus projections (user-provided file, model/Consensus_Projections_BBG.xlsx)", ""),
 "S35": ("stockanalysis.com VIA statistics: mkt cap $2.41B, EV $2.09B, 81.51M shares, short interest 9.87% of float, 7.98 days to cover", "https://stockanalysis.com/stocks/via/statistics/"),
 "S36": ("Bloomberg RV screen (BICS Best Fit comps), user screenshot, Sep 2026", ""),
 "S26": ("User research notes (VIA_1.pdf): Arlington, DCTA, King County, Mobile, New Braunfels, Miami-Dade, Gastonia, Passaic, Q4'25 Texas example", ""),
}

# ================= Sheet 1: Summary =================
ws = wb.active; ws.title = "Summary"
ws.column_dimensions["A"].width = 62; ws.column_dimensions["B"].width = 14; ws.column_dimensions["C"].width = 74
put(ws, "A1", "VIA: software vs. services revenue mix", T)
put(ws, "A2", "All $ in millions. Blue = hardcoded input; black = formula; green = link to another sheet. Yellow = key assumption to flex.", Font(name=F, italic=True, size=9))
def block(r0, title, rows):
    put(ws, f"A{r0}", title, H); r = r0 + 1
    for lab, f, fmt, note in rows:
        put(ws, f"A{r}", lab); put(ws, f"B{r}", f, GRN, fmt); c = put(ws, f"C{r}", note, Font(name=F, size=9)); c.alignment = WRAP; r += 1
    return r + 1
r = block(4, "1) Bleecker's method, replicated and updated (task 2)", [
 ("Bleecker as published (Q3'25 adj GM 40%, TaaS GM 26.2%, SaaS 75%)", "='Bleecker_Replication'!C22", PCT, "(75 − 40)/(75 − 26.2) = 71.7%, which they round to 72%. Their 72% is a margin back-out, not a sum of contract dollars."),
 ("Bleecker's own inputs, arithmetic corrected", "='Bleecker_Replication'!D22", PCT, "Their 80/20 weighting of 27.1% (micro) and 37.5% (para) gives 29.2%, not 26.2%. 26.2% = 80%×27.1% + 20%×22.9%, which looks like a cell-reference slip."),
 ("UPDATED: 2026 contract pricing, TTM adj GM (base case)", "='Bleecker_Replication'!E22", PCT, "Micro $/hr = avg of 2026 rates (Douglas Co. $70, University Park $64.52); para $67.75 (University Park); costs +3% since Dec-25."),
 ("Updated, at Q2'26 adj GM instead of TTM", "='Bleecker_Replication'!E25", PCT, "Mgmt says Q2'26 GM was boosted by one-time revenue and will revert."),
 ("Updated, paratransit at 30% of hours (2026 wins bundle ADA paratransit)", "='Bleecker_Replication'!E26", PCT, "Plano, Addison, Highland Park and University Park all include paratransit."),
 ("Check: software GM implied by the reported cost split at the updated mix", "='Bleecker_Replication'!E32", PCT, "Should land near the 75% assumption. It does, so the updated mix is internally consistent."),
])
r = block(r, "2) Mix implied by the reported cost split (task 1, Q2'26)", [
 ("Tech-enabled services cost / revenue", "='Margin_Decomp'!I22", PCT, "Floor on the services share if services earn a 0% gross margin."),
 ("Services share at base-case services GM (Margin_Decomp!C5)", "='Margin_Decomp'!I16", PCT, "Base 22% services GM, half of launch & support staff counted as services."),
 ("Implied software GM at base case", "='Margin_Decomp'!I19", PCT, "Plausibility check (vertical SaaS typically 70–85%)."),
 ("Services GM needed to reproduce 72%", "='Margin_Decomp'!I25", PCT, "~25%. Bleecker's own estimate is 26.2%."),
 ("Your formula (gS − g)/(gS − gV) at 80% / 25%", "='Blended_Formula'!C8", PCT, "Q2'26 reported GAAP GM."),
])
r = block(r, "3) Cross-check: Bleecker 72% + incremental contract ACV (not their method)", [
 ("Scenario A: + identified public contracts", "='ACV_CrossCheck'!D24", PCT, "All priced new wins are turnkey (~96% services)."),
 ("Scenario B: A + mgmt's 4 network deals (>$40M ACV)", "='ACV_CrossCheck'!D33", PCT, ""),
])
put(ws, f"A{r}", "Read-across", H); r += 1
notes = [
 "• Bleecker's 72% is a gross-margin back-out: services share = (SaaS GM − blended GM)/(SaaS GM − TaaS GM). The contracts feed the TaaS unit economics ($/hr prices, cost/hr); they aren't summed.",
 "• Their published TaaS GM (26.2%) doesn't match their own inputs (29.2%). Corrected, their method gives ~76% services, more services-heavy than they reported.",
 "• 2026 contract pricing: microtransit ~$64.50–70/hr (above Bleecker's $60); paratransit $67.75/hr (well below their $90). Net, the updated mix is ~73–76% services. It moves most with the blended GM (TTM vs Q2'26) and the paratransit share of hours.",
 "• Via's FY2025 10-K confirms Bleecker's accounting point: G&A 'includes customer support costs as well as ... insurance expenses', so reported gross margin excludes both.",
 "• Services cost has risen from 49.7% of revenue (FY24) to ~51–52% (FY25–Q2'26). The financials show no shift toward software yet.",
]
for n in notes:
    c = put(ws, f"A{r}", n); ws.merge_cells(f"A{r}:C{r}"); c.alignment = WRAP; ws.row_dimensions[r].height = 40; r += 1
# ================= Sheet 2: Bleecker_Replication =================
br = wb.create_sheet("Bleecker_Replication")
br.column_dimensions["A"].width = 3; br.column_dimensions["B"].width = 52
for col in "CDE": br.column_dimensions[col].width = 16
br.column_dimensions["F"].width = 70
put(br, "B1", "Bleecker's TaaS-vs-SaaS mix method, replicated and updated", T)
put(br, "B2", "Services (TaaS) share = (SaaS GM − blended adj. GM) / (SaaS GM − TaaS GM). TaaS GM comes from hourly unit economics: contract $/hr price minus driver, vehicle, ops-support and field-manager cost per hour, weighted across microtransit and paratransit hours.", Font(name=F, italic=True, size=9))
br.merge_cells("B2:F2"); br["B2"].alignment = WRAP; br.row_dimensions[2].height = 30
hdr(br, 4, ["", "Input / output", "Bleecker as published (Dec-25)", "Bleecker inputs, arithmetic corrected", "UPDATED: 2026 contracts", "Note / source"], 1)
MR = f"'Contracts'!$I$5:$I$60"; MT = f"'Contracts'!$J$5:$J$60"; MW = f"'Contracts'!$E$5:$E$60"
rows = [
 (5, "Microtransit price ($/veh-hr)", 60.0, "=C5", f'=AVERAGEIFS({MR},{MT},"Micro",{MW},"Post")', USD, "Bleecker: $60 illustrative (OMNIA catalog midpoint $66.95). Updated = avg of 2026 rates in Contracts (Douglas Co. $70; University Park $64.52)."),
 (6, "Paratransit price ($/veh-hr)", 90.0, "=C6", f'=AVERAGEIFS({MR},{MT},"Para",{MW},"Post")', USD, "Bleecker: $90 illustrative (OMNIA midpoint $82.40). Updated = University Park 2026: $67.75."),
 (7, "Cost/hr inflation since Dec-25", 0.0, 0.0, 0.03, PCT, "3% matches the annual escalator in Via's own contract example (Q4'25 call). Covers driver wage pressure."),
 (8, "Micro: driver labor $/hr", 20.50, "=C8", "=C8*(1+$E$7)", USD, "Bleecker exhibit ('livable wage' contract clauses)."),
 (9, "Micro: vehicle lease/maint $/hr", 10.75, "=C9", "=C9*(1+$E$7)", USD, ""),
 (10, "Micro: project ops support $/hr", 8.00, "=C10", "=C10*(1+$E$7)", USD, "Monitoring, project mgmt, IT hosting, dispatch."),
 (11, "Micro: field manager $/hr", 4.50, "=C11", "=C11*(1+$E$7)", USD, ""),
 (12, "Para: driver labor $/hr", 26.50, "=C12", "=C12*(1+$E$7)", USD, ""),
 (13, "Para: vehicle lease/maint $/hr", 13.50, "=C13", "=C13*(1+$E$7)", USD, ""),
 (14, "Para: project ops support $/hr", 11.75, "=C14", "=C14*(1+$E$7)", USD, ""),
 (15, "Para: field manager $/hr", 4.50, "=C15", "=C15*(1+$E$7)", USD, ""),
 (16, "Microtransit GM (GAAP basis, pre-insurance)", "=(C5-SUM(C8:C11))/C5", "=(D5-SUM(D8:D11))/D5", "=(E5-SUM(E8:E11))/E5", PCT, "Bleecker: 27.1%."),
 (17, "Paratransit GM", "=(C6-SUM(C12:C15))/C6", "=(D6-SUM(D12:D15))/D6", "=(E6-SUM(E12:E15))/E6", PCT, "Bleecker: 37.5%. At 2026 pricing, paratransit is Via's thinnest-margin service."),
 (18, "Microtransit share of hours", 0.80, "=C18", 0.80, PCT, "Bleecker: 80/20 per experts. Flex in row 26: 2026 wins bundle ADA paratransit."),
 (19, "TaaS GM (hours-weighted)", 0.262, "=D18*D16+(1-D18)*D17", "=E18*E16+(1-E18)*E17", PCT, "C19 = Bleecker's published 26.2%. Their inputs give 29.2%; 26.2% = 80%×27.1% + 20%×22.9% (micro after insurance), an apparent slip."),
 (20, "SaaS GM (assumption)", 0.75, "=C20", 0.75, PCT, "Bleecker assumption. Checked against the reported cost split in row 32."),
 (21, "Blended adjusted GM", 0.40, "=C21", "='Margin_Inputs'!D25", PCT, "Bleecker: Q3'25 adj GM rounded to 40.0% (actual 39.6%). Updated: TTM to Q2'26 adj GM."),
 (22, "SERVICES (TaaS) SHARE OF REVENUE", "=(C20-C21)/(C20-C19)", "=(D20-D21)/(D20-D19)", "=(E20-E21)/(E20-E19)", PCT, "Bleecker published: 72%."),
 (23, "Software (SaaS) share", "=1-C22", "=1-D22", "=1-E22", PCT, ""),
]
for rr, lab, c, d, e, fmt, note in rows:
    put(br, f"B{rr}", lab, B if rr in (19, 22) else BLK)
    for col, v in (("C", c), ("D", d), ("E", e)):
        isf = isinstance(v, str) and v.startswith("=")
        fnt = (GRN if "!" in v else BLK) if isf else BLUE
        fill = YEL if (col == "E" and rr in (7, 18, 20)) else None
        put(br, f"{col}{rr}", v, fnt, fmt, fill)
    c_ = put(br, f"F{rr}", note, Font(name=F, size=9)); c_.alignment = WRAP
for col in "CDE": br[f"{col}22"].fill = PatternFill("solid", fgColor="E2EFDA")
put(br, "B25", "Updated, at Q2'26 adj GM (instead of TTM)")
put(br, "D25", "='Margin_Inputs'!D24", GRN, PCT); put(br, "E25", "=(E20-D25)/(E20-E19)", BLK, PCT)
put(br, "B26", "Updated, paratransit = 30% of hours")
put(br, "D26", "=0.7*E16+0.3*E17", BLK, PCT); put(br, "E26", "=(E20-E21)/(E20-D26)", BLK, PCT)
put(br, "F25", "D = blended GM used; E = services share.", Font(name=F, size=9)); put(br, "F26", "D = TaaS GM at 70/30; E = services share.", Font(name=F, size=9))

put(br, "B28", "Cross-check vs reported cost split (TTM to Q2'26, GAAP)", H)
REV = "SUM('Margin_Inputs'!B7:B8,'Margin_Inputs'!B10:B11)"
put(br, "B29", "Implied services cost, % of revenue (E22 × (1 − E19))"); put(br, "E29", "=E22*(1-E19)", BLK, PCT)
put(br, "B30", "Reported tech-enabled services cost, % of revenue"); put(br, "E30", f"=SUM('Margin_Inputs'!C7:C8,'Margin_Inputs'!C10:C11)/{REV}", GRN, PCT)
put(br, "B31", "Reported tech-enabled + launch & support, % of revenue"); put(br, "E31", f"=(SUM('Margin_Inputs'!C7:C8,'Margin_Inputs'!C10:C11)+SUM('Margin_Inputs'!D7:D8,'Margin_Inputs'!D10:D11))/{REV}", GRN, PCT)
put(br, "B32", "Implied software GM = 1 − (total COGS% − E29)/(1 − E22)"); put(br, "E32", f"=1-(SUM('Margin_Inputs'!F7:F8,'Margin_Inputs'!F10:F11)/{REV}-E29)/(1-E22)", GRN, PCT)
put(br, "F29", "Should fall between rows 30 and 31: services cost = tech-enabled cost plus part of launch & support.", Font(name=F, size=9))
put(br, "F32", "Close to the 75% SaaS assumption means the updated mix is consistent with reported COGS.", Font(name=F, size=9))

put(br, "B35", "Sensitivity (updated column): services share vs microtransit $/hr and paratransit share of hours", H)
put(br, "B36", "Micro $/hr \\ para share", B)
paras = [0.10, 0.20, 0.30, 0.40]; prices = [60, 64.52, 67.26, 70, 75]
for j, p in enumerate(paras): put(br, f"{'CDEF'[j]}36", p, BLUE, PCT)
for i, pr in enumerate(prices):
    rr = 37 + i; put(br, f"B{rr}", pr, BLUE, USD)
    for j in range(4):
        c = "CDEF"[j]
        tg = f"((1-{c}$36)*(($B{rr}-SUM($E$8:$E$11))/$B{rr})+{c}$36*$E$17)"
        put(br, f"{c}{rr}", f"=($E$20-$E$21)/($E$20-{tg})", BLK, PCT)
put(br, "B43", "Sensitivity: services share vs SaaS GM (rows) and blended adj GM (cols), updated TaaS GM", H)
put(br, "B44", "SaaS GM \\ blended GM", B)
gms = [0.39, 0.40, 0.4025, 0.415]
for j, g in enumerate(gms): put(br, f"{'CDEF'[j]}44", g, BLUE, PCT)
for i, sg in enumerate([0.70, 0.75, 0.80, 0.85]):
    rr = 45 + i; put(br, f"B{rr}", sg, BLUE, PCT)
    for j in range(4):
        c = "CDEF"[j]; put(br, f"{c}{rr}", f"=($B{rr}-{c}$44)/($B{rr}-$E$19)", BLK, PCT)
# ================= Sheet 2: Margin_Inputs =================
mi = wb.create_sheet("Margin_Inputs")
for col, w in zip("ABCDEFGHI", [14, 13, 16, 16, 13, 13, 13, 11, 70]): mi.column_dimensions[col].width = w
put(mi, "A1", "Reported revenue and cost-of-revenue split ($mm, GAAP)", T)
put(mi, "A2", "Via splits cost of revenue into: technology-enabled services (drivers, vehicles, fleet mgmt, call center), launch & support personnel, IT & other (hosting, amortization).", Font(name=F, italic=True, size=9))
hdr(mi, 4, ["Period", "Revenue", "Tech-enabled services cost", "Launch & support personnel", "IT & other", "Total COGS", "Gross profit", "GM %", "Source / note"])
data = [
 ("FY2024", 337.6, 167.7, 24.3, 14.8, "S-1/A: FY24 revenue $337.6M; cost split $167.7 / $24.3 / $14.8M (total $206.8M)."),
 ("H1 2025", 205.775, 105.0, 12.3, 6.7, "Q3'25 10-Q: 6M revenue = GP $81.761M + COGS $124.014M; cost split $105.0 / $12.3 / $6.7M."),
 ("Q3 2025", 109.653, 57.1, 6.3, 3.2, "Q3'25 10-Q: revenue $109.653M, GP $43.086M; cost split $57.1 / $6.3 / $3.2M."),
 ("Q4 2025", None, None, None, None, "Derived: FY2025 − H1 2025 − Q3 2025."),
 ("FY2025", 434.337, 223.5, 25.8, 13.3, "10-K FY25: revenue $434.337M; cost split $223.5 / $25.8 / $13.3M."),
 ("Q1 2026", 127.43, 66.8, 7.3, 3.3, "Q1'26 10-Q: revenue $127.43M; COGS $77.4M; GP $50.1M."),
 ("Q2 2026", 135.7, 69.8, 6.9, 3.4, "Q2'26 10-Q: COGS $80.1M, GP $55.6M (so revenue = $135.7M)."),
]
for i, (p, rev, tes, lsp, it, note) in enumerate(data):
    r = 5 + i
    put(mi, f"A{r}", p, B)
    if p == "Q4 2025":
        for col in "BCDE":
            put(mi, f"{col}{r}", f"={col}9-{col}6-{col}7", BLK, USD)
    else:
        for col, v in zip("BCDE", [rev, tes, lsp, it]): put(mi, f"{col}{r}", v, BLUE, USD)
    put(mi, f"F{r}", f"=C{r}+D{r}+E{r}", BLK, USD)
    put(mi, f"G{r}", f"=B{r}-F{r}", BLK, USD)
    put(mi, f"H{r}", f"=IF(B{r}=0,0,G{r}/B{r})", BLK, PCT)
    c = put(mi, f"I{r}", note, Font(name=F, size=9)); c.alignment = WRAP
put(mi, "A13", "Check: Q2'26 COGS", B); put(mi, "B13", 80.1, BLUE, USD); put(mi, "C13", "=F11-B13", BLK, USD); put(mi, "D13", "← should be ~0 (rounding)", Font(name=F, size=9))
put(mi, "A14", "Check: Q1'26 COGS", B); put(mi, "B14", 77.4, BLUE, USD); put(mi, "C14", "=F10-B14", BLK, USD)
put(mi, "A15", "Check: Q3'25 COGS", B); put(mi, "B15", 66.567, BLUE, USD); put(mi, "C15", "=F7-B15", BLK, USD)
put(mi, "A19", "Adjusted gross profit (non-GAAP, from press-release reconciliations)", H)
hdr(mi, 20, ["Period", "Revenue", "Adj. gross profit", "Adj. GM %", "", "", "", "", "Source / note"])
adj = [("Q3 2025", "=B7", 43.471, "Q3'25 PR reconciliation."), ("Q4 2025", "=B8", 47.404, "Q4'25 PR: adj GP $47,404K."),
       ("Q1 2026", "=B10", 50.725, "Derived: 6M'26 adj GP $107.022M − Q2'26 $56.297M."), ("Q2 2026", "=B11", 56.297, "Q2'26 PR: adj GP $56,297K.")]
for i,(p,rf,v,n) in enumerate(adj):
    r=21+i; put(mi,f"A{r}",p,B); put(mi,f"B{r}",rf,BLK,USD); put(mi,f"C{r}",v,BLUE,USD); put(mi,f"D{r}",f"=C{r}/B{r}",BLK,PCT); put(mi,f"I{r}",n,Font(name=F,size=9))
put(mi,"A25","TTM to Q2'26",B); put(mi,"B25","=SUM(B21:B24)",BLK,USD); put(mi,"C25","=SUM(C21:C24)",BLK,USD); put(mi,"D25","=C25/B25",BLK,PCT)
put(mi,"I25","Base-case blended GM for the Bleecker update. Mgmt says Q2'26 was boosted by one-time revenue that will revert.",Font(name=F,size=9))
put(mi, "A17", "Adjusted GM (non-GAAP, excludes SBC and acquired-intangible amortization) is within ~0.5pt of GAAP (e.g. Q3'25 adj. GP $43.471M vs GAAP $43.086M), so GAAP is used throughout. Mgmt: Q2'26 adj. GM 41%, LT target 50%.", Font(name=F, size=9))
mi.merge_cells("A17:I17"); mi["A17"].alignment = WRAP; mi.row_dimensions[17].height = 28

# ================= Sheet 3: Margin_Decomp =================
md = wb.create_sheet("Margin_Decomp")
md.column_dimensions["A"].width = 3; md.column_dimensions["B"].width = 58
for col in "CDEFGHI": md.column_dimensions[col].width = 12
put(md, "B1", "Backing out the mix from the cost-of-revenue split", T)
put(md, "B2", "Services revenue = services cost / (1 − services GM). Software revenue = revenue − services revenue. Implied software GM follows. If implied software GM comes out implausible, the services GM assumption is wrong.", Font(name=F, italic=True, size=9))
md.merge_cells("B2:I2"); md["B2"].alignment = WRAP; md.row_dimensions[2].height = 30
put(md, "B4", "Assumptions", H)
put(md, "B5", "Services gross margin (gV)"); put(md, "C5", 0.22, BLUE, PCT, YEL)
md["C5"].comment = Comment("Base case 22%. Contract transit operators typically run low-teens to ~20% gross margins. Via's routing software should lift utilization, so it's set slightly above that.", "model")
put(md, "B6", "Share of launch & support personnel allocated to services (α)"); put(md, "C6", 0.5, BLUE, PCT, YEL)
md["C6"].comment = Comment("Per the 10-K, launch & support personnel covers local ops staff and field managers doing implementation AND ongoing operations support. 50% is a split-the-difference assumption.", "model")
put(md, "B7", "Insurance outside COGS, % of revenue (Bleecker claim)"); put(md, "C7", 0.0, BLUE, PCT, YEL)
md["C7"].comment = Comment("CONFIRMED in the FY2025 10-K: G&A includes insurance expenses and customer support costs (not cost of revenue). Bleecker estimates insurance at ~3–4pts of GM. Set to 3.5% to test.", "model")
put(md, "B8", "Bleecker services share (target to reconcile)"); put(md, "C8", 0.72, BLUE, PCT)

hdr(md, 10, ["", "Line", "FY2024", "H1 2025", "Q3 2025", "Q4 2025", "FY2025", "Q1 2026", "Q2 2026"], 1)
lines = [
 (11, "Revenue", "='Margin_Inputs'!B{r}", GRN, USD),
 (12, "Tech-enabled services cost", "='Margin_Inputs'!C{r}", GRN, USD),
 (13, "Services cost incl. α·LSP + insurance", "={c}12+$C$6*'Margin_Inputs'!D{r}+$C$7*{c}11", BLK, USD),
 (14, "Software cost = IT&other + (1−α)·LSP", "='Margin_Inputs'!E{r}+(1-$C$6)*'Margin_Inputs'!D{r}", BLK, USD),
 (15, "Implied services revenue", "={c}13/(1-$C$5)", BLK, USD),
 (16, "Services share of revenue", "=IF({c}11=0,0,{c}15/{c}11)", BLK, PCT),
 (17, "Implied software revenue", "={c}11-{c}15", BLK, USD),
 (18, "Software share of revenue", "=1-{c}16", BLK, PCT),
 (19, "Implied software GM", "=IF({c}17<=0,0,({c}17-{c}14)/{c}17)", BLK, PCT),
 (20, "Blended GM (check vs reported)", "=({c}11-{c}13-{c}14)/{c}11+$C$7", BLK, PCT),
 (22, "Services cost intensity: tech-enabled cost / revenue (0%-margin floor)", "={c}12/{c}11", BLK, PCT),
 (23, "Services share if services GM = 15%", "=({c}13/(1-0.15))/{c}11", BLK, PCT),
 (24, "Services share if services GM = 30%", "=({c}13/(1-0.30))/{c}11", BLK, PCT),
 (25, "Services GM required to hit Bleecker share", "=1-{c}13/($C$8*{c}11)", BLK, PCT),
 (26, "…and the software GM that implies", "=({c}11*(1-$C$8)-{c}14)/({c}11*(1-$C$8))", BLK, PCT),
]
cols = "CDEFGHI"; mrows = [5, 6, 7, 8, 9, 10, 11]
for rr, lab, f, font, fmt in lines:
    put(md, f"B{rr}", lab, B if rr in (16, 19, 22, 25) else BLK)
    for c, mr in zip(cols, mrows):
        put(md, f"{c}{rr}", f.format(c=c, r=mr), font, fmt)
put(md, "B27", "Row 20 should equal the reported GM on Margin_Inputs (insurance is added back because it's being moved into COGS only for the mix calculation).", Font(name=F, size=9))

# Sensitivity grid Q2 2026
put(md, "B30", "Sensitivity (Q2 2026): services share of revenue", H)
put(md, "B31", "rows = services GM; cols = α (share of launch & support in services)", Font(name=F, size=9))
alphas = [0, 0.5, 1.0]; gvs = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35]
put(md, "B32", "gV \\ α", B)
for j, a in enumerate(alphas): put(md, f"{cols[j]}32", a, BLUE, PCT)
for i, g in enumerate(gvs):
    rr = 33 + i; put(md, f"B{rr}", g, BLUE, PCT)
    for j in range(3):
        c = cols[j]
        put(md, f"{c}{rr}", f"=(('Margin_Inputs'!$C$11+{c}$32*'Margin_Inputs'!$D$11+$C$7*'Margin_Inputs'!$B$11)/(1-$B{rr}))/'Margin_Inputs'!$B$11", BLK, PCT)
put(md, "B40", "Sensitivity (Q2 2026): implied software GM", H)
put(md, "B41", "gV \\ α", B)
for j, a in enumerate(alphas): put(md, f"{cols[j]}41", a, BLUE, PCT)
for i, g in enumerate(gvs):
    rr = 42 + i; put(md, f"B{rr}", g, BLUE, PCT)
    for j in range(3):
        c = cols[j]; sr = 33 + i
        sw_rev = f"('Margin_Inputs'!$B$11*(1-{c}{sr}))"
        sw_cost = f"('Margin_Inputs'!$E$11+(1-{c}$41)*'Margin_Inputs'!$D$11)"
        put(md, f"{c}{rr}", f"=IF({sw_rev}<=0,0,({sw_rev}-{sw_cost})/{sw_rev})", BLK, PCT)

# ================= Sheet 4: Blended_Formula =================
bf = wb.create_sheet("Blended_Formula")
bf.column_dimensions["A"].width = 3; bf.column_dimensions["B"].width = 44
for col in "CDEFG": bf.column_dimensions[col].width = 12
put(bf, "B1", "Your formula: services share = (gS − g) / (gS − gV)", T)
put(bf, "B3", "Blended GM used (g)"); put(bf, "C3", "='Margin_Inputs'!H11", GRN, PCT)
put(bf, "D3", "← Q2'26 reported. Overwrite with 0.393 for Q1'26/Q3'25.", Font(name=F, size=9))
put(bf, "B4", "Software GM (gS)"); put(bf, "C4", 0.80, BLUE, PCT, YEL)
put(bf, "B5", "Services GM (gV)"); put(bf, "C5", 0.25, BLUE, PCT, YEL)
put(bf, "B6", "LT target blended GM (mgmt)"); put(bf, "C6", 0.50, BLUE, PCT)
put(bf, "B8", "Services share at inputs above", B); put(bf, "C8", "=(C4-C3)/(C4-C5)", BLK, PCT)
put(bf, "B9", "Services share needed for 50% GM at same gS/gV", B); put(bf, "C9", "=(C4-C6)/(C4-C5)", BLK, PCT)
put(bf, "B10", "…or services GM needed for 50% at today's mix", B); put(bf, "C10", "=(C6-(1-C8)*C4)/C8", BLK, PCT)
put(bf, "B12", "Grid: services share (rows = gS, cols = gV), at blended g in C3", H)
put(bf, "B13", "gS \\ gV", B)
gvl = [0.15, 0.20, 0.25, 0.30, 0.35]
for j, g in enumerate(gvl): put(bf, f"{'CDEFG'[j]}13", g, BLUE, PCT)
for i, gs in enumerate([0.70, 0.75, 0.80, 0.85]):
    rr = 14 + i; put(bf, f"B{rr}", gs, BLUE, PCT)
    for j in range(5):
        c = "CDEFG"[j]; put(bf, f"{c}{rr}", f"=($B{rr}-$C$3)/($B{rr}-{c}$13)", BLK, PCT)
put(bf, "B19", "Limitation: blended GM alone can't separate a high services share at good margins from a lower share at poor margins. Margin_Decomp adds the second equation (the reported cost split), which pins down the trade-off.", Font(name=F, size=9))
bf.merge_cells("B19:G19"); bf["B19"].alignment = WRAP; bf.row_dimensions[19].height = 40

# ================= Contracts =================
ct = wb.create_sheet("Contracts")
heads = ["#", "Agency / customer", "Via entity", "Approved / effective", "Window", "Scope", "Total value ($mm)", "Term (months)", "Hourly rate ($/veh-hr)", "Rate type", "Annualized value ($mm)", "Software % of value", "Software $ (annual)", "Services $ (annual)", "Line-item basis", "Include in ACV update (1/0)", "Possible network deal (1/0)", "Notes", "Source"]
widths = [4, 30, 18, 14, 9, 14, 11, 9, 10, 9, 12, 10, 11, 11, 12, 10, 10, 60, 8]
for i, w in enumerate(widths): ct.column_dimensions[L(i + 1)].width = w
put(ct, "A1", "Contract tracker: Bleecker reference set (pre-Dec 16, 2025) + contracts since", T)
put(ct, "A2", "Hourly rate + rate type (Micro/Para) on 'Post' rows feed Bleecker_Replication (updated $/hr). Software % 'Assumed' links to ACV_CrossCheck!C8. 'Include' = 1 only for post-window contracts with a public $ value that were actually approved and are additive.", Font(name=F, italic=True, size=9))
ct.merge_cells("A2:S2"); ct["A2"].alignment = WRAP; ct.row_dimensions[2].height = 28
hdr(ct, 4, heads)
TK = "='ACV_CrossCheck'!$C$8"
C = [
 ("LA Metro – Metro Micro ops (North+South)", "Nomad Transit LLC", "2024-11-21", "Pre", "Turnkey", 135.0, 72, 82.35, "", 0.0, "Actual", 0, 0, "IDIQ, 3+3 yrs; $82.35→$94.50/rev-hr on 253,003 hrs. Software went to Spare Labs; Via kept operations only.", "S24,S26"),
 ("Arlington, TX – On-Demand", "Via", "2024-12", "Pre", "Turnkey", 20.7, 24, None, "", 0.04, "Actual", 0, 0, "Ceiling cut 31% from $30.2M. TaaS ~96% of value; software <5% (Bleecker).", "S8,S26"),
 ("DCTA GoZone (2023–24 extension)", "Via", "2023", "Pre", "Turnkey", 10.46, 12, 42.11, "", 0.0, "Actual", 0, 0, "234,895 van hrs @ ~$42.11/hr + customer service $283.5K per 6 months.", "S26"),
 ("King County Metro – Metro Flex", "Via", "2023-02", "Pre", "Turnkey", 21.0, 36, None, "", TK, "Assumed", 0, 0, "~$7M/yr, 3-yr term.", "S26"),
 ("Mobile, AL – The Wave (full system)", "Port City Transit LLC", "2025-09-16", "Pre", "Turnkey", 36.3, 36, None, "", TK, "Assumed", 0, 1, "$12.1M/yr; takeover from Transdev. Network deal.", "S26"),
 ("New Braunfels, TX", "River North Transit LLC", "2025-10-13", "Pre", "Turnkey", 6.08, 60, None, "", TK, "Assumed", 0, 0, "$1.15–1.29M/yr; ARPA-funded yr 1.", "S26"),
 ("Miami-Dade", "River North Transit LLC", "2020", "Pre", "Turnkey", 4.66, 36, None, "", TK, "Assumed", 0, 0, "", "S26"),
 ("Lorain County, OH – ViaLC extension", "River North Transit LLC", "2025-07", "Pre", "Turnkey", 2.2, 12, None, "", TK, "Assumed", 0, 0, "Through Jul 2026. Jan 2026 $2.8M federal expansion grant (grant, not contract).", "S23"),
 ("Gastonia, NC", "River North Transit LLC", "2024", "Pre", "Turnkey", 1.65, 12, None, "", TK, "Assumed", 0, 0, "", "S26"),
 ("Q4'25 call example – Texas customer", "Via", "2025", "Pre", "Turnkey", 3.4, 36, 50.0, "", 0.0044, "Actual", 0, 0, "22,000 veh-hrs/yr @ $50/hr; $15K implementation; 3% annual escalator.", "S26"),
 ("OMNIA co-op catalog – microtransit (pricing reference)", "Via", "2025-05", "Pre", "Pricing ref", 0, 12, 66.95, "", 0.0, "Actual", 0, 0, "Midpoint TaaS fee per vehicle-hour (Bleecker exhibit).", "S8"),
 ("OMNIA co-op catalog – paratransit (pricing reference)", "Via", "2025-05", "Pre", "Pricing ref", 0, 12, 82.40, "", 0.0, "Actual", 0, 0, "Midpoint paratransit fee per vehicle-hour (Bleecker exhibit).", "S8"),
 ("Transport for London – Dial-a-Ride (software)", "Via Technologies B.V.", "2022-08-05", "Pre", "Software-only", 2.93, 60, None, "", 1.0, "Actual", 0, 0, "£2,307,950 over 5 yrs (~$1.27/£).", "S25"),
 # ---- post-window ----
 ("TCATA (Benton Harbor / St. Joseph, MI)", "Via", "2025-12 (ops 2026-04-01)", "Post", "Turnkey (network)", 0, 12, None, "", TK, "Assumed", 0, 1, "Full network takeover; $ value not found.", "S20"),
 ("Plano, TX – Plano Rides", "Via Transportation Inc.", "2026-02-23", "Post", "Turnkey", 3.952247, 6, None, "", TK, "Assumed", 1, 1, "$3,952,247 for 6 months; ~$8M/yr renewals. Bought through 791 Cooperative Contract 791202505008 (same vehicle as the Dallas-area deals).", "S11,S28"),
 ("Douglas County, CO – Link On Demand (Lone Tree/Highlands Ranch/Parker)", "River North Transit LLC", "2026-02", "Post", "Turnkey", 4.4, 12, None, "", TK, "Assumed", 0, 0, "$4.4M to continue and expand service east into Parker. Mostly a renewal of existing service, so not added to ACV.", "S33"),
 ("Addison, TX – Addison Orbit", "Via Transportation Inc.", "2026-03-24", "Post", "Turnkey", 0.872231, 6, None, "", TK, "Assumed", 1, 0, "NTE $872,231, 6-month pilot, micro + ADA paratransit.", "S12"),
 ("NJ TRANSIT MicroLink – Bergen", "Via", "2026-04-06", "Post", "Turnkey", 0, 24, None, "", TK, "Assumed", 0, 0, "Via operates; value not found.", "S15"),
 ("NJ TRANSIT MicroLink – Monmouth", "Via", "2026-04-06", "Post", "Software-only", 0, 24, None, "", 1.0, "Actual", 0, 0, "NJT operates on Via software. The only software-only new deal found.", "S15"),
 ("Highland Park, TX – On-Demand", "Via", "2026-04 (launch 5/14)", "Post", "Turnkey", 1.55, 6, None, "", TK, "Assumed", 1, 0, "$1.55M FY26 budget amendment for 6-month pilot (4 vehicles + paratransit).", "S13"),
 ("University Park, TX – paratransit", "Via", "2026-04-21", "Post", "Turnkey", 1.06, 12, 67.75, "Para", TK, "Assumed", 0, 0, "Approved 4/21 at $67.75 per vehicle-hr; CANCELLED after the DART vote. Excluded from ACV, but the rate is used as 2026 pricing evidence.", "S27,S14"),
 ("University Park, TX – microtransit option", "Via", "2026-04-21", "Post", "Pricing ref", 0, 12, 64.52, "Micro", 0.0, "Actual", 0, 0, "Quoted microtransit rate $64.52 per vehicle-hr (not exercised). Pricing evidence only.", "S27"),
 ("Union County, NJ", "River North Transit LLC", "2026-06", "Post", "Turnkey", 0, 12, None, "", TK, "Assumed", 0, 0, "Turnkey pilot; value not disclosed.", "S16"),
 ("Douglas County, CO – Link On Demand Castle Rock", "River North Transit LLC", "2026-07-14", "Post", "Turnkey", 1.99172, 12, 70.0, "Micro", TK, "Assumed", 1, 0, "$1,991,720 initial scope; ~$70/hr operating cost per county (search extract).", "S17,S31"),
 ("Cobb County, GA – microtransit expansion", "Via", "2026-09 (consent agenda)", "Post", "Turnkey", 6.3, 24, None, "", TK, "Assumed", 1, 0, "$6.3M: Acworth/Kennesaw (2 yrs) + Mableton (1 yr); Via paid a fixed cost. Existing south Cobb pilot ~$1.1M/yr.", "S18"),
 ("Jersey City, NJ – Via service cut", "Via", "2026-07-01", "Post", "Reduction", -4.0, 12, None, "", 0.0, "Assumed", 1, 0, "Hours roughly halved, Saturday service ended: ~$4M/yr.", "S19"),
 ("Garner, NC – feasibility study", "Via", "2026", "Post", "Consulting (one-time)", 0, 2, None, "", 1.0, "Assumed", 0, 0, "60-day feasibility contract.", "S22"),
]
M2 = '$#,##0.00;($#,##0.00);-'
for i, row in enumerate(C):
    r = 5 + i
    (name, ent, dt, win, scope, tcv, term, rate, rtype, swp, basis, inc, net, note, src) = row
    put(ct, f"A{r}", i + 1)
    put(ct, f"B{r}", name); put(ct, f"C{r}", ent); put(ct, f"D{r}", dt, BLUE); put(ct, f"E{r}", win, BLUE); put(ct, f"F{r}", scope, BLUE)
    put(ct, f"G{r}", tcv, BLUE, M2); put(ct, f"H{r}", term, BLUE, '0')
    if rate is not None: put(ct, f"I{r}", rate, BLUE, M2)
    if rtype: put(ct, f"J{r}", rtype, BLUE)
    put(ct, f"K{r}", f"=IF(H{r}=0,0,G{r}/H{r}*12)", BLK, M2)
    if isinstance(swp, str): put(ct, f"L{r}", swp, GRN, PCT)
    else: put(ct, f"L{r}", swp, BLUE, PCT)
    put(ct, f"M{r}", f"=K{r}*L{r}", BLK, M2)
    put(ct, f"N{r}", f"=K{r}-M{r}", BLK, M2)
    put(ct, f"O{r}", basis); put(ct, f"P{r}", inc, BLUE, '0'); put(ct, f"Q{r}", net, BLUE, '0')
    c = put(ct, f"R{r}", note, Font(name=F, size=9)); c.alignment = WRAP
    put(ct, f"S{r}", src, Font(name=F, size=9))
    ct.row_dimensions[r].height = 36
last = 4 + len(C)
tr = last + 2
put(ct, f"B{tr}", "Avg hourly rate, 2026 contracts – microtransit", B); put(ct, f"I{tr}", f'=AVERAGEIFS(I5:I{last},J5:J{last},"Micro",E5:E{last},"Post")', BLK, M2)
put(ct, f"B{tr+1}", "Avg hourly rate, 2026 contracts – paratransit", B); put(ct, f"I{tr+1}", f'=AVERAGEIFS(I5:I{last},J5:J{last},"Para",E5:E{last},"Post")', BLK, M2)
put(ct, f"B{tr+2}", "Pre-window turnkey reference set: $-weighted services share", B)
put(ct, f"K{tr+2}", f'=SUMIFS(N5:N{last},E5:E{last},"Pre",F5:F{last},"Turnkey")/SUMIFS(K5:K{last},E5:E{last},"Pre",F5:F{last},"Turnkey")', BLK, PCT)
ct.freeze_panes = "C5"
CT_LAST = last
# ================= Sheet 6: Updated_Mix =================
um = wb.create_sheet("ACV_CrossCheck")
um.column_dimensions["A"].width = 3; um.column_dimensions["B"].width = 62
for col in "CDEF": um.column_dimensions[col].width = 14
put(um, "B1", "Cross-check: Bleecker 72% baseline + incremental contract ACV (NOT Bleecker's method)", T)
put(um, "B3", "1) Baseline (Bleecker, Dec 16, 2025)", H)
put(um, "B4", "Run-rate revenue base at Bleecker date: Q4'25 ARR ($mm)"); put(um, "C4", 476, BLUE, USD)
um["C4"].comment = Comment("Q4 2025 Annual Run-Rate Revenue $476M (4x Q4 revenue). Source: Q4/FY25 press release.", "model")
put(um, "B5", "Also: FY2025 revenue ($mm), for reference"); put(um, "C5", "='Margin_Inputs'!B9", GRN, USD)
put(um, "B6", "Bleecker services share"); put(um, "C6", 0.72, BLUE, PCT, YEL)
put(um, "B7", "Baseline services $ / software $"); put(um, "C7", "=C4*C6", BLK, USD); put(um, "D7", "=C4-C7", BLK, USD)
put(um, "B8", "Turnkey contracts: software % of contract value (Bleecker exhibit: 1.9–4.6% on OMNIA pricing)"); put(um, "C8", 0.04, BLUE, PCT, YEL)
um["C8"].comment = Comment("Arlington TX: software <5%, TaaS ~96% (Bleecker). Texas Q4'25 example: 0.44%. LA Metro: 0% (unbundled). 4% is the high end, which is generous to software.", "model")

rng = lambda col: f"'Contracts'!{col}5:{col}{CT_LAST}"
put(um, "B10", "2) Scenario A: add identified public contracts (Include = 1)", H)
hdr(um, 11, ["", "Item", "Services $", "Software $", "Total $"], 1)
put(um, "B12", "Baseline"); put(um, "C12", "=C7", BLK, USD); put(um, "D12", "=D7", BLK, USD); put(um, "E12", "=C12+D12", BLK, USD)
put(um, "B13", "New turnkey wins (annualized)")
put(um, "C13", f'=SUMIFS({rng("N")},{rng("P")},1,{rng("F")},"<>Reduction")', GRN, USD)
put(um, "D13", f'=SUMIFS({rng("M")},{rng("P")},1,{rng("F")},"<>Reduction")', GRN, USD)
put(um, "E13", "=C13+D13", BLK, USD)
put(um, "B14", "Reductions (Jersey City)")
put(um, "C14", f'=SUMIFS({rng("N")},{rng("P")},1,{rng("F")},"Reduction")', GRN, USD)
put(um, "D14", f'=SUMIFS({rng("M")},{rng("P")},1,{rng("F")},"Reduction")', GRN, USD)
put(um, "E14", "=C14+D14", BLK, USD)
put(um, "B15", "Updated total", B); put(um, "C15", "=SUM(C12:C14)", BLK, USD); put(um, "D15", "=SUM(D12:D14)", BLK, USD); put(um, "E15", "=C15+D15", BLK, USD)
put(um, "B17", "New-contract-only services share (flow, excl. reductions)"); put(um, "D17", "=IF(E13=0,0,C13/E13)", BLK, PCT)
put(um, "B18", "Net new ACV identified ($mm)"); put(um, "D18", "=E13+E14", BLK, USD)
put(um, "B24", "Scenario A: updated services share", B); put(um, "D24", "=C15/E15", BLK, PCT)
put(um, "B25", "Change vs Bleecker (pts)"); put(um, "D25", "=D24-C6", BLK, '+0.0%;-0.0%;0.0%')

put(um, "B27", "3) Scenario B: A, but replace possible network deals with mgmt's disclosed total", H)
put(um, "B28", "Mgmt: 4 network deals won in 2026, >$40M total ACV (Q1'26 call)"); put(um, "C28", 40, BLUE, USD)
put(um, "B29", "Network deals software % (turnkey)"); put(um, "C29", "=C8", BLK, PCT)
put(um, "B30", "Identified A contracts NOT flagged as possible network ($)")
put(um, "C30", f'=SUMIFS({rng("N")},{rng("P")},1,{rng("Q")},0)', GRN, USD)
put(um, "D30", f'=SUMIFS({rng("M")},{rng("P")},1,{rng("Q")},0)', GRN, USD)
put(um, "B31", "Network deals")
put(um, "C31", "=C28*(1-C29)", BLK, USD); put(um, "D31", "=C28*C29", BLK, USD)
put(um, "B32", "Updated total (baseline + rows 30–31)", B)
put(um, "C32", "=C12+C30+C31", BLK, USD); put(um, "D32", "=D12+D30+D31", BLK, USD); put(um, "E32", "=C32+D32", BLK, USD)
put(um, "B33", "Scenario B: updated services share", B); put(um, "D33", "=C32/E32", BLK, PCT)

put(um, "B36", "4) Scenario C: roll forward to latest run-rate (Q2'26 ARR)", H)
put(um, "B37", "Q2'26 ARR ($mm)"); put(um, "C37", 543, BLUE, USD)
put(um, "B38", "Growth since baseline explained by Scenario B adds"); put(um, "C38", "=E32-C4", BLK, USD)
put(um, "B39", "Residual (organic expansion, unlisted wins, Downtowner, FX)"); put(um, "C39", "=C37-E32", BLK, USD)
put(um, "B40", "Services share assumed on residual"); put(um, "C40", 0.72, BLUE, PCT, YEL)
um["C40"].comment = Comment("About 2/3 of growth comes from existing customers (mgmt), mostly added vehicle-hours per Bleecker. Downtowner (acquired 12/12/25, $40.7M) is a turnkey destination-city operator. Set lower if you think software-only logos drive the residual.", "model")
put(um, "B41", "Note: part of Scenario B ACV hasn't launched yet (mgmt: H2 launches), so C38 can exceed what's in Q2 ARR. If the residual is negative, treat C as an upper bound.", Font(name=F, size=9))
put(um, "B42", "Rolled-forward services $ / software $")
put(um, "C42", "=C32+C39*C40", BLK, USD); put(um, "D42", "=D32+C39*(1-C40)", BLK, USD); put(um, "E42", "=C42+D42", BLK, USD)
put(um, "B44", "Scenario C: services share at Q2'26 run-rate", B); put(um, "D44", "=C42/E42", BLK, PCT)

put(um, "B47", "5) Cross-check against the financials (Q2 2026)", H)
put(um, "B48", "Financial-implied services share at base services GM"); put(um, "D48", "='Margin_Decomp'!I16", GRN, PCT)
put(um, "B49", "Services GM needed to match Scenario A share")
put(um, "D49", "=1-'Margin_Decomp'!I13/(D24*'Margin_Decomp'!I11)", BLK, PCT)
put(um, "B50", "Software GM implied at that point")
put(um, "D50", "=('Margin_Decomp'!I11*(1-D24)-'Margin_Decomp'!I14)/('Margin_Decomp'!I11*(1-D24))", BLK, PCT)
put(um, "B51", "Services GM needed to match Scenario B share")
put(um, "D51", "=1-'Margin_Decomp'!I13/(D33*'Margin_Decomp'!I11)", BLK, PCT)

put(um, "B54", "6) Implied customer economics at Bleecker-style mix (Q2'26)", H)
put(um, "B55", "Customers (Q2'26)"); put(um, "C55", 847, BLUE, '#,##0')
put(um, "B56", "Share of customers buying services (mgmt: ~20%)"); put(um, "C56", 0.20, BLUE, PCT)
put(um, "B57", "Avg services ACV per turnkey customer ($mm)"); put(um, "C57", "=C37*D44/(C55*C56)", BLK, '$#,##0.00')
put(um, "B58", "Avg software ACV per customer, all customers ($mm)"); put(um, "C58", "=C37*(1-D44)/C55", BLK, '$#,##0.00')
put(um, "B59", "Sanity check vs benchmarks: TfL Dial-a-Ride software ~$0.59M/yr; LA Metro's Spare software $0.45M; Arlington software ~4% of $10.4M ≈ $0.4M.", Font(name=F, size=9))

# ================= Consensus_Check =================
cc = wb.create_sheet("Consensus_Check")
cc.column_dimensions["A"].width = 3; cc.column_dimensions["B"].width = 50
for i in range(3, 16): cc.column_dimensions[L(i)].width = 10
put(cc, "B1", "What consensus already assumes (Bloomberg BST, user-provided file)", T)
put(cc, "B2", "Source: model/Consensus_Projections_BBG.xlsx (Bloomberg, as provided). $mm. Q3'25–Q2'26 actual, Q3'26–Q4'27 consensus.", Font(name=F, italic=True, size=9))
qs = ["Q3'25A","Q4'25A","Q1'26A","Q2'26A","Q3'26E","Q4'26E","Q1'27E","Q2'27E","Q3'27E","Q4'27E"]
hdr(cc, 4, [""] + ["Line"] + qs + ["", "FY26E", "FY27E"], 1)
data = {
 "Revenue": [109.653,118.909,127.434,135.707,138,150.5556,156.6667,167.4444,169.1111,181.5556],
 "Gross profit": [43.086,46.953,50.055,55.606,54.7256,60.2660,63.1311,68.0971,69.1450,75.0060],
 "Total opex (GAAP, incl. SBC)": [61.977,71.344,73.639,77.36,75.8772,76.1139,76.7026,78.2679,78.3161,81.6391],
 "  of which G&A": [21.189,27.615,28.621,30.11,29.1743,29.3484,29.3128,29.7220,29.7493,30.5597],
 "Stock-based compensation": [6.592,14.396,15.564,16.01,15.5808,16.1594,15.9350,16.1104,16.2258,16.5433],
 "Adjusted EBITDA": [-8.692,-7.384,-5.809,-0.003441,-4.0322,2.4098,3.4154,6.9811,7.79,11.2567],
 "Insurance payables (BS)": [15.751,15.144,14.882,15.329,14.9242,18.1774,18.3044,20.1841,20.0667,22.0113],
 "Acquisitions, net of cash (CF)": [0,-39.892,0,0.279,-7.515,-14.157,-15,-15,-7.505,-16.3677],
}
r = 5
rowmap = {}
for lab, vals in data.items():
    put(cc, f"B{r}", lab, B if lab in ("Revenue", "Adjusted EBITDA") else BLK)
    for j, v in enumerate(vals): put(cc, f"{L(3+j)}{r}", v, BLUE, USD)
    if lab != "Insurance payables (BS)":
        put(cc, f"N{r}", f"=SUM(E{r}:H{r})", BLK, USD); put(cc, f"O{r}", f"=SUM(I{r}:L{r})", BLK, USD)
    rowmap[lab] = r; r += 1
R, GP, OX, GA, SBC, EB = (rowmap[k] for k in ["Revenue","Gross profit","Total opex (GAAP, incl. SBC)","  of which G&A","Stock-based compensation","Adjusted EBITDA"])
cc["M4"].value = None
put(cc, "N4", "FY26E", B); put(cc, "O4", "FY27E", B)
r += 1
put(cc, f"B{r}", "Derived", H); r += 1
der = [
 ("Revenue growth YoY", lambda c, i: f"=IF({i}<4,0,{c}{R}/{L(3+i-4)}{R}-1)" if False else None),
]
# explicit derived rows
put(cc, f"B{r}", "Gross margin"); 
for j in range(10): c = L(3+j); put(cc, f"{c}{r}", f"={c}{GP}/{c}{R}", BLK, PCT)
put(cc, f"N{r}", f"=N{GP}/N{R}", BLK, PCT); put(cc, f"O{r}", f"=O{GP}/O{R}", BLK, PCT); GMr = r; r += 1
put(cc, f"B{r}", "Opex / revenue")
for j in range(10): c = L(3+j); put(cc, f"{c}{r}", f"={c}{OX}/{c}{R}", BLK, PCT)
put(cc, f"N{r}", f"=N{OX}/N{R}", BLK, PCT); put(cc, f"O{r}", f"=O{OX}/O{R}", BLK, PCT); r += 1
put(cc, f"B{r}", "Adj. EBITDA margin")
for j in range(10): c = L(3+j); put(cc, f"{c}{r}", f"={c}{EB}/{c}{R}", BLK, PCT)
put(cc, f"N{r}", f"=N{EB}/N{R}", BLK, PCT); put(cc, f"O{r}", f"=O{EB}/O{R}", BLK, PCT); r += 1
put(cc, f"B{r}", "Revenue QoQ growth")
for j in range(1, 10): c = L(3+j); p = L(2+j); put(cc, f"{c}{r}", f"={c}{R}/{p}{R}-1", BLK, PCT)
r += 1
put(cc, f"B{r}", "FY27E vs FY26E growth: revenue / opex / G&A", B)
put(cc, f"C{r}", f"=O{R}/N{R}-1", BLK, PCT); put(cc, f"D{r}", f"=O{OX}/N{OX}-1", BLK, PCT); put(cc, f"E{r}", f"=O{GA}/N{GA}-1", BLK, PCT); GRr = r; r += 2

put(cc, f"B{r}", "Test: can G&A stay flat if insurance sits in G&A?", H); r += 1
put(cc, f"B{r}", "Insurance expense as % of revenue (Bleecker est. 3–4pts of GM)"); put(cc, f"C{r}", 0.035, BLUE, PCT, YEL); ins = r; r += 1
put(cc, f"B{r}", "Incremental insurance FY27E vs FY26E ($mm)"); put(cc, f"C{r}", f"=C{ins}*(O{R}-N{R})", BLK, USD); insd = r; r += 1
put(cc, f"B{r}", "Consensus total G&A increase FY27E vs FY26E ($mm)"); put(cc, f"C{r}", f"=O{GA}-N{GA}", BLK, USD); gad = r; r += 1
put(cc, f"B{r}", "Insurance growth as % of consensus G&A growth", B); put(cc, f"C{r}", f"=IF(C{gad}=0,0,C{insd}/C{gad})", BLK, PCT); r += 1
put(cc, f"B{r}", "Customer support costs also sit in G&A (10-K) and scale with rides/hours; not quantified here.", Font(name=F, size=9)); r += 2

put(cc, f"B{r}", "Valuation at current price", H); r += 1
put(cc, f"B{r}", "Share price ($)"); put(cc, f"C{r}", 28.37, BLUE, '$#,##0.00', YEL); px = r
put(cc, f"D{r}", "Bloomberg, Sep 2026 close (user screenshot). BBG: mkt cap $2.31B, EV $1.99B.", Font(name=F, size=9)); r += 1
put(cc, f"B{r}", "Shares outstanding (mm, basic; ties to BBG mkt cap)"); put(cc, f"C{r}", 81.51, BLUE, '#,##0.0'); sh = r; r += 1
put(cc, f"B{r}", "Cash, Q2'26 ($mm; no debt)"); put(cc, f"C{r}", 336.0, BLUE, USD); cash = r; r += 1
put(cc, f"B{r}", "Enterprise value ($mm)", B); put(cc, f"C{r}", f"=C{px}*C{sh}-C{cash}", BLK, USD); ev = r; r += 1
put(cc, f"B{r}", "EV / revenue FY26E | FY27E"); put(cc, f"C{r}", f"=C{ev}/N{R}", BLK, '0.0x'); put(cc, f"D{r}", f"=C{ev}/O{R}", BLK, '0.0x'); r += 1
put(cc, f"B{r}", "EV / gross profit FY26E | FY27E"); put(cc, f"C{r}", f"=C{ev}/N{GP}", BLK, '0.0x'); put(cc, f"D{r}", f"=C{ev}/O{GP}", BLK, '0.0x'); r += 1
put(cc, f"B{r}", "EV / adj. EBITDA FY27E"); put(cc, f"C{r}", f"=C{ev}/O{EB}", BLK, '0.0x'); r += 2

put(cc, f"B{r}", "Illustrative sum-of-the-parts on FY27E gross profit (multiples are placeholders: source comps)", H); r += 1
put(cc, f"B{r}", "Services share of revenue (Bleecker_Replication updated)"); put(cc, f"C{r}", "='Bleecker_Replication'!E22", GRN, PCT); ss = r; r += 1
put(cc, f"B{r}", "Services GM | software GM"); put(cc, f"C{r}", "='Bleecker_Replication'!E19", GRN, PCT); put(cc, f"D{r}", "='Bleecker_Replication'!E20", GRN, PCT); gms_ = r; r += 1
put(cc, f"B{r}", "FY27E services GP | software GP ($mm)")
put(cc, f"C{r}", f"=O{R}*C{ss}*C{gms_}/(C{ss}*C{gms_}+(1-C{ss})*D{gms_})*O{GMr}/O{GMr}*O{GP}/O{R}/(C{ss}*C{gms_}+(1-C{ss})*D{gms_})*(C{ss}*C{gms_}+(1-C{ss})*D{gms_})", BLK, USD)
cc[f"C{r}"].value = f"=O{GP}*(C{ss}*C{gms_})/(C{ss}*C{gms_}+(1-C{ss})*D{gms_})"
put(cc, f"D{r}", f"=O{GP}-C{r}", BLK, USD); gp2 = r; r += 1
put(cc, f"B{r}", "EV / GP multiple: services | software"); put(cc, f"C{r}", 3.0, BLUE, '0.0x', YEL); put(cc, f"D{r}", 10.0, BLUE, '0.0x', YEL); mult = r
put(cc, f"E{r}", "Placeholders. Justify with comps (outsourced transport operators vs vertical SaaS).", Font(name=F, size=9)); r += 1
put(cc, f"B{r}", "Implied EV ($mm)"); put(cc, f"C{r}", f"=C{gp2}*C{mult}+D{gp2}*D{mult}", BLK, USD); iev = r; r += 1
put(cc, f"B{r}", "Implied price per share ($)", B); put(cc, f"C{r}", f"=(C{iev}+C{cash})/C{sh}", BLK, '$#,##0.00'); ip = r; r += 1
put(cc, f"B{r}", "Upside / (downside) vs current", B); put(cc, f"C{r}", f"=C{ip}/C{px}-1", BLK, '+0.0%;-0.0%'); r += 1
put(cc, f"B{r}", "Blended EV/GP multiple the market pays today (FY27E)"); put(cc, f"C{r}", f"=C{ev}/O{GP}", BLK, '0.0x'); r += 1
put(cc, f"B{r}", "Software multiple needed to justify today's price, at services multiple above"); put(cc, f"C{r}", f"=(C{ev}-C{gp2}*C{mult})/D{gp2}", BLK, '0.0x')

# ================= Comps_BBG =================
cb = wb.create_sheet("Comps_BBG")
cb.column_dimensions["A"].width = 3; cb.column_dimensions["B"].width = 34
for col in "CDEFGHIJ": cb.column_dimensions[col].width = 12
put(cb, "B1", "Bloomberg RV: 'BICS Best Fit' comps (VIA classified 100% Application Software)", T)
put(cb, "B2", "Source: Bloomberg RV screen, user screenshot, price $28.37 (Sep 2026). '--' = not meaningful (negative). FY1 = 2026, FY2 = 2027.", Font(name=F, italic=True, size=9))
hdr(cb, 4, ["", "Name", "Mkt cap ($B)", "EV ($B)", "EV/EBITDA LTM", "EV/EBITDA FY1", "EV/EBITDA FY2", "P/E FY1", "P/E FY2", "P/FCF"], 1)
rows = [
 ("LiveRamp", 2.28, 1.94, 15.17, 8.48, 7.16, 13.06, 10.88, 11.96),
 ("Ethos Technologies", 2.31, 2.14, None, 17.58, 12.50, None, 22.86, None),
 ("DoubleVerify", 2.08, 1.98, 10.79, 7.16, 6.66, 27.18, 21.14, 13.22),
 ("Privia Health", 2.49, 2.14, 37.55, 14.03, 12.29, 27.56, 21.87, 18.21),
 ("Neutron Holdings", 1.84, 1.98, None, 7.18, 5.93, 6.79, 21.39, None),
 ("Vertex Inc", 1.91, 2.03, 17.67, 9.75, 7.91, 14.38, 11.60, 26.35),
 ("ACV Auctions", 1.77, 1.74, 123.93, 23.14, 17.23, 68.30, 57.42, None),
 ("Pagaya Technologies", 1.73, 2.31, 5.06, 4.90, 4.13, 6.62, 5.71, 5.49),
 ("SoundHound AI", 2.75, 2.56, None, None, None, None, None, None),
 ("Progress Software", 1.67, 2.89, 8.76, 7.15, 7.15, 6.60, 6.45, 5.64),
]
for i, rw in enumerate(rows):
    r = 5 + i; put(cb, f"B{r}", rw[0])
    for j, v in enumerate(rw[1:]):
        if v is not None: put(cb, f"{'CDEFGHIJ'[j]}{r}", v, BLUE, '0.00' if j > 1 else '0.00')
last = 4 + len(rows)
mr = last + 1
put(cb, f"B{mr}", "Comp median", B)
for col in "CDEFGHIJ": put(cb, f"{col}{mr}", f"=MEDIAN({col}5:{col}{last})", BLK, '0.00')
vr = mr + 1
put(cb, f"B{vr}", "VIA (Bloomberg)", B)
for col, v in zip("CDEFGHIJ", [2.31, 1.99, None, None, 69.64, None, 67.87, None]):
    if v is not None: put(cb, f"{col}{vr}", v, BLUE, '0.00')
put(cb, f"B{vr+1}", "VIA premium to median (x)", B)
put(cb, f"G{vr+1}", f"=G{vr}/G{mr}", BLK, '0.0x'); put(cb, f"I{vr+1}", f"=I{vr}/I{mr}", BLK, '0.0x')
put(cb, f"B{vr+2}", "Blended forward P/E (chart): VIA 96.6x vs comps avg 30.6x", Font(name=F, size=9))
r = vr + 4
put(cb, f"B{r}", "Read-across", H); r += 1
for n in [
 "• Bloomberg's own classification puts VIA 100% in Application Software. Screens and quant peer sets benchmark it against software, even though ~75% of revenue is services.",
 "• These 'peers' are a grab-bag (ad-tech, health services, auctions, fintech). Use this to show how the market labels VIA, not as the valuation comp set.",
 "• EV/EBITDA on near-breakeven EBITDA exaggerates the premium. Anchor valuation on EV/GP and EV/Sales (Consensus_Check) with separate software and services comp sets.",
 "• The chart shows VIA's forward P/E expanding from ~50x to ~97x from late July into September, around the Q2 print (Aug 6), while comps held ~30x. Mgmt says the Q2 margin beat came from one-time revenue that will revert.",
]:
    c = put(cb, f"B{r}", n); cb.merge_cells(f"B{r}:J{r}"); c.alignment = WRAP; cb.row_dimensions[r].height = 30; r += 1

# ================= Revenue_Build =================
rb = wb.create_sheet("Revenue_Build")
rb.column_dimensions["A"].width = 3; rb.column_dimensions["B"].width = 52
for i in range(3, 14): rb.column_dimensions[L(i)].width = 10
rb.column_dimensions["N"].width = 60
put(rb, "B1", "Revenue build and operating model by revenue stream", T)
put(rb, "B2", "Four streams with different economics: software, microtransit/paratransit services (hours × $/hr), network deals (contract value launched), one-time. FY25 actual; FY26 matched to consensus; FY27–30 driven by inputs; FY31–35 growth fades linearly to terminal growth.", Font(name=F, italic=True, size=9))
rb.merge_cells("B2:N2"); rb["B2"].alignment = WRAP; rb.row_dimensions[2].height = 30
put(rb, "B4", "SCENARIO: 1 = Short case, 2 = Bull (matches consensus FY26–27)", B); put(rb, "D4", 1, BLUE, '0', YEL)
YRS = ["FY25A","FY26E","FY27E","FY28E","FY29E","FY30E","FY31E","FY32E","FY33E","FY34E","FY35E"]
COLS = [L(3+i) for i in range(11)]  # C..M
hdr(rb, 6, ["", "($mm)"] + YRS + ["Notes"], 1)
put(rb, "B7", "Consensus revenue (BBG)"); put(rb, "C7", 434.337, BLUE, USD); put(rb, "D7", 551.697, BLUE, USD); put(rb, "E7", 674.778, BLUE, USD)
put(rb, "B8", "Consensus adj. EBITDA (BBG)"); put(rb, "C8", -32.4, BLUE, USD); put(rb, "D8", -7.435, BLUE, USD); put(rb, "E8", 29.443, BLUE, USD)
put(rb, "N8", "FY25A from company (adj. EBITDA ≈ −$32M); FY26–27 Bloomberg consensus.", Font(name=F, size=9))

put(rb, "B10", "DRIVERS (Short / Bull input rows; 'Live' row feeds the model)", H)
DRV = [
 ("Software revenue growth", [0.18,0.12,0.11,0.10,0.09], [0.18,0.16,0.15,0.14,0.13], PCT, "FY26 incl. Downtowner. Software ≈ customers × revenue per customer; organic customer growth ~9%."),
 ("Hours: expansion at existing customers", [None,0.12,0.11,0.10,0.10], [None,0.13,0.13,0.12,0.12], PCT, "10-K: expansion with existing customers drives most growth."),
 ("Hours: new customers", [None,0.04,0.04,0.04,0.04], [None,0.04,0.04,0.04,0.04], PCT, "Organic logo growth ~9% but new logos start small."),
 ("Hours: downsell / budget cuts / churn", [None,-0.08,-0.07,-0.06,-0.06], [None,-0.03,-0.03,-0.03,-0.03], PCT, "Short: funding tightens 2027 (stopgap, ARPA end). Jersey City −50%, Arlington −31%."),
 ("Price escalator ($/hr)", [None,0.03,0.03,0.03,0.03], [None,0.03,0.03,0.03,0.03], PCT, "3% annual escalator in Via's Q4'25 example contract."),
 ("Network: contract value launched ($mm)", [35,30,30,30,30], [35,40,45,50,55], USD, "2026 wins >$40M + Rochester $14.6M, mostly launching H2'26–27. ~$10–15M per deal."),
 ("Network: rebid loss (% of opening run-rate)", [0,0,0,0.05,0.05], [0,0,0,0,0], PCT, "5-yr terms: first rebids ~2029 (Sioux Falls through 2028)."),
 ("One-time revenue (% of total)", [0.03]*5, [0.03]*5, PCT, "3% in FY24 and FY25 (10-K)."),
 ("Software gross margin", [0.75]*5, [0.75]*5, PCT, "Bleecker assumption; reported cost split implies ~73%."),
 ("Microtransit/paratransit gross margin", [0.293]*5, [0.293,0.303,0.313,0.323,0.333], PCT, "Bleecker_Replication updated TaaS GM. Bull: +1pt/yr from AI/routing."),
 ("Network gross margin", [0.20]*5, [0.25,0.26,0.27,0.28,0.29], PCT, "ASSUMPTION (undisclosed). Short: bus-operator economics. CFO: 'some accretive, some less.'"),
 ("One-time gross margin", [0.75]*5, [0.75]*5, PCT, "High-margin implementation/consulting."),
 ("Hour-driven opex (% of services revenue)", [0.065]*5, [0.065,0.065,0.06,0.055,0.05], PCT, "Insurance (~3.5%, Bleecker) + customer support (~3%, Bleecker unit economics), both in G&A (10-K). Bull: AI cuts support."),
 ("Fixed opex growth (R&D, S&M, corporate)", [None,0.04,0.04,0.04,0.04], [None,0.03,0.03,0.03,0.03], PCT, "Consensus total opex +3.9% FY27."),
]
live = {}
r = 11
for name, s, bvals, fmt, note in DRV:
    put(rb, f"B{r}", name, B)
    put(rb, f"B{r+1}", "   Short"); put(rb, f"B{r+2}", "   Bull"); put(rb, f"B{r+3}", "   Live")
    for j in range(5):
        c = COLS[1+j]
        if s[j] is not None: put(rb, f"{c}{r+1}", s[j], BLUE, fmt)
        if bvals[j] is not None: put(rb, f"{c}{r+2}", bvals[j], BLUE, fmt)
        if s[j] is not None or bvals[j] is not None:
            put(rb, f"{c}{r+3}", f"=IF($D$4=1,{c}{r+1},{c}{r+2})", BLK, fmt)
    for c in COLS[6:]:  # FY31-35 hold FY30 value
        put(rb, f"{c}{r+3}", f"=$H{r+3}", BLK, fmt)
    cc_ = put(rb, f"N{r}", note, Font(name=F, size=9)); cc_.alignment = WRAP
    live[name] = r + 3
    r += 4
LV = lambda n: live[n]
g_sw, h_exp, h_new, h_dn, h_px = LV("Software revenue growth"), LV("Hours: expansion at existing customers"), LV("Hours: new customers"), LV("Hours: downsell / budget cuts / churn"), LV("Price escalator ($/hr)")
n_acv, n_loss, ot_pct = LV("Network: contract value launched ($mm)"), LV("Network: rebid loss (% of opening run-rate)"), LV("One-time revenue (% of total)")
gm_sw, gm_mp, gm_nw, gm_ot = LV("Software gross margin"), LV("Microtransit/paratransit gross margin"), LV("Network gross margin"), LV("One-time gross margin")
vo_pct, fx_g = LV("Hour-driven opex (% of services revenue)"), LV("Fixed opex growth (R&D, S&M, corporate)")

r += 1
put(rb, f"B{r}", "Terminal growth (from DCF tab)"); put(rb, f"D{r}", "='DCF'!C9", GRN, PCT); TG = f"$D${r}"; r += 1
put(rb, f"B{r}", "Network opening run-rate FY26 ($mm)"); put(rb, f"D{r}", 25, BLUE, USD, YEL)
put(rb, f"N{r}", "Estimate: Mobile $12.1M + Sioux Falls + Twin Cities (MI). Sioux Falls value/structure unverified.", Font(name=F, size=9)); NOPEN = f"$D${r}"; r += 1
put(rb, f"B{r}", "Blended $/vehicle-hour FY25 (for implied hours)"); put(rb, f"D{r}", 60, BLUE, USD)
put(rb, f"N{r}", "Illustrative: 2026 rates $64.5–70 micro, $67.75 para; legacy lower ($42–50).", Font(name=F, size=9)); PX0 = f"$D${r}"; r += 2

put(rb, f"B{r}", "REVENUE", H); r += 1
R_SW = r; put(rb, f"B{r}", "Software"); put(rb, f"C{r}", 101.1, BLUE, USD)
put(rb, f"N{r}", "FY25 est: 24% of recurring revenue (services ~76%).", Font(name=F, size=9)); r += 1
R_MP = r; put(rb, f"B{r}", "Microtransit / paratransit services (hours × $/hr)"); r += 1
R_NW = r; put(rb, f"B{r}", "Network deals"); put(rb, f"C{r}", 13.0, BLUE, USD)
put(rb, f"N{r}", "FY25 est: Sioux Falls + Mobile Q4.", Font(name=F, size=9)); r += 1
R_REC = r; put(rb, f"B{r}", "Recurring subtotal", B); r += 1
R_OT = r; put(rb, f"B{r}", "One-time (implementation, consulting)"); r += 1
R_TOT = r; put(rb, f"B{r}", "TOTAL REVENUE", B); r += 1
R_GR = r; put(rb, f"B{r}", "   growth"); r += 1
R_VC = r; put(rb, f"B{r}", "   vs consensus"); r += 1
R_SS = r; put(rb, f"B{r}", "   Services share (micro/para + network)"); r += 1
R_PX = r; put(rb, f"B{r}", "   Blended $/vehicle-hour"); r += 1
R_HR = r; put(rb, f"B{r}", "   Implied micro/para vehicle-hours (mm)"); r += 1
r += 1
put(rb, f"B{r}", "Network detail", B); r += 1
R_NO = r; put(rb, f"B{r}", "   Opening run-rate"); r += 1
R_NN = r; put(rb, f"B{r}", "   Opening after escalator and rebid losses"); r += 1
R_NL = r; put(rb, f"B{r}", "   Launched in year (links driver)"); r += 1
R_NC = r; put(rb, f"B{r}", "   Closing run-rate"); r += 1
r += 1
put(rb, f"B{r}", "GROSS PROFIT", H); r += 1
R_GSW, R_GMP, R_GNW, R_GOT = r, r+1, r+2, r+3
for k, lab in enumerate(["Software", "Microtransit / paratransit", "Network", "One-time"]): put(rb, f"B{r+k}", lab)
r += 4
R_GP = r; put(rb, f"B{r}", "TOTAL GROSS PROFIT", B); r += 1
R_GM = r; put(rb, f"B{r}", "   Gross margin"); r += 1
R_GMC = r; put(rb, f"B{r}", "   Consensus gross margin"); put(rb, f"D{r}", 0.40, BLUE, PCT); put(rb, f"E{r}", 0.408, BLUE, PCT); r += 2
put(rb, f"B{r}", "OPERATING COSTS (adjusted: ex-SBC, ex-D&A)", H); r += 1
R_VO = r; put(rb, f"B{r}", "Hour-driven (insurance, support): % × services revenue"); r += 1
R_FO = r; put(rb, f"B{r}", "Fixed (R&D, S&M, corporate); FY26 matched to consensus EBITDA"); r += 1
R_OX = r; put(rb, f"B{r}", "Total adjusted opex", B); r += 1
R_OXP = r; put(rb, f"B{r}", "   % of revenue"); r += 1
R_EB = r; put(rb, f"B{r}", "ADJUSTED EBITDA", B); r += 1
R_EBM = r; put(rb, f"B{r}", "   margin"); r += 1
R_EBC = r; put(rb, f"B{r}", "   vs consensus ($mm)"); r += 1

for i, c in enumerate(COLS):
    p = COLS[i-1] if i > 0 else None
    k = i - 5  # fade step for FY31+ (i=6 -> 1)
    # software
    if i == 0: pass
    elif i <= 5: put(rb, f"{c}{R_SW}", f"={p}{R_SW}*(1+{c}{g_sw})", BLK, USD)
    else: put(rb, f"{c}{R_SW}", f"={p}{R_SW}*(1+$H${g_sw}+({TG}-$H${g_sw})*{k}/5)", BLK, USD)
    # network detail + revenue
    if i == 1:
        put(rb, f"{c}{R_NO}", f"={NOPEN}", GRN, USD); put(rb, f"{c}{R_NN}", f"={c}{R_NO}", BLK, USD)
    elif 2 <= i <= 5:
        put(rb, f"{c}{R_NO}", f"={p}{R_NC}", BLK, USD)
        put(rb, f"{c}{R_NN}", f"={c}{R_NO}*(1+{c}{h_px})*(1-{c}{n_loss})", BLK, USD)
    if 1 <= i <= 5:
        put(rb, f"{c}{R_NL}", f"={c}{n_acv}", BLK, USD)
        put(rb, f"{c}{R_NC}", f"={c}{R_NN}+{c}{R_NL}", BLK, USD)
        put(rb, f"{c}{R_NW}", f"={c}{R_NN}+0.5*{c}{R_NL}", BLK, USD)
    elif i >= 6:
        put(rb, f"{c}{R_NW}", f"={p}{R_NW}*(1+($H${R_NW}/$G${R_NW}-1)+({TG}-($H${R_NW}/$G${R_NW}-1))*{k}/5)", BLK, USD)
    # micro/para
    if i == 0:
        put(rb, f"{c}{R_MP}", f"={c}7*(1-0.03)-{c}{R_SW}-{c}{R_NW}", BLK, USD)
    elif i == 1:
        put(rb, f"{c}{R_MP}", f"={c}7*(1-{c}{ot_pct})-{c}{R_SW}-{c}{R_NW}", BLK, USD)
    elif i <= 5:
        put(rb, f"{c}{R_MP}", f"={p}{R_MP}*(1+{c}{h_exp}+{c}{h_new}+{c}{h_dn})*(1+{c}{h_px})", BLK, USD)
    else:
        put(rb, f"{c}{R_MP}", f"={p}{R_MP}*(1+($H${R_MP}/$G${R_MP}-1)+({TG}-($H${R_MP}/$G${R_MP}-1))*{k}/5)", BLK, USD)
    put(rb, f"{c}{R_REC}", f"={c}{R_SW}+{c}{R_MP}+{c}{R_NW}", BLK, USD)
    if i == 0:
        put(rb, f"{c}{R_OT}", f"={c}7*0.03", BLK, USD); put(rb, f"{c}{R_TOT}", f"={c}7", GRN, USD)
    elif i == 1:
        put(rb, f"{c}{R_OT}", f"={c}7*{c}{ot_pct}", BLK, USD); put(rb, f"{c}{R_TOT}", f"={c}7", GRN, USD)
    else:
        put(rb, f"{c}{R_OT}", f"={c}{R_REC}*{c}{ot_pct}/(1-{c}{ot_pct})", BLK, USD)
        put(rb, f"{c}{R_TOT}", f"={c}{R_REC}+{c}{R_OT}", BLK, USD)
    if i >= 1: put(rb, f"{c}{R_GR}", f"={c}{R_TOT}/{p}{R_TOT}-1", BLK, PCT)
    if i in (1, 2): put(rb, f"{c}{R_VC}", f"={c}{R_TOT}/{c}7-1", BLK, '+0.0%;-0.0%;0.0%')
    put(rb, f"{c}{R_SS}", f"=({c}{R_MP}+{c}{R_NW})/{c}{R_TOT}", BLK, PCT)
    if i == 0: put(rb, f"{c}{R_PX}", f"={PX0}", GRN, USD)
    elif i <= 5: put(rb, f"{c}{R_PX}", f"={p}{R_PX}*(1+IF({c}{h_px}=\"\",0.03,{c}{h_px}))", BLK, USD)
    else: put(rb, f"{c}{R_PX}", f"={p}{R_PX}*1.03", BLK, USD)
    put(rb, f"{c}{R_HR}", f"={c}{R_MP}/{c}{R_PX}", BLK, '0.00')
    if i >= 1:
        put(rb, f"{c}{R_GSW}", f"={c}{R_SW}*{c}{gm_sw}", BLK, USD)
        put(rb, f"{c}{R_GMP}", f"={c}{R_MP}*{c}{gm_mp}", BLK, USD)
        put(rb, f"{c}{R_GNW}", f"={c}{R_NW}*{c}{gm_nw}", BLK, USD)
        put(rb, f"{c}{R_GOT}", f"={c}{R_OT}*{c}{gm_ot}", BLK, USD)
        put(rb, f"{c}{R_GP}", f"=SUM({c}{R_GSW}:{c}{R_GOT})", BLK, USD)
        put(rb, f"{c}{R_GM}", f"={c}{R_GP}/{c}{R_TOT}", BLK, PCT)
        put(rb, f"{c}{R_VO}", f"={c}{vo_pct}*({c}{R_MP}+{c}{R_NW})", BLK, USD)
        if i == 1: put(rb, f"{c}{R_FO}", f"=({c}{R_GP}-{c}8)-{c}{R_VO}", BLK, USD)
        else: put(rb, f"{c}{R_FO}", f"={p}{R_FO}*(1+{c}{fx_g})", BLK, USD)
        put(rb, f"{c}{R_OX}", f"={c}{R_VO}+{c}{R_FO}", BLK, USD)
        put(rb, f"{c}{R_OXP}", f"={c}{R_OX}/{c}{R_TOT}", BLK, PCT)
        put(rb, f"{c}{R_EB}", f"={c}{R_GP}-{c}{R_OX}", BLK, USD)
        put(rb, f"{c}{R_EBM}", f"={c}{R_EB}/{c}{R_TOT}", BLK, PCT)
    if i in (1, 2): put(rb, f"{c}{R_EBC}", f"={c}{R_EB}-{c}8", BLK, USD)
for rr, n in [(R_MP, "FY25–26: residual so total = actual/consensus. FY27+: hours growth (expansion + new − cuts) × price escalator."),
              (R_NW, "Revenue = opening run-rate (escalated, net of rebid losses) + half of the year's launches."),
              (R_FO, "FY26 backed out so adj. EBITDA = consensus (−$7.4M)."),
              (R_EB, "Adjusted = before stock comp. DCF tab deducts stock comp.")]:
    cc_ = put(rb, f"N{rr}", n, Font(name=F, size=9)); cc_.alignment = WRAP
rb.freeze_panes = "C7"
RB = dict(TOT=R_TOT, EB=R_EB, GP=R_GP)

# ================= DCF =================
dc = wb.create_sheet("DCF")
dc.column_dimensions["A"].width = 3; dc.column_dimensions["B"].width = 46
for i in range(3, 14): dc.column_dimensions[L(i)].width = 10
dc.column_dimensions["N"].width = 50
put(dc, "B1", "DCF (unlevered free cash flow, valuation at end-FY26, mid-year convention)", T)
put(dc, "B2", "Scenario is set on Revenue_Build!D4. Stock comp is deducted as a real cost (toggle below).", Font(name=F, italic=True, size=9))
inp = [
 (4, "Risk-free rate", 0.0425, PCT, "10-yr UST (update)."),
 (5, "Equity beta", 1.30, '0.00', "Small-cap, high-growth; check Bloomberg BETA."),
 (6, "Equity risk premium", 0.055, PCT, ""),
 (7, "Cost of equity = WACC (no debt)", "=C4+C5*C6", PCT, "Via has no debt (10-Q)."),
 (8, "WACC used", "=C7", PCT, "Override here to test."),
 (9, "Terminal growth", 0.03, PCT, ""),
 (10, "Cash tax rate (after NOLs)", 0.25, PCT, ""),
 (11, "First year of cash taxes", 2030, '0', "NOL shield assumption. Check 10-K tax note."),
 (12, "D&A % of revenue", 0.017, PCT, "Consensus D&A ≈ $9–10M on ~$550M."),
 (13, "Capex + capitalized software % of revenue", 0.015, PCT, "FY25 capitalized software $4.3M + capex."),
 (14, "Net working capital % of revenue", 0.08, PCT, "Q2'26: AR+prepaids ≈ $122M less payables/accruals/deferred ≈ $81M → ~$41M on $543M run-rate."),
 (15, "Deduct stock comp? (1 = yes)", 1, '0', "SBC is ~11% of revenue in FY26."),
 (16, "Cash (Q2'26, no debt)", 336.0, USD, ""),
 (17, "Diluted shares (mm)", 84.2, '0.0', "Consensus Q4'26E diluted."),
 (18, "Current share price", "='Consensus_Check'!C29", '$#,##0.00', ""),
 (19, "Exit EV/EBITDA multiple (cross-check)", 15.0, '0.0x', "Applied to FY35 adj. EBITDA."),
]
for rr, lab, v, fmt, note in inp:
    put(dc, f"B{rr}", lab)
    isf = isinstance(v, str)
    put(dc, f"C{rr}", v, (GRN if isf and "!" in v else BLK) if isf else BLUE, fmt, YEL if rr in (8, 9, 15, 19) else None)
    put(dc, f"D{rr}", note, Font(name=F, size=9))
hdr(dc, 21, ["", "($mm)"] + YRS[1:] + ["Notes"], 1)  # D..M = FY26..FY35 -> use columns C..L? keep aligned: FY26 in C
DC = [L(3+i) for i in range(10)]   # C..L = FY26..FY35
RBC = COLS[1:]                      # D..M in Revenue_Build
put(dc, "B22", "Revenue"); put(dc, "B23", "Adjusted EBITDA"); put(dc, "B24", "Stock comp % of revenue"); put(dc, "B25", "Stock comp")
put(dc, "B26", "EBITDA after stock comp"); put(dc, "B27", "D&A"); put(dc, "B28", "EBIT"); put(dc, "B29", "Cash taxes")
put(dc, "B30", "Capex + capitalized software"); put(dc, "B31", "Increase in net working capital"); put(dc, "B32", "UNLEVERED FREE CASH FLOW", B)
put(dc, "B33", "Discount period (years from end-FY26)"); put(dc, "B34", "PV of FCF")
sbc = [0.115, 0.096, 0.08, 0.065, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
for i, c in enumerate(DC):
    rc = RBC[i]; yr = 2026 + i
    put(dc, f"{c}22", f"='Revenue_Build'!{rc}{RB['TOT']}", GRN, USD)
    put(dc, f"{c}23", f"='Revenue_Build'!{rc}{RB['EB']}", GRN, USD)
    put(dc, f"{c}24", sbc[i], BLUE, PCT)
    put(dc, f"{c}25", f"={c}22*{c}24", BLK, USD)
    put(dc, f"{c}26", f"={c}23-$C$15*{c}25", BLK, USD)
    put(dc, f"{c}27", f"={c}22*$C$12", BLK, USD)
    put(dc, f"{c}28", f"={c}26-{c}27", BLK, USD)
    put(dc, f"{c}29", f"=IF({yr}>=$C$11,MAX(0,{c}28)*$C$10,0)", BLK, USD)
    put(dc, f"{c}30", f"={c}22*$C$13", BLK, USD)
    if i == 0: put(dc, f"{c}31", 0, BLUE, USD)
    else: put(dc, f"{c}31", f"=({c}22-{DC[i-1]}22)*$C$14", BLK, USD)
    put(dc, f"{c}32", f"={c}26-{c}29-{c}30-{c}31", BLK, USD)
    if i >= 1:
        put(dc, f"{c}33", i - 0.5, BLK, '0.0')
        put(dc, f"{c}34", f"={c}32/(1+$C$8)^{c}33", BLK, USD)
put(dc, "M24", "FY26–27 = consensus SBC; fades to 5%.", Font(name=F, size=9))
put(dc, "M31", "FY26 excluded (valuation at end-FY26).", Font(name=F, size=9))
put(dc, "B36", "VALUATION", H)
rows = [
 (37, "Sum of PV of FCF (FY27–35)", "=SUM(D34:L34)", USD),
 (38, "Terminal value (perpetuity growth) at end-FY35", "=L32*(1+C9)/(C8-C9)", USD),
 (39, "PV of terminal value", "=C38/(1+C8)^9", USD),
 (40, "Enterprise value", "=C37+C39", USD),
 (41, "+ Cash", "=C16", USD),
 (42, "Equity value", "=C40+C41", USD),
 (43, "VALUE PER SHARE (perpetuity growth)", "=C42/C17", '$#,##0.00'),
 (44, "Upside / (downside) vs current price", "=C43/C18-1", '+0.0%;-0.0%'),
 (45, "Terminal value as % of EV", "=C39/C40", PCT),
 (47, "Cross-check: exit multiple on FY35 adj. EBITDA", "=L23*C19", USD),
 (48, "   Value per share (exit multiple)", "=(C37+C47/(1+C8)^9+C16)/C17", '$#,##0.00'),
 (49, "   Implied perpetuity growth in exit multiple", "=(C47*C8-L32)/(C47+L32)", PCT),
]
for rr, lab, f, fmt in rows:
    put(dc, f"B{rr}", lab, B if rr in (40, 43) else BLK); put(dc, f"C{rr}", f, BLK, fmt)
dc["C43"].fill = PatternFill("solid", fgColor="E2EFDA")
put(dc, "B51", "Sensitivity: value per share (perpetuity), WACC (rows) × terminal growth (cols)", H)
put(dc, "B52", "WACC \\ g", B)
gs = [0.02, 0.025, 0.03, 0.035, 0.04]; ws_ = [0.09, 0.10, 0.11, 0.12, 0.13]
for j, g in enumerate(gs): put(dc, f"{L(3+j)}52", g, BLUE, PCT)
for i, w in enumerate(ws_):
    rr = 53 + i; put(dc, f"B{rr}", w, BLUE, PCT)
    for j in range(5):
        c = L(3+j)
        put(dc, f"{c}{rr}", f"=(SUMPRODUCT($D$32:$L$32/((1+$B{rr})^$D$33:$L$33))+$L$32*(1+{c}$52)/($B{rr}-{c}$52)/(1+$B{rr})^9+$C$16)/$C$17", BLK, '$#,##0.00')
put(dc, "B59", "Scenario results (switch Revenue_Build!D4 to 1 or 2 and re-read C43). Our run is recorded in the README.", Font(name=F, size=9))

# ================= Sheet 7: Sources =================
so = wb.create_sheet("Sources")
so.column_dimensions["A"].width = 6; so.column_dimensions["B"].width = 80; so.column_dimensions["C"].width = 100
put(so, "A1", "Sources", T)
put(so, "A2", "Primary pages (SEC, council sites) were blocked from this environment. Figures come from search-engine extracts of these pages, so verify key numbers against the originals before presenting.", Font(name=F, italic=True, size=9, color="C00000"))
hdr(so, 4, ["ID", "Description", "URL"])
for i, (k, (d, u)) in enumerate(SRC.items()):
    r = 5 + i; put(so, f"A{r}", k); put(so, f"B{r}", d); put(so, f"C{r}", u)

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
wb.save("/home/user/VIA/model/VIA_software_services_mix.xlsx")
print("ok")

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

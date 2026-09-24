import sys
from copy import copy
import openpyxl
from openpyxl.comments import Comment
from openpyxl.workbook.properties import CalcProperties
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src)
dc, rb = wb['DCF'], wb['Revenue Build']
COLS = 'BCDEFGHIJ'
F = 'FGHIJ'
note = lambda cell, t: setattr(cell, 'comment', Comment(t, 'Model'))

# 1) remove the SBC add-back toggle (row 38): shift rows 39-41 up one, columns B:J only
#    (the valuation panel in L:M shares these rows and must not move)
for r in (39, 40, 41):
    for c in COLS:
        s, d = dc[f'{c}{r}'], dc[f'{c}{r-1}']
        v = s.value
        if isinstance(v, str) and v.startswith('='):
            v = v.replace(f'C{r-20}', f'C{r-20}')  # formulas in these rows point at rows 19/20/4, unchanged
        d.value = v
        d._style = copy(s._style)
        d.comment = copy(s.comment) if s.comment else None
for c in COLS:
    dc[f'{c}41'].value = None
    dc[f'{c}41'].comment = None
    dc[f'{c}41']._style = copy(dc['B42']._style)
for c in F:
    dc[f'{c}19'] = f'={c}4*{c}38'
    dc[f'{c}20'] = f'=-{c}4*{c}39'
dc['F29'] = "='WACC Calculations'!C27*(1+F40)"
for p, c in zip('FGHI', 'GHIJ'):
    dc[f'{c}29'] = f'={p}29*(1+{c}40)'
# SBC is a real cost in the forecast, so nothing is added back
for c in F:
    dc[f'{c}18'] = 0
dc['B18'] = '(+) SBC (historical only)'
note(dc['F18'], 'Stock comp is treated as a real cost in the forecast (it is ~11% of revenue and dilutes holders), so it is not added back to UFCF.')

# 2) NWC: -2% of revenue -> -1.5% (FY23-25 average about -1.3%)
for c in F:
    dc[f'{c}38'] = -0.015
note(dc['F38'], 'FY23-25 average about -1.3% of revenue (10-K); receivables grow with revenue (AR +$23.7M in 1H26). -1.5%.')

# 3) Revenue Build growth drivers
sw = [0.12, 0.11, 0.10, 0.09, 0.08]
mp = [0.25, 0.16, 0.12, 0.10, 0.08]
for c, v in zip(F, sw): rb[f'{c}19'] = v
for c, v in zip(F, mp): rb[f'{c}20'] = v
note(rb['F19'], 'FY26 +12%: organic customer growth ~9% (ex-94 Downtowner customers) plus ~2% price, and a small Downtowner contribution. FY27+ fades 11% to 8% as software fees face near-zero bids (Spare bid $0.01 at LA Metro).')
note(rb['F20'], 'FY26 +25% ties total FY26 revenue to 1H26 actuals ($263M) plus the H2 ramp (~consensus). FY27+ 16% to 8%: expansion at existing customers less budget-driven downsell (Jersey City cut ~half; federal stopgap / ARPA cliff). Revenue stays near consensus: the short rests on margins, not a revenue miss.')

wb.calculation = CalcProperties(fullCalcOnLoad=True)
wb.save(out)

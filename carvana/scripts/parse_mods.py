# Stream-parse one monthly Reg AB II auto file: per-loan status plus modification / extension fields.
# Usage: python3 parse_mods.py <deal> <period> <out.csv.gz> < ex102.xml
import sys, csv, gzip
import xml.etree.ElementTree as ET
deal, period_tag, outp = sys.argv[1], sys.argv[2], sys.argv[3]
NS = '{http://www.sec.gov/edgar/document/absee/autoloan/assetdata}'
F = ['assetNumber', 'reportingPeriodBeginningDate', 'reportingPeriodEndingDate',
     'reportingPeriodBeginningLoanBalanceAmount', 'reportingPeriodActualEndBalanceAmount',
     'currentDelinquencyStatus', 'zeroBalanceCode',
     'reportingPeriodModificationIndicator', 'modificationTypeCode', 'paymentExtendedNumber',
     'obligorCreditScore', 'originationDate', 'originalLoanTerm', 'remainingTermToMaturityNumber']
w = csv.writer(gzip.open(outp, 'wt', newline=''))
w.writerow(['deal', 'file'] + F)
n = 0
for ev, el in ET.iterparse(sys.stdin.buffer, events=('end',)):
    if el.tag == NS + 'assets':
        # modificationTypeCode can repeat (1 APR, 2 principal, 3 term, 4 extension, 98 other); join with '|'
        w.writerow([deal, period_tag] + ['|'.join((e.text or '').strip() for e in el.findall(NS + f)) for f in F])
        n += 1
        el.clear()
print(deal, period_tag, n, file=sys.stderr)

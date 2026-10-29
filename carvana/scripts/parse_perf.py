# Stream-parse one monthly Reg AB II file: per-loan status fields only.
import sys, csv, gzip
import xml.etree.ElementTree as ET
deal, period_tag, outp = sys.argv[1], sys.argv[2], sys.argv[3]
NS='{http://www.sec.gov/edgar/document/absee/autoloan/assetdata}'
F=['assetNumber','reportingPeriodEndingDate','currentDelinquencyStatus','repossessedIndicator','zeroBalanceCode',
   'chargedoffPrincipalAmount','recoveredAmount','reportingPeriodActualEndBalanceAmount','reportingPeriodBeginningLoanBalanceAmount',
   'paymentExtendedNumber']   # cumulative count of payment extensions (Reg AB II auto field); used by extensions.py
w=csv.writer(gzip.open(outp,'wt',newline=''))
w.writerow(['deal','file']+F)
n=0
for ev,el in ET.iterparse(sys.stdin.buffer,events=('end',)):
    if el.tag==NS+'assets':
        w.writerow([deal,period_tag]+[(el.find(NS+f).text or '').strip() if el.find(NS+f) is not None else '' for f in F]); n+=1; el.clear()
print(deal,period_tag,n,file=sys.stderr)

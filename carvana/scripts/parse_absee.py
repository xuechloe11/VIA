# Stream-parse a Reg AB II auto-loan asset-data XML (EX-102) from stdin into a compact CSV.
import sys, csv, re, gzip
import xml.etree.ElementTree as ET

deal = sys.argv[1]
out = gzip.open(sys.argv[2], 'wt', newline='')
NS = '{http://www.sec.gov/edgar/document/absee/autoloan/assetdata}'
F = ['assetNumber','originatorName','originationDate','originalLoanAmount','originalLoanTerm',
     'originalInterestRatePercentage','vehicleManufacturerName','vehicleModelName','vehicleNewUsedCode',
     'vehicleModelYear','vehicleTypeCode','vehicleValueAmount','obligorCreditScoreType','obligorCreditScore',
     'obligorIncomeVerificationLevelCode','obligorEmploymentVerificationCode','coObligorIndicator',
     'paymentToIncomePercentage','obligorGeographicLocation','reportingPeriodScheduledPaymentAmount',
     'nextReportingPeriodPaymentAmountDue','reportingPeriodBeginningLoanBalanceAmount',
     'reportingPeriodActualEndBalanceAmount','currentDelinquencyStatus','repossessedIndicator',
     'zeroBalanceCode','chargedoffPrincipalAmount','recoveredAmount','reportingPeriodEndingDate',
     'subvented','gracePeriodNumber','reportingPeriodModificationIndicator']
w = csv.writer(out)
w.writerow(['deal'] + F)
n = 0
for ev, el in ET.iterparse(sys.stdin.buffer, events=('end',)):
    if el.tag == NS + 'assets':
        row = [deal]
        for f in F:
            c = el.find(NS + f)
            row.append(c.text.strip() if c is not None and c.text else '')
        w.writerow(row)
        n += 1
        el.clear()
out.close()
print(deal, n, file=sys.stderr)

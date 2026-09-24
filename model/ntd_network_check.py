"""Reproduce the NTD figures in evidence_network_services.md.

Pulls FTA National Transit Database annual data (2022-2024) from data.transportation.gov:
  j5uj-anzx  Operating Expenses (by Type)   -> cost structure of bus systems
  ekg5-frzt  Metrics                          -> opex and vehicle revenue hours
"""
import csv, io, statistics, urllib.request

BASE = "https://data.transportation.gov/resource/{}.csv?$limit=100000"
LABOR = ["operators_wages", "other_salaries_wages", "operator_paid_absences",
         "other_paid_absences", "fringe_benefits"]
# NTD ID -> (name, Via annual contract value $M, source)
VIA_NETWORK = {
    "80002": ("Sioux Falls, SD", None, "Via took over 2024"),
    "40043": ("Mobile, AL", 12.1, "from Oct 2025"),
    "50092": ("Rochester, MN", 77.8 / 64 * 12, "$77.8M / 64 mo from Sep 2026"),
}


def load(ds):
    with urllib.request.urlopen(BASE.format(ds)) as r:
        return list(csv.DictReader(io.TextIOWrapper(r, "utf-8")))


def f(row, k):
    return float(row.get(k) or 0)


def main():
    opex, metrics = load("j5uj-anzx"), load("ekg5-frzt")

    peers = [x for x in opex if x["report_year"] == "2024" and x["mode"] == "MB"
             and x["type_of_service"] == "DO" and x["reporter_type"] == "Full Reporter"
             and 5e6 <= f(x, "total") < 50e6]
    tot = sum(f(x, "total") for x in peers)
    share = lambda ks: sum(f(x, k) for x in peers for k in ks) / tot
    agency_labor = [sum(f(x, k) for k in LABOR) / f(x, "total") for x in peers]
    q = statistics.quantiles(agency_labor, n=4)
    print(f"US directly operated bus, full reporters $5-50M, 2024 (n={len(peers)}):")
    print(f"  labor {share(LABOR):.1%} (median agency {q[1]:.1%}, IQR {q[0]:.1%}-{q[2]:.1%})")
    print(f"  fuel/tires/parts {share(['fuel_and_lube', 'tires', 'other_materials_supplies']):.1%}"
          f"  casualty & liability {share(['casualty_and_liability']):.1%}"
          f"  services {share(['services']):.1%}"
          f"  utilities/taxes/misc {share(['utilities', 'taxes', 'miscellaneous']):.1%}")

    for tos in ["DO", "PT"]:
        rows = [x for x in metrics if x["report_year"] == "2024" and x["mode"] == "MB"
                and x["type_of_service"] == tos and x["reporter_type"] == "Full Reporter"
                and 5e6 <= f(x, "total_operating_expenses") < 50e6 and f(x, "vehicle_revenue_hours") > 0]
        s = [f(x, "total_operating_expenses") / f(x, "vehicle_revenue_hours") for x in rows]
        q = statistics.quantiles(s, n=4)
        print(f"US bus {tos} $5-50M 2024 cost/VRH: median ${q[1]:.0f} (IQR ${q[0]:.0f}-${q[2]:.0f}, n={len(rows)})")

    for nid, (name, acv, note) in VIA_NETWORK.items():
        print(f"\n{name} (NTD {nid}) - Via contract: {f'${acv:.1f}M/yr' if acv else 'n/a'} {note}")
        for y in ["2022", "2023", "2024"]:
            rows = [x for x in opex if x["ntd_id"] == nid and x["report_year"] == y]
            m = [x for x in metrics if x["ntd_id"] == nid and x["report_year"] == y]
            t = sum(f(x, "total") for x in rows)
            vrh = sum(f(x, "vehicle_revenue_hours") for x in m)
            lab = sum(f(x, k) for x in rows for k in LABOR) / t
            pt = sum(f(x, "purchased_transportation") for x in rows) / t
            tos = ",".join(sorted({x["mode"] + "-" + x["type_of_service"] for x in rows}))
            line = f"  {y} [{tos}] opex ${t / 1e6:.2f}M, VRH {vrh:,.0f}, ${t / vrh:.0f}/VRH, labor {lab:.0%}, purchased transp. {pt:.0%}"
            if acv and y == "2024":
                line += f" | Via ACV = {acv / (t / 1e6):.0%} of 2024 opex, ${acv * 1e6 / vrh:.0f}/VRH"
            print(line)


if __name__ == "__main__":
    main()

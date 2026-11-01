import csv, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def _rows(name):
    with open(os.path.join(BASE, "data", name), encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_claims():
    return _rows("claims_12.csv")

def load_stage_graph():
    return {r["stage"]: [x for x in r["nextStages"].split("|") if x] for r in _rows("stages.csv")}

def load_daily_counts():
    return [int(r["claims"]) for r in _rows("daily_claims_14.csv")]

def load_office_lists():
    return {r["office"]: r["claimIds"].split("|") for r in _rows("office_lists.csv")}

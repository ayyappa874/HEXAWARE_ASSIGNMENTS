import csv, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def load_hubs():
    with open(os.path.join(BASE, "data", "hubs_10.csv"), encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_graph():
    """Adjacency list: hubCode -> list of neighbour hubCodes."""
    return {h["hubCode"]: h["connectedTo"].split("|") for h in load_hubs()}

def load_scans():
    with open(os.path.join(BASE, "data", "scans_12.csv"), encoding="utf-8") as f:
        return list(csv.DictReader(f))

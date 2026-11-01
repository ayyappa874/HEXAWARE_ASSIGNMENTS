from common import load_scans
from task2_hashmap import build_lookup, find_double_scans
scans = load_scans()
print("TRK1003 :", build_lookup(scans).get("TRK1003"))
print("Double scans:")
for row in find_double_scans(scans): print("  ", row)

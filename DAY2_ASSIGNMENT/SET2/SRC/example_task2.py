from common import load_claims
from task2_hashing import find_duplicates
for key, grp in find_duplicates(load_claims()):
    print(key, "->", grp)

from common import load_office_lists
from task5_merge import merge_sorted
o = load_office_lists()
print(merge_sorted(o["North"], o["South"]))

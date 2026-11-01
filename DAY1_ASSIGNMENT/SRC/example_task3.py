# Example 3 - find duplicate orders by sorting (no hashing)
from common import load_sample
from task3_duplicates import find_duplicates

orders = load_sample()

for group in find_duplicates(orders):
    ids = [o["orderId"] for o in group]
    first = group[0]
    print(f"Duplicate group {ids}: customer {first['customerId']}, amount {first['amount']}")

# 1014/1015 differ by one minute, 1017/1018 have different customers,
# 1019/1020 have different amounts, so none of those are reported.

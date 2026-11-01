# Example 5 - refund with the fewest notes/coins
from task5_refund import greedy_change, dp_change, count, show, INR

used = greedy_change(2499, INR)
print("Refund Rs 2499 (greedy):", count(used), "pieces ->", show(used))

for name, fn in (("greedy", greedy_change), ("DP", dp_change)):
    used = fn(6, [1, 3, 4])
    print(f"Coins [1, 3, 4], refund 6 ({name}):", count(used), "coins ->", show(used))

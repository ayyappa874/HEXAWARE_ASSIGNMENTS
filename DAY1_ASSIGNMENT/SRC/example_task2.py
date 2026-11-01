# Example 2 - rank the 20 orders by amount (highest first)
from common import load_sample
from task2_sorting import bubble_sort_desc, merge_sort_desc

orders = load_sample()

ranked = merge_sort_desc(orders)
print("Top 5 orders by amount:")
for rank, o in enumerate(ranked[:5], start=1):
    print(f"  #{rank}  order {o['orderId']}  amount {o['amount']}")

same = [o["orderId"] for o in bubble_sort_desc(orders)] == [o["orderId"] for o in ranked]
print("Bubble sort and merge sort give the same ranking:", same)

print("\nFirst 3 bubble-sort passes on the first 10 amounts:")
first10 = orders[:10]
print("  Start :", [o["amount"] for o in first10])
bubble_sort_desc(first10, trace=True)

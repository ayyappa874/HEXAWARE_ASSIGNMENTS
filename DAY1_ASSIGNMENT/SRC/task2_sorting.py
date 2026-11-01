"""Task 2 - Rank orders by amount (descending): Bubble sort O(n^2) vs Merge sort O(n log n)."""
import os
import time
from common import ensure_dataset, load_orders, merge_sort, DATA_DIR


def bubble_sort_desc(orders, trace=False):
    """O(n^2). Repeatedly swaps adjacent out-of-order pairs; early exit if no swap."""
    a = list(orders)
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for j in range(n - 1 - p):
            if a[j]["amount"] < a[j + 1]["amount"]:       # descending
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if trace and p < 3:
            print(f"  After pass {p + 1}: {[x['amount'] for x in a]}")
        if not swapped:
            break
    return a


def merge_sort_desc(orders):
    """O(n log n). Divide, sort halves, merge (shared stable implementation)."""
    return merge_sort(orders, key=lambda o: o["amount"], reverse=True)


def main():
    # ---- Part A: trace first 3 passes on the first 6 of the 20 sample records
    sample = load_orders(os.path.join(DATA_DIR, "orders_20.csv"))[:6]
    print("TRACE (bubble sort, descending) on first 6 sample amounts")
    print(f"  Start        : {[x['amount'] for x in sample]}")
    bubble_sort_desc(sample, trace=True)

    # ---- Part B: 10,000-record comparison
    orders = load_orders(ensure_dataset(10000))
    print(f"\nBENCHMARK on {len(orders)} records")
    results = {}
    for name, fn in [("Bubble sort  O(n^2)", bubble_sort_desc),
                     ("Merge sort  O(n log n)", merge_sort_desc),
                     ("Built-in sorted() (Timsort)", lambda o: sorted(o, key=lambda x: x["amount"], reverse=True))]:
        t0 = time.perf_counter()
        results[name] = fn(orders)
        print(f"  {name:<30}{(time.perf_counter() - t0):>9.4f} s")

    ref = [o["amount"] for o in results["Built-in sorted() (Timsort)"]]
    assert all([o["amount"] for o in r] == ref for r in results.values()), "outputs must match"
    print("  All three produce the same ranking: OK")

    print("\nTop 5 orders by amount:")
    for rank, o in enumerate(results["Merge sort  O(n log n)"][:5], 1):
        print(f"  #{rank}  order {o['orderId']}  customer {o['customerId']}  amount {o['amount']}")


if __name__ == "__main__":
    main()

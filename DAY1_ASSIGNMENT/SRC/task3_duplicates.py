"""Task 3 - Detect duplicate submissions using SORTING (no hashing).

Duplicate = same customerId + same amount + same minute.
Idea: build a key (customerId, amount, minute), sort by key, and equal keys become
neighbours - so one linear scan over adjacent rows finds every duplicate group.
"""
import os
from common import ensure_dataset, load_orders, merge_sort, DATA_DIR


def minute_of(created_at):
    """'2026-10-29 10:12:48' -> '2026-10-29 10:12' (drop the seconds)."""
    return created_at[:16]


def find_duplicates(orders):
    """Return list of duplicate groups (each group = list of orders, size >= 2)."""
    key = lambda o: (o["customerId"], o["amount"], minute_of(o["createdAt"]))
    ordered = merge_sort(orders, key=key)                 # O(n log n)
    groups, current = [], [ordered[0]] if ordered else []
    for prev, cur in zip(ordered, ordered[1:]):           # O(n) adjacent scan
        if key(cur) == key(prev):
            current.append(cur)
        else:
            if len(current) > 1:
                groups.append(current)
            current = [cur]
    if len(current) > 1:
        groups.append(current)
    return groups


def main():
    for label, orders in [("20 sample records", load_orders(os.path.join(DATA_DIR, "orders_20.csv"))),
                          ("50,000 generated records", load_orders(ensure_dataset(50000)))]:
        groups = find_duplicates(orders)
        flagged = sum(len(g) for g in groups)
        print(f"\n{label}: {len(groups)} duplicate group(s), {flagged} orders flagged")
        for g in groups[:6]:
            ids = ", ".join(str(o["orderId"]) for o in g)
            f = g[0]
            print(f"  customer {f['customerId']}  amount {f['amount']}  minute {minute_of(f['createdAt'])}  -> orders [{ids}]")
        if len(groups) > 6:
            print(f"  ... and {len(groups) - 6} more groups")

    print("\nComplexity (sorting approach):")
    print("  Time : O(n log n) for the sort + O(n) scan  => O(n log n)")
    print("  Space: O(n) for the sorted copy (O(1) extra if sorted in place)")
    print("\nNote: near-miss orders 1014/1015 (same customer & amount, but 12:05 vs 12:06)")
    print("      are correctly NOT flagged - minute boundary is respected.")


if __name__ == "__main__":
    main()

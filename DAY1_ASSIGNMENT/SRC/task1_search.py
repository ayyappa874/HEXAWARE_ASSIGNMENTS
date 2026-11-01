"""Task 1 - Linear search vs Binary search on 50,000 orders."""
import random
import time
from common import ensure_dataset, load_orders


def linear_search(orders, target_id):
    """Scan left to right. Returns (index, comparisons)."""
    comparisons = 0
    for i, o in enumerate(orders):
        comparisons += 1
        if o["orderId"] == target_id:
            return i, comparisons
    return -1, comparisons


def binary_search(orders, target_id):
    """Needs orders sorted by orderId. Returns (index, comparisons)."""
    lo, hi, comparisons = 0, len(orders) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if orders[mid]["orderId"] == target_id:
            return mid, comparisons
        if orders[mid]["orderId"] < target_id:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comparisons


def timed(fn, orders, target, repeats):
    start = time.perf_counter()
    for _ in range(repeats):
        res = fn(orders, target)
    return (time.perf_counter() - start) / repeats, res


def main():
    orders = load_orders(ensure_dataset(50000))
    assert all(orders[i]["orderId"] < orders[i + 1]["orderId"] for i in range(len(orders) - 1)), "must be sorted"
    n = len(orders)
    print(f"Loaded {n} orders (sorted by orderId)\n")

    cases = {
        "Best  (first order)": orders[0]["orderId"],
        "Middle order": orders[n // 2]["orderId"],
        "Worst (last order)": orders[-1]["orderId"],
        "Not found (id=0)": 0,
    }
    print(f"{'Case':<22}{'Linear cmp':>11}{'Binary cmp':>11}{'Linear time':>14}{'Binary time':>14}")
    for name, tid in cases.items():
        tl, (il, cl) = timed(linear_search, orders, tid, 20)
        tb, (ib, cb) = timed(binary_search, orders, tid, 2000)
        assert il == ib, "both searches must agree"
        print(f"{name:<22}{cl:>11}{cb:>11}{tl*1e6:>11.1f} us{tb*1e6:>11.2f} us")

    rng = random.Random(7)
    targets = [rng.choice(orders)["orderId"] for _ in range(1000)]
    t0 = time.perf_counter(); [linear_search(orders, t) for t in targets]; tl = time.perf_counter() - t0
    t0 = time.perf_counter(); [binary_search(orders, t) for t in targets]; tb = time.perf_counter() - t0
    print(f"\n1000 random lookups: linear = {tl*1000:.1f} ms, binary = {tb*1000:.2f} ms, "
          f"binary is ~{tl/tb:.0f}x faster")

    print("\nExplanation:")
    print("  Linear search is O(n): in the worst case it checks all 50,000 records.")
    print("  Binary search is O(log n): it halves the range each step, max ~16 checks")
    print("  (log2 50,000 = 15.6). Condition: data MUST already be sorted by orderId.")


if __name__ == "__main__":
    main()

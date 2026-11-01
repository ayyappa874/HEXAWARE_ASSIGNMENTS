"""Task 5 - Find all pairs of order values that add up to a gift-card value (two pointers)."""
import random
import time
from common import load_order_values


def find_pairs(values, target, steps=None):
    """values must be SORTED. One pointer at each end; move the one that fixes the sum.
    Returns each different pair of values once."""
    left, right = 0, len(values) - 1
    pairs = []
    while left < right:
        total = values[left] + values[right]
        if steps is not None:
            steps.append((left, right, values[left], values[right], total))
        if total == target:
            pairs.append((values[left], values[right]))
            a, b = values[left], values[right]
            while left < right and values[left] == a:      # skip repeats of the same value
                left += 1
            while left < right and values[right] == b:
                right -= 1
        elif total < target:
            left += 1          # sum too small -> need a bigger left value
        else:
            right -= 1         # sum too big   -> need a smaller right value
    return pairs


def find_pairs_brute(values, target):
    """Slow check: try every pair."""
    found = set()
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                found.add((values[i], values[j]))
    return sorted(found)


def main():
    values = load_order_values()
    target = 1000
    print("Sorted order values:", values)
    print(f"Gift-card value: Rs {target}")
    pairs = find_pairs(values, target)
    print(f"\nA) Two-pointer result: {len(pairs)} pairs")
    for a, b in pairs:
        print(f"  {a} + {b} = {a + b}")
    print("  Brute-force check gives the same pairs:", find_pairs_brute(values, target) == pairs)

    rng = random.Random(3)
    big = sorted(rng.randint(50, 50000) for _ in range(5000))
    t0 = time.perf_counter()
    fast = find_pairs(big, 25000)
    t_fast = time.perf_counter() - t0
    t0 = time.perf_counter()
    slow = find_pairs_brute(big, 25000)
    t_slow = time.perf_counter() - t0
    print(f"\nB) 5,000 sorted order values, gift card Rs 25,000")
    print(f"  Two pointers : {len(fast)} pairs in {t_fast * 1e3:.2f} ms")
    print(f"  Brute force  : {len(slow)} pairs in {t_slow * 1e3:.1f} ms  (same result: {fast == slow})")
    print(f"  Brute force is about {t_slow / t_fast:,.0f}x slower")

    huge = sorted(rng.randint(50, 500000) for _ in range(100000))
    t0 = time.perf_counter()
    big_pairs = find_pairs(huge, 250000)
    t_huge = time.perf_counter() - t0
    print(f"\nC) 100,000 sorted values with two pointers: {len(big_pairs)} pairs in {t_huge * 1e3:.1f} ms")
    return {"pairs": pairs, "fast_ms": t_fast * 1e3, "slow_ms": t_slow * 1e3, "ratio": t_slow / t_fast,
            "n_pairs_5000": len(fast), "huge_ms": t_huge * 1e3, "huge_pairs": len(big_pairs)}


if __name__ == "__main__":
    main()

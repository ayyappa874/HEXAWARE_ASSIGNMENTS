"""Task 5 - Minimum notes/coins for a refund: Greedy, and DP where greedy fails."""
import os
from common import load_orders, DATA_DIR

INR = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


def greedy_change(amount, denoms):
    """Always take the largest denomination that fits. O(k) after sorting."""
    used = {}
    for d in sorted(denoms, reverse=True):
        if amount >= d:
            used[d], amount = divmod(amount, d)
    return used if amount == 0 else None


def dp_change(amount, denoms):
    """Bottom-up DP. best[x] = min coins to make x. O(amount * k) time, O(amount) space."""
    INF = float("inf")
    best = [0] + [INF] * amount
    choice = [0] * (amount + 1)
    for x in range(1, amount + 1):
        for d in denoms:
            if d <= x and best[x - d] + 1 < best[x]:
                best[x], choice[x] = best[x - d] + 1, d
    if best[amount] == INF:
        return None
    used, x = {}, amount
    while x > 0:                                   # walk back to rebuild the coins
        used[choice[x]] = used.get(choice[x], 0) + 1
        x -= choice[x]
    return used


def count(used):
    return sum(used.values()) if used else None


def show(used):
    return " + ".join(f"{c} x {d}" for d, c in sorted(used.items(), reverse=True))


def main():
    print("A) GREEDY on Indian currency", INR)
    orders = load_orders(os.path.join(DATA_DIR, "orders_20.csv"))
    for o in [orders[1], orders[6], orders[8], orders[11]]:
        g = greedy_change(o["amount"], INR)
        print(f"  refund order {o['orderId']} (Rs {o['amount']}): {count(g)} pieces -> {show(g)}")
    ok = all(count(greedy_change(a, INR)) == count(dp_change(a, INR)) for a in range(1, 3001))
    print(f"  Greedy matches the DP optimum for every amount 1..3000 on INR set: {ok}")

    print("\nB) WHERE GREEDY FAILS: denominations [1, 3, 4], refund = 6")
    d, amt = [1, 3, 4], 6
    g, p = greedy_change(amt, d), dp_change(amt, d)
    print(f"  Greedy : {count(g)} coins -> {show(g)}")
    print(f"  DP     : {count(p)} coins -> {show(p)}   <-- optimal")
    bad = [a for a in range(1, 31) if count(greedy_change(a, d)) > count(dp_change(a, d))]
    print(f"  Amounts 1..30 where greedy is suboptimal: {bad}")

    print("\nC) Another failing set: [1, 5, 6, 9], refund = 11")
    d, amt = [1, 5, 6, 9], 11
    print(f"  Greedy : {count(greedy_change(amt, d))} coins -> {show(greedy_change(amt, d))}")
    print(f"  DP     : {count(dp_change(amt, d))} coins -> {show(dp_change(amt, d))}")

    print("\nWhy: greedy makes the locally best pick (largest coin) and never reconsiders.")
    print("DP tries every coin for every sub-amount, so it always finds the true minimum.")


if __name__ == "__main__":
    main()

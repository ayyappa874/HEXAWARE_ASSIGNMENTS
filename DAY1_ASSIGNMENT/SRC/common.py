"""Shared helpers: CSV loading, dataset generation, and a reusable merge sort.

Retail Order Desk - Day 1 (Problem Solving Techniques & Data Structures - I)
"""
import csv
import os
import random
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
FIELDS = ["orderId", "customerId", "amount", "createdAt"]


def load_orders(path):
    """Load orders.csv -> list of dicts (orderId, amount as int)."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["orderId"] = int(r["orderId"])
        r["amount"] = int(r["amount"])
    return rows


def load_sample():
    """Load the 20 hand-made sample records from data/orders_20.csv."""
    return load_orders(os.path.join(DATA_DIR, "orders_20.csv"))


def generate_orders(n, seed=42):
    """Deterministic synthetic orders, sorted by orderId (needed for binary search).

    Every 500th order is a planted duplicate of the previous one
    (same customer, same amount, seconds later) so Task 3 has something to find.
    """
    rng = random.Random(seed)
    ts = datetime(2026, 10, 29, 0, 0, 0)
    rows = []
    for i in range(n):
        ts += timedelta(seconds=rng.randint(1, 2))
        if i > 0 and i % 500 == 0:
            cust, amt = rows[-1]["customerId"], rows[-1]["amount"]
        else:
            cust, amt = f"C{rng.randint(1, 5000):04d}", rng.randint(50, 50000)
        rows.append({"orderId": 100001 + i, "customerId": cust,
                     "amount": amt, "createdAt": ts.strftime("%Y-%m-%d %H:%M:%S")})
    return rows


def ensure_dataset(n):
    """Return path of orders_<n>.csv, generating it if missing."""
    path = os.path.join(DATA_DIR, f"orders_{n}.csv")
    if not os.path.exists(path):
        rows = generate_orders(n)
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            w.writerows(rows)
    return path


def merge_sort(items, key, reverse=False):
    """Stable O(n log n) merge sort; `key` extracts the comparable value."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid], key, reverse)
    right = merge_sort(items[mid:], key, reverse)
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        a, b = key(left[i]), key(right[j])
        take_left = a >= b if reverse else a <= b   # ties -> left (keeps stability)
        if take_left:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

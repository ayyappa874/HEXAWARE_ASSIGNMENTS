"""Shared helpers: file loading and test-data generators (Day 2 - E-Commerce Catalogue)."""
import csv
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")


def _rows(name):
    with open(os.path.join(DATA_DIR, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_categories():
    """15 product categories, in the order they are inserted into the BST."""
    return [r["category"] for r in _rows("categories_15.csv")]


def load_sample_skus():
    """20 sample SKUs -> list of (sku, product name, price)."""
    return [(r["sku"], r["product"], int(r["price"])) for r in _rows("skus_20.csv")]


def load_dependencies():
    """services.csv -> {service: [services it depends on]} (arrow means 'depends on')."""
    deps = {}
    for r in _rows("dependencies.csv"):
        deps.setdefault(r["service"], [])
        if r["depends_on"]:
            deps[r["service"]].append(r["depends_on"])
    return deps


def load_traffic():
    """1,440 rows (one per minute of the day) -> list of requests-per-minute."""
    return [int(r["requests"]) for r in _rows("traffic_24h.csv")]


def load_order_values():
    """20 sorted order values (in Rs)."""
    return [int(r["value"]) for r in _rows("order_values_20.csv")]


def generate_skus(n, seed=11):
    """n distinct random SKU codes like 'SKU-482913' with a product name and price."""
    rng = random.Random(seed)
    numbers = rng.sample(range(100000, 1000000), n)
    return [(f"SKU-{x}", f"Product {x}", rng.randint(49, 9999)) for x in numbers]


def minute_label(index):
    """0 -> '00:00', 1439 -> '23:59'."""
    return f"{index // 60:02d}:{index % 60:02d}"

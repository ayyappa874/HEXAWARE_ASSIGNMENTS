"""Creates the small data files in /data (run once; the files are already included)."""
import csv
import math
import os
import random
from common import DATA_DIR


def write(name, header, rows):
    with open(os.path.join(DATA_DIR, name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# 15 categories, listed so that inserting them in this order gives a well-balanced tree
CATEGORIES = ["Grocery", "Clothing", "Sports", "Beauty", "Furniture", "Music", "Toys",
              "Appliances", "Books", "Electronics", "Garden", "Jewellery",
              "Pet Supplies", "Stationery", "Watches"]
write("categories_15.csv", ["category"], [[c] for c in CATEGORIES])

SKUS = [("SKU-1001", "Wireless Mouse", 799), ("SKU-1002", "USB-C Cable", 299),
        ("SKU-1003", "Laptop Stand", 1499), ("SKU-1004", "Bluetooth Speaker", 2499),
        ("SKU-1005", "Phone Case", 349), ("SKU-1006", "Notebook A5", 120),
        ("SKU-1007", "Water Bottle", 450), ("SKU-1008", "Desk Lamp", 899),
        ("SKU-1009", "Backpack", 1899), ("SKU-1010", "Running Shoes", 3299),
        ("SKU-1011", "Coffee Mug", 249), ("SKU-1012", "Yoga Mat", 999),
        ("SKU-1013", "Headphones", 1999), ("SKU-1014", "Power Bank", 1299),
        ("SKU-1015", "Smart Watch", 4999), ("SKU-1016", "Hair Dryer", 1199),
        ("SKU-1017", "Board Game", 899), ("SKU-1018", "Face Wash", 199),
        ("SKU-1019", "Cricket Bat", 2799), ("SKU-1020", "Table Fan", 1799)]
write("skus_20.csv", ["sku", "product", "price"], SKUS)

# "service depends on depends_on"  (cart -> pricing -> inventory ... as in the brief)
DEPS = [("api-gateway", "auth"), ("api-gateway", "cart"), ("api-gateway", "order"),
        ("cart", "pricing"), ("pricing", "inventory"), ("inventory", "database"),
        ("order", "cart"), ("order", "payment"), ("payment", "auth"),
        ("auth", "database"), ("notification", "order"), ("database", "")]
write("dependencies.csv", ["service", "depends_on"], DEPS)

# requests per minute for 24 hours: quiet night, small lunch bump, big evening peak
rng = random.Random(2026)
rows = []
for m in range(24 * 60):
    h = m / 60
    base = 120 + 600 * math.exp(-((h - 12.5) / 2.0) ** 2) + 1500 * math.exp(-((h - 20.0) / 1.8) ** 2)
    rows.append([f"{m // 60:02d}:{m % 60:02d}", max(0, int(base * rng.uniform(0.9, 1.1)))])
write("traffic_24h.csv", ["time", "requests"], rows)

VALUES = [150, 250, 250, 320, 400, 450, 500, 500, 600, 650,
          750, 800, 850, 899, 950, 1100, 1250, 1500, 1800, 2499]
write("order_values_20.csv", ["value"], [[v] for v in VALUES])
print("data files written")

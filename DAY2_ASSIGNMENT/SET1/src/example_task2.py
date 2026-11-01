# Example 2 - a tiny hash table with chaining, forcing a collision
from task2_hashing import ChainedHashTable

table = ChainedHashTable(capacity=3, auto_resize=False)   # only 3 buckets
for sku, name in [("SKU-1", "Mouse"), ("SKU-2", "Cable"), ("SKU-3", "Stand"), ("SKU-4", "Lamp")]:
    table.put(sku, name)

for i, chain in enumerate(table.buckets):
    print(f"bucket {i}:", [k for k, _ in chain])

print("get('SKU-3') ->", table.get("SKU-3"))
print("get('SKU-9') ->", table.get("SKU-9"))
table.remove("SKU-3")
print("after remove, get('SKU-3') ->", table.get("SKU-3"))

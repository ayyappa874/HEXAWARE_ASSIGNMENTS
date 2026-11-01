"""Task 2 - Hash table with chaining for SKU look-up, vs Python's built-in dict."""
import random
import time
from common import load_sample_skus, generate_skus


class ChainedHashTable:
    """Each bucket holds a list (a chain) of [key, value] pairs that landed there."""

    def __init__(self, capacity=8, auto_resize=True):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0
        self.auto_resize = auto_resize

    def _index(self, key):
        h = 0
        for ch in key:
            h = (h * 31 + ord(ch)) % self.capacity
        return h

    def put(self, key, value):
        chain = self.buckets[self._index(key)]
        for pair in chain:
            if pair[0] == key:          # key already stored -> update it
                pair[1] = value
                return
        chain.append([key, value])      # new key (a collision just makes the chain longer)
        self.size += 1
        if self.auto_resize and self.size / self.capacity > 0.75:
            self._grow()

    def get(self, key, default=None):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):
        chain = self.buckets[self._index(key)]
        for i, pair in enumerate(chain):
            if pair[0] == key:
                del chain[i]
                self.size -= 1
                return True
        return False

    def _grow(self):
        """Too crowded: make more buckets and re-place every key."""
        old = self.buckets
        self.capacity = self.capacity * 2 + 1
        self.buckets = [[] for _ in range(self.capacity)]
        for chain in old:
            for k, v in chain:
                self.buckets[self._index(k)].append([k, v])

    def longest_chain(self):
        return max(len(c) for c in self.buckets)


def timed_lookups(fn, keys):
    start = time.perf_counter()
    found = 0
    for k in keys:
        if fn(k) is not None:
            found += 1
    return time.perf_counter() - start, found


def main():
    # ---------- A) small table: show a collision ----------
    skus = load_sample_skus()[:10]
    small = ChainedHashTable(capacity=7, auto_resize=False)
    for sku, name, price in skus:
        small.put(sku, name)
    print("A) COLLISION DEMO - 10 SKUs into a table of only 7 buckets")
    collisions = 0
    for i, chain in enumerate(small.buckets):
        text = " -> ".join(k for k, _ in chain) if chain else "(empty)"
        note = "   <-- COLLISION" if len(chain) > 1 else ""
        collisions += 1 if len(chain) > 1 else 0
        print(f"  bucket {i}: {text}{note}")
    print(f"  Buckets with a collision: {collisions}; get('SKU-1004') -> {small.get('SKU-1004')}")

    # ---------- B) 100,000 SKUs: own table vs dict ----------
    data = generate_skus(100000)
    keys = [s[0] for s in data]
    shuffled = keys[:]
    random.Random(5).shuffle(shuffled)

    t0 = time.perf_counter()
    mine = ChainedHashTable()
    for sku, name, price in data:
        mine.put(sku, name)
    build_mine = time.perf_counter() - t0

    t0 = time.perf_counter()
    builtin = {}
    for sku, name, price in data:
        builtin[sku] = name
    build_dict = time.perf_counter() - t0

    t_mine, f1 = timed_lookups(mine.get, shuffled)
    t_dict, f2 = timed_lookups(builtin.get, shuffled)
    assert f1 == f2 == 100000

    names = [(s[0], s[1]) for s in data]            # plain list, for the "no hashing" baseline
    sample = shuffled[:200]
    def scan(key):
        for k, v in names:
            if k == key:
                return v
    t_scan, _ = timed_lookups(scan, sample)

    n = len(shuffled)
    print(f"\nB) 100,000 SKUs - look up every SKU once (all {n:,} found by both)")
    print(f"  Own chained table : build {build_mine:.3f} s, lookups {t_mine:.3f} s  ({t_mine / n * 1e6:.2f} us each)")
    print(f"  Built-in dict     : build {build_dict:.3f} s, lookups {t_dict:.3f} s  ({t_dict / n * 1e6:.2f} us each)")
    print(f"  Plain list scan   : {t_scan / len(sample) * 1e6:,.1f} us each  (measured on 200 lookups only)")
    print(f"  Own table at the end: {mine.capacity:,} buckets, load {mine.size / mine.capacity:.2f}, "
          f"longest chain {mine.longest_chain()}")
    print(f"  dict is about {t_mine / t_dict:.1f}x faster than the own table")
    return {"collisions_in_demo": collisions, "own_total": t_mine, "dict_total": t_dict,
            "own_us": t_mine / n * 1e6, "dict_us": t_dict / n * 1e6, "scan_us": t_scan / len(sample) * 1e6,
            "own_build": build_mine, "dict_build": build_dict, "capacity": mine.capacity,
            "load": mine.size / mine.capacity, "longest_chain": mine.longest_chain(),
            "ratio": t_mine / t_dict}


if __name__ == "__main__":
    main()

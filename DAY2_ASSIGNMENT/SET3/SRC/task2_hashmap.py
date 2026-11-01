class HashMap:
    """Hash map with separate chaining; resizes when load factor > 0.75."""
    def __init__(self, capacity=8):
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _index(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        b = self.buckets[self._index(key)]
        for pair in b:
            if pair[0] == key:
                pair[1] = value; return
        b.append([key, value]); self.size += 1
        if self.size / len(self.buckets) > 0.75:
            self._resize()

    def get(self, key, default=None):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def _resize(self):
        old = self.buckets
        self.buckets = [[] for _ in range(len(old) * 2)]
        self.size = 0
        for b in old:
            for k, v in b:
                self.put(k, v)

    def items(self):
        return [(k, v) for b in self.buckets for k, v in b]

def build_lookup(scans):
    """trackingNo -> latest scan record."""
    m = HashMap()
    for s in scans:
        m.put(s["trackingNo"], s)
    return m

def find_double_scans(scans):
    """Parcels scanned more than once at the same hub at the same time.
    Returns sorted list of (trackingNo, hubCode, scannedAt, count)."""
    counts = HashMap()
    for s in scans:
        key = (s["trackingNo"], s["hubCode"], s["scannedAt"])
        counts.put(key, counts.get(key, 0) + 1)
    return sorted((k[0], k[1], k[2], c) for k, c in counts.items() if c > 1)

def linear_lookup(scans, tracking_no):
    for i, s in enumerate(scans):
        if s["trackingNo"] == tracking_no:
            return i
    return -1

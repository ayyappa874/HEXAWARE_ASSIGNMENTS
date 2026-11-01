def stable_hash(key):
    """djb2 hash of the key's text. Same result on every run and computer
    (Python's built-in hash() for strings changes on every run)."""
    h = 5381
    for ch in repr(key):
        h = (h * 33 + ord(ch)) & 0xFFFFFFFF
    return h

class HashMap:
    """Separate-chaining hash map. Collisions: keys that land in the same
    bucket sit in that bucket's list and are compared one by one."""
    def __init__(self, capacity=8):
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _index(self, key):
        return stable_hash(key) % len(self.buckets)

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

    def longest_chain(self):
        return max(len(b) for b in self.buckets)

    def collisions(self):
        """Number of keys that share a bucket with an earlier key."""
        return sum(len(b) - 1 for b in self.buckets if len(b) > 1)

def normalise(policy_no, incident_date):
    """Ignore letter case and ALL spaces inside the policy number."""
    return ("".join(policy_no.split()).upper(), incident_date.strip())

def find_duplicates(claims, table=None):
    """Group claim IDs that share the same normalised (policy, date).
    Returns sorted list of (key, [claimIds]) for groups of 2 or more."""
    table = table or HashMap()
    for c in claims:
        key = normalise(c["policyNo"], c["incidentDate"])
        group = table.get(key)
        if group is None:
            table.put(key, [c["claimId"]])
        else:
            group.append(c["claimId"])
    return sorted((k, sorted(v)) for k, v in table.items() if len(v) > 1)

def find_duplicates_pairwise(claims):
    """Slow check: compare every pair. O(n^2). Used only to cross-check."""
    groups = {}
    for i in range(len(claims)):
        ki = normalise(claims[i]["policyNo"], claims[i]["incidentDate"])
        for j in range(i + 1, len(claims)):
            if ki == normalise(claims[j]["policyNo"], claims[j]["incidentDate"]):
                groups.setdefault(ki, {claims[i]["claimId"]}).add(claims[j]["claimId"])
    return sorted((k, sorted(v)) for k, v in groups.items())

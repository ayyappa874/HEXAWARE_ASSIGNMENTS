import random

class Node:
    def __init__(self, code):
        self.code, self.left, self.right = code, None, None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, code):
        """Returns True if inserted, False if duplicate."""
        if self.root is None:
            self.root = Node(code); self.size += 1; return True
        cur = self.root
        while True:
            if code == cur.code:
                return False
            side = "left" if code < cur.code else "right"
            nxt = getattr(cur, side)
            if nxt is None:
                setattr(cur, side, Node(code)); self.size += 1; return True
            cur = nxt

    def search(self, code):
        """Returns (found, comparisons)."""
        cur, steps = self.root, 0
        while cur is not None:
            steps += 1
            if code == cur.code:
                return True, steps
            cur = cur.left if code < cur.code else cur.right
        return False, steps

    def height(self):
        """Height in nodes (empty tree = 0). Iterative level count."""
        if self.root is None:
            return 0
        level, h = [self.root], 0
        while level:
            h += 1
            level = [c for n in level for c in (n.left, n.right) if c]
        return h

    def inorder(self):
        out, stack, cur = [], [], self.root
        while stack or cur:
            while cur:
                stack.append(cur); cur = cur.left
            cur = stack.pop(); out.append(cur.code); cur = cur.right
        return out

def build(codes):
    t = BST()
    for c in codes:
        t.insert(c)
    return t

def make_codes(n):
    return [f"H{i:05d}" for i in range(n)]

def height_experiment(n=1000, seed=7):
    codes = make_codes(n)
    shuffled = codes[:]; random.Random(seed).shuffle(shuffled)
    return build(codes).height(), build(shuffled).height()

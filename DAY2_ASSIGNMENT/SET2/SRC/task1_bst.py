class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        """Returns True if inserted, False if the claim ID already exists."""
        if self.root is None:
            self.root = Node(key); self.size += 1; return True
        cur = self.root
        while True:
            if key == cur.key:
                return False
            side = "left" if key < cur.key else "right"
            nxt = getattr(cur, side)
            if nxt is None:
                setattr(cur, side, Node(key)); self.size += 1; return True
            cur = nxt

    def search(self, key):
        """Returns (found, comparisons)."""
        cur, steps = self.root, 0
        while cur is not None:
            steps += 1
            if key == cur.key:
                return True, steps
            cur = cur.left if key < cur.key else cur.right
        return False, steps

    def inorder(self):
        """Left, node, right. Gives SORTED order."""
        out, stack, cur = [], [], self.root
        while stack or cur:
            while cur:
                stack.append(cur); cur = cur.left
            cur = stack.pop(); out.append(cur.key); cur = cur.right
        return out

    def preorder(self):
        """Node, left, right. Gives the order to copy/rebuild the tree."""
        out, stack = [], [self.root] if self.root else []
        while stack:
            n = stack.pop(); out.append(n.key)
            if n.right: stack.append(n.right)
            if n.left: stack.append(n.left)
        return out

    def postorder(self):
        """Left, right, node. Children come before parent (safe delete order)."""
        out, stack = [], [self.root] if self.root else []
        while stack:
            n = stack.pop(); out.append(n.key)
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)
        out.reverse()
        return out

def build(keys):
    t = BST()
    for k in keys:
        t.insert(k)
    return t

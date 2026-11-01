"""Task 1 - Binary Search Tree of product categories (insert, search, 3 traversals)."""
from common import load_categories


class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        """Add a category. Smaller goes left, bigger goes right. Duplicates are ignored."""
        if self.root is None:
            self.root = Node(key)
            self.size = 1
            return True
        current = self.root
        while True:
            if key == current.key:
                return False
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    break
                current = current.right
        self.size += 1
        return True

    def search(self, key):
        """Returns (found, comparisons)."""
        current, comparisons = self.root, 0
        while current is not None:
            comparisons += 1
            if key == current.key:
                return True, comparisons
            current = current.left if key < current.key else current.right
        return False, comparisons

    def inorder(self):
        """Left, Node, Right  -> gives the keys in sorted order."""
        out = []
        def walk(node):
            if node:
                walk(node.left)
                out.append(node.key)
                walk(node.right)
        walk(self.root)
        return out

    def preorder(self):
        """Node, Left, Right  -> visits a parent before its children."""
        out = []
        def walk(node):
            if node:
                out.append(node.key)
                walk(node.left)
                walk(node.right)
        walk(self.root)
        return out

    def postorder(self):
        """Left, Right, Node  -> visits children before their parent."""
        out = []
        def walk(node):
            if node:
                walk(node.left)
                walk(node.right)
                out.append(node.key)
        walk(self.root)
        return out

    def height(self):
        """Number of levels (a tree with only a root has height 1)."""
        def h(node):
            return 0 if node is None else 1 + max(h(node.left), h(node.right))
        return h(self.root)

    def tree_lines(self):
        """Text picture of the tree (each level indented, L = left child, R = right child)."""
        lines = []
        def walk(node, indent, tag):
            lines.append(f"{indent}{tag}{node.key}")
            if node.left:
                walk(node.left, indent + "    ", "L: ")
            if node.right:
                walk(node.right, indent + "    ", "R: ")
        if self.root:
            walk(self.root, "", "")
        return lines


def build(categories):
    tree = BST()
    for c in categories:
        tree.insert(c)
    return tree


def main():
    categories = load_categories()
    tree = build(categories)
    print(f"Inserted {tree.size} categories in this order:")
    print("  " + ", ".join(categories))

    print("\nTree shape (L = left child, R = right child):")
    for line in tree.tree_lines():
        print("  " + line)

    print("\nTraversals:")
    print("  Inorder   (Left, Node, Right):", tree.inorder())
    print("  Preorder  (Node, Left, Right):", tree.preorder())
    print("  Postorder (Left, Right, Node):", tree.postorder())

    print("\nSearching:")
    for name in ("Garden", "Grocery", "Watches", "Laptops"):
        found, steps = tree.search(name)
        print(f"  {name:<9} -> {'found' if found else 'NOT found'} after {steps} comparisons")

    balanced_height = tree.height()
    worst = build(sorted(categories))
    print(f"\nTree height with the file's insert order : {balanced_height} levels")
    print(f"Same 15 categories inserted A to Z       : {worst.height()} levels (a straight line)")
    found, steps = worst.search("Watches")
    print(f"  Searching 'Watches' in that tree takes {steps} comparisons")
    return {"height": balanced_height, "sorted_height": worst.height(), "sorted_search_steps": steps,
            "inorder_is_sorted": tree.inorder() == sorted(categories)}


if __name__ == "__main__":
    main()

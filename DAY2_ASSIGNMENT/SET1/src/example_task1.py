# Example 1 - build a small category tree and read it three ways
from task1_bst import BST

tree = BST()
for name in ["Grocery", "Clothing", "Sports", "Books"]:
    tree.insert(name)

print("Inorder  :", tree.inorder())      # alphabetical
print("Preorder :", tree.preorder())
print("Postorder:", tree.postorder())

found, steps = tree.search("Books")
print(f"Search 'Books': found={found} after {steps} comparisons")
found, steps = tree.search("Toys")
print(f"Search 'Toys' : found={found} after {steps} comparisons")

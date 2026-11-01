from task1_bst import build
t = build(["NAG","DEL","BOM","PNQ","HYD","BLR","MAA","CCU","AMD","JAI"])
print("In-order :", t.inorder())
print("Height   :", t.height())
print("MAA      :", t.search("MAA"))
print("XYZ      :", t.search("XYZ"))
print("Sorted-input height:", build(sorted(t.inorder())).height())

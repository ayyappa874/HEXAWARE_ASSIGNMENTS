from task1_bst import build
t = build(["CL1050","CL1020","CL1080","CL1010","CL1030"])
print("Inorder  :", t.inorder())
print("Preorder :", t.preorder())
print("Postorder:", t.postorder())
print("CL1030   :", t.search("CL1030"))

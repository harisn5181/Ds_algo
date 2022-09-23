def num_leaf_nodes(root):
    if root ==None:
        return 0
    if root.left==None and root.right ==None:
        return 1
    numleft=num_leaf_nodes(root.left)
    numright=num_leaf_nodes(root.right)
    return numleft+numright

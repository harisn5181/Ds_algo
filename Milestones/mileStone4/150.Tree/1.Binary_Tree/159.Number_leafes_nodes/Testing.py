def Leaf_nodes(root):
    
    if root==None:
        return 0
    
    if root.left ==0 and root.right ==0:
        return 1
    
    l=Leaf_nodes(root.left)
    r=Leaf_nodes(root.right)
    
    return l+r
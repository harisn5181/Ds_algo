def node_exist(root,x):
    if root==None:
        return False
    
    elif root.data==x:
        return True
    else:
        return node_exist(root.left) or node_exist (root.right)
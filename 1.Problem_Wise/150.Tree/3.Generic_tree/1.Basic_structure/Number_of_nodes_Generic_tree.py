def numnodes(root):
    if root==None:
        return 0
    count= 1
    for child in root.children:
        count=count+numnodes(child)#1+1+
    return count
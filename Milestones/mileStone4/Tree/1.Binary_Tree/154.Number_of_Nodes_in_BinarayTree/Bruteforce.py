def numNode(root):
    if root ==None:
        return 0
    leftcount=numNode(root.left)
    rightcount=numNode(root.right)
    return  1+leftcount+rightcount
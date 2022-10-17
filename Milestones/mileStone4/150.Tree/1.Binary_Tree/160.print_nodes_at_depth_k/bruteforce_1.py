def printDepthk(root,k):
    if root = None:
        return
    if k ==0 :
        print(root.data)
        return
    printDepthk(root.left,k-1)
    printDepthk(root.right,k-1)


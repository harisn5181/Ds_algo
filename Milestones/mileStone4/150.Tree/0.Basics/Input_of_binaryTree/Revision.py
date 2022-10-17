import queue

class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def treelevelwiseinput():
    print("enter the root Node: ")
    rootHeadData= int(input())

    if rootHeadData==-1:
        return
    rootHeadData=Binarytree(rootHeadData)
    q=queue.Queue()
    q.put(rootHeadData)

    while not(q.empty()):
        currentnode=q.get()

        print("Enter left child",currentnode.data)
        rootData=int(input())
        if rootData != -1:
            root=Binarytree(rootData)
            q.put(root)
            currentnode.left=root

        print("Enter right Child",currentnode.data)
        rootData=int(input())
        if rootData != -1:
            root=Binarytree(rootData)
            q.put(root)
            currentnode.right=root

    return rootHeadData

#print Preorderwise
def printTree(root):
    if root ==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

root=treelevelwiseinput()
printTree(root)
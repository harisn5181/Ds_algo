import queue
from sys import stdin


class binaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def takeInputLevelWise():
    levelOrder = [ 1, 2 , 3 , 4, 5, 6,7 ,-1 ,-1,-1,-1,-1,-1,-1,-1]

    start=0

    root=binaryTree(levelOrder[start])
    start += 1

    q=queue.Queue()
    q.put(root)



    while not q.empty():

        currentNode=q.get() #5


        leftChild=levelOrder[start] # -1
        start+=1 #8

        if leftChild !=-1:
            leftNode=binaryTree(leftChild)
            currentNode.left=leftNode
            q.put(leftNode)

        rightChild=levelOrder[start] #-1
        start+=1 #9

        if rightChild !=-1:
            rightNode=binaryTree(rightChild)
            currentNode.right=rightNode
            q.put(rightNode)

    return root
def preorder(root):
    if root ==None:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def heightTree(root):
    if not root:
        return 0

    return 1 + max(heightTree(root.left), heightTree(root.right))



root=takeInputLevelWise()
preorder(root)
heightTree(root)

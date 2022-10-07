from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)

    while not pendingNodes.empty(): 
       
        frontNode = pendingNodes.get()
    
        print((str(frontNode.data) + ":L:"), end = "")

        if frontNode.left is not None :
            pendingNodes.put(frontNode.left)
            print((str(frontNode.left.data) + ",R:"), end = "")

        else :
            print(("-1,R:"), end = "")


        if frontNode.right is not None :
            pendingNodes.put(frontNode.right)
            print((frontNode.right.data))

        else :
            print(-1)
























    



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder =[8, 3, 10, 1 ,6 ,-1 ,14, -1, -1, 4, 7 ,13, -1 ,-1, -1, -1, -1, -1, -1]
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)
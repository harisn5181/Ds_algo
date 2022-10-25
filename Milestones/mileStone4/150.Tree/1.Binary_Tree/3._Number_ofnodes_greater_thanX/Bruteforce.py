from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



        
def countNodesGreaterThanX(root,x):
    if root ==None:
        return 0
    left=countNodesGreaterThanX(root.left,x)
    right=countNodesGreaterThanX(root.right,x)
    if root.data>x:
        return 1+left+right
    else:
        return left+right
        


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = [ 1, 2 , 3 , 4, 5, 6,7 ,-1 ,-1,-1,-1,-1,-1,-1,-1]
    start = 0
    length = len(levelOrder)

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
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
x = int(stdin.readline().strip())

count = countNodesGreaterThanX(root, x)
print(count)
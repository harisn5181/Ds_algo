import queue
from sys import stdin

# Taking level-order input using fast I/O method

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None






def takeInput():
    levelOrder = [2 ,4, 5, 6, -1, -1 ,7 ,20, 30, 80, 90, -1, -1, 8, -1, -1, 9 ,-1, -1 ,-1 ,-1, -1, -1 ]
    start = 0

    length = len(levelOrder)

    if length == 1:
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
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root == None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


def diameterOfBinaryTree(root):

    if root ==None:
        return 0,0

    lh,left = diameterOfBinaryTree(root.left)
    rh,right = diameterOfBinaryTree(root.right)

    height= 1+  max (lh,rh)
    daimeter= 1+ lh+ rh

    return height,daimeter




# Main
root = takeInput()

print(diameterOfBinaryTree(root))


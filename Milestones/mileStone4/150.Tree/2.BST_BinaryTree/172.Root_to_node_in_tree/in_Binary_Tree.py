from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None






def nodetoRootPath (root,s):
    if root ==None:
        return None
    if root.data == s:
        l=list()
        l.append(root.data)
        return l

    leftoutput=nodetoRootPath(root.left,s)
    if leftoutput != None:
        leftoutput.append(root.data)
        return leftoutput

    rightoutput=nodetoRootPath(root.right,s)
    if rightoutput != None:
        rightoutput.append(root.data)
        return rightoutput
    else:
        return None




# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = [8 ,5 ,10, 2, 6, -1, -1, -1, -1 ,-1, 7, -1, -1]
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


# Main
root = takeInput()

root=nodetoRootPath(root,2)

print(root)
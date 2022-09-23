from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):


    q = queue.Queue()
    q.put(root)


    while (not (q.empty())):
        current_node = q.get()


        print(current_node,end="")
        if current_node != -1:

            left_child=current_node.left
            right_child=current_node.right
            if left_child==None :
                q.put(-1)

            else:

                q.put(left_child)
            if right_child ==None:
                q.put(-1)
            else:

                q.put(right_child)









# Your code goes here


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = [1, 2, 3, 1, 5, -1,  8, -1, -1, -1, -1, -1, -1]
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


# Main
root = takeInput()
printLevelWise(root)
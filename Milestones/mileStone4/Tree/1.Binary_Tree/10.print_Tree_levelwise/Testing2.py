import queue


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():
    levelOrder = [8, 3, 10, 1, 6, -1, 14, -1, -1, 4, 7, 13, -1, -1, -1, -1, -1, -1, -1]
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


    q=queue.Queue()
    q.put(root)

    while not(q.empty()):
        currentNode=q.get()
        print(currentNode.data, end=":L:")

        left=currentNode.left

        if left == None:
            print(-1,end=",R:")
        else:
            print(left.data,end=",R:")
            q.put(left)

        right= currentNode.right
        if right==None:
            print(-1)
        else:
            print(right.data)
            q.put(right)


# Main
root = takeInput()
printLevelWise(root)
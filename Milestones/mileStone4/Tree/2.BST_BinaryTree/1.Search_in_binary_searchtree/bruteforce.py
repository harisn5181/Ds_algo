import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Solution


def searchInBST(root, k):
    global Found

    if root is None:
        Found = False
        return Found
    if root.data == k:

        Found = True
        return Found


    if k >= root.data:
        searchInBST(root.right,k)
    else:
        searchInBST(root.left,k)
    return Found







def takeInput():
    levelOrder = [4 ,-1 ,-1]
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

root =takeInput()
k = 4
Found=False
ans = searchInBST(root, k)
if ans:
    print("true")
else:
    print("false")
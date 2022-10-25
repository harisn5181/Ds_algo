import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        




    # Solution


def searchInBST(root, k):


    if root is None:

        return False
    if root.data == k:


        return True


    if k >= root.data:
        return searchInBST(root.right,k)
    else:
        return searchInBST(root.left,k)








def takeInput():
    levelOrder = [8 ,5, 10, 2, 6, -1, -1, -1, -1, -1, 7 ,-1, -1]
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
k = 7

ans = searchInBST(root, k)
if ans:
    print("true")
else:
    print("false")
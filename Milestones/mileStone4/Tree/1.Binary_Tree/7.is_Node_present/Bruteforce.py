import queue
    
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def isNodePresent(root, x):
    
    if root == None :
        return False

    # If the current node value is equal to x, return true.
    elif root.data == x :
        return True

    # Check whether x is present in the left tree or right tree of the current node.
    else :
        return isNodePresent(root.left, x) or isNodePresent(root.right, x)
    # Write your code here.
    




















# To build the tree
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)

    if length<=0 or levelorder[0]==-1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:

            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:

            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

x = int(input())

present = isNodePresent(root, x)

if present:
    print('true')
else:
    print('false')
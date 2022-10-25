import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def constructBST(lst):

    ans = solve(lst, 0, n - 1)
    return ans


def solve(lst, si, ei):


    return
    # when start index crosses end index then simply return
    if si > ei:
        return None
    mid = (si + ei) // 2
    midP = lst[mid]

    # creating a root node of the mid point of array
    # so left side of this mid will be lesser than mid and right side will be greater than mid
    root = BinaryTreeNode(midP)

    # recusive call on leftsubtree and rightsubtree
    leftSubtree = solve(lst, si, mid - 1)
    rightSubtree = solve(lst, mid + 1, ei)

    root.left = leftSubtree
    root.right = rightSubtree

    return root


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = 7
if (n > 0):
    lst = [1,2,3,4,5,6,7]
else:
    lst = []
root = constructBST(lst)
preOrder(root)
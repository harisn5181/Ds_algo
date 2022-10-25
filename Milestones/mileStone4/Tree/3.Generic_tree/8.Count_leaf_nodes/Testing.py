import sys


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    if tree == None:
        return

    if len(tree.children) == 0:
        return 1

    count = 0
    for child in tree.children:
        count += leafNodeCount(child)

    return count


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
sys.setrecursionlimit(10 ** 6)
arr=[10, 3, 20 ,30, 40, 2, 40, 50, 0, 0 ,0,0 ]
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))


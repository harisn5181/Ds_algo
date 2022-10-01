
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def maxDataNode(tree):
    global l
    if tree is None:
        return
    if l is None:
        l = tree
    elif tree.data > l.data:
        l = tree
    for i in tree.children:
        maxDataNode(i)
    return l


def numnodes(root):
    if root == None:
        return 0
    minimum = root.data

    for child in root.children:
        minimum = max(numnodes(child), minimum)

    return minimum

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
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
l = None
tree = createLevelWiseTree(arr)
#print(maxDataNode(tree))
print(numnodes(tree))
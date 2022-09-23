#it have some edge cases

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []



def nextLargest(tree, n):
    global next_largest

    if tree ==None:
        return

    if  tree.data > n and tree.data < next_largest:
        next_largest= tree.data

    for child in tree.children:
        nextLargest(child,n)

    return next_largest







def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = [10 ,3 ,20, 30, 40, 2, 40, 50, 0, 0 ,0, 0]
n = 15
tree = createLevelWiseTree(arr)
next_largest=99999999999999999999999999999999999999999999999999999999999999999999999

print(nextLargest(tree,n))
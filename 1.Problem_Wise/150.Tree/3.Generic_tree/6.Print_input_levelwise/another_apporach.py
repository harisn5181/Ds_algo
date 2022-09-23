


#Code from ta



import sys
import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(tree):
    q=queue.Queue()
    q.put(tree)
    while not q.empty():
        a=q.get()
        n=len(a.children)
        print(a.data, end=':')
        for i in range(n):
            print(a.children[i].data, end=',')
            q.put(a.children[i])

        print()

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
sys.setrecursionlimit(10**6)
arr = [10, 3, 20, 30, 40, 2, 40, 50, 0, 0, 0, 0 ]
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)





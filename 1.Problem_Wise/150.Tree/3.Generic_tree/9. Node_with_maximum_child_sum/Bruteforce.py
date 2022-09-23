from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans


def maxSumNode(tree):
    if tree == None:
        return 0

    max_child_sum = 0
    max_child_node = None
    root_sum = tree.data
    for child in tree.children:
        root_sum += child.data
        node, sum = maxSumNode(child)
        if sum > max_child_sum:
            max_child_sum = sum
            max_child_node = node

    if max_child_sum > root_sum:
        return node, max_child_sum

    return tree, root_sum


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
arr = [10 ,3 ,20, 30, 40, 2, 40, 50, 0, 0 ,0, 0]
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)
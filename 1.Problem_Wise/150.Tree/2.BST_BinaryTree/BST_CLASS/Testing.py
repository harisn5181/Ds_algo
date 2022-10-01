class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeH(self, root):
        if root == None:
            return
        print(root.data, end=":")
        if root.left is not None:
            print("L:{}".format(root.left.data), end=",")
        if root.right is not None:
            print("R:{}".format(root.right.data), end="")
        print()
        self.printTreeH(root.left)
        self.printTreeH(root.right)
        return

    def printTree(self):
        self.printTreeH(self.root)
        return

    def searchHeavyIncrement(self, root, data):
        if root == None:
            return False
        if data < root.data:
            return self.searchHeavyIncrement(root.left, data)
        elif data > root.data:
            return self.searchHeavyIncrement(root.right, data)
        else:
            return True

    def search(self, data):
        return self.searchHeavyIncrement(self.root, data)

    def insertHeavyIncrement(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if data <= root.data:
            root.left = self.insertHeavyIncrement(root.left, data)
        else:
            root.right = self.insertHeavyIncrement(root.right, data)
        return root

    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHeavyIncrement(self.root, data)

    def deleteHeavyIncrement(self, root, data):
        if root == None:
            return False, None
        if data < root.data:
            bl, root.left = self.deleteHeavyIncrement(root.left, data)
            return bl  and root
        elif data > root.data:
            br, root.right = self.deleteHeavyIncrement(root.right, data)
            return br and root
        else:
            if root.left == None and root.right == None:
                return True, None
            elif root.left == None:
                return True, root.right
            elif root.right == None:
                return True, root.left
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data = temp.data
                tempb, root.right = self.deleteHeavyIncrement(root.right, temp.data)
                return True, root
        return (bl or br), root

    def delete(self, data):
        deleted,newRoot = self.deleteHeavyIncrement(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root=newRoot
        return deleted
        return

    def count(self):
        return self.numNodes


b = BST()
q = int(input())
while (q > 0):
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q -= 1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
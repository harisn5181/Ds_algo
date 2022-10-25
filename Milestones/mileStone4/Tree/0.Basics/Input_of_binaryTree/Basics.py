#application

#File system in our computer
#Binary Tree
#Having upto 2 nodes

class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def printTree(root):
    if root ==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)


T1=BinaryTree(1)
T2=BinaryTree(4)
T3=BinaryTree(5)

T1.left=T2
T1.right=T3

printTree(T1)
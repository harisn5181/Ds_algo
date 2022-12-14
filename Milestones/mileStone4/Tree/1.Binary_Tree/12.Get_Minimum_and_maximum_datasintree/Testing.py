from sys import stdin, setrecursionlimit
import queue
import math
setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum

def getMinAndMax(root) :
    #Your code goes here
    if root==None:
        return 0
    left=getMinAndMax(root.left)
    right=getMinAndMax(root.right)
    #minimum= min(left,right,root.data) 
    maximum=max(left,right,root.data)
    
    return maximum 
    

#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = [8 ,3 ,10, 1 ,6, -1, 14, -1, -1, 4 ,7 ,13 ,-1 ,-1, -1, -1, -1 ,-1 ,-1]
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

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()

max= getMinAndMax(root)
print(max)
#print(str(str(pair.minimum) + " " + str(pair.maximum)))
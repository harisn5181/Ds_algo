from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def changeToDepthTree(root,k) :
	#Your code goes here
    if root == None or k<0:
        return
    if k==0:
        print(root.data)
        return
    changeToDepthTree(root.left, k-1)
    changeToDepthTree(root.right, k-1)        

def nodesAtDistanceK(root, node, k) :
	#Your code goes here
    if root is None:
        return None
    if root.data==node:
        changeToDepthTree(root,k)
        return 0
    d1 = nodesAtDistanceK(root.left, node, k)
    if d1 != None:
        if d1 + 1==k:
            print(root.data)
        else:
           changeToDepthTree(root.right,k-d1-2)
        return 1 + d1
    
    d2 = nodesAtDistanceK(root.right, node, k)
    if d2 != None:
        if(d2+1==k):
            print(root.data)
        else:
            changeToDepthTree(root.left,k-d2-2)
        return 1 + d2




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

target =3
k = 1

nodesAtDistanceK(root, target, k)
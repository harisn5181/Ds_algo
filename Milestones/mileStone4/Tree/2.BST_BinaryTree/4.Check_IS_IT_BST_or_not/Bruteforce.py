


def minTree(root):
    if root==None:
        return 10000
    
    leftMin=minTree(root.left)
    rightMin=minTree(root.right)
    return (min(root.data,leftMin,rightMin))



def maxTree(root):
    if root==None:
        return -10000
    
    leftMin=maxTree(root.left)
    rightMin=maxTree(root.right)
    return (max(root.data,leftMin,rightMin))


def isBst(root):
    if root ==None:
        return True
    
    leftMax=maxTree(root.left)   #3
    rightMin=minTree(root.right) #5
    
    if root.data >rightMin or root.data <=leftMax:
        return False
    
    isleftBst  =  isBst(root.left) #
    isRightBst = isBst(root.right)
    return isleftBst and isRightBst
    
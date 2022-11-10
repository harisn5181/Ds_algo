


def isBst2(root):
    if root ==None:
        return 10000,-10000,True    
    
    leftMin,leftMax,isLeftBst=isBst2(root.left) #2
    rightMin,rightMax,isRightBst=isBst2(root.right)
    
    minimum = min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)
    
    isTreeBst=True
    
    if root.data <=leftMax or root.data >rightMin:
        isTreeBst=False
    if not(isLeftBst) or not (isRightBst):
        isTreeBst=False
        
    return minimum,maximum,isTreeBst



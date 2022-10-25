def isBst3(root,min_range,max_range):
    if root==None:
        return True
    
    if root.data<min_range or root.data >max_range:
        return False
    
    isLeftWithinconstraints=isBst3(root.left,min_range,root.data -1)
    
    isRightWithinConstraints =isBst3(root.right,root.data,max_range)
    
    
    return isLeftWithinconstraints and isRightWithinConstraints
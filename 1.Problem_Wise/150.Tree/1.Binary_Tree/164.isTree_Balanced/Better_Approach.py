def getHeightAndCheckBalanced(root):
	if root==None:
		return 0 ,True
	lh,isleftbalanced=getHeightAndCheckBalanced(root.left)
	rh,isrightbalanced=getHeightAndCheckBalanced(root.right)

	h=1+max(lh,rh)
	if lh-rh>1 or rh-lh>1:
		return h,False
	if isleftbalanced and isrightbalanced:
		return h,True
	else:
		return h,False
def height(root):
	if root==None:
		return 0
	return 1+ max(height(root.left),height(root.right))



def is_balanced(root):
	if root== None:
		return True
	lh=height(root.left)
 
	rh=height(root.right)
 
	if lh-rh>1 or rh-lh>1 :
		return False
	isleftBalanced=is_balanced(root.left)
	isrightBalanced=is_balanced(root.right)
	if isrightBalanced and isleftBalanced:
		return True
	else:
		return False









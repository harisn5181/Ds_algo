
def treeinput():
	rootData=int(input())

	if rootData==-1:
		return None

	root=BinaryTreeNode(rootData)
	leftTree=treeinput()
	righttree=treeinput()
	root.left=lefttree
	root.right=righttre
	return root

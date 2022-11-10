







def remove(root):
    if root ==None:
        return None

    if root.left == None and root.right == None:
        return None
    root.left=remove(root.left)
    root.right=remove(root.right)
    return root

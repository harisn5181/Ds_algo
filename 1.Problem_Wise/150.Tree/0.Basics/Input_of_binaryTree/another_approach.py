import queue
def takelevelwisetreeinput():
    q=queue.Queue()
    print("Enter root")
    rootdata=int(input())
    if (rootdata== -1):
        return None
    root=Binarytreenode(rootdata)
    q.put(root)
    while (not (q.empty())):
        current_node=q.get()
        print("Enter left child of ",current_node.data)
        leftchilddata=int(input())
        if leftchilddata != -1:
            leftchild =Binarytreenode(leftchilddata)
            current_node.left=leftchild
            q.put(leftchilddata)


        print("Enter right child of ", current_node.data)
        rightchilddata = int(input())
        if rightchilddata != -1:
            rightchild = Binarytreenode(rightchilddata)
            current_node.right = rightachild
            q.put(rightchild)
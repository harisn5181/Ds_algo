import  queue


def taketreeInputlevelwise():
    q=queue.Queue()
    print("enter root")
    rootdata=int(input())
    if rootdata == -1:
        return None
    root=TreeNode(rootdata)
    q.put(root)

    while (not(q.empty())):
        current_node=q.get()
        print("enter number of children for",current_node.data)
        n_node=int(input())

        for i in n_node:
            print("child for",current_node)
            child=int(input())
            root=Treenode(child)
            current_node.children.append(child)
            q.put(child)
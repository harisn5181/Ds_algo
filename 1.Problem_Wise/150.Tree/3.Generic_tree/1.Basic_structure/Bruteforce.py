class Generic_tree:
    def __int__(self,data):
        self.data=data
        children=list()

n1=Generic_tree(5)
n2=Generic_tree(2)
n3=Generic_tree(9)
n4=Generic_tree(8)
n5=Generic_tree(7)
n6=Generic_tree(15)
n7=Generic_tree(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)
#iteravative with recursion . A nice combination
#This will print list of elements in this root by preorderwise
def printTree(root):
    print(root.data)
    for child in root.children:
        printTree(child)


#Take_input()
def takeTreeinput():
    print("Enter root data")
    rootdata =int(input())
    if rootdata== -1:
        return None

    root=Generic_tree(rootdata)

    print("Enter number of children of ",rootdata)
    childrenCount= int(input())
    for i in range(childrenCount):
        child=takeTreeinput()
        root.children.append(child)


    return root

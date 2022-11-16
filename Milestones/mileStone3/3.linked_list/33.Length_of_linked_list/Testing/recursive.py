class Node:
    def __init__(self,data) :
        
        self.data=data
        self.next=None
        
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4

def count_linked_list(head):
    if head ==None:
        return 0
    return 1+count_linked_list(head.next)        
print(count_linked_list(node1))
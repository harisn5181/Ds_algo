class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    
node1=Node(10)
node2=Node(20)
node3=Node(10)
node4=Node(20)
node1.next=node2
node2.next=node3
node3.next=node4
    
def size_linked_list(head):
    count=0
    oldhead=head
    while head is not None:
        head=head.next
        count=count+1    
    return count    
print(size_linked_list(node1))
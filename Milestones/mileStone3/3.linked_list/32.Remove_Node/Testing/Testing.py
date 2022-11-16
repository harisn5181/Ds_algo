from sys import stdin


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



def takeinput():

    head=None
    tail =None
    i=0
    datas =[1,2,3,4,5]

    while i< len(datas) and datas[i]!= -1:

        newnode=Node(datas[i])
        if head is None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=tail.next
        i=i+1

    return head
#iterative  1 2 3 4 5
def remove_ithelement(head,x,i=0):
    if head == None:
        return -1

    prev=None
    curr=head
    while curr is not None:
        if i ==x and prev!= None:
            prev.next=curr.next
            return head
        if i == x and prev == None:
            head=head.next

        prev=curr
        curr=curr.next
        i=i+1

    return head


def print_linkedlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next

head=takeinput()
head=remove_ithelement(head,4)
print_linkedlist(head)
from sys import stdin

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def takeinput():

    head=None
    tail =None
    i=0
    datas =[0,1,2,3,4,5]

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
#Recursvie 1 2 3 4 5
def remove_ithelement(head,x,i=0):
    if head == None:
        return None
    if x==i:
        head=head.next
        return head
    ans=remove_ithelement(head.next,x,i=i+1)
    head.next = ans
    return head


def print_linkedlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next

head=takeinput()
head=remove_ithelement(head,0)
print_linkedlist(head)
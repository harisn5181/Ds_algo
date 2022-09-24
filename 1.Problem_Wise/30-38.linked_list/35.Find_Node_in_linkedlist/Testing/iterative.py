from sys import stdin

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def takeinput():

    head=None
    tail =None
    i=0
    datas =[10,20,30,40,50]

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
    if head==None:
        return -1

    while head is not None:
        if head.data==x:
            return i
        head=head.next
        i=i+1
    return -1

def print_linkedlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next

head=takeinput()
print(remove_ithelement(head,70))
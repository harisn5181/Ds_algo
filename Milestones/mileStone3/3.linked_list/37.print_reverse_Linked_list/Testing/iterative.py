#1 2 3 3 3 3 4 4
#1 2 3 4


from sys import stdin


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



def takeinput():

    head=None
    tail =None
    i=0
    datas = [1,2,3,4,5,-1]

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

def reverse(head):
    prev=None
    curr=head
    while curr is not None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev


def print_ll(head):
    while head is not None:
        print(head.data," ")
        head=head.next



head=takeinput()
head=reverse(head)
print_ll(head)
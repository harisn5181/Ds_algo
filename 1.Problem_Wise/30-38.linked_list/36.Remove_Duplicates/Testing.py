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
    datas = [10 ,10,10,10,10,-1]

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

def remove_duplicates(head):
    if head==None:
        return

    if head.next !=None:
        k = head.next
        if head.data != k.data:
            smalloutput = remove_duplicates(head.next)
            head.next = smalloutput
            return head

        else:
            return remove_duplicates(head.next)
    else:
        return head

def print_ll(head):
    while head is not None:
        print(head.data," ")
        head=head.next



head=takeinput()
head=remove_duplicates(head)
print_ll(head)
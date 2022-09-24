from sys import stdin


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



def takeinput():

    head=None
    tail =None
    i=0
    datas = list(map(int, stdin.readline().rstrip().split(" ")))

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

def print_ithelement(head,x,i=0):
    if head == None:
        return -1
    if i ==x:
        return i
    return print_ithelement(head.next,x,i=i+1)



head=takeinput()
print(print_ithelement(head,2))
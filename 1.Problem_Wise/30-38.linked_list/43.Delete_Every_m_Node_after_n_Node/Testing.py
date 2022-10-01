"""

1 2 3 4 5 6 7 8 -1
2 2

"""


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipMdeleteN(head, M, N):
    if M ==0 or N==0:
        return head
    curr=head
    prev=None
    while curr is not None:
        #skip
        i=0
        j=0

        while i < M and head is not None:
            prev=curr
            curr=curr.next
            i=i+1

        while j <N and head is not None:
            curr=curr.next
            j=j+1
        prev.next=curr
    return head






# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = [1,2,3,4,5,6,7,8]

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main

head = takeInput()

m = 2
n = 2

newHead = skipMdeleteN(head, m, n)
printLinkedList(newHead)

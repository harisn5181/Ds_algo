from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head,evenhead,eventail,oddhead,oddtail):
    if head==None:
        if oddhead is None:
            return evenhead
        else:
            oddtail.next = evenhead

        if evenhead is not None:
            eventail.next = None
        return oddhead

    if head.data%2==0:
        if evenhead.data ==None:
            evenhead=head #4
            eventail=head #4
        else:
            eventail.next=head # 4=> 2
            eventail=eventail.next #2
    else:
        if oddhead.data ==None:
            oddhead=head #5
            oddtail=head #5
        else:
            oddtail.next=head # 5=>3 =>1
            oddtail=head# 1



    return evenAfterOdd(head.next,evenhead,eventail,oddhead,oddtail)



# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = [2,4,6]

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


# to print the linked list
def printLinkedList(head):
    while head is not None:
        if head.data!=None:
            print(head.data, end=" ")
        head = head.next

    print()


# main

head = takeInput()
evenhead=Node(None)
oddhead=Node(None)
eventail=Node(None)
oddtail=Node(None)
newHead = evenAfterOdd(head,evenhead,eventail,oddhead,oddtail)
printLinkedList(newHead)


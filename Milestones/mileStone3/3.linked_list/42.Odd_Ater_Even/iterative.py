from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head):
    if head is None:
        return head
    evenHead, oddHead, evenTail, oddTail = None, None, None, None
    while head is not None:
        if (head.data % 2) == 0:
            if evenHead is None:
                evenHead = head
                evenTail = head
            else:
                evenTail.next = head
                evenTail = head
        else:
            if oddHead is None:
                oddHead = head
                oddTail = head
            else:
                oddTail.next = head
                oddTail = head
        head = head.next
    if oddHead is None:
        return evenHead
    else:
        oddTail.next = evenHead

    if evenHead is not None:
        evenTail.next = None
    return oddHead


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = [1,2,3,4,5]

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
        print(head.data, end=" ")
        head = head.next

    print()


# main

head = takeInput()
newHead = evenAfterOdd(head)
printLinkedList(newHead)


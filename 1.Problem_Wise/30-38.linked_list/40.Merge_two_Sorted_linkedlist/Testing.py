
from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists(head1, head2):
    fh = Node(3)
    ft = fh

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next

    while head1 is not None:
        ft.next = head1
        ft = ft.next
        head1 = head1.next

    while head2 is not None:
        ft.next = head2
        ft = ft.next
        head2 = head2.next

    return fh.next



def takeInput1():
    head = None
    tail = None

    datas = [1,3,5,7,9,11]

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


def takeInput2():
    head = None
    tail = None

    datas = [2,4,6,8,10]

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


# Main

head1 = takeInput1()
head2 = takeInput2()

newHead = mergeTwoSortedLinkedLists(head1, head2)
printLinkedList(newHead)


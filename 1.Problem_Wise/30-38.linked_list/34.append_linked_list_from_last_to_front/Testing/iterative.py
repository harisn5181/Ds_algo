from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def len_link(head):
    count = 0
    tail = None
    while head is not None:
        count = count + 1
        tail = head
        head = head.next
    return count, tail


def appendLastNToFirst(head, n):
    count = 1
    temp_head = head
    nodes, old_tail = len_link(head)

    if n >= nodes or n <= 1 or nodes < 1:
        return head

    x = nodes - n

    while temp_head is not None:
        if count == x:
            new_tail = temp_head
            break
        temp_head = temp_head.next
        count = count + 1

    old_tail.next = head

    head = new_tail.next

    new_tail.next = None

    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

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
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1
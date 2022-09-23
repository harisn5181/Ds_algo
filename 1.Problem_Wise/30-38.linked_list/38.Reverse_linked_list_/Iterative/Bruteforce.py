from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


# To print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


def reverse(head):
    # Write your code here
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head



head = takeInput()

ans = reverse(head)
printLinkedList(ans)


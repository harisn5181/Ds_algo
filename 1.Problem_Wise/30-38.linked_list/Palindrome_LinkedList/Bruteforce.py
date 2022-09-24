from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindrome(head):
    curr = head
    stack = []
    ispalin = True
    while curr is not None:
        stack.append(curr.data)
        curr = curr.next

    while head is not None:

        i = stack.pop()
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            return ispalin
        head = head.next
    return ispalin


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

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1
#Return head ,that will become new tail


from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedListRec(head):
    # Your code goes here
    if head is None or head.next is None:
        return head,head
    smallhead,smalltail = reverseLinkedListRec(head.next)

    smalltail.next = head
    head.next = None
    return smallhead,head


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


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()



head = takeInput()
newHead ,tail= reverseLinkedListRec(head)
printLinkedList(newHead)


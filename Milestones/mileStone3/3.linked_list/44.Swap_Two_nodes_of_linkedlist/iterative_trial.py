# i need to study this program again

from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swapNodes(head, i, j):
    if i == j:
        return head
    currentNode = head
    prev = None
    firstNode = None
    secondNode = None
    firstNodePrev = None
    secondNodePrev = None
    pos = 0
    while currentNode is not None:
        if pos == i:
            firstNodePrev = prev
            firstNode = currentNode
        elif pos == j:
            secondNodePrev = prev
            secondNode = currentNode
        prev = currentNode
        currentNode = currentNode.next
        pos += 1


    temp = secondNode.next
    firstNodePrev.next = secondNode

    secondNode.next = secondNodePrev

    secondNodePrev.next = temp

    return firstNodePrev



# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = [10, 20, 30 ,40 ,-1]
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


i = 1
j = 2

newHead = swapNodes(head, i, j)
printLinkedList(newHead)


from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNodeRec(head, n,):
    global count
    count=count+1


    if head is None :
        print("head is none ")
        count=-1
        return count

    if head.data == n:

        return count


    findNodeRec(head.next,n)
    return count




def takeInput():
    head = None
    tail = None

    datas = [-1]

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

count=-1
print(findNodeRec(head, 0))

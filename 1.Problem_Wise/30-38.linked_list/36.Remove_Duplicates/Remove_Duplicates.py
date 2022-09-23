from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicates(head):

    # Your code goes here
    prev = None
    curr = head
    temp_head=head

    while temp_head is not None:
        if prev == curr:
            while curr != prev and temp_head is not None:
                curr = curr.next
                temp_head = temp_head.next

            prev.next = curr
            print(prev.data,curr.data)


        prev = curr
        curr = curr.next

        temp_head = temp_head.next

    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = [1,2,3,3,3,3,4,4,4,5,5,7,-1]

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



def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()



head = takeInput()

heads = removeDuplicates(head)
printLinkedList(heads)


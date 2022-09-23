#Following is the Node class already written for the Linked List



from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = [10,20,30,40]

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




    
def printReverse(head):
  
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


  

head = takeInput()
printReverse(head)
printLinkedList(head)


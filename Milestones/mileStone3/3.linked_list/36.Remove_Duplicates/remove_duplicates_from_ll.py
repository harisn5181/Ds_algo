
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def removeDuplicates(head) :
    #Your code goes here
    prev=None
    curr=head
    while head is not None:
        if prev==curr:
            print("same")
        else:
            print("not same")





















    



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = [1,2,3,3]

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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
#t = int(stdin.readline().strip())


head = takeInput()

removeDuplicates(head)
    

    
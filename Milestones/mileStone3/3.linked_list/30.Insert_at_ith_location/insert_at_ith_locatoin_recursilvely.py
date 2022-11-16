from sys import stdin


class Node :
  def __init__(self,data):
    self.data=data
    self.next=None


def len_link(head):
  count=0
  while head is not None:
    count=count+1
    head=head.next

  return count  


  
def insert_linkedlist(head,i,data):
  if i <0 or i> len_link(head):
    return head

  if i ==0:
    newNode=Node(data)
    newNode.next=head
    return newNode

    
  smallhead=insert_linkedlist(head.next,i-1,data)
  head.next=smallhead
    
  
  return head
  
  



def takeinput():
  head=None
  tail = None

  datas=list(map(int,stdin.readline().rstrip().split(" ")))

  i=0

  while(i<len(datas)) and (datas[i]!= -1):
    data=datas[i]
    newNode=Node(data)

    if head is None:
      head=newNode
      tail=newNode
    else:
      tail.next=newNode
      tail=newNode

    i+=1

  return head

def printLinkedList(head):
  while head is not None:
    print(head.data,end=' ')
    head=head.next

  print()




head=takeinput()  
i=int(input())
data=int(input())
insert_linkedlist(head,i,data)
printLinkedList(head)


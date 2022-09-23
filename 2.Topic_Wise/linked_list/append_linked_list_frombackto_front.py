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


  
def insert_linkedlist(head,n):
    if n>=len_link(head) or n <=1:
        return head
    
    count=0
    temp_head=head
    x=len_link(head)-n
    while head is not None:
        if count==x:
            new_head=head
            
        tail=head
        head=head.next
        count=count+1
        
    new_head.next=head
    tail.next=temp_head
    
    while new_head is not None:
      print(new_head.data,end=' ')
      new_head=new_head.next
    
    
  
  



def takeinput():
  head=None
  tail = None

  datas=[1, 2, 3, 4 ,5]

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
#i=int(input())

insert_linkedlist(head,3)



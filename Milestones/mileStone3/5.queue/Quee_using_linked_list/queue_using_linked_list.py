class Node:
  def __init__ (self,initData):
    self.data=initData
    self.next=None


class Queue:
  def __init__(self):
    self.__head=None
    self.__tail=None
    self.__count=0

    
  def enqueue(self,element):
    newNode=Node(element)
    if self.__head is None:
      self.__head=newNode
    else:
      self.__tail.next=newNode
    self.__count=self.__count+1
    self.__tail=newNode
        
  def dequeue(self):
    if self.__head is None:

      return

    data=self.__head.data
    self.__head=self.__head.next
    self.__count=self.__count-1
    return data
    
  def isEmpty(self):
    return self.size() == 0

  def size(self):
    return self.__count

  def front(self):  
    if self.__head is None:

      return
    data=self.__head.data
    return data


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while q.isEmpty() is False:
  print(q.dequeue())

q.front()
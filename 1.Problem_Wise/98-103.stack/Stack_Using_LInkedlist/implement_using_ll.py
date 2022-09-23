class Node:
  def __init__ (self,initData):
    self.data=initData
    self.next=None

class Stack:
  def __init__ (self):
    self.__head= None
    self.__count=0

  def push(self,element):
    newNode=Node(element)
    newNode.next=self.__head
    self.__head= newNode
    self.__count=self.__count+1
    

    
    
  def pop(self):
    if self.isEmpty is True:
      print("stack is empty")
      return
    data=self.__head.data  
    self.__head=self.__head.next
    self.__count=self.__count -1 
    return data

  def top(self):
    
    if self.isEmpty is True:
       print("stack is empty")
       return
    data=self.__head.data  
    return data


  def size(self):
    return self.__count


  def isEmpty(self):
    return self.size() == 0



s=Stack()
s.push(10)
s.push(13)
s.push(15)

while s.isEmpty() is False:
  print(s.pop())





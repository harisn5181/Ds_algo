class QueueTwostacks:
    def __int__(self):
        self.__s1=[]
        self.__s2=[]

    def enque(self,data):
        #0 (n)

      while (len(self.__s1) !=0):
          self.__s2.append(self.__s1.pop())
      self.__s1.append(data)

      while(len(self.__s2) !=0):
          self.__s1.append(self.__s2.pop())
      return

    def deque(self):

        #0 (1)
        if len(self.__s1)==0:
            return -1
        return self.__s1.pop()
    def front(self):
        if len(self.__s1)==0:
            return -1
        return self.s1[-1]

    def size(self):
        return len(self.__s1)
    def isEmpty(self):


        return self.size()==0


q=QueueTwostacks()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)

while (q.isEmpty() is False):
    print(q.front())
    q.deque()

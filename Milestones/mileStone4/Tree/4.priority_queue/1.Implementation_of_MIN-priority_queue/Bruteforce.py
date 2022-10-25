
class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority



class PriorityQueue:

    def __init__(self):
        self.pq=[]

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() ==0

    def getMin(self):

        if self.isEmpty() is True:
            return None

        return self.pq[0].value



    def __percolateUp(self):

        childINdex=self.getSize()-1

        while childINdex > 0:
            
            parentIndex =(childINdex-1) //2
            
            if self.pq[childINdex].priority < self.pq[parentIndex].priority:
                
                self.pq[childINdex],self.pq[parentIndex] =self.pq[parentIndex],self.pq[childINdex]
                
                childINdex=parentIndex
            else:
                break


    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        
        self.pq.append(pqNode)
        
        self.__percolateUp()


    def __percolateDown(self):
        parentIndex = 0
        leftIndex = 2 * parentIndex + 1
        rightIndex = 2 * parentIndex + 2
        while leftIndex < self.getSize():
            
            minIndex = parentIndex
            
            if (self.pq[minIndex].priority > self.pq[leftIndex].priority):
                minIndex = leftIndex
                
            if (rightIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightIndex].priority):
                minIndex = rightIndex

            if minIndex != parentIndex:
                self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
                parentIndex = minIndex
                leftIndex = 2 * parentIndex + 1
                rightIndex = 2 * parentIndex + 2
            else:
                break


    def removeMin(self):
        if self.isEmpty():
            return None
        
        element = self.pq[0]
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        #Heapify-Down
        self.__percolateDown()
        return element.value

pq=PriorityQueue()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)

for i in range(4):
    print(pq.removeMin())
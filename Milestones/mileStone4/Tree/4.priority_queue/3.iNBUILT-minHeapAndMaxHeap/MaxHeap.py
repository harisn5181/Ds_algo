#Four import function in minHeap and maxHeap are Push , pop ,replace , Heapify

import heapq
li=[1,2,34,333,43,23]
heapq._heapify_max(li)
print(li)

print(heapq._heappop_max(li))
print(li)
heapq._heapreplace_max(li,0)
print(li)
#there is no push function directly so we do like this 
li.append(1000)
heapq._siftdown_max(li,0,len(li)-1)
print(li)
import heapq

li=[10,12,2,3,4,1,2]
heapq.heappush(li,0)
heapq.heappush(li,-1)
#print(li)
print(heapq.heappop(li))
print(li)
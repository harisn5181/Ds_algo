import heapq as pq

def peekValue(heap) :
    peekValue = pq.heappop(heap)
    pq.heappush(heap, peekValue)
    
    return peekValue

def isEmpty(heap) :
    if len(heap) != 0 :
        return False
    
    return True

def kLargest(li, k) :
    heap = []
    for i in range(k) :
        pq.heappush(heap, li[i])
    
    
    for i in range(k, len(li)) :
        if li[i] > peekValue(heap) :
            pq.heappop(heap)
            pq.heappush(heap, li[i])
            
    ans = []
    
    while not isEmpty(heap) :
        ans.append(pq.heappop(heap))
        
    return ans
     
#main

arr = [2, 12, 9, 16, 10, 5, 3 ,20, 25, 11, 1 ,8 ,6 ]
k = 4

ans = kLargest(arr, k)

for elem in ans :
	print(elem)
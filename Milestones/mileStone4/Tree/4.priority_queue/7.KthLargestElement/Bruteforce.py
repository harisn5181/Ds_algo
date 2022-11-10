import heapq




def kthLargest(lst, k):
    heap=lst[:k]
    heapq.heapify(heap)
    n=len(lst)
    for i in range(k,n):
        if heap[0]<lst[i]:
            heapq.heapreplace(heap,lst[i])
    return min(heap)
    
# Main Code

lst=[2, 6, 10, 11 ,13, 4 ,1 ,20]
k=3
ans=kthLargest(lst, k)
print(ans)
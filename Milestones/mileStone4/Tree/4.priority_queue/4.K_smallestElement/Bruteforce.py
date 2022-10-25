import heapq

def kSmallest(lst, k):
    heap = lst[:k]
    heapq._heapify_max(heap)
    n = len(lst)
    for i in range(k,n):
        if heap[0]>lst[i]:
            heapq._heapreplace_max(heap,lst[i])
    return heap
   


# Main

lst=[10,6,7,2,3,8,9,11,1]
k=4
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')
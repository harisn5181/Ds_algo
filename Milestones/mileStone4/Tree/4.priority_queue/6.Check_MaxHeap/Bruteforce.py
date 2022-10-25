import heapq

def checkMaxHeap(lst):
    
    for pi in range(len(lst)):
        li=2*pi+1
        ri=2*pi+2
        if li<len(lst) and lst[pi]<lst[li]:
            return False
        elif ri<len(lst) and lst[pi]<lst[ri]:
            return False
        
    return True
        

# Main Code

lst=[42, 20, 18, 6 ,14 ,11, 9 ,4]
print('true') if checkMaxHeap(lst) else print('false')
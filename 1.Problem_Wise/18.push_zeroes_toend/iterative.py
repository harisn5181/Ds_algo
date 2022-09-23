#question  :move  zero to end ,but not change the position of other numbers

#using two loops

def pushZerosAtEnd(arr, n) :
    for i in range(n):
        if i !=0:
            for j in range(0,i):
                if arr[j]==0:
                    arr[i],arr[j]= arr[j],arr[i]
                    break

    print(arr)





arr=[5 ,0 ,7 ,4 ,8 ,1 ,3 ,0 ,7 ,2, 0]
#arr=[5 ,7 ,4 ,8 ,1 ,3 ,7 ,2 ,0 ,0, 0]
n=len(arr)
pushZerosAtEnd(arr,n)

"""
Dry run

arr=[5 ,0 ,7 ,4 ,8 ,1 ,3 ,0 ,7 ,2, 0]
arr=[5 ,7 ,4 ,8 ,1 ,3 ,7 ,2 ,0 ,0, 0]



#using single loop




# def sortZeroesAndOne(arr, n) :
#     end=n-1
#     start=0

#     while (start<end):
#       if arr[start] < arr[end]:
        
#         arr[start],arr[end]=arr[end],arr[start]
#         start=start+1
#         end=end-1

        
#       elif arr[start]> arr[end]:
            
#                 start=start+1
        
#       elif arr[start] == arr[end]:
#         start=start+1

#     print(arr)  


# arr=[5 ,0 ,7 ,4 ,8 ,1 ,3 ,0 ,7 ,2, 0]

# n=len(arr)
# sortZeroesAndOne(arr,n)



"""

#using single scan
"""
from sys import stdin

def pushZerosAtEnd(arr, n) :
    #Your code goes here
    count = 0 # Count of non-zero elements
     
    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:
             
            # here count is incremented
            arr[count] = arr[i]
            count+=1
     
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1
"""
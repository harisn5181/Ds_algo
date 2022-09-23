#Iterative Approach


def longest_increasing_sequence(arr,n):
    max_count=-1
    for i in range(n):
        prev=0
        count=0
        j=i+1
        while j< n :

            if arr[j]>=arr[i] and arr[j]>= prev:
                count=count+1
                prev=arr[j]
            j=j+1
        if count!=0:
            if count > max_count:
                max_count=count



    return max_count+1


arr=[6 ,3, 1, 2, 7, 0, 9]
n=len(arr)
print(longest_increasing_sequence(arr,n))
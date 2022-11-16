




def sum_array(arr,k):
    for i in range (len(arr)):
        for j in  range (i+1,len(arr)):
            if arr[i]+arr[j] == k:
                print(arr[i],arr[j])





arr=[5, 12 ,3 ,17, 1, 18 ,15 ,3, 17 ]
sum_array(arr,6)
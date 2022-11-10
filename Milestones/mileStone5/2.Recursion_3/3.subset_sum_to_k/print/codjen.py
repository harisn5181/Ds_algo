def printSubsets(arr,k,output=[]):

    if len(arr)==0:
        if k==0:
            print(*output)
            return
        else:
            return
    
    printSubsets(arr[1:],k-arr[0],output+[arr[0]])
    printSubsets(arr[1:],k,output)
    

arr=[5 ,3, 1, 4]
k=6
printSubsets(arr,k)



def printSubsets_helper(arr,output):
    if len(arr)==0:
        print(*output)
        return
    printSubsets_helper(arr[1:],output)
    # output.append(arr[0])
    printSubsets_helper(arr[1:],output+[arr[0]])
    # output.pop()
    
def printSubsets(arr):
    printSubsets_helper(arr,[])


arr=[10,20,30]
printSubsets(arr)
    
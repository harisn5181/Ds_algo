def lis(arr, n,  i=0):
    if i == n:
        return (0, 0)

    excluding_res = lis(arr, n, i+1)[1]
    
    max_lis = 0
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            
              
            new_lis =   lis(arr, n, j)[0]
            
            if new_lis > max_lis:
                max_lis = new_lis
            
    including_res = 1 + max_lis
    
    return (including_res, max(including_res, excluding_res))



arr = [6, 3, 1, 2, 7, 0, 9]

n = len(arr)

print(lis(arr, n)[1])
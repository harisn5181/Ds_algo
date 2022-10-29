def lis(arr, n, dp, i=0):
    if i == n:
        return (0, 0)
    
    if dp[i+1] is None:
        dp[i+1] = lis(arr, n, dp, i+1)[1]
        
    excluding_res = dp[i+1]
    
    max_lis = 0
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            if dp[j] is None:
                dp[j] = lis(arr, n, dp, j)[0]
            new_lis = dp[j]
            
            if new_lis > max_lis:
                max_lis = new_lis
            
    including_res = 1 + max_lis
    
    return (including_res, max(including_res, excluding_res))



arr = [0,5,2,3,4,]
n = len(arr)
dp = [None for _ in range(n+1)]
dp[1]=lis(arr, n, dp)[1]
print(dp[1])
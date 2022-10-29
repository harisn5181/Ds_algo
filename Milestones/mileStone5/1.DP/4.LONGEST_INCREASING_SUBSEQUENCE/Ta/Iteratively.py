def lisIter(arr, n):
    dp = [0 for _ in range(n+1)]
    
    dp[-1] = (0, 0)
    for i in range(n-1, -1, -1):
        excluding_res = dp[i+1][1]
        
        max_lis = 0
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                max_lis = max(max_lis, dp[j][0])
            
        including_res = 1 + max_lis
        
        dp[i] = including_res, max(including_res, excluding_res)
        
    return dp[0][1]
    
arr = [6, 3, 1, 2, 7, 0, 9]
n = len(arr)
print(lisIter(arr, n))
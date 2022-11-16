










import sys
#Bottom up approach
def mincost(cost,n,m):  
    dp=[[sys.maxsize for j in range(m+1)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i == n-1 and j==m-1:
                dp[i][j] = cost[i][j]
            else:
                ans1=dp[i+1][j] #Down
                ans2=dp[i][j+1] #right
                ans3=dp[i+1][j+1] #diagonal
                dp[i][j]=cost[i][j]+min(ans1,ans2,ans3)
    return dp[0][0]



Cost=[[1,2,3],[4,5,6],[7,8,9]]
#ans=mincost(Cost,3,3)
#print(ans)


# topp down approach


def mincostiterativetopdown(cost,n,m):
    dp=[[sys.maxsize for j in range(m+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i ==1 and j==1:
                dp[i][j]=cost[0][0]
            else:
                ans1=dp[i-1][j] #Top
                ans2=dp[i][j-1] #Left
                ans3=dp[i-1][j-1] # left diagonal
                dp[i][j]=cost[i-1][j-1]+min(ans1,ans2,ans3)
    return dp[n][m]

print(mincostiterativetopdown(Cost,3,3))

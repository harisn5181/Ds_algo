









import sys
def mincost(cost,i,j,n,m):

    if i==n-1 and j==m-1:
        return cost [i][j]

    if i >= n or j >= m:
        return sys.maxsize

    ans1=mincost(cost,i,j+1,n,m) #Right
    ans2=mincost(cost,i+1,j,n,m) #Down
    ans3=mincost(cost,i+1,j+1,n,m) #Diagonal
    
    ans=cost[i][j] + min(ans1,ans2,ans3)
    return ans


Cost=[[1,2,3],[4,5,6],[7,8,9]]
ans=mincost(Cost,0,0,3,3)
print(ans)
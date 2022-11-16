import sys





def mincost(cost,i,j,n,m,dp):
    if i==n-1 and j==m-1:
        return cost [i][j]

    if i >= n or j >= m:
        return sys.maxsize

    if dp[i][j+1] ==sys.maxsize:

        ans1=mincost(cost,i,j+1,n,m,dp)
        dp[i][j + 1]=ans1
    else:
        ans1=dp[i][j+1]

    if dp[i+1][j] == sys.maxsize:
        ans2=mincost(cost,i+1,j,n,m,dp)
        dp[i + 1][j]=ans2
    else:
        ans2=dp[i+1][j]

    if dp[i+1][j+1 ] == sys.maxsize:

         ans3=mincost(cost,i+1,j+1,n,m,dp)
         dp[i + 1][j + 1]=ans3
    else:
        ans3=dp[i+1][j+1]

    ans=cost[i][j] + min(ans1,ans2,ans3)
    return ans



n=3
m=3
dp=[[sys.maxsize for j in range(m+1)] for i in range(n+1)]

Cost=[[1,2,3],[4,5,6],[7,8,9]]
ans=mincost(Cost,0,0,3,3,dp)
print(ans)


#
#
#

#correct answer
#
# import sys
#
#
# def minCost(cost, i, j, n, m, dp):
#     # Special Case
#     if i == n - 1 and j == m - 1:
#         return cost[i][j]
#     # Base case
#     if i >= n or j >= m:
#         retu
#         rn sys.maxsize
#
#     if dp[i][j + 1] == sys.maxsize:
#         ans1 = minCost(cost, i, j + 1, n, m, dp)
#         dp[i][j + 1] = ans1
#     else:
#         ans1 = dp[i][j + 1]
#
#     if dp[i + 1][j] == sys.maxsize:
#         ans2 = minCost(cost, i + 1, j, n, m, dp)
#     else:
#         ans2 = dp[i + 1][j]
#
#     if dp[i + 1][j + 1] == sys.maxsize:
#         ans3 = minCost(cost, i + 1, j + 1, n, m, dp)
#     else:
#         ans3 = dp[i + 1][j + 1]
#     ans = cost[i][j] + min(ans1, ans2, ans3)
#
#     return ans
#
#
# cost = [[1, 5, 11], [8, 13, 12], [2, 3, 7], [15, 16, 18]]
# n = 4
# m = 3
# dp = [[sys.maxsize for j in range(m + 1)] for i in range(n + 1)]
# ans = minCost(cost, 0, 0, 4, 3, dp)
# print(ans)
#









# #####
# import sys
#
#
# def minCost(cost, i, j, n, m, dp):
#     # Special Case
#     if i == n - 1 and j == m - 1:
#         return cost[i][j]
#     # Base case
#     if i >= n or j >= m:
#         return sys.maxsize
#
#     if dp[i][j + 1] == sys.maxsize:
#         ans1 = minCost(cost, i, j + 1, n, m, dp)
#         dp[i][j + 1] = ans1
#     else:
#         ans1 = dp[i][j + 1]
#
#     if dp[i + 1][j] == sys.maxsize:
#         ans2 = minCost(cost, i + 1, j, n, m, dp)
#     else:
#         ans2 = dp[i + 1][j]
#
#     if dp[i + 1][j + 1] == sys.maxsize:
#         ans3 = minCost(cost, i + 1, j + 1, n, m, dp)
#     else:
#         ans3 = dp[i + 1][j + 1]
#     ans = cost[i][j] + min(ans1, ans2, ans3)
#
#     return ans
#
#
# cost = [[1, 5, 11], [8, 13, 12], [2, 3, 7], [15, 16, 18]]
# n = 4
# m = 3
# dp = [[sys.maxsize for j in range(m + 1)] for i in range(n + 1)]
# ans = minCost(cost, 0, 0, 4, 3, dp)
# print(ans)
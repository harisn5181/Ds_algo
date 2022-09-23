#Iterative solution for Fibnocci

def fibb1(n):
    dp =[0 for i in range (n+1)]
    dp[0] =0
    dp[1] =1
    i=2
    while (i <= n):
        dp[i]=dp[i-1] + dp [i-2]
        i=i +1
    return dp[n]

n=int(input())
ans=fibb1(n)
print(ans)

#why does iterative solution are better than recursive solution in DP

#1)Recursion have the headachhe of stack overflow
    #we cant solve fibb(n ^6)  in recursion , call avove 10 ^ 3 in python and 10 ^4 in c++ and java is not allowed
    #so in this problem we cant solvve using recustion,we must use iteration for that
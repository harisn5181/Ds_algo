import sys




def minStepsto1(n):
    
    if n==1:
        return 0
    
    ans1=sys.maxsize
    if n%3 ==0:
        ans1=minStepsto1(n//3)
    ans2=sys.maxsize
    
    if n%2 ==0:
        ans2=minStepsto1(n//2)
    ans3=minStepsto1(n-1)
    
    ans=1+min(ans1,ans2,ans3)
    return ans
    
    
n=100
ans=minStepsto1(n)
print(ans)
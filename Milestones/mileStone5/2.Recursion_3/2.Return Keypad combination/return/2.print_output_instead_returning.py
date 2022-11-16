










def fact(n,ans=1):
    if n== 1:
        print(ans)
        return
        
    ans=n*ans
    fact(n-1,ans)
    
fact(5)
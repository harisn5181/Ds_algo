#recursive approach for recusion

def fibb(n):

    if n== 0 or n ==1 :
        return n

    ans1=fibb(n-1)
    ans2=fibb(n-2)

    myans=ans1 + ans2

    return myans

n=3
ans=fibb(n)
print(ans)

#Memmorisation for fibnocci
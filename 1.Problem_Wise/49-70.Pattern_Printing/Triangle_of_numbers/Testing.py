"""
   1
  232
 34543
4567654

"""
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")


    for k in range(i,2*(i-1)+1):
        print(k,end="")
    for h in range(2*(i-1)+1,i-1,-1):
        print(h,end="")
    print()
"""
          5432*

          543*1

          54*21

          5*321

          *4321
"""
n=5
for i in range(n):
    for j in range(n,0,-1):

        if j==i+1:
            print("*",end="")
        else:
            print(j,end="")
    print()

#17-09
"""
Dry run

   *
  ***
 *****
*******

n=4
for i in range(n):
    for j in range(n-i-1):
        print(' ',end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

#Recursive


def print_star(n):
    if n==0:
        return
    print("*",end="")
    print_star(n-1)

def spaces(n):
    if n==0:
        return
    spaces(n-1)
    print(" ",end="")

def pattern(n,n_orginal):
    if n ==-1:
        return
    pattern(n-1,n_orginal)
    spaces(n_orginal-n)
    print_star(2*n+1)
    print()
pattern(3,3)










"""





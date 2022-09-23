
#Bruteforce Approach
#TC: 0 (n)   SC: 0 (1)
#
# def square_pattern(n,n_copy):
#   if n==0:
#     return
#
#   square_pattern(n-1,n_copy)
#   print( str(n_copy) * n_copy )
#
#
#
#
# #Main
# n=int(input("Enter Number"))
# n_copy=n
# square_pattern(n,n_copy)
#

"""
Dry run 
5 4
4 3
3 2 
2 1 *  *
1 0 *
"""


"""def square_pattern(n, k):
  if n == 0:
    return
  for i in range(k):
    print(k, end="")
  print()
  square_pattern(n - 1, k)


n = 4
k = n
square_pattern(n, k)"""


def square(num, i=0):
  if num == 0:
    return
  if num == i:
    return
  else:
    square(num, i + 1)
    print(str(num) * num, end="")
    print()


n = int(input())
square(n)

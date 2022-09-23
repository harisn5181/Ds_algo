"""

Sample Input 1:

7

Sample Output 1:

7777777
7777777
7777777
7777777
7777777
7777777
7777777

"""
# for i in range(7):
#     for j in  range(7):
#         print(7,end="")
#     print()


#Recursion
#wrong code

def square_pattern(n):
    if n ==0:
        return
    square_pattern(n-1)

    square_pattern(n-1)
    print(7,end=" ")
square_pattern(3)

#15-09
#iterative
# for i in range(1,5):
#     for j in range(i):
#         print("1",end="")
#     print()

#recursion

# def number_pattern(n):
#     if n==0:
#         return
#     number_pattern(n-1)
#     print(str(1)* n)
#
# number_pattern(4)

#Testing

#Number_pattern

"""

1234
123
12
1
"""



# for i in range(4): # 0 1 2 3
#     for j in range(4-i): # 4
#         print(j+1,end="")
#     print()


#Recursive
# def helper(n):
#
#
# def recursive(n):
#     if n==0:
#         return
#     recursive(n-1)
#
#
#
#
#
#
#
#
#
# recursive(4)
#


n=3
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(ord('A')+i-1), end='')
        j+=1
    i=i+1
    print()












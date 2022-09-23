
#Testing on 14-09-22






#iterate

# n=12
# sum=15
# for i in range(n+1):
#     if i % 2==0:
#
#         sum=sum+i
# print (sum)


#Recusion


# def sum_even_number(n):
#     if n==1 or n==0 :
#         return 0
#     sum= sum_even_number(n-1)
#     if n% 2==0:
#         sum=sum+n
#     return sum
#
# print(sum_even_number(15))


#recursion other approach



#
# def sum_even_number(n):
#     global sum
#
#
#     if n==0 or n ==1:
#         return
#     sum_even_number(n-1)
#     if n%2==0:
#         sum=sum+n
#
#
# sum=0
# sum_even_number(10)
# print(sum)
#

#recursion other approach




def sum_even_number(n):
    global sum


    if n==0 or n ==1:
        return


    sum_even_number(n-1)
    if n%2==0:
        sum=sum+n
    return sum



sum=0
print(sum_even_number(15))

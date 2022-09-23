#Check on 14-09-22
#Factorial = iteration

# n=5
# fact=n #5
# n=n-1 # 4
#
# for i in range(n):
#     fact= fact*n
#     n=n-1 # 3,2,1
# print(fact)

# iteraion

# n=5
# fact=1
# k=n
# for i in range(k):
#   fact=fact*n
#   n=n-1
#
# print(fact)





# 5* 4= 20   # 1*5 =5
# 20 *3=60    #5*4 =20
# 60*2=120      # 20 * 3=60
# 120*1         #60 * 2=120
                #120*1= 120



#recursion


def factorial(n):
    if n ==1:
        return 1
    return factorial(n-1)*n

print(factorial(4))
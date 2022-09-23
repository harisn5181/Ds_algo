"""#test on 15 -09
# num=25
# flag =False
# for i in range (2,num):
#     if num%i==0:
#         flag=True
#         break
#
# if flag==True:
#     print("not a prime number")
#
#


#recursive solution

def prime(n,i=2):

    if n<=2 :
        return  True if n==2 else False

    if n%i==0:
        return False


    if (i*i > n):
        return True
    return prime(n,i=i+1)

print(prime(14))


"""
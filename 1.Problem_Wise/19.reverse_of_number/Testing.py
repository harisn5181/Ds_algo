#on 15-09-22

"""
Dry run

15300
351



n=150300
reverse="0"
while (n!=0):
    remainder=n%10
    remainder_string=str(remainder)
    if remainder==0 and reverse =="0":
        pass
    else:
        if reverse=="0":

            reverse = remainder_string
        else:
            reverse =   reverse+remainder_string
    n=n//10
print(reverse)



n=3500320000 #for taking reverse of element
reverse=0

while n>0:
    remainder=n%10
    reverse=reverse*10+remainder
    n=n//10

print(reverse)


# using recursion

n=15300#for taking reverse of element
reverse=0

def reverse_function(n,reverse=0):
    if n<=0:
        return reverse

    remainder = n % 10

    reverse = reverse * 10 + remainder

    return reverse_function(n//10,reverse)

print(reverse_function(n))
"""
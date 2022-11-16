





def count_zeroes(n):
    if n ==0:
        return 0
    count=count_zeroes(n//10)
    if n%10==0:
        return count+1
    else:
        return count

print(count_zeroes(120120))

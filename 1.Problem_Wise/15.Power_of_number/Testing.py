def power_number(n,x):
    if n ==0:
        return 1
    return x*power_number(n-1,x)

print(power_number(3,4))
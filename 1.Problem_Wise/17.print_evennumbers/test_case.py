def print_even_number(n):
    if n ==1:
        return
    print_even_number(n-1)
    if n%2 ==0:
        print(n)


print_even_number(10)
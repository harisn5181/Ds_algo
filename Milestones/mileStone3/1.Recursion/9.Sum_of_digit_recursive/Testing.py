def sum_of_digit_recursive(n):
    if n==0:
        return 0
    
    return (sum_of_digit_recursive(n//10)+n%10)

print(sum_of_digit_recursive(12345))
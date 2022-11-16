## Read input as specified in the question.
## Print output as specified in the question.




def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))


# Driven code to check above
num = int(input())
result = sum_of_digit(num)
print(result)
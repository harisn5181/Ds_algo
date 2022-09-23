#Factorial Example


def fact(n, output):
    if n == 0:
        print(output)
        return

    output = output * n
    fact(n -1, output)



n=int(input())
fact(n, 1)
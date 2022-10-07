from sys import stdin
def pairSum0(arr, n):

    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    print(d)

    for i in d:
        if -i in d:
            postive_answer=d[i]
            negative_answer=d[-i]
            ans=postive_answer*negative_answer
            for j in range(ans):

              print(i,-i)

def takeInput():
    # To take fast I/O
    n = 5
    if n == 0:
        return list(), 0
    arr = [0,0,0,0,0]
    return arr, n


arr, n = takeInput()
pairSum0(arr, n)


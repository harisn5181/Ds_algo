from sys import stdin

#arr=[9, 3, 6, 2, 9]

def secondLargestElement(arr, n):
    #Your code goes here
    l=-2147483648
    s=-2147483648
    for i in range(n):
        if arr[i]>l and arr[i]!=l:
            s=l # 13
            l=arr[i] #20
        elif (arr[i]>s and arr[i]!= l):
        	s = arr[i] #15
    return s

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1


#this code just find the pair sum or not ,not performing  count

"""from sys import stdin

def pairSum(arr, n, num) :
	#Your code goes here
    arr.sort()
    s=0
    f=n-1
    count=0
    while(s<f):
        if (arr[s]+arr[f]> num):
            f=f-1
        elif (arr[s]+arr[f] < num):
            s=s+1
        elif(arr[s]+arr[f]== num ) :
            count=count+1
            s=s+1
            f=f-1
            
    return count




























#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1"""




#by using set method

# i need to improve this approach




def pairSum(arr, n, num) :
	#Your code goes here
    if n<2:
        return
    found=set()
    output=set()
    count=0
    
    for i in arr:
        k=num-i
        if k not in found:
            found.add(i)
            
        else:
            count=count+1
    return count        

print(pairSum([3, 3, 3 ,3 ,3],5,6))




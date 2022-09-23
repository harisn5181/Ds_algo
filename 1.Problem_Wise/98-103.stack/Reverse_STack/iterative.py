from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)




def reverseStack(inputStack, extraStack) :

    if(len(inputStack)==1 or len(inputStack)==0):
        return

    while(len(inputStack)!=1):
        extraStack.append(inputStack.pop())

    temp=inputStack.pop()

    while(len(extraStack)!=0):
        inputStack.append(extraStack.pop())
    reverseStack(inputStack, extraStack)
    inputStack.append(temp)


'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
from sys import stdin
import queue


def reverseKElements(inputQueue, k):
    # Your code goes here
    c = 0
    s = []
    while (c < k):
        s.append(inputQueue.get())
        c += 1
    while (len(s) != 0):
        inputQueue.put(s.pop())
    c = 0
    s = inputQueue.qsize() - k
    while (c < s):
        ele = inputQueue.get()
        inputQueue.put(ele)
        c += 1

    return inputQueue


'''-------------- Utility Functions --------------'''


# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0


# Takes a list as a stack and returns the element at the top
def top(stack):
    # assuming the stack is never empty
    return stack[len(stack) - 1]


def takeInput():

    k = 3

    qu = queue.Queue()
    values = [1,2,3,4,5]

    for i in range(5):
        qu.put(values[i])

    return k, qu


# main
k, qu = takeInput()
c = 1
s = qu.qsize()
qu = reverseKElements(qu, k)

while not qu.empty():
    print(qu.get(), end=" ")
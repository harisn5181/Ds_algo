from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


def reverseQueue(inputQueue):
    if inputQueue.qsize() <= 1:
        return

    front = inputQueue.get()

    reverseQueue(inputQueue);

    inputQueue.put(front)


'''-------------- Utility Functions --------------'''


def takeInput():
    n = 5

    qu = queue.Queue()
    values = [1,2,3,4,5]

    for i in range(n):
        qu.put(values[i])

    return qu




qu = takeInput()
reverseQueue(qu)

while not qu.empty():
    print(qu.get(), end=" ")


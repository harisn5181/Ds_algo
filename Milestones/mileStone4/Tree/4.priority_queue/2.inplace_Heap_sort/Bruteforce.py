def heapify(arr, n, i): #1,0
    smallest = i  # 0 
    l = 2 * i + 1 # 1
    r = 2 * i + 2 # 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l # 1

    if r < n and arr[r] < arr[smallest]:
        smallest = r 

    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])
        heapify(arr, n, smallest) # 1

def heapSort(arr, n):
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def printArray(arr, n):
    for i in arr[::-1]:
        print(i, end=" ")
    print()

if __name__ == '__main__':

    arr = [52,4,32,2,100]
    n = len(arr)
    heapSort(arr, n)
    printArray(arr, n)
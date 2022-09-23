arr=[9, 3, 6, 2, 9]
l=-2147483648
s=-2147483648

def second_largest(arr):
    l = -2147483648
    s = -2147483648

    for i in range(len(arr)):
        if arr[i] > l and arr[i] != l:
            s = l
            l = arr[i]
        elif arr[i] > s and arr[i]!= l:
            s = arr[i]
    return s

print(second_largest(arr))


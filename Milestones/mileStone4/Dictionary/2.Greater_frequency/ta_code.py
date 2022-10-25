from sys import stdin


def maxfreq(arr):
    d = {}
    for num in arr:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    ans = arr[0]
    for num in arr:
        if d[num] > d[ans]:
            ans = num
    return ans





arr = [2 ,12, 2, 11, 12, 2 ,1 ,2 ,2 ,11, 12, 2 6 ]
print(maxfreq(arr))
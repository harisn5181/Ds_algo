def subsetSum(a):
    d = {}
    sum = 0
    maxL = -100000
    flag = False
    for i in range(len(a)):
        sum += a[i]
        if sum == 0:
            l = i + 1
            flag = True

        elif sum not in d:
            d[sum] = i
        else:
            l = i - d[sum]
            flag = True

        if flag and l > maxL:
            maxL = l
    return maxL


# Main
n = int(input())
l = list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
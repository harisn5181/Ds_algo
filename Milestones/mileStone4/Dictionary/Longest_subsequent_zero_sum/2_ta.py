







def subsetSum(a):
    d = {} #6:0 ,9:1,8:2, 10:3,
    sum = 0
    maxL = -100000
    flag = False
    for i in range(len(a)):
        sum += a[i]  #8
        if sum == 0:
            l = i + 1
            flag = True

        elif sum not in d:
            d[sum] = i
          
        else:
            l = i - d[sum] # 7-2=5
            flag = True

        if flag and l > maxL:
            maxL = l #4
    return maxL


# Main
n = 9
l = [0, 0, 0,0,0, -435 ,-5, -70, 897, 127, 23 ,284]
print(subsetSum(l))
def longest(l):
    dic = {}
    const = []
    for ele in l:
        dic[ele] = dic.get(ele, True)


    for curr in dic:
     if dic[curr] != False:
        curr1 = curr # 
        temp = [curr] #[7,]
        dic[curr] = False #3:False
        while dic.get(curr + 1, False):
            temp.append(curr + 1)
            dic[curr + 1] = False
            curr = curr + 1
        while dic.get(curr1 - 1, False):
            temp.append(curr1 - 1) # [3,2,1]
            dic[curr1 - 1] = False  #2:False
            curr1 = curr1 - 1

        lentemp = len(temp) #3
        lenconst = len(const) #0
        if lentemp > lenconst:
            const = temp #[3,2,1]
        elif lentemp == lenconst:
            min_a = min(temp)
            min_b = min(const)
            if l.index(min_a) < l.index(min_b):
                const = temp

    return const


# You have To Return the list of longestConsecutiveSubsequence



l = [3 ,7 ,2 ,1 ,9 ,8 ,41 ]
final = longest(l)
final.sort()
print(final[0], final[-1])
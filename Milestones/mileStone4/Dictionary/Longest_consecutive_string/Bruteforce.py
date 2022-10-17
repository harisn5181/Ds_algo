def longest(l):
    dic = {}
    const = []
    for ele in l:
        dic[ele] = dic.get(ele, True)

    for curr in dic:
        curr1 = curr
        temp = [curr]
        dic[curr] = False
        while dic.get(curr + 1, False):
            temp.append(curr + 1)
            dic[curr + 1] = False
            curr = curr + 1
        while dic.get(curr1 - 1, False):
            temp.append(curr1 - 1)
            dic[curr1 - 1] = False
            curr1 = curr1 - 1

        lentemp = len(temp)
        lenconst = len(const)
        if lentemp > lenconst:
            const = temp
        elif lentemp == lenconst:
            min_a = min(temp)
            min_b = min(const)
            if l.index(min_a) < l.index(min_b):
                const = temp

    return const


# You have To Return the list of longestConsecutiveSubsequence


n = int(input())
l = list(int(i) for i in input().strip().split(' '))
final = longest(l)
final.sort()
print(final[0], final[-1])
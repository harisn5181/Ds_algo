def uniqueChar(string):
    d = {}
    for i in string:
        d[i] = d.get(i, 0) + 1

    for i in d:
            print(i,end="")


# Main
s=input()
uniqueChar(s)
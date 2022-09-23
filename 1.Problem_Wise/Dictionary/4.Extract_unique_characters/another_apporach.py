
def uniqueChar(s):
    d = {}
    for x in s:
        d[x] = 1

    out = ""


    for a in d:
       out=out+a
    return out


# Main
s = input()
print(uniqueChar(s))
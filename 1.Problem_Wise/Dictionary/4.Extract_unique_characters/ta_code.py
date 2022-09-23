
def uniqueChar(s):
    d = {}
    for x in s:
        d[x] = 1

    out = ""
    print(d)

    for x in s:
        if d[x] != None:
            out += x
            d[x] = None  # as we used x we mark its value as None
    return out


# Main
s = input()
print(uniqueChar(s))
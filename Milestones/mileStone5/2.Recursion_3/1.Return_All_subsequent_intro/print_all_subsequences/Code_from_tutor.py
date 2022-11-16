




def printSubs(s,o):
    if len(s) ==0:
        print(o)
        return

    #dont include oth char
    printSubs(s[1:],o)

    # include
    newoutput=o+s[0]
    printSubs(s[1:],newoutput)

printSubs("abc","")

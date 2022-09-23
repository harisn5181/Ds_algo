def getstring(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return " "


def printkeypad(n,outputsofar):
    if n==0:
        print(outputsofar)
        return
    smallnumber=n//10
    lastdigit=n%10
    optionsforlastdigit=getstring(lastdigit)

    for c in optionsforlastdigit:
        newoutput=outputsofar+c
        printkeypad(smallnumber,newoutput)



printkeypad(35,"")
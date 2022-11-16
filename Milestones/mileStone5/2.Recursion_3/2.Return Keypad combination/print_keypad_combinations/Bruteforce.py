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
    smallnumber=n//10 # 0
    lastdigit=n%10 # 2 
    optionsforlastdigit=getstring(lastdigit) # def, abc 

    for c in optionsforlastdigit: # def ,abc 
        newoutput=c+outputsofar  #  bf 
        printkeypad(smallnumber,newoutput)



printkeypad(23,"")
"""

base case = [0]  => [""]

remainter=digit%10
small_int= digit /10
smalloutput = getcombination (smaller output )



"""
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


def keypad(n):
    if n ==0:
        output=[]
        output.append("")
        return output
    smallernumber=n//10 # 23
    lastdigit=n%10 #

    smalleroutput=keypad(smallernumber) #j, k, l,""

    optionforlastdigit=getstring(lastdigit) #def

    output=[]

    for s in  smalleroutput :
        for c in optionforlastdigit:
            option=s+c
            output.append(option) #j, k, l,
    return output
print(len(keypad(235)))

#Questioin 1: why output does not get after intilising on if condition

def subs(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output
    smalleststring=s[1:]
    smalleroutput=subs(smalleststring)

    output=[]
    for sub in smalleroutput:
        output.append(sub)
    for sub in smalleroutput:
        subs_with_zeros_character=s[0]+sub
        output.append(subs_with_zeros_character)
    return output

print(subs("abc"))
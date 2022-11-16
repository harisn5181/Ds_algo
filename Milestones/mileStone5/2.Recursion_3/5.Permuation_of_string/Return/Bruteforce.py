















def permutationString(s):
    if len(s)==0:
        return [""]
    

    smallOutput=permutationString(s[1:])
    
    output=[]
    
    for i in range(len(s)):
        for string in smallOutput:
            if i==0:
                output.append(s[0]+string)
            else:
                output.append(string[:i]+s[0]+string[i:])
    return output
s="abc"
permutation=permutationString(s)
for i in permutation:
    print(i)
from sys import stdin

def countBracketReversals(inputString) :
    # Your code goes here
    s=[]
    if len(inputString)%2!=0:
        return -1
    for x in inputString:
        if x is '{':
            s.append(x)
        elif x is '}':
            if len(s)==0:
                s.append(x)
            elif len(s)!=0 and s[-1]!='{':
                s.append(x)
            elif len(s)!=0 and s[-1]=='{':
                s.pop()
    count=0
    while len(s)>=2:
        c1=s.pop()
        c2=s.pop()
        if c1==c2:
            count+=1
        elif c1!=c2:
            count+=2
    return count

#main
print(countBracketReversals(stdin.readline().strip()))
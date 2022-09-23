# Problem: Remove x from string
def removeX(s,a):
  
    if len(s) ==0:
        return s
    smalloutput=removeX(s[1:],a)
    if s[0] == a:
        return smalloutput
    else:
        return s[0]+smalloutput
# Main
string = input()
print(removeX(string,"x"))
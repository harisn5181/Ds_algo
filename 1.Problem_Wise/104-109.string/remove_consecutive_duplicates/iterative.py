
from sys import stdin

def removeConsecutiveDuplicates(string) :
    
    answerStr = string[0]
    
    for i in range(1,len(string)):
        if(string[i]!=answerStr[-1]):
            answerStr += string[i]
            
    return answerStr


#main
string = "aabbccd"

ans = removeConsecutiveDuplicates(string)

print(ans)
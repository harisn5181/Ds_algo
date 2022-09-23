from sys import stdin
def isPermutation(string1, string2) :
    if len(string1) != len(string2) :
        return False
    frquency = [0] * 256

    for i in range(len(string1)) :
        ch = ord(string1[i])
        frquency[ch] += 1
    for i in range(len(string2)) :
        ch = ord(string2[i])
        frquency[ch] -= 1
    for i in range(256) :
        if frquency[i] != 0 :
            return False
    return True
  
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();
ans = isPermutation(string1, string2)
if ans :
    print('true')
else :
    print('false')

""""""
#second Approach but can only use if there is no duplicate elements in first string
"""from sys import stdin


def isPermutation(string1, string2) :


    for i in string1:
        find =False
        for j in string2:
            if i==j:
                
              find=True
              break
        if find ==True:
            pass    
        else :
            return False    
    return True    

string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')
"""
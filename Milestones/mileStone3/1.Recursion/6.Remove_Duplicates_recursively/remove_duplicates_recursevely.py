# Problem ID 91, removeConsecutiveDuplicates





"""def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0:
        return string
    if string[0] == string[1]:
        smalloutput=removeConsecutiveDuplicates(string[2:])
        return smalloutput
    else:
        smalloutput=removeConsecutiveDuplicates(string[1:])
        return smalloutput"""
    

# Main
#print(removeConsecutiveDuplicates(string))



#modified correct code from ta


def removeConsecutiveDuplicates(string):

    if len(string)==0 or len(string)==1:
        return string
    
    if string[0]==string[1]:
        smallOutput=removeConsecutiveDuplicates(string[1:])
        return smallOutput
    else:
        smallOutput=removeConsecutiveDuplicates(string[1:])
        return string[0]+smallOutput

# Main
string="aaabb"
print(removeConsecutiveDuplicates(string))

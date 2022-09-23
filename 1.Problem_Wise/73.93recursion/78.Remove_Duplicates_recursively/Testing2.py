def remove_duplicates(string):
    if len(string)==0 or string ==1:
        return string

    if string[0]==string[1]:
        smalloutput=remove_duplicates(string[1:])
        return smalloutput
    else:
        smalloutput=remove_duplicates(string[1:])
        return string[0]+smalloutput


string="aazc"

print(remove_duplicates(string))

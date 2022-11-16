string="aaabbbczcba"






def remov_duplicates(string):
    if len(string) ==1:
        new_string=""
        new_string=string[0]
        return new_string
    new_string=remov_duplicates(string[1:])
    if string[0] == new_string[0] :
        return new_string
    return string[0]+new_string



print(remov_duplicates(string))



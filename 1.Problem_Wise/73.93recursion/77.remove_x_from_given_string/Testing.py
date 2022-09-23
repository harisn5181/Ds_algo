string="axbxc"


def remove_x(string):
    if len(string) ==0:
        new_string=""
        return new_string

    ans=remove_x(string[1:])
    if string[0]=="x":
        return ans
    return string[0]+ans



print(remove_x(string))



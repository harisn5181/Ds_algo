def pair_star(str):
    if len(str)==1:
        new_string=str[0]
        return new_string
    new_string=pair_star(str[1:])

    if new_string[0]==str[0]:
        return str[0]+"*"+new_string
    return str[0]+new_string



str="hello"
print(pair_star(str))
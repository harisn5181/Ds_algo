def rasi(string,string2,string3):

    if len(string) == 0:
        string3.append("")
        return
    rasi(string[1:],string2,string3)
    for i in string3:
        temp=string[0]+i
        string2.append(temp)
    for i in string2:
         string3.append(i)
    string2.clear()
    return string3

string="abc"
string2=[]
string3=[]
print(rasi(string,string2,string3))






# string2=['c',"","bc","b"]
# string="abc"
# string3=[]
# for i in string2:
#     string3.append(i)
# for i in string2:
#          temp=string[0]+i
#          #print(temp)
#          string3.append(temp)
# print(string3)
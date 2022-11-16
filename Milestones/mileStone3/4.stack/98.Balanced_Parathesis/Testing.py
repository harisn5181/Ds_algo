stack=[]
string="(()))"
for i in string:
    if i=="(":
        stack.append(i)
    elif i==")" and len(stack)!=0:
        stack.pop()

if len(stack)==0:
    print("True")
else:
    print("False")
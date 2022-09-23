#After recursion
def check_if_number_exist(arr,x):

    if len(arr) ==0:
        return False
    Found=check_if_number_exist(arr[1:],x)

    if Found==True:
        return True
    if arr[0]==x:
        return True
    else:
        return False

arr=[1,2,3,4]
#print(check_if_number_exist(arr,5))

#Before recursion




def check_element(arr,x):
    if len(arr)==0:
        return False
    if arr[0] ==x:
        return True
    return check_element(arr[1:],x)




arr=[1,2,3,4,6]
print(check_element(arr,5))
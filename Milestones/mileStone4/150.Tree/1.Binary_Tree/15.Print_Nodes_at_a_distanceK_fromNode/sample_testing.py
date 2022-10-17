
def student(amount,RegularOrNot):
    discountedPrice=amount-(amount*0.10)
    if RegularOrNot==1:
        regular(discountedPrice,discountedPrice*0.05)
        return
    print(discountedPrice)

def regular(discountedPrice,discountFive):
    print(discountedPrice-discountFive)

amount=int(input("Enter the Fees for student:"))
if amount >=0:
    RegularOrNot=int(input("Is studnet Regualar: \n Enter 1 for yes \n Enter 2 for no \n:"))
    student(amount,RegularOrNot)
else:
    print("Data is invalid")
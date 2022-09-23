
# from sys import stdin


# def removeAllOccurrencesOfChar(string, ch) :
# 	sting_list=list(string)
#   for i in sting_list:
        
#         if i==ch:
            
#             sting_list.remove(i)
#     string = ''.join(sting_list)        
#     return string 



























	

# #main
# string = stdin.readline().strip()
# ch = stdin.readline().strip()[0]

# ans = removeAllOccurrencesOfChar(string, ch)

# print(ans)

# Python3 code to demonstrate working of
# Deleting all occurrences of character


# initializing string
test_str = "GeeksforGeeks"

# initializing removal character
rem_char = "e"

# printing original string
print("The original string is : " + str(test_str))

new_str = ""
# Deleting all occurrences of character
for i in test_str:
	if(i != rem_char):
		new_str += i
res = new_str
# printing result
print("The string after character deletion : " + str(res))

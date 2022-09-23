
input_list=[13, 17, 5 ,4 ,6]
length=len(input_list)
n=length





for i in range(0,n):
  Flag=False
  for j in range(i+1,n):
    if input_list[i] > input_list[j]:
      pass
    else:
      Flag=True
      break
  if Flag==False:
    print(input_list[i])

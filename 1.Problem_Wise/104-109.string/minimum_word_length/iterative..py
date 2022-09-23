str="this is i test string l"
length=len(str)
if length >=1: 
    
  st_new=str.split(' ')
  min=len  (st_new[0])

  
  for i in st_new:
    count=0
    for j in i:
      count=count+1
    if count<min:
      min=count
      word=i
  print(word)    
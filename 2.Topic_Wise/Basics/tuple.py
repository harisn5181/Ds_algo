tuple=()
#tuples are accesing like list by using indexes because list string and tuple follow orderd number of indexes 

#tuple and string are immutable .wecant change once created

#by using tuple we can pass many number of arguemnts to function

def sum2(a,b,*more):
  print(a)
  print(b)
  print(more)
  ans=a+b
  for i in more:
    ans=ans+i
  return ans


sum2(2,3,4,5,8,8,9)

#if we are returning more than one value,python will consider that as tuple


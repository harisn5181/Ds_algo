"""

Dry run 

arr=[4,2,1,6,18,0,1]
start=1  index
end=6    index
i=1
temp= 1 index

1 to 0 

if 4 > 2:
  arr=[2,4,1,6,18,0,1]
  i=0

i=2 

temp=2

2 to 0 
2 1 

if 4 > 1:
  arr=[2,1,4,6,18,0,1]
  


i=1

temp=1
if 2 > 1:
arr=[1,2,4,6,18,0,1]


i=3
temp=3
3 to 0
3 2 1 

if 4> 6
i=2

temp=2 
if 2> 4

i=1
temp=1

if 1> 2
i=0



i=4

temp=4

4 to 0 
4 3  2 1 

  if 6> 18


i=5

temp=5

 5 to 0 
 5 4 3 2 1 

temp=5

if 18> 0:
    arr=[1,2,4,6,0,18,1]

i=4
temp=4

if  6 > 0:
   arr=[1,2,4,0,6,18,1]

i=3
termp=3

if 4> 0:
arr=[1,2,0,4,6,18,1]


 i=2
temp=2

if 2 > 0:
arr=[1,0,2,4,6,18,1]
i=1
temp=1


if 1>0:
 arr=[0,1,1,2,4,6,18,]

  

 


arr=[3,2,8,6,18,0,1]
arr=[4,2,1,6,18,0,1]
arr=[4,2,1,6,18,0,1]

n= 7

"""




"""#no of unsorted_elements
for i in range(start,end):
	#nows of sorted items
	temp=i
	for j in range(temp,0,-1):
			if arr[i-1]> arr[i]:
        arr[i-1],arr[i]=arr[i],arr[i-1] 
			else:
				 break
              
print(arr)			

"""
n= 4
start =1
end=n
arr=[2,3,4,1]

for i in range(start,end):
  temp=i
  for j in range(temp,0,-1):
    if arr[i-1]> arr[i]:
      arr[i-1],arr[i] =arr[i],arr[i-1]
      i=i-1
    else:
      break 
print(arr)
# 123 4
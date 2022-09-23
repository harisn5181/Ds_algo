#square root of element 
li=[1,2,3,4]
li_new=[ele**2 for ele in li ]


#for even square
li_new=[ele**2 for ele in li if ele%2==0  if ele%3==0  ]

#multiple loops 
li_1=[1,2,3,4]
li_2=[3,4,5,8]

li_common=[ele for ele in li_1 for ele2 in li_2 if ele==ele2]

#if else condition

li_if_else=[ele**2 if ele%2 ==0 else ele for ele in li ]


#2d list
lii=["paris","parirs","paris"]
li_2d=[ [ s for  s in ele]for ele in lii]



#taking input of 2d list using list comprehension

# str=input.split()
# n,m=int(str([0]),int(str[1])
        
# li= [[int(j) for j in input().split()] for i in range(n)]

# str=input().split()
# n,m=int(str[0]),int(str[1])
# li=[[int (j) for j in input().split()]for i in range(n)]


#printing 2d list


#join operation


a= 'ab'.join('abcd')



b='ab'.join(['1','2'])



li=[[1,2,3,4],[5,7],[9,10,11]]

for row in li:
  output=' '.join([str (ele) for ele in row ] )
  print(output)
def isBalanced(string):
  s=[]
  for chr in string:
    if chr in '({[':
      s.append(chr)
    elif chr is ')':
      if (not s or s [-1] != '('):
        return False
      s.pop()
      

    elif chr is '}':
       if (not s or s [-1] != '{'):
        return False
       s.pop()

    elif chr is ']':
       if (not s or s [-1] != '['):
        return False
       s.pop()

  if (not s ) :
    return True
  return False  
    
      
  

string="(a+b"

ans=isBalanced(string)

print(ans)
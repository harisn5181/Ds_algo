while True:
    terms = int(input())
   
    if terms == 1:
        c = int(input()) + int(input())
        print(c)    
    if terms == 2:
            c = int(input()) - int(input())
            print(c)
    elif terms == 3:
            c = int(input()) * int(input())
            print(c)
    elif terms == 4:
            c = int(input()) // int(input())
            print(c)
    elif terms == 5:
            c = int(input()) % int(input())
            print(c)
    elif terms == 6:
            break
    elif terms > 6:
            c ="Invalid Operation" 
            print(c)
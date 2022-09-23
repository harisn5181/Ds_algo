#take matrix input
n=int(input())
maze=[]
for i in range(n):
    row=[int (ele) for ele in input().split()]
    maze.append(row)


def printpathhelper(x,y,maze,n,solution):
    if x==n-1 and y ==n-1:
        solution[x][y]=1
        print(solution)
        return
    if x<0 or y<0 or x>=n or y>=n or maze[x][y]==0 or solution [x][y]==1:
        return

    solution [x][y]=1
    printpathhelper(x+1,y,maze,n,solution) #Downward Direction
    printpathhelper(x, y + 1, maze, n, solution)  # right direction
    printpathhelper(x - 1, y, maze, n, solution) #upward direction

    printpathhelper(x , y-1, maze, n, solution)#left direction
    solution[x][y]=0
    return




def printpath(maze):
    n=len(maze)
    print(n)
    solution=[[0 for j in range(n)] for i in range(n)]
    printpathhelper(0,0,maze,n,solution)



printpath(maze)
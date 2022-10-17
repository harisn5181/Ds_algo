def printpathhelper(x,y,maze,n,solution):
    if x== n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return

    if x<0 or y<0 or x>=n or y>=n or maze[x][y] == 0  or solution [x][y] == 1:
        return

    solution [x][y]=1
    printpathhelper(x+1,y,maze,n,solution)
    printpathhelper(x , y+1, maze, n, solution)
    printpathhelper(x-1, y, maze, n, solution)
    printpathhelper(x, y-1, maze, n, solution)
    solution[x][y]= 0
    return


def printpath(maze):
    n=len(maze)
    solution=[[0 for j in range(n)] for i in range(n)]
    printpathhelper(0,0,maze,n,solution)


maze=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]]

printpath(maze)
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):

    # init f array

    n = len(grid)
    f = []

    def isBlock(x, y, n, grid):
        if x == -1 or y == n or x == n or y == -1:
            return True
        return grid[x][y] == 'X'

    for i in range(n):
        f.append([])
        for j in range(n):
            f[i].append([])
            for k in range(4):
                f[i][j].append(0)

    for i in range(n):
        for j in range(n):
            if not isBlock(i, j, n, grid):
                if isBlock(i-1,j, n, grid):
                    f[i][j][0] = (i, j)
                else:
                    f[i][j][0] = f[i-1][j][0]
                if isBlock(i,j-1,n,grid):
                    f[i][j][1] = (i, j)
                else:
                    f[i][j][1] = f[i][j-1][1]
    
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if not isBlock(i,j,n,grid):
                if isBlock(i+1,j,n,grid):
                    f[i][j][2] = (i, j)
                else:
                    f[i][j][2] = f[i+1][j][2]
                if isBlock(i, j+1,n,grid):
                    f[i][j][3] = (i,j)
                else:
                    f[i][j][3] = f[i][j+1][3]
    #print(f)
    mark = [[-1] * n for i in range(n)]
    mark[startX][startY] = 0
    q = deque()
    q.append((startX, startY))
    while len(q) > 0:
        t = q.pop()
        x = t[0]; y=t[1]
        for i in range(4):
            #print('{} {}'.format(x, y))
            #print(f[x][y][i])
            u = f[x][y][i][0]; v = f[x][y][i][1]
            if mark[u][v] < 0:
                mark[u][v] = mark[x][y] + 1
                q.append((u,v))
                if u == goalX and v == goalY:
                    return mark[u][v]

    print(mark)


if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)
 #   fptr.write(str(result) + '\n')

#    fptr.close()

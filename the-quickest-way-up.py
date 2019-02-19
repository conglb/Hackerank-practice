#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    a = []
    for i in range(102):
        a.append([])
    for i in range(1,101):
        a[i].append(0)
        for j in range(1,101):
            if abs(i-j) <= 6:
                a[i].append(1)
            else:
                a[i].append(123456789)
    for i in range(1,101):
        a[i][i] = 0
    for ladder in ladders:
        a[ladder[0]][ladder[1]] = 0
    for snake in snakes:
        for j in range(1,101):
            a[snake[0]][j] = 123456789
        a[snake[0]][snake[1]] = 0

    d = []
    for i in range(102):
        d.append([])
        for j in range(102):
            d[i].append(123456789)
    for i in range(1,101):
        for j in range(1,101):
            d[i][j] = a[i][j]
    for i in range(1,101):
        for j in range(1,101):
            for k in range(1,101):
                if d[j][i] + d[i][k] < d[j][k]:
                    d[j][k] = d[j][i] + d[i][k]

    if d[1][100] != 123456789:
        return d[1][100]
    else:
        return -1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()

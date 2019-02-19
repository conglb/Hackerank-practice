#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

def getBit(state, i):
    return (state >> (i-1)) & 1

def shop(n, k, centers, roads):
    # Write your code here
    centers = [list(map(int, centers[i].split(' '))) for i in range(n)]

    MAX_STATE = pow(2, k)

    """
    a = []
    for i in range(n+1):
        a.append([])
        for j in range(n+1):
            a[i].append(123456789)
    for road in roads:
        u = road[0]
        v = road[1]
        c = road[2]
        a[u][v] = c
        a[v][u] = c
    """

    adj = []
    for i in range(n+1):
        adj.append([])
    for road in roads:
        u = road[0]
        v = road[1]
        c = road[2]
        adj[u].append((v, c))
        adj[v].append((u, c))

    f = []
    for state in range(MAX_STATE):
        f.append([])
        for u in range(n+1):
            f[state].append(1234567890)

    f[0][1] = 0
    state = 0
    for i in range(centers[0][0]):
        item_id = centers[0][i+1]
        state += pow(2, item_id - 1)
        f[state][1] = 0

    print(adj)
    for state in range(MAX_STATE):
        for u in range(1,n+1):
            for t in adj[u]:
                v = t[0]
                c = t[1]
                state2 = state
                f[state2][v] = min(f[state2][v], f[state][u] + c)
                for i in range(centers[v-1][0]):
                    item_id = centers[v-1][i+1]
                    if getBit(state2, item_id) == 0:
                        state2 += pow(2,item_id-1)
                    f[state2][v] = min(f[state2][v], f[state][u] + c)

    ans = 1234567899
    for state in range(MAX_STATE):
        for state2 in range(MAX_STATE):
            if state | state2 == MAX_STATE-1:
                print(f[state][n])
                ans = min(ans, max(f[state][n], f[state2][n]))

    return ans


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)
    print(res)

    #fptr.write(str(res) + '\n')

    #fptr.close()

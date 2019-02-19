#!/bin/python3

import math
import os
import random
import re
import sys

def DFS(u):
    global res
    global visited
    global adj
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            DFS(v)
            res += c_road

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road > c_lib:
        return c_lib * n

    global res
    res = 0

    global adj
    adj = []
    for i in range(n+1):
        adj.append([])
    for edge in cities:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    global visited
    visited = [False] * (n+1)
    for i in range(1,n+1):
        if not visited[i]:
            DFS(i)
            res += c_lib

    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + '\n')
        #fptr.write(str(result) + '\n')

    #fptr.close()

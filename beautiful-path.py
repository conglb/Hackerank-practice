#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the beautifulPath function below.
def beautifulPath(edges, A, B):
    adj = [[] for i in range(n+1)]
    for edge in edges:
        u = edge[0]
        v = edge[1]
        c = edge[2]
        adj[u].append((v,c))
        adj[v].append((u,c))
    q = Queue()
    q.put((A,0))
    while q.empty() == False:
        first = q.get()
        print(q.empty())
        print(first)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    AB = input().split()

    A = int(AB[0])

    B = int(AB[1])

    result = beautifulPath(edges, A, B)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')

    #fptr.close()

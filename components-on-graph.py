#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
#
def componentsInGraph(gb):
    #
    # Write your code here.
    #
    result = [123456789, -123456789]
    p = [-1] * (2 * n + 1)
    f = [1] * (2 * n + 1)

    def union(u, v, p, f):

        def find(x, p):
            while p[x] != -1: x = p[x]
            return x
            
        x = find(u, p)
        y = find(v, p)
        if x < y:
            p[x] = y
            f[x] += f[y]
        elif x > y:
            p[y] = x
            f[y] += f[x]

    for edge in gb:
        u = edge[0]
        v = edge[1]
        union(u, v, p, f)
    for i in range(2*n + 1):
        if p[i] == -1:
            result[0] = min(result[0], f[i])
            result[1] = max(result[1], f[i])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

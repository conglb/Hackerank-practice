#!/bin/python3

import os
import sys

#
# Complete the jennysSubtrees function below.
#
def jennysSubtrees(n, r, edges):
    #
    # Write your code here.
    #
    # init adj array
    adj = []
    for i in range(n):
        adj.append([])
    for edge in edges:
        u = edge[0] - 1
        v  = edge[1] - 1
        adj[u].append(v)
        adj[v].append(u)

    # module base
    base = 10**9 + 7

    '''
    @:return hash of tree 
    '''
    def hash_tree(u, r):
        mark[u] = True
        res = 17
        for v in adj[u]:
            if mark[v] == False and v in s:
                res = (res + hash_tree(v, r-1)) % base

        mark[u] = False
        return (res * 13) % base


    def find_vert(u, r):
        if r == -1:
            return
        mark[u] = True
        deg = 0
        if r != 0:
            for v in adj[u]:
                deg += 1
                if mark[v] == False:
                    find_vert(v, r-1)
        ver.append((u, deg))
        mark[u] = False

    h = []
    for i in range(n):
        mark = [False] * n
        ver = []
        find_vert(i, r)
        ver.sort()
        id = 0
        for i in range(len(ver)):
            if ver[i][1] > ver[id][1]:
                id = i
        s = []
        for tuple in ver:
            s.append(tuple[0])
        h.append(hash_tree(ver[id][0], r))
    from collections import Counter
    return len(Counter(h))

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().split()

    n = int(nr[0])

    r = int(nr[1])

    edges = []

    for _ in range(n-1):
        edges.append(list(map(int, input().rstrip().split())))

    result = jennysSubtrees(n, r, edges)
    print(result)
#    fptr.write(str(result) + '\n')

#    fptr.close()

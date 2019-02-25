#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#

def dfs(u):
    global result
    global indexes
    global depth
    depth += 1
    if depth % query == 0:
        tg = indexes[u-1][0]
        indexes[u-1][0] = indexes[u-1][1]
        indexes[u-1][1] = tg
    if indexes[u-1][0] != -1:
        dfs(indexes[u-1][0])
    result[len(result)-1].append(u)
    if indexes[u-1][1] != -1:
        dfs(indexes[u-1][1])
    depth -= 1

def swapNodes(indexess, queriess):
    #
    # Write your code here.
    #
    global indexes
    global query
    global result
    indexes = indexess
    for query in queries:
        result.append([])
        global depth
        depth = 0
        dfs(1)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sys.setrecursionlimit(1500)

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    global result
    result = []
    swapNodes(indexes, queries)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

def second_cut(u):
    global sumTree, mark2, cutId, sumCut, res, adj
    mark2[u] = True
    sum = c[u]
    for v in adj[u]:
        if v != cutId and mark2[v] == False:
            sum += second_cut(v)


    if sum  == sumCut:
        res = min(res, sum - (sumTree - 2 * sumCut))
    if sumTree - sumCut - sum == sumCut:
        res = min(res, sumCut - sum)
        
    return sum


# Return sum of subtree
def first_cut(u):
    global sumTree, upper_bound, lower_bound, mark1, mark2, cutId, sumCut, adj, res
    mark1[u] = True
    sum = c[u]
    for v in adj[u]:
        if mark1[v] == False:
            sum += first_cut(v)

    if sum <= upper_bound and sum >= lower_bound:
        mark2 = [False for i in range(n)]
        if sum < sumTree - sum:
            cutId = u
            sumCut = sum
            second_cut(0)
        elif sum > sumTree - sum:
            cutId = 0
            sumCut = sumTree - sum
            second_cut(u)
        else:
            res = min(res, sum)
    return sum

# Complete the balancedForest function below.
def balancedForest(c, edges):
    n = len(c)

    global adj
    adj = []
    # neighbor list
    for i in range(n):
        adj.append([])
    for edge in edges:
        adj[edge[0]-1].append(edge[1] - 1)
        adj[edge[1]-1].append(edge[0] - 1)

    # caclute bound
    global sumTree
    sumTree = 0
    for i in range(n):
        sumTree += c[i]
    global upper_bound, lower_bound, result
    upper_bound = 2 * sumTree / 3
    lower_bound = sumTree / 3

    # travel
    global mark1, mark2, cutId, res
    mark1 = [False for i in range(n)]
    mark2 = [False for i in range(n)]
    res = 12345678999999999
    first_cut(0)

    if res == 12345678999999999:
        return -1
    else:
        return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n = len(c)

    s = 0
    for i in range(n): s+= c[i]
    if k >= n: return s

    c = list(reversed(sorted(c)))

    turn = 0
    ans = 0

    for i in range(n):
        if i % k == 0:
            turn += 1
        ans += turn * c[i]

    return  ans
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
    #fptr.write(str(minimumCost) + '\n')

    #fptr.close()

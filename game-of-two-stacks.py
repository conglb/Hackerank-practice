#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#

def binarySearch(a, left, right, x):
    l = left
    r = right
    res = -1;
    while l <= r:
        m = int((l + r) / 2)
        if a[m] <= x:
            l = m + 1
            res = max(res, m)
        else:
            r = m - 1
    return res

def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    c = []
    s = 0
    for num in b:
        s += num
        c.append(s)
    s = 0
    res = binarySearch(c,0, len(c)-1, x) + 1
    for i in range(len(a)):
        s += a[i]
        if (s <= x):
            j = binarySearch(c, 0, len(c)-1, x-s)
            if j != -1:
                res = max(res, i + j + 2)
            else:
                res = max(res, i + 1)
        else:
            break
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()

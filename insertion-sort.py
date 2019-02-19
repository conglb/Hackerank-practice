#!/bin/python3

import math
import os
import random
import re
import sys

def search(a, value):
    l = 0
    r = len(a)-1
    res = len(a)
    while l <= r:
        m = int((l + r) / 2)
        if a[m] > value:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res

# Complete the insertionSort function below.
def insertionSort(arr):
    n = len(arr)
    a = [(arr[i], i) for i in range(n)]
    a.sort(key= lambda a: (a[0], a[1]))

    b = []
    ans = 0
    for i in range(n):
        tmp = search(b, a[i][1])
        b.insert(tmp, a[i][1])
        pos = len(b) -1 - tmp + a[i][1]
        ans += pos - i
    return ans

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()

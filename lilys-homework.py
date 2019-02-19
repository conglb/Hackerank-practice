#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):
    n = len(arr)
    b = sorted(arr)
    b = dict((b[i], i) for i in range(n))

    mark = [False for i in range(n)]

    cycle = 0
    for i in range(n):
        if mark[i] == True:
            continue
        j = i
        while mark[j] == False:
            mark[j] = True
            j = b[arr[j]]
        cycle += 1

    mark = [False for i in range(n)]

    cycle2 = 0
    b = sorted(arr, reverse=True)
    b = dict((b[i], i) for i in range(n))

    for i in range(n):
        if mark[i] == True:
            continue
        j = i
        while mark[j] == False:
            mark[j] = True
            j = b[arr[j]]
        cycle2 += 1

    return n - max(cycle, cycle2)





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

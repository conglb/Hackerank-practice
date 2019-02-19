#!/bin/python3

import math
import os
import random
import re
import sys

"""
# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0]
    left = []
    right = []
    equal = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    return left + equal + right
"""

def quickSort(arr):
    pivot = arr[0]
    l = 0
    r = len(arr) - 1
    while True:
        while arr[l] > pivot:
            l += 1
        while arr[r] < pivot:
            r -= 1
        if l >= r:
            break
        else:
            tg = arr[l]
            arr[l] = arr[r]
            arr[r] = tg


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

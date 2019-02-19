#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    n = len(arr)

    arr.sort()

    ans = 1234567890

    for i in range(k-1,n):
        ans = min(ans, arr[i] - arr[i-k+1])
    return ans

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

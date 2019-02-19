#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    maxSubarray = -123456789
    maxSubsequence = 0
    ma = -123456789
    for num in arr:
        if num > 0:
            maxSubsequence += num
        ma = max(ma, num)

    if ma  < 0:
        maxSubsequence = ma

    mi = 0
    sum = 0
    for num in arr:
        sum += num
        maxSubarray = max(sum - mi, maxSubarray)
        mi = min(sum, mi)
    return [maxSubarray, maxSubsequence]
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        #fptr.write(' '.join(map(str, result)))
        #fptr.write('\n')
        print(' '.join(map(str, result)))


    #fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def solve(a):
    # Write your code here
    res = 0
    madelta = 0
    for i in range(len(a)):
        if i != 0:
            res += abs(a[i] - a[i-1])
        else:
            res += a[i]
        for j in range(i+1, len(a)):
            tmp = 0
            if i != 0:
                tmp += abs(a[i] - a[i-1])
            else:
                tmp += a[i]
            tmp += abs(a[i] - a[i+1])
            tmp += abs(a[j] - a[j-1])
            if j != len(a) - 1:
                tmp += abs(a[j] - a[j+1])
            a[i], a[j] = a[j], a[i]
            # calculate delta
            if i != 0:
                tmp -= abs(a[i] - a[i-1])
            else:
                tmp -= a[i]
            tmp -= abs(a[i] - a[i+1])
            tmp -= abs(a[j] - a[j-1])
            if j != len(a) - 1:
                tmp -= abs(a[j] - a[j+1])
            a[i], a[j] = a[j], a[i]
            madelta = max(madelta, tmp)
    return res - madelta

            

if __name__ == '__main__':
   #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p_count = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = solve(p)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

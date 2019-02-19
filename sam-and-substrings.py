#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    base = 1e9 + 7
    pre = 0
    cur = 0
    res = 0
    for i in range(len(n)):
        cur = pre * 10 + int(n[i]) * (i+1)
        pre = cur % base
        res = (res + pre) % base
    return int(res)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

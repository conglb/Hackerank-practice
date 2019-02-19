#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    for c in s:
        if c == '(':
            tmp1 += 1
        elif c == ')':
            tmp1 -= 1
            if tmp1 < 0: return 'NO'
        elif c == '{':
            tmp2 += 1
        elif c == '}':
            tmp2 -= 1
            if tmp2 < 0: return "NO"
        elif c == '[':
            tmp3 += 1
        elif c == ']':
            tmp3 -= 1
            if tmp3 < 0: return 'NO'
    if tmp1 == 0 and tmp2 == 0 and tmp3 == 0:
        return 'YES'
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


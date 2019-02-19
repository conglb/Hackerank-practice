#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function bRelow.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.print
    f1 = 1
    f2 = 0
    for i in range(1,n):
        tmp = f2
        if i == 1:
            if x == 1:
                f2 = 0
            else:
                f2 = 1
        else:
            f2 = f1
        if x != 1 or i != 1:
            f1 = (f1 * (k-2) + tmp * (k-1)) % (1e9+7)
        else:
            f1 = (k-1)
    return f2


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    print(str(int(answer)) + '\n')

    #fptr.close()


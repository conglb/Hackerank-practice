#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    h1 = list(reversed(h1))
    h2 = list(reversed(h2))
    h3 = list(reversed(h3))
    sum1 = 0
    for num in h1:
        sum1 += num
    sum2 = 0
    for num in h2:
        sum2 += num
    sum3 = 0
    for num in h3:
        sum3 += num
    if sum1 == sum2 == sum3:
        return sum1
    while len(h1) > 0:
        sum1 -= h1.pop()
        while sum2 > sum1 and len(h2) > 0:
            sum2 -= h2.pop()
        while sum3 > sum1 and len(h3) > 0:
            sum3 -= h3.pop()
        if sum1 == sum2 == sum3:
            return sum1
    return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

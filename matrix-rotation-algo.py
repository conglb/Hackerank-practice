#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    level = int(min(m, n) / 2)

    for l in range(level):
        for _ in range(r % ((m+n-4*l)*2 -4)):
            cur = matrix[l][l]
            # down vertical
            for mm in range(l+1, m-l):
                tg = matrix[mm][l]
                matrix[mm][l] = cur
                cur = tg

            # right horizon
            for nn in range(l+1, n-l):
                tg = matrix[m-l-1][nn]
                matrix[m-l-1][nn] = cur
                cur = tg
            # up vertical
            for mm in range(m-l-2, -1 + l, -1):
                tg = matrix[mm][n-l-1]
                matrix[mm][n-l-1] = cur
                cur = tg
            # right horizon
            for nn in range(n-l-2, -1 + l, -1):
                tg = matrix[l][nn]
                matrix[l][nn] = cur
                cur = tg

    for row in matrix:
        for _ in row:
            print(_, end=' ')
        print()


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

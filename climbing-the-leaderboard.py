#!/bin/python3

import math
import os
import random
import re
import sys

def binarySearch(left, right, value):
    l = left
    r = right
    res = right
    while (l <= r):
        m = int((l + r) / 2)
        if scores[m] > value:
            l = m + 1
        else:
            r = m - 1
            res = m
    return res

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank = [1]
    for i in range(1,len(scores)):
        if scores[i] != scores[i-1]:
            rank.append(rank[i-1] + 1)
        else:
            rank.append(rank[i-1])
    scores.append(-1234567890)
    res = []
    for score in alice:
        i = binarySearch(0, len(scores)-1, score)
        if i == 0:
            res.append(1)
        else:
            res.append(rank[i-1] + 1)
    return res


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

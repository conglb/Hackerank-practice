#!/bin/python3

import math
import os
import random
import re
import sys

base = 1e9 + 7
"""
factorial = [0 , 1]
for i in range(2,1e6+1):
    factorial.append((factorial[i-1] * i) % base)
"""
def binarySearchUpper(value, c):
    l = 0
    r = len(dict[c]) -1
    res = -1
    while l <= r :
        m = int((l + r) / 2)
        if value >= dict[c][m]:
            l = m + 1
        else:
            res = m
            r = m - 1
    return res

def binarySearchDownper(value, c):
    l = 0
    r = len(dict[c]) - 1
    res = -1
    while l <= r:
        m = int((l + r) / 2)
        if dict[c][m] < value:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res

def findOnSegment(left, right, excep):
    res = 0
    for c in dict:
        if len(dict[c]) > 1:
            l = binarySearchUpper(left, c)
            if c != excep:
                r = len(dict[c])-1 #binarySearchDownper(right, c)
            else:
                r = len(dict[c]) - 2
            if r > l and r != -1 and l != -1:
                n = r - l + 1
                res += (n * (n-1) / 2) % base
    return res

# Complete the shortPalindrome function below.
def shortPalindrome(s):
    global dict
    dict = {}
    f = {}

    res = 0


    for c in s:
        if not c in dict:
            dict[c] = []
            f[c] = []

    for i in range(len(s)):
        c = s[i]
        dict[c].append(i)
        n = len(dict[c])


        tmp = 0
        if n > 1:
            k =  n - 2
            while k >= 0:
                tmp = findOnSegment(dict[c][k], dict[c][n-1] , c)
                res += tmp
                k -= 1
    return int(res)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

#!bin/python3

import math
import os
import random
import re
import sys

hx = [1, 1, -1, -1]
hy = [-1, 1, 1, -1]

class Queue:

    inbox = []
    outbox = []
    size = 0

    def __init__(self):
        self.inbox = []
        self.outbox = []
        self.size = 0

    def push(self, x):
        self.inbox.append(x)
        self.size += 1

    def pop(self):
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())
        self.size -= 1
        return self.outbox.pop()

    def getSize(self):
        return self.size

def inBoard(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def BFS(x1, y1, x2, y2, a, b):
    q = Queue()
    q.push([x1, y1])
    d = []
    for i in range(n+2):
        d.append([])
        for j in range(n+2):
            d[i].append(-1)
    d[x1][y1] = 0
    while q.getSize() > 0:
        [x, y] = q.pop()
        if d[x2][y2] != -1:
            return d[x2][y2]
        for i in range(4):
            for j in range(4):
                u = x + hx[i] * a
                v = y + hy[j] * b
                if inBoard(u,v):
                    if d[u][v] == -1:
                        d[u][v] = d[x][y] + 1
                        q.push([u, v])
        for i in range(4):
            for j in range(4):
                u = x + hx[i] * b
                v = y + hy[j] * a
                if inBoard(u,v):
                    if d[u][v] == -1:
                        d[u][v] = d[x][y] + 1
                        q.push([u, v])
    return d[x2][y2]

def knightlOnAChessboard(n):
    res = []
    for a in range(1,n):
        res.append([])
        for b in range(1,n):
            res[a-1].append(BFS(0,0,n-1,n-1,a,b))
    return res

if __name__ == "__main__":
    n = int(input())

    result = knightlOnAChessboard(n)

    print('\n'.join(' '.join(map(str, resultt)) for resultt in result))
#!/bin/python3

def process():
    HW = input().split(' ')
    H = int(HW[0])
    W = int(HW[1])
    a = []
    for i in range(H+2):
        a.append([])
        for j in range(W+2):
            a[i].append(0)
    for i in range(1,H+1):
        tmp = input().split()
        for j in range(1,W+1):
            a[i][j] = int(tmp[j-1])
    ans = H * W * 2
    for i in range(1,H+1):
        for j in range(1,W+1):
            if (a[i][j] > a[i-1][j]): ans += a[i][j] - a[i-1][j]
            if (a[i][j] > a[i][j-1]): ans += a[i][j] - a[i][j-1]
            if (a[i][j] > a[i+1][j]): ans += a[i][j] - a[i+1][j]
            if (a[i][j] > a[i][j+1]): ans += a[i][j] - a[i][j+1]
    print(ans)
if __name__ == "__main__":
    process()
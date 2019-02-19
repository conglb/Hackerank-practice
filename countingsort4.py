import sys

a = []
for i in range(100):
    a.append([])
n = int(input())
ma = 0;
for i in range(int(n/2)):
    text = input();
    x = int(text.split()[0])
    a[x].append('-')
    ma = max(ma, x)
for i in range(int(n/2)):
    text = input();
    b = text.split()
    x = int(b[0])
    a[x].append(b[1])
    ma = max(ma, x)
for i in range(ma+1):
    for s in a[i]:
        print(s, end=' ')

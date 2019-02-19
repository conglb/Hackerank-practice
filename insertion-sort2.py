n = int(input())

a = []
a = list(map(int, input().split()));

for i in range(1,n):
    x = a[i]
    j = i
    while a[j-1] > a[i] and j >= 1:
        j -= 1
    for k in range(i-1, j-1, -1):
        a[k+1] = a[k]
    a[j] = x
    for h in range(n):
        print(a[h], end=' ')
    print()

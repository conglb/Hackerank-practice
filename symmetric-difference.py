# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
c = a.difference(b).union(b.difference(a))
res = {}
for num in c:
    res.add(num)
for num in res:
    print(num)
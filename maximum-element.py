# Enter your code here. Read input from STDIN. Print output to STDOUT

def query_1(x):
    s.append(x)
    if len(sma) > 0:
        if x >= sma[len(sma) - 1]:
            sma.append(x)
    else:
        sma.append(x)

def query_2():
    if len(s) == 0: return
    x = s.pop()
    if x == sma[len(sma)-1]:
        sma.pop()

def query_3():
    return sma[len(sma)-1]

if __name__ == '__main__':
    n = int(input())
    s = []
    sma = []
    for _ in range(n):
        query = input()
        query = query.split(' ')
        if query[0] == '1':
            query_1(int(query[1]))
        if query[0] == '2':
            query_2()
        if query[0] == '3':
            print(int(query_3()))


import string
import sys

def checkHorizontal(i, j):
    if (j == 0): return True
    if (j == 9): return False
    if (a[i][j-1][0] == '+' and a[i][j+1][0] == '-'): return True
    return False

def checkVertical(i, j):
    if (i == 0): return True
    if (i == 9): return False
    if (a[i-1][j][0] == '+' and a[i+1][j][0] == '-'): return True;
    return False

def update():
    for i in range(10):
        for j in range(10):
            if (a[i][j][0] == '-'):
                return
    for i in range(10):
         for j in range(10):
             print(a[i][j][0], end='')
         print()
    sys.exit()

def printMatrix():
    for i in range(10):
         for j in range(10):
             print(a[i][j][0], end='')
         print()

def checkHorizontalWithWord(b, w, id):
    x = b[0];
    y = b[1];
    m = b[3];
    if (len(w) != m): return False
    for j in range(y,y+m):
        if (a[x][j][0] != '-' and  w[j-y] != a[x][j][0]): return False;
    for j  in range(y,y+m):
        if (a[x][j][0] == '-'):
            a[x][j][0] = w[j-y]
            a[x][j][1] = id;
    return True

def checkVerticalWithWord(b, w, id):
    x = b[0]
    y = b[1]
    m = b[3]
    if (len(w) != m): return False
    for i in range(x,x+m):
        if (a[i][y][0] != '-' and w[i-x] != a[i][y][0]): return False;

    for i in range(x,x+m):
        if (a[i][y][0] == '-'):
            a[i][y][0] = w[i-x];
            a[i][y][1] = id
    return True

def deleteHorizontalWithWord(b, id):
    x = b[0]
    y = b[1]
    m = b[3]
    for j in range(y,y+m):
        if (a[x][j][1] == id):
            a[x][j][1] = -1
            a[x][j][0] = '-'

def deleteVerticalWithWord(b, id):
    x = b[0]
    y = b[1]
    m = b[3]
    for i in range(x,x+m):
        if (a[i][y][1] == id):
            a[i][y][1] == '-';
            a[i][y][0] = '-';

def Try(i):
    for j in range(1,-1,-1):
        if (j == 1):
            if b[i][2] == 0:
                for w in word:
                    if (not checkHorizontalWithWord(b[i], w, i)):
                        continue
                    else:
                        if (i < len(b)-1):
                            Try(i+1)
                        else:
                            update()
                        deleteHorizontalWithWord(b[i], i)
            else:
                for w in word:
                    if (not checkVerticalWithWord(b[i], w, i)):
                        continue
                    else:
                        if (i < len(b)-1):
                            Try(i+1)
                        else:
                            update()
                        deleteVerticalWithWord(b[i], i)
        else:
            if (i < len(b)-1):
                Try(i+1)
            else:
                update()

# b have i, j, direction, amount


def foo():
    print(word)
    print(a)
    print(b)

a = []
b = []
word = []

def process():
    for i in range(10):
        tmp = input()
        tmp2 = []
        for j in range(10):
            tmp2.append([tmp[j], -1])
        a.append(tmp2)
    words = input()
    global word;
    word = words.split(';');
    for i in range(10):
        for j in range(10):
            if (a[i][j][0] == '-'):
                if checkHorizontal(i,j):
                    tmp = 0
                    for k in range(j,10):
                        if (a[i][k][0] == '-'):
                            tmp += 1
                        else:
                            break
                    b.append([i,j,0,tmp])
                elif checkVertical(i,j):
                    tmp = 0
                    for k in range(i,10):
                        if (a[k][j][0] == '-'):
                            tmp += 1
                        else:
                            break
                    b.append([i,j,1,tmp])
    foo()
    Try(0)

if __name__ == "__main__":

    process()
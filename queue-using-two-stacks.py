inbox = []
outbox = []

def push(x):
    inbox.append(x)

def pop():
    first()
    outbox.pop()

def first():
    if len(outbox) == 0:
        while len(inbox) > 0:
            outbox.append(inbox.pop())
    return outbox[len(outbox)-1]

t = int(input())
for tt in range(t):
    a = input().split();
    a = list(map(int, a))
    if a[0] == 1:
        push(a[1])
    elif a[0] == 2:
        pop()
    elif a[0] == 3:
        print(first())
#!/bin/python3

import sys

def passwordCracker(passs, attempt):
    # Complete this function
    f = []
    for i in range(len(attempt)):
        f.append(-2)
        for password in passs:
            # password longer than i
            if len(password) - 1 > i:
                continue

            # parenly check
            duplication = True
            for j in range(i-len(password) + 1, i+1):
                if password[j-i+len(password)-1] != attempt[j]:
                    duplication = False

            if duplication:
                if i - len(password) == -1:
                    f[i] = -1
                else:
                    if f[i-len(password)] != -2:
                        f[i] = i - len(password)
                if f[i] != -2:
                    break
    if f[len(attempt)-1] == -2:
        return 'WRONG PASSWORD'
    else:
        res = ''
        i = len(attempt) - 1
        while i != -1:
            if i == len(attempt) - 1:
                res = attempt[f[i] + 1: i + 1]
            else:
                res = attempt[f[i]+1:i+1] + ' ' + res
            i = f[i]
        return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        passs = input().strip().split(' ')
        attempt = input().strip()
        result = passwordCracker(passs, attempt)
        print(result)


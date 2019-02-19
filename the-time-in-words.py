#!/bin/python3

a = [
                        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
                        "thirteen", "fourteen", "quater", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
                        "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
def process():
    if (m == 0):
        print(a[h] + "o' clock")
    elif (m == 1):
        print(a[m] + "minute past " + a[h])
    elif (m == 15):
        print("quarter past " + a[h])
    elif (m == 30):
        print("half past " + a[h])
    elif (m == 45):
        print("quarter to " +  a[h])
    elif (m == 59):
        print("one minute to " + a[j])
    else:
        if (m < 30):
            print(a[m] + ' minutes past ' + a[h])
        else:
            print(a[60 - m] + ' minutes to ' + a[h+1])
h = 0
m = 0

if __name__ == "__main__":
    h = int(input())
    m = int(input())
    process()
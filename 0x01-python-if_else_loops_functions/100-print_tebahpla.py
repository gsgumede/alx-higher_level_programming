#!/usr/bin/python3
n = 1
for c in range(122, 96, -1):
    if n % 2 == 0:
        c = c - 32
    print("{:s}".format(chr(c)), end="")
    n += 1

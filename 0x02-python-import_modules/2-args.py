#!/usr/bin/python3
import sys


n = len(sys.argv)
if n > 1:
    print("{:d} arguments:".format(n - 1))
    for index in range(1,n):
        print("{:d}: {:s}".format(index, sys.argv[index]))
else:
    print("{:d} argument.".format(n))

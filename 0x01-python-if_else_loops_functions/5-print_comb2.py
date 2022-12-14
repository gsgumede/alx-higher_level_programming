#!/usr/bin/python3
for index in range(0, 100):
    if index != 99:
        print("{:02d}, ".format(index), end="")
    else:
        print("{:02d}".format(index))

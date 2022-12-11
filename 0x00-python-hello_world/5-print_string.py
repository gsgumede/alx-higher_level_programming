#!/usr/bin/python3
str = "Holberton School"
for index in range(3):
    print("{:s}".format(str), end="")
print()
slice_str = str[:9]
print("{:s}".format(slice_str))

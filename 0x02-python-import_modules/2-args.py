#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    if n > 2:
        print("{:d} arguments:".format(n - 1))
        for index in range(1, n):
            print("{:d}: {:s}".format(index, sys.argv[index]))
    elif n == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(n - 1, sys.argv[1]))
    else:
        print("{:d} arguments.".format(0))


if __name__ == "__main__":
    main()

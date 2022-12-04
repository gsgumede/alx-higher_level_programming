#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    total = 0
    for index in range(1, n):
        total += int(sys.argv[index])
    print("{:d}".format(total))


if __name__ == "__main__":
    main()

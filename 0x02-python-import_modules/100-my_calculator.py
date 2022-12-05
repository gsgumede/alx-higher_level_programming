#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    ops = {"+": add,
           "-": sub,
           "*": mul,
           "/": div}
    n = len(sys.argv) - 1
    if n == 3:
        op = sys.argv[2]
        if op == "+" or op == "-" or op == "*" or op == "/":
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, ops[op](a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")


if __name__ == "__main__":
    main()

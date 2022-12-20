#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    while (1):
        try:
            for index in range(x):
                print("{:d}".format(my_list[index]), end="")
        except Exception as err:
            break
        print("")
        return x

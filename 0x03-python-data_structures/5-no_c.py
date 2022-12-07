#!/usr/bin/python3


def no_c(my_string):
    if my_string:
        my_string = list(my_string)
        n = len(my_string)
        for index in range(n):
            if my_string[index] == "c" or my_string[index] == "C":
                my_string[index] = " "
        my_string = "".join(my_string)
        return my_string

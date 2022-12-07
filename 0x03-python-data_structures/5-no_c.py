#!/usr/bin/python3


def no_c(my_string):
    new_string = my_string[:]
    new_string = list(new_string)
    for index in range(len(new_string)):
        if new_string[index] == "c" or new_string[index] == "C":
            new_string[index] = " "
    new_string = "".join(new_string)
    return new_string

#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        resul = a / b
    except (TypeError, ZeroDivisionError):
        resul = None
    finally:
        print("Inside Result: {}".format(resul))
    return (resul)

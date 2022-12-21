#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    resul_list = []
    for index in range(list_length):
        try:
            resul = my_list_1[index] / my_list_2[index]
        except TypeError:
            resul = 0
            print("wrong type")
        except ZeroDivisionError:
            resul = 0
            print("division by 0")
        except IndexError:
            resul = 0
            print("out of range")
        finally:
            resul_list.append(resul)
    return (resul_list)

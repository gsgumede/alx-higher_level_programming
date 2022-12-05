#!/usr/bin/python3
import hidden_4


def main():
    listdir = dir(hidden_4)
    lendir = len(listdir)
    for index in range(lendir):
        if listdir[index][0] != '_':
            print(listdir[index])


if __name__ == "__main__":
    main()

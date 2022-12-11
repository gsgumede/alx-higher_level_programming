#!/usr/bin/python3
import sys
str = "and that piece of art is useful - Dora Korpar, 2015-10-19"
for letter in str:
    sys.stderr.write(letter)
sys.stderr.write('\n')
exit(1)

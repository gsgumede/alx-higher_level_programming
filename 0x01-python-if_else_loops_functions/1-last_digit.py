#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
temp_number = number
if number < 0:
    temp_number *= -1
    last_digit = temp_number % 10
    last_digit *= -1
else:
    last_digit = temp_number % 10
if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit))
elif last_digit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))

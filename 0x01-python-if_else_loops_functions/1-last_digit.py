#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last = number % 10
else:
    last = number % -10

if last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5\n".format(number, last))
elif last < 6 and last != 0:
    print("Last digit of {:d} is {:d} and is less thn 6 and not 0\n".format(number, last))
else:
    print("Last digit of {:d} is {:d} and is 0\n".format(number, last))    
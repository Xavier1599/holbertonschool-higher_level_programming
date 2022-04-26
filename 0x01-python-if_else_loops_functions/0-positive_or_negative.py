#!/usr/bin/python3
import random
from traceback import print_tb
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive\n".format(number))
elif number < 0:
    print("{:d} is negative\n".format(number))
else:
    print("{:d} is negative\n".format(number))
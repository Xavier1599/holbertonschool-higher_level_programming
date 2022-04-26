#!/usr/bin/python3
import random
from traceback import print_tb
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive\n".format(number))
elif number < 0:
    print("{} is negative\n".format(number))
else:
    print("{} is zero\n".format(number))

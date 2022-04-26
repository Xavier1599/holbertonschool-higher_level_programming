#!/usr/bin/python3
def uppercase(str):
    text = " "
    for i in (str):
        char = ord(i)
        if char >= ord('a') and char <= ord('z'):
            char = char - 32
            text = chr(char)
        else:
            text = i
        print("{:s}".format(text), end="")
    print("")

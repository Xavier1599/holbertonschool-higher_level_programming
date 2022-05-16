#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    lenght = 0
    cnt = 0
    for i in my_list:
        lenght += 1
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
        except IndexError:
            print("")
            return lenght
        cnt += 1
    print("")
    return cnt

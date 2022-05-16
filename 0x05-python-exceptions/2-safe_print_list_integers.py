#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    lenght = 0
    cnt = 0
    for i in my_list:
        lenght += 1
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            cnt += 1
        except (ValueError, TypeError):
            continue
        print("")
        return cnt

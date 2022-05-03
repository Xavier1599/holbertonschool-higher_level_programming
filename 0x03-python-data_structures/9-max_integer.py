#!/usr/bin/python
def max_integer(my_list=[]):
    cnt = len(my_list)
    if cnt == 0:
        return None
    v_max = my_list[0]
    for i in my_list:
        if i > v_max:
            v_max = i
    return v_max

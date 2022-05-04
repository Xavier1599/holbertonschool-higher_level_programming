#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lst = my_list[:]
    for i in range(len(new_lst)):
        if new_lst[i] == search:
            new_lst[i] = replace
    return (new_lst)

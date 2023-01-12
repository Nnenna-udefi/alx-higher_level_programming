#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = set(my_list)
    res = 0
    for i in unique:
        res += i
    return res

#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        biggest_int = my_list[0]
        for i in my_list:
                if i > biggest_int:
                    biggest_int = i
        return biggest_int

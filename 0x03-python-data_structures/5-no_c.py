#!/usr/bin/python3

def no_c(my_string):
    result = ""
    for cha in my_string:
        if cha != 'c' and cha != 'C':
            result += cha
        return result

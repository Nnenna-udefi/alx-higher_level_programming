#!/usr/bin/python3

def no_c(my_string):
    result = my_string.translate({ord(i): None for i in 'cC'})
    return result

#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    for tup in my_list:
        numerator += tup[0] * tup[1]
        denominator += tup[1]
        average = float(numerator / denominator)
    return average

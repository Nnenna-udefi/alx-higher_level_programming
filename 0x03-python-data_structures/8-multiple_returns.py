#!/usr/bin/python3

def multiple_returns(sentence):
    first = sentence[0]
    if len(sentence) == 0:
        first = None
    else:
        return (len(sentence), first)

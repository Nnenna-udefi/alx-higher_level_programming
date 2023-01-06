#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{:d} argument.".format(n))
    elif n == 1:
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))
    for i in range(n):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))

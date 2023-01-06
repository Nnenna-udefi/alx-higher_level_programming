#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{:d}".format(n))
    else:
        total = 0
        for i in range(n):
            total += int(sys.argv[i + 1])
        print("{}".format(total))

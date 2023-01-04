#!/usr/bin/python3

s = ''
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
         s = chr(i) + s
    else:
        s = chr(i - 32) + s
print(s, end='')

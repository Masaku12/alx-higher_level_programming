#!/usr/bin/python3
# Print numbers from 0 to 100
for num in range(0, 100):
    if num != 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num))

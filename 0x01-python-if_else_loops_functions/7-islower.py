#!/usr/bin/python3
# function that checks for lowercase character
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    elif ord(c) > 64 and ord(c) < 91:
        return False

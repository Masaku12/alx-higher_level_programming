#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # print(dict(sorted(a_dictionary.items())))
    for i in sorted(a_dictionary.items()):
        print("{}: {}".format(i[0], i[1]))

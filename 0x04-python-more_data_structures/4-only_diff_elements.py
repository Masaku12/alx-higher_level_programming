#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []

    for i in sorted(list(set_1)):
        if i not in sorted(list(set_2)):
            diff.append(i)

    for j in sorted(list(set_2)):
        if j not in sorted(list(set_1)):
            diff.append(j)

    return set(diff)

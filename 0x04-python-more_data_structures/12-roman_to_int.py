#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    skip = False

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    for i in range(len(roman_string)):
        if skip:
            skip = False
            continue

        current = roman.get(roman_string[i])

        if i + 1 < len(roman_string):
            next = roman.get(roman_string[i + 1])

            if current < next:
                sum += next - current
                skip = True
            else:
                sum += current
        else:
            sum += current

    return sum

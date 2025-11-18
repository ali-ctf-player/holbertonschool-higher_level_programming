#!/usr/bin/python3

def roman_to_int(roman_number):
    prev_value = 0
    total_value = 0
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if not isinstance(roman_number, str) or roman_number is None:
        return 0
    else:
        for i in reversed(roman_number):
            current_value = roman_values[i]
            if current_value < prev_value:
                total_value -= current_value
            else:
                total_value += current_value
            prev_value = current_value
    return total_value

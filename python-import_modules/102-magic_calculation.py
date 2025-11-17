#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)


if __name__ == "__main__":
    result1 = magic_calculation(2, 5)
    print(f"magic_calculation(2, 5) = {result1}")
    # Test case 2: a >= b
    result2 = magic_calculation(8, 3)
    print(f"magic_calculation(8, 3) = {result2}")
    # Test case 3: a == b
    result3 = magic_calculation(4, 4)
    print(f"magic_calculation(4, 4) = {result3}")

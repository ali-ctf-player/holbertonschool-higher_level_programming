#!/usr/bin/python3

import sys


def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)


if __name__ == "__main__":
    if (len(sys.argv)) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if not (sys.argv[2] in ("+", "-", "*", "/")):
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            if sys.argv[2] == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            if sys.argv[2] == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            if sys.argv[2] == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            if sys.argv[2] == "/":
                print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

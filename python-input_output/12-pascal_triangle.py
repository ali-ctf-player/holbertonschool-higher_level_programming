#!/usr/bin/python3
"""It is doc string"""


def pascal_triangle(n):
    """It is doc string"""
    results = []
    if n <= 0:
        return []
    else:
        for i in range(n):
            result = []
            for x in range(i + 1):
                if x == 0 or x == i:
                    result.append(1)
                else:
                    value = results[i - 1][x] + results[i - 1][x - 1]
                    result.append(value)
            results.append(result)

    return results

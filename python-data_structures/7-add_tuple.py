#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        a1 = tuple_a[0]
    else:
        a1 = 0
    if len(tuple_a) >= 2:
        a2 = tuple_a[1]
    else:
        a2 = 0
    if len(tuple_b) >= 1:
        b1 = tuple_b[0]
    else:
        b1 = 0
    if len(tuple_b) >= 2:
        b2 = tuple_b[1]
    else:
        b2 = 0
    return (a1 + b1, a2 + b2)


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

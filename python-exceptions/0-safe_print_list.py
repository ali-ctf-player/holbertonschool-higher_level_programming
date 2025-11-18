#!/usr/bin/python3

def safe_print_list(mylist, x=0):
    count = 0
    try:
        for i in range(x):
            print(mylist[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

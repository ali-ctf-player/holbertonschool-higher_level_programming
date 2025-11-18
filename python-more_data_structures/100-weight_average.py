#!/usr/bin/python3

def weight_average(my_list):
    if not my_list:
        return 0
    else:
        prime = 0
        counter = 0
        for mytuple_ in my_list:
            temp = 1
            for val in mytuple_:
                temp *= val
            prime += temp
            counter += mytuple_[1]
        return prime / counter

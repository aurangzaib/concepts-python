import functools as ft


def reducer(i1, i2):
    print(i1, i2)
    return i1 + i2


input_array = [x for x in range(1, 10)]
output1 = ft.reduce(reducer, input_array)
output2 = ft.reduce(lambda x, y: x + y, input_array)
output2 = ft.reduce
pass

import numpy as np


def even_number(input, output=[]):
    for element in input:
        output.append(element) if (element % 2 == 0) else None
    return output


def even_number2(input):
    if input % 2 == 0: return input


list1 = [x for x in range(0, 10)]
list2 = even_number(list1)
list3 = list(filter(lambda x: x % 2 == 0, list1))
list4 = list(filter(even_number2, list1))

pass

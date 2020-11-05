from functools import reduce

def my_func(perv_el, el):
    return perv_el * el

print([el for el in range(99, 1001) if el % 2 == 0])
print(reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0]))
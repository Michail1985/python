from itertools import count, cycle

for el in count(int(input('Введите стартовое число: '))):
    if el > 10:
        break
    print(el)

my_list = ['asd', 4, True, 234]
counts = 1
for el_p in cycle(my_list):
    if counts > 10:
        break
    counts += 1
    print(el_p)
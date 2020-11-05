def fact():
    generator = (el for el in range(1, int(input('Введите целое число: '))+1))
    el_p = 1
    for el in generator:
        el_p = el_p * el
    print(el_p)
fact()
def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        arg = y * -1
        cisl = x
        for i in range(arg -1):
            cisl = cisl * x
        return 1 / cisl
    except TypeError:
        return 'Введено не число'
print(my_func(5, -3))
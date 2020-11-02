def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        answer = x ** y
    except TypeError:
        return 'Введено не число'
    return answer
print(my_func(5, -3))